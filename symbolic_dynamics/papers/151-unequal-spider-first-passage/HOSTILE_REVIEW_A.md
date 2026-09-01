# Hostile Review A — P151 leaf-marked first passage

**Review date:** 2026-09-01 UTC  
**Reviewer status:** independent of the P151 authoring pass  
**External status:** `HOLD_EXTERNAL`  
**Verdict:** **REVISE**

## Severity summary

| severity | count | disposition |
|---|---:|---|
| Critical | 0 | no theorem-level contradiction found |
| Major | 1 | owner subtraction is incomplete and must be repaired before an internal accept |
| Minor | 3 | version-of-record metadata, control-independence wording, and a formal/analytic bridge |

The mathematics survived independent re-derivation, including unit arms,
`r=2`, the all-one profile, exact equality classes, and the dilation inverse.
The executable and PDF artifacts also reproduce.  The blocking issue is not a
counterexample: it is a missing direct generic owner whose formulas sit
immediately upstream of the manuscript's marked-law and moment claims.

## Major finding

### M1 — The owner firewall omits a direct generic time/place law and its moment formulas

The subtraction table in `main.tex` cites general-tree endpoint/mean work,
equal-arm stars, half-line spider spectral theory, and network tomography, but
does not cite the most direct generic finite-chain result located in this
review:

