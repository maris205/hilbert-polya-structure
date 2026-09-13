# Novelty Assessment

## Decision

**GO: THE CORRECTED COMBINED PACKAGE PASSES THE PAPER-19 CANDIDATE GATE.**

The bounded primary-source search through 2026-08-19 found no direct external
collision. This is a scoped negative result, not an absolute priority claim.

The gate evidence is:

| Audit | Novelty | Standalone value | Proof confidence/readiness | Verdict |
|---|---:|---:|---:|---|
| Independent combined novelty scout | 8.2 | 8.4 | not scored | `PROCEED` |
| Independent candidate gate review | 7.9 | 8.2 | 9.1 | `ACCEPT` with scope locks |
| Adversarial character-theorem review | not scored | not scored | 0.97 probability/confidence | `PROVABLE AS STATED` |

The conservative scored triple `7.9 / 8.2 / 9.1` clears the Batch-05
conjunctive thresholds `7.5 / 7.5 / 9.0` without waiver.

## What is actually new

The novelty object is the combined package below, after all predecessor
deductions.

### Part A net-new content

Paper 17 already gives the anchored bound `dim H<=k-m`, one special equality
family, qualitative `T_k` finiteness, and special-coefficient sharpness.
Paper 19 receives credit only for:

1. `TA1`: every maximum-dimensional translate has the same canonical
   underlying subgroup `H_m`;
2. `TA2`: all such translates are classified by the explicit normalized
   scheme `E_m`;
3. `TA3--TA4`: exact activity count, nonemptiness for every coefficient tuple,
   geometric branch counts, multiple-root local rings, and the fixed-support
   flat lci family; and
4. `CA1`: coefficientwise compatible-field, compatible-group sharpness.

The general facts about characters, finite-flat root schemes, discriminants,
and lci morphisms are tools rather than novelty claims.

### Part B net-new content

The strongest new contribution is the support-one arbitrary-dimensional
theorem:

1. gcd reduction into `g` core residue classes;
2. arbitrary-rank colored component-height classification;
3. exact character extinction after `q^2` core equations;
4. the unique `q^2-1` Laurent shadow with explicit generating functions;
5. the seven-label theorem; and
6. universal scalar incompatibility of that shadow for every `q>=3`.

The `q=2,k=2` `CBA` endpoint is already owned by Paper 16. Its reproduction
inside the all-`g` theorem is a recovered boundary check, not a novelty bullet.

## Candidate history and dispositions

| Candidate | Disposition | Reason |
|---|---|---|
| Maximum-dimensional anchored translate moduli alone | `MERGE / NOT STANDALONE` | Proof-ready but portfolio-adjusted novelty was about 5.5; too directly adjacent to Paper 17. |
| Universal support-one sharp clock `kq/(kq-1)` | `STOP-S1 / FALSE` | The unique `q^2-1` character shadow fails to lift already at `(k,nu,d)=(3,1,2)`; the corrected proof shows failure for every `q>=3`. |
| Character extinction alone | `MERGE` | Elegant but arithmetically incomplete without scalar-lift analysis and too narrow without Part A. |
| Corrected support-one gcd obstruction alone | `MERGE` | Novel and proof-heavy, but the maximum-translate contrast supplies the natural character-versus-scalar-lift narrative. |
| Part A plus corrected Part B | `SELECT / GO` | Clears novelty, standalone, and proof gates with one mechanism and distinct theorem mass. |

## STOP-S1: retained false-sharpness history

The initial support-one conjecture reasoned incorrectly from a unique
rank-one-looking character pattern to a scalar lift. It asserted that
`V_(kq-1)` should always contain a positive-dimensional translate and that
`kq` should be an exact scalar clock.

The failure has two layers.

1. A character-pattern classification must cover arbitrary actual
   `X*(H)`, not only a rank-one ansatz. This is repaired by colored scaling
   components, integer heights, and ambient-character surjectivity.
2. Even the unique character shadow need not satisfy its scalar pairings.
   The seven forced labels imply `bc^(d-1)=-1` and `a=-1`, after which a `Z`
   equation gives `2c=0` for every `q>=3`.

The corrected theorem therefore calls `kq-1` a universal obstruction or a
one-step improvement over character extinction. It never calls it exact,
optimal, shortest, or minimal. `STOP-S1` remains visible in every lifecycle
document so that the false claim cannot be silently revived.

## External collision matrix

