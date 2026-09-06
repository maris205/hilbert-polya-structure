# 算术 Hénon scout：三个候选，零个保留合同

日期：2026-09-06。状态：**scout 完成；0 个 paper-level 合同**。
本报告不占 C404–C408 中的论文编号，不是正式 Route-A 评估，不是新论文。
只新增本目录；未改旧封存包、CURRENT、注册表、其他 lane 或 Git。

## 决定与范围

| 候选 | 决定 | 决定性原因 |
|---|---|---|
| 普通周期方案的跨素数 Galois／Artin 所有者 | 不保留 | 有自然算术对象，但固定周期框架及低周期实例已拥有；全周期 Galois 增量未证明 |
| 加性 Hénon–Frobenius 真共振 | 不保留：来源碰撞 | 明确落入二维向量群的 confined endomorphism；经典理论覆盖所提机制 |
| 非加性 Hénon–Frobenius 真共振 | 不保留：证明未闭合 | 低阶精确反例击破常密度外推；全部 p-power 抵消塔仍无证明 |

这不是对所有算术 Hénon 模型的 no-go。尤其第三项属于“未完成”，不是
“已排除”。没有把源系统计数、经典 Artin 因子或一次计算成功提升为目标
A2/A3 成功，也没有 Route B 或额外发表授权。

## 1. 普通周期方案跨素数：对象自然，但没有新的全周期定理

### 精确候选

取保面积二次族

\[
H_c(x,y)=(y,y^2+c-x),\qquad c\in\mathbb Q^\times,
\]

并令 \(X_{c,n}=\operatorname{Fix}(H_c^n)\) 为仿射周期方案，
\(E_{c,n}\) 为其几何支撑中最小周期恰为 \(n\) 的点集。
参数整模型可取 \(\mathbb Z[c,c^{-1}]\) 上的循环递推方案；固定有理参数后删去
分母及所讨论周期的坏素数。不能假设同一个有限坏素数集合对所有周期适用。
时钟分别是动力周期 \(n\)、素数 \(p\)、扩域次数 \(r\)；不是一个时钟。

候选 observable 是 Galois 置换表示

\[
\rho_{c,n}=\mathbb Q_\ell[E_{c,n}],\quad
T_{c,n,p}(r,j)=\operatorname{Tr}
(\operatorname{Frob}_p^rH_c^{-j}\mid\rho_{c,n})
\]

（在良约化、未分歧处作相应识别），以及固定 \(n\) 的 Artin 局部行列式。
这里 Frobenius 在点上采用 \(z\mapsto z^p\) 的算术 convention；对偶的
几何 Frobenius convention 需同时反转。可设想的实质问题是对整个周期族
证明 Galois 像、周期之间的兼容性或自然 trace／determinant，而不是重命名
一个有限置换因子。

### 便宜决定性检查及库内所有权

先把对象映射到已有 [C12A 推导包](../../henon_frobenius_scheme_obstruction/DERIVATION_PACKAGE.md)
及其 [来源碰撞记录](../../henon_frobenius_scheme_obstruction/SOURCE_AUDIT.md)。
这些文件已证明循环周期方案有限平坦、固定周期 Frobenius 置换行列式、
nilpotent-blindness，以及普通矩形计数不能恢复完整 joint action。
从 \(H_A(q,p)=(1-Aq^2-p,q)\) 经 \((x,y)=(-Ap,-Aq)\)，得到上述
\(c=-A\) 的族，故不是靠换坐标得到新对象。

固定周期的特征零约化代数分解为有限个数域时，其跨素数 zeta 是相应
Dedekind zeta 的乘积（删去相应坏因子）。这确实是算术，但这一所有者
已经存在。\(R(x,y)=(y,x)\) 满足 \(RH_cR=H_c^{-1}\)；Galois 同时
与 \(H_c,R\) 交换，故控制组还必须保留这一 dihedral 约束。

最强的便宜反例是“低周期因子等于新 Hénon 算术编码”这个增量标准本身：
\(c=-6\) 时固定点域为 \(\mathbb Q(\sqrt7)\)，真二周期点域为
\(\mathbb Q(\sqrt3)\)。它们给出的 \(\zeta L(\chi_{28})\)、
\(\zeta L(\chi_{12})\) 是已有经典因子；并不能声称它们没有全局零点。
这两个实例仅从既有证明读取，未重跑旧程序。

