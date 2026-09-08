# IR1 source applicability and collision audit

Checked 2026-09-07. This is a bounded primary-source applicability audit,
not a claim that the entire literature has been exhausted. The research-lit,
idea-creator and proof-writer workflow instructions governed the lane;
ARS source verification was used only for provenance and applicability.
No paid external model, full paper-production pipeline or GPU was used.

## Frozen object against which every source is compared

`a in Z`, `T_a(x,y,z)=(y,z,yz+a-x)`, all ordinary integer points,
all levels of `K_a=x^2+y^2+z^2-xyz-a(x+y+z)`, one native iterate
per clock step. The output is a complete periodic-orbit classification
and exact per-level counts, not a whole-automorphism-group orbit theorem,
positive-point descent theorem, finite-field count or real escape cone.

## Nearest applicable sources and exact deductions

### Roberts: inherited trace-map escape, not forced integral exhaustion

Primary author PDF: [J. A. G. Roberts, Escaping orbits in trace maps,
Physica A 228 (1996), 295–325](https://web.maths.unsw.edu.au/~jagr/R96.pdf).
Read the abstract and introduction, the discussion identifying Theorems
3.1/4.1, and the displayed statements/discussion surrounding Corollary
4.1 and Section 5. The source treats polynomial maps preserving the
unforced Fricke–Vogt invariant, with product coefficient two in its
normalization. Its escape exclusions and reversal framework are prior
theory and are deducted. A scalar rescaling recovers our `a=0` map;
it does not remove the additive `a` or its invariant's linear terms.
No statement read supplies our all-`a` integer terminal-cycle list.
OCR-distorted formulas were not used as proof premises.

### Cantat–Loray: same cubic family, different quantified group action

Verified publication metadata at the
[AIF publisher record](https://aif.centre-mersenne.org/item/AIF_2009__59_7_2927_0/):
Serge Cantat and Frank Loray, Annales de l'Institut Fourier 59 (2009),
2927–2978, DOI 10.5802/aif.2512. Read the explicit cubic equation,
Theorem A, Theorem C and Section 5.2's group-orbit statements in
[arXiv:0711.1579v2](https://arxiv.org/pdf/0711.1579v2), dated 2007-12-05.
Their cubic has product sign plus. Our change `(X,Y,Z)=(-x,-y,-z)`
gives their parameters `(A,B,C,D)=(-a,-a,-a,k)`; our map becomes
`(Y,Z,-YZ-a-X)`, a cyclic permutation after a Vieta involution.
This is a genuine source-family overlap, not a new geometric family.
Theorems about bounded or finite *whole-group* orbits do not classify
points periodic under this one fixed element. The quantified action
cannot be exchanged. The new difference-amplitude proof does not invoke
a group-boundedness conclusion for a merely `T_a`-periodic point.

### Baragar: integral descent/counting is prior, but not this fixed clock

Primary archive metadata:
[Arthur Baragar, Asymptotic growth of Markoff–Hurwitz numbers,
Compositio Mathematica 94 (1994), 1–18](https://numdam.org/item/CM_1994__94_1_1_0/).
The introduction and initial descent discussion were read from its
archive PDF during the initial round-two retrieval; subsequent PDF
opens were intermittent failures, while the non-`www` item record was
successfully rechecked. Ordered positive solutions, group moves and
growth estimates are deducted. They are not an all-sign, forced-linear
cubic, fixed-native-clock cycle classification.
The separate *Integral solutions of Markoff–Hurwitz equations*, JNT 49
(1994), 27–44, is a verified bibliographic lead, not a theorem imported
from a text that was not read in this lane.

### Gamburd–Magee–Ronan: modern complete counting does not transfer

Primary publisher PDF:
[An asymptotic formula for integer points on Markoff–Hurwitz varieties,
Annals of Mathematics 190 (2019), 751–809](https://annals.math.princeton.edu/wp-content/uploads/annals-v190-n3-p02-s.pdf),
DOI 10.4007/annals.2019.190.3.2. Read the abstract, introduction through
Theorem 3 and the initial move/descent construction. Their equation has
a multiplicative product coefficient and a constant level; the task is
asymptotic counting of integral tuples using many allowed moves. Its
symbol `a` is not our additive forcing parameter. Neither the counted
set nor its clock is the present single-map periodic locus. No counting
asymptotic or exceptional-family assertion is promoted to our theorem.

## Fresh 2024–2026 collision checks, limited to the material actually read

- [Seung Uk Jang, arXiv:2502.18976](https://arxiv.org/abs/2502.18976),
  submitted 2025-02-26. Read metadata and abstract, not full text.
  Its residual transitivity/minimality statement concerns nonsingular
  `p`-adic integer points and algebraic-automorphism actions. This is not
  our all-singularity ordinary `Z^3` single-map period problem.
- [Matthew de Courcy-Ireland, Matthew Litman and Yuma Mizuno,
  arXiv:2509.02187](https://arxiv.org/abs/2509.02187), v3 revised
  2026-06-05. Read the current metadata and abstract, not full text.
  It concerns group-orbit divisibility over prime fields for Markoff-like
  surfaces. This does not yield ordinary characteristic-zero integral
  cycle lengths. The current revision date was verified, not inferred
  from a search engine's indexing date.
- [Tim Browning and Florian Wilsch,
  arXiv:2407.16315](https://arxiv.org/abs/2407.16315), submitted 2024-07-23.
  Read metadata and abstract only. Density heuristics and numerical
  integral-point data for affine cubic surfaces are relevant background,
  not the required exact periodic classification.

These abstract-level exclusions are claims about the stated subject,
not assertions that an unseen full text contains no related observation.

## Local ownership and closest-claim subtraction

The existing C413 package at
`henon_dynamics/continuation_c409_c413_round2/nonlinear_geometry/PROOF_PACKAGE.md`
already owns the complete unforced `a=0` integer trace classification.
It was read but not edited or recomputed. The entire `a=0` content,
including the six- and twelve-step families and level formulas, is
deducted from novelty. The first-pass NG1 work already knew F4 for every
`a` and only a partial section/escape reduction; F4 itself is also
deducted. The admitted M1/AS2, old sealed reserve and prior batch
manuscripts remain untouched.

The surviving candidate contribution is narrowly the *uniform all-`a`
exhaustion*: parameter elimination in the two-step difference equation,
the five-center signed maximum proof, the height-versus-difference
four-channel lemma, an explicitly terminated universal recurrent core,
and its complete native oriented classification and level counts.
The two sporadic words alone, a finite period table alone, or another
formula for F4 would not meet that contribution claim.

## Search and access record

Fresh searches included more than eight distinct formulations. Among
the actually executed queries were the following:

1. `"integer" "periodic orbits" "trace map" Roberts`
2. `"x" "yz+a-x" periodic integer`
3. `"x_{n+3}" "periodic" "integer" trace map parameter`
4. `Baragar 1994 "Hurwitz" "94" integer points`
5. `"x^2+y^2+z^2" "periodic" "integers" "a" Markoff cubic 2025 2026`
6. `"Markoff" "integer periodic points" parameter`
7. `"x_{n+3}" "x_{n+1}x_{n+2}" constant periodic integers`
8. `site:arxiv.org "Residual Transitivity" "Markoff" Jang`
9. `site:arxiv.org "Markoff" "Courcy-Ireland" "2025"`
10. `site:arxiv.org "Integral points on cubic surfaces" Browning Wilsch`

Earlier round-two broad Cantat–Loray/Roberts/Hurwitz queries supplied
the nearest-source leads before computation. Aggregators and search
snippets were used only for discovery; substantive source statements
above point to actually opened primary material. A failed nonexistent
arXiv HTML-version attempt and intermittent Numdam PDF failures supplied
no mathematical evidence. No Zotero/Obsidian backend or local arXiv
download helper was available, so the announced primary-web fallback
was used. No unrelated papers were downloaded into the workspace.

## Audit verdict and boundaries

No complete matching all-parameter single-map integer classification was
located in the inspected primary material. That bounded observation is
not a claim of global first priority. The source-family overlap is high,
but no theorem read removes the actual fixed-clock exhaustion delta.
Independent mathematical and finite-certificate review is still required
before admission. `IR2` remains an unused conditional slot because IR1
now has a complete candidate closure; no replacement question is counted.

Source arithmetic remains distinct from target arithmetic;
`NO_BAD_EULER_OR_ROOT_NUMBER` remains unconditional. The zeta factors
in `IR1_CLASSIFICATION.md` count native dynamical cycles only.
