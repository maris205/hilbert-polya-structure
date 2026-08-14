# Proof Package

## Claim

Let \(L_1,L_3,L_4>1\) be the positive unstable moduli of the exact primitive
period \(1,3,4\) orbits specified in paper/paper.tex. For every real
\(h>0\), the three numbers

$$
L_1^h,\qquad L_3^h,\qquad L_4^h
$$

cannot all be rational primes. More precisely:

1. if \(h\in\mathbb Q_{>0}\), none is a rational integer greater than one;
2. if \(h\notin\mathbb Q\), at least one is transcendental.

## Status

PROVABLE AS STATED

## Assumptions

- The Hénon map is \(H_6(q,p)=(1-6q^2-p,q)\).
- The three displayed coordinate cycles are interpreted with the frozen
  four-state survivor rectangles \(X_\pm=\pm[1/3,5/8]\).
- Real powers use the positive real logarithm.
- The real Six Exponentials Theorem is used exactly in the form of Pila,
  Theorem 3.1.
- Standard ramification facts for finite number-field extensions are used:
  a field discriminant divides the discriminant of an integral primitive
  element; ramification persists in overfields; and the compositum of local
  unramified extensions is unramified.

## Notation

- \(K_j=\mathbb Q(L_j)\).
- \(T_3=38+42\sqrt5\).
- \(d_3=T_3^2-4=10260+3192\sqrt5\).
- \(E=K_1K_3K_4\).
- \(\iota_j\) is the reciprocal-root automorphism of \(K_j\).

## Proof Strategy

First reconstruct the three periodic orbits and their multiplier fields.
Use ramification at \(5,11,29\) to prove the full compositum degree \(32\).
This makes the three reciprocal-root automorphisms independently extensible
to \(E\), which yields multiplicative and logarithmic independence. Finally
split according to whether \(h\) is rational and apply, respectively, the
algebraic-unit theorem or Six Exponentials.

## Dependency Map

1. The main claim depends on the rational-exponent unit argument and the
   irrational-exponent Six-Exponentials argument.
2. Six Exponentials depends on \(\mathbb Q\)-linear independence of the three
   positive logarithms.
3. Logarithmic independence depends on independent extensions of the three
   reciprocal-root automorphisms.
4. Independent extension depends on
   \([K_1K_3K_4:\mathbb Q]=[K_1:\mathbb Q][K_3:\mathbb Q][K_4:\mathbb Q]=32\).
5. The degree product depends on the ramification ladder at \(5,11,29\).
6. Membership in the survivor depends on the exact recurrence, rectangle
   inequalities and allowed state transitions.

## Proof

### Step 1: exact primitive survivor orbits

Periodic \(q\)-coordinates satisfy

$$
q_{i+1}=1-6q_i^2-q_{i-1}.
$$

Direct substitution verifies the fixed point, the sequence
\((-\sqrt5/6,(1+\sqrt5)/6,-\sqrt5/6)\), and the period-four sequence
\((-1/\sqrt6,-1/\sqrt6,1/\sqrt6,1/\sqrt6)\). Their coordinate absolute
values lie in \([1/3,5/8]\). Their state cycles are, up to cyclic rotation,

$$
(--),\qquad (--,+-,-+),\qquad (--,+-,++,-+),
$$

and every transition occurs in the frozen adjacency graph. The period-three
sequence is nonconstant, hence primitive because \(3\) is prime. The
period-four sequence has neither period one nor period two, hence is
primitive.

Chronological matrix multiplication gives traces

$$
2+2\sqrt7,\qquad -38-42\sqrt5,\qquad 578.
$$

The positive unstable moduli satisfy

$$
L_j+L_j^{-1}=|\operatorname{tr}M_j|.
$$

Elimination yields the monic reciprocal polynomials

$$
f_1=X^4-4X^3-22X^2-4X+1,
$$

$$
f_3=X^4-76X^3-7374X^2-76X+1,
$$

$$
f_4=X^2-578X+1.
$$

Every \(L_j\) is an algebraic unit because both the constant and leading
coefficients are one and the reciprocal root belongs to the same quadratic
equation over the trace field.

### Step 2: individual field degrees

For \(L_1\), the discriminant over \(\mathbb Q(\sqrt7)\) is
\(28+8\sqrt7\), with rational norm \(336\). If it were a square in
\(\mathbb Q(\sqrt7)\), its norm would be a rational square, which \(336\) is
not. Thus the quadratic extension over \(\mathbb Q(\sqrt7)\) is nontrivial.
Also

$$
\sqrt7=(L_1+L_1^{-1}-2)/2\in\mathbb Q(L_1),
$$

so \([K_1:\mathbb Q]=4\).

For \(L_3\), the trace field is \(\mathbb Q(\sqrt5)\) and the relative
quadratic discriminant is \(d_3\). Its norm is

$$
54323280=2^4 3^2 5\cdot11\cdot19^3,
$$

