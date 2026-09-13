# Paper30 qPI 整系数新问题：组合内定理包含增量核查 V1

日期：2026-09-09 UTC。执行者：`/root/p30_qpi_integral_portfolio_delta_v1`。
类型：独立任务上下文中的有界组合内比较；不是数学独审、全球查新、正式四门、评分、容量判断或立项。
唯一写入为本文件。原作者证明、旧 T1–T7、失败票、锁、状态、项目与 PDF 均不修改。

## 1. 结论及准确效力

`NO_DIRECT_CONTAINMENT_FOUND_IN_ACTUAL_READ_SCOPE`

对新 Phase A 的 **C1–C3 原对象完整主张**，在本次实际读取的 P18 接受源主定理与相关完整证明、
P29 接受 successor 的上同调主定理与相关完整证明，以及 P11 有限平移定理范围内，
没有找到一个旧定理通过参数代入就输出这些完整结论。
Papers1–29 的索引筛选并非逐篇全文比较；本报告不把上述结论扩大为全作品逐字排除。

同时必须保留以下实质扣除：

1. P18 已明确使用任意基变换下的 Kähler 微分及有限呈示模 Fitting 理想的标准操作。
   新 C1 的 Fitting 乘积不是新的一般方法；其派生基变换也必须归于相应标准定理。
2. 新 C2 的全扭子 Smith 分布，在 C1 的指定对角复形成立后就是圆分 DVR 特化及根单位赋值的推论，
   不是与 C1 分离的第二套一般上同调发现。
3. C3 的 Hasse 迭代指数在 Phase A 中已经扣为 Vlasenko 一般定理的特例。
   本报告保留该扣除，不在组合核查中重授原创性；此次没有独立重读该外部论文。
4. 旧 qPI 模型识别后的整套有限群循环计数确实被 P11 一般定理包含，不能因新研究中心变化而撤回。
   但当前 C1–C3 没有循环计数主张，不能用这一旧包含替代对新整系数问题的比较。

“尚未找到直接包含”不是“已证明新颖”，更不是科学接受、独立价值或准入结论。
本报告不建议把 C1、C2、C3 拆成论文，也不建议把标准形式推论计成独立发现。

## 2. 本次比较的准确新对象

按全文读取的 Phase A、U、G、D 固定以下量词，不将新问题泛化成旧 qPI T1–T7 的重评：

- C1：同一八截面吹起族，底环为无根单位关系的
  $R=\mathbb Z[q^{\pm1},\tau^{\pm1}]$；末次四中心在不同边界分量上，坐标为 $1,\tau,\tau,q$。
  对全部 $n\ge0$，研究 $L_n=\mathcal O(nD)$ 的真实层上同调，特别是
  $$R\Gamma(S,L_n)\simeq R[0]\oplus\bigoplus_{j=1}^{n}[R\xrightarrow{1-q^j}R].$$
  每个 $n$ 固定一个保常数项的选择之后，才获得所有交换 $R$-代数上的自然基变换公式。
  不增加跨不同 $n$ 的兼容派生过滤、乘法、cup product 或动力作用同构。
- C2：任意素数 $p$、整数 $m,a\ge1$、$p\nmid m$、$N=p^a$、$r=mN$，原 $s=\zeta_r$ 在
  $\mathcal O=\mathbb Z[\zeta_r]_{\mathfrak p}$（$\mathfrak p\mid p$）上降为精确 $m$ 阶 $\eta$；
  任取 $t\in\mathcal O^*$，$J=I_{m,\eta}(x,y;\bar t)$、$\varepsilon=(-1)^{m+1}$。
  同一个完整相对光滑曲面上的原 pencil 射影平坦并满足
  $\bar f_r=\operatorname{Pow}_N\circ f_m$；完整纤维的概形重数、
  基变换像 $\kappa\langle1,J^N\rangle$、完整特殊线性系
  $\kappa\langle1,J,\ldots,J^N\rangle$ 和全扭子模均保留。
  每个有限几何剩余纤维是对应小阶完整纤维的 $N$ 倍，无穷纤维准确为 $r\bar D$。
