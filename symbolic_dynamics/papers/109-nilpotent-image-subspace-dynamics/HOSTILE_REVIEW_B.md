# Independent cross-hostile review B — P109

Audit date: 2026-08-29 UTC.  This is a team-internal independent audit, not
an external referee report.  The reviewer did not author P109.  No novelty,
priority, submission, or release endorsement is implied.

Verdict: **GO_INTERNAL / HOLD_EXTERNAL**.  CRITICAL: 0.  Mathematical MAJOR:
0.  Repaired owner/scope MAJOR: 1.  Repaired MINOR: 2.

## Independent theorem reconstruction

### Iterates and pointed fibres

Write `K_t=ker N^t` and `I_t=im N^t`, so for `0<=t<=d` their dimensions are
`t` and `d-t`.  Images respect composition, hence `T^t(U)=N^t(U)`.  If an
`r`-space `U` maps onto an `s`-space `W<=I_t`, rank--nullity forces

```text
dim(U intersect K_t)=r-s=:k.
```

The fibre is empty when `k<0` or `k>t`, in agreement with the zero convention
for the Gaussian coefficient.  Otherwise choose the kernel intersection
`R<=K_t` in `[t choose k]_q` ways.  The restricted preimage
`E=(N^t)^(-1)(W)` fits into

```text
0 -> K_t -> E -> W -> 0.
```

After choosing a linear section and a complement of `R` in `K_t`, every
admissible `U` is uniquely the graph of a map `W -> K_t/R`.  There are
`q^(s(t-k))=q^(s(t-r+s))` such maps.  This reconstructs the pointed formula

```text
#{U in Gr(r,V): N^t(U)=W}
  = [t choose r-s]_q q^(s(t-r+s)).
```

There are `[d-t choose s]_q` targets `W<=I_t`; multiplication gives the joint
rank transition.  Summing the pointed formula over `r=s+k` gives the stated
iterated indegree.  At `t=1` the two terms are exactly `q^s` and `1`.

### Independent recurrence route

For a fixed `t`-space `K`, let `C(d,t;r,k)` count `r`-spaces meeting `K` in
dimension `k`.  Slice by a hyperplane `H` containing `K`.  Spaces contained
in `H` contribute `C(d-1,t;r,k)`.  Every other space meets `H` in an
`(r-1)`-space `U_0` with the same intersection with `K`; the possible
extension lines are the lines of `V/U_0` outside `H/U_0`, whose number is

```text
[d-r+1 choose 1]_q - [d-r choose 1]_q = q^(d-r).
```

Thus

```text
C(d,t;r,k)=C(d-1,t;r,k)+q^(d-r) C(d-1,t;r-1,k).
```

Gaussian Pascal verifies independently that its solution is

```text
[t choose k]_q [d-t choose r-k]_q q^((t-k)(r-k)).
```

Putting `k=r-s` recovers the joint transition without using the pointed graph
parametrization.

### Absorption, periodic points, and rigidity

The condition `T^t(U)=0` is equivalent to `U<=K_t`.  Therefore the absorption
CDF is `G_min(t,d)(q)` and its successive differences give the exact depth
layers.  A line through a cyclic top vector has depth `d`, so the upper bound
is sharp.

If `T^n(U)=U`, then iterating gives `N^(mn)U=U` for every `m`; choosing
`mn>=d` forces `U=0`.  Hence every positive iterate has one fixed point and
the formal Artin--Mazur zeta function is `(1-z)^(-1)`.  A dynamical conjugacy
preserves the depth census.  Its last nonempty layer recovers `d`, and for
`d>=2` the time-two CDF is `G_2(q)=q+3`, recovering `q`.  At `d=1`, all
fields give exactly the same two-state map, so the stated collapse is both
real and exhaustive.

## Findings and implemented repairs

### MAJOR (owner/scope) — direct subspace-profile owners were omitted

The earlier draft cited Gaussian enumeration and invariant-subspace lattices,
but not the closer literature that enumerates subspaces by their dimension
sequence relative to a linear operator.  The paper, README, claims ledger,
and bibliography now explicitly subtract:

