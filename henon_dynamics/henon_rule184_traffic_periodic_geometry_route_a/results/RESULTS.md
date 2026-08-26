# C175 results / 结果

Status: all theorem-led symbolic and exhaustive regression gates pass.

- All `N>=1`, all sectors: periodic states are exactly isolated-minority words (`PROVED`).
- Finite attraction: every state reaches the core in at most `m^2` updates (`PROVED`).
- Every iterate: closed fixed-count formula through `gcd(N,n)` and cyclic independent sets (`PROVED`).
- Primitive cycles and Artin--Mazur zeta: exact Möbius inversion and Euler product (`PROVED`).
- Koopman boundary: full sector is a permutation iff `m<=1`; every periodic core is a rotation permutation (`PROVED`).
- Finite sentinels: 90 sectors, 8,190 words, 1,636 fixed-count rows, 299 primitive rows, and 196,608 word/iterate checks.
- Independent checker: 34,545 assertions. SymPy: 25,563 checks. Mutation suite: 17/17 rejected.
- Citation and reference registries: 0 entries.

Route-A v0.2: `(A0_FAIL, A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)`, overall `ROUTE_A_REJECTED`, Route B false.

中文结论：周期核、吸引机制和计数公式均为全参数定理；有限穷举只承担回归验证。该系统没有算术来源，含瞬态的全扇区也不能被宣称为酉动力学。
