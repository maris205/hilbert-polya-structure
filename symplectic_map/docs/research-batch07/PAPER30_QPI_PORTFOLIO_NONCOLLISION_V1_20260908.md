# Paper30 qPI 完整候选：组合内非碰撞事实核查 V1

日期：2026-09-08。范围：本工作区 Papers1–29 与保留的 Paper30 内部算术候选。
核查类型：独立、有界的对象／结论／方法比较；不是全球查新、数学重审、正式候选评价或立项。
唯一新增文件：本报告。没有修改作者包、冻结稿、报告、锁、README 或 PDF，没有创建 Paper30 项目。

## 1. 结论与效力

`NO_MATERIAL_DUPLICATION_IN_READ_SCOPE`

对下列明确读取的源文件和科学主张，未发现当前 qPI 完整候选是 Papers1–29 中某篇主定理的改名、同对象特例重报，或旧内部算术候选的缩写／重分组版本。
该判断来自实际摘要、最近邻主定理与必要方法段的逐项比较，不来自题目差异、历史接受状态、新意分数或旧非碰撞报告。

确有应扣除的共同工具：有限群／torsor 上平移的周期公式、有限域二维矩阵阶分类、有限代数上保重数的乘法特征多项式、相对微分与 Fitting 理想的基变换。
它们在旧项目已有消费者，但旧项目未给出当前 qPI 的实际曲面／原积分／原基底之间的几何桥。
因此“工具已使用”与“同一对象定理重复发表”必须分开。

本结论不意味着九份作者包的数学全部经本核查认证，不意味着全球无人先做，更不意味着新意、独立价值、自然正文容量或正式候选合取通过。
尤其全阶准确临界多项式等式在本次任务中按待独立处置的完整候选输入比较；本报告不读取其新数学独审报告，也不给它数学 PASS。

索引1–29并非29篇全部具有相同的接受／发布状态：19是内部参考包，23、24、26存在保留的产物边界。
本轮把这些现存科学源码也纳入排重范围，但不改变其状态；是否完成 PDF 验收不是科学重复与否的证据。

## 2. 本次比较的完整候选身份

所有几何量词均保留：根单位 $s$ 的精确阶为 $r$，任意固定 $t\ne0$，全部允许特征；正特征自动不整除 $r$。
原单步映射及时间推进是

$$F_t(x,y)=\left(\frac{st}{sx-y},\frac{sx}{y}\right),\qquad t\mapsto st.$$

比较的是以下合取，而不是抽出一个通用椭圆曲线推论单独算候选：

1. 原八次吹起曲面、实际边界法丛的精确阶、原显式积分 $I_r$ 的极除子 $rD$，以及由 $1,I_r$ 生成的最小完整 Halphen pencil。
2. 原 $I_r$ 的每个有限概形纤维几何整且约化、算术亏格一；每个坏纤维唯一奇点、正规化有理；一般纤维光滑亏格一。
3. 实际几何泛纤维的 Jacobian 在原参数上准确识别为
   $\lambda^2-(T+cZ+Z^2)\lambda+\varepsilon Z^3=0$ 的光滑射影商曲线，$T=t^r$，$\varepsilon=(-1)^{r+1}$；保留 torsor，不擅自断言存在泛有理点。
4. 实际回返在泛纤维为非挠平移，在每个有限光滑几何纤维为平移；其无限阶由实际整数 Picard 格增长识别。
5. 每个有限域、全部原合法状态的完整一步周期满足 reduced length $\#\gamma/r$ 的 Hasse 上界及 JR 原分箱；奇异状态没有删去。
6. 在原基底坐标上定义的实际临界代数乘法特征多项式
   $R_{r,t,s}(C)=\det(C\mathrm{id}-m_{I_r})$ 等于 $\delta(C,T)$，包括非约化临界长度的重数，而非仅比较两个四次式的次数或零集。

原 $z$ 谱曲线、其 $Z=z^r$ 循环商和实际动力学纤维是三个需分别识别的对象；不以“都称谱”或“都亏格一”合并。
谱商入口的部分陈述原限非二特征；完整候选的全特征接口来自后续作者桥，不能把早期入口的范围自行扩大。

### 2.1 九份作者输入的实际读取与身份

下列区间均为源文件行号；读取 Claim、对象／假设、来源扣除与方法图，不声称通读其全部证明。
九份文件均位于本报告同目录；SHA256 是本轮实际计算值。

