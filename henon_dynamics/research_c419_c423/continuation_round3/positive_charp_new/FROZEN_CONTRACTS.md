# Round 3 positive-characteristic contracts

Frozen: 2026-09-07, before candidate computation. This bounded scout is not an admission or novelty claim. All earlier M1/AS2/IR1 decisions remain untouched. At most the following two candidates receive deep screening; no third replacement is authorized in this lane. The canonical location is under `henon_dynamics/research_c419_c423/`; an initial prefix omission was corrected without changing either mathematical contract and before any candidate computation.

## PC3-A — a non-additive unicritical rational family

- Exact map: for every odd prime p, f_p(z) = z^p + 1/z = (z^(p+1)+1)/z, with f_p(0)=infinity and f_p(infinity)=infinity.
- Domain: P^1 over an algebraic closure of F_p; distinct geometric points, not scheme lengths and not F_(p^r)-point tables.
- Parameters: every odd prime p; there is no hidden coefficient specialization or cutoff.
- Clock: the original n-th iterate f_p^n for every integer n >= 1.
- Observable: N_p(n)=#Fix(f_p^n) and the formal Artin–Mazur series Z_p(t)=exp(sum_(n>=1) N_p(n)t^n/n).
- Full target: a proved all-p classification of rationality versus nonrationality of Z_p, with an exact all-n count mechanism sufficient to prove that classification. An iterated gcd algorithm by itself is not closure.
- Candidate statement to test, not assume: Z_p is nonrational for every odd p.
- First source owners to test: Bridy, arXiv:1306.5267; Byszewski–Cornelissen–Houben–van der Meijden, arXiv:1904.04942; Faber's classification of rational functions with a unique critical point.
- Cheapest falsifiers: symbolic ramification and multiplier calculation; determine whether the entire family is conjugate/semiconjugate to a listed dynamically affine exception; if computation is warranted later, exact polynomial numerator/gcd counts for p in {3,5} at small native n only. A finite list is never evidence for the all-n conclusion.
- Stop loss: reject if a classical theorem already supplies the promised conclusion or this is a renamed prior xH(x)^p contract; hold without admission if distinct cycle multipliers/ramification prevent an all-n proof. No widening to coefficient families, extension clocks, or different rational maps.

## PC3-B — integer-matrix isogenies on ordinary Kummer quotients

- Exact data: any odd prime p, any ordinary elliptic curve E over algebraic closure F_p, any integer g >= 2, and any A in M_g(Z) with det(A) != 0 and no eigenvalue a root of unity.
- Exact map: A acts on E^g by integer multiplication and addition; it commutes with simultaneous inversion. Let f_A be its induced self-map of the coarse quotient X=E^g/{+1,-1}.
- Domain: all distinct geometric points of X, including the quotient branch locus. No deletion of 2-torsion and no weighted orbifold count.
- Clock: the original f_A^n for all n >= 1.
- Observables: N_A(n)=#Fix(f_A^n) and Z_A(t)=exp(sum_(n>=1) N_A(n)t^n/n).
- Full target: exact all-n N_A and a rational/nonrational classification of Z_A for this entire parameter class. A formula plus an unproved rationality conjecture is not admission.
- Candidate statements to test, not assume: N_A(n) is half the sum of the geometric kernels of A^n-I and A^n+I; Z_A is rational exactly when the reduction of A modulo p is nilpotent.
- First source owners to test: dynamically affine maps in positive characteristic (arXiv:1904.04942) and the general finite-adelic-distortion framework for algebraic-group endomorphisms.
- Cheapest falsifiers: Burnside orbit counting including stabilizers, Smith normal form for kernels, and direct verification of the hypotheses of the closest general theorem. No numerical matrix search is needed if these show a short classical companion.
- Stop loss: exclude immediately as a short classical companion if Burnside + standard kernel counts + a general zeta theorem close the proposal. Hold if the count formula is routine but the proposed general zeta classification is not proved; a missing literal matrix example in an abstract is not novelty.

## Shallow third idea (not a deep-screen contract)

Integral cycles of x^d+c over F_q[T], p not dividing d and c nonconstant, were noted only for a source/elementary obstruction screen. They do not receive computations, a proof package, or a replacement slot here. The ring-unit factorization obstruction is a strong prior-classical-risk flag.

## Allowed outputs and exclusions

Only this directory may be written. No manuscript, global admission registry, C-number, Git operation, legacy experiment, or rerun of IR1 is authorized. This round does not reopen xH(x)^p / NC1, Drinfeld invariant factors, Hénon–Frobenius intersections, or trace-quadratic skew NC2.
