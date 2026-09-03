# P178 claims–evidence ledger

**Proof status:** `PROVABLE AS STATED`  
**Round:** Round 2 dual-review freeze  
**External state:** `OWNER_THIN / HOLD_EXTERNAL`  
**Evidence rule:** enumeration is falsification pressure; the all-prime
argument in `main.tex` is the proof.

## Dependency map

1. The theorem depends on the binomial-basis description of the cyclic
   difference \(N=\tau_1-I\).
2. Every inverse formula depends on the factorization
   \(D_a=N U_a(N)\) for \(a\ne0\), followed by the anchored-lift lemma.
3. The image tower follows from those unique lifts; it is not inferred from
   finite data.
4. Depth shells are consecutive differences of the proved cumulative zero
   fibres.
5. The Jordan inventory depends on the proved image sizes and a rank-one
   recurrent/nilpotent splitting of the deterministic transition operator.

## C1 — difference flag

\[
J^t=N^t\mathcal V_p
=\operatorname{span}\{e_0,\ldots,e_{p-1-t}\},
\qquad \dim J^t=p-t.
\]

- **Proof:** \(e_j(x)=\binom{x}{j}\) is a basis and
  \(Ne_j=e_{j-1}\).
- **Paper:** equations (8)–(9).
- **Exact control:** full modular ranks and Pascal ladders for
  \(p=2,3,5,7,11,13,17,19\).
- **Credit boundary:** the flag and finite-difference nilpotence are
  classical background.

## C2 — nonzero-direction layer map and anchored lift

For \(a\in\mathbb F_p^\times\),

\[
D_a=N U_a(N),\qquad U_a(0)=a,
\]

so \(D_a:J^i\to J^{i+1}\) is onto with constant kernel. Adding
\(f(0)=b\) selects one solution for every \(b\in\mathbb F_p\).

- **Proof:** a polynomial in a nilpotent operator with nonzero constant term
  is invertible; evaluation at zero maps the constant kernel bijectively to
  \(\mathbb F_p\).
- **Paper:** Lemma 2.
- **Exact control:** layer rank and augmented anchor rank for every nonzero
  direction and every layer through \(p=19\).
- **Fragile point checked:** the domain is \(J^i\), not the whole
  \(\mathcal V_p\); constants lie in each \(J^i\) for \(i<p\).

## C3 — every-time image and fibre atlas

For \(0\le t\le p\),

\[
\operatorname{im}T^t=J^t,\qquad |\operatorname{im}T^t|=p^{p-t}.
\]

For \(1\le t\le p\), each nonzero target in \(J^t\) has
\((p-1)^t\) sources; the zero fibre has

\[
p^p-(p^{p-t}-1)(p-1)^t
\]

sources.

- **Proof:** each nonzero direction word gives exactly one anchored backward
  history; forward histories recover their word. The zero count is the
  remaining source mass.
- **Paper:** Theorem 1(i)–(ii), equations (2)–(3) and (10).
- **Exact control:** every literal source, every codomain target, and each
  time \(0,\ldots,p\) for \(p=2,3,5\).
- **Boundary:** at \(t=p\), \(J^p=0\); for \(t>p\), all states remain at
  zero.

## C4 — sharp rooted functional graph

Zero is the unique recurrent state, the maximum depth is \(p\), and

\[
A_0=1,\qquad
A_d=(p-1)^{d-1}(p^{p-d}+p-2),\quad 1\le d\le p.
\]

- **Proof:** \(T^p=0\); the binomial witness
  \(f_\star=\sum_{j=0}^{p-1}e_j\) selects direction one for \(p\) steps;
  exact depths are consecutive cumulative-fibre differences.
- **Paper:** Theorem 1(iii), Section 3.
- **Exact control:** all source depths, the witness direction trace, and all
  target indegrees for \(p=2,3,5\).
- **Small boundary:** \(p=2\) gives image sizes \(4,2,1\) and depth layers
  \(1,2,1\).

## C5 — characteristic polynomial and complete Jordan inventory

\[
\chi_P(\lambda)=(\lambda-1)\lambda^{p^p-1},
\]

\[
m_s=(p-1)^2p^{p-s-1}\quad(s<p),\qquad m_p=p-1.
\]

- **Proof:** \(E=P^p\) is a rank-one idempotent. On \(\ker E\), the
  nilpotent restriction has ranks \(r_t=p^{p-t}-1\). Exact block counts are
  the second differences \(r_{s-1}-2r_s+r_{s+1}\), with
  \(m_p=r_{p-1}\).
- **Paper:** Theorem 1(iv), equations (6)–(7) and (11).
- **Exact control:** dimension and rank-sequence reconstruction for every
  checked prime.
- **Credit boundary:** the rank-to-Jordan conversion is explicitly generic
  and receives no mechanism credit.

## C6 — ownership and scope

- Aichinger–Moosbauer directly delimit translation differences,
  augmentation ideals, and functional-degree nilpotence.
- Hernández Toledo delimits fixed linear finite dynamical systems and their
  nilpotent decomposition.
- Internal A05 owns the fixed cyclic-difference candidate.
- Internal P164 owns a nonlinear front followed by a fixed cyclic
  finite-difference tail.
- The residual is only the repeated state-selected direction plus its
  observable word and uniquely anchored inverse lift.
- Exact-literal search nonhits are recorded as `OWNER_THIN`, never as
  novelty or clearance.

## Computational certificate

- Program: `verify_p178.py`.
- Imports: Python standard library only.
- Exhaustive literal boxes: \(p=2,3,5\).
- Modular proof-pressure boxes:
  \(p=2,3,5,7,11,13,17,19\).
- Literal arrows: 3,156.
- Assertions: 44,689.
- Canonical edge digest:
  `35a2ac173151700d2840526791cd3d2c743f4660f1075bea7e924cfd12de1a89`.