which is not a rational square. Therefore \(d_3\) is not a square in the
trace field. Since

$$
\sqrt5=(L_3+L_3^{-1}-38)/42,
$$

we have \(K_3=\mathbb Q(\sqrt5,\sqrt{d_3})\) and
\([K_3:\mathbb Q]=4\). Finally
\(K_4=\mathbb Q(\sqrt{145})\), so \([K_4:\mathbb Q]=2\).

### Step 3: degree multiplication

The polynomial discriminant of \(f_1\) is \(2^{12}3\,7^3\). The field
discriminant of \(K_1\) divides this integer, so \(K_1/\mathbb Q\) is
unramified at \(5\). If \(\mathbb Q(\sqrt5)\) were contained in \(K_1\),
ramification at \(5\) in that quadratic subfield would persist in \(K_1\), a
contradiction. Thus

$$
[K_1\mathbb Q(\sqrt5):\mathbb Q]=8.
$$

The prime \(11\) splits in \(\mathbb Q(\sqrt5)\), because \(5\) is a square
modulo \(11\). The exponent of \(11\) in \(N(d_3)\) is one, so one of the
two primes above \(11\) has valuation one on \(d_3\). Since
\(11\nmid\operatorname{disc}(f_1)\), base change by \(K_1\) is unramified at
that prime. Every extended valuation of \(d_3\) remains odd. A square has
even valuation at every prime, hence \(d_3\) remains nonsquare in
\(K_1\mathbb Q(\sqrt5)\). Adjoining \(\sqrt{d_3}\) doubles the degree:

$$
[K_1K_3:\mathbb Q]=16.
$$

Neither \(\operatorname{disc}(f_1)\) nor

$$
\operatorname{disc}(f_3)=2^{12}3^6 5^3 7^4 11\,19^3
$$

is divisible by \(29\). Thus every completion of \(K_1\) and \(K_3\) above
\(29\) is unramified, and their local composita are unramified. Therefore
\(K_1K_3\) is unramified at \(29\). The quadratic field
\(\mathbb Q(\sqrt{145})\) is ramified at \(29\), so it cannot be a subfield
of \(K_1K_3\). Adjoining it doubles the degree and proves

$$
[E:\mathbb Q]=32.
$$

### Step 4: logarithmic independence

The natural multiplication map

$$
K_1\otimes_{\mathbb Q}K_3\otimes_{\mathbb Q}K_4\longrightarrow E
$$

is an isomorphism because both sides have dimension \(32\). Hence the
reciprocal-root automorphism on any one factor, tensored with the identity on
the other two, defines a \(\mathbb Q\)-automorphism of \(E\).

Suppose

$$
m_1\log L_1+m_3\log L_3+m_4\log L_4=0
$$

with integers \(m_j\). Exponentiating gives

$$
L_1^{m_1}L_3^{m_3}L_4^{m_4}=1.
$$

Apply the automorphism that inverts \(L_1\) and fixes the other two factors,
then divide the original equality by the transformed equality. This gives
\(L_1^{2m_1}=1\). Since \(L_1>1\), \(m_1=0\). Repeating with the other two
automorphisms gives \(m_3=m_4=0\). Clearing denominators proves the same for
rational coefficients, so the three real logarithms are linearly independent
over \(\mathbb Q\).

### Step 5: rational exponents

Let \(h=a/b>0\) with coprime positive integers \(a,b\). If
\(L_j^h=N\in\mathbb Z\) and \(N>1\), then

$$
L_j^a=N^b.
$$

The left side is an algebraic unit. Equality would make the rational integer
\(N^b\) an algebraic unit. Its inverse \(N^{-b}\) would then be a rational
algebraic integer, hence an ordinary integer, which is impossible for
\(N>1\). Thus no \(L_j^h\) is a rational integer greater than one.

### Step 6: irrational exponents

Let \(h\notin\mathbb Q\). The pair \((1,h)\) is linearly independent over
\(\mathbb Q\), and Step 4 proves that
\((\log L_1,\log L_3,\log L_4)\) is linearly independent over
\(\mathbb Q\). The real Six Exponentials Theorem applies to these two sets.
At least one of

$$
L_1,L_3,L_4,L_1^h,L_3^h,L_4^h
$$

is transcendental. The first three are algebraic, so at least one of the last
three is transcendental. A transcendental number is not a rational prime.

Steps 5 and 6 cover every real \(h>0\), proving the claim. ∎

## Corrections or Missing Assumptions

- No correction to the main claim is required.
- The paper was strengthened to print the exact survivor intervals and
  adjacency transitions rather than leaving survivor membership implicit.

## Open Risks

- The theorem does not identify which pressure label is nonprime when the
  common exponent is transcendental.
- The theorem does not obstruct collective prime-ideal, Galois-packet,
  cyclic-resultant or distributional-trace constructions.
- The pressure prime-orbit counting theorem is a separate positive result
  and is not revoked by this scalar obstruction.
