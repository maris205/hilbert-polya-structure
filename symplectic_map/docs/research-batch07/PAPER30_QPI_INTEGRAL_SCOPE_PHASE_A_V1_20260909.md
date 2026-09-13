# Paper30 qPI：整系数新问题的 Phase A 主张范围 V1

日期：2026-09-09。主控 `/root`。
类型：下一轮完整查新的问题提取；不是正式候选 brief、四门派发、立项或写稿授权。
本件采用 novelty-check 的 Phase A，仅完成准确对象和三个比较主张；
Phase B–D、组合内非碰撞和正式准入均未由本件完成。

## 1. 新问题及其与旧失败的区别

研究同一个 qPI 八截面初值空间沿根单位关系的整系数退化。
顶层对象是原几何族及其反典范线性系，不是有限域周期计数的重新措辞。
新的量词同时覆盖：无关系 $R=\mathbb Z[q^{\pm1},\tau^{\pm1}]$ 上全部 $nD$，
任意 $R$-代数的基变换，以及原精确阶 $mp^a$ 在 $p$ 上降为 $m$ 阶时的完整模型和微分。

旧 qPI T1–T7、V1/V2 的完整失败票与数学接受全部保留。
本件不把旧 T1–T7 删除、改成弱命题或声称旧票已经失效；
也不直接把旧候选加一个标题后重投。
新问题的正文范围与必要证明图尚待完整价值／容量审查，
不预判能够容纳全部义务，不以缩写或移出正文消除未来容量风险。

## 2. 固定原对象

使用 G 和 U 指定的同一八截面吹起，末次四中心坐标为 $1,\tau,\tau,q$。
$D$ 为八环反典范边界，$L_n=\mathcal O(nD)$；完整环面补集还包含四条末端例外曲线。
原矩阵及顺序为
$$M_j(z)=A(q^{j-1}z)\cdots A(qz)A(z).$$
在精确阶 $j$ 的域上，原积分由
$$\operatorname{tr}M_j(z)=t^j+I_jz^j+z^{2j}$$
固定；不作能级重标定或拟合。在 $q^j=1$ 但非本原的整数基环上，
使用实际系数 $C_j=[z^j]\operatorname{tr}M_j(z)$，不把其他谱系数合并成 $I_j$。

## 3. 三个应逐一比较的核心主张

### C1. 通用整系数反典范上同调及精确扩张消失

对所有 $n\geq0$，在 $R$ 上有
$$R\Gamma(S,L_n)\simeq R[0]\oplus\bigoplus_{j=1}^{n}[R\xrightarrow{1-q^j}R],$$
两项复形在次数 $0,1$，同构保留常数项。
固定一次选择后，得到所有交换 $R$-代数 $A$ 上的 kernel/cokernel 公式，
包括 $H^0$ 中的 $\operatorname{Ann}_A(1-q_A^j)$。
该主张来自 [U 的完整证明](PAPER30_QPI_UNIVERSAL_COHOMOLOGY_DIAGNOSTIC_V1_20260909.md)，
关键截面引理来自 [S 的 Steps 1–5](PAPER30_QPI_CYCLOTOMIC_TORSION_SPLITTING_PROBE_V1_20260909.md)。

比较重点是 $q^j=1$ 整个非正规整数基环上的真实单位边界截面和逐级扩张消失。
节点复形、Bockstein、投射维数一、派生基变换与 Fitting 计算都是标准工具。
任意基变换的形式推论、全部 Fitting 乘积及其圆分因子分解不另计一般方法创新。
需要查清：Looijenga／Halphen 通用周期族上是否已有定理直接包含这个具体对角复形，
尤其是否覆盖整数坏素位与非约化根单位关系，而不是只有复数纤维维数。

### C2. 原根单位 pencil 的完整平坦降阶及精确扭子模

固定任意 $p,a\geq1,m\geq1$，$p$ 为素数且 $p\nmid m$；
$N=p^a,r=mN,s=\zeta_r$，$\mathcal O=\mathbb Z[\zeta_r]_{\mathfrak p}$，$\mathfrak p\mid p$。
任取 $t\in\mathcal O^*$，剩余参数 $\eta=\bar s$ 精确阶为 $m$，$J=I_{m,\eta}$。
同一个完整光滑相对曲面上的原 pencil 射影平坦，并满足
$$\bar f_r=\operatorname{Pow}_N\circ f_m.$$
每个有限几何剩余纤维为小阶完整纤维的 $N$ 倍；无穷纤维准确为 $r\bar D$。
原完整线性系的基变换像为 $\kappa\langle1,J^N\rangle$，
相对于 $\kappa\langle1,J,\ldots,J^N\rangle$ 的余核维数为 $N-1$。
此外
$$H^1(\mathcal S,\mathcal L_r)\simeq\mathcal O\oplus\bigoplus_{j=1}^{r-1}\mathcal O/(1-s^j),$$
完整初等因子按 S 的 (S15)，而不只给总长度 $a\,v_\pi(p)$。