| ID | 作者文件 | 实际读取 | SHA256 |
| --- | --- | --- | --- |
| N | [边界法丛](PAPER30_QPI_BOUNDARY_NORMAL_BUNDLE_ENTRY_V1_20260908.md) | 1–105：Claim、假设、粘合机制、实际中心开头 | `8234b5584adba10ec02adb0269300b0c5191b5445fca345e28e1eb5171c12469` |
| P | [辛与极除子](PAPER30_QPI_SYMPLECTIC_POLAR_ENTRY_V1_20260908.md) | 1–100：Claim、原积分输入、边界赋值方法 | `61d2b0ace7003e19ff1e81242e4080402049d98c024657b94d9b812086f358b3` |
| S | [谱循环商](PAPER30_QPI_SPECTRAL_QUOTIENT_ENTRY_V1_20260908.md) | 1–126：Claim、谱／动力边界、结式与 Kummer 方法 | `049941aad912cabc3788d8063ba3cec20d3f7a863a2ef50e3d29e1747d3e3738` |
| G | [原始亏格一桥](PAPER30_QPI_PRIMITIVE_GENUS_ONE_BRIDGE_V1_20260908.md) | 1–92：Claim、最小线性系、Stein／横向临界排除 | `0d7a3e2d37eb7218feddfe5c85bf244a0be358bfcc880279d5f14afd5cb77ace` |
| F | [实际有限纤维](PAPER30_QPI_ACTUAL_SINGULAR_FIBRE_ENTRY_V1_20260908.md) | 1–127：Claim、实际正交格、Chern 临界长度、旧全阶接口 | `3b7a495b723d9ba45003fe767431c4420053c0b3de6656a2335c3aad01307003` |
| R | [实际回返平移](PAPER30_QPI_RETURN_TRANSLATION_ENTRY_V1_20260908.md) | 1–106：Claim、实际同构、Picard 增长、平移特化方法 | `9ee29e426c14334c41c26b1265bd71fe53b232c37949d5ad21aef14550a6851c` |
| J | [Lax／Jacobian 桥](PAPER30_QPI_LAX_JACOBIAN_BRIDGE_ENTRY_V1_20260908.md) | 1–118：Claim、谱线丛逆重建、不变 Picard 与无核下降 | `a6aa5e30ea0795b05790b058dfd4debc6431de1918090b9a6add88351a1eb63f` |
| H | [全部轨道 Hasse 分箱](PAPER30_QPI_ALL_ORBIT_HASSE_BINS_ENTRY_V1_20260908.md) | 1–114：Claim、原状态／原分箱、光滑与奇异层的方法 | `78191a3faa7d2a867e45eccd708b106b722d43e6f5ea73d583e0385637be2469` |
| B | [全阶准确坏值桥](PAPER30_QPI_EXACT_BAD_VALUES_BRIDGE_ENTRY_V1_20260908.md) | 1–136：完整等式、长 Weierstrass、henselian 模型同构与 Fitting 方法 | `1e7ade432e62b1e116270d2588d0d798accbf482fcc6edd46dca12b76be42bb1` |

作者文件内冻结时的“待审／OPEN”只用于识别各入口的原范围，不作为撤销后续独立接受的依据。
本报告只做组合排重，没有重新处置这些状态。

## 3. Papers1–29 的筛选与定向读取

先读 `docs/WORKFLOW.md` 全文；README 仅用于1–29题目／项目位置与区分索引身份。
随后读取全部29项现存论文源码的实际摘要；对可能最近邻继续读主定理、对象定义和必要方法段。
搜索限定在 `papers/` 的 TeX 源码，排除所有 `build*` 子树、旧 revisions、图文件与宏文件；未遍历或重哈希旧构建树。

定向词包括 qPI、QRT、Painlevé、Halphen、genus-one、elliptic、Hasse、Picard、q-invariant、rational first integral、finite field、Jacobian。
在上述源码搜索范围未见 qPI／QRT／Halphen／genus-one／Hasse／Picard 的相关定理命中；明确积分／可积性近邻是29。
这只是找近邻的辅助线索，不把字符串缺失当成数学非碰撞证明。
“Hasselblatt”不是 Hasse 定理；“Jacobian determinant”不是曲线 Jacobian；Paper4的“elliptic cycle”是线性稳定性类型，并非亏格一曲线。
Paper4为此额外实读435–462行，确认其内容是共轭倒数乘子的模长与五条低周期数值审计轨道。

