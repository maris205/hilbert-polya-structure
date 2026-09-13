# Paper30 qPI Integral V1：当前完整必要证明图

日期：2026-09-09。组织者：/root/p30_qpi_integral_portfolio_delta_v1。
类型：第一次 Integral V1 正式候选包的证明依赖组织；不是新证明、数学重审、正式四门票、论文或 PDF。
route_applicability：NOT_APPLICABLE。效力仅限本地。

## 1. 本图的目标、状态与使用方式

本件完整组织 [新 Phase A](PAPER30_QPI_INTEGRAL_SCOPE_PHASE_A_V1_20260909.md) 的 C1–C3，
并按本次明确范围保留 C3 的实际泛 Jacobian 及原光滑闭能级 Hasse 解释。
目标已与主控 [Integral V1 brief](PAPER30_QPI_INTEGRAL_CANDIDATE_BRIEF_V1_20260909.md) 全文对照；
[预审处置](PAPER30_QPI_INTEGRAL_PREFLIGHT_DISPOSITION_V1_20260909.md)的“继续完整评价而非预授准入”保持。
不以只写谱多项式名称代替真实谱模识别或闭纤维同构。
必要证明全部进入当前图；表中依赖节点和行号是查读入口，不是可以代替证明的摘要。

新 [Phase C/D](PAPER30_QPI_INTEGRAL_NOVELTY_PHASE_CD_V1_20260909.md) 的
7.0/10、PROCEED_WITH_CAUTION 完整保留，不称为正式新意 PASS。
本件不另给新意、独立价值、证明信心或容量分数。
纸面完整性与自然正文容量交 fresh 两份正式四门各自判断；不从文件行数推算篇幅。
旧 qPI T1–T7、V1/V2 的接受、失败票和正确替代证明全部冻结保留。
本图不是旧 T1–T7 的重评、删减版或同字节重抽票。

已经接受且未变的数学按原处置消费，不因重新组织候选而重开局部数学审查。
尤其 U 的 S5/S7 审查所有权条件已由
[整系数数学合取处置](PAPER30_QPI_INTEGRAL_MATHEMATICS_DISPOSITION_V1_20260909.md)关闭；
作者件的历史“待独审”以及独审提交时的待合取措辞不被改写。

后续正式评审必须按共同输入清单实际全文读取各必要作者件、对应独审和接受处置。
不能只读本图、旧 brief 的 T1/T2 结论或其他人的已读字段。
本图组织者本人的定向读取范围另列于第 10 节，不将其冒充后续评审的全文责任。

## 2. 唯一记号、原对象与全部量词

### 2.1 文件别名

| 本图别名 | 实际作者输入 | 与同名对象的区别 |
|---|---|---|
| P | [辛结构与原极除子](PAPER30_QPI_SYMPLECTIC_POLAR_ENTRY_V1_20260908.md) | 原曲面、实际八中心及原积分 |
| Nbd | [边界正规丛](PAPER30_QPI_BOUNDARY_NORMAL_BUNDLE_ENTRY_V1_20260908.md) | 文件别名；不与整数 $N=p^a$ 混用 |
| Gfield | [原始亏格一桥](PAPER30_QPI_PRIMITIVE_GENUS_ONE_BRIDGE_V1_20260908.md) | 旧域上 T1，不是新的整模型 G |
| Ffib | [实际有限奇异纤维](PAPER30_QPI_ACTUAL_SINGULAR_FIBRE_ENTRY_V1_20260908.md) | 当前消费其实际纤维几何，不预设临界长度 |
| Jspec | [真实谱 Jacobian 桥](PAPER30_QPI_LAX_JACOBIAN_BRIDGE_ENTRY_V1_20260908.md) | 文件别名；不与小阶积分 $J$ 混用 |
| Wreuse | [共享 Weierstrass 证明复用 V2](PAPER30_QPI_SHARED_WEIERSTRASS_PROOF_REUSE_V2_20260908.md) | 已接受 V2，包含任意原域 Step 2a |
| Bbad | [准确坏值桥](PAPER30_QPI_EXACT_BAD_VALUES_BRIDGE_ENTRY_V1_20260908.md) | 纯方程子段与强实际临界出口分开消费 |
| Hloc | [指定点／局部模型证明复用](PAPER30_QPI_POINT_MODEL_PROOF_REUSE_V1_20260909.md) | 本图只直接消费 L(a) 及其实际前提；不是新通用上同调 U |
| Ucoh | [通用上同调诊断](PAPER30_QPI_UNIVERSAL_COHOMOLOGY_DIAGNOSTIC_V1_20260909.md) | 无关系整数环上的通用分裂 |
| Ssplit | [圆分扭子分裂探针](PAPER30_QPI_CYCLOTOMIC_TORSION_SPLITTING_PROBE_V1_20260909.md) | 新 S；不是旧谱商文件 |
| Gint | [圆分完整模型诊断](PAPER30_QPI_CYCLOTOMIC_GLOBAL_MODEL_DIAGNOSTIC_V1_20260909.md) | 新 G；不是 Gfield |
| Ddiff | [圆分整除微分诊断](PAPER30_QPI_CYCLOTOMIC_DIFFERENTIAL_DIAGNOSTIC_V1_20260909.md) | 新 D 文件；不与边界除子 $D$ 混用 |

旧谱商文件仅在保留的替代路径中称 Sspectral。
Wreuse 内部的 $W_0$ 仍按其 44–50 行原定义理解为完整纯模型计算包；
本图只细分它的实际出边，不改写旧 $W_0$ 的定义或删掉其矩阵计算。

### 2.2 原族和原矩阵规范

