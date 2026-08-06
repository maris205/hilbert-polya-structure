# Chronological dyadic-solenoid cocycles

**Candidate:** HCS-C14  
**Research status:** proved arithmetic-dynamics theorem package  
**Hilbert--Pólya status:** Route-A rejected

## Main outcome

This project changes dynamical form after the Hénon and Fibonacci lanes.  It
retains the source Hénon program's demand for invertible, conservative
dynamics, but it does **not** derive a new Hénon map or quantize the old one.
The smooth real-plane system is replaced by an autonomous chronological skew
product whose fibre is the dyadic two-solenoid

\[
X_2=\widehat{\mathbb Z[1/2]^2}.
\]

Let

\[
A=\begin{pmatrix}3&1\\1&3\end{pmatrix},\qquad
B=\begin{pmatrix}3&2\\2&4\end{pmatrix},
\qquad \det A=\det B=8.
\]

The matrices are not area-preserving on \(\mathbb R^2\).  Because \(8\) is
a unit of \(\mathbb Z[1/2]\), however, their dual maps are genuine
compact-group automorphisms of \(X_2\) and preserve Haar measure.  Define

\[
F(\omega,x)=\bigl(\sigma\omega,\alpha_{M_{\omega_0}}x\bigr),
\qquad M_a=A,\quad M_b=B,
\]

on the two-sided full shift times \(X_2\).  The convention
\(\alpha_M=\widehat{M^{\mathsf T}}\) makes a word
\(w=w_0\cdots w_{n-1}\) carry the chronological return

\[
M_w=M_{w_{n-1}}\cdots M_{w_0}.
\]

Every return matrix is uniformly expanding at the archimedean place.  If

\[
D_w=\det(I-M_w)=8^n-\operatorname{tr}(M_w)+1,
\]

then \(D_w>0\), and localization of Smith normal form gives the intrinsic
fibre count

\[
\#\operatorname{Fix}(\alpha_{M_w})
=|D_w|_\infty|D_w|_2
=\frac{D_w}{2^{\nu_2(D_w)}}
=\operatorname{oddpart}(D_w).
\]

No prime table, zero table, or fitted spectral parameter is used.

## Four exact results

### 1. The archimedean comparison collapses rationally

After every ordered product has been evaluated,

\[
N_n^{(\infty)}
=\sum_{|w|=n}D_w
=2^n+16^n-\operatorname{tr}\bigl((A+B)^n\bigr).
\]

Since
\(A+B=\left(\begin{smallmatrix}6&3\\3&7\end{smallmatrix}\right)\),

\[
Z_\infty(z)
=\frac{1-13z+33z^2}{(1-2z)(1-16z)}.
\]

This exact post-summation identity is not an averaged dynamical evolution.

### 2. The first dyadic correction is a cyclic symbolic language

Modulo two,

\[
\bar A=\begin{pmatrix}1&1\\1&1\end{pmatrix},\qquad
\bar B=\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad
\bar A^2=0.
\]

For a based cyclic word,

\[
2\mid D_w
\quad\Longleftrightarrow\quad
w\text{ has no cyclic occurrence of }\texttt{aa}.
\]

The active length-\(n\) words form the cyclic golden-mean language and are
counted by the Lucas number \(L_n\).  Higher conditions
\(2^k\mid D_w\) are recognized by chronological multiplication modulo
\(2^k\).  Each fixed \(k\) gives a finite monoid recurrence, while

\[
\operatorname{oddpart}(d)
=d\left(1-\sum_{k\ge1}2^{-k}\mathbf1_{2^k\mid d}\right)
\]

organizes the exact weight as a coefficientwise finite congruence tower.  No
single finite-state or trace-class operator for the full tower is claimed.

### 3. Chronology changes a primitive base sector's analytic type

The primitive period-five words

\[
w_0=\texttt{aabbb},\qquad w_1=\texttt{ababb}
\]

have the same Parikh vector \((2,3)\) and are not cyclic or dihedral copies.
Nevertheless,

\[
M_{w_0}=\begin{pmatrix}1162&1222\\1468&1572\end{pmatrix},
\quad \operatorname{tr}M_{w_0}=2734,
\quad D_{w_0}=30035,
\]

whereas

