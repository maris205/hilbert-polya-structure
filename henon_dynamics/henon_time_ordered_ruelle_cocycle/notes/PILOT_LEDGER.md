# Pilot ledger

> **Historical target-selection record.** Labels and future-tense statements
> below are frozen as of 2026-08-08.  T1 and T3 are now proved, while T2 is an
> independently checked exact-rational computer-assisted result.  See
> [`../DERIVATION_PACKAGE.md`](../DERIVATION_PACKAGE.md) and
> [`../results/RESULTS.md`](../results/RESULTS.md) for current status.  Pilot
> values are not used as release evidence.

**Purpose:** target selection only
**Freeze date:** 2026-08-08
**Certification status at freeze:** no entry below was then a released C22 theorem

## Evidence labels

- `EXACT_PILOT`: exact within the stated finite computation, but not yet
  reproduced by the Stage-2 independent checker.
- `NUMERICAL_PILOT`: high-precision floating-point result with no rigorous
  interval enclosure.
- `DERIVATION_TO_CERTIFY`: hand/computer-algebra derivation that must be
  rebuilt in the formal producer and checker.
- `THEOREM_CANDIDATE`: plausible general identity, not established here.

## P1 -- common signed-root contraction

**Label:** `DERIVATION_TO_CERTIFY`

For a variable protocol \(a_i\in[59/10,61/10]\), the periodic recurrence can
be written

\[
(T_{\omega,\varepsilon}q)_i
=\varepsilon_i
 \sqrt{\frac{1-q_{i-1}-q_{i+1}}{a_i}}.
\]

On the inherited real sequence box, the candidate uniform sup-norm
contraction constant is

\[
\theta=\sqrt{\frac{240}{1003}}<0.49<\frac12.
\]

The broader strict self-map calculation gives

\[
\frac{144}{25}<a_i<\frac{51}{8},
\]

which contains the frozen interval.  Formal work must specify the exact box,
all radicand margins, and the dependence on neighboring coordinates.

## P2 -- common four-box covering window

**Label:** `DERIVATION_TO_CERTIFY`

Using the inherited inner boundary \(|q|=1/3\), outer boundary
\(|q|=5/8\), and the Paper-5 map convention, direct endpoint inequalities
suggest the common covering graph persists for

\[
\frac{289}{50}<a<\frac{99}{16}.
\]

Both \(59/10\) and \(61/10\) lie strictly inside.  The tight candidate
endpoint margins are

\[
\frac{7}{720}
\quad\text{and}\quad
\frac{3}{64}.
\]

The graph, in state-symbol order \(--,-+,+-,++\), is

\[
A=\begin{pmatrix}
1&0&1&0\\
1&0&0&0\\
0&1&0&1\\
0&1&0&0
\end{pmatrix}.
\]

This is a new switched-family derivation, not an imported certificate from a
fixed-parameter project.

## P3 -- minimal protocol pairs

**Label:** `EXACT_PILOT`

Exhaustive finite enumeration gives:

| Constraint | Minimal length | Pair |
|---|---:|---|
| same Parikh vector, primitive, non-dihedral | 5 | `aaabb`, `aabab` |
| same cyclic bigram counts, primitive, non-dihedral | 7 | `0000101`, `0001001` |
| same cyclic trigram counts, primitive, non-dihedral | 8 | `00101011`, `00101101` |

For the length-seven pair, both cyclic bigram ledgers are

\[
N_{00}=3,\qquad N_{01}=2,\qquad N_{10}=2,\qquad N_{11}=0.
\]

The Stage-2 checker must reproduce minimality without importing the producer's
canonicalization functions.

## P4 -- real multiplier separation

**Label:** `NUMERICAL_PILOT`

Parameters are \(a_0=5.9\), \(a_1=6.1\).  For the all-negative state branch:

| Protocol | Monodromy trace | Instability length |
|---|---:|---:|
| `aaabb` | 18604.9243237984736725 | 9.8311815703639067661 |
| `aabab` | 18604.3646127334614459 | 9.8311514858831609380 |

The length difference is approximately
\(3.00844807458\times10^{-5}\).

For the same-bigram length-seven pair, the strongest scanned admissible state
word was \(++--+--\):

| Protocol | Monodromy trace | Instability length |
|---|---:|---:|
| `0000101` | -74867.860713863704092 | 11.223479981295822075 |
| `0001001` | -73590.339288743760787 | 11.206269036253202574 |

The absolute length separation is approximately

\[
0.017210945042619501039.
\]

This is the predeclared first interval target.  It does **not** pass T2 until
the two branches are certified and all local state cycles above both protocol
necklaces are aggregated.

## P5 -- finite-field chronology witness

**Label:** `EXACT_PILOT`

At \(a_0=59/10\), \(a_1=61/10\), reduction modulo \(43\) gives

\[
a_0\equiv36,\qquad a_1\equiv19\pmod{43}.
\]

For protocol `0000101`, the pilot found a fixed point \((29,23)\) with

\[
\operatorname{tr}M=15,
\quad
\det(I-M)=30,
\quad
\det(I-M)^{-1}=33
\pmod{43}.
\]

For protocol `0001001`, it found a fixed point \((37,27)\) with

\[
\operatorname{tr}M=18,
\quad
\det(I-M)=27,
\quad
\det(I-M)^{-1}=8
\pmod{43}.
\]

This is an exact witness that full ordered map data need not be determined by
cyclic bigram counts.  It neither proves a real survivor statement nor a
difference between complete aggregate trace sums.

## P6 -- unweighted local symbolic control

**Label:** `DERIVATION_TO_CERTIFY`

If the common survivor has full binary base independently over the four-state
graph, its unweighted adjacency is \(J_2\otimes A\).  The candidate control is

\[
\frac{1}{\det(I-z(J_2\otimes A))}
=\frac{1}{1-2z-8z^3-16z^4}.
\]

This factor measures the chosen base extension and local symbolic survivor;
it is not an arithmetic anomaly.

## P7 -- global complex collapse

**Label:** `THEOREM_CANDIDATE`

For every length-\(n\) protocol, the cyclic polynomial equations have
multidegree two in each coordinate, suggesting total scheme length \(2^n\)
with multiplicity.  Summing over the \(2^n\) base words would give bare count
\(4^n\) and formal zeta

\[
(1-4z)^{-1}.
\]

Possible global-residue identities for signed flat weights are recorded in
`EXPERIMENT_PLAN.md`.  They remain unproved.  Points at infinity,
degeneracies, and the difference between the full complex scheme and the
local real survivor must be handled before any theorem label is assigned.

## P8 -- periodic block collapse

**Label:** `THEOREM_CANDIDATE`

For a periodic word of length \(m\), let \(\mathcal B_w\) be the block-cyclic
one-step operator and \(\mathcal M_w\) the chronological period monodromy.
Under nuclear/trace-class hypotheses, the expected identities are

\[
\operatorname{Tr}(\mathcal B_w^k)=0\quad(m\nmid k),
\]

\[
\operatorname{Tr}(\mathcal B_w^{mr})
=m\operatorname{Tr}(\mathcal M_w^r),
\qquad
\det(I-z\mathcal B_w)=\det(I-z^m\mathcal M_w).
\]

These identities explain why a Floquet block is a diagnostic sector and not
the global C22 object.  They may be stated as operator theorems only after the
relevant trace hypotheses are proved.
