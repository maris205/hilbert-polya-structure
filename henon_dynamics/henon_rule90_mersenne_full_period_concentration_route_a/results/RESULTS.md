# C155 results

- Family: Mersenne circumferences `L=2^r-1`, every `r>=2`.
- Periodic set: the `2^(L-1)`-point image; all periods divide `L`.
- Proper fixed-space theorem:
  `dim Fix(g^j)=dim Fix(g^gcd(j,L))<=2 gcd(j,L)<=2L/3`.
- State concentration: `Pr(period<L)<=2L*2^(-L/3)`, hence full-period
  probability tends to one.
- Burnside concentration:
  `|L*C_L/2^(L-1)-1|<=2L*2^(-L/3)`.
- Cycle-averaged length divided by `L` tends to one.
- Exact replay: seven family rows, 26 divisor-period cells, and 494
  proper-time fixed-dimension cells.
- Independent checker: 2,291 assertions; SymPy: 2,255 checks.
- Mutation audit: 53 repaired-hash plus one stale-hash rejection.
- Power-of-two control: nilpotent, with only zero periodic.

Evidence SHA-256: `d1c63b082265ba2906be1f7a5aeb51b95224f0d1efaaed01dd9bb62986a8f399`.
