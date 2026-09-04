# Route A — Round-2 hostile Review-B closure for P192–P196

Status: `5/5 ROUND2 FROZEN / 10/10 REVIEWS ACCEPTED / OPEN FINDINGS
0 CRITICAL / 0 MAJOR / 0 MINOR / HOLD_EXTERNAL`.

## Frozen Round-2 manuscripts

| paper | pages | Review-B decision | Review-B assertions | Round-2 PDF SHA-256 |
|---:|---:|---|---:|---|
| P192 | 4 | `ACCEPTED_NO_CHANGE` | 4,606,117 | `e06aac2579f0d90a15c1a7a2c8fa09ce57286f15818a10c2466cd06d210d6b57` |
| P193 | 5 | `ACCEPTED_NO_CHANGE` | 1,170,066 | `b5b2f4e77bada6229a0716d9780a871f95b8e6ba75fa2c9e6794b5bf524ad0d9` |
| P194 | 5 | `ACCEPTED_REPAIR` | 16,194,669 | `682eeced97037b899f91dc2b93afaaf514b6dcbf8f95d1225ddb87f4cce6203b` |
| P195 | 3 | `ACCEPTED_NO_CHANGE` | 9,390,311 | `d5dbac8ed78f1f3eccc3c7aeccda852e6f44f77a513091032120254119ff9c0a` |
| P196 | 3 | `ACCEPTED_NO_CHANGE` | 421,266 | `bb0ee2d7e155bd515a250fe1c84146fcea3d2586b903fd5a71ecedb1a3d34948` |
| **total** | **20** | **five accepted Review-B decisions** | **31,782,429** | — |

P192, P193, P195, and P196 required no change after Review B; their Round-2
PDFs are byte copies of their accepted Round-1 PDFs. P194 alone has an
intentional Round-1-to-Round-2 change. Its four-page immutable Round-1 PDF is
still pinned at
`9f1b67680b4c915e5bd60d01730095d5d06817368244d83ecfc84d39a86bf207`,
while the accepted source-only repair reflows to the five-page Round-2 PDF in
the table.

## Process-separated Review-B attacks

| paper | fresh Review-B carrier/proof route | theorem surfaces reopened |
|---:|---|---|
| P192 | residual-cycle splitting plus a parking-content dynamic program | `n=2`, Hurwitz orientation, advancing-index clock, fixed census, every labelled target fibre, maximum fibre, Campion Loth–Rattan subtraction, and the conjecture firewall |
| P193 | cut bits plus recursive consecutive-interval groupings | simultaneous mutual pairs, block refinement, pointwise and sharp depths, depth OGFs, full image criterion, target product, and unique fibre maximum |
| P194 | adjacent sign rewriting, Fomin growth diagrams, Gelfand–Tsetlin branching, cyclotomic products, Young-poset linear extensions, and matching-generated involutions | highest sinks, exact clock, Schur depth layers, component multiplicities, sharp tail, every-target inverse atlas, stable full-fibre threshold, and source ownership |
| P195 | rerooted oriented-edge component-size arrays plus rational EGF reconstruction | odd fixed points, even two-cycles, sharp witnesses, recurrent weighted EGFs, every-root fibres, maxima, and the multiple-cycle counterexample inside one `H` component |
| P196 | packed-radix words, labelled relation matrices, cyclic constraint products, and Faddeev–LeVerrier characteristic polynomials | one-step core, rotation restriction, fixed-iterate and cycle counts, corrected characteristic polynomial, and every-target gap fibre product |

Every Review-B verifier imports neither author code nor Review-A code. Each
package records two fresh Review-B executions that are byte-identical to each
other and to its canonical transcript. All five packages end with zero open
Critical, Major, and Minor findings.

## P194 source repair and acceptance

Review B opened historical finding P194-B1, a Major source-owner omission,
against the immutable Round-1 package. The missing nearest source was Colin
Defant and Nathan Williams, *Crystal Pop-Stack Sorting and Type A Crystal
Lattices*, *European Journal of Combinatorics* 103 (2022), article 103514,
DOI `10.1016/j.ejc.2022.103514`, arXiv `2109.08251`.

The author added the bibliographic record and a conservative subtraction in
the abstract, comparison discussion, close, and source ledgers. The repaired
paper gives the whole crystal pop-stack orbit-to-highest and sharp-orbit
surface zero contribution credit. It distinguishes Defant–Williams' one
macrostep to the unique source of a component restricted by the starting
descent-colour set from P194's one Kashiwara edge of the least currently
available colour, followed by recomputation.

The repair changes no literal update, theorem statement, numbered equation,
proof, example, author verifier, or canonical transcript. Reviewer B accepted
the repair, and the original Reviewer A independently accepted it as a
post-B source-only nonregression. Thus P194-B1 is historical and resolved; it
is not an open finding.

## Finding accounting

Review B itself encountered `0 Critical / 1 Major / 0 Minor` historically:
only P194-B1, now resolved. Across the complete author–A–B lifecycle, the
historical census is `0 Critical / 4 Major / 4 Minor`, all resolved. The
current open census is separately and exactly `0 Critical / 0 Major / 0
Minor`.

The four historical Majors are P192-A1, P193-A1, P194-B1, and P195-A1. The
four historical Minors are P192-A2/A3/A4 and P195-A2. No closed item is
carried forward as an open defect.

## P192 theorem-status firewall

P192's four reviewed proved axes remain: strict advance of executed collision
indices with sharp tail `n-2`; fixed count `(n-1)^(n-2)`; a complete
every-target one-step inverse atlas; and unique maximum one-step fibre `n-1`.
The separate history-set formula

```text
#Hist = I = (n-1)^(n-2-|I|)
```

is still `CONJECTURE_ONLY`. Its binomial depth census and general
unique-deepest consequence are conjectural as well. Exact checks through
`n=8` and the independent `n=9` Prüfer stream are finite evidence only and
are not used to prove the four theorem axes.

## Meaning of the Round-2 freeze

Round 2 records internal mathematical, source-subtraction, replay, and PDF
acceptance. It does not establish novelty, priority, owner completeness,
freedom to operate, or permission to circulate. The binding states are
`OWNER_RED_AMBER / HOLD_EXTERNAL` for P192 and
`OWNER_AMBER / HOLD_EXTERNAL` for P193–P196.
