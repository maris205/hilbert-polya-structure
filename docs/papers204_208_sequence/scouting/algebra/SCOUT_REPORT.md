# Algebra scout: eight literal maps, one pending value gate

2026-09-05. Owner/proof author: `/root/batch197_lzk_gate`.
No paper IDs, central index edits, Git mutations or external actions.

Outcome: **CS is proof-complete but VALUE_GATE_PENDING / OWNER_AMBER**;
the other seven maps receive NO_PROMOTION recommendations. In particular,
OF was initially a strong mathematical signal, then failed the
different-mechanism test by an explicit generic polarity-memory deduction.
These are candidate dispositions, not completed papers or independent PASS.

## Breadth and exact pilots

All maps are finite autonomous deterministic self-maps on the stated full
carrier. `pilot.py` is original stdlib code. `PILOT_CANONICAL.jsonl` is
actual stdout from two fresh byte-identical runs, 41 parameter boxes total.
No runtime or higher-dimensional experiment is being used as a proof.

| Code | Literal carrier and update | Pilot box / selected actual signal | Disposition |
|---|---|---|---|
| JS | Mat_n(F_q), A->A+A^2 | n=2, q=2,3,4; n=3,q=2. At (2,4), 256 states, core16, H4. | NO_PROMOTION: polynomial functional calculus/Frobenius-type spectral reduction; no second non-transfer axis. Not asserted to equal a particular old power map. |
| TM | Mat_n(F_q), A->[A,A^T] | Same four boxes; H2 throughout, including 512 states at n=3,q=2. | NO_PROMOTION: first output is symmetric, hence the second is zero. General inverse problem was not closed; no rescue by larger boxes. |
| TF | Mat_n(F_q), A->A(tr(A)I-A) | Same boxes. n=2,q=4 has image4 and H1; n=3,q=2 has H3, core109. | NO_PROMOTION: n=2 is det(A)I by Cayley-Hamilton, then scalar squaring. n=3 lacks an all-parameter two-axis contract. |
| CS | Mat_2(F_{2^e})^2, (A,B)->([A,B],A+B) | q=2: 256 states, core40, H2. q=4: 65,536 states, core3,136, H2; all one-step and 2/3-step target fibres checked. | PROOF_COMPLETE, VALUE_GATE_PENDING, OWNER_AMBER. Root to assign independent gate; no seat reservation. |
| OF | L(F_q^{2m})^2 with a nondegenerate alternating form, (U,V)->(V,(U+V)^perp) | (q,2m)=(2,2),(3,2),(4,2),(2,4),(3,4). Last: 44,944 states, core433, H3, unique max fibre212. | NO_PROMOTION after deductive generic polarity-memory transfer; exact symplectic proofs retained. |
| FC | Full functions f:F_p->F_p, f->(x->f(f(x))-f(x)) | p=2,3,5, respectively 4,27,3,125 states; H2,3,11. p=5 has periods1,2,4,8. | NO_PROMOTION: no uniform temporal or inverse theorem; affine restriction already carries scalar quadratic dynamics and does not control the full carrier. |
| GH | (Z/NZ)^2 using least residues, (a,b)->(gcd(a,b,N) mod N,a+b mod N) | N=2,3,4,6,8,9,10,12,15. At N=15: 225 states, image=core24, H1. | NO_PROMOTION: after one step the gcd coordinate is fixed and the second is an additive rotor on its multiples; inverse is a one-line gcd/CRT count. |
| DS | Divisors d of N, d->gcd(N,d+N/d) | N=4,8,12,16,36,60,100,144,300,1,020,100. The last has 27 states, one fixed root, H5. | NO_PROMOTION: close exponent-1 variant of P142's exponent-2 divisor map; valuation cancellation does not justify a new seat. |

GH's full proof-engine subtraction is explicit: the image consists of
(d,b) with d|N and b a multiple of d, with d=N encoded as 0. Each d-stratum
is the single additive cycle of length N/d. A target (d,c) with d|c has

    (N/d) product_{p | gcd(c/d,N/d)} (1-1/p)

predecessors, by choosing the first input residue a and requiring
gcd(a,c,N)=d. Thus both axes are direct normalizer/rotor/CRT transfers.