### 3.1 最近邻源码、实际读取区间与身份

表中路径相对工作区根；摘要区间均包含摘要正文。
27–29采用已接受版本的源码入口：27的 layout 主文件 SHA 与本地接受记录中的源伴随 SHA 相同；28、29的 successor 路径由本地接受记录的源身份项确认。
这几条产物记录仅定位源身份，不消费其审稿结论或科学评分。

| Paper | 实际源文件 | 实际读取区间／用途 |
| --- | --- | --- |
| 7 | `papers/7-base2-exponent-clock/paper/manuscript.tex` | 44–63 摘要；230–266 局部单位／乘子定理；284–374 冻结2-adic定理、Frobenius–Hensel范数模型 |
| 8 | `papers/8-cat-torsion-capacity/paper/manuscript.tex` | 50–69 摘要；271–288 uniform carrier；443–468 标准cat精确周期分类 |
| 9 | `papers/9-cat-prime-shell-multiplicity/paper/manuscript.tex` | 53–75 摘要；172–241 prime-shell定理与split/inert证明；412–453 标量分母障碍 |
| 10 | `papers/10-cat-centralizer-quotient/paper/manuscript.tex` | 53–74 摘要；258–291 centralizer torsor；336–374 商动力消失；398–434 辛中心化子范数类 |
| 11 | `papers/11-cat-equivariant-clock/paper/manuscript.tex` | 54–78 摘要；239–366 carrier定义段；404–515 有限阿贝尔群平移主定理及证明 |
| 12 | `papers/12-henon-period3-residue/paper/manuscript.tex` | 54–83 摘要；86–194 问题／方法边界；254–333 两项主定理、完整quartic fibre范围 |
| 13 | `papers/13-henon-primitive-cycle-cover/paper/main.tex` | 78–97 摘要；189–342 对象、Theorems A/B与rank-one边界；960–991 乘法特征多项式／判别式方法 |
| 15 | `papers/15-henon-quartic-trace-fibers/paper/main.tex` | 59–63 摘要；95–140 unified quartic trace-fibre主定理 |
| 18 | `papers/18-marked-henon-scalar-boundary/paper/main.tex` | 69–71 摘要；525–642 完整主定理与依赖表；1055–1153 相对微分与Fitting基变换实际证明 |
| 27 | `papers/27-positive-newton-translation-reciprocity/paper-layout-20260905/main.tex` | 1–190 题名、28–55摘要、对象／方法／边界；365–455 typed branch、seed、五项主定理 |
| 28 | `papers/28-primitive-selector-cycle-monodromy/paper-successor-20260905/main.tex` | 1–205 题名、54–77摘要、对象与完整Theorem A八项 |
| 29 | `papers/29-filtered-henon-cohomology/paper-successor-20260906-transcription-v1/` | `main.tex` 全文1–49；`sections/0_abstract.tex` 全文1–19；`1_introduction.tex` 全文1–160；`7_univariate_rigidity.tex` 45–84；`8_symplectic_lift.tex` 1–218、270–321 |

以上区间之外不声称已阅读整篇证明。以下 SHA 绑定具体读本，不替代旧产物验收。

| 源 ID | SHA256 |
| --- | --- |
| 7 manuscript | `60a9868f92b2d34e9ae140cebc534118225d05fe647530df1341c5ad0cc96974` |
| 8 manuscript | `95ebccff1eb5f2b939be92c9a8b7020b625d4b8056cc5b6bda3b3814fcae580c` |
| 9 manuscript | `fb54cb9273c89ad5f76a9485d67a815555050b3c71e630e47d367b043ae6e26c` |
| 10 manuscript | `65bd460ac888ff5527f4401696788034973c3f97a532ee8a34184ce05fae72a6` |
| 11 manuscript | `2a49333745477cd553b97a1e14734484774621ffa7b09e405c25e23073be7958` |
| 12 manuscript | `5c3b09a835aa41f35899f3c720982f911acf7046559c8433f38ab38ce61a0447` |
| 13 main | `f62f72ad129bc371d0e76d1daf48b0a2df82cf60d0d1e750d6c0f049047539ce` |
| 15 main | `faa8f60bc7c51c2310b2e48450599823386e8d339fc92feeaf43161d247210d5` |
| 18 main | `65ed1e9fb328411737646d1385c053382469a31f3e2088946a161f4d92eebb2d` |
| 27 layout main | `9fbc475fa435b66983fe97807e7fdf5544dbd9cc8952e892d0830848b39724a8` |
| 28 successor main | `7beb4f783cd370dc4b0d9d1e9178e3e48ce1ef9ed1497e0e9883b10739d4a1f9` |
| 29 successor main | `2cf3dd2419e4349910055da786bed739e0de02177ba3f2fc869fb07c97df86ea` |
| 29 abstract | `5b692a7a380f7af064d5be044c7ff02f6ff9bcd2b6566974839ceaa94f69e285` |
| 29 introduction | `7a93eba84684809c101dd6d4500c0c97702d816da7d3821603b2ac79805289d8` |
| 29 rigidity | `ce400f2ae1a49abeb78b2f4045203aa24c6849b3213d4c0f0c4024cfe374c2cd` |
| 29 lift | `d9c5d2279bc23ff4954bf0f2d20ff58b000b13e093ff09ad37791e5de8cce0d0` |

