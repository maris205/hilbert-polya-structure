# Independent hostile review A — P108

Review date: 2026-08-29 UTC.  Scope: `main.tex`, bibliography, README and
evidence/control/build records, the exact verifier and stored stdout, and a
fresh four-stage PDF build.  This is not final QA.  External release remains
**HOLD**.

## Verdict and severity

**GO_INTERNAL / HOLD_EXTERNAL.**  The complete theorem package is
**PROVABLE AS STATED**.

- **CRITICAL: 0.**
- **MAJOR: 0.**
- **MINOR: 1, repaired.**  The paper had no explicit P1--P106 collision
  paragraph even though Fibonacci/cap vocabulary overlaps three occupied
  systems.  I added a system-level firewall to `main.tex`, `README.md`, and
  `CLAIMS_EVIDENCE.md`: P83 is a countable Catalan renewal shift, P89 is an
  iid reset/golden-mean matrix product, and P101 is a random cap--floor
  composition on an interval.  P108 is instead one deterministic saturated
  second-order update on a finite integer square.

## Proof reconstruction

### Exact iterate

The identity

```text
min(a, min(a,u)+min(a,v)) = min(a,u+v),  u,v>=0,
```

is valid in every clipping regime.  If the two uncapped forms at time `t`
are

```text
U=F_(t-1)x+F_t y,    V=F_t x+F_(t+1)y,
```

one update is `(min(a,V), min(a,U+V))`.  The two Fibonacci recurrences in
the coefficients give exactly the asserted time-`t+1` pair.  The base case
`t=1` is the defining map, so intermediate saturation causes no loss.

### Recurrence and depth census

The fixed equations force `x=y` and `y=min(a,2y)`, hence only `(0,0)` and
`(a,a)`.  Every other integer state has at least one positive coordinate,
so both Fibonacci forms eventually cross the positive cap; consequently no
other cycle exists and every nonzero state reaches `(a,a)`.

For `t>=1`, the second uncapped form dominates the first coefficientwise.
Thus a nonfixed state reaches `(a,a)` at exactly the first time

```text
F_(t-1)x+F_t y >= a.
```

At positive time the recurrent states consist of `(0,0)` plus this
half-plane, which explains the otherwise easy-to-miss leading `1` in the
CDF.  Since `F_t>=F_(t-1)`, every nonzero state crosses no later than the
first `t` with `F_(t-1)>=a`; `(1,0)` realizes equality.  Therefore

```text
D_a = 1 + min{k>=0 : F_k>=a}.
```

The endpoint `a=1` was checked separately: the repeated values
`F_1=F_2=1` give `D_1=2`, as the orbit `(1,0)->(0,1)->(1,1)` requires.
The manuscript's refined staircase wording is correct: plateau endpoints
are Fibonacci caps, and a jump occurs when the integer cap passes one.

For the lattice-point sum, `v_t=F_t>=1`, so division is safe.  The lower
bound `max(0,ceil((a-u_t x)/v_t))` never exceeds `a`; hence no missing outer
truncation is needed.  Successive CDF differences give every exact layer.

### Image and fibres

Solving `T_a(x,y)=(u,v)` first gives `y=u`.  If `v<a`, then
`x=v-u` is the unique solution and exists exactly when `u<=v`.  If `v=a`,
then `a-u<=x<=a`, giving `u+1` solutions.  Hence the image is exactly the
upper triangular half-square; the lower triangle has
`a(a+1)/2` Garden-of-Eden states, and the fibre sum returns `(a+1)^2`.
This inverse derivation does not use the Fibonacci iterate.

## Ownership and collision attack

Publisher records confirm the Koshy and Miles Fibonacci sources and the
Hmamed--Mesquine--Tadeo--Benhayoun--Benzaouia saturated-systems citation.
Targeted searches for the exact map `(x,y)->(y,min(a,x+y))`, capped
Fibonacci dynamics, and saturated Fibonacci recurrences did not identify a
direct theorem-package owner.  This negative result is not a novelty or
priority certificate.  Classical Fibonacci identities, Binet estimates,
saturation algebra, and Artin--Mazur zeta receive zero credit, leaving only
the exact finite portrait as the bounded residual claim.

The historical collision audit was performed against P83, P89, and P101
and is now explicit in the package.  Their phase spaces, randomness, and
updates differ at the system level rather than merely by parameters.

## Exact-control replay

I ran

```text
python3 code/verify_capped_fibonacci.py > /tmp/p108-fresh.txt
diff -u code/verification_output.txt /tmp/p108-fresh.txt
```

The diff was empty.  The replay passed **67,475,970 exact assertions** over
all 3,622,410 states for caps `1..220`, including 60,226,906 iterate-formula
checks and 3,622,410 fibre checks.  Python syntax checking passed.  The
literal update and reverse fibre table are convention-sensitive finite
controls, not extrapolative proofs.

## Build and visual replay

After the collision repair I ran the full sequence
`pdflatex -> bibtex -> pdflatex -> pdflatex`.  The final artifact has:

- 3 A4 pages, 269,727 bytes, PDF 1.5;
- zero undefined citations or references;
- zero LaTeX/package/pdfTeX or BibTeX warnings;
- zero overfull or underfull boxes and no unresolved sentinels;
- all 21 font entries embedded, subsetted, and Unicode-mapped;
- 10,135 extracted bytes under `pdftotext -layout`;
- all three pages visually inspected with no clipping, overlap, malformed
  formula, or orphan bibliography material.

## Residual risks

1. The theorem package is elementary once the saturation identity is seen;
   contribution density and an undiscovered saturated-recurrence owner are
   the main external risks.
2. The logarithmic depth asymptotic and Fibonacci plateau description add
   no separate novelty beyond the exact threshold formula.
3. No public release, submission, specialist contact, novelty, or priority
   conclusion is authorized.

Final decision: **GO_INTERNAL / HOLD_EXTERNAL**.