底环为无根单位关系的
$$R=\mathbb Z[q^{\pm1},\tau^{\pm1}].$$
在同一个原八截面吹起族 $S/R$ 上，$D$ 为相对反典范八环，$L_n=\mathcal O_S(nD)$。
末次四中心位于各自不同的边界分量，坐标为 $1,\tau,\tau,q$；
其为单位，不因坏素位特化而碰到节点。
完整环面补集 $E$ 包含 $D$ 和四条末端例外曲线，$S\setminus E=(\mathbb G_m)^2_R$；
本题开放初值空间 $S\setminus D$ 仍包含那四条末端线，二者不能混同。

使用 Ddiff 31–52、Ssplit 60–82 和 Jspec 119–150 的同一个原矩阵：
$$A(z)=A_0+zA_1+z^2\operatorname{diag}(1,0),\qquad
M_j(z)=A(q^{j-1}z)\cdots A(qz)A(z).$$
矩阵逐项系数、乘积方向、时间参数及能级均不重标定。
精确阶 $j$ 的域上，原 $I_j$ 由
$$\operatorname{tr}M_j(z)=t^j+I_jz^j+z^{2j},\qquad
\det M_j(z)=(-1)^{j+1}z^{3j}$$
固定；JR 的这些原恒等式及 Laurent 首项是已有来源输入，不是本候选新发现。
在整个 $R/(1-q^j)$ 上使用实际系数
$$C_j=[z^j]\operatorname{tr}M_j(z),$$
不能将非本原分支的 $C_j$ 换成 $\operatorname{tr}M_j(1)-(\tau^j+1)$。

### 2.3 C1：全部反典范幂及任意基变换

原 $R$ 上 $H^0(S,L_n)=R\langle1\rangle$、$H^{\ge2}(S,L_n)=0$，
且边界给出的每一级实际短正合列
$$0\longrightarrow H^1(S,L_{j-1})\longrightarrow H^1(S,L_j)
\longrightarrow R/(1-q^j)\longrightarrow0$$
均分裂；完整共振截面和单位边界是其必要具体内容。
对每个整数 $n\ge0$，保留真实常数映射的非典范同构为
$$R\Gamma(S,L_n)\simeq R[0]\oplus
\bigoplus_{j=1}^{n}[R\xrightarrow{1-q^j}R],$$
两项复形位于次数 $0,1$。
对每个固定 $n$ 选择一次该同构后，对每个交换 $R$-代数 $A$ 均有对应派生基变换；
允许 $A$ 非平坦、非约化、非 Noetherian。于是
$$H^0(S_A,L_{n,A})\simeq A\oplus
\bigoplus_{j=1}^{n}\operatorname{Ann}_A(1-q_A^j),\qquad
H^1(S_A,L_{n,A})\simeq\bigoplus_{j=1}^{n}A/(1-q_A^j),\qquad H^{\ge2}=0.$$
原通用有限呈示模的零阶 Fitting 理想为
$$\operatorname{Fitt}_0^R H^1(S,L_n)
=\left(\prod_{j=1}^{n}(1-q^j)\right)
=\left(\prod_{d=1}^{n}\Phi_d(q)^{\lfloor n/d\rfloor}\right).$$
$n=0$ 取空和、空乘积。不同 $n$ 之间的派生过滤兼容、乘法、动力或对偶兼容不在主张内。
普通 $H^0$ 的非平坦基变换不被宣称总是同构。

### 2.4 C2：原圆分 pencil 的完整特化与全部初等因子

任意素数 $p$、整数 $a,m\ge1$、$p\nmid m$，
$$N=p^a,\quad r=mN,\quad s=\zeta_r,\quad
\mathcal O=\mathbb Z[\zeta_r]_{\mathfrak p},\quad\mathfrak p\mid p,\quad
t\in\mathcal O^*.$$
令 $\pi$ 为该 DVR 的参数，$\kappa$ 为剩余域，$e=v_\pi(p)$，
$\eta=\bar s$ 的精确阶为 $m$，$J=I_{m,\eta}$，其时间参数为 $\bar t$。
沿 $q=s,\tau=t$ 取 $(\mathcal S,\mathcal D)=(S,D)_{\mathcal O}$，
并令 $\mathcal L_n=\mathcal O_{\mathcal S}(n\mathcal D)$。
在同一个完整光滑相对曲面 $\mathcal S/\mathcal O$ 上，
原 $1,I_r$ 生成射影平坦态射 $f_r:\mathcal S\to\mathbb P^1_{\mathcal O}$，且
$$\bar f_r=\operatorname{Pow}_N\circ f_m.$$
这里 $\operatorname{Pow}_N$ 保持底域常数，不偷换成绝对 Frobenius。
每个有限几何剩余纤维是小阶完整几何整约化纤维的 $N$ 倍；
无穷纤维准确为 $r\bar D$，不是仅比较点集。

原截面空间准确为 $H^0(\mathcal S,\mathcal L_r)=\mathcal O\langle1,I_r\rangle$，
其实际基变换像为
$$\kappa\langle1,J^N\rangle\subset
H^0(\bar{\mathcal S},\bar{\mathcal L}_r)
=\kappa\langle1,J,\ldots,J^N\rangle,$$
余核维数为 $N-1$。又有
$$H^1(\mathcal S,\mathcal L_r)\simeq
\mathcal O\oplus\mathcal T,\qquad
\mathcal T\simeq\bigoplus_{j=1}^{r-1}\mathcal O/(1-s^j)
\simeq\bigoplus_{b=0}^{a-1}
\left(\mathcal O/(\pi^{e/\varphi(p^{a-b})})\right)^{\oplus\varphi(p^{a-b})}.$$
自由项来自通用复形的 $j=r$ 项。全部初等因子保留，不只报告总长度；
其推论为 $\operatorname{length}_{\mathcal O}\mathcal T=ae$、
最少生成元数 $N-1$、$\operatorname{Fitt}_0^{\mathcal O}\mathcal T=(r)=(\pi^{ae})$。

