# HCS-C61 hostile paper/source audit

Verdict: **`PAPER_HOSTILE_PASS`**.

The audit was run after the stabilized double build and treats the manuscript,
PDF, machine results, formal package, and source audit as untrusted inputs.

## Findings

1. The title and abstract match the locked C61 object: three tensor algebras,
   the mixed atlas, and the Fourier descent.
2. All required data classes are visible in extracted text: 36 rows, 18 Q
   types, 8 P types, 160/12/8 counts, both local branches, global arithmetic,
   and all explicit scope nonclaims.
3. The proof does not infer field isomorphism from subgroup order or serialized
   hashes; it states the core-free common-normal-closure criterion.
4. The P3 self-join correction and P6 mixed-Fourier distinction are explicit.
5. The Fourier text distinguishes the vanished direct component `R_0` from
   the product carrier `r_0=r_+r_3` and includes exact normalization.
6. Both `ToM 140` and `ToM 206` are retained and no branch is selected.
7. The manuscript does not claim bad Euler factors, decomposition Frobenius,
   epsilon/root numbers, automorphy, RH, a Hilbert--Polya operator, maximal
   orders, integral bases, class numbers, regulators, local-field
   classification, or rational points.
8. Citation keys and bibliography entries are one-to-one and the source audit
   locators are represented without absolute-priority language.

## Rebound evidence

- Machine report: `4b8b3bd21209cc9346ac7e38fbb9771d0b8b33de0cd28ccbb117beaa95e8c161`.
- Payload: `b7fb70451433fd4c93fd9d60a338426362f42c4594ff4de5a35e25f49819ab1a`.
- Formal root aggregate: `c5fc87d395e1e76d602d58bcbdba448e333a987c22d265aae80e1f4107a3dc28`.
- Paper source aggregate: `b35138c8497f7f9f0e5cb3db426c9c3b667f1395fc2d8a221fe737ce24633bf6`.
- Paper PDF: `7fc2af35298df1eaa15b2ec842b83e7aade01288f34826c382f96f2461c578e8`.
- Frozen source-stable producer/checker: `dadf8899f2fe82b65131a43ffbe438602db79a12654489b34d35ae8a6ee83d99` /
  `571de05ce06cf98c1acb6809800cf5f212755ce91c5d2f8eb5733eb1aa708887`.

No paper byte is used as a C61 machine certificate input.  Release promotion
remains a separate handoff gate.
