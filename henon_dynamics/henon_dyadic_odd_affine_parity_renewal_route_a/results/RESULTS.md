# Exact results / 精确结果

## Headline / 主结论

For every odd integer pair \((a,b)\), the first return of \(T_{a,b}\) to the odd coset is a geometric renewal shift. Its roof recovers the original branch clock exactly, while both the unweighted and reciprocal-stability periodic invariants are independent of \((a,b)\). This is a complete dynamical theorem and a decisive Route-A parameter-blindness obstruction.

对任意奇整数对 \((a,b)\)，奇数截面的首返是几何 renewal 移位；屋顶函数精确恢复原始分支时钟，而无权与稳定性加权周期不变量均与参数无关。这是完整动力学定理，同时也是决定性的 Route-A 参数盲性障碍。

## Exact identities / 精确恒等式

\[
\#\operatorname{Fix}(T^n)=2^n,
\qquad
P(n)=\sum_{d\mid n}\mu(n/d)2^d,
\qquad
\zeta_{AM}(z)=\frac1{1-2z}.
\]

\[
\sum_{x\in\operatorname{Fix}(T^n)}|1-(T^n)'(x)|_2^{-1}=1,
\qquad
\zeta_{\rm stab}(z)=\frac1{1-z}.
\]

\[
\mu_O(\tau=k)=2^{-k},
\qquad
\zeta_{\rm roof}(z)=\frac{1-z}{1-2z},
\qquad
\zeta_{\rm roof}(z)(1-z)^{-1}=\zeta_{AM}(z).
\]

The accelerated return map has infinitely many fixed points \(b/(2^k-a)\), so no ordinary Artin–Mazur zeta is assigned to it.

加速首返映射的时间一不动点为 \(b/(2^k-a)\)，共有可数无限多个，因此不为它虚构普通 Artin–Mazur zeta。

## Exact finite sentinels / 精确有限哨兵

- 36 frozen odd parameter pairs.
- 288 aggregate fixed-word rows.
- 18,360 exact fixed words through \(n=8\).
- 9,216 exact finite-tail inverse parity prefixes.
- 432 first-return fixed-point rows through \(k=12\).
- 16 primitive-period rows and 32 roof-recovery rows.

These numbers are regression coverage, not proof coverage.

这些计数只描述回归覆盖，不表示证明范围；证明覆盖所有奇整数 \(a,b\) 和全部正时期。

## Route-A result / Route-A 结果

`(A0_FAIL, A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)`

Overall: `ROUTE_A_REJECTED`. A0 failure is decisive. No Route B is invoked.

整体拒绝，A0 具有决定性；不调用 Route B。

## Content hashes / 内容哈希

- Evidence payload SHA-256: `4c4515bc863b83c7f5d20607658e25f14d9c60d4c6f533678f36f84ed3bfa9e2`.
- Evidence file SHA-256: `9cdedc898e8624b00c73ccde4bd316fb4bb2cb948720d7201bed16e0bcd81004`.
- Final PDF SHA-256: `5d236849a52afa5d54d7f9d6423020754bf9d0565bd4b8fb7215a4eb0f886e24`.

The release-manifest hash is intentionally reported outside payload files because the manifest excludes itself.

发布清单自排除，因此其自身哈希不写入 payload 文件，避免循环依赖。