### 3.2 其余17项实际摘要筛选

这些项未因摘要／对象筛选发现需要按 qPI 最近邻加读主定理的风险；不声称已通读全文。
路径给出唯一项目目录；1–6使用 `paper/manuscript.tex`，14、16、17、19–26使用 `paper/main.tex`。

| Paper／项目目录 | 摘要行号 | 实际对象和结论；与当前合取的区别 |
| --- | --- | --- |
| 1 `1-symp-vs-diss` | 43–79 | PCF参数的Hénon保守–耗散同伦、符号载体运输实验失败；不是可积有理曲面的原积分纤维定理 |
| 2 `2-branch-baker` | 57–78 | 固定有限记忆局部常数乘子钟的有理秩障碍及Markov–baker载体；不是有限域椭圆纤维周期分类 |
| 3 `3-prime-multiplier-obstruction` | 46–66 | PCF二次多项式周期导数乘子的整除性与raw-prime排除；不是原积分的坏值多项式 |
| 4 `4-integral-henon-multipliers` | 58–87；另435–462 | $S$-整Hénon的周期点整性、代数单位乘子与有理模长；elliptic指线性稳定性，不是genus-one |
| 5 `5-algebraic-action-clocks` | 52–74 | 代数归一化周期作用量不能等于$\log p$；不识别qPI原积分、Jacobian或轨道Hasse区间 |
| 6 `6-arithmetic-clock-escape-trichotomy` | 51–76 | 固定加法读出的秩加坏素支撑命中上界；不构造椭圆纤维或计算原周期 |
| 14 `14-henon-four-step-torus-escape` | 52–72 | 特征零有限秩乘法群中的单项式Hénon四步存活界／三步尖锐性；非全部有限域全状态分类 |
| 16 `16-henon-support-size-torus-escape` | 56–62 | 多项支撑Hénon两步存活界及支撑一四步分支；固定秩单位方程与退化链，不是曲面pencil |
| 17 `17-shiftlike-torus-coset-decay` | 48–50 | shift-like存活簇中乘法环面平移的维数衰减；“translate”是子环面陪集，不是椭圆Jacobian上的回返 |
| 19 `19-shiftlike-translate-gcd-obstruction` | 52–54 | 内部参考包：最大环面方向的标量提升方案及GCD残余障碍；没有qPI谱线丛／亏格一曲面声明 |
| 20 `20-coupled-shear-degree-matrix` | 50–74 | 四维Hamiltonian剪切的精确次数矩阵及$(\sqrt g+1)^2$增长；权次数机制而非Picard纤维结构 |
| 21 `21-three-mode-hamiltonian-cubic-degree` | 51–77 | 六维三模剪切的精确次数与三次Perron子族；模5只是不可约性工具，不是有限域动力主定理 |
| 22 `22-hamiltonian-cubic-spectral-collapse` | 49–88 | 全维剪切选子矩阵的三维商／三次特征因子；“spectral quotient”是线性矩阵商，不是谱代数曲线的Jacobian |
| 23 `23-hamiltonian-quartic-spectral-escape` | 59–84 | 保留源码的八维剪切精确次数与四次Perron子族；四次为次数矩阵特征式，不是临界值四次 |
| 24 `24-hamiltonian-period-two-selector-exchange` | 50–66 | 保留源码的Hamiltonian权次数选子二周期交换、两步monodromy与奇偶次数律；不是原状态周期 |
| 25 `25-hamiltonian-support-rank-unbounded-perron-degree` | 57–59 | 全秩Hamiltonian族、不可约Perron次数与最小标量递推阶；不识别曲面不变量或有限域轨道 |
| 26 `26-hamiltonian-newton-envelope-contraction` | 45–92 | 保留源码的Newton包络收缩、前后向次数律、固定射线；不是原辛曲面上的椭圆平移 |