### 2.5 C3：原整除微分、实际 Jacobian 与原光滑能级

在 C2 的全部参数下，$d$ 只作用于状态 $x,y$，固定 $s,t$。
令 $T=\bar t^m$、$\varepsilon=(-1)^{m+1}$、$\sigma=(N-1)/(p-1)$，则
$$\alpha=p^{-a}dI_r\in
\Gamma(\mathcal U,\Omega^1_{\mathcal U/\mathcal O}),\qquad
\bar\alpha=H_p(T,J;\varepsilon)^\sigma dJ,\qquad
\mathcal U=\mathcal S\setminus\mathcal D.$$
准确多项式为
$$H_p(T,h;\varepsilon)=
\begin{cases}
[Z^{p-1}]\big((T+hZ+Z^2)^2-4\varepsilon Z^3\big)^{(p-1)/2},&p\ne2,\\
h,&p=2.
\end{cases}$$
其关于 $h$ 首一、次数 $p-1$。在全部四末端线及任意局部自由微分标架中，
$$\operatorname{coeffideal}(\bar\alpha)
=(H_p(T,J;\varepsilon)^\sigma)\operatorname{coeffideal}(dJ).$$
$dI_r$ 沿整个剩余曲面泛点的公共 $\pi$-阶恰为 $ae$，与 C2 的扭子长度及其 Fitting 参数阶相等。
这不是逐闭点提升的实际赋值，不是理想的 $\pi$-饱和，也不是两类对象的典范模同构。

保留谱曲线
$$E_{T,h}:\lambda^2-(T+hZ+Z^2)\lambda+\varepsilon Z^3=0$$
上指定微分 $\omega=dZ/(2\lambda-(T+hZ+Z^2))$；
特征二按 $dZ/(T+hZ+Z^2)$ 解释。
在完美域上的 Cartier 规范为 $\mathcal C(\omega)=H_p^{1/p}\omega$，
Hasse 系数是 $H_p$，不把二者混为同一个线性矩阵标量。
其一般域零点性质可几何基变换检验。

本候选进一步保留：原 $m$ 阶实际泛曲线的 Jacobian 经真实谱模构造同构于该 $E$，
并以所运输的指定微分解释 Hasse；原每条光滑几何闭能级与对应光滑谱／Weierstrass 曲线
通过保持原能级参数的完整局部模型同构相接。
因此在原光滑能级开集，$dJ$ 不消失，系数理想是 Hasse 零除子的拉回并将重数乘 $\sigma$；
光滑层的 Hasse 为零等价于其椭圆 Jacobian 超奇异。
不把奇异三次曲线称为超奇异，不以同一四次式代替实际 Jacobian 或闭纤维识别。

## 3. 可拓扑排序的当前依赖图

下表每行依赖的节点均在其前；同一行的来源区间代表必须保留的完整推导入口，
不是宣称一个结论句已经替代相应证明。节点是已有证明的组织标识，不新增更短引理。

