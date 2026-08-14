# Session 5 批次报告：论文 2--6

封板日期：**2026-08-13**  
研究依据：[`propose-flow-systems.md`](propose-flow-systems.md)、
[`skills/route-a-evaluator.md`](skills/route-a-evaluator.md) 与
[`skills/route-b-evaluator.md`](skills/route-b-evaluator.md)

本批连续完成五个论文项目。所有候选定义、时钟、归一化、算子域和 Route
判定均在使用目标零点前冻结；本批没有使用黎曼零点拟合、训练、筛选或参数
调整。五篇发布稿均经过独立数学审稿、来源/引用审计、PDF 构建检查和确定性
复现。

## 1. 五篇论文各自一句话总结

| 论文 | 一句话总结 | 当前判定 |
|---|---|---|
| [Paper 2](papers/2-flow-zeta/paper/paper.pdf), *Arithmetic Period Packets and the Missing Trace* | Deninger 的每个素数 packet 含不可数条同长本原轨道，普通逐轨 Ruelle 乘积因而在单个 packet 内即发散，而测度/群胚替代尚缺规范 lift、跨素数质量和 trace-bearing operator。 | `DEN-WITT-Z-FIN`: `ROUTE_A_EXPLORATORY`; Route B 不可调用。 |
| [Paper 3](papers/3-trace-bridge/paper/paper.pdf), *One Orbit Is Not a Trace* | `T0--T7` 同一对象证书证明局部 orbit germ 不决定全局 trace，且模曲面全部重复闭轨长度与所有 `k log p` 严格不相交，排除了坐标式拼接。 | Deninger 保持探索；`MOD-GEO`: `ROUTE_A_REJECTED`。 |
| [Paper 4](papers/4-arith-flow/paper/paper.pdf), *One Clock, One Characteristic* | `P^1/F_2` Frobenius suspension 给出闭点、闭轨、点计数与 Hasse--Weil zeta 的完全精确正控，同时证明一个固定有限域时钟不能覆盖 characteristic-zero 的全体有理素数。 | 原生有限域 `ROUTE_A_SUCCESS_ROUTE_B_NOT_READY`; 黎曼目标与逐素数编译器均 `ROUTE_A_REJECTED`。 |
| [Paper 5](papers/5-quantum-flow/paper/paper.pdf), *The Canonical Koopman Lift Is Too Large* | 自然 Koopman 生成元虽定义完整且自伴，但其点谱为 `(2*pi/log 2)Q`、每点无穷重且全谱与本质谱均为 `R`，所以在 Route-B 的 B3 谱型门槛严格失败。 | 有限早期审计：B1、B2 通过，B3 失败；B4、B5 不调用。 |
| [Paper 6](papers/6-cohomological-owner/paper/paper.pdf), *Which Operator Owns the Zeta?* | 精确 Hasse--Weil 行列式由分次 étale Frobenius 拥有，而自伴悬挂时间由不同的 Koopman 算子拥有，共同算术母体不足以合并成同一 Route-B 证书。 | 原生有限域 `ROUTE_A_SUCCESS_ROUTE_B_NOT_READY`; 黎曼目标 `ROUTE_A_REJECTED`; 有限完整 Route B `ROUTE_B_REJECTED`。 |

## 2. 当前最强进展

最强正进展是一个没有拟合成分的有限域同源校准链：对冻结的
`P^1/F_2`，闭点、primitive cycles、悬挂闭轨、
`#P^1(F_{2^n})=1+2^n`、Lefschetz 迹、Euler 乘积和分次上同调行列式
全部精确相容。这给出了后续任何 characteristic-zero 候选必须达到的最低
“同一对象、同一时钟、同一重复账本、同一行列式拥有者”标准。

最强负进展是把“看起来共享结构”升级为两个可证明的排除原则：

1. **同一长度或局部奇性不等于同一全局 trace。** Paper 3 的
   `T0--T7` certificate 阻止从不同系统分别摘取周期、振幅、谱和行列式。
2. **同一算术母体不等于同一算子。** Paper 6 证明 Frobenius 的精确
   determinant credit 不能转移给自伴 Koopman 生成元；有限维 block repair
   也不能消除后者的本质谱、无穷重和非紧性。

这两条原则显著缩小了可行研究空间：下一候选必须在一个冻结对象内同时给出
素数幂账本、trace、算子域、谱型和全局 determinant，不能再依靠跨对象或跨
算子的“拼装式对应”。

## 3. 当前主要障碍

1. **characteristic-zero 素数时钟仍无合格动力来源。** 模曲面标准 norm
   不是有理素数，固定有限域又只产生单一 characteristic 的度时钟；人为逐
   素数圆周虽能编译任意 Euler 乘积，却因 `PROVES_TOO_MUCH` 失去解释力。