## 4. 最近邻逐项比较：对象—结论—机制

### 4.1 Batch07 的27–29

**27：对角“平移”并非曲线群平移。**
对象是特征零、$r\ge3$的分离Hamiltonian多项式剪切，在完整严格证书分支上的加权首次数状态。
主定理给 $u'=u+\delta\mathbf1$、有限选子变换计数、字面逆序互反与单步稳定半径；证明用分组面Hessian、关联分次注入、严格carry和直线上包络。
当前qPI的平移作用在原 $I_r=c$ 的亏格一曲线上，由实际曲面同构、整数Picard格增长和椭圆自同构分解建立。
27没有原积分pencil、有限坏纤维、曲线Jacobian或全状态有限域结论；两种“translation”不能识别。

**28：选子字与权状态周期不是原动力状态轨道。**
对象是每个长度$\ell\ge3$的rooted primitive词对应一个维数$2(\ell+1)$的置换扭曲Hamiltonian多项式映射。
Theorem A给normal-fan严格选子分类、incidence实现、实际权次数lift、rank-one周期矩阵及字恢复；明确排除由此推断多项式状态周期。
qPI固定二维有理映射、有限阶时间参数与实际完整初值空间。其Lax谱线丛、循环谱商和Jacobian识别不等于28的首次数矩阵或carry-free数字解码。
共同的“rooted／primitive／period／monodromy”词汇不足以构成结论包含关系。

**29：真正的有理积分近邻，已核对完整固定域应用。**
其基础对象是特征零辛Hénon多项式复合；结论为无次数损失的多项式余边界原函数、精确Hilbert级数及一个完整周期概形的有效检测。
方法是轨道坐标基、mixed-radix次数重编码和no-alias；不是反典范节点环的线丛阶或曲面临界代数。
§8的四维保参数辛lift有固定域 $\mathbb C(a)$，仅在 $V_a=c(a)V_t$ 时为 $\mathbb C(a,r-c(a)s)$；其例外是势函数的多项式参数平移，且不存在有理Liouville pair。
当前对象不是该多项式lift的一个已识别特例，目标也不是其余边界／固定域分类；qPI已有原始Laurent积分，需识别其实际亏格一pencil及全特征纤维。
29“不存在Liouville pair”的对象与辛结构限制不能外推为排除qPI；qPI也不反驳29。

### 4.2 7–11：有限域、平移torsor与矩阵阶

**7** 把特征零2-adic二次映射周期点识别为有限域Frobenius轨道的Hensel lift，研究正规化导数乘子的非分歧范数。
当前qPI的底域本身可以是任意有限域，结论是实际能级曲线上的周期上界／原分箱；并非7的归一乘子范数或$\pm2^n$排除。
Hensel这一共同词也对应不同用途：7提升标量周期根，qPI B在有限DVR模型的光滑点提升局部截面。

**8** 用$\det(M^n-I)$的原始素因子给双曲整数矩阵的素数加法阶载体，精确排除标准cat的周期$1,6,12$。
这里是环面扭点上的线性作用，不是带原积分的有理曲面。它不提供qPI光滑／奇异纤维的几何身份，也不提供Hasse分箱。

**9** 与qPI奇异层共享真实的有限域算术工具：split/inert特征值阶分别整除$p-1,p+1$，以及ramified/Jordan例外。
但9作用于标准cat的非零$p$-torsion向量壳，结论是同周期壳的轨道重数和单标量Euler分母障碍。
qPI H先把每个实际奇异纤维识别为唯一奇点加有理正规化，再在$\operatorname{PGL}_2(\mathbb F_q)$中处理回返，保留奇点且覆盖所有$q$；后接JR固定阈值的整数分箱。
不能把“矩阵特征值／Jordan分类”作为新一般方法；也不能把9的特定向量壳定理当成qPI全部原状态结论。

