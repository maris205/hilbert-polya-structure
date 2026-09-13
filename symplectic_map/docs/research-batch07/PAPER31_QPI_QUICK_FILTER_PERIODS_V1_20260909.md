# Paper31：I08／I10 周期方向首筛 V1

日期：2026-09-09 UTC；执行席：`/root`。
状态：`FIRST_PASS_FILTER_ONLY`，不是完整查新、数学接受或正式候选票。
技能：`idea-creator` Phase 3，按 `research-lit` 逐源核读；未进入数值／GPU实验。
`route_applicability: NOT_APPLICABLE`；这里不提出 Riemann 行列式主张。

## 1. 输入及读取身份

主控已全文读取本轮[十项问题](PAPER31_QPI_IDEA_GENERATION_V1_20260909.md)164行、
[景观](PAPER31_QPI_LANDSCAPE_V1_20260909.md)208行、
[组合内基线](PAPER31_QPI_PORTFOLIO_BASELINE_V1_20260909.md)121行和
[两接口接受](PAPER31_QPI_DISCOVERY_INTERFACES_DISPOSITION_V1_20260909.md)。
景观／基线的全文读取发生在本连续发现阶段，非本文件新增的15篇原文全文阅读。

| 输入 | 本轮 SHA-256 |
|---|---|
| 十项问题 | `385ee36d1788b4060d8371150e2d2db8a86484231999ce08b085328ea787e9dd` |
| 景观 | `a2597b8d90a19bc9e1d7d36345cab9564c86170f2305255016a38257d42d69a9` |
| 组合内基线 | `9f7b0971dfe741f2dd4f2785c08fc7a83d2eb9e67613f02cf5409790a5cd1374` |
| 两接口接受 | `909b3adfae273991d44c02ddeafe158d9e1039c96a630cf3a75c5f576f5dbba7` |

必须先扣除原有限域的全部闭纤维自治共轭、指定回返点、点阶决定的完整循环清单及 P11 通用群论计数。
新的统计不能把已知但未数值确定的 $d_h=\operatorname{ord}(P_h)$ 再作为最终答案的未知输入。
I08 的有限域能级族与 I10 的固定有理能级跨素数问题严格分开。

## 2. 实际查询

每项恰三条首筛查询；Q7是命中后的精确书目定位，不假称第四个独立问题检索。

| 号 | 对象 | 实际 query |
|---|---|---|
| Q1 | I08 | `Jones Rouse Galois theory iterated endomorphisms elliptic curve point global fields 0706.2384 theorem` |
| Q2 | I08 | `finite field elliptic surface point order distribution Kummer monodromy rational elliptic surface fixed family` |
| Q3 | I08 | `"Kummer" "point order" "finite fields" elliptic monodromy` |
| Q4 | I10 | `elliptic analogue Artin primitive root conjecture Gupta Murty 1986 GRH point generates reductions` |
| Q5 | I10 | `"elliptic" "primitive points" "2026" density` |
| Q6 | I10 | `"37a1" "primitive" "density" elliptic` |
| Q7 | 来源定位 | `"Locally imprimitive points on elliptic curves" arxiv Jones Pappalardi Stevenhagen` |

Q2/Q3产生大量 Kummer 曲面／密码学噪声，Q6产生无关 L 函数材料；均不计相关证据。
不根据检索未命中宣告全球新意；完整近期、多源逐核心主张查新留给幸存者。

## 3. 已实际读取的一手来源

