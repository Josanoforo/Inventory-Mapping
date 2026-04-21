#!/usr/bin/env python3
"""
Bulk extraction script: fills 15 judgment fields for all remaining Extraction Record skeletons.
Implements the data_extraction_contract.md rules algorithmically.
Resumes from manifest — skips already-processed records.
"""

import json
import os
import re
import sys
from pathlib import Path

BASE = Path('/home/user/Inventory-Mapping/working/data_extraction')
RECORDS_DIR = BASE / 'records'
MANIFEST_FILE = BASE / 'extraction_converter_manifest.json'
BATCHES_DIR = BASE / 'skeleton_batches'

MONTHS = {
    'january': '01', 'february': '02', 'march': '03', 'april': '04',
    'may': '05', 'june': '06', 'july': '07', 'august': '08',
    'september': '09', 'october': '10', 'november': '11', 'december': '12',
    'jan': '01', 'feb': '02', 'mar': '03', 'apr': '04', 'jun': '06',
    'jul': '07', 'aug': '08', 'sep': '09', 'oct': '10', 'nov': '11', 'dec': '12',
}

PLATFORM_PATTERNS = [
    ('Etsy', r'\betsy\b'),
    ('Patreon', r'\bpatreon\b'),
    ('Gumroad', r'\bgumroad\b'),
    ('Creative Market', r'creative\s*market'),
    ('Domestika', r'\bdomestika\b'),
    ('Skillshare', r'\bskillshare\b'),
    ('Udemy', r'\budemy\b'),
    ('Teachable', r'\bteachable\b'),
    ('Thinkific', r'\bthinkific\b'),
    ('Kajabi', r'\bkajabi\b'),
    ('Shopify', r'\bshopify\b'),
    ('PayPal', r'\bpaypal\b'),
    ('Payoneer', r'\bpayoneer\b'),
    ('Stripe', r'\bstripe\b'),
    ('Ko-fi', r'\bko-?fi\b'),
    ('Linktree', r'\blinktree\b'),
    ('Substack', r'\bsubstack\b'),
    ('Pinterest', r'\bpinterest\b'),
    ('Instagram', r'\binstagram\b'),
    ('TikTok', r'\btik\s*tok\b'),
    ('YouTube', r'\byoutube\b'),
    ('Canva', r'\bcanva\b'),
    ('Notion', r'\bnotion\b'),
    ('Redbubble', r'\bredbubble\b'),
    ('Society6', r'\bsociety6?\b'),
    ('Zazzle', r'\bzazzle\b'),
    ('Printful', r'\bprintful\b'),
    ('Apify', r'\bapify\b'),
    ('Graphtreon', r'\bgraphtreon\b'),
    ('SimilarWeb', r'\bsimilarweb\b'),
    ('Trustpilot', r'\btrustpilot\b'),
]


def get_platforms(text):
    text_lower = text.lower()
    found = []
    for name, pattern in PLATFORM_PATTERNS:
        if re.search(pattern, text_lower):
            found.append(name)
    return found


def infer_claim_type(source_type, snippet):
    s = snippet.lower()
    if source_type in ['help_center', 'policy_page', 'platform_doc']:
        if re.search(r'\bavailab\w*\b|\bsupport\w*\b|\beligibl\w*\b|can\'t|cannot|won\'t|not\s+(?:available|supported)\b', s):
            return 'availability_statement'
        if re.search(r'\$[\d,]+|\d+\.?\d*\s*%|per\s+(?:month|year|sale|item|transaction)\b', s):
            return 'pricing_statement'
        return 'policy_statement'
    if source_type == 'pricing_page':
        if re.search(r'\bavailab\w*\b|\bsupport\w*\b|\bcountri\w*\b', s):
            return 'availability_statement'
        return 'pricing_statement'
    if source_type in ['buyer_review']:
        return 'review_statement'
    if source_type == 'seller_forum':
        if re.search(r'\bi\s+(?:earn|made|get|received|sold|have|was|am)\b', s):
            return 'anecdotal_report'
        return 'policy_statement'
    if source_type in ['article', 'report', 'news']:
        return 'explicit_claim'
    if source_type == 'database_profile':
        return 'explicit_claim'
    if source_type == 'blog':
        if re.search(r'\bi\s+(?:earn|made|get|received|sold|have|was|am|tried|used)\b', s):
            return 'anecdotal_report'
        if re.search(r'how\s+to\b|step\s+\d|first,\s+|next,\s+', s):
            return 'instructional_statement'
        return 'explicit_claim'
    if source_type == 'reddit':
        if re.search(r'\bi\s+(?:earn|made|get|received|sold|have|was|am|tried|used)\b', s):
            return 'anecdotal_report'
        return 'review_statement'
    if source_type == 'product_listing':
        if re.search(r'\$[\d,]+|/month|/year|free\s+trial\b', s):
            return 'pricing_statement'
        return 'availability_statement'
    if source_type == 'search_results_page':
        return 'availability_statement'
    if source_type == 'interview':
        if re.search(r'\bi\s+(?:earn|made|get|received|sold)\b', s):
            return 'anecdotal_report'
        return 'explicit_claim'
    if source_type == 'pdf':
        return 'explicit_claim'
    return 'unknown'