准确模型为 [G1–G2](PAPER30_QPI_CYCLOTOMIC_GLOBAL_MODEL_DIAGNOSTIC_V1_20260909.md)，
分裂为 S，亦由 C1 特化得到。C2 的模结构不是脱离 C1 的第二个一般发现。
需扣除域上 Halphen 判据、矩阵迹 Frobenius、正常性延拓与逐纤维平坦工具。
保留同一原能级、完整末端线、概形重数及原 pencil 非完整特化的区别。
不宣称任意能级提升已经获得稳定／半稳定模型或野导子。

### C3. 完整开放空间上的先除后约化微分与 Hasse 系数

在 C2 的全部参数下，相对微分仅作用于状态 $x,y$，固定 $s,t$。
原 $p^{-a}dI_r$ 在完整 $\mathcal U=\mathcal S\setminus\mathcal D$ 正则，且
$$\overline{p^{-a}dI_r}=H_p(t^m,J;\varepsilon)^{(N-1)/(p-1)}dJ,
\qquad\varepsilon=(-1)^{m+1}.$$
其中 $H_p$ 为 D 的准确谱 Hasse 多项式，特征二为 $H_2=h$。
系数理想等式在全部四条末端线也成立；公共 $\pi$-阶恰为 $a\,v_\pi(p)$，
与 C2 扭子长度相同、与其零阶 Fitting 理想相应。
证明为 [D1–D3](PAPER30_QPI_CYCLOTOMIC_DIFFERENTIAL_DIAGNOSTIC_V1_20260909.md)
及 [G3](PAPER30_QPI_CYCLOTOMIC_GLOBAL_MODEL_DIAGNOSTIC_V1_20260909.md)。

这里的 Hasse 迭代乘子已经被准确识别为 Vlasenko Theorem 1(i) 的直接特例，
见[来源差分](PAPER30_QPI_DIVIDED_DIFFERENTIAL_SOURCE_DELTA_V1_20260909.md)。
循环迹微分、Cayley–Hamilton 及 Cartier 半线性也是一般机制。
剩余比较量只能是原排序／原能级的整数桥接、全模型延拓及准确统一阶，
不能把上述标准指数、光滑层 Hasse 解释或理想乘法再列为独立新发现。
若进一步在正文称它为“实际泛 Jacobian 的 Hasse 不变量”，
必须保留旧 T2 的实际谱 Jacobian 识别所需完整证明，不能仅以相同四次式替代。
逐闭点提升赋值、$\pi$-饱和、超奇异下一阶 jet 与典范模同构均未证明。

## 4. 下一阶段必须完成而尚未完成的事项

1. 合取实际 D/G/S/U 非作者数学报告，核对全部依赖接口；作者证明数量不替代独立接受。
2. 对 C1–C3 各做完整多来源查新，至少三个准确查询表述，核近六个月至当前日期的相关 arXiv，
   区分找到的准确包含、一般工具、主题近邻和未取得全文的来源。
   ICLR／NeurIPS／ICML 不属本纯代数几何问题的针对数据库，不以无关会议检查装作覆盖。
3. Phase C/D 由非作者执行；若技能指定的 GPT-5.4 MCP 不可用，应如实披露实际替代，
   不把同家族独立代理说成跨模型核验，也不以该报告代替锁定的正式双份四门。
4. 定向核 C1–C3 与现有 Papers1–29 的真正消费者和定理包含，
   尤其 P18 的 Fitting／基变换及 P29 的 filtered cohomology；术语相同既不证明碰撞也不证明无碰撞。
5. 只有准确剩余与独立价值支持继续时，才形成完整新候选包及必要正文证明图。
   每位新意和价值至少7.5、证明信心至少9及完整自然22–30页门槛不变；
   不重抽旧票、不据作者稿行数测页、不预建项目／source/publication locks／论文 PDF。

本件不选泛 torsor 最小覆盖或 Weil–Châtelet 分类作为新中心，
也不并入仍未证明的全部点阶分布、稳定退化、跨系统族推论。
这些方向保留在本轮有界诊断中，不以它们的潜在价值补本件的新意。