- C3：原矩阵、原乘积排序、原 $I_r$ 不变；$d$ 只作用于状态 $x,y$，固定 $s,t$。
  $p^{-a}dI_r$ 在完整 $\mathcal U=\mathcal S\setminus\mathcal D$ 上正则，包含四条末端线，且
  $$\overline{p^{-a}dI_r}=H_p(t^m,J;\varepsilon)^{(N-1)/(p-1)}dJ.$$
  统一公共 $\pi$-阶为 $a v_\pi(p)$，不是所有提升闭点的赋值；系数理想不被改成根集或 $\pi$-饱和。

此处沿用输入的数学主张作包含比较，不以“全文读过”替代 U/G/D/S 的非作者证明检查。

## 3. 接受版本的定位，而非任意旧 draft

### 3.1 P18

README 的接受条目定位 `papers/18-marked-henon-scalar-boundary/`。
最终锁的 `terminal_build_contract.source_copies_only` 指向 `paper/main.tex`，
其期望 SHA-256 与当前实际文件均为
`65ed1e9fb328411737646d1385c053382469a31f3e2088946a161f4d92eebb2d`。
同锁的 PDF 身份与当前 `paper/main.pdf` 哈希吻合；终审尾部保留
`FINAL_INTEGRITY_PASS`、`RELEASE_CONFIRMED`。
这里仅作接受源身份定位；没有重构或重新验收 PDF。

### 3.2 P29

项目 README 与 `notes/LOCAL_ACCEPTANCE_20260906.md` 一致指定
`paper-successor-20260906-transcription-v1/main.tex`，而非旧 `paper/main.tex`。
本次从这个接受入口实际跟随 `sections/`，完整读取摘要、引言、§3、§4。
接受记录所指 PDF 是 `build/natural-20260906-r0/work/main.pdf`；此次不需要也没有重审其图像或构建树。

## 4. 主张—旧定理—标准推论映射

| 新主张/消费者 | 实读旧定理或最近接口 | 是否仅参数代入已包含 | 必须扣除或保留的准确差额 |
| --- | --- | --- | --- |
| C1 的无关系 $R$ 上全部 $n$ 对角 $R\Gamma$ 与边界扩张分裂 | P18 主定理(5)、`prop:fitting-basechange`；P29 `thm:orbit-obstructions`、`thm:bounded-primitive`、`thm:hilbert` | 没有在这些定理中找到直接包含 | P18 不计算这个 $H^1$；P29 是另一种 cohomology。仍需实际证明 $R/(1-q^j)$ 上的单位边界截面及其 Bockstein 提升；旧定理不输出这些对象 |
| C1 的任意 $A$ 上 kernel/cokernel 与 annihilator、Fitting 乘积 | P18 §6 有限呈示/minor 基变换；U 所引 proper-flat 派生基变换 | **形式工具层包含/标准推论**，不是 C1 完整几何定理的包含 | 对角复形一经识别，逐项张量、kernel/cokernel 与行列式即给公式；不能把这些各计一次创新 |
| C2 原 pencil 的完整幂态射降阶、重数、非完整特化像 | 旧 qPI T1 的域上完整 pencil；P18 的标记 Hénon 多项式边界并非此族 | 没有在已读 P18/P29/P11 中找到完整包含；域上输入明确是旧依赖 | 重复矩阵块/Frobenius、正常性延拓、逐纤维平坦和投影公式为标准机制；差额仅可能在原完整 qPI 模型与原规范的落实 |
| C2 全 $H^1$ 分裂、Smith 分布、长度和 Fitting | C1/U3 的圆分特化；S (S14)–(S15) | **被本次同一包 C1 特化加标准赋值直接给出**；不是 P18/P29 的现成同对象定理 | 不把通用结果、DVR 特例、总长度、生成元数分别包装成多套发现；G 原稿只给过滤，不可把其过滤误当已分裂 |
| C3 先除后约化的原 $p^{-a}dI_r$ 与完整 $\mathcal U$ 延拓 | P18 §6 的局部系数/理想操作；P29 rational-reduction 的去极点论证仅是方法近邻 | 没有在已读旧定理中找到完整原规范恒等式的直接包含 | 循环迹插入、Cayley–Hamilton、Hasse 迭代、reflexive 延拓分别扣为一般工具；保留原排序整数桥接与四末端线接口 |
| C3 的系数理想乘积及公共阶=扭子长度 | P18 明确区分理想与根集、DVR 长度与泛重数 | **理想乘法是标准形式推论**；没有由旧定理提供典范模同构 | $\overline\alpha=H^\sigma dJ$ 后逐系数即得理想式；两个数都等于 $a v_\pi(p)$ 不证明两种对象典范同构 |