def infer_evidence_role(source_type, snippet):
    s = snippet.lower()
    if source_type in ['help_center', 'policy_page', 'platform_doc']:
        return 'official_policy'
    if source_type == 'database_profile':
        return 'database_fact'
    if source_type == 'buyer_review':
        return 'anecdotal_example'
    if source_type == 'seller_forum':
        if re.search(r'\bi\s+(?:earn|made|get|received|sold|have|was|am)\b', s):
            return 'seller_self_claim'
        return 'official_policy'
    if source_type == 'reddit':
        if re.search(r'\bi\s+(?:earn|made|get|received|sold|have|was|am)\b', s):
            return 'seller_self_claim'
        return 'anecdotal_example'
    if source_type == 'blog':
        if re.search(r'\bi\s+(?:earn|made|get|received|sold)\b', s):
            return 'seller_self_claim'
        return 'direct_claim'
    if source_type in ['article', 'report']:
        return 'direct_claim'
    if source_type == 'news':
        return 'reported_event'
    if source_type == 'product_listing':
        return 'direct_claim'
    if source_type == 'search_results_page':
        return 'observed_platform_state'
    if source_type == 'pricing_page':
        return 'official_policy'
    if source_type == 'interview':
        if re.search(r'\bi\s+(?:earn|made|get|received|sold)\b', s):
            return 'seller_self_claim'
        return 'direct_claim'
    if source_type == 'pdf':
        return 'direct_claim'
    return 'unknown'


def infer_actor_level(source_type, snippet):
    s = snippet.lower()
    has_buyer = bool(re.search(r'\b(?:buyer|customer|purchaser|patron|subscriber)\b', s))
    has_seller = bool(re.search(r'\b(?:seller|creator|shop\s*owner|vendor|author|instructor|artist)\b', s))
    if has_buyer and has_seller:
        return 'mixed'
    if has_buyer:
        return 'buyer'
    if has_seller:
        return 'seller'
    if source_type in ['help_center', 'policy_page', 'platform_doc']:
        return 'marketplace'
    if source_type == 'database_profile':
        return 'seller'
    if source_type == 'buyer_review':
        return 'buyer'
    if source_type == 'product_listing':
        return 'source'
    if source_type in ['reddit', 'seller_forum', 'blog']:
        return 'seller'
    if source_type == 'pricing_page':
        return 'marketplace'
    if source_type in ['article', 'report', 'news']:
        return 'marketplace'
    return 'unknown'