For DS the nontrivial cancellation is real, not a numerical mistake:
at a prime p with v_p(d)=a and v_p(N)=e, the new exponent is min(a,e-a)
unless 2a=e. At the midpoint it can jump above e/2 by unit cancellation.
The category potential (0 below midpoint, 2 at midpoint, 1 above midpoint),
summed over p|N, strictly drops whenever the state changes; all cycles are
fixed. This elementary valuation argument does not erase the close P142
parameter-variant collision. The H5 box is preserved rather than enlarged.

## CS: exact proposed conjunction for the independent value gate

For q=2^e, set C=[A,B], S=A+B, s=tr S. The complete iterate is

    F^{k+1}(A,B)=(s^k C, S+(1+s+...+s^{k-1})C).

This is proved from the polarized two-by-two Cayley-Hamilton identity and
tr C=tr(CS)=0. The recurrent set consists of all (0,B) and the nonzero-C
image states with s!=0. Height is exactly 2; fixed states number q^4.
Nonfixed recurrent periods are 2 for s=1 and ord(s) for s!=0,1.

With D=q^5-q^3 there are D/2 strict 2-cycles and phi(d)D/d strict
d-cycles for each d>1 dividing q-1. Core size is q^6-q^5+q^3; depth-2
size is q^7-2q^5+q^3. One-step fibres are q^4 at (0,lambda I), q^2 at
all other image states, and zero elsewhere. For every t>=2, every target
fibre is one of

    q^2                  (recurrent target of nonzero trace),
    q^5+q^4-q^3          (scalar fixed target),
    q^4-q^3              (nonscalar trace-zero fixed target),
    0                    (all other targets).

The q scalar fixed targets are exactly the maximizers at every time.
Full deductions and source decoders: `PROOF_NOTES.md`, CS-T and CS-I.

At q=4 the literal graph has 256 fixed points, 480 strict 2-cycles and
640 strict 3-cycles; depth counts are 3,136 / 48,000 / 14,400. The q=2
graph has 16 fixed points, 12 strict 2-cycles, depths 40 / 144 / 72.
`collision_controls.py` also retains a literal q=3 counterexample to
the characteristic-two iterate identity; no odd-characteristic extension
is claimed.

Zero credit: ordinary scalar order/Jordan shear, centralizer kernels,
trace-pairing orthogonality, affine solution counts and finite graph census.
Remaining candidate value: the full feedback stratification and its
all-time rank-jump atlas. If the independent gate finds these are only an
elementary bilinear/shear transfer, reject CS; do not inflate the dimension
or field box to fill a seat.

## OF rejection and preserved negative control

The exact symplectic results are valid: F^6=F^3, sharp H3, recurrent pairs
are orthogonal with equal radicals, and target (X,Y), X<=Y^perp, has fibre
sum_k [a choose k]_q q^{(a-k)b}, where a=dim X and b=dim Y^perp-a.
The core is counted by a common radical followed by an ordered orthogonal
triple decomposition of its symplectic quotient.

However the F^6=F^3 clock follows for **every** self-adjoint antitone
polarity P under the two-register update (A,B)->(B,P(A join B)). Consecutive
compatible triples imply a_i<=a_{i+3}; antitonicity gives the reverse
three-step inclusion after the initial transient. PROOF_NOTES.md OF-K
contains the complete deduction. The attempted generic-polarity
counterexample search returned none in 266,376 pair-states through four
points; `COLLISION_CANONICAL.jsonl` preserves that actual result, rather
than relabeling it as a successful obstruction. This deduction is the
reason for NO_PROMOTION relative to P106/P182 proof engines.

## Handoff

Artifacts: this report; `PROOF_NOTES.md`; `SOURCE_AND_COLLISION_NOTES.md`;
`pilot.py`; `PILOT_CANONICAL.jsonl`; `collision_controls.py`;
`COLLISION_CANONICAL.jsonl`; package `SHA256SUMS`.

Root may assign CS an independent proof/value gate. This author has not
reviewed its own work as an independent reviewer. No formal manuscript,
numbered seat, accepted review, frozen paper package or external release
exists for this lane. HOLD_EXTERNAL remains in force.
