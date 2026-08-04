#!/usr/bin/env python3
"""
Regression fixtures for FICHA E5a (content_not_captured rejection branch) and
FICHA E5b (infer_actor_level vs pipeline_vocabulary.yaml assignment_rule).
Invoke directly: python3 test_e5_fixtures.py
Not wired into CI — that is a separate, un-taken decision.
"""

import json
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import bulk_extract as be

FIXTURE_SKELETON = json.loads('''
{
  "extraction_id": "ER-SP-fixture-001-SNP-001",
  "source_packet_id": "SP-fixture-001",
  "source_id": "SRC-fixture-001",
  "source_type": "database_profile",
  "source_title": "marmalead.com",
  "source_ref": "https://marmalead.com/",
  "source_date_if_available": "Accessed April 2026; page undated",
  "author_or_actor_if_available": null,
  "snippet_primary": "n/a \\u2014 content recovered via research subagent's direct fetch of marmalead.com homepage; verbatim character-for-character accuracy cannot be independently confirmed.",
  "snippet_context_before": null,
  "snippet_context_after": null,
  "traceability_pointer": {"pointer_type": "url", "pointer_value": "https://marmalead.com/", "secondary_pointer": null},
  "claim_type": null, "subject_exact": null, "actor_level": null, "platforms": [],
  "product_type_if_explicit": null, "metric_type": null, "metric_value_raw": null,
  "metric_unit": null, "time_scope_raw": null, "time_scope_normalized_if_safe": null,
  "geography_if_explicit": null, "evidence_role": null, "local_qualifiers": [],
  "uncertainties": [], "parser_notes": [], "_extraction_stage": 1,
  "_source_snippet_id": "SNP-001", "_source_finding_ids": null
}
''')


def test_e5a_recovery_note_rejects():
    with tempfile.TemporaryDirectory() as tmp:
        be.REJECTED_ARCHIVE_DIR = Path(tmp) / 'rejected_archive_phase1b'
        try:
            be.process_skeleton(FIXTURE_SKELETON)
        except be.SkeletonRejected as rej:
            assert rej.recovery_class == 'content_not_captured'
            assert rej.issue_type == 'required_field_unfillable'
            out = be.stage_rejected_skeleton(FIXTURE_SKELETON, rej, staged_at='2026-04-21T03:00:00Z')
            packet = json.loads(out.read_text())
            assert packet['recovery_class'] == 'content_not_captured'
            assert packet['skeleton_original']['extraction_id'] == FIXTURE_SKELETON['extraction_id']
            print('PASS test_e5a_recovery_note_rejects')
        else:
            raise AssertionError('process_skeleton did not reject a recovery-note skeleton')


def test_e5a_normal_skeleton_still_produces_record():
    normal = dict(FIXTURE_SKELETON)
    normal['snippet_primary'] = 'Etsy charges a 6.5% transaction fee on the total sale price.'
    record = be.process_skeleton(normal)
    assert record['snippet_primary'] == normal['snippet_primary']
    print('PASS test_e5a_normal_skeleton_still_produces_record')


def test_e5b_help_center_maps_to_platform():
    result = be.infer_actor_level(
        'help_center',
        'Payments are issued automatically within 3 business days of shipment confirmation.',
    )
    assert result == 'platform', result
    print('PASS test_e5b_help_center_maps_to_platform')


def test_e5b_help_center_ignores_buyer_vocabulary():
    result = be.infer_actor_level(
        'help_center',
        'If a buyer requests a refund, the platform processes it automatically.',
    )
    assert result == 'platform', result
    print('PASS test_e5b_help_center_ignores_buyer_vocabulary')


if __name__ == '__main__':
    test_e5a_recovery_note_rejects()
    test_e5a_normal_skeleton_still_produces_record()
    test_e5b_help_center_maps_to_platform()
    test_e5b_help_center_ignores_buyer_vocabulary()
    print('All fixtures passed.')