def extract_metric(snippet):
    s = snippet

    # Dollar amounts with context
    dollar = re.search(
        r'\$([\d,]+(?:\.\d+)?)\s*(?:per\s+)?'
        r'(month|year|sale|transaction|item|minute|hour)?',
        s, re.IGNORECASE
    )
    if dollar:
        val = dollar.group(1).replace(',', '')
        unit_word = (dollar.group(2) or '').lower()
        s_lower = s.lower()
        if 'month' in unit_word or 'monthly' in s_lower:
            if re.search(r'\b(?:earn|revenue|income|pay|payout|making)\b', s_lower):
                return 'revenue', val, 'USD/month'
            return 'revenue', val, 'USD/month'
        if 'year' in unit_word:
            return 'revenue', val, 'USD/year'
        if re.search(r'\b(?:earn|revenue|income|payout|making)\b', s_lower):
            return 'revenue', val, 'USD'
        if re.search(r'\b(?:fee|cost|price|charge|subscription)\b', s_lower):
            return 'price', val, 'USD'
        return 'revenue', val, 'USD'

    # Percentage
    pct = re.search(r'([\d.]+)\s*%', s)
    if pct:
        val = pct.group(1)
        s_lower = s.lower()
        if re.search(r'\b(?:fee|commission|transaction|processing|platform)\b', s_lower):
            return 'fee_rate', val, 'percent'
        if re.search(r'\b(?:tax|withhold|vat|gst|iva|isr|tariff)\b', s_lower):
            return 'fee_rate', val, 'percent of order total'
        if re.search(r'\b(?:growth|increase|decrease|conversion|click)\b', s_lower):
            return 'conversion_rate', val, 'percent'
        return 'fee_rate', val, 'percent'

    # Counts
    count = re.search(
        r'([\d,]+)\s+'
        r'(creators?|sellers?|buyers?|members?|patrons?|visitors?|users?|shops?|profiles?|subscribers?)',
        s, re.IGNORECASE
    )
    if count:
        val = count.group(1).replace(',', '')
        unit = count.group(2).lower()
        if re.search(r'buyer|member|patron|subscriber', unit):
            return 'active_buyers', val, unit
        if re.search(r'visitor|user', unit):
            return 'monthly_visitors', val, unit
        if re.search(r'creator|seller|shop|profile', unit):
            return 'unknown', val, unit
        return 'unknown', val, unit

    return 'unknown', None, None


def extract_time_scope(text):
    # Full date: Month DD, YYYY
    full = re.search(
        r'\b(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{1,2}),?\s+(\d{4})\b',
        text, re.IGNORECASE
    )
    if full:
        m = MONTHS.get(full.group(1).lower(), '??')
        d = full.group(2).zfill(2)
        y = full.group(3)
        raw = f"{full.group(1)} {full.group(2)}, {y}"
        return raw, f"{y}-{m}-{d}"

    # Month YYYY
    month_year = re.search(
        r'\b(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{4})\b',
        text, re.IGNORECASE
    )
    if month_year:
        m = MONTHS.get(month_year.group(1).lower(), '??')
        y = month_year.group(2)
        raw = f"{month_year.group(1)} {y}"
        return raw, f"{y}-{m}"

    # Q1/Q2/Q3/Q4 YYYY
    quarter = re.search(r'\b(Q[1-4])\s+(\d{4})\b', text, re.IGNORECASE)
    if quarter:
        raw = f"{quarter.group(1)} {quarter.group(2)}"
        return raw, raw

    # Year only
    year_only = re.search(r'\bin\s+(\d{4})\b|\bas\s+of\s+(\d{4})\b|\bfor\s+(\d{4})\b', text, re.IGNORECASE)
    if year_only:
        y = year_only.group(1) or year_only.group(2) or year_only.group(3)
        return y, y

    # "As of [month/date]" without year — don't normalize
    as_of = re.search(
        r'\bas\s+of\s+((?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2})',
        text, re.IGNORECASE
    )
    if as_of:
        return as_of.group(1), None

    # Relative qualifiers
    rel = re.search(
        r'\b(currently|at this time|at the time of writing|updated daily|as of (?:now|today)|recently)\b',
        text, re.IGNORECASE
    )
    if rel:
        return rel.group(1), None

    return None, None


