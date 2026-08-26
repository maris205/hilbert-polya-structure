# Paper 9 中文阶段摘要

## 一句话结论

对每个有理素数 `p`，Deninger 有理 Witt 有限核系统中的真实素数 packet
`Gamma_p`、其中每条继承周期轨道以及时间轨道商 `Q_p`，在悬挂商中实际继承的
拓扑下都是非平凡不可分空间；相应限制轨道关系不是闭关系。

## 最强新定理

令

```text
A_p = product_{ell != p} Z_ell,
U_p = A_p^x,
D_p = Z[1/p]_{>0}.
```

本文首先给出一个构造性同时逼近：对任意 `c>0` 与 `a in A_p`，可选
`q_j=m_j/p^{k_j}`，使 `q_j -> c` 在实拓扑中成立，同时 `q_j -> a` 在全部
prime-to-`p` 的 profinite 坐标中成立。关键是把同余条件施加在有理数
`q_j` 本身，即令 `m_j = a_j p^{k_j} (mod M_j)`，而不是只控制分子。

当 profinite 端点为单位时，这个序列还能在同一个固定 `E_f` 原始特征纤维
内合法提升：所有逼近特征仍有有限核，并在逐个有限阶元素上最终稳定。之后才
依次通过 Galois 商和初始余极限嵌入，避免把 raw character、商点与 colimit
点混写。

将两步结合后，对 packet 内任意有序点对 `x,y`，可构造一列上游代表，它们
全部属于 `x` 的同一悬挂等价类，却收敛到 `y` 的代表。因此商空间中的常值
序列 `x,x,...` 收敛到任意 `y`。这精确推出：

- `Gamma_p` 非平凡且不可分，因而非 `T0`、非 `T1`、非 Hausdorff；
- 每条真实继承周期轨道的子空间拓扑同样不可分；
- `Q_p=Gamma_p/(R_{>0}/p^Z)` 非平凡且不可分，集合上虽为 `U_p/H_p`，但不能
  据此认作既有紧 Hausdorff 群 `B_p`；
- 限制对角轨道关系存在显式“相关点列收敛到不相关点对”的见证，因此非闭。

## 对 Paper 8 的版本化更正

Paper 8 把真实继承单轨当作标准 Hausdorff 圆，并在此基础上使用标准 LCH
作用群胚。Paper 9 证明这一拓扑前提为假，因此真实 packet/轨道的标准
LCH--Hausdorff branches 在 A1 前提处被否证。

更正是 owner 重归属，不是抹掉旧数学：

- Zak/Floquet 分解、Poisson 公式、regular FNS trace 与有限角 normality
  obstruction 在显式赋予普通圆拓扑的 proxy 上仍严格成立；
- `Tau_L(a_f)=L f(0)` 的回归盲性与
  `tau_0(a_f)=L sum_r f(rL)` 的重复 comb 都改由标准圆 proxy 拥有；
- 这些 proxy 结果不再获得真实 Deninger 轨道的拓扑、Haar、完备化或 trace
  transport credit；
- coefficient-one 正时间 scalar ledger `Theta_+` 不依赖 packet 拓扑，保持
  原结论不变。

## 阿代尔与 scaling-site 分型

本文另证，朴素双重商
`Q^x \ A_Q / Zhat^x` 中真实继承的素轨道 `C_p` 也是不可分空间。修正后的
Morishita 映射在真实 `E_f` 轨道与这个真实阿代尔轨道之间仍可成为同胚，但
这是两个不可分空间之间的 actual-to-actual 同胚。

Connes--Consani scaling site 内生赋予的 `C_p` 则具有普通 Hausdorff 圆拓扑；
它与朴素双重商子空间、以及人为标准圆 proxy 是不同 topology owners。集合
对应或相同的 `p^Z` 稳定子不足以传输拓扑。

## Route A/B 状态

Stage 9 冻结八份 Route-A 记录：

- 真实 packet 与继承轨道拓扑定理：`A1_WEAK`；
- 真实 packet/轨道标准 LCH 分支：`A1_FAIL`；
- `Q_p` 裸轨道商：`A0_WEAK_ARITHMETIC_RELATION, A1_FAIL`；
- 标准圆裸 proxy：`A1_WEAK`；
- 标准圆 regular-trace proxy：`A1_FAIL`；
- 标准圆 trivial-character proxy：`A1_PASS_ANALYTIC`。

八者全部为 `A2_FAIL/A3_FAIL/A4_FAIL`，overall 均为
`ROUTE_A_EXPLORATORY`。Route B 未调用，也没有 Stage-9 Route-B YAML。

## 复现与发布

- 20/20 deterministic controls 通过；
- 8 个 CSV，共 240 行；
- 两次全新生成逐字节一致；
- 控制 manifest SHA-256：
  `52e7a4242f91fcff1b622c9455e90ad3380ae40e742e15bf5b922a3dd4415668`；
- 21 页论文 PDF SHA-256：
  `c55e4f45fe5f58841864e9af695c4664bdb1a77cff6e087fd2869d4ecd385e02`；
- 独立引用审计与同行评审均为 `ACCEPT`，未解决问题 0/0/0。

本地来源 PDF 仅用于核验；公开同步时必须排除 `notes/sources/*.pdf`，除非精确
manifestation 的再分发许可已有记录。论文中的 CRediT、利益冲突、资助、致谢
及最终 AI 披露仍需作者在正式投稿前确认。

## 下一项最小问题

既然每个真实 packet 都不可分，下一步不应再假设存在标准圆拓扑，而应直接
研究它的 `T0`、Hausdorff 与完全正则反射，以及连续复值函数、Borel 可观测量、
概率测度和连续算子场能否保留任何 packet 内信息。若所有分离反射都坍缩为
单点，就能把“拓扑代理的必要性”升级为严格的连续可观测量 no-go；若仍有
非平凡信息，则那才是后续非 Hausdorff 算子路线应使用的合法 owner。