### 4.1 P18 为什么不是 C1/C2 的直接母定理

接受源第194行明确全篇工作在 $\mathbb C$。主定理 `thm:main` 的对象为
广义 Hénon 标记 simple-exact-disjoint 周期分支，坐标映射
$\Psi=(-b,\rho_1,\ldots,\rho_{d-1})$；第(5)项比较
$\operatorname{Fitt}_0\Omega_{\mathcal C/T}$ 与多项式边界上的相对微分模。
完整 §6 证明先用实际 Cartesian 方形识别
$\Omega_{A/B}\otimes_A A'\simeq\Omega_{A'/B'}$，再逐 minor 约化。
这一步不要求平坦，但它的消费者是**已经识别的相对微分模**。

C1 的消费者则是 $H^1(S,\mathcal O(nD))$，其逐级扩张是否分裂是前置问题。
把 $A'$ 改名为 $R/(1-q^j)$ 并不能从 P18 得到该模或其对角呈示。
尤其通常的 $H^0$ 非平坦基变换不自动交换；P18 的微分基变换不能填补这一义务。
P18 §8 自列不延伸到正特征、不宣称越过 nonsimple 或 compactified incidence 的限制。
这些限制说明旧**对象定理**不能直接提供当前整数族；不妨碍其所用一般 Fitting 规则在更广环上成立。

同理，P18 的泛分量局部长度保真不是 C2 的扭子 Smith 分类。
“长度是赋值”只是共同 DVR 工具；没有给出 $1-s^j$ 各商或扩张分裂，不能复原全部初等因子。

### 4.2 P29 的 cohomology 与 C1 的 cohomology 不同

P29 接受引言明定特征零域 $K$、$A=K[x,y]$，
$F=H_{k-1}\circ\cdots\circ H_0$、每相次数至少二，并研究
$\mathcal H=A/(F^*-1)A$ 的**向量空间商**及原坐标普通次数滤过。
§3 的完整证明使用被 shift 置换的无限轨道词基与累计系数原函数；
§4 的 Hilbert 公式使用混合进位及 rank-nullity。
那里没有反典范边界层、有限呈示 $R$-扭子、根单位整数环下降或边界 Bockstein。

不能把 P29 的宏步 shift 写作 $q$，再把其 Hilbert 分母 $1-t^{\delta+1}$
当成 C1 的 $1-q^j$ 矩阵元：前者是记录普通次数的形式级数变量，后者是底环内真实参数。
P29 §3 `cor:rational-reduction` 还证明其平面映射 $K(x,y)^F=K$；
旧 qPI 根单位回返则有原非恒定积分 $J$。因此连域上动力对象的直接认同也不是单纯换名。
这不排除未来另建联系，但本次未提供或需要这样的联系。

两文都区分系数与对象、常数核与非平凡商，也都使用基础线性代数，
这些只构成方法近邻；“两个两项复形”并不自动建立同一几何或同一模。

### 4.3 C2 Smith 数据只计一次

U3 在 $q=s,\tau=t,n=r$ 的特化给
$$H^1(\mathcal S,\mathcal L_r)\simeq\mathcal O\oplus
\bigoplus_{j=1}^{r-1}\mathcal O/(1-s^j).$$
只有 $m\mid j$ 给非零扭子商。S 已给出的 (S15) 是
$$\mathcal T\simeq\bigoplus_{b=0}^{a-1}
\left(\mathcal O/(\pi^{e/\varphi(p^{a-b})})\right)^{\oplus\varphi(p^{a-b})},
\qquad e=v_\pi(p).$$
此式是指定分裂模加根单位赋值分类，不是独立的新一般 Smith 算法。
长度 $ae$、最少生成元数 $N-1$ 及 $\operatorname{Fitt}_0\mathcal T=(p^a)$
是不同消费者，但不分别增加原创定理的数量；相同长度和生成元数本身也不能反推出分裂。