| 次序／节点 | 前置节点 | 所供给内容、实际消费者及来源 |
|---|---|---|
| 01 Mraw | 无；原已知矩阵／JR 输入 | 原矩阵、排序、迹与行列式、首项；Ddiff 31–52，Ssplit 60–82，Jspec 119–150；供 Ppole、Ssec、Jdata、Dzero、Ddiv |
| 02 Pgeom | Mraw 的原系统 | 实际辛映射、八中心、反典范 SNC 八环及四末端图；P 94–163，Nbd 68–146；供 Ppole、Nglue、Gfield、Ffinite、Imodel、Hlocal |
| 03 Ppole | Mraw、Pgeom | 八边界赋值传递及四末端完整无极点式，原极除子与 pencil 截面；P 165–257；供 Gfield、Ssec、Gpencil |
| 04 Nglue | Pgeom | 实际正规丛、节点标架、单位粘合及精确阶；Nbd 148–269；供 Gfield、Inode、Ssec |
| 05 Gfield | Pgeom、Ppole、Nglue | 域上完整最小 pencil、Stein、全特征泛光滑及完整能级；Gfield 95–253；供 Ffinite、Specgeom、Jactual、Gpencil、C2image、Hlocal |
| 06 Ffinite | Pgeom、Gfield | 实际有限纤维几何整约化；Ffib 128–245 的完整格与分量论证；供 Gpencil、Hlocal |
| 07 Imodel | Pgeom | 同一整数八截面光滑射影族、完整 $E$ 的相对 SNC／平坦性；Ucoh 105–112、Ssplit 112–129；Gint 113–121 是其原 DVR 消费；供 Iconst、Inode、Ssec、Gpencil |
| 08 Iconst | Imodel | 实际逐次吹起推前、Leray／Čech，$R\Gamma(\mathcal O)=R[0]$；Ucoh 114–125；供 Uext |
| 09 Inode | Imodel、Nglue | 单位节点消元、全 $R$ 上边界两项复形；Ucoh 127–148；供 Uext，亦供原 DVR 边界消费者 |
| 10 Ssec | Mraw、Ppole、Imodel、Nglue | 全共振整数基上的 $C_j$ 完整截面与单位限制；Ssplit 131–266，连同其 Step 1 模型；Ucoh 150–179 为准确消费；供 Uext |
| 11 Uext | Iconst、Inode、Ssec | 非零因子层序列、边界 Bockstein、自然性及有限阶商生成元，逐级分裂；Ucoh 181–197；供 Uderived |
| 12 Uderived | Uext | 保留常数映射的截断三角、投射维数一与 $\operatorname{Ext}^2$ 消失；Ucoh 199–209；供 Ubase |
| 13 Ubase | Uderived | 任意派生基变换、kernel/cokernel、Fitting；Ucoh 211–236；完成 C1，供 C2image、Smith 和 DVR 共享上同调输入 |
| 14 Jdata | Mraw | 原谱二图、循环作用及矩阵数据；Jspec 119–182、214–234；供 Wpure、Specgeom、Jactual |
| 15 Wpure | Jdata | 原谱开集变换、纯三次族性质、完整临界概形双向消元及有限性；Wreuse 70–104，实际供给 Bbad 140–161、217–244、305–311、331–365；供 Specgeom、Hlocal |
| 16 Specgeom | Jdata、Wpure、Gfield | 所有端点、有限平坦推送、循环商／固定分歧点及任意原域几何前提；Wreuse 106–161；供 Jactual、Hlocal、DHasse |
| 17 Jactual | Gfield、Jdata、Specgeom | 真正谱模、有理逆、固定 Picard 差、无核及原域 torsor/Jacobian 下降；Jspec 236–453；供 Hlocal、DHasse |
| 18 Hlocal | Pgeom、Gfield、Ffinite、Wpure、Specgeom、Jactual | Hloc L(a) 及完整实际前提；Hloc 193–257、278–299，Bbad 138–166、217–251；供 C3 原光滑闭能级解释 |
| 19 Dzero | Mraw | 重复矩阵块、迹 Frobenius，原 $\bar I_r=J^N$；Ddiff 101–109；供 Gpencil |
| 20 Ddiv | Mraw | 原顺序的循环插入、整数先除、约化、Cayley–Hamilton、Hasse 迭代和非零首项；Ddiff 111–204；供 Dglobal、DHasse |
| 21 Gpencil | Imodel、Ppole、Gfield、Ffinite、Dzero | 原整截面延拓、全模型无基点、射影平坦、幂复合与概形纤维；Gint 123–148；供 C2image、Dglobal |
| 22 C2image | Ubase、Gpencil、Gfield | 保留原 $1,I_r$ 基及其实际特化像、投影公式、余核；Gint 181–198、207–220；完成 C2 的几何线性系部分 |
| 23 Smith | Ubase；C2 的固定圆分参数 | Ucoh 227–230 的 DVR 特化、Ssplit 360–387 的完整 (S14)–(S15) 赋值与重数；完成 C2 的全扭子部分，供 C3 公共阶比较 |
| 24 Dglobal | Gpencil、Ddiv | 局部自由微分层的余维一延拓、四末端线、局部系数理想及准确公共阶；Gint 222–233；供 C3 |
| 25 DHasse | Ddiv、Specgeom、Jactual、Hlocal | Ddiff 206–233 的 Cartier 与理想式，结合真实泛 Jacobian 和原光滑闭能级同构；完成 C3 的实际 Hasse 解释 |

主结果的合取出口为：

| 主结果 | 必要完成节点 |
|---|---|
| C1 | Imodel、Iconst、Inode、Ssec、Uext、Uderived、Ubase；其 P/N/原矩阵前提按图保留 |
| C2 | Gpencil、C2image、Smith；完整消费域上 Gfield/Ffinite，而非只引用旧 T1 名字 |
| C3 | Dzero、Ddiv、Dglobal、DHasse、Smith；DHasse 的 Jactual/Hlocal 不因其他代数式已经成立而删除 |

## 4. C1 与 C2 共用证明的精确选择

### 4.1 不能删除的整数截面与扩张接口

Ssplit Steps 1–5（112–266）必须完整保留：
完整环面边界 $E$ 的平坦性；允许极点商 $L_j(kE)/L_j$ 的有限过滤与平坦性；
共振环嵌入全部 $d\mid j$ 的特征零分支；重复块与 Cayley–Hamilton 给原 $C_j$
关于低阶 $I_d$ 的首一多项式；各分支的域上极除子输入；实际下降；
原矩阵幂等负 $x$ 首项
$$[x^{-j}]C_j=(-\tau)^j q^{j(j-1)/2}\in(R/(1-q^j))^*$$
及 Nbd 指定节点单位帧的全八环传播。
不能只检查本原分支、只说特征零点稠密、对非正规共振环套 Hartogs，或将非零误作单位。

Ucoh 181–197 的 Bockstein 自然性和有限阶必须保留；
在非局部 $R$ 上直接在被 $1-q^j$ 杀死的模中乘商环单位，不增加其在 $R$ 中可单位提升的假设。
Ucoh 199–209 的二阶扩张障碍必须保留；上同调模同构本身不自动给派生分裂。

### 4.2 合法共用与已接受替代

当前主路径采用完整已接受的 Ucoh 通用扩张证明。
Gint 150–205 中的节点、常数／高次上同调、扭子过滤与长度模块，
以及 Ssplit 268–295 的相同 DVR 输入，按 Ucoh 的同模型特化只计算一次共同证明。
这不是新增更短引理，也不是只保留通用结论而删掉其整数图、常数上同调或节点计算。

C2 的模分裂从 Ucoh 227–230 得到；
Ssplit 268–359 的 DVR 层序列、Bockstein 和逐级分裂作为已接受的独立替代证明原地保留，
不回头充当 Ucoh 的分裂前提，故没有 U 与 S 的分裂循环。
但 Ssplit 112–266 的通用截面和 360–387 的 (S15) 根单位赋值证明仍为当前必要块。

