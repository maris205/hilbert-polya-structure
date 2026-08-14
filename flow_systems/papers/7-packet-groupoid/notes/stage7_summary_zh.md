# Paper 7 中文阶段摘要

## 研究问题

本篇检验：Deninger 的有理 Witt 素数周期 packet 是否已经内生地带有一个
可测/算子代数结构，使 `log p` 闭轨账本能够成为规范的 return trace，并进一步
拥有动力 zeta 或 Fredholm 型行列式。

## 一句话结论

来源内生的 packet 拓扑与 `log p` 时钟是真实的，但来源没有提供横向测度、
跨素数质量或 trace-bearing operator；显式 decomposable proxy 可以严格产生
一个局部有限回归分布和一个右半平面零模迹行列式，但两者是不同 typed owner，
且零模机制对 packet 几何盲、可编译任意时钟，因此不能晋级为算术动力 zeta。

## 最强新进展

1. **同一来源的拓扑桥得到严格修复。** Morishita 的 full-character 版本存在
   trivial-character 反例，printed prime-circle proof 也缺少远离 `p` 的非零性；
   限制到 Deninger 的 finite-kernel subsystem `E_f` 并使用其 equation (35)
   后，可以严格构造连续、flow-anti-equivariant 的同一来源映射。
2. **该桥的边界也被严格证明。** 每条 `p`-packet circle 都 onto 同一个
   adelic circle `C_p`，所以横向标签被压塌；源像的有限 adele 至多有一个零
   坐标，而目标含两个零坐标的类，故全局满射严格失败。
3. **半有限迹的域被完整分层。** 选定 proxy 上每个正有限中心质量列都给出
   faithful normal semifinite trace；affiliated `L1` 与 bounded trace ideal 被
   分开，避免把逐 component 可迹误写成全局 normal trace。
4. **回归分布与行列式 owner 被拆开。** 非零正时间测试下，全局 smear 属于
   bounded `L1(tau_m)` 当且仅当 `sum_p m_p log p` 收敛；单位质量失败。但
   `Theta_m=sum_{p,r>=1}m_p log(p) delta_{r log p}` 仍是独立定义、局部有限的
   正 Radon measure，不能在域外写成 `tau_m(C_f)`。
5. **零模分支给出精确但受限的正结果。** 对
   `K_s=direct_sum_p p^{-s}P_{0,p}`，单位质量的 bounded `L1` 域精确为
   `Re(s)>1`；在那里 principal trace-log 满足
   `D_tau^pr(s)=product_p(1-p^{-s})`，其逆为对应 Euler product。证明包括
   relative-norm holomorphy、branch、Fuglede--Kadison modulus、
   de la Harpe--Skandalis quotient 与 ordinary Fredholm/Breuer 边界。

## 主要障碍

- **来源所有权缺失：** 没有 source theorem 从 Deninger flow 传输横向测度、
  Borel/disintegration、von Neumann algebra、normal trace、中心质量、零模或
  determinant。
- **质量不唯一：** packet 内 Haar probability 只归一局部基底；任何正有限
  `m_p` 都保留局部对称性。用目标 Dirichlet 系数反推 `m_p=1` 是 provenance
  circularity，不是来源推导。
- **几何不敏感：** singleton、任意原子/非原子概率基底和任意 locally finite
  时钟都能通过同一个零模编译器；精确标量恒等式因此 `PROVES_TOO_MUCH`。
- **算子链未建立：** `K_s` 是复参数 holomorphic bounded family，不是自然
  自伴 Hamiltonian；return distribution 也不是同一闭算子的全局谱迹。
- **全局解析结构缺失：** 没有 continuation、functional equation、Gamma
  factor、completed divisor、Riemann--von Mangoldt law 或 Weil compression。

## Route 状态

四个对象必须分别记账，均为 `ROUTE_A_EXPLORATORY`：

| 对象 | Route-A tuple |
|---|---|
| source `DEN-WITT-Z-FIN` | `(A0_ANALYTIC_ARITHMETIC_ORIGIN, A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)` |
| mass-family proxy | `(A0_WEAK_ARITHMETIC_RELATION, A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)` |
| return-distribution record | `(A0_WEAK_ARITHMETIC_RELATION, A1_PASS_ANALYTIC, A2_FAIL, A3_FAIL, A4_FAIL)` |
| unit-mass zero-mode record | `(A0_WEAK_ARITHMETIC_RELATION, A1_FAIL, A2_ANALYTIC_DETERMINANT, A3_FAIL, A4_FAIL)` |

`A1_PASS_ANALYTIC` 与 `A2_ANALYTIC_DETERMINANT` 属于不同 typed records，
禁止拼接。Route B 未调用，也没有创建 Route-B YAML。

## 下一篇最值得继续的方向

优先研究一个**几何敏感、来源内生的横向 owner**：从 finite-kernel packet 的
真实 chart transition / groupoid 出发，明确 units、arrows、Haar system、
representation 与 trace，并首先证明或否证其横向测度和跨素数质量是否唯一。
最小判别测试不是再算 Euler product，而是要求候选在 singleton base、任意
probability base、copied packet 与 arbitrary-clock controls 中至少失败一项；
只有通过这一 provenance gate，才值得研究同一 operator 的 determinant、
continuation 或量子化。

## 证据边界

全部控制均 target-free：未使用 Riemann 零点、拟合质量、拟合时钟、随机数或
网络数据。21/21 tests、9 张 CSV（407 行）和两次独立 byte-identical
regeneration 只验证有限约定与反例，不替代无限定理。15 份全文及 sidecar
统一列于 `notes/sources/paper7_source_manifest.md`；公开再分发 PDF 前需另行
核验许可。
