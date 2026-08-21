# Adaptive batch plan and release record: HCS-C79 through HCS-C83

Status: **round complete; five packages prefreeze-verified and release-ready**

Scope firewall: `NO_BAD_EULER_OR_ROOT_NUMBER`.

This is a five-paper continuation of the frozen named-core mark lane.  Each
paper answers a distinct finite question selected from the preceding exact
certificate; none is a relabeling of an earlier matrix invariant.  The round
does not claim arithmetic/local data, Euler factors, root numbers, automorphy,
a full Burnside ring or table of marks, or a Hilbert--Polya operator.

## Research sequence

1. **C79 — minimum-repair witness multiplicity.**  For every retained support,
   enumerate the minimum number of restored labels and the number of minimum
   witnesses; publish the joint repair/witness atlas.
2. **C80 — all-20-subgroup threshold-repair atlas.**  For every one of the 20
   frozen subgroup targets and all 65536 supports, compute the exact threshold
   repair profile and recover the C78 marginal.
3. **C81 — effective-1920 repair-profile orbit quotient.**  Quotient the C79/C80
   profiles by the faithful 1920-element label action while retaining the
   distinction from the 11520-element ambient lift.
4. **C82 — bit-flip noise and Walsh spectrum.**  Treat the full-core indicator
   as a Boolean function, compute its exact integer Walsh transform, degree
   energy, and Hamming-distance noise response.
5. **C83 — random-order prefix stopping time.**  Weight every pivotal full-core
   support by prefix/suffix factorials to obtain the exact stopping-time law for
   a uniformly random order of the sixteen labels.

## Authority chain

The common source is the frozen named coordinate model and its exact closure
certificates:

```text
C73 generation criterion
        |
C75 11520 ambient lifted closure-incidence symmetry
        |
C76 1920 effective label image and 65536-support orbit atlas
        |
C78 repair-distance boundary --------------------+
        |                                         |
 C79 witness atlas ---- C80 threshold atlas       C82 Walsh/noise atlas
        |                 |                       |
        +-------- C81 effective repair profiles --+
                              |
                         C83 random-order stopping law
```

C75's order `11520` is an ambient lifted pair action.  Its six-element
label-action kernel yields the faithful effective order `1920` used by C76,
C81, and the orbit quotient.  These orders are not interchangeable and are
kept separate in the code, evidence, and papers.

## Gate and artifact ledger

All five rows passed: producer, independent checker, separate symbolic or
finite cross-check, clean-process replay, hostile semantic mutations, and two
isolated deterministic LaTeX builds with embedded fonts and zero undefined
references.  The evidence and manifest hashes are SHA-256 values of the exact
committed artifacts.

| paper | gate result | hostile mutations | evidence SHA-256 | manifest SHA-256 | PDF SHA-256 |
|---|---|---:|---|---|---|
| C79 | producer/checker/SymPy/replay PASS | 22/22 | `147a9b77e0ee7459040a7cc3c026bb21bce950a806e4fbc3ce0441dc9bb6c879` | `982cce509de371d59c4b87cda75af057d994c6fc36146daddc3b983c9c63246c` | `d6f75f6988400da3723bded7de4c523f1cb0d802b65459bc647b0fae82bbdbb2` |
| C80 | producer/checker/SymPy/replay PASS | 13/13 | `8d27428b14dbd7354e9c8308ad76b1108e3f551702165833301509cd52de7df5` | `a674116ab6f8f9478130219cc525478525f10f2e42f515e71418a3066e2b229c` | `853886c1cc20424eeb3eb71227df6135a90ccc3166c97a31e1119ea59cd73a31` |
| C81 | producer/checker/SymPy/replay PASS | 14/14 | `c3cc35f45e1c8f7c9d4ecaecca820bf9dbc4db1c6a5769c20c75bad21f32fd9f` | `ff3028fd68817795b08ff24332ef44de4cf520ccba543f053fbd78140ac1b512` | `d6bb73164b5e4602604944d359d54c83e2e0bfe1c40044ae653ea8d13b4bdf80` |
| C82 | producer/checker/SymPy/replay PASS | 13/13 | `6fc49cad02956f463b1e37d017506f437edce6717414da74770ad94913ccefa1` | `5934de3a933e559e941fc636860db2f9f5ceca181acd9d4915396e9facdc8f8b` | `b111d8ea403d5c87c0565a99633b0815b861d4a532eae356b6e295e40c78fa30` |
| C83 | producer/checker/SymPy/replay PASS | 15/15 | `033f42f0eea2518f7cb269dd465d82d4871a729d2b93679fcd9f3af38cf9ca28` | `981f9b07297f1b69676e8ced2625e69df5bd8fcd366415a2f984eb6311ddaa85` | `47fdd116564bac2790593f67a4d65e1b664d98e3f3206231c131c7827fe0722c` |

## Round-wide release checklist

- [x] C79--C83 producers regenerate canonical evidence with no byte drift.
- [x] Independent checkers pass without using producer output as a shortcut.
- [x] SymPy/finite cross-checks, clean replay, and hostile mutation tests pass.
- [x] C81 keeps the 11520 ambient versus 1920 effective distinction explicit.
- [x] C82 has a project-local `C82_PREFREEZE_MANIFEST.json` and linked docs.
- [x] All manifest-listed file hashes match their local files.
- [x] All five papers compile twice in isolation; PDFs have embedded fonts and
      zero undefined references/citations.
- [x] `henon_dynamics/codex_prompt.md` is unchanged.
- [x] The accidental empty root-level path
      `henon_mu3_yukawa_mark_bitflip_noise_fourier_spectrum/` is absent.
- [x] No bad Euler, root-number, automorphy, full-Burnside, or Hilbert--Polya
      claim is introduced.

The release operation is limited to these five packages, this batch plan, the
index additions in `henon_dynamics/README.md`, and the required evidence and
manifest files.  The next five-paper round remains unselected until explicit
confirmation.