Gint 191–198 的原基识别不能仅靠抽象自由秩二替代：
需要原 $I_r$ 的单位边界限制、限制映射满射及原常数，才确认基确为 $1,I_r$。
Gint 207–220 还必须保留 Gfield 的 $f_{m*}\mathcal O=\mathcal O$、
投影公式、实际像 $\kappa\langle1,J^N\rangle$ 与乘 $\pi$ 序列。
$N-1$ 是余核维数／生成元数，不与长度 $ae$ 混同。

## 5. 实际泛 Jacobian：不能用纯谱方程替代的完整链

本节旧域上接口用 $\ell\ge1$ 表示参数的精确阶：先在任意特征代数闭域 $k$ 上取
$s,t\in k^*$、$\operatorname{ord}(s)=\ell$、$T=t^\ell$、$\varepsilon=(-1)^{\ell+1}$；
正特征自动有 $p\nmid\ell$，再按 Wreuse Step 2a 返回任意原域 $k_0$。
C3 的实际剩余 Jacobian 消费取 $\ell=m$；此记号不将剩余精确阶误写为 $r=mp^a$。

Jspec 236–453 逐段为当前必要证明，不采用“同一亏格／同一四次式所以 Jacobian 相同”的捷径：

| 段落 | 真实供给与不能丢失的义务 |
|---|---|
| 236–267，Step 2 | 原谱代数对秩二丛的作用、非标量／循环向量、完整谱线丛族及原能级到 Picard 的态射 |
| 269–288，Step 3 | 谱线丛只决定常数共轭；族上的 Picard 开集／原点刚性化使重构成为有理数据 |
| 290–334，Step 4 | 原矩阵系数恢复 $x,y$，给实际有理逆；不能只取得分离度一而遗漏纯不可分次数 |
| 336–384，Step 5 | 循环线丛同态的乘积是 $\lambda$，不是恒等；实际 $\operatorname{div}(\lambda)$ 给与原能级点无关的固定差类 |
| 386–423，Step 6 | norm／pullback、阶数可逆、完全固定点消除整个核及切空间平均，准确识别不变连通 Picard 部分 |
| 425–453，Step 7 | 连通像占满陪集、有理逆成为同构、作用在原域下降；给真正 torsor 与 $\operatorname{Jac}(X)\simeq E$，不预设 $X(K)$ 有点 |

其泛几何前提采用 Wreuse V2 106–161 的已接受替代：
谱二图的四端点偏导为 $-T,T,-1,1$；
中间覆盖 $Z=z^\ell$ 在 $\ell\in k_0^*$ 时 étale；
有限平坦推送分别为 $\mathcal O\oplus\mathcal O(-2\ell)$ 与 $\mathcal O\oplus\mathcal O(-2)$；
据此核定射影性、几何连通／整性、亏格、循环商及完全固定分歧点。
$\ell=1$ 是恒等覆盖；正特征的域上精确阶自动与特征互素。

Wreuse 148–161 的 Step 2a 保留任意原域 $k_0$、
$K_0=k_0(c)\subset\bar k_0(c)$ 的忠实平坦接口，不要求扩张可分或 $k_0$ 完美。
几何前提下降后，Jspec Steps 2–7 仍在原 $K_0$ 上执行，不只在代数闭扩域识别。
Wreuse 只替代这些前提的证明，绝不替代 Jspec 的上述真实谱模链。

## 6. W 的纯有限临界代数与 H 的闭纤维接口

### 6.1 Wpure 的无循环入口及必要消元

Wreuse 70–104 先把原谱方程当作纯方程，消费 Bbad 140–161 的开集互逆变换与清分母恒等式，
此时不引用尚未核定光滑性的射影同构，不引用实际 Jacobian 或实际临界长度。
Bbad 217–244 的纯三次族证明给唯一光滑零截面、所有几何纤维整约化、平坦与总空间正则；
总空间正则不被用来直接断言所有纤维光滑。
Bbad 305–311 的 hypersurface 微分表示给相对临界理想 $(F_u,F_v)$，无穷远为单位理想。

泛光滑出边实际需要 Bbad 331–365 的完整概形级双向消元：
临界概形全在 $uv\ne0$ 开集，包括其非约化结构；
由 $F=F_u=F_v=0$ 消去 $c$，保留
$$v^2=u^2(T-u),\qquad\varepsilon Tv=u^3,\qquad
z=v/u,\quad u=T-z^2,\quad v=z(T-z^2).$$
得到
$$Z_W\simeq\operatorname{Spec}k[z]/\big((T-z^2)^2-\varepsilon Tz\big),\qquad
c=\varepsilon-z-z^3/T.$$
逆向构造不可略：常数项 $T^2\ne0$ 给 $z$ 可逆；
关系 $(T-z^2)^2=\varepsilon Tz$ 给 $u$ 可逆，再给 $v=zu$ 可逆；
反向代入三个原方程，排除除法漏支。
整个证明只用 $T\ne0,\varepsilon^2=1$，不除以 $2,3$，不假定四次式可分。
首一四次商环是有限四维代数，故泛相对临界概形为空；
Wreuse 103–104 再用 hypersurface Jacobian 判据取得几何泛光滑。
这里四维是纯 $Z_W$ 的商环维数，不是实际 $Z(dI)$ 的长度。

Bbad 366–387 的四列 $4\times4$ 乘 $c$ 矩阵和 389–408 的完整行列式求值
属于原 $W_0$ 包并完整保留，但不是 Wreuse 103 的泛光滑前提。
它们的强消费者是 Wreuse 188–196、Hloc 311–333 的实际临界特征多项式出口。
不能从那个出口画返回泛谱光滑或 Jactual 的依赖边。

### 6.2 Hlocal：原光滑闭能级的直接消费者

