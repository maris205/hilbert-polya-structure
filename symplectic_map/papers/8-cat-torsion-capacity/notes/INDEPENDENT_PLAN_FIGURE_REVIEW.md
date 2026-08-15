# Independent Plan, Citation, and Figure Integrity Review

Review date: 2026-08-14 UTC  
Reviewer role: fresh independent, read-only plan/figure/citation reviewer  
Verdict: **PASS — `PAPER8_PLAN_FIGURE_CITATION_PASS`**

## Scope and execution boundary

I reviewed the frozen paper plan, citation ledger and bibliography, figure
generators, machine manifest, provenance record, and all nine figure outputs.
I did not modify the plan, figures, citations, source lock, raw result, result
manifest, reviews, or manuscript. I did not invoke the candidate or a test
suite. Figure regeneration was performed only in an isolated temporary tree
that contained the five hash-locked source documents and figure generators;
it contained no candidate code.

## Bound artifacts

| Artifact | Observed SHA-256 |
|---|---|
| `PAPER_PLAN.md` | `3dd4162ac543b177d07aad8e4fb2921d7812dc1ed4d2b07320324aee0f33af35` |
| `notes/CITATION_VERIFICATION.md` | `7c984ced5d1ac9a22b61795d080393f9e8c83dabe04e2f4b612560f04fbdf779` |
| `paper/references.bib` | `f4567be30ef6b8d6e0bc1a3a8f6a294499221de51de4064e864cbbe448b79775` |
| `paper/figures/FIGURE_MANIFEST.json` | `e292df2cd1d9d2c19675bc36cf30ed75e88e730fca17c7cd47420285be07fb2c` |
| `paper/figures/PROVENANCE.md` | `a5f29b9fc53cfc5ea722b9083ef7f5f1ff0589b87a3ebe3d9241f4aa4d5d43a3` |
| source lock | `87d80da28cacb349c0e277b8f73812287eeb6f8a2e244945a05f90a2f6269dce` |
| raw exact result | `0d8054ad36ad8cdef1496948cf5dd98d6a1a55c186d68124f45a5e6e35bddaa0` |
| final result manifest | `045f3c3d935cd5670e900a210be9d26a2e272bd715c8e0b997da6510efd7d49f` |

The proof package, novelty audit, official experiment report, official
validation report, and Round-2 analyzer review also reproduce every hash
recorded in the plan and figure manifest.

## Plan and claims--evidence audit

The plan's release state correctly records the passing V2 final manifest and
Round-2 post-run analyzer authority. Its seven manuscript claims agree with
the frozen proof and exact result:

- the `n>12` carrier statement is theorem-only and keeps Flatters' positive
  norm-one theorem separate from Paper 8's negative-trace parity conversion;
- the standard-cat iff statement has exception set `{1,6,12}`;
- period 10 is explicitly a nonprimitive modulo-five Jordan repair with 20
  points and two cycles;
- the torsion-order clock reaches prime and composite orders alike, is locally
  unbounded/discontinuous, and is kept separate from native monodromy;
- the conclusion remains
  `INTRINSIC_TORSION_CAPACITY_CERTIFIED / A0_FAIL_PROVES_TOO_MUCH`.

The plan never uses the finite `n<=12` audit as evidence for the infinite
tail. Its nonclaims correctly exclude prime/zero matching, transfer/Fredholm
or zeta novelty, quantization, Route-A A1--A4, Route B, a primitive-divisor
converse, and priority claims. The unchecked downstream workflow boxes in the
plan are not self-issued evidence; this independent gate supplies the figure
and citation verification without altering that frozen planning snapshot.

## Citation-ledger audit

The citation ledger has final result-closure status `PASS` and is bound to
the exact result-manifest and Round-2 review hashes. It contains 12 distinct
source keys. `references.bib` contains exactly the same 12 distinct keys,
one entry per key, and the plan cites exactly that 12-key set. The existing
compiled bibliography contains 12 `bibitem` records and its BibTeX log
reports zero warnings.

The claim-role firewall is coherent: Flatters is used only for the imported
norm-one primitive-divisor results; the negative-trace conversion remains
Paper 8's derivation; arithmetic-lattice sources provide context; Ruelle and
Parry--Pollicott delimit zeta/transfer scope; Hannay--Berry and
Kurlberg--Rudnick delimit quantum scope. Tan--Li and Chandra retain preprint
status. No citation is used as evidence for an unsupported priority,
transfer, quantization, or prime/zero claim.