**S1. Jones–Rouse, Galois theory of iterated endomorphisms.**
[arXiv v4](https://arxiv.org/pdf/0706.2384v4)，2009-11-07版本；2010年发表于 PLMS。
本人读摘要与完整引言，并定向读 §3 的 Theorem 3.2、3.4、Lemmas 3.5–3.7、Theorem 3.8，
及 §5 的 Theorem 5.2、Corollary 5.3、Example 5.4 和 Theorem 5.5 的陈述。
包括相关证明，但不称40页全文审计；合并输出截断时另行补读 Theorem 3.2。
该文已将分点塔、仿射 Kummer 群和点阶的素数幂信息联系起来；基础范围明确包括全局函数域。
§3 区分 Dirichlet 密度与函数域自然密度；§5 的满 $\operatorname{GL}_2$ 假设不自动适用于代数闭常数的几何 $\operatorname{SL}_2$。
因此原族满像、固定行列式和固定次数有限域计数仍要核实，但通用研究方案不是新增机制。

**S2. Gupta–Murty, Primitive points on elliptic curves.**
[Compositio 58 (1986), 13–44](https://www.numdam.org/item/CM_1986__58_1_13_0.pdf)。
本人读刊本首页引言和 Theorem 1 的开头条件，不称全文核验。
CM、分裂素数及 GRH 条件必须保留；它不能供应 I10 指定非CM曲线的无条件正密度。

**S3. Jones–Pappalardi–Stevenhagen, Locally imprimitive points on elliptic curves.**
[2026刊本](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/FBEB9EA77B0CBC3EF462666C911C7E8E/S0305004125101795a.pdf/locally_imprimitive_points_on_elliptic_curves.pdf)，180，663–683，在线日期2026-01-29。
本人读刊本摘要、§1完整引言、§2至 Lemma 2.3 的陈述；不把该引理后证明或后续分类称已审。
刊本把固定点生成整个约化群的问题与循环约化分开，指出前者无界分裂条件的解析控制仍有缺口。
其局部不可原始点分类还提醒：全球不可除不自动意味着跨素数原始点正密度。
搜索可返回出版全文，但一次正文打开失败、后一次PDF读取超时；没有绕过限制。

**S4. Murty–Naik, A Non-abelian Large Sieve and Artin’s primitive root conjecture.**
[arXiv:2608.21573v1](https://arxiv.org/html/2608.21573v1)，2026-08-21。
本人读摘要与§1全部定理陈述及条件，不称证明审查。
Theorem 1 仍假设指定非阿贝尔大筛不等式，且对象是乘法群；不能把新题名误读成无条件解决 I10。

**未作正文证据的命中。**
Benoist–Perucca 的[机构记录](https://orbilu.uni.lu/handle/10993/64259)显示2026-04-08版本、2025-02-13起可获取。
本人只读元数据；下载链接打开内部错误，命令行对该站证书校验失败，未禁用校验。
不据此书目的标题或摘要声称其具体定理已经覆盖／解决本题。
arXiv 的 `2304.03964v3` HTML 一次404；改读已公开的实际出版PDF，不虚构该HTML的内容。

## 4. I08：保留用于深查，但通用部分先扣除

处置：`KEEP_FOR_DEEP_VALIDATION / HIGH_RISK / NO_NOVELTY_SCORE`。

原目标是 $E_{T,h}:v^2+huv-Tv=u^3-Tu^2$ 的原 $P=(0,T)$，
不是任选一个能方便满足满像的点，也不改动回返的时间／状态权重。
“识别为 Tate/QRT/Lyness 模型”“建立抽象分点塔”“有限群共轭类比例”均不能独计新意。
目前可保留的实际输入是：统一验证原固定 $T$ 能级族的仿射像、所有声明的参数例外、
随 $q$ 的 Frobenius 行列式层，以及真正对应点阶的截断与尾项。
这能把循环表中未知的点阶输入变成可证的族统计；若最终只剩某个泛参数的标准套用，则淘汰。

数学可行性正在独立并行核查，不在此提前合取为已证。
有界线索为 $p\ge5,T\ne0,-27/256,\ell\ge5,\ell\ne p$：
原有理椭圆曲面的 $I_8+4I_1$、prime-to-$p$ 同源的高度约束、原点的不可除性与 Kummer 提升。
即使这一范围证明成功，也不授其他时间、小特征、小辅助素数或完整跨素数密度。
不使用“$P\in\ell E(\mathbb F_q)$ 等价于 $\ell\nmid\operatorname{ord}(P)$”这一错误替代。
在 $v_\ell\#E_h<k$ 的有限层可以尝试从实际仿射数据恢复点阶的 $\ell$ 部分；
尾层若未处理，就保留误差和范围，不改写成所有周期的精确分布。

资源：没有缺数据／GPU障碍；GPU预算及实际耗用均0。
可先做3–5天规模的纸面诊断；完整统一定理按原生成件估计2–3月，当前不把此估计当完成承诺。
容量与独立价值仍未知；22–30页需完整新核心及必要旧证明真实共存，不能据猜想预授PASS。

## 5. I10：当前形式淘汰，不宣告数学不可能

处置：`ELIMINATE_THIS_FORM — FEASIBILITY_AND_UNBOUNDED_ANALYTIC_INPUT`。

原指定 $T=1,h=2$ 下，$Y=v+u$，再令 $y=Y-1$，得到
$y^2+y=u^3-u$，而 $P=(0,1)$ 映为 $(u,y)=(0,0)$。
这是代入等式的直接核对，不是新的模型分类。
**恰好同一曲线和点**已出现在 S1 的 Example 5.4，连各素数分点塔的满像核验都已有来源。
所以“先确认点非挠、核固定低层满像”不能成为本项的新诊断核心。
S1 的单个辅助素数点阶密度不供应“生成整个 $E(\mathbb F_p)$”所需的无界跨素数尾控制。
S3 的2026年刊本与 S4 的最新条件结果没有给出本题缺失的无条件解析桥。

本轮没有证明某个障碍迫使密度为零，也没有证明该特殊曲线的全部相关问题无解。
淘汰的是“以当前已知输入承诺一次完成无条件正／精确密度长文”的形式。
若以后有真正新解析输入，应作为新输入重新判断；有限扫描或静默加GRH不算修复当前目标。
GPU0，实际未运行此项扫描；计算百万素数不能提供所缺证明。

## 6. 接续与边界

本件仅补足十项首筛中的 I08 与 I10；其他八项由独立席完成。
I08 尚须逐核心主张深查及独立反对意见；I10 不进入当前幸存者列表。
没有正式四门、论文立项、锁、试写、编译或PDF；Batch07仍4/5，旧接受与失败均不变。
本轮没有持久下载论文到 `papers/`／`literature/`；PDF只经公开读取工具或内存管道作定向核读。
保存后全文自读、核直接本地链接及终态哈希；唯一新增本报告。