Hloc L(a) 的准确陈述／前提在 193–212，完整证明在 224–257。
它需要两个正则、proper、flat、finite type 模型，
几何光滑射影整亏格一泛纤维、几何整约化特殊纤维，
Weierstrass 零截面、给定的带原点泛同构，以及真实固定的 $E$-torsor 作用。
任意原域版本还要求光滑原域点 $q_0$；不能无条件删去该点条件。

证明必须保留普通 henselization、光滑点提升、相对最小性与唯一延伸：
普通 henselization 保持原剩余域；局部截面不授予原 $k_0(c)$ 全局截面；
唯一重数一主纤维自交零，排除第一类例外曲线；
固定 torsor 作用和选定截面给指定泛同构；
正亏格最小正则模型唯一性使同构及其逆延伸，稠密性确认两个复合恒等。
不同截面选择不被宣称给同一个同构。

Hloc 278–299 逐项核定实际前提：
Gfield 给实际 proper/flat/泛亏格一，Ffib 128–245 给特殊纤维几何整约化；
P 给原光滑吹起曲面，局部化及 ind-étale henselization 保持所需正则性；
Bbad 217–251 给纯 W 模型对应性质，泛光滑按 Wpure 的有限临界代数路径；
Jactual 给真实作用，Bbad 162–166 在已知泛光滑之后给带原点 $E\simeq W_K$。

本 C3 的原光滑几何闭能级解释可在代数闭域选取实际非空光滑开集中的点，
正是 Hloc 297–299 的非动力消费者；不需要 V、有限域 Weil 选点或指定回返共轭。
据 L(a) 得到保持原 $c$ 的完整特殊纤维同构，
从而取得 Bbad 422–439 的 (20) 首项“实际纤维光滑当且仅当 W 纤维光滑”所用接口。
再与 Ddiff 的指定微分及 Cartier 解释相接，完成 C3，不能只保留泛同构。

### 6.3 不倒灌旧强 T3，也不删除旧证明

Hloc L(c) 的临界出口在 219–222、262–274，实际消费者在 301–333；
它继续消费 Bbad 293–327 的内禀 Fitting 与原 $Z(df)$ 识别、两侧有限性、
henselization 有限阶商、原 Artin 块及乘 $c$ 算子的保真，
再消费 Bbad 329–408 的完整消元、矩阵、行列式，取得实际长度四与强 $R=\delta$。
这是旧强 T3 的完整证明链，保持冻结和接受。
但 C3 的微分系数理想乘积由 Ddiff 恒等式直接给出，
其光滑闭能级 Hasse 解释直接消费 L(a) 模型同构，不逐项调用上述全部强数值结论。
因此不能把旧 T3 额外结论反向增列为新 C3 主张。

Hloc 236–243 的最小正则模型与 Bbad 168–215 的最小整 Weierstrass 方程不同。
前者直接服务当前 L(a)；后者的判别式赋值、十二次幂变换及其旧结论完整保留，
不被前者替代，也不因当前选择 Wpure 泛光滑路线而变成必要前提。
同样，Bbad 422–439 的全部精确判别式／好约化链保持为旧出口；
当前保留完整光滑纤维同构，不据此添入全部好约化主张。

## 7. 原微分证明与主要标准工具的实际位置

Ddiff 111–142 必须先在原整数表达式中完成长度 $r$ 的循环插入整除，
再约化为长度 $m$ 的表达式；不得在特征 $p$ 中除以 $r$ 或从零式 $d(J^N)$ 猜首项。
144–192 的二阶矩阵递推及 Hasse 迭代保留，194–204 的原 Laurent 首项保证非零与准确公共阶；
206–233 的指定微分、特征二残差表达、Cartier 半线性及理想而非根集保留。
Gint 222–233 使用原完整曲面和局部自由微分层作余维一延拓，
不仅是在四末端线计算有限极限。

| 标准工具 | 已有证明中适用条件与位置；本图不新增工具定理 |
|---|---|
| 吹起推前、Čech、Leray、节点正规化序列 | Ucoh 105–148 实际图与相对节点单位计算；不从逐点维数猜全环自由性 |
| Cayley–Hamilton、平坦允许极点商、Bockstein、截断三角 | Ssplit 131–266，Ucoh 181–209；非零因子、平坦性、商单位和 $\operatorname{Ext}^2$ 条件逐项保留 |
| proper 相干平坦的 perfectness／任意派生基变换 | Ucoh 213–218 引 Stacks 30.22.1／07VJ；底环 $R$ Noetherian，$S/R$ proper，$L_n$ 相干且底平坦；目标 $A$ 不受 Noetherian 限制 |
| Stein、Riemann–Roch、伴随及全特征泛光滑 | Gfield 95–253、Ffib 128–245；包括不可分复合排除及 $p=2,3$ 的准椭圆风险，不以算术亏格一代替 |
| 正常反身模余维一交、逐纤维平坦 | Gint 123–148、222–233，原引用 Stacks 0AVB、039C；正常光滑完整模型、局部自由层和有限呈示条件保留 |
| 根单位赋值及 Fitting／Smith | Ssplit 360–387、Ucoh 220–230；用 $\Phi_{p^h}(1)=p$ 和单位比值证明全部赋值及重数，不由长度猜初等因子 |
| henselian 光滑点提升、最小正则模型唯一性 | Hloc 224–257 的 Stacks 15.9.14、55.8.4、55.10.1–2 及 henselization 条件；不是未知 Jacobian 身份的替代物 |
| Cartier 半线性及 Hasse 迭代 | Ddiff 164–233；Hasse 迭代作为 Vlasenko Theorem 1(i) 的直接特例按既有来源差分扣除，不要求 ordinary，不借逆矩阵结论增加超奇异下一阶 |

这里的标准来源入口沿已接受证明和来源记录消费；
本次没有重新打开外部原证，也不声称对这些来源作新的全文核查。