| Claim family | Closest checked work | What the checked work supplies | Remaining Paper 19 content | Judgment |
|---|---|---|---|---|
| Maximum subgroup `H_m` | Habegger; Suciu--Yang--Zhao | General subgroup/translated-subtorus intersection geometry. | Equality rigidity inside a specific recurrence variety. | No direct collision. |
| Normalized scheme `E_m` | General contained-subvariety parameter spaces; root schemes. | Standard torus and scheme tools. | Exact active indices, reconstruction, open inequalities, branch formula. | Recurrence-specific contribution remains. |
| Fixed-support family | Standard discriminant and lci theory. | General smoothness/multiple-root language. | Identification of the recurrence translate family with an open root-scheme product. | Application is new; tools are not. |
| Coefficientwise sharpness | Laurent 1984. | No-coset-to-finiteness bridge. | Nonempty equality translate for every permitted coefficient tuple. | No collision. |
| `q^2` extinction and unique shadow | Linear recurrences/LFSR as a broad neighborhood. | General finite-field recurrence language. | Colored height theorem and exact monomial window for this character automaton. | No direct collision. |
| `q>=3` scalar obstruction | Group-algebra character independence. | Standard local cancellation tool. | Seven forced labels and the universal `2c=0` obstruction. | Strongest new claim. |
| `q=2` `CBA` | Local Paper 16. | Exact planar `T_4/T_3`, `CBA`, effective bound. | Only general-`g` fill and unified endpoint bookkeeping. | Planar core deducted. |
| Shift-like terminology | Bedford--Pambuccian; Bera; Bera--Verma; Kaur. | Complex dynamics of the map class. | Finite-rank contained-translate geometry. | Provenance only. |
| Orbit/subgroup arithmetic | Bell--Ghioca; Ji--Xie--Zhang; Mello--Yasufuku. | Fixed-orbit hitting, cyclotomic rigidity, multiplicative dependence. | All-initial-state finite-window survivor varieties. | Different quantifiers. |

## Portfolio audit

### Paper 16 penalty

Paper 16 owns the planar support-one `CBA` theorem and a stronger effective
bound. Paper 19:

- gives no newness score to `q=2,k=2`;
- calls it a recovered endpoint;
- states that Paper 16 remains quantitatively stronger; and
- does not revive Paper 14, which Paper 16 already absorbed.

### Paper 17 penalty

Paper 17 owns the entire anchored dimension law and its terminal arithmetic
corollary. Paper 19:

- does not headline `dim H<=k-m`;
- starts its contribution at equality-kernel rigidity;
- clearly separates the special predecessor equality family from the complete
  normalized translate scheme; and
- treats coefficientwise sharpness as an upgrade with compatible quantifiers.

### Paper 18 boundary

Paper 18's marked trace coordinates and Fitting/ramification boundary do not
intersect the Paper 19 theorem package. “Scheme-theoretic” is a shared style,
not a shared result.

## Proof-risk audit

The candidate gate originally isolated one potentially fatal quantifier gap:
why a unique rank-one shadow analysis excludes a positive-dimensional torus
of arbitrary rank. The adversarial review closed it as follows.

1. Exclusive `A/B/C/Z` labels make every active triple contain exactly two
   nonzero vertices in one scaling component.
2. Signed cycle weights define an integer height on each component.
3. Distinct formal colors prevent accidental equality of disconnected
   component values from merging them.
4. The `q^2-1` zero triangle forces every nonzero component to contain the
   same central vertex; hence only one component exists.
5. Ambient coordinate characters generate the actual `X*(H)`, so no unused
   direct summand remains and the actual torus has rank one.

The explicit generating functions prove every window entry is zero or one
monomial; no finite enumeration is used. The adversarial verdict is
`PROVABLE AS STATED` with confidence `0.97`. The residual risk is typesetting
of the core/original index conversion, not a mathematical blocker.

## Unified-article and page test

The project passes the unity test because both parts ask the same question:
after characters force an extremal subgroup pattern, which translating
scalars lift it into the recurrence variety?

- In Part A, every maximum-dimensional anchored pattern lifts along the
  explicitly parameterized nonempty scheme `E_m`.
- In Part B, the unique support-one penultimate pattern does not lift for
  `q>=3`; only the recovered `q=2` endpoint lifts on a precise coefficient
  locus.

The proof architecture supports `26--29` genuine pages, with a current
29-page budget. About 14 pages are Part A and 13 pages are Part B proof
material; related work and limitations use about one page. No appendix,
background inflation, code, data, or formatting padding is needed.

## AC01--AC18 novelty audit

All anti-claims are active. In particular:

- “maximum-dimensional” never means inclusion-maximal;
- `E_m` is not a Hilbert/Fano scheme;
- geometric component counts retain their field and squarefree qualifiers;
- coefficientwise sharpness never means every fixed group;
- `q>=3` never receives exact-threshold language;
- Paper 16 and Paper 17 ownership is explicit;
- standard machinery is not called novel;
- positive characteristic and zero coefficients are excluded;
- Laurent is qualitative; and
- no global priority or external lifecycle effect is asserted.

## Final novelty judgment

Part A alone would be too incremental, and the original Part B sharpness
claim was false. The corrected combination is materially different: it gives
one complete lift space and one universal lift obstruction, joined by the
same character-scalar mechanism. After the full Paper 16 and Paper 17
portfolio deductions, all three gate axes remain above threshold.

**NOVELTY STATUS: GO / AUTHOR SOURCE DESIGN COMPLETE SUBJECT TO FRESH
INDEPENDENT SOURCE REVIEW.**