## Figure package and deterministic regeneration

The machine manifest is canonical JSON with schema
`paper8.figure_manifest.v1`, status `PASS`, the exact five source hashes,
eight generator/support-file hashes, and nine output hashes. Every live input,
generator, PDF, SVG, and PNG independently reproduces the recorded size and
SHA-256. Its scientific firewall records computed periods exactly 1--12,
`tail_periods_computed=[]`, theorem-only range `n>12`, no candidate rerun,
and no new scientific result.

In a fresh isolated temporary tree, `generate_all.py` regenerated each figure
twice under the frozen hash seed, source date, and bytecode settings. Both
runs were byte-identical for all nine outputs. The regenerated output hashes
and regenerated `FIGURE_MANIFEST.json` were byte-for-byte identical to the
live package, including manifest SHA-256
`e292df2cd1d9d2c19675bc36cf30ed75e88e730fca17c7cd47420285be07fb2c`.
No bytecode/cache artifact appeared.

The frozen output hashes are:

| Figure | PDF | SVG | PNG |
|---|---|---|---|
| 1 | `b6c0b975bc45e94da0c3e012498a507df9378239726adb2f654f6bb0225dc4ed` | `d56200f919428b99e3955f775b02b67af468905d64ca2f921f740eb74c11923e` | `2f5531531cce2ab3a8b264b5bc8d2998875a4644b67ddcf85681b966507b87ba` |
| 2 | `9983862ebabd20ba783441fd121925950ffffc14a9f0c397b5c1ff379d2e1789` | `7189fd770a731a70d2d4c17a2d26e4fb911fd48ab113c84712829298dcb75df4` | `6406a12408bf77c938bcead284aeb17a36408d31a046db546272737c2fc8d21e` |
| 3 | `b5205fbf59daf6f693318c8820419b79f2e5edc4824a0269f73d6675e0548f2f` | `c14d2790a6ce30a041543f75718de72bfcb5536ceaed40d2fdde493c461270ec` | `db6dc23956e4bf957fd7a174a93c2b349f7f44121fcee4a2562e5dcd4981d111` |

## Format and original-resolution visual QA

Independent inspection reproduced the format claims:

- every PDF is one-page, fully vector, contains zero raster image objects,
  and embeds/subsets all three DejaVu Serif font variants;
- every SVG parses, contains zero `<image>` nodes, and retains selectable
  text (27, 89, and 39 text nodes for Figures 1--3);
- the PNG fallbacks are RGBA at 300 dpi tolerance, with dimensions
  `2160x1065`, `2160x1305`, and `2160x1140`.

All three PNGs were inspected at original resolution. No label, panel heading,
arrow, box, axis, or right-edge element is cropped; no text/data or legend
overlap is present; mathematical text is rendered rather than exposed as raw
markup. The palette is supported by glyph/hatch redundancy.

Semantic inspection also passed:

1. Figure 1 visibly separates the exact computed audit `1<=n<=12` from the
   theorem-only range `n>12`, places the boundary at 12, records zero computed
   tail periods, and separates positive-trace import from negative-trace
   routing through indices `2n`, `n`, and `k`.
2. Figure 2 displays all twelve exact determinant/factor cells, distinguishes
   primitive carriers from the period-10 Jordan mechanism, labels its 20
   points/two cycles, marks exactly `1,6,12` as excluded, and shows the exact
   mod-2, mod-3, and mod-5 profiles without encoding determinant magnitude as
   evidence.
3. Figure 3 sends the same construction to prime and composite orders, shows
   the exact order-18 perturbation witnesses `342,990,2286`, and contrasts
   `L`, `S_10 L`, and repetition scaling with the period-dependent,
   torsion-order-blind `A^10` monodromy.

The provenance narrative and self-contained LaTeX captions make these same
evidence boundaries explicit.

## Immutability and decision

After isolated regeneration and all read-only checks, the source-lock, raw
result, and final result-manifest hashes remain exactly
`87d80d...`, `0d8054...`, and `045f3c...`; no live scientific or figure file
was changed.

The frozen plan, citation package, and figures are aligned, exact,
reproducible, visually publication-ready, and within the certified scope.
No blocking issue remains. **PASS.**