### 4.4 旧 T1–T7 及 P11 包含保留

本次定向重读 brief V2 的 T1–T2：原域上极除子、法丛阶、完整 pencil 与
$f_*\mathcal O=\mathcal O$ 是 C1/C2 真正消费的旧输入。
在 C3 如进一步称 $H_p$ 为**实际泛 Jacobian** 的 Hasse 不变量，
必须继续给出 T2 的实际谱 Jacobian 识别；相同四次式或相同亏格不足以替代。
P、N 的原中心/边界帧、JR 的原矩阵和积分恒等式也须按 U/G/D 的依赖表归属，不能新算。

P11 实读 `thm:finite-hierarchy` 及其完整证明：对
$X=\coprod_K n_K(C/K)$、$H=\langle a\rangle$，周期为 $[H:H\cap K]$，
循环数为 $[C:HK]$。将旧 qPI 各能级群装入乘积 $C=\prod_hG_h$，
取 $K_h=\ker(C\to G_h)$ 并给各奇点一个 $C/C$，就涵盖模型识别后的全循环求和。
这与旧组合增量报告的明确代入一致；此处不重新证明或重新评分旧 T5–T7。
若未来在新正文消费该循环结论，P11 的包含与原模型识别依赖都应引用，不能另拆为原创计数篇。

P18/P29 目前是必要的近邻定位与方法归属对象，**不是** U/G/D 已列出的数学证明依赖。
不能为了显得链条完整而虚构对它们的引理依赖；真正一般工具宜引用其一手基础来源。

## 5. Papers1–29 索引覆盖与未读潜在碰撞

本次全文读取 README 的成果索引；P27/P28 由 Batch07 接受表补全，并从各自接受源读取摘要。
索引层面的主题筛选如下，不授予各组全文无碰撞结论：

| 旧论文组 | 索引中实际主题 | 本次处理 |
| --- | --- | --- |
| P1–7 | 辛/耗散载体、算术时钟、代数单位、指数及坏素数边界 | 索引筛选；没有全文排除 |
| P8–11 | cat torsion、壳重数、中心化子商、有限平移层级 | 只对与保留旧循环结论直接相关的 P11 读原定理及证明 |
| P12–13、P15、P18 | 周期迹/留数、周期覆盖、迹纤维与标记分支临界概形 | P18 是 Fitting/基变换的首要近邻，读接受主定理及 §6 完整证明；其他仅索引 |
| P14、P16–17、P19 | 有限秩环面存活、平移维数、支撑/GCD 内部包 | 索引筛选；未把内部包误当已接受 PDF |
| P20–28 | Hamiltonian 剪切、Newton 选子、次数矩阵、Perron/monodromy | P20–26 索引；P27/P28 接受源摘要筛选，不把选子周期误作状态周期 |
| P29 | 特征零多项式差分上同调及有限周期概形检测 | 接受 successor 的摘要、引言、§3、§4 全读，其余未逐字比较 |

仍未读的潜在碰撞边界必须明确列出：

- P4/P7 的整数、局部赋值工具及 P8–10 的根单位/群论辅助引理可能共享标准计算；没有全文排除。
- P12/P13/P15 的迹、有限代数、临界矩阵及非约化重数论证可能是进一步工具近邻；没有逐定理排除。
- P19 内部包及 P20–28 未读证明区间可能含一般矩阵、乘积、递推或退化引理；摘要不保证不存在它们。
- P18 未读的其他证明区间、P29 §2 与 §§5–8 没有作逐字碰撞审查。
  P29 摘要/引言说明后部涉及周期概形与加法扩张，但此次不对全部辅助引理作全覆盖断言。
- 不重新扫描旧 47 件或全构建树；也不以历史非碰撞票替代当前 C1–C3 比较。

这些限制不等于发现了完整结论的碰撞，只表示对应全文尚未作为本结论证据。

## 6. 实际文件读取与身份

哈希绑定文件字节，不扩大阅读范围。下列“全文”均指本次实际返回并阅读完整内容；
“区间/字段”只作定向阅读。P18 锁首次整行输出和一次旧账本定位搜索出现截断，
截断输出不计作全文阅读；后续改为只提取最终锁的源/PDF 身份字段。
未由这些诊断加载或认证全部旧账本，也未产生任何文件改写。

