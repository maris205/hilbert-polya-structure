# 第一阶段研究摘要：经典流的算术来源与闭轨结构

日期：2026-08-13  
范围：`propose-flow-systems.md` 的 Stage 1，Route A 的 A0（算术自然性）与 A1（经典闭轨结构）  
数据边界：候选冻结、证明与轨道枚举均未使用黎曼零点；有理素数只在本地账本冻结后用于预先声明的反例控制。

## 结论

本阶段得到一个可证明的“两半阻碍”，而不是一个已经通过 Route A 的 Hilbert--Pólya 候选：

1. **Deninger 的 rational-Witt 流给出最强 A0。** 对 `Spec Z` 和显式冻结的有限核 admissibility 条件，闭点 `(p)` 内生地索引一个紧致周期轨道包 `Gamma_p`，包内轨道的最小周期为 `log p`，所有周期轨道也被这些包穷尽。因此它获得 `A0_ANALYTIC_ARITHMETIC_ORIGIN`。但是一个素数对应的是轨道包而非唯一孤立轨道；规范化 packet measure、重数、相位、光滑 monodromy 和 trace 权重尚未导出，所以 A1 只能是 `A1_WEAK`，综合判定为 `ROUTE_A_EXPLORATORY`。

2. **模曲面测地流给出最强 A1，但标准 prime-norm 机制被严格排除。** 对双曲元素 `gamma in PSL(2,Z)`，记 `t=|tr gamma|>=3`、扩张特征值为 `lambda>1`，则

   ```text
   ell(gamma) = 2 log(lambda),
   N(gamma)   = exp(ell) = lambda^2,
   N + N^(-1) = t^2 - 2.
   ```

   `N` 的非平凡 Galois 共轭是 `N^(-1)`。若任意 `r>=1` 使 `N^r` 为有理数，则共轭不变性强迫 `N^r=N^(-r)`，与 `N>1` 矛盾。因此所有重复长度 `r ell(gamma)` 都不可能等于任何 `k log p`。该候选获得 `A1_PASS_ANALYTIC`，但作为标准时钟下的 rational-prime 候选被判为 `ROUTE_A_REJECTED`；它仍被保留为精确的闭轨、稳定性、Selberg/Ruelle 和自然量子化基准。

目前没有候选同时达到严格 A0 和 pass-level A1，因此本阶段**不允许调用 Route B**。

## 容易产生误判的近素数代理

模曲面存在一个危险但可精确解释的数值假象：

```text
q = t^2 - 2 = tr(gamma^2) = N + N^(-1),
log(q) - ell = log(1 + N^(-2)).
```

当 `q` 恰为素数时，`log(q)` 会以 `O(N^(-2))` 的误差逼近真实闭轨长度，长轨道上看起来尤其“准确”。但这不是素数轨道字典：`q=p` 要求 `p+2` 为平方，并强迫 `p ≡ 7 (mod 8)`，截至 `X` 只有 `O(sqrt(X))` 个候选，相对全部素数的覆盖上界趋于零。

冻结后的控制扫描取 `3<=t<=5000`，即 `q<=24,999,998`。在该范围的 1,565,927 个素数中只有 639 个形如 `t^2-2`，观测比例为 `4.08065e-4`；回归斜率为 `-1.9999589`，只是在验证上述误差恒等式的渐近行为，不是对 prime-orbit 对应的支持。

## 闭轨账本与复现

零点无关的枚举使用 `PSL(2,Z) ≅ C2 * C3` 的 primitive oriented cyclic classes，最多 16 个 `S-R` blocks，保留时间反向的 inverse class：

- oriented primitive classes：8,798；
- inversion 商：4,517；self-reverse：236，满足 `8798=2*4517-236`；
- distinct traces：1,020；
- cutoff 内最大同迹重数：36（只是截断下界，不是完整 class-number 结论）；
- 10 个单元测试和 6 个运行时不变量均通过；
- Selberg 系数的双重计算最大绝对残差：`4.44e-16`；
- 有理 norm 命中和 prime-power 长度支撑碰撞均为 0；后二者是代数定理的结果，不是浮点检验。

复现命令：

```bash
cd /root/rh_dyna/flow_systems/papers/1-classical-flow
bash experiments/reproduce.sh
```

结果汇总见 [`results/arithmetic_audit_summary.json`](../results/arithmetic_audit_summary.json)，主账本见 [`results/modular_orbit_ledger.csv`](../results/modular_orbit_ledger.csv)，本地冻结清单见 [`results/orbit_ledger_manifest.json`](../results/orbit_ledger_manifest.json)。`S-R` block cutoff 不是几何长度 cutoff，同迹重数只能解释为 cutoff 内下界。

## 先前工作的继承边界

对六份先前稿件的逐页审计给出以下继承原则：

- 可继承 Logistic/topological 方向中显式的 MSS 缺陷、奇偶约束和“低维模型丢失模信息”的负结果；不可把 conjectural isomorphism、用目标常数校准后的恢复或有限扫描当成定理。
- Uniform Young tower 结果只能在其强假设下使用；普通 Birkhoff 平均不会自动产生 `1/log n` 包络。
- 可继承保面积 Hénon 映射 `F(x,y)=(1-a x^2-y,x)` 的可逆性、`det DF=1`、双曲不动点与稳定/不稳定流形几何；不能继承以黎曼零点为目标的参数拟合、近似连续 Hamiltonian 或缺少 holdout 的谱匹配。
- 极新的有限 Hermitian/Weil 压缩稿件可作为形式化结构 benchmark，但截至本阶段只能标为“形式化强证据、外部共识未建立”，而且它本身不是经典流构造。

完整审计见 [`prior_work_audit.md`](prior_work_audit.md)；每个关键来源的身份、公式位置和限制见 [`source_verification.md`](source_verification.md)。

## 最小下一步

若继续 Stage 2，应以本阶段的否定结果作为硬约束，而不是重新拟合模曲面：

1. 对 Deninger packet，尝试构造 `Gamma_p/R` 上 functorial 的 canonical transverse measure，或一个真正的 groupoid/Lefschetz trace，使整个 packet 的重复贡献从几何中导出，而不是手动“每包计一次”。
2. 将模曲面的 Ruelle quotient `Z(s)/Z(s+1)` 作为振幅基准：它可以消去 Selberg 稳定性分母，却不能修复算术支撑、同迹重数或自伴宿主问题。
3. 任何新流必须先通过同样的 source lock、禁用数据、proves-too-much controls 和 primitive/repetition ledger，再讨论零点或量子化。

正式论证、限制和引用见 [`paper/paper.pdf`](../paper/paper.pdf)；机器可读判定见 [`DEN-WITT-Z-FIN`](../../../evaluations/route_a/DEN-WITT-Z-FIN/2026-08-13-stage1.yaml) 与 [`MOD-GEO`](../../../evaluations/route_a/MOD-GEO/2026-08-13-stage1.yaml)。
