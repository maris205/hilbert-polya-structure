# Source lock

## Candidate identity

- Proposed candidate: `SD-C45`
- Historical parent: `SD-C02`
- Family: symbolic dynamics
- Stage: Phase-1 preauthority research inputs
- Portable namespace: `papers/43-squarefree-factor-periodic-rigidity/preauthority`

## Frozen source object

Let \(\mathbb P\) be the rational primes and define

\[
X_{\rm sf}=\left\{x\in\{0,1\}^{\mathbb Z}:
\operatorname{supp}(x)\bmod p^2
\ne \mathbb Z/p^2\mathbb Z\quad\forall p\in\mathbb P\right\}.
\]

The dynamics is the two-sided left shift
\((\sigma x)_j=x_{j+1}\). The roof is one, the potential is zero, and the
cocycle is trivial. The source function space inherited from C02 is the
locally constant cylinder algebra.

All rational-prime-square exclusions are explicit grammar inputs. This is a
frozen modeling choice and remains an A0 failure under strict emergence.

No finite subset is an equivalent source. If \(P_0\subset\mathbb P\) is
finite, set

\[
Q=\prod_{p\in P_0}p^2,
\qquad
x_n=\mathbf 1_{\{n\equiv1\pmod Q\}}.
\]

Then \(x\) is nonzero and \(Q\)-periodic, while for every \(p\in P_0\) its
support modulo \(p^2\) is the singleton residue one. Thus every finite
prime-square approximation admits a nonzero periodic point and fails the
full source's periodic-collapse and proximality conclusions.

## Frozen factor category

A lawful target is a compact metrizable space \(Y\) with a homeomorphism
\(S:Y\to Y\). A lawful factor map is a continuous surjection
\(\pi:X_{\rm sf}\to Y\) satisfying

\[
\pi\circ\sigma^n=S^n\circ\pi
\qquad\text{for every }n\in\mathbb Z.
\]

The theorem quantifies over every such \((Y,S,\pi)\). It does not require a
finite alphabet, expansivity, a finite sliding-block radius, finite fibers,
soficity, or a symbolic presentation of \(Y\).

## Primitive, repetition, and marker lock

- Source/target primitive type: a periodic orbit of least period \(n\).
- Repetition: the \(r\)-fold traversal of the same primitive orbit.
- Clock: one unit per application of the homeomorphism.
- Marker: \(z\) records one unit of this frozen discrete time.
- Sole primitive factor after the theorem: the fixed orbit of
  \(y_0=\pi(0^{\mathbb Z})\), with primitive monomial \(z\).
- Its \(r\)-fold traversal contributes \(z^r\) in the logarithm; it is not a
  new primitive atom.

## Determinant lock

For every lawful factor, fixed-point counts are finite and the convention is

\[
\zeta_{\rm AM,Y}(z)
=\exp\left(\sum_{m\ge1}\frac{\#\operatorname{Fix}(S^m)}{m}z^m\right),
\qquad
D_{\rm AM,Y}(z)=\zeta_{\rm AM,Y}(z)^{-1}.
\]

The theorem gives \(D_{\rm AM,Y}(z)=1-z\). The one-dimensional periodic-core
operator \(K_{\rm per}=I_{\mathbb C}\) realizes
\(\det(I-zK_{\rm per})=1-z\) and
\(\operatorname{tr}(K_{\rm per}^m)=1\). This is only a ledger realization. It
is not declared to be a Ruelle operator on \(X_{\rm sf}\), a transfer operator
on \(C(Y)\), or a Hilbert--Polya operator.

## Rational-prime comparator firewall

The separately owned rational-prime primitive type is `RationalPrimeAtom`.
Its optional comparison marker is \(u\), not \(z\), and its formal marked
Euler product is

\[
\prod_{p\in\mathbb P}(1-u p^{-s})^{-1}.
\]

No equality with the factor determinant is asserted. The factor ledger has
one primitive atom; the rational-prime ledger has infinitely many. Traversals
\(z^r\) cannot be retyped as distinct primes without changing primitive type,
marker ownership, and repetition law.

## Allowed evidence

- immutable C02, C03, and C05 Session-4 cards;
- the C02 source definition, source-only proof, and exact fixed-point census;
- exact modular arithmetic and the Chinese remainder theorem;
- compact topological dynamics and uniform continuity;
- primary squarefree, \(\mathscr B\)-free, proximality, factor, and
  Artin--Mazur literature;
- sealed P39--P42 material only for collision, chronology, and integrity.

## Forbidden evidence and moves

- Riemann-zero data, fitting, validation, or target-driven parameters;
- a prime table used to construct a new candidate;
- treating P39, P40, P41, or P42 as a ranking or authorization source;
- claiming the retrospective selector was prospective or outcome independent;
- replacing all prime-square exclusions by a finite subset without declaring
  a changed source;
- importing cycles through a product or extension and calling them factors of
  the original source;
- using a noncontinuous, nononto, or nonequivariant observation as a factor;
- switching from Artin--Mazur counts to aperiodic statistics under the same
  source lock;
- calling \(K_{\rm per}\) a full-state transfer or spectral operator;
- claiming external novelty for known proximality or elementary factor
  permanence.

## Exact claim boundary

The strongest authorized scientific statement is:

> Every continuous surjective equivariant compact metrizable
> \(\mathbb Z\)-factor of the frozen squarefree admissible shift has exactly
> one periodic point and hence inverse Artin--Mazur determinant \(1-z\).

No universal theorem for arbitrary aperiodic systems, arbitrary
\(\mathscr B\)-free systems, extensions, changed observables, or completed
arithmetic zeta functions is included.
