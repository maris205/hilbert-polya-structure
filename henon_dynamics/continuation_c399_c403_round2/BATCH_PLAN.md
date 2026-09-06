# C399–C403：五篇合同冻结计划

冻结日期：2026-09-05；基线 `1667dfc0c24e10a8a3627e80f93e301538d18012`。
用户“确认，下一轮”续接尚未完成的 C399–C403，不跳号、不开启第六篇。
本计划在三个新合同完整证明及独立内部审查完成后冻结；冻结不是论文发布。

## 编号与五个独立问题

| 编号 | 精确对象与时钟 | 一个论文级问题与新增范围 | 主要载荷 |
|---|---|---|---|
| C399 | `T(x)=a x-b/x`，`a,b>0`，删除全部 prepoles 的有限实域；原整数迭代；正稳定性分母 `(T^n)'−1` | 全参数有限实稳定性乘积、完整共振除子及抛物转变处的双侧补偿极限；域、无权计数及圆周谱扣归经典来源 | [已完成 9 页正文](../research_c399_c403/boole/paper/main.pdf)、[完整证明](../research_c399_c403/boole/PROOF_PACKAGE.md)、[正文审查](../research_c399_c403/reviews/BOOLE_MANUSCRIPT_REVIEW.md) |
| C400 | 半直线 Dirichlet 谱问题，`x_n=πH_n` 的等强度有限正 δ 梳；频率 `k=√E`，原长度 | 每个有限 `κ>0` 的 `2k log k+[log(4π/κ)+γ−2]k+Oκ(log k)`，及范数预解式 Dirichlet 极限与高能极限不交换；模型与经典离散性归原作者 | [已完成 14 页正文](../research_c399_c403/delta_comb/paper/main.pdf)、[完整证明](../research_c399_c403/delta_comb/PROOF_PACKAGE.md)、[正文审查](../research_c399_c403/reviews/DELTA_MANUSCRIPT_REVIEW.md) |
| C401 | `H(x,y)=(y,f(y)−ax)` over `F_q`，`deg f=d≥2`、`a≠0`；`A²(overline F_q)`；保留 Hénon 时钟 `n` 与 Frobenius 时钟 `r` | 对 `d^n≠q^r` 证明精确约化交数 `max(q^(2r),d^n q^r)`；非 p 幂次数族全部双时钟成立；给出边界局部长度与精确短时缺陷/阈值，不冒称 eventual trace 原理新颖 | [完整合同及证明](henon_arithmetic/CONTRACT_SCOUT.md)、[独立证明审查](reviews/HENON_ARITHMETIC_PROOF_REVIEW.md) |
| C402 | 首一复 Hénon `H(x,y)=(p(x)−ay,x)`、`deg p=d≥2`、`a≠0`；固定一元多项式坐标权重 `q(π₁P)`；原周期 `n`，带负号全局留数约定 | 所有周期共用一个有限边矩阵 `W`，`τ_n=−Tr W^n`、`D(z)=det(I−zW)^(−1)`；增量为任意次数坐标权重的周期无关流界与闭合，Hill/单位权重/固定系统留数算法均扣归既有工作 | [完整合同及证明](nonlinear_return/CONTRACT_SCOUT.md)、[独立证明审查与修订闭合](reviews/NONLINEAR_RETURN_PROOF_REVIEW.md) |
| C403 | `a(k)=k^(−σ)L(k)`，`σ<1/2`，正可测慢变 `L` 在紧区间上下有界；非乘性亦可；整除 Toeplitz 截断 Gram，截断时钟 `N` | 正规化 Gram 在每个且仅每个 `q(1−2σ)>1` 的 `S_q` 拟范数收敛到经典 LCM 核；包括 `q<1`，证明统一尾界。LCM 谱渐近、素数张量及原有限偶整数结论不算新增 | [完整证明](spectral_regular_variation/PROOF_PACKAGE.md)、[来源核对](spectral_regular_variation/SOURCE_AUDIT.md)、[独立证明审查](reviews/SPECTRAL_REGULAR_VARIATION_REVIEW.md) |