- Bruno Sericola, “On cover times of Markov chains,” *Stochastic Models*
  40(4), 685--727 (2024),
  [DOI 10.1080/15326349.2024.2319201](https://doi.org/10.1080/15326349.2024.2319201),
  [author-hosted HAL record](https://inria.hal.science/hal-04364216).

For a finite Markov chain and a target set `A`, Sericola gives the full joint
time/place law in matrix form,

```text
Pr_i(T_A=n, X_(T_A)=j)=(P_(A^c)^(n-1) P_(A^c,A))_(i,j),
```

as well as endpoint masses, first moments, second moments, and mixed
time/place moments.  Taking the generating function of this identity already
gives a generic leaf-marked resolvent.  It does **not** appear to state P151's
closed continuant product for an unequal finite spider, so this is not yet a
same-formula kill.  It is nevertheless a direct owner of the generic marked
law and moment machinery, not merely distant “resolvent language.”

A second omitted nearest source is Haiyan Chen, “The generating functions of
hitting times for random walk on trees,” *Statistics & Probability Letters*
77, 1574--1579 (2007),
[DOI 10.1016/j.spl.2007.03.044](https://doi.org/10.1016/j.spl.2007.03.044).
The publisher record states an algorithm for hitting-time probability
generating functions on general trees.  Chen's target is an ordinary hitting
time rather than P151's full first-leaf mark, so it is nearest rather than a
literal owner, but it belongs in the continuant/PGF subtraction lane.

Why this is Major: the abstract says “we derive the complete probability
generating function jointly marked by the absorbing leaf,” and the
contribution paragraph calls the marked transform one of four retained axes.
Without subtracting the generic joint time/place identity, a reader cannot
tell whether the residual is the existence of a marked PGF, the use of a
resolvent, or only the particularly simple unequal-spider continuant closed
form.  The first two are already generic inputs.

Required repair:

1. Add and verify the Sericola 2024 and Chen 2007 primary records in
   `references.bib` and `SOURCE_VERIFICATION.md`.
2. Put Sericola in the main subtraction table as **direct generic owner** of
   the joint hitting-time/location law and first/second moment matrices; put
   Chen in the nearest tree-PGF row.
3. Narrow contribution language everywhere: the residual transform axis is
   the explicit unequal-spider continuant factorization and elementary
   excursion reduction, not generic existence, rationality, or a generic
   time/place law.  Likewise the variance axis is the compact scalar
   specialization, not the availability of a second moment.
4. Compare Sericola's subset-hitting formulas and Chen's tree algorithm
   explicitly against the literal spider specialization.  If either source
   already prints the same unequal-arm closed form after notation changes,
   reopen or remove that axis rather than relying on the present bounded
   non-hit.
5. Keep the result under `HOLD_EXTERNAL` until this subtraction is complete.

## Minor findings

### m1 — de la Iglesia--Juarez is cited only as a 2021 preprint although a version of record exists

`references.bib` currently has only `arXiv:2111.10450`.  The work was published
as Manuel D. de la Iglesia and Claudia Juarez, *Journal of Mathematical
Analysis and Applications* 517(2), article 126624 (2023),
[DOI 10.1016/j.jmaa.2022.126624](https://doi.org/10.1016/j.jmaa.2022.126624).
The [publisher record](https://www.sciencedirect.com/science/article/pii/S0022247X22006382)
confirms the journal metadata and that “reflecting--absorbing” is a stochastic
UL factorization, as the manuscript correctly explains.

Repair: cite the journal version of record, optionally retaining the arXiv URL,
and update the source ledger and printed bibliography consistently.

### m2 — The claimed independence of the exact checks is overstated

The abstract calls all 1,446,432 checks “independent,” and the audit table
labels 400 assertions “Independent one-attempt moments.”  In
`verify_p151.py`, `verify_excursion_moments()` uses the same `continuant()`,
`poly_shift()`, and `quotient_derivatives()` machinery used for the transform
and derivative checks.  It is a useful additional parameter sweep, but it is
not an independent computational route.  The literal state recursion is
genuinely separate for the coefficient checks; the one-attempt derivative
block is not.

Repair: either replace “independent” by “exact”/“additional” in the abstract,
main audit, ledgers, and README, or implement the advertised independence with
a separate finite-difference or literal absorbing-chain recurrence for the
one-attempt first and second moments.  Do not change the frozen assertion count
without regenerating every dependent table and transcript.

### m3 — Connect the formal renewal identity to evaluation at `z=1`

The transform proof correctly invokes a formal series at equation (4), then
the moment proof evaluates that rational identity at `z=1`.  The bridge is
true but implicit.  A single sentence would close it cleanly:

```text
Q(0)=0, while Q(1)=1-H/r<1 and
D(1)=H product_i ell_i>0.
```

This simultaneously justifies the formal inverse near zero, almost-sure
renewal at one, and the endpoint/moment evaluations.  It is especially useful
because the Chebyshev display contains `1/z` even though the equivalent
continuant expressions are regular at zero.

## Independent mathematical audit

### Marked transform

For an arm of length `m`, fair walk started at one and killed at `{0,m}` has
the success and return transforms

```text
z^(m-1)/P_m(z),                 z P_(m-1)(z)/P_m(z).
```

After restoring the centre step and the uniform arm choice, a successful
attempt at leaf `i` has transform `z^ell_i/(r P_ell_i)` and a failed attempt
has transform

```text
Q(z)=z^2/r sum_j P_(ell_j-1)(z)/P_(ell_j)(z).
```

Renewal gives `F_i=S_i/(1-Q)`, and denominator clearing is exactly the stated
`D(z)`.  Since every continuant is even in `z`, the parity support follows;
the unique monotone path gives the first atom.  No missing factor of `z`, `r`,
or `2` was found.

### Mean and variance

For one selected arm of length `m`, including the departure step, direct
recurrences give

```text
Pr(success)=1/m,
E[A_m]=m,
E[A_m^2]=m(m^2+2)/3,
E[A_m 1_return]=2(m^2-1)/(3m).
```

Averaging over arms yields

```text
p=H/r, mu=L/r, nu=(C+2L)/(3r), rho=2(L-H)/(3r).
```

From `T=A+(1-B)T'`, first moments give `E[T]=mu/p=L/H`, and
second moments give `p E[T^2]=nu+2 rho E[T]`.  Subtracting the square of the
mean simplifies to the printed variance.  The dependence between attempt
duration and failure is retained through `rho`; no false independence step is
present.

### Sharp fixed-mass extrema

For `2<=a<=b`, the outward transfer `(a,b)->(a-1,b+1)` strictly increases
the reciprocal sum by

```text
1/[a(a-1)]-1/[b(b+1)]>0.
```

Thus the mean is minimized only by permutations of the one-long-arm profile.
For `b>=a+2`, the inward transfer strictly decreases the reciprocal sum by

```text
1/[a(a+1)]-1/[b(b-1)]>0,
```

so the mean is maximized only by the balanced multiset.  The denominators in
both printed bounds and both equality classes are correct.

### Coarse-data inverse

The endpoint ratios satisfy `pi_i/pi_j=ell_j/ell_i`; under the stated model
class this recovers the unique gcd-one positive integer representative `d`.
Writing `ell=c d` leaves all endpoint masses unchanged and changes the mean by
the factor `c^2`, giving exactly the displayed recovery equation.  The proof
does not silently infer an unknown topology, transition kernel, or noisy
parameter.

## Edge-case pressure

| case | result |
|---|---|
| one or more arms of length `1` | `P_0=0` correctly removes the impossible return on that arm; first atom is `1/r` |
| all arms of length `1` | `D=r`, `F_i=z/r`, `T=1`, variance `0`; both extremal classes coincide |
| `r=2` | the spider is an absorbing interval; endpoint, mean, variance, parity, and transform reduce correctly to gambler's ruin, which the paper treats as zero credit |
| `L=r` | both equality classes reduce to `(1,...,1)`, as stated |
| `s=0` in `L=qr+s` | the balanced denominator reduces to `r/q` without division or equality ambiguity |
| common dilation | endpoint vector is unchanged and mean scales quadratically |
| `r=1` | deliberately outside the theorem and never used internally; no hidden division requires it |
| zero-length arm | explicitly excluded; this is necessary because the path/continuant construction would otherwise call an undefined negative index |

No counterexample or missing equality case was found in these boundaries.

## Executable, PDF, and package audit

- `sha256sum -c SHA256SUMS`: every listed artifact passes.
- Fresh verifier replay: byte-identical to `verification_output.txt`, SHA-256
  `af9c4bba9094e149b5c070351cad0b48697eb3fd999fc4f8b60e155513242f7c`.
- Frozen totals: 1,360 literal profiles, 190,026 fixed-mass profiles, 37,440
  inverse profiles, and 1,446,432 assertions; final status `PASS`.
- Source-only cold sequence `pdflatex -> bibtex -> pdflatex -> pdflatex`:
  success; output is byte-identical to the package's `main.pdf`.
- Current PDF: 6 A4 pages, 351,762 bytes, SHA-256
  `456480f4472e8b33f9ce4525b71d33af5a78cacd407cd4ca976a3dcbe5b17af7`.
- Bibliography: 5/5 current entries cited and resolved.  Final log has no
  unresolved citation/reference, rerun request, bad box, or multiply-defined
  label.
- Fonts: all 25 reported rows embedded.  Identifying title/author/subject/
  keyword metadata are blank; PDF is unencrypted and has no form or
  JavaScript.
- All six pages were rasterized and inspected.  The theorem, two tables,
  displayed formulas, declarations, and bibliography are legible and inside
  page bounds.
- The source, PDF, transcript, README, ledgers, and build record agree on the
  theorem formulas, six-page count, PDF hash, profile ranges, assertion total,
  and `HOLD_EXTERNAL` status.

## Required repair order and acceptance condition

1. Repair M1 and rerun the owner subtraction against the two omitted primary
   sources.
2. Correct the de la Iglesia--Juarez version-of-record metadata.
3. Either relabel or genuinely separate the one-attempt computational route.
4. Add the one-line formal/analytic bridge.
5. Recompile, replay, visually inspect affected pages, and regenerate all
   hashes and build/source ledgers.

After those repairs, and provided the direct comparison does not reveal the
same unequal-arm continuant closed form in prior work, the manuscript would be
eligible for a second internal review.  This review does not authorize public
posting, circulation, author contact, submission, novelty language, or any
other external action.