- Edward A. Bender, Raymond Coley, David P. Robbins, and Howard Rumsey, Jr.,
  *Enumeration of subspaces by dimension sequence*, JCTA 59 (1992), DOI
  [`10.1016/0097-3165(92)90093-A`](https://doi.org/10.1016/0097-3165(92)90093-A);
- Samrith Ram, *Subspace profiles over finite fields and q-Whittaker
  expansions of symmetric functions*, Forum of Mathematics, Sigma 14
  (2026), e48, DOI
  [`10.1017/fms.2026.10193`](https://doi.org/10.1017/fms.2026.10193).

Those sources own dimension-sequence/subspace-profile enumeration, including
the regular-nilpotent profile setting.  P109 assigns no credit to those
counts or to invariant-subspace classification.  Its residual bounded object
is only the conjunction of pointed fibres `N^tU=W`, local functional-graph
counts, absorption, periodic census, and dynamical recovery.  A bounded owner
search is not a novelty certificate; external circulation remains HOLD.

### MINOR — the graph proof skipped impossible kernel dimensions

The displayed Gaussian formula already vanishes when `r-s<0` or `r-s>t`, but
the prose immediately entered the graph parametrization.  The proof now
separates those empty cases before assuming `0<=r-s<=t`, closing the
quantifier-level gap without changing the theorem or control count.

### MINOR — BibTeX parsed the junior suffix incorrectly

The initial owner repair rendered the fourth author as “Jr. Rumsey, Howard.”
The BibTeX name was changed to `Rumsey, Jr., Howard`; the rebuilt reference
now reads “Howard Rumsey, Jr.”  No mathematical content changed.

## Endpoint and collision attacks

- `t=0`: `K_0=0`; the fibre is one exactly when `U=W`, and the formula
  reduces to the identity transition.
- `t=d`: `I_d=0`; only `W=0` is admissible and the fibre formula returns all
  `[d choose r]_q` input spaces.
- `r<s` or `r-s>t`: the fibre is empty and the invalid Gaussian coefficient
  is zero; this case is now explicit in the proof.
- `W` outside `I_t`: no preimage exists, since every `N^t(U)` lies in `I_t`.
- `d=1`: the recovery theorem does not claim to determine `q`; every field
  genuinely yields the same two-vertex absorbing map.
- Prime-power fields: the theorem is not restricted to prime `q`; the
  literal controls include `F_4`, `F_8`, `F_9`, and `F_16`.

The P1--P106 firewall was rechecked against P73, P99, and P103.  P73 evolves
symbolic substitution discrepancies, P99 applies an invertible shear to
fixed-index integer sublattices, and P103 applies double adjugation to full
matrix space.  P109 instead applies a noninvertible image map to every
finite-field subspace and studies pointed transient fibres.  Shared linear
algebra, Gaussian coefficients, or zeta bookkeeping receives no credit.

## Fresh exact control and stored-output audit

On the final repaired tree I ran

```text
python3 code/verify.py > /tmp/p109-review-b-fresh.txt
diff -u code/verification_output.txt /tmp/p109-review-b-fresh.txt
```

The diff was empty.  The final line is:

```text
PASS: 515,379 exact assertions
```

Across 28 complete RREF lanes, the script materializes all subspaces, applies
the Jordan shift to their vectors, and checks phase sizes, iterates, every
pointed fibre and joint rank cell, depths and CDFs, periods, one-step
indegrees, and the rigidity signature.  The extension-field lanes use
explicit polynomial-basis arithmetic over `F_4`, `F_8`, `F_9`, and `F_16`.
This finite computation does not call either analytic proof and does not
prove a quantified all-parameter statement.

## Four-stage build and PDF inspection

After the repairs I ran `pdflatex -> bibtex -> pdflatex -> pdflatex` from the
paper directory.  The result is:

- 5 A4 pages, 302,089 bytes, PDF 1.5;
- zero undefined citations or references, LaTeX/package/pdfTeX warnings,
  BibTeX warnings, multiply defined labels, and overfull/underfull boxes;
- all 22 font entries embedded, subsetted, and Unicode-mapped;
- 17,773 extracted-text bytes in 267 lines, with no unresolved sentinels;
- all five pages rendered and visually checked, including the repaired
  author suffix: no clipping, overlap, malformed formula, or orphan material.

## Disposition

- Exact fibres, transition laws, absorption, periodic census, and recovery:
  **GO_INTERNAL**.
- Literal control and stored finite evidence: **GO_INTERNAL**.
- Owner language after direct-profile subtraction: adequate for internal use.
- External circulation, public posting, specialist contact, novelty, and
  priority language: **HOLD_EXTERNAL** pending specialist owner review and
  later final QA/freeze.