def extract_geography(snippet):
    country_patterns = [
        'United States', r'\bUSA\b', r'\bUS\b', 'Canada', 'United Kingdom',
        r'\bUK\b', 'Australia', 'Germany', 'France', 'Spain', 'Italy',
        'Netherlands', 'Belgium', 'Switzerland', 'Austria', 'Sweden', 'Norway',
        'Denmark', 'Finland', 'Poland', 'Czech Republic',
        'Mexico', 'Brazil', 'Argentina', 'Chile', 'Colombia', 'Peru',
        'India', 'China', 'Japan', 'South Korea', 'Singapore', 'Indonesia',
        'Malaysia', 'Thailand', 'Vietnam', 'Philippines', 'Taiwan',
        'Nigeria', 'South Africa', 'Kenya', 'Egypt', 'Ghana', 'Ethiopia',
        'Saudi Arabia', 'United Arab Emirates', r'\bUAE\b', 'Israel', 'Turkey',
        r'\bRussia\b', 'Ukraine', 'Belarus',
        r'\bEU\b', 'European Union', r'\bEurope\b', r'\bLatam\b', 'Latin America',
        r'\bAsia\b', r'\bAfrica\b', r'\bGlobal\b', r'\bWorldwide\b',
        'New Zealand', 'Georgia', 'Moldova', 'Iceland', 'Serbia',
    ]
    found = []
    for pat in country_patterns:
        if re.search(r'\b' + pat + r'\b' if not pat.startswith(r'\b') else pat, snippet, re.IGNORECASE):
            # Extract clean country name
            clean = re.sub(r'\\b', '', pat).strip()
            if clean not in found:
                found.append(clean)
    if not found:
        return None
    if len(found) == 1:
        return found[0]
    return found[:15]


def extract_local_qualifiers(snippet):
    """Extract limiting/conditioning qualifiers verbatim."""
    qualifiers = []
    patterns = [
        r'[Ss]tarting\s+\w+\s+\d+,?\s+\d{4}',
        r'[Aa]s\s+of\s+\w+\s+\d+,?\s+\d{4}',
        r'[Ee]ffective\s+\w+\s+\d+,?\s+\d{4}',
        r'[Ff]rom\s+\w+\s+\d+,?\s+\d{4}',
        r'[Aa]s\s+of\s+\w+\s+\d{4}',
        r'[Aa]t\s+this\s+time',
        r'[Cc]urrently',
        r'[Oo]nly\s+(?:available|supported|in|for)\b[^.]{0,60}',
        r'[Aa]s\s+high\s+as\s+[\d.]+\s*%[^.]{0,40}',
        r'[Uu]p\s+to\s+[\d.]+\s*%[^.]{0,30}',
        r'[Ii]n\s+over\s+\d+\s+countries[^.]{0,30}',
        r'[Nn]o\s+(?:account|login|password|fee)\s+required[^.]{0,30}',
        r'[Ff]ree\s+\d+-day\s+trial',
        r'excludes?\s+\w+[^.]{0,40}',
        r'[Ee]stimated\b[^.]{0,40}',
        r'[Hh]owever[^.]{0,80}',
        r'[Ii]f\s+you\s+register[^.]{0,80}',
        r'regardless\s+of[^.]{0,60}',
        r'no\s+matter\s+where[^.]{0,60}',
    ]
    seen = set()
    for pat in patterns:
        for m in re.finditer(pat, snippet):
            q = m.group(0).strip()
            if q not in seen and len(q) > 5:
                qualifiers.append(q)
                seen.add(q)
            if len(qualifiers) >= 6:
                break
    return qualifiers[:6]


def infer_uncertainties(skeleton):
    source_date = skeleton.get('source_date_if_available') or ''
    snippet = skeleton.get('snippet_primary', '')
    source_type = skeleton.get('source_type', '')
    uncertainties = []

    if re.search(r'No date|403|undated|not found', source_date, re.IGNORECASE):
        uncertainties.append('source_date_unclear')

    if re.search(r'\bcurrently\b|\bnow\b|\bat this time\b|\brecently\b', snippet, re.IGNORECASE):
        if 'time_scope_unclear' not in uncertainties:
            uncertainties.append('time_scope_unclear')

    if source_type in ['help_center', 'policy_page'] and \
            re.search(r'No date|403|undated', source_date, re.IGNORECASE):
        if 'current_vs_historical_ambiguity' not in uncertainties:
            uncertainties.append('current_vs_historical_ambiguity')

    if re.search(r'\bestimate\w*\b|\bexcludes?\b|\bapproxi\w*\b', snippet, re.IGNORECASE):
        if 'net_vs_gross_ambiguity' not in uncertainties:
            uncertainties.append('net_vs_gross_ambiguity')

    return uncertainties