## 8. 必要共享、保留替代与不消费的旧背景

| 类别 | 当前准确处理 |
|---|---|
| 必要共享 | 原模型 P/N、Ucoh 的完整整数常数／节点／扩张／派生证明、Ssplit 的通用截面和 (S15)、Wpure 的完整有限临界代数；每个共同推导只计一次实际证明 |
| 必要且不能被共享名义略掉 | 原 $I_r$ 的完整极除子及四末端正则性，Gfield 的完整 pencil／Stein／全特征泛光滑，Ffib 的实际有限纤维整约化，Jspec 真实谱模全链，Hloc 同底完整模型及实际前提 |
| 已接受替代，原地保留 | Ssplit 的 DVR 分裂另证；Gint 的原 DVR 上同调过滤／长度证明；旧 Sspectral 长判别式、Jspec 单独特征二消元；Bbad 原局部模型比较及 Hloc 接替路径；Wreuse V1 和其真实条件记录不被 V2 覆盖 |
| 旧强结论保留，不反灌新主张 | Bbad/Hloc/Wreuse 的实际 Artin 块、长度四、完整临界特征多项式、最小整方程及全部好约化；Ffib 的 Chern／GRR 长度与自治校验 |
| 不被 C1–C3 直接消费的旧动力结果 | R 的全回返／Picard 增长／非挠性，V 的指定回返点，C 的指定闭纤维回返共轭及有限域选点，Q 的奇异群与指定元素，I 的循环清单，O 的 Hasse 点数界与分箱，Paper11 的旧循环包含 |

最后一行是新消费者范围，不删除原 T1–T7。
尤其 Ddiff 的 Cartier–Hasse 多项式不是 O 的 Hasse 点数界；
原光滑闭能级同构的非动力出口不通过指定回返或循环结论证明。

## 9. 不能删的接口、无新假设与未授权扩张

1. C1 保留全部 $n\ge0$、全部交换 $R$-代数、非约化与非平坦基变换；
   共振基不假设正规；$q,\tau$ 仅按原范围为单位。
2. C2/C3 保留所有素数，含 $2,3$，所有 $a,m\ge1$ 且 $p\nmid m$、每个固定 $t\in\mathcal O^*$，
   包括 $m=1$、$a=1$、特殊时间参数和坏值碰撞；不要求四次式可分或 Hasse 非零。
3. 域上精确阶的几何证明用于其本来允许的特征；整数 $r=mp^a$ 不被当成剩余域中仍精确阶 $r$。
4. 原矩阵、能级、整数系数提取和完整四末端线保留；
   幂态射不与绝对 Frobenius 混用，剩余曲面本身不变成 $N$ 个曲面。
5. 实际泛 Jacobian 保留任意原域下降和非平凡 torsor；
   闭能级解释经真实模型同构；任意域 L(a) 的点条件不被抹去。
6. U/S 接受合取、Wreuse V2 的任意原域修正、Hloc 的已接受局部模型复用保持；
   不能因图中出现“共享”而跳过已接受推导，也不因为旧文件仍含强结论而强迫每个新消费者全部调用。
7. 不声明跨 $n$ 派生过滤兼容、截面环／cup product／动力／对偶兼容、
   稳定或半稳定约化、野导子、超奇异下一阶 jet、逐闭点精确提升赋值、$\pi$-饱和或典范模同构。
8. 本图没有补充新数学假设，没有重做作者证明或局部独审；它只是显式列出已经接受的必要链和合法复用。
   如果后续正式评审提出真实新增缺口，应定位相应消费者，不用本图预先宣告其必然通过。
9. 不估页、不试写英文正文、不编译，不建立论文项目或 source/publication locks；
   准入及后续动作服从主控正式双票处置，不由本图代签。

## 10. 输入身份、本人的实际读取与停止边界

### 10.1 必要作者件与范围输入

下表哈希为本次在实际文件上核对的完整 SHA-256。
“全文”包括在紧邻只读依赖任务中本人已亲读、此次复核身份后复用的区间；
定向读取不借其他代理的已读记录冒称全文。
所有本图现列必要科学区间均已由组织者本人读到；Ssplit 此次补齐全文，
Wpure 的 Bbad 双向消元和 Hloc 直接消费者此次再次按行号核读。

| 输入 | 本人实际读取范围 | SHA-256 |
|---|---|---|
| Integral V1 brief | 全文 1–270；对照 C1–C3，无范围／接口变更 | 59f21705782443e9ac57aeb0f62c80f198f7fd18cec1a5ad3e496f0cf2f71f13 |
| Integral 预审处置 | 全文 1–133 | 1ff8473c05956d88075dacc9705d79d621b2e9db059b59f5b13f06c72326641e |
| Phase A | 全文 1–107 | bb463d1e1c27f543e4a0fe1bda17b584ffce28148e49ab1e1f3c3b1fce6b7ad5 |
| Phase C/D | 全文 1–267；合并输出中段曾截断，已补读相应区间 | d76e5e71001cd8033608a76673f61169f264caee57cb37aab4f86d1390dd8f02 |
| P | 全文 1–275 | 61d2b0ace7003e19ff1e81242e4080402049d98c024657b94d9b812086f358b3 |
| Nbd | 全文 1–284 | 8234b5584adba10ec02adb0269300b0c5191b5445fca345e28e1eb5171c12469 |
| Gfield | 全文 1–270 | 0d7a3e2d37eb7218feddfe5c85bf244a0be358bfcc880279d5f14afd5cb77ace |
| Ffib | 7–57、79–93、128–272 | 3b7a495b723d9ba45003fe767431c4420053c0b3de6656a2335c3aad01307003 |
| Jspec | 7–77、119–182、214–334、336–454 | a6aa5e30ea0795b05790b058dfd4debc6431de1918090b9a6add88351a1eb63f |
| Wreuse V2 | 全文 1–213 | 21196a27cd0612db0fc858ce38b6671d4a8b9a7b6e183c48c570dd11994febe2 |
| Bbad | 138–251、293–456；旧 253–291 以已接受 Hloc 替代定位，未在本次重读 | 1e7ade432e62b1e116270d2588d0d798accbf482fcc6edd46dca12b76be42bb1 |
| Hloc | 191–336，含 L 全文、实际前提与旧强 B 消费者 | 0a6624550ed0f8765b51b01a1a481fd9a545d1791e10c3431effbf3f25428a3e |
| Ucoh | 全文 1–255 | a1e50c82c32f5411dce28a2bf2ff2b10bf4fdefdb8ac9b127de852de5e36c42b |
| Ssplit | 全文 1–418；最终记号补齐版 | 2848ab1623d4e339b5f17fb184433ed68a4eb0bba8d37ca04291031d4b32f7ac |
| Gint | 全文 1–254 | 59b308f605832d82e00720c5a3a7871c862698e194503ff3b289da592ced28e0 |
| Ddiff | 全文 1–268 | e2f032ff1197d415be611670e3d233efd7f6ead0d7dbe16b05f796ed42f43652 |