### 最近主来源与证明可行性

Walton 的 [作者预印本 §4.2、Definitions 4.5–4.6](https://arxiv.org/html/1705.09034v1#S4.SS2)
已经定义周期集上的 Frobenius twisted counts 及其 character-averaged
\(L\)-functions。在有限周期支撑上令 \(G=\langle H_c\rangle\)，
\(g=H_c^{-j}\)，即得到上面的有限 joint trace；这不是新 zeta formalism。

Endler–Gallas 的 [原文 §3、Eqs. (3)–(6)](https://inaesp.org/PublicJG/endler_gallas_orbital_sums_PLA2006.pdf)
给出 \(c=-6\) 的周期五 sextic、判别式及对称 Galois 群陈述，与 C12A
所核对的 marker 完全碰撞。这里新鲜读取原文相关段落及公式，未重新做
周期五消元，也未把该论文的一句 Galois 陈述当作新的独立证明。

有限平坦与固定周期 Artin 因子可完整证明，但无实质增量。要保留本候选，
至少需要新的全周期／参数族 Galois 像定理或兼容的非有限 trace owner；
目前没有这样的证明。高周期计算和未发现文献都不能替代它。**不保留**。

## 2. 加性真共振：明确还原到经典二维向量群

### 精确候选及还原

令 \(q=p^e\)，\(a\in\mathbb F_q^\times\)，\(b\in\mathbb F_q\)，
在 \(\mathbb A^2(\overline{\mathbb F}_p)\) 上取

\[
H(x,y)=(y,y^q+b y-a x),\quad
\Phi_q(x,y)=(x^q,y^q).
\]

时钟是共振对角线 \(H^n z=\Phi_q^n z\)，observable 为其几何点数
\(N_n\) 与 \(Z(t)=\exp(\sum_{n\ge1}N_nt^n/n)\)。因为系数在
\(\mathbb F_q\)，\(H\) 与 \(\Phi_q\) 交换。准确设置

\[
S=H^{-1}\Phi_q,
\qquad
S(x,y)=\left(a^{-1}(x^{q^2}+b x^q-y^q),x^q\right).
\]

于是 \(\operatorname{Fix}(S^n)=\{H^n z=\Phi_q^n z\}\)。每个坐标都是
加性多项式，因此 \(S\in\operatorname{End}(\mathbb G_a^2)\)，不是
仅在有限点集上碰巧线性的系统。\(DS=0\)，所以 \(D(S^n-I)=-I\)：
所有 fixed schemes 都是有限约化的（Jacobian criterion 给零维有限型
étale scheme）。零点始终固定，故该 endomorphism 是 confined。

用 \(T=\Phi_q\) 表示这个有限域系数下的交换子环，有

\[
H\leftrightarrow
\begin{pmatrix}0&1\\-a&T+b\end{pmatrix},\qquad
S\leftrightarrow
\begin{pmatrix}a^{-1}T(T+b)&-a^{-1}T\\T&0\end{pmatrix}.
\]

这个矩阵是与来源 theorem scope 的直接对应，不是数值拟合。

### 决定性检查、最近来源和最强反例

已经实际读取 Byszewski–Cornelissen–Houben，
[Dynamics of endomorphisms of algebraic groups, v2](https://arxiv.org/html/2209.00085v2)：
Theorem A、§5.2 的向量群矩阵说明、Smith reduction、Lemma 22、Proposition
10，以及导言 Theorem C 的适用条件。上述 confined \(\mathbb G_a^2\)
对象直接在其范围内。特别是 Proposition 10 本来就允许
\(\deg(S^n-I)\) 随 \(p\)-adic valuation 波动；不存在“fixed scheme
已约化，所以度数必须是纯指数”这条捷径。未宣称读完全部 176 页，亦未
重做其全部一般性证明或替本实例判定一个未核实的具体解析分支。

便宜反例取 \(b=0\)、\(n=1\)：由 \(y=x^q\) 与
\(y^q-a x=y^q\) 得 \(x=y=0\)，所以 \(N_1=1\neq q^2\)。
它说明真正共振可以改变固定点数；但这并未逃离现成代数群机制。

本库 [wild-additive 全族证明](../../henon_wild_additive_geometric_zeta_route_a/proof/ANALYTIC_PROOF.md)
已经拥有加性映射的 valuation 计数、几何／长度区分、扩域 gcd 与自然边界
机制；[C401](../../continuation_c399_c403_round2/henon_arithmetic/CONTRACT_SCOUT.md)
拥有非共振双时钟 max-law。二维化和选择共振对角线与 C401 有对象差异，
却没有关闭新的经典机制之外的问题。求出某个特例的所有 \(N_n\) 本身
不能满足此次新论文增量要求。因此停止这一候选，不为补齐公式重写已有
理论。**不保留：来源碰撞**。

## 3. 非加性真共振：有限反例已得到，全族证明尚缺

### 精确候选

取 \(q=p^e\)，\(a,b\in\mathbb F_q^\times\)，整数
\(1<m<q\)、\(p\nmid m\)，令

\[
H_{a,b,m}(x,y)=(y,y^q+b y^m-a x).
\]

相同的仿射域、对角时钟和 \(N_n,Z\) convention 沿用上节。
\((u+v)^m-u^m-v^m\) 的 \(u^{m-1}v\) 系数为非零 \(m\)，
故这个坐标式不是标准 \(\mathbb G_a^2\) endomorphism。该检查**不证明**
它不可能在另一坐标、另一群或有限商下具有更深的 dynamically affine
来源；不能据此宣布无文献碰撞或全球新颖性。

它与 C401 的实质边界是 \(\deg H^n=q^n\) 对所有 \(n\) 恒共振。
所需合同应关闭整个参数族、包括所有 \(p\mid n\) 时的无穷抵消塔，
而不是再计算一个 C401 已排除的共振点。

### 便宜检查的真实结果

新写 [bounded_probe.py](bounded_probe.py) 直接组成 Hénon 迭代，再对
\(H^n-\Phi_q^n\) 做有限域 grevlex Gröbner 基及标准单项式计数。
[实际输出](bounded_probe.json) 保存所有五个基和环境。

| \(p,q,m,a=b=1\) | \(n\) | 基的首单项式 | \(N_n\) | 常密度试探式 \(m q^{2n-1}\) |
|---|---:|---|---:|---:|
| \(3,3,2\) | 1 | \(x^3,y^2\) | 6 | 6 |
| \(3,3,2\) | 2 | \(x^9,y^6\) | 54 | 54 |
| \(3,3,2\) | 3 | \(x^{27},y^{14}\) | 378 | 486 |
| \(2,4,3\) | 1 | \(x^4,y^3\) | 12 | 12 |
| \(2,4,3\) | 2 | \(x^{16},y^{11}\) | 176 | 192 |

每对首单项式互素；例如第三行的标准单项式有 \(27\cdot14=378\) 个。
直接核验所有方程 Jacobian determinant 均为 1，所以这些长度就是几何点数，
不是重复根加权数。第三、第五行已反驳把头几项的密度比例外推至全部周期。
\(q=4\) 一行在特征 2 的多项式环中计算，绝未把 \(\mathbb Z/4\mathbb Z\)
当成有限域；此处系数全在素子域，\(x\mapsto x^4\) 是正确的 \(q\)-Frobenius。

这里没有证明任何全周期公式，也没有从五项拟合有理性、超越性或自然边界。
第二种 staircase 加总只复核同一个首项理想的组合计数，不冒称独立代数证明。
\(n=1,q=3\) 的 6-versus-9 反例早已由 C401 拥有；本次重复仅作为校准。

### 最近来源、完整证明可行性与缺口

Shuddhodan 的 [作者 v2 §2](https://arxiv.org/html/1803.06461v2#S2)
区分 Frobenius 扭曲 fixed points 与紧支撑 cohomological trace，
Proposition 2.10 只对足够大的 Frobenius twist 保证一般非 proper 空间的
二者相等。其 Definition 2.12／Lemma 2.14 的有理 zeta 是所定义的
cohomological 对象，不能无条件替换这里的 geometric diagonal zeta。
这也是 C401 原有来源边界，不是本次新发现。

完整证明现在缺少共振边界处交数／消元首项随任意 \(n\) 的控制，
特别是 \(p\mid n\) 时抵消后下一项的位置及其参数例外。
\(D(S^n-I)=-I\) 仍保证仿射固定点约化，因此困难在无穷远的抵消，
不能误说成仿射多重根校正。加性矩阵的 binomial／valuation 证明也不能
直接用于非加性复合。

**最强已得反例**就是上表的 378-versus-486 与 176-versus-192；它们排除
指定的常密度外推，不排除某个更精细的全周期定理。本次没有能够完成的
有质变全族 proof contract。**不保留：未闭合，而非已证明全族 no-go**。

## 4. 来源读取与工作流边界

检索先查本库相关对象和引用，再用当前浏览工具访问主来源。可用工具中
没有 Zotero／Obsidian；没有声称运行它们或 Semantic Scholar API。
检索词包括 Hénon／Frobenius／resonance、periodic scheme／Galois，及
Byszewski–Cornelissen–Houben／algebraic groups／vector groups。此为有界
候选所有权核查，不是穷尽文献综述或全球 novelty certificate。

| 主来源 | 本次实际读取 | 使用限度 |
|---|---|---|
| Byszewski–Cornelissen–Houben, arXiv:2209.00085v2 (2024 修订) | 官方摘要与作者 HTML 的 Theorem A、§5.2 指定内容、导言 Theorem C | 数学主预印本；仅确认本对象落入所读范围，未声称读完全部证明 |
| Walton, arXiv:1705.09034v1 (2017) | 官方摘要、作者 HTML §4.2、Definitions 4.5–4.6 及相邻 Lemma 4.7 | 核查 twisted periodic counting 的已有定义；发表版题名不同，未假装打开受限发表版全文 |
| Shuddhodan, arXiv:1803.06461v2 (2018) | 作者 HTML §2，尤其 Lemma 2.6、Proposition 2.10、Definitions 2.11–2.12、Lemma 2.14；Example 3.6 后段 | 核查 trace 与 geometric count 的适用边界；不是本候选全共振公式 |
| Endler–Gallas (2006), DOI 10.1016/j.physleta.2006.01.031 | 作者网站原文 PDF §3 Eqs. (3)–(6) 与后段 Galois／判别式；出版商搜索元数据 | 周期五来源碰撞；没有重新证明其 Galois 陈述 |

仅使用作者／官方文献和本库证明，没有把搜索到的聚合站作为数学依据。
尝试过不存在的 arXiv v3／v2 HTML 后已改用官方实际版本；若出版商页面
拒绝访问，明确以上述作者全文与官方摘要为依据。没有本地下载 PDF，未
产生本地页码锚定或虚构本地 PDF preflight 结果。

采用 idea-creator、research-lit／novelty-check、proof-writer 的适用检查，
并按仓库 henon-route-a-batch 与 ARS 的主来源纪律保留边界。用户授权的
最多三个自主 scout 优先于旧模板的 ML 实验配额、旧模型、额外候选数及
中间确认；ARS 仅做当前来源核查阶段，不宣称完成其全 pipeline。
纯数学原文按证明／定理适用性判断，不机械套用 RCT 分级。
未运行 Scopus、Cabell、COI 或全领域撤稿审计，故没有 venue-integrity
认证。此记录为当前 AI 团队产物，没有外部模型、付费 API、稿件上传或
人类已读／人类审稿声称。

## 5. 可重跑证据与停止点

命令（仓库根目录）：

```sh
python henon_dynamics/research_c404_c408/henon_arithmetic/bounded_probe.py
```

Python 3.12.3、SymPy 1.14.0。保存输出的实际执行退出 0、约 0.50 秒。
此前交互试探使用默认 lex order，在 \(n=3\) 后续计算耗时过长；已定位
本任务进程并以 SIGINT 停止，退出 130，无 \(n=3\) 结果。随后 grevlex
试探完成五个小例；成文件后先执行一次，再执行一次捕获上述 JSON。
不把被中断的 lex 运行记作成功，不留下后台计算。

- `bounded_probe.py` SHA256：`ca127d51e16454c32d423ad6c810f6ffb017ae76da9a0345081541eefdc80c9f`。
- `bounded_probe.json` SHA256：`1577f848d6f0c787644fa4be2e5705be64d6454f28eb515c319f7ee21e92fd1f`。

这些哈希仅绑定实际输入输出，不证明数学。没有大型 census、新稿、PDF、
正式评估或占位论文。下一次若要重开第三候选，必须带来覆盖全部周期的
边界交数／抵消定理；在此之前，本 lane 的正确交付是三个透明 scout 与
两个有限外推反例，**保留 0 个合同**。