### 6.1 新主张与旧 qPI 依赖

下表路径均相对 `docs/research-batch07/`。

| 文件 | 实际阅读范围 | SHA-256 |
| --- | --- | --- |
| `PAPER30_QPI_INTEGRAL_SCOPE_PHASE_A_V1_20260909.md` | 全文107行 | `bb463d1e1c27f543e4a0fe1bda17b584ffce28148e49ab1e1f3c3b1fce6b7ad5` |
| `PAPER30_QPI_UNIVERSAL_COHOMOLOGY_DIAGNOSTIC_V1_20260909.md` | 全文255行；与派发指定哈希一致 | `a1e50c82c32f5411dce28a2bf2ff2b10bf4fdefdb8ac9b127de852de5e36c42b` |
| `PAPER30_QPI_CYCLOTOMIC_GLOBAL_MODEL_DIAGNOSTIC_V1_20260909.md` | 全文254行 | `59b308f605832d82e00720c5a3a7871c862698e194503ff3b289da592ced28e0` |
| `PAPER30_QPI_CYCLOTOMIC_DIFFERENTIAL_DIAGNOSTIC_V1_20260909.md` | 全文268行 | `e2f032ff1197d415be611670e3d233efd7f6ead0d7dbe16b05f796ed42f43652` |
| `PAPER30_QPI_CYCLOTOMIC_TORSION_SPLITTING_PROBE_V1_20260909.md` | 360–406行，S14/S15及边界；不声称全读S证明 | `2848ab1623d4e339b5f17fb184433ed68a4eb0bba8d37ca04291031d4b32f7ac` |
| `PAPER30_QPI_CANDIDATE_BRIEF_V2_20260909.md` | 121–159行 T1–T2；另定向检索标题/依赖 | `b8f1ca66927b977b05a2996e42d299390d6a895d1a3378119d1be5415d70a00f` |
| `PAPER30_QPI_POINT_PERIOD_PORTFOLIO_DELTA_V1_20260908.md` | 1–26、106–143、213–230行；另定向检索 | `7216525bf1226d4d0512eb7ca0e7b94a8573a4c18520e27afa6f0fefaa28c65d` |

### 6.2 接受近邻源

| 文件（相对工作区） | 实际阅读范围 | SHA-256 |
| --- | --- | --- |
| `papers/18-marked-henon-scalar-boundary/paper/main.tex` | 188–252、507–640、1052–1295、1428–1511行；完整主定理和Fitting相关完整证明，非全篇 | `65ed1e9fb328411737646d1385c053382469a31f3e2088946a161f4d92eebb2d` |
| `papers/18-marked-henon-scalar-boundary/experiments/finalization_lock.json` | `terminal_build_contract.source_copies_only`、`five_way_pdf_identity` 字段；其他只见截断输出 | `3d6dbd22282cfb528784a09d3d1370fd3383907e846cd3cc62a3ae026e8bed92` |
| `papers/18-marked-henon-scalar-boundary/paper/reviews/final_integrity_review.md` | 末5行，身份终态定位，非重新终审 | `251d78d2989c0c76b6f1a3090c9aeccf9c66a7171829ca6b795c9ca97d359713` |
| `papers/29-filtered-henon-cohomology/README.md` | 全文36行 | `3b3f5a7bc444ee5747201b71ebb2760d2a3730225951682972e35be762e0119f` |
| `papers/29-filtered-henon-cohomology/notes/LOCAL_ACCEPTANCE_20260906.md` | 全文66行 | `efb0f0058ae55ab1ffb681581838df1b652985ed2d647ad0a3fbda467245c017` |
| `papers/29-filtered-henon-cohomology/paper-successor-20260906-transcription-v1/main.tex` | 全文49行，跟随本入口而非旧稿 | `2cf3dd2419e4349910055da786bed739e0de02177ba3f2fc869fb07c97df86ea` |
| 同上 successor 的 `sections/0_abstract.tex` | 全文19行 | `5b692a7a380f7af064d5be044c7ff02f6ff9bcd2b6566974839ceaa94f69e285` |
| 同上 successor 的 `sections/1_introduction.tex` | 全文160行 | `7a93eba84684809c101dd6d4500c0c97702d816da7d3821603b2ac79805289d8` |
| 同上 successor 的 `sections/3_filtered_primitives.tex` | 全文315行 | `e8e5410a2df50f5591da6a4eacaebbe350fad7c4c179911d39f259fc176e4bf1` |
| 同上 successor 的 `sections/4_hilbert_series.tex` | 全文256行 | `e62e02e9511c77e2a739cde7d36e659cf9ff666f536af5346dd9d0d7c6a93884` |
| `papers/11-cat-equivariant-clock/paper/manuscript.tex` | 390–518行，含一般有限平移定理及完整证明；另定向检索 | `2a49333745477cd553b97a1e14734484774621ffa7b09e405c25e23073be7958` |
| `papers/27-positive-newton-translation-reciprocity/notes/LOCAL_ACCEPTANCE_20260905.md` | 全文41行 | `c74faa836e06b700b5b41ed40df50435100adb25226b034f4e2bf101db2828ce` |
| `papers/27-positive-newton-translation-reciprocity/build/final-20260905-r0/main.tex` | 28–55行摘要 | `9fbc475fa435b66983fe97807e7fdf5544dbd9cc8952e892d0830848b39724a8` |
| `papers/28-primitive-selector-cycle-monodromy/notes/LOCAL_ACCEPTANCE_SUCCESSOR_20260905.md` | 1–32行，接受源定位 | `9f0bb26d43ed68e5d7732b31c784facd2186d6bc15d4527cfdef1a9fbcbad27c` |
| `papers/28-primitive-selector-cycle-monodromy/paper-successor-20260905/main.tex` | 54–77行摘要 | `7beb4f783cd370dc4b0d9d1e9178e3e48ce1ef9ed1497e0e9883b10739d4a1f9` |

