# HCS-C174 — Dyadic odd-affine parity renewal / 二进奇仿射奇偶更新

This release treats, for every odd integer pair \(a,b\), the map

\[
T_{a,b}(x)=\begin{cases}x/2,&x\equiv0\pmod2,\\(ax+b)/2,&x\equiv1\pmod2,\end{cases}\qquad x\in\mathbb Z_2.
\]

The classical parity-vector conjugacy is a foundation, not a C174 novelty claim. The package's substantive progress is the exact first-return renewal theorem on the odd coset, recovery of the original clock through the roof \(r(k)=k\), and a proof that both unweighted periodic data and reciprocal-derivative stability data are blind to every odd parameter pair.

本包研究所有奇整数参数 \(a,b\) 的二进奇仿射奇偶映射。经典 parity 共轭只作为先验基础；C174 的实质进展是：奇数截面上的精确首返 renewal 定理、通过屋顶函数 \(r(k)=k\) 恢复原始时钟，以及证明无权周期数据和二进稳定性加权数据对全部奇参数均失明。

## Release verdict / 发布结论

Route-A tuple:

`(A0_FAIL, A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)`

Overall: `ROUTE_A_REJECTED`. A0 failure is decisive. The exact mathematics is retained as a renewal/clock-recovery theorem and as a hostile parameter-blindness control; it is not promoted to an arithmetic target model.

总体结论为 `ROUTE_A_REJECTED`，且 A0 失败具有一票否决效力。本文保留其 renewal、时钟恢复和参数盲性定理价值，但不把它提升为算术目标模型。

## Main exact results / 主要精确结果

- Every length-\(n\) parity word has one fixed point
  \(x_\epsilon=bA_\epsilon/(2^n-a^{s_n})\), hence \(\#\operatorname{Fix}(T^n)=2^n\) and \(\zeta_{AM}(z)=(1-2z)^{-1}\).
- At every periodic word, \(|1-(T^n)'|_2=2^n\); therefore the stability sum is one and \(\zeta_{\rm stab}(z)=(1-z)^{-1}\).
- On the odd cross-section, \(\tau=v_2(ax+b)\) has conditional Haar law \(2^{-k}\). After removing the countable eventually-zero exceptional set, the return map is the full one-sided shift on symbols \(k\ge1\).
- The accelerated return map has infinitely many fixed points \(x_k=b/(2^k-a)\), so its ordinary Artin–Mazur zeta is undefined. With the original-clock roof,
  \(F(z)=z/(1-z)\) and \(\zeta_{\rm roof}=(1-z)/(1-2z)\). Restoring the zero orbit gives \((1-2z)^{-1}\).
- The natural Haar Koopman operator is a proper isometry with Wold model
  \(I_{\mathbb C}\oplus S^{(\aleph_0)}\), not a trace-class or Hilbert–Pólya operator.

## Reproduce / 复现

Run from this directory:

```bash
python3 code/c174_parity_renewal_producer.py
python3 code/c174_parity_renewal_checker.py
python3 code/c174_sympy_crosscheck.py
python3 code/c174_replay.py
python3 code/c174_mutation.py
python3 code/c174_release_manifest.py
```

The evidence is exact and deterministic. Finite ledgers are regression sentinels, not the proof. Proofs are in `THEOREM_PACKAGE.md` and `paper/main.tex`.

证据文件采用精确算术并可逐字节回放。有限表格只是回归哨兵，不替代定理证明；证明见 `THEOREM_PACKAGE.md` 与 `paper/main.tex`。

## Scope firewall / 范围防火墙

Literal scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.

No prime correspondence, arithmetic local data, Euler factor, root number, automorphy, target divisor match, Collatz resolution, Hilbert–Pólya operator, acceptance rate, external review, or Route-B authorization is claimed.

本包不声称素数对应、算术局部数据、Euler 因子、根数、自守性、目标除子匹配、Collatz 猜想进展、Hilbert–Pólya 算子、接受率、外部评审或 Route B 授权。