五个问题分别是实稳定性除子、奇异谱渐近、有限特征双时钟交数、复留数全周期压缩、非乘性算术 Gram 理想拓扑极限。没有把一个结果按参数或推论拆成五篇。
每个新合同的反例/替换条件见其完整合同；来源检索有界，不认证全球优先权。

## 冻结输入与审查裁决

- C399/C400 全部既有证明、正文、PDF、审查、构建日志及旧清单保留原字节。
  其原计划中的“未编号/待审查”等语句描述前轮快照，不是本轮当前状态；
  本计划只作编号映射，不回写历史。此前完成的双新目录确定性构建与全部
  页面 QA，在源文件及工具环境不变时复用，不为换编号重跑。
- C401 合同 SHA-256：`a891beca49be4b1cc2a460a4320596097a22c13a39056e20727db5058b982378`。
  证明审查无 blocking；正文中采用“有限态射次数”，并准确指向源版本
  Example 3.6 后的阈值讨论，避免未核实的 remark 标签。
- C402 最终合同 SHA-256：`b8780f67d4a9a23e66d2d0fe3f5a2c3c77a50c53a5930697baa00b23e8c28dfb`。
  审查状态 `PROOF_PASS_MINOR_ITEMS_CLOSED`，0 blocking、0 未闭合 minor。
  不扩成任意二元权重或自然 Banach 转移算子。
- C403 证明 SHA-256：`0f8e436657de4207087137502236b2d48f69dae947f368b5d586039b7a282fee`。
  独立证明审查无 blocking；正文须保留 L 的局部上下界假设。

上述均为当前团队独立内部检查，不是外部专家评审或录用意见。冻结后的
新证明错误须修复并做受影响复核，不用既有审查自动覆盖新版本。

## 剩余完成门槛与写入分工

1. 三篇新稿各含完整量词、全部证明、来源所有权和适用边界；作者各自
   只写所属 lane 的 `PAPER_PLAN.md`、`paper/`、初编译收据。
   C401：arithmetic 作者；C402：nonlinear 作者；C403：charp reviewer 转作者。
2. 新稿由非作者独立核对全文、引文与已有证明的对应，修复真实问题后
   只复核受影响部分。已有精确检查输出不因 TeX 转写重复计算。
3. 协调者按完整 Route A v0.2.0 及其来源路由评估五篇，保存完整 tuple、
   scope flags 和未做/不适用的理由。哈希固定为
   `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`。
4. 每份新终稿两次空目录确定性构建、字节比较、日志/字体/文本检查、
   全页目视；不规定页数。原两稿复用已验证且输入不变的收据。
5. 批次载荷清单与自排除 manifest 覆盖实际交付依赖，最终只读核验；
   不增造发布代码，不宣称哈希证明数学正确性。保存真实命令和退出状态。
6. 协调者独占 CURRENT、批次总结、评估、共享索引及 Git；精确暂存，
   先检查远端变动，再按授权提交同步，保留八个遗留未跟踪目录。

## 算术和历史依赖边界

`NO_BAD_EULER_OR_ROOT_NUMBER` 始终有效。源系统算术、有限维行列式、
自伴源算子、平均计数律都不能替代目标 Euler 因子、root number、自守性、
目标零除子对应或 Hilbert–Pólya 实现。没有 Route B 授权；不预填 A2/A3 通过。

C108 旧 producer 的二周期方程与指定映射不符；本轮独立反例将以新路径
单独记录并在状态入口隔离依赖。修复历史冻结载荷不在此轮普通新增写稿
操作内，旧字节不改，纠错本身不另算论文。

`paper-plan → paper-write → paper-compile` 仅用于完整数学论述和可复现 PDF；
不采用其旧模型/外部 API、ML 实验或版式配额。ARS 的适用写作及完整性
检查保留；没有调用或宣称完整十阶段运行、外部上传或期刊投稿。