P18 `paper/main.pdf` 只作身份哈希检查，SHA-256 为
`e9044c2a9e6452b58b9e345a17c33a211feed909414798fa4696e169b24be06b`，不声称此次阅读PDF。
首次被截断的 P18 `experiments/source_lock.json` / `publication_lock.json` 不作科学证据，
对应哈希为 `b29378068f5da669f6b9c15d4d4a3e81daa6a2ca345fd86481c403f86771fac3` /
`052ba1d2ed94055feaa7af53aa667019ec81481621d86fbe5775fd73eaf6d542`。

### 6.3 工作入口与运行披露

- `AGENTS.md` 全文28行：`73ff82bcf298285ef8c3b6a4d3e1dff80eedb7eeda93ea47a55334c862c43412`。
- `docs/WORKFLOW.md` 全文39行：`b9da6524de44e1eb8fe6a61fb6a8221077c2eba88af38c25d20440de178f50a2`。
- `README.md` 全文62行：`040f810ddd95c153f1b628ac9edf49390663a02913756c9c9c32b83485758649`。
- `BATCH_07_CONTEXT.md` 1–28、346–370行及定向检索，非全文：
  `4d11047ef4b883d78f34149981a1054e6fbc44555e61b1291c4754f9f115b7d5`。

本任务由主控通知因 usage limit 中断，用户明确“继续，额度重置了”后恢复。
恢复前已有 Phase A/U/G 的全文读取和哈希记录，指定输出文件尚不存在；恢复沿这些实际进度继续，
没有将中断期间描述为持续执行，也没有伪造中断期间的阅读或完成。
此次为可用 Codex 独立任务上下文；不声称跨模型复核或统计意义上的独立错误过程。
采用 academic-research-suite 的证据绑定和范围诚实原则，不启动其完整审稿/评分流程。
没有外部浏览、外部发信、实验、编译、页数估计或新证明。

## 7. 最终停止边界

保留的准确差额候选，是**同一原 qPI 整数族**的单位边界截面/扩张消失、原 pencil 的完整降阶落实、
原整除微分的统一规范与全模型接口；它们是否新颖、重要以及是否适合一篇论文，仍须另外评估。
所有标准工具和直接消费者已扣除；旧失败票、数学接受及 P11 循环包含保持不变。
本件到组合内有界比较为止，不以该结论创建候选、拆论文或重投旧包。
