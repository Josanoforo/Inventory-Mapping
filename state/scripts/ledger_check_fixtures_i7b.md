# Pendientes — Ledger (FIXTURE I7b)

**Generado:** fixture sintético para la prueba de R-B del encargo E-S35-3. No es estado real.

**Sesión vigente:** S35

**Qué es.** Fixture mínimo que satisface I1-I6 y expone el caso (b) de R-B: una fila abierta
cuya última sesión con movimiento está a 3 o más sesiones de la vigente. Antes de I7 el gate
no dice nada sobre ella; después, I7b la REPORTA sin gatear (exit 0).

## A. Nunca verificados contra el repo actual — objetivo de Run 2

| ID | Enunciado | Clase | Pregunta verificable | Dónde | Estado |
|---|---|---|---|---|---|
| P-911 | Fila abierta a 4 sesiones de la vigente | hecho | ¿Cuántas sesiones sin movimiento? | CC | verificado ·mov:S31 |
| P-912 | Fila abierta a 3 sesiones de la vigente | hecho | ¿Cuántas sesiones sin movimiento? | CC | verificado ·mov:S32 |

## B. Ya verificados en S28 — no requieren Run 2, esperan decisión

| ID | Enunciado | Clase | Qué falta | Dónde | Estado |
|---|---|---|---|---|---|
| P-913 | Fila abierta a 1 sesión de la vigente | hecho | nada | CC | verificado ·mov:S34 |

## C. Decisiones de DSC — no tocan el repo

| ID | Enunciado | Clase | Dónde | Estado |
|---|---|---|---|---|

## D. Candidatos a parqueo — necesitan condición de desparqueo, no discusión

| ID | Enunciado | Condición de desparqueo propuesta | Estado |
|---|---|---|---|

## Conteo

| Grupo | Filas |
|---|---|
| A | 2 |
| B | 1 |
| C | 0 |
| D | 0 |
| **Total abiertos** | **3** |

---

## Nota sobre la forma de la cola

1 de 3 ya están verificados y esperan juicio del operador. 2 esperan que alguien mire el repo.

De los 1 del grupo B, ninguno es hueco de puente.