\[
M_{w_1}=\begin{pmatrix}1133&1247\\1422&1594\end{pmatrix},
\quad \operatorname{tr}M_{w_1}=2727,
\quad D_{w_1}=30042=2\cdot15021.
\]

The first return has rational fibre zeta

\[
Z_{[w_0]}(z)=
\frac{1-2734z^5+32768z^{10}}
{(1-z^5)(1-32768z^5)}.
\]

The second return has a \(2\)-adic unit, or isometric, eigenvalue direction.
Bell--Miles--Ward's theorem applies to this single return automorphism and
gives a natural boundary at \(|z|=1/8\) in the base clock.  Its exact
repetition valuations are

\[
\nu_2\det(I-M_{w_1}^r)=
\begin{cases}
1,&r\text{ odd},\\
3+\nu_2(r),&r\text{ even}.
\end{cases}
\]

Thus abelianized symbol incidence cannot recover orbit-resolved analytic type.

### 4. The full zeta crosses its first convergence circle

Let

\[
N_n^{(2)}=\sum_{|w|=n}\operatorname{oddpart}(D_w),\qquad
\Delta_n=N_n^{(\infty)}-N_n^{(2)}.
\]

For \(\varphi=(1+\sqrt5)/2\), exact upper and lower bounds give

\[
\lim_{n\to\infty}\Delta_n^{1/n}=8\varphi.
\]

Consequently

\[
Z_2(z)=Z_\infty(z)
\exp\left(-\sum_{n\ge1}\frac{\Delta_n}{n}z^n\right)
\]

extends meromorphically to

\[
|z|<(8\varphi)^{-1}>1/16.
\]

In this disk it has exactly one simple pole, at \(z=1/16\), and no zeros.
Equivalently, \((1-16z)Z_2(z)\) is holomorphic and nowhere zero throughout
the disk.  The behavior at the secondary circle
\(|z|=(8\varphi)^{-1}\) remains open.  Individual natural-boundary factors
do not by themselves determine the boundary of the full infinite product.

## Primitive base-sector factorization

For a primitive base necklace \([w]\) of length \(\ell\), the correct
repetition weight is \(\#\operatorname{Fix}(\alpha_{M_w}^r)\), not a power
of the first-return count.  Accounting for its \(\ell\) base phases gives

\[
Z_F(z)=
\prod_{[w]\ \mathrm{primitive\ base}}
\zeta_{\alpha_{M_w}}\!\left(z^{|w|}\right)
\]

as a formal identity and analytically in the initial convergence disk.  This
is a complete decomposition into primitive **base sectors**; each fibre zeta
still contains its own primitive fibre orbits.

## Route-A ruling

The system has an exact arithmetic weight, a chronology-preserving
base-sector factorization, and a congruence transfer tower.  Its clocks are the
lattice scales \(16\), \(8\varphi\), and \(8\), not \(\log p\).  It has no
Riemann divisor, functional equation, Gamma factor, or discrete self-adjoint
spectral realization.

The scoped Route-A tuple is

```text
(A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)
```

with overall decision `ROUTE_A_REJECTED` as a Hilbert--Pólya candidate and
`PROVED_STRUCTURAL_RESULT` as an arithmetic-dynamics project.  Route B is not
authorized.

## Reproduction

From this directory:

```bash
python code/solenoid_zeta.py --max-period 20 --parity-period 12 --tower-level 8
python code/independent_check.py --max-period 12
python code/test_solenoid_zeta.py -v
```

The producer enumerates all \(2{,}097{,}150\) based words through period 20.
The independent checker does not import the producer; version 2 also
cross-checks all 20 Dold/zeta rows, all 20 valuation reconstructions, and all
96 persisted congruence rows.

## Directory guide

- `paper/`: manuscript, PDF, and compilation report;
- `code/`: exact producer, independent implementation, and tests;
- `results/`: certificates, exact tables, independent report, and hashes;
- `evaluations/route_a/`: append-only formal Route-A record;
- `DERIVATION_PACKAGE.md`: theorem proofs and claim boundaries;
- `SOURCE_AUDIT.md`: primary-source and scoped novelty audit;
- `PAPER_PLAN.md`: claims--evidence and manuscript plan;
- `IDEA_REPORT.md`: breadth-first candidate decision;
- `EXPERIMENT_PLAN.md`: frozen claims, controls, and kill criteria.