2. **Deninger packet 的 measured trace 尚未成为数学对象。** 普通 orbitwise
   计数已被否证；替代方案至少还需要来源内生的 packet Haar lift/disintegration、
   跨素数 component masses、可测全局 assembly、trace domain 和与 flow
   return map 相连的算子或群胚。
3. **自然自伴时间算子的谱过大。** 当前 Koopman lift 的稠密、无穷重本质谱
   排除紧预解式、正宽区间局部有限计数和 trace-class heat；调整正 component
   weights 不会改变这一点。
4. **completed `xi` 的全局结构尚未出现。** 现有正控只拥有有限域
   Hasse--Weil determinant；它没有给出有理素数幂显式公式、无穷位 Gamma
   因子、`s <-> 1-s` 对称或同一自伴算子的 zeta-regularized determinant。

## 4. Route A / Route B 当前状态

### Route A

- **已建立的成功仅是正控：** 原生有限域 Frobenius suspension 在其自身
  Hasse--Weil 目标上达到 `ROUTE_A_SUCCESS_ROUTE_B_NOT_READY`。
- **仍存活的探索路线：** `DEN-WITT-Z-FIN` 保持
  `ROUTE_A_EXPLORATORY`，但在 A2/A3 前必须先构造可检验的 measured trace
  与 operator bridge。
- **已拒绝的当前实现：** 标准模曲面 rational-prime 映射、固定
  `P^1/F_2` 面向黎曼目标的解释，以及 prescribed norm-circle Euler compiler。
- 因此目前**没有 rational-prime 候选可以晋级为
  `ROUTE_A_SUCCESS_ROUTE_B_READY`**。

### Route B

- Paper 5 的自然 Koopman 算子通过 B1（完整定义）和 B2（自伴），在 B3
  （所需离散谱型）失败；该论文没有调用 B4/B5。
- Paper 6 经授权做有限完整审计：B1/B2 通过，B3/B4/B5 失败，整体
  `ROUTE_B_REJECTED`，`hilbert_polya_claim_allowed: false`。
- 当前 Route B **整体不就绪**。有限域上同调 determinant 不能替代复 Hilbert
  空间中同一自伴算子的 trace/determinant 证明。

## 5. 下一批最值得继续的方向

按价值与可证伪性排序：

1. **Deninger packet-groupoid 硬门审计。** 只研究能否从既有来源或明确新增
   公理构造 N2 lift/disintegration、N3 component masses 和 trace-bearing
   representation；若不能，给出条件化 uniqueness/no-go 定理并关闭路线。
2. **同一算子拥有权搜索。** 在核算子/anisotropic transfer space、相对 trace
   或上同调动力框架中，优先寻找一个同时拥有 primitive ledger 与 determinant
   的单一算子；先冻结空间、域、scalar field 和 trace class，再讨论黎曼目标。
3. **adèlic / 多 characteristic 时钟的自然性门槛。** 研究是否存在非逐素数
   拼接的全局 arithmetic assembly，并把 one-clock obstruction 推广为可判定
   的多时钟定理。
4. **Weil 显式公式的有限压缩基准。** 对最新形式化/有限 Gabor 压缩结果做
   独立来源和同一对象审计，检验其 prime-power trace、Hermitian form 与
   operator ownership 是否能提供接口；在外部共识形成前只作为暂定强证据。
5. **暂不回访已关闭的修补。** 正 component reweighting、模曲面 trace/norm
   换名、有限维 block sum、目标零点拟合和逐素数圆周编译器均已有结构性反例，
   除非出现改变 frozen object 的新定理。

## 6. 发布与复现锁

| 论文 | 页数 | 确定性测试 | 发布 PDF SHA-256 | 独立审稿 |
|---|---:|---:|---|---|
| Paper 2 | 20 | 5/5 | `86a60810f1f2a975bc5e694cb854a7de4bb796168f9a273888c013f84323a183` | 修订后通过 |
| Paper 3 | 14 | 11/11 | `7ba58d4c389f476950125975c0c041e76d7691b8d0f769ab69ce319f8ed4fde7` | ACCEPT |
| Paper 4 | 16 | 13/13 | `775c6016ae17fceb2f875b3cc5608563efae85b037553d8167597c4c45b5ae6a` | ACCEPT |
| Paper 5 | 14 | 8/8 | `802ad1a1169be166d5a82da2e0247a92e6c848113303c7d70818bbdfd90acef5` | ACCEPT |
| Paper 6 | 9 | 10/10 | `f8eccdd7d486a10885d6f5502ad929f08d5ce27b14cb2457f1de8999b9f14573` | ACCEPT |

合计：**47/47** 项确定性测试通过。Paper 3 的 8/8 artifact manifest 与
Paper 6 的 5/5 artifact manifest 另行通过；全部 11 份历史/当前 Route YAML
均可解析。各论文的 `notes/` 目录保存 proof、source、citation、peer-review
与 release audit，正式结论以表中发布 PDF 哈希和最新 Route YAML 为准。
