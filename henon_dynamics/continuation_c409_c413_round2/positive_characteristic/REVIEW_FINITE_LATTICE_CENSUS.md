# Independent review: finite-lattice census

2026-09-06. Internal, non-author mathematical review by the
positive-characteristic scout. This is not an external review, formal Route-A
score, priority certification, admission, or manuscript edit.

## Reviewed object and verdict

I read all 409 lines of
[FINITE_LATTICE_CENSUS_PROOF.md](../arithmetic/FINITE_LATTICE_CENSUS_PROOF.md),
sections 1–10, including every displayed identity and the ownership gate.
The reviewed SHA-256 is
`0d1d802f9d647f14afa45053d2dd439955034a8c1806a5b14ba31d6961a9ab7e`.
I did not rerun the author's finite enumeration, modify the author file,
or change any frozen result.

**Mathematics: PASS for Theorems A and B and Corollary C as stated.**
No missing all-period, all-modulus, signed-trace, realization, or local-class
argument was found. The one external classification result is applicable in
exactly the group and coefficient ring used. One non-theorem sentence in
section 9 should be narrowed, as explained below.

**Substance/ownership: not cleared for an independent-new-paper admission.**
The residual contribution is a genuine observation-fibre classification,
not just another list of examples. However, its remaining proof is short and
elementary after classical recurrence, Smith, and local-conjugacy deductions.
The explicitly identified 1996/1999 source gate is material and remains open
in this review. My recommendation is to retain this as a mathematically
complete candidate/possible companion result, not to fill a paper slot on
the strength of the mathematical PASS alone.

## Primary dependency check

