# Final lane self-check

- Canonical replay: byte-identical (`cmp` exit 0).
- Exact assertions: `811549`; systems: `9`; terminal line:
  `PASS / HOLD_EXTERNAL`.
- Control characters: none in any retained lane artifact after repairing the
  accidental backspace before `\mathbf{1}_{H_\ell}` in the RHT proof.
- RHT boundary checked explicitly: `d=1` excluded; only nonzero forms sampled;
  every increment has odd size and every class therefore has period two.
- RHT arithmetic checked independently at `t=1,2`: the zero-sum history counts
  are respectively `0,N`, while each nonzero sum has `1,N-1` histories; totals
  are `N,N^2`.
- Spectrum multiplicities sum to the full carrier:
  `K+K+NK+NK=2^(2^d-1)` with `K=2^(2^d-d-2)`.
- The source record for finite-field edge labels is correctly attributed to
  Hirobumi Mizuno and Iwao Sato.
- Collision disposition: one live spike (`RHT`), one reserve (`LFS`), seven
  kills; no paper number allocated and no external action authorized.