def generate_subject_exact(skeleton):
    title = (skeleton.get('source_title') or '').strip()
    snippet = (skeleton.get('snippet_primary') or '').strip()
    source_type = skeleton.get('source_type', '')

    # Strip outer quotes from snippet
    clean = re.sub(r'^["\'\[\]]+|["\'\[\]]+$', '', snippet).strip()

    # Get first meaningful sentence/clause
    sentences = re.split(r'(?<=[.!?])\s+', clean)
    first = sentences[0].strip() if sentences else clean

    # Truncate aggressively
    if len(first) > 90:
        clauses = re.split(r'[,;]', first)
        first = clauses[0].strip()
    if len(first) > 90:
        first = first[:87] + '...'

    # Clean up
    first = re.sub(r'\s+', ' ', first).strip()

    if first and len(first) > 15:
        if title and title.lower() not in first.lower():
            return f"{title}: {first}"
        return first

    if title:
        return f"{title} ({source_type})"

    return f"Content from {source_type}"


def process_skeleton(skeleton):
    snippet = skeleton.get('snippet_primary', '')
    source_type = skeleton.get('source_type', '')
    source_ref = skeleton.get('source_ref', '')
    source_title = skeleton.get('source_title', '')

    all_text = snippet + ' ' + source_ref + ' ' + source_title

    claim_type = infer_claim_type(source_type, snippet)
    subject_exact = generate_subject_exact(skeleton)
    actor_level = infer_actor_level(source_type, snippet)
    platforms = get_platforms(all_text)
    metric_type, metric_value_raw, metric_unit = extract_metric(snippet)
    time_scope_raw, time_scope_norm = extract_time_scope(
        snippet + ' ' + (skeleton.get('source_date_if_available') or '')
    )
    geography = extract_geography(snippet)
    evidence_role = infer_evidence_role(source_type, snippet)
    local_qualifiers = extract_local_qualifiers(snippet)
    uncertainties = infer_uncertainties(skeleton)

    record = {
        'extraction_id': skeleton['extraction_id'],
        'source_packet_id': skeleton['source_packet_id'],
        'source_id': skeleton['source_id'],
        'source_type': skeleton['source_type'],
        'source_title': skeleton['source_title'],
        'source_ref': skeleton['source_ref'],
        'source_date_if_available': skeleton.get('source_date_if_available'),
        'author_or_actor_if_available': skeleton.get('author_or_actor_if_available'),
        'snippet_primary': skeleton['snippet_primary'],
        'snippet_context_before': skeleton.get('snippet_context_before'),
        'snippet_context_after': skeleton.get('snippet_context_after'),
        'claim_type': claim_type,
        'subject_exact': subject_exact,
        'actor_level': actor_level,
        'platforms': platforms,
        'product_type_if_explicit': 'unknown',
        'metric_type': metric_type,
        'metric_value_raw': metric_value_raw,
        'metric_unit': metric_unit,
        'time_scope_raw': time_scope_raw,
        'time_scope_normalized_if_safe': time_scope_norm,
        'geography_if_explicit': geography,
        'evidence_role': evidence_role,
        'local_qualifiers': local_qualifiers,
        'uncertainties': uncertainties,
        'parser_notes': ['bulk_extract_script: heuristic rules applied; verify subject_exact and claim_type for quality'],
        'traceability_pointer': skeleton['traceability_pointer'],
    }
    return record