**10** 的torsor是$R_q[A]^\times$在模整数$q$的cyclic-vector locus上的简单传递集合，full-centralizer商把$A$本身除掉，诱导动力恒等；辛中心化子留下范数类。
qPI J的torsor是函数域上亏格一曲线对其Jacobian的代数几何torsor，商发生在原谱曲线的循环自同构上，并要求Picard拉回无核与实际谱线丛逆重建。
两者的基底、范畴、群、商对象和保留动力不同；不能因“torsor／quotient”相同就视为同一构造。

**11** 是最明确的一项通用结论重用：其Finite translation hierarchy对任意有限阿贝尔群$C$和$C/K$给每点周期$[\langle a\rangle:\langle a\rangle\cap K]$。
在自由torsor情形，周期等于$a$的阶；qPI光滑有限域纤维完成几何识别后使用的群论结论正属于这一标准机制。
11没有证明qPI回返是平移，没有建立实际纤维／Jacobian身份，也没有Hasse点数输入、奇异层覆盖或JR原分箱。
因此不把周期等于元素阶单列新定理，但完整qPI消费者不是11的有限等变zeta／stack保留层级结果的重报。

### 4.3 12、13、15、18：完整概形、谱与准确临界结构

**12与15** 的“fiber”是归一Hénon模空间中周期导数迹数据的纤维；不是一个有理第一积分在固定曲面上的能级。
12用完整周期代数、留数和局部长度得到quartic例外族的周期三迹矩；15将其接到pure-trace Jacobian候选界和全quartic准有限截断。
15的Jacobian是多项式映射的常Jacobian参数，非曲线的$\operatorname{Pic}^0$。
它们与qPI F/B确实共享“保留nilpotent重数、在有限代数取乘法谱”的原则；但旧代数是$\operatorname{Fix}(H^n)$，新代数是$Z(dI_r)$，旧可观测量为导数迹，新算子为原积分值乘法。
没有由旧迹矩或其长度60推导实际qPI临界长度4及$R=\delta$的关系。

**13** 的完整源对象是$\mathbb Q[a,c]$上Hénon原始周期点覆盖、其归一化和循环移位商。
Theorems A/B证明泛周期域、全对称cycle monodromy及orbit sum／derivative trace分别生成cycle field；$\det(T\mathrm{id}-m_s)$保持整性和无基选择。
qPI的Lax矩阵谱不是13的周期导数矩阵谱；其曲线Jacobian也不是13的有限cycle field。
循环不变量、归一化、Henselian方法与乘法特征多项式都是通用接口；13未建立原qPI纤维与谱商之间的无核Jacobian桥。

**18** 是准确临界概形的最近邻：在特征零simple／exact／disjoint marked Hénon incidence上，证明选定迹坐标占优／泛étale，且scalar boundary的Fitting临界概形准确基变换。
已实读其1055–1153行：相对Kähler微分与有限展示矩阵的Fitting理想任意基变换保留nilpotent结构，确与qPI B的保重数比较共享标准方法。
但是18比较的是Hénon标记迹映射与多项式边界；其临界支撑通常是模空间中的Cartier divisor，并非固定辛曲面上原 $I_r$ 的长度4临界概形。
它不提供qPI的长Weierstrass方程、henselian最小模型同构、准确原参数值或四维乘法矩阵。共享Fitting原理不等于对象定理重复。

## 5. 与旧内部算术候选的实质比较

实际读取 [完整冻结候选brief V2](PAPER30_TWIST_INTERNAL_ARITHMETIC_CANDIDATE_BRIEF_V2_20260908.md) 第1–240行，覆盖问题、实际模型、四项完整主张、非标准系数输入及当前证明选择。
SHA256：`6ef58db6f009260312102d6ba35570160e5f86fb9be7d411e091a323bfd0da0b`。
未读取旧正式评分票或旧非碰撞报告来形成结论；未重审A01–A23证明链。

旧对象为二谐波twist map
$y'=y+\epsilon\sin q+2\lambda\epsilon^2\sin(2q)$、$q'=q+y'$，在素数幂旋转分母$p^a$的正规化Lindstedt消元中取实际正频对角jet。
由三角递推得到内部位置$p,2p,3p$的forcing参数多项式$\mathcal B_1,\mathcal B_2,\mathcal B_3$；它们不是整个共振作用项，也不是共轭不变量。
对$p\ge5,a\ge2$，旧合取为第三forcing正规化的完整两边Newton图、次数$m=(p-1)/2$和$p$的两个不可约可分因子、正簇循环tame分裂域、负簇单根wild全分歧，以及三个forcing两两互素。
准确高端点$-3/16$来自实际有限系数窗口／factorial band／伴随与矩复用；完整负簇分裂域和最终共振系数不在其已证合取内。