I checked the author-hosted published
[Baake–Roberts–Weiss paper](https://web.maths.unsw.edu.au/~jagr/BRW08.pdf):
*Periodic orbits of linear endomorphisms on the 2-torus and its lattices*,
Nonlinearity 21 (2008), 2427–2446, DOI 10.1088/0951-7715/21/10/012.
The inspected passages are Definition 2, Proposition 3 and its proof,
Lemma 3 and Proposition 6, Theorem 2 with its proof, and Corollaries 3–4
with the latter's proof. This is not a claim to have read all 20 pages.

Their matrix gcd is precisely the author's g=gcd(b,c,d−a), not the content
k or centered content h. Theorem 2 equates equality of determinant, trace,
and this gcd with conjugacy over every finite quotient. Corollary 4 gives
the profinite conjugacy equivalence. Both use GL, not SL; integral conjugacy
is not asserted. Proposition 3 already recovers the finite periodic abelian
group from all lattice cardinalities. Thus the present attribution and
application are correct. None of these inspected statements supplies the
new draft's complete quotient from g to census labels (t,h).

## 1. Object, nondegeneracy and quantifiers

The assumptions det A=1 and |tr A|>2 imply two distinct real reciprocal
eigenvalues, neither a root of unity. Therefore det(A^n−I) is nonzero for
every n≥1. They also exclude A=I, scalar A, and a zero centered matrix, so
k,h,g are all positive. Every division in the Smith formulas is legitimate.

The modulus q and the period n have distinct roles throughout. Theorems A/B
really cover every positive integer n, including even n, and every positive
integer modulus q. No prime-to-characteristic or bounded-modulus substitute
enters the argument. Theorem B fixes the signed trace as part of the label.

## 2. Smith reconstruction and the two period identities

For an integral full-rank 2×2 matrix, reduction of a Smith decomposition is
valid over every Z/qZ. The scalar kernel count gcd(q,s) proves equation (3).
At prime powers, the first differences of the logarithmic counts recover
the number of Smith exponents at or above each level, including zero
exponents. Hence the reconstruction really determines the ordered pair,
not just its product. The maximum in equation (4) is attained at q=s₂.

I checked (6) and (7) on each reciprocal eigenvalue; both have the displayed
signs for negative as well as positive trace. The m=0 case of (6) is valid.
The integral inverse of A^m justifies preservation of content; no rational
change of basis is being used for that step. Thus the odd and even formulas
for the first Smith invariant in (8) are exact for all n. Neither scalar
factor can vanish under hyperbolicity. Equation (9) follows from det A^n=1.

These observations establish the complete reduction to (t,k,h), independently
of any finite experiment.

## 3. Audit of the elimination of k

Equation (10) follows by an integral elementary replacement inside a gcd.
For odd t, d−a is odd; therefore h=g is odd and multiplication by 2 is
invertible modulo every divisor of g. This proves k=gcd(h,t−2), including
negative traces and negative diagonal entries.

For even t=2T, the decomposition A=TI+rN uses an integral primitive
traceless N. Its determinant equation gives D=(T²−1)/r²=x²+yz>0.
The gcd gcd(y,z,2x) divides 2 because N is primitive, so the exhaustive
alternatives are g=r and g=2r. The first gives k=gcd(T−1,r).

In the second alternative, x is odd and y,z are even. Thus D≡1 (mod 4),
and the replacement rx≡r (mod 2r) gives equation (13). The subsequent
valuation argument is sound:

- r odd is incompatible with r²D=T²−1 modulo 4, so r is even and T odd;
- writing e=v₂(r), f=v₂(T−1), ℓ=v₂(T+1), one has
  2e=f+ℓ and min(f,ℓ)=1;
- e=f would force f=ℓ=e, impossible for these consecutive even integers;
- hence v₂(T−1+r)=min(f,e), giving exactly the same 2-adic valuation
  in both gcds; at odd primes one simply reduces modulo r.

There is no hidden possible cancellation at 2: the proof has explicitly
excluded the equality of the summands' valuations. Thus equation (14) is
proved for both branches and both signs. This is the main arithmetic point
I tried to break; I found no exceptional case.

## 4. Theorem A and signed trace recovery

The two reconstructed determinant magnitudes are |2−t| and t²−4.
The second gives |t|, and the first selects its sign by the distinct values
|t|−2 and |t|+2. The second row also recovers h. Conversely, (t,h)
recovers k by the audited parity cases and hence all Smith data and all
cardinalities. The final statement with signed trace fixed follows directly.

The row distinctions are not cosmetic. Replacing A by −A leaves its square
unchanged but reverses signed trace. Conversely, companion matrices of
traces 7 and −3 both have first-row Smith data (1,5), so the first row by
itself would not suffice either. These are direct algebraic observations,
not another finite census run or an extra theorem required by the draft.

## 5. Theorem B: admissibility, realization and exact fibres

For odd trace, divisibility h² | t²−4 is necessary. The converse matrix
(15) is integral because both t,h are odd and E≡1 (mod 4). Direct
determinant expansion gives 1; its off-diagonal h and diagonal difference
−h force g=h, and centered content is h. Therefore every claimed odd label
is attained and has exactly one profinite conjugacy class.

For even trace, equations (12) give all necessary labels and the only two
possible g-values. Matrix (16) attains g=r for every admissible r. Matrix
(17) is integral when D≡1 (mod 4), and its primitive centered triple
(1,2,(D−1)/2) has the required even last coordinate, giving g=2r.
Its determinant computation is correct. Conversely, the parity argument
in section 5.2 prohibits this second value for other D. Thus no candidate
label or third class has been omitted. Applying the verified external
classification separately for each g proves uniqueness in the stated
quotient, not uniqueness of integral conjugacy classes.

## 6. Corollary C: minimum and infinite family

The two-class valuations force e≥2: one of f,ℓ is 1 and their sum is the
even number 2e, so the other is an odd integer at least 3. Hence r≥4.
The draft's short examination of |T|<9 is correct.

As an independent non-enumerative check, D is positive and ≡1 (mod 4).
D=1 would give (|T|−r)(|T|+r)=1, impossible for r>0. Thus D≥5 and
T²=1+r²D≥1+16·5=81. Equality is attained at |T|=9,r=4,D=5.
This independently confirms minimum absolute trace 18.

The displayed pair has determinant 1, trace 18, k=4, h=8, and respective
g-values 4 and 8. Modulo 8, B is the scalar 5I whereas A is not scalar,
so local nonconjugacy needs no search. The infinite family has
D=64j²+36j+5≡1 (mod 4) and trace 64j+18 exactly as stated.

## 7. Section 9: one wording correction and one justification

At a fixed modulus, invertibility makes the maps permutations; Möbius
inversion and the stated finite permutation determinant are valid. The
Smith data also identify the abelian groups of toral periodic points at
each period. The warnings about target Euler factors and Riemann
determinants are appropriate.

**Narrow the sentence about compatible conjugating maps.** The proof
excludes compatible *linear/group-homomorphic* conjugacies in a two-class
fibre. It does not establish nonexistence of arbitrary nonlinear,
set-theoretic conjugacies compatible with reduction. The sentence
currently saying that the census does not give compatible conjugating maps
across moduli is defensible as a warning about what the proof constructs,
but ambiguous if read as a nonexistence theorem. A safe replacement is:

> The census does not determine compatible linear conjugators across
> moduli; such a family would imply profinite linear conjugacy and is
> impossible in the two-class fibres. No claim is made here about
> compatible nonlinear conjugators.

The claimed failure of action-preserving periodic-group equivalence can be
justified directly, without conflating it with the preceding issue. If two
matrices are nonconjugate modulo q, choose n divisible by both of their
orders in GL₂(Z/qZ). Then the q-torsion subgroup of each toral Fix_n is
the full lattice (Z/qZ)². An action-intertwining group isomorphism of the
two Fix_n groups would restrict to a forbidden GL₂(Z/qZ) conjugacy.
For the displayed pair, q=8 and n=2 already suffice. Under the usual
action-retaining strong Bowen–Franks terminology, this supports the
strict-weakness claim. Merely isomorphic underlying finite abelian groups
do not supply such an intertwiner.

## 8. Separate substance and ownership decision

The potential residual result is sharply identifiable: two period rows
recover the complete ordinary census, and the resulting forgetful map has
the explicitly realized one-/two-class fibres. This is more meaningful
than the trace-18 example alone, and all of it is mathematically proved.
However, the algebraic engine consists of two elementary reciprocal-power
factorizations and a short content/valuation analysis, atop established
Smith reconstruction and a fully classical local-classification theorem.
It should not be presented as a new local-conjugacy theory or new general
Bowen–Franks machinery.

I have not obtained or read the identified Rodrigues 1996 thesis and the
1999 Rodrigues–Sousa Ramos Grazer paper. Nor did this task authorize
replacing the coordinator's broader ownership audit with an abstract-level
priority inference. The author correctly keeps those sources as a gate.
An exact theorem absent from the BRW passages I inspected does not prove
that the two-period recurrence or its fibre consequence is unpublished.

Accordingly: mathematical PASS, minor scope wording recommended,
ownership UNRESOLVED, no independent-paper admission recommendation at
this stage. No larger numerical check would close that source gate.