### 10.2 接受证据的定位与阅读责任

| 接受输入 | 本人实际范围与效力 | SHA-256 |
|---|---|---|
| [域上入口处置](PAPER30_QPI_GENERIC_FIBRE_ENTRY_DISPOSITION_V1_20260908.md) | 本人读 1–115；原 P/N/Gfield 的独审与同哈希合取按该处置继承，不冒称本人重审旧报告 | ed09aadb40752ed579bc45edb7b3531c1f78f6c7f7413072cd120315f2b22245 |
| [动力几何处置](PAPER30_QPI_DYNAMICS_GEOMETRY_DISPOSITION_V1_20260908.md) | 本人读 8–75、151–176；Ffib/Jspec/Bbad 接受按原处置继承 | 0bfbde8003d049d80523a2001d410dfa4f38ab2f14838d2dbbe4c1363f7155a7 |
| [Wreuse 非作者 V2](PAPER30_QPI_SHARED_WEIERSTRASS_PROOF_REUSE_NON_AUTHOR_REVIEW_V2_20260908.md) | 本人全文；任意原域 Step 2a 的 V2 接受，不覆盖 V1 条件记录 | 0db56630eab29ed89952f28dd2fd8038fa3c724040f99afbec527dd0e42c70f2 |
| [Hloc 接受处置](PAPER30_QPI_POINT_MODEL_PROOF_REUSE_DISPOSITION_V1_20260909.md) | 本人全文 1–87；明确 L(a)/L(b)/L(c) 的不同消费者，12 PASS 的既有合取 | 40e4fa6460d34ebff7cfc0e20d614f3a2050590f10c58605819cba867e65dad7 |
| [整系数数学处置](PAPER30_QPI_INTEGRAL_MATHEMATICS_DISPOSITION_V1_20260909.md) | 本人全文 1–162；新 D/G/S/U 同哈希接受，关闭 U 的 S5/S7 条件 | 1465d67fffba05e83bd1d00cd12c8d6057c25888b31e119e315ed8dcbc2306af |

下列对应独审的完整文件身份也已在本次核对；其科学接受由上表处置消费。
本依赖组织任务没有新读其全文或再做局部审查，不能将哈希核对说成证明检查。
它们仍须与作者件一同进入正式共同全文输入；其余旧作者独审由主控清单逐一绑定。

| 对应独审 | SHA-256 |
|---|---|
| [Ddiff 独审](PAPER30_QPI_CYCLOTOMIC_DIFFERENTIAL_CHECK_V1_20260909.md) | 7c0ecd10991f80f0614713f344ab600a4eb69fd7356135fcfc927ed71a95d0bb |
| [Gint 独审](PAPER30_QPI_CYCLOTOMIC_GLOBAL_MODEL_CHECK_V1_20260909.md) | ec49d4eaadbf4c0d53603cf6c902df375e2b1c779b6f243897521d786b206a0b |
| [Ssplit 独审](PAPER30_QPI_CYCLOTOMIC_TORSION_SPLITTING_CHECK_V1_20260909.md) | ae768ae89301af115dc917e9a4b075b401258fb563628e1238b01844a30da941 |
| [Ucoh 独审](PAPER30_QPI_UNIVERSAL_COHOMOLOGY_CHECK_V1_20260909.md) | 9f54da405b8a40f58e34dc372fad7200452871171a92a0e0063edf1742e3cd55 |
| [Hloc 独审](PAPER30_QPI_POINT_MODEL_PROOF_REUSE_NON_AUTHOR_REVIEW_V1_20260909.md) | 10122ea2a617203dcf0ef7d9755ce0ae22ec7906c70ab141891998f94294093b |

本次亲读 proof-writer 全文；只应用准确主张、假设、依赖图与边界组织，不运行新证明可行性评分。
另读 AGENTS、WORKFLOW，并从 BATCH 当前 qPI 段定位；批次快照中较早“查新进行中”不撤销本次新授权。
有一个不写文件、不重审数学的独立子任务定向定位 Wpure/Hlocal 出边及行号；
组织者本人已读相同必要科学段落，子任务结果只作组织边界交叉检查，不是一张独立数学票。

本轮唯一新增对象是本文件；未修改作者稿、独审、处置、旧失败、组合报告、锁或接受产物。
未扫描旧 47 件全文或构建树；未外部写入。
提交前对本文件全文回读并另报最终哈希，随后停止改动；本文件不放自引用哈希。
