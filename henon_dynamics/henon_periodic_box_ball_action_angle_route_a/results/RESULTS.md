# C182 exact results

## The mathematical advance

For every periodic binary box--ball system with `L>=2M`, every soliton content `m`, every exact internal-symmetry tuple `alpha`, and every commuting `T_l`, the KTT/Takagi component is the finite lattice quotient

`Z^H / F_alpha Z^H`,

and `T_l` is translation by `h_l=(min(j,l))`.  If the nonzero Smith factors of the augmented matrix `[F_alpha|h_l]` are `e_i`, the exact component order is

`q_(alpha,l)=det(F_alpha)/prod_i e_i`.

Therefore one component contributes `det(F_alpha)` fixed points at iterate `n` exactly when `q_(alpha,l)|n`, and otherwise contributes zero.  Multiplication by the exact Takagi component multiplicity and finite summation gives level, fixed-mass, and complete positive-weight fixed-point laws.  Primitive cycles follow by Möbius inversion.  For cycle counts `C_q`,

`zeta(z)=prod_q(1-z^q)^(-C_q)=det(I-z U)^(-1)`

for the ordinary finite counting-measure Koopman permutation.

The vacuum, half-filled `p_max=0`, and all saturated capacities `l>=max H` are included.

## Deterministic ledger

- `193` soliton levels.
- `236` positive internal-symmetry sectors.
- `1,524` component translations.
- `342` fixed-mass aggregate rows.
- `62` full positive-weight aggregate rows.
- `23,136` component/global fixed-point cells.
- Sum of component multiplicities across sentinels: `494`.
- Sum of sector points across sentinels: `18,735`.

For every level, the exact sector sum `sum_alpha c(alpha) det(F_alpha)` equals the KTT cardinality `Omega_L(m)`.  For every `(L,M)`, summing all soliton contents equals `binom(L,M)`.

## Independent validation

- Independent checker: `55,907` assertions.
- Actual periodic-carrier enumeration: all `559` binary states through `L=9`, `108` complete maps, and `437` primitive cycles.
- SymPy: `38,979` checks and `38` distinct observed cycle orders; explicit cycle determinants for all `20` observed orders at most `24`.
- Replay: `5,765,655` bytes, byte identical.
- Mutation: `64/64` repaired-hash semantic mutations and `1/1` stale-hash mutation rejected.

## Route-A result

`(A0_FAIL, A1_WEAK, A2_FAIL, A3_FAIL, A4_NATURAL_QUANTIZATION)`; overall `ROUTE_A_REJECTED`; Route B false.

The candidate has complete intrinsic cycles and a natural finite same-clock Koopman unitary.  It has no intrinsic rational-prime origin, logarithmic arithmetic clock, target divisor comparison, global target analytic structure, or Weil compression.
