# Control results — P90

Final registered exact execution (2026-08-28 UTC):

```bash
python3 code/verify_rule184.py
```

Output:

```text
PASS: 298,283 exact assertions
rings n<=14: reflection conjugacy, recurrent core, and sharp particle-layer entry depths verified
rings n<=12: min-plus formula through t=2n and all iterate-fixed weight polynomials verified
rings n<=13: temporal orbit and particle-resolved Mobius ledgers verified
```

Coverage added during the hostile audit:

- exact particle–hole/reflection conjugacy and preservation of the recurrent
  core for every state through `n=14`;
- the solid-block sharpness witness in every particle layer;
- the min-plus identity at every time `0<=t<=2n`, rather than only before
  first entry;
- direct weighted fixed-polynomial, temporal-cycle, and particle-cycle
  comparisons, including the even half-filled two-cycle.

The program uses integer arithmetic and the Python standard library only. No
random sampling or floating-point tolerance occurs. The original package
reported 144,216 assertions; the final total is 298,283 because the audit
strengthened coverage, not because a theorem range was reduced.