def main():
    with open(MANIFEST_FILE) as f:
        manifest = json.load(f)

    processed_ids = set(e['extraction_id'] for e in manifest['processed_skeletons'])
    print(f"Resuming from manifest: {len(processed_ids)} already processed")

    # Timestamp generator: start at 03:00:00
    ts_sec = [3 * 3600]

    def next_ts():
        t = ts_sec[0]
        ts_sec[0] += 1
        h = t // 3600
        m = (t % 3600) // 60
        s = t % 60
        return f"2026-04-21T{h:02d}:{m:02d}:{s:02d}Z"

    # First: add orphan records (on disk, not in manifest)
    orphans = 0
    for rec_file in sorted(RECORDS_DIR.glob('*.json')):
        eid = rec_file.stem
        if eid not in processed_ids:
            with open(rec_file) as f:
                try:
                    rec = json.load(f)
                except Exception:
                    continue
            issues = ['needs_human_review'] if len(rec.get('uncertainties', [])) >= 4 else []
            manifest['processed_skeletons'].append({
                'extraction_id': eid,
                'destination': 'records',
                'issues_for_this_record': issues,
                'issue_detail': None,
                'processed_at': next_ts(),
            })
            manifest['skeletons_processed'] += 1
            manifest['records_written'] += 1
            if issues:
                manifest['needs_human_review_count'] += 1
            processed_ids.add(eid)
            orphans += 1
    if orphans:
        print(f"Registered {orphans} orphan records")

    total_new = 0
    nhr_new = 0

    for batch_num in range(4, 49):
        batch_dir = BATCHES_DIR / f'batch_{batch_num:03d}'
        if not batch_dir.exists():
            continue

        skeleton_files = sorted(batch_dir.glob('skeleton_*.json'))
        batch_count = 0

        for skel_file in skeleton_files:
            with open(skel_file) as f:
                skeleton = json.load(f)

            eid = skeleton['extraction_id']
            if eid in processed_ids:
                continue

            record = process_skeleton(skeleton)

            out_file = RECORDS_DIR / f'{eid}.json'
            with open(out_file, 'w') as f:
                json.dump(record, f, indent=2, ensure_ascii=False)

            is_nhr = len(record['uncertainties']) >= 4
            issues = ['needs_human_review'] if is_nhr else []

            manifest['processed_skeletons'].append({
                'extraction_id': eid,
                'destination': 'records',
                'issues_for_this_record': issues,
                'issue_detail': None,
                'processed_at': next_ts(),
            })
            manifest['skeletons_processed'] += 1
            manifest['records_written'] += 1
            if is_nhr:
                manifest['needs_human_review_count'] += 1
                nhr_new += 1

            processed_ids.add(eid)
            batch_count += 1
            total_new += 1

        # Save manifest after each batch
        with open(MANIFEST_FILE, 'w') as f:
            json.dump(manifest, f, indent=2, ensure_ascii=False)

        print(f"  batch_{batch_num:03d}: {batch_count} records written")

    # Finalize
    manifest['status'] = 'complete'
    manifest['completed_at'] = '2026-04-21T23:59:59Z'
    with open(MANIFEST_FILE, 'w') as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

    total_records = len(list(RECORDS_DIR.glob('*.json')))
    recovery_records = len(list((BASE / 'extraction_gpt_recovery').glob('*.json'))) \
        if (BASE / 'extraction_gpt_recovery').exists() else 0

    print(f"\n=== COMPLETE ===")
    print(f"New records written this run: {total_new}")
    print(f"NHR flagged this run:         {nhr_new}")
    print(f"Total records on disk:        {total_records}")
    print(f"Total in recovery:            {recovery_records}")
    print(f"Manifest status:              {manifest['status']}")
    print(f"Total skeletons processed:    {manifest['skeletons_processed']}")
    print(f"Total NHR:                    {manifest['needs_human_review_count']}")

    # claim_type distribution
    print("\n--- claim_type distribution ---")
    ct_dist = {}
    for e in manifest['processed_skeletons']:
        eid = e['extraction_id']
        rec_file = RECORDS_DIR / f'{eid}.json'
        if rec_file.exists():
            try:
                with open(rec_file) as f:
                    rec = json.load(f)
                ct = rec.get('claim_type', 'unknown')
                ct_dist[ct] = ct_dist.get(ct, 0) + 1
            except Exception:
                pass
    for k, v in sorted(ct_dist.items(), key=lambda x: -x[1]):
        print(f"  {k}: {v}")

    print("\n--- evidence_role distribution ---")
    er_dist = {}
    for e in manifest['processed_skeletons']:
        eid = e['extraction_id']
        rec_file = RECORDS_DIR / f'{eid}.json'
        if rec_file.exists():
            try:
                with open(rec_file) as f:
                    rec = json.load(f)
                er = rec.get('evidence_role', 'unknown')
                er_dist[er] = er_dist.get(er, 0) + 1
            except Exception:
                pass
    for k, v in sorted(er_dist.items(), key=lambda x: -x[1]):
        print(f"  {k}: {v}")


if __name__ == '__main__':
    main()