这与qPI有三项不可混淆：

- **对象不同：** 旧对象是特征零局部消元的内部jet参数多项式及其$p$-adic完成；新对象是JR实际有理曲面和原第一积分的全纤维族。
- **结论不同：** 旧对象分类内部取消根的Newton簇与分歧／互素性；新对象识别最小pencil、曲线Jacobian、实际坏能级及全部有限域轨道。
- **机制不同：** 旧链的有限窗口、指数递推、双factorial带及端点系数不参与新qPI的八中心吹起、边界线丛、Lax谱线丛、Picard格或最小正则模型桥。

两者都出现根单位、赋值、有限代数与参数多项式等一般语言，不能据此把当前包解释为失败候选的简写重投。
尤其qPI的$r$是底域中$s$的精确乘法阶，旧$p^a$是特征零旋转分母；旧$p$-adic素数、qPI有限域特征和谱变量也不可互换。
未发现当前六项合取继承旧内部jet算术定理作为必要已证明消费者。

## 6. 应合并说明、归属或引用的部分

本节仅说明避免重报的边界，不授权写论文、拆稿或建立任何新项目。

1. 九份qPI作者入口是同一对象的一条依赖链；八中心／节点边界、原积分身份、有限纤维结构等共同基础应统一陈述和引用，不能按文件数计算独立定理项目。
2. H的“平移周期等于点阶”和奇异层“split／inert／Jordan阶分类”分别扣除11与9已经使用的通用群论机制；如后续直接复用旧稿文字或具体证明，需明确前件归属。标准原理的文献归属由主控外部来源整合确定，不将内部旧稿包装成首创来源。
3. F/B的有限代数特征多项式、保重数的概形约定，与12／13／15已有接口统一术语；B中的相对微分／Fitting基变换与18已有接口同样注明是标准工具。对象上的长度4、原参数识别和$R=\delta$不能省略为这些一般事实的无条件推论。
4. 12的quartic周期三内容已进入15，14的支撑一逃逸分支已进入16；在组合定位中各自按一条相关成果链处理，不重复累计“不同旧先例”或重复贡献。
5. 27–28的degree translation／selector period／matrix spectrum与qPI的curve translation／actual state period／Lax spectral curve应始终带对象限定；29的固定域／Liouville边界只用于说明研究问题差异。
6. qPI原映射、原积分、原谱式和JR原Hasse分箱已经在九份作者包中明确归属于外部既有工作；Halphen、椭圆平移、谱对应、Hasse与最小模型理论也不能因为在1–29未成为主定理，就改称本工作区的原创一般理论。本报告不追加全球先例判断。

## 7. 剩余不确定性与自查

本轮没有发现需立即合并到某篇已接受论文的同对象主定理重报；也没有发现应把当前qPI包归回旧内部算术候选的事实依据。
但对仅读摘要的17项，本结论只覆盖摘要明示科学范围及定向源码筛选，不保证其未读细节中绝无相同标准引理或局部计算。
对最近邻也只声称读过所列区间，不以哈希计算冒充全文阅读。未来若直接引入旧稿中的特定证明／文字，仍需对该实际借用定向比对与归属说明。

自查项目：

- [x] 已读工作流程；1–29全部实际摘要已覆盖，27–29主定理／范围已定向读取。
- [x] 已核查积分／genus-one／有限域／Hasse／Picard潜在近邻，并排除术语误命中。
- [x] 已逐项比较最近邻的对象、结论与机制；不是只比较题名。
- [x] 已读旧内部算术完整科学brief；不以失败评分作非碰撞证据。
- [x] 当前候选保留全阶、每个非零固定$t$、全部特征、全状态与临界重数；未缩小到自治或光滑层。
- [x] 未读取本轮新数学独审或候选评分票；未作全球检索、数学重审、新意／价值／页数评分。
- [x] 标准工具重用已扣除；内部链的合并引用与科学对象区别已说明。
- [x] 只新增本报告，无其他本地改写、构建、项目创建或外部操作。

最终范围结论保持：`NO_MATERIAL_DUPLICATION_IN_READ_SCOPE`。它是局部组合事实核查，不是全球非重复证明或正式立项许可。
