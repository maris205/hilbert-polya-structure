# Source Lock — All-Radix Carry-Free Operator

## Candidate identity

- Candidate: SD-C50
- Paper position: Paper 48
- Portable namespace: papers/48-all-radix-carry-free-schatten/preauthority
- Phase-2 parent seal:
  d035310ac046981abe7a37a033b1354e3d8da3f53f33d631786ed80f40b90181

## Frozen relation

Fix an integer radix \(b\ge2\). Write positive integers in their ordinary
finite base-\(b\) expansion. Two vertices are adjacent exactly when each
digit sum is strictly less than \(b\); equivalently, their addition has no
carry.

For prime \(b=p\), Kummer supplies the comparator

$$
p\nmid\binom{m+n}{m}
\iff m+n\text{ is carry-free in base }p.
$$

This binomial statement is a corollary/control, not the definition and not an
all-composite-radix assertion.

## Frozen symbolic object

The source is the one-sided countable edge shift of this symmetric graph.
A primitive is a least-period cyclic vertex word. One edge is one unit of
time and \(z\) is the free edge marker.

For \(b=2\) there are no loops. For \(b>2\), loops exist. The positive
vertex set excludes zero throughout; zero-completed finite matrices are
controls only.

## Frozen operator

$$
B_{b,s}(m,n)
=\mathbf 1_{\{\text{no base-}b\text{ carry}\}}(mn)^{-s/2}
$$

acts on \(\ell^2(\mathbb N)\). Complex powers use the real logarithm.

## Digit matrix

$$
C_b=(\mathbf 1_{\{a+c<b\}})_{0\le a,c<b}.
$$

Its finite singular values and Schatten norms are prior-controlled inputs to
the infinite shell theorem. Put

$$
\kappa_{b,q}=\|C_b\|_{S_q},\quad
\tau_b=\kappa_{b,1},\quad
\alpha_b=\log_b\tau_b.
$$

## Internal ownership lock

Paper 26 SOURCE_LOCK.md, SHA-256
749e61a4e99ee55839928046a7114ea62ba0726a041d0e3bf971729f6fbf54ab,
owns the supplied pure-power inventory mechanism. Here \(b^j\) is only a
digit-position support witness, not a rational-prime atom or temporal
repetition. Paper 30 SOURCE_LOCK.md, SHA-256
6a09c46e9c04326728cd838deb654e69529fc661cdb616e255fdb10910b5957e,
owns the free-UFD/divisibility indistinguishability firewall. No
divisibility or free-UFD selectivity is claimed. Randomized digit masks and
all finite mask/tensor calculations are zero-credit controls.

## Determinant and trace convention

- \(\det_2(I-zB_{b,s})\) is legal for \(\Re s>1\);
- the ordinary determinant and trace are legal for
  \(\Re s>\alpha_b\);
- the trace is the positive-vertex digit-restricted Dirichlet series, with
  structural vanishing only in radix two and no complex zero-free claim;
- no unweighted Artin–Mazur zeta is asserted.

## Forbidden moves

- include vertex zero in the infinite source;
- use a finite zero-completed census as novelty;
- apply Kummer's prime-base equivalence to arbitrary composite \(b\);
- omit equality from the \(S_q\) threshold;
- use the odd-radix same-shell proof at \(b=2\);
- split the binary instance into a second paper;
- replace the positive-vertex trace by a finite Lucas census;
- infer infinite ideal membership from cutoff singular values;
- claim rational-prime or target-zero emergence.

## Exact claim boundary

The strongest authorized theorem is the all-radix finite-\(q\) Schatten
surface, separate bounded/compact statement, exact equality rejection,
trace-class exponent \(\alpha_b\), legal determinant/trace, and corrected
least-period set.
