# P191 Review A — standalone delta acceptance

## Disposition

**PASS — DELTA ACCEPTED.**

Formal counterexamples: **0**.  Critical findings: **0**.  Major findings:
**0**.  Open Minor findings: **0**.  Historical Minor findings: **1, closed**.
No manuscript theorem, proof, formula, reference, or PDF change was required.

## P191-A-MI-01 — exact repair

Round-0 `SOURCE_VERIFICATION.md` contained

```text
submitted 16 July 2026 and modified 27 August 2026; accessed 4 September 2026
```

The accepted requested-only repair is

```text
submitted 16 July 2026; approved/latest entry revision 22 July 2026; accessed 4 September 2026
```

The official history has no 27 August entry revision; the old text had
mistaken a database-wide footer for entry history.

```text
old SOURCE_VERIFICATION.md SHA-256:
  71e6ed195bc75584e071ff5f27975ab756eb66287acd99299fbeea596c9a1c70
accepted SOURCE_VERIFICATION.md SHA-256:
  26a0e2d9112a938d8dcc388e378f5cf1f89cdea99b4f3941729db094d70373b9
unchanged main.tex SHA-256:
  bdccfa1e266988c1215c7a6735f25f334a39eb99963320b7d8bf43e0d5e6db84
unchanged main_round0_original.pdf / main_round1.pdf / main.pdf SHA-256:
  d8675928ecfe528b950af5402097b5f69657efc9cba7c8eb0bb5c27ec96df78b
unchanged references.bib SHA-256:
  1141067122be2dc4613007009d732fdcfc1dd35edf0c85d19ced38ef47acad0c
```

## Acceptance checklist

- [x] The unsupported 27 August entry-modification claim is absent.
- [x] The replacement date is explicitly tied to the official OEIS entry
      history and is 22 July 2026.
- [x] The distinction `A398023: i | s_i` versus `P191: a_i | s_i` remains.
- [x] The bounded non-hit disclaimer and `OWNER_AMBER / HOLD_EXTERNAL` remain
      unchanged in force.
- [x] `main.tex`, the immutable Round-0 PDF, theorem/proof package, author
      verifier, and author canonical remain byte-identical.
- [x] `main_round1.pdf`, live `main.pdf`, and `references.bib` retain their
      no-change hashes.
- [x] Review A pins the repaired source ledger, reruns the independent control
      twice, and obtains byte-identical canonical output.

Finding `P191-A-MI-01` is accepted and closed.  Final open counts are
`Critical 0 / Major 0 / Minor 0`, and the Review A verdict is
`PASS_DELTA_ACCEPTED`.  Acceptance does not constitute novelty, priority,
ownership, or external-release clearance; lifecycle remains `HOLD_EXTERNAL`.
