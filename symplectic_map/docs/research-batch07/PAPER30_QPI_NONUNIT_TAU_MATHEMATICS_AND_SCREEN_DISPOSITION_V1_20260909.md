# Paper30 qPI：非单位时间有界数学接受与预筛处置 V1

日期：2026-09-09。主控：`/root`。效力：本地研究记录。
`route_applicability: NOT_APPLICABLE`。
不是正式四门票、论文准入或整个全次数整数模问题的终结。

## 1. 当前结论

原八截面族延到 $B=\mathbb Z[q^{\pm1},\tau]$ 后，以下四项数学接受：
一阶真实上同调、零时间完整纤维的全次数固定部及维数、全次数实际 jet 复形、
以及精确 $q=1$ 切片的三阶整系数混合块。
四份作者输入及两份承担相应责任的非作者检查均由主控全文读取，最终身份见 §5。
没有把有限矩阵计算当成全次数几何证明，也没有把数学通过当成新意通过。

有界原始文献预筛指出：固定部与维数是 Harbourne 工具的具体推论；
全次数 fat-jet 呈示属于既有相对簇／吹起评价路线；
孤立混合列本身准确来自平移差分
$$ (z+\tau)^2-z^2=\tau^2+2\tau z. $$
所以非主 Fitting、不分裂和特征二厚度差异不能各自再计为新的通用机制。
本轮保留的窄残余是这些结构在指定八次吹起的实际上同调中如何出现。
现有证据不足以仅凭这个局部实现组织一篇满足当前价值与自然篇幅要求的独立长文。

因此处置为 **BOUNDED_PROBE_CLOSED / NO_FORMAL_CANDIDATE_AT_CURRENT_SCOPE**。
这不是正式评分 FAIL，也不是证明全素数猜式为假。
全次数整数规范形与全素数首现规律仍 OPEN；未把它们计入结果或篇数。
不重投旧 C1–C3，接续同族 P03 的一个小特征垂直微分诊断。
Paper30 未立项；Batch07 仍为 3/5，Paper31 尚未开展。

## 2. 准确接受范围

保持原四簇 $1+2+3+2$ 的有序中心。$S/B$ 光滑射影，$L=-K_{S/B}$。
这里延续的是指定曲面族与层，不声称原离散映射在 $\tau=0$ 仍双有理；
其原有理公式在该处塌缩的 caveat 不撤销。

### A. 一阶与零时间完整纤维

真实一阶复形为
$$R\Gamma(S,L)\simeq B[0]\oplus[B\xrightarrow{\tau(q-1)}B].$$
对任意基变换使用该实际两项复形，而非普通 $H^0$ 张量。
零时间反典范除子是十环，两个相邻 $(-3)$ 分量之和记为 $F$。
对任意底域、任意单位 $q$、任意 $n\ge0$，准确固定部分为
$\lceil n/2\rceil F$，去固定后部分无基点，且
$$h^0(S_0,L^n)=1+\frac{n(n+1)}2,\qquad
h^1(S_0,L^n)=\frac{n(n+1)}2,\qquad h^2=0.$$
零阶另由常数层处理。此全次数证明有明确固定部和 Harbourne 条件检查，
不是由 $n\le8$ 的数值序列外推；一般工具和直接推论不另计创新。

### B. 全次数实际评价模型

令 $d_n=2n(n+1)$。全次数作者件给出原中心的明确整数二项式矩阵 $J_n$，并证明
$$R\Gamma(S_A,L_A^n)\simeq[A^{d_n+1}\xrightarrow{J_n\otimes A}A^{d_n}]$$
对每个 $n\ge0$ 和每个交换 $B$-代数 $A$ 成立，包括非平坦与非约化基变换。
证明先作四次 toric 吹起，逐次评价均有单项式单位右逆；
最后四个相异 fat 截面产生真正的评价三角及 cokernel。
原八组矩阵与 $J_n$ 相差明确的可缩单位块，不仅 kernel 相同。

二阶进一步有完整整数分解
$$B[0]\oplus[B\xrightarrow{\tau}B]
\oplus[B\xrightarrow{\tau^2(q-1)}B]
\oplus[B\xrightarrow{\tau^2(q^2-1)}B].$$
独立检查重放全部 21 个单位 pivot 及四步剩余变换，没有反演 $2$ 或 $\tau$。

### C. 精确 $q=1$ 的三阶混合块

令 $R=\mathbb Z[\tau]$。实际复形为
$$R\Gamma(S_R,L^3)\simeq(R^{[0]})^4\oplus(R^{[1]})^2
\oplus[R\xrightarrow{\tau^2}R]^2
\oplus[R\xrightarrow{(\tau^2,2\tau)^t}R^2].$$
原 $48\times49$ 矩阵的全部 42 个单位 pivot、原 49 维源提升及七列整基均获精确核验；
源基行列式为 1，故不存在从有理函数域倒猜整数格的步骤。
记末块余核为 $\mathcal M$，则
$$\operatorname{Fitt}_1\mathcal M=\tau(\tau,2),\qquad
\operatorname{Fitt}_3H^1(S_R,L^3)=\tau^5(\tau,2).$$
第二个是实际余核首个非零 Fitting 理想，在 $(2,\tau)$ 非主，
因此不能由全标量对角有限自由呈示得到该实际模。
有不分裂正合列
$$0\longrightarrow R/(\tau)\longrightarrow\mathcal M
\longrightarrow(2,\tau)\longrightarrow0.$$
在 $k[\tau]$ 上，非二特征的三个扭子指数为 $(1,2,2)$，特征二为 $(2,2,2)$；
长度分别 5、6，但最底层 $\tau=0$ 域纤维均为 $(h^0,h^1)=(7,6)$。
“首次三阶”只指已完整比较的精确 $q=1$ 切片 $n=0,1,2,3$，不外推一般 $q$ 或素数。

## 3. 开放部分与有限计算的准确地位

[首素数作者探针](PAPER30_QPI_NONUNIT_TAU_FIRST_PRIME_OBSTRUCTION_PROBE_V1_20260909.md)
对其原全素数整模猜式 (P)、Fitting 目标 (F) 及全素数 Smith 目标均报告
**NOT CURRENTLY JUSTIFIED**。未得到反例，也没有全素数整数消元或实际连接映射计算。
同件 W1–W3 给概形基点集、真实 Koszul 递推及截面幂自由直和项的作者证明；
主控已全文读，但本件不授予这些新增引理非作者合取接受，不以它们代签 (P)。

此前有限精确 Smith 计算在 $p=2,3,5,7$ 的首个样本 $n=p+1$ 中，
均观察到相对特征零有 $p-1$ 个指数从 $p-1$ 升到 $p$。
这些是原实际矩阵上有限域／有理数域的诊断，不证明全素数首现、整数模同构或连接态射分裂。
各次有限样本实际输出保留；新的[可复算 Smith 脚本](qpi_nonunit_tau_smith_probe_v1_20260909.py)
只实跑过 `--case 3:0 --case 3:2`，正常 exit 0，不伪称其余旧样本已由新脚本重跑。

另有准确实现边界：冻结 `qpi_nonunit_tau_jets_diagnostic_v1_20260909.py` 的
`jet_matrix(0,...)` 会构造 $0\times0$ 空矩阵，而数学零阶应为 $0\times1$。
脚本主循环及本轮消元消费者均只处理 $n\ge1$；零阶数学由常数层与空评价另证。
因此不影响接受的全次数定理，但不把该函数声称为已实现零阶的完整接口；冻结文件不修改。

## 4. 来源扣除与为何当前不立项

两份有界来源报告分别为
[非单位参数初筛](PAPER30_QPI_NONUNIT_TAU_PRIOR_ART_SCREEN_V1_20260909.md)及
[三阶混合块原始文献预筛](PAPER30_QPI_NONUNIT_TAU_MIXED_BLOCK_PRIOR_ART_V1_20260909.md)。
主控均全文读取；报告准确披露其 primary 实读段、查询与访问边界。
主控另已读 Callan 四页原文及 Harbourne 所用定理必要段，不冒称读完所有来源。

- Harbourne 的非 nef 反典范曲面消失与固定部工具吸收零纤维增长的普遍机制。
- Kleiman–Piene–Tyomkin 的正／混合特征近点簇框架及 Proposition 5.9
  适用于重排后 $Y$ 上四个不同根点的 fattening；原簇内 strict diagram 的变化不能用来否认这一包含。
- Callan §5 的带权 Pascal 矩阵直接容纳上述平移差分列；这是准确的代数对应，
  不是声称原文写过本 qPI 的整个上同调余核。其全矩阵 Smith 结论也不能偷换为受限源子模的答案。
- Evain 碰撞方法、Zahariuc 反典范／fat-point 的特征依赖实例均保留；
  所读结论未直接给出本 $R\Gamma(L^3)$ 的整系数分解，不等于排除全球先例。

具体几何实现是可保存的算术例子和后续基准；但“多一个非单位参数”、
低阶显式块及标准模论后果不足以自动构成新的长篇中心定理。
全素数结构尚未证明，不能把它的潜在价值借给当前已证范围。
据此停止当前有界预筛，不写正式候选 brief、锁、稿件或试排，不通过拼装旧结果凑篇幅。

## 5. 身份、责任与接续

以下 SHA-256 于主控处置前实际重核，作者与检查字节均未变化：

| 文件简称（均在同目录） | SHA-256 |
|---|---|
| [FIRST_LAYER_PROOF](PAPER30_QPI_NONUNIT_TAU_FIRST_LAYER_PROOF_V1_20260909.md) | `ef975ded12f7263842e208f6eda87df213e210e9dbf7ef3c08fbd8724fe6270d` |
| [ALL_DEGREE_FIBRE_PROOF](PAPER30_QPI_NONUNIT_TAU_ALL_DEGREE_FIBRE_PROOF_V1_20260909.md) | `dd9cc251bed71eeca5e0063b8dd67c83d820cbedd49dcec43322001840e6b620` |
| [FIRST_AND_FIBRE_CHECK](PAPER30_QPI_NONUNIT_TAU_FIRST_AND_FIBRE_INDEPENDENT_CHECK_V1_20260909.md) | `cc21bf738c64136b6f2842a1ba60e7407208126feed6566b5ddef6802fa5f5bc` |
| [ALL_DEGREE_JET_COMPLEX](PAPER30_QPI_NONUNIT_TAU_ALL_DEGREE_JET_COMPLEX_V1_20260909.md) | `0acbfc4866b0cf944c84f88c8db3e7c535fdbff366ead4f166c3d8f01e3e2005` |
| [DEGREE3_MIXED_PROOF](PAPER30_QPI_NONUNIT_TAU_DEGREE3_MIXED_OBSTRUCTION_PROOF_V1_20260909.md) | `fe9f9f1c70b20eea4d587d57959eafd9dd8ab42cc128119c32ac6714c77470e8` |
| [JET_AND_MIXED_CHECK](PAPER30_QPI_NONUNIT_TAU_JET_AND_MIXED_INDEPENDENT_CHECK_V1_20260909.md) | `b3b68ac29e95c2db273ad83a528c131a4fdca63a94e6fb7e5abc8235eede4eb7` |
| [FIRST_PRIME_PROBE](PAPER30_QPI_NONUNIT_TAU_FIRST_PRIME_OBSTRUCTION_PROBE_V1_20260909.md) | `360741298e0a3478586031eb7ef19b18e0a36ce899b78c856cd3473c8671249a` |
| [MIXED_BLOCK_PRIOR_ART](PAPER30_QPI_NONUNIT_TAU_MIXED_BLOCK_PRIOR_ART_V1_20260909.md) | `45c998ff56bfd79f228ee7840e5de7d0a266fc0461d407387daa4553cd7c665d` |

第一份非作者报告承担 A 的两件全文，第二份承担 B/C 的两件全文及其明确必要接口。
两位此前均接触相关方向／进展，但不是被查证明的作者；不是盲审、fresh 正式四门票或跨模型认证。
主控未拼接不同构造的有利分项，全部数学接受指同一原八次吹起模型。

下一步已启动[发散报告 P03](PAPER30_QPI_POST_INTEGRAL_IDEATION_PROPOSALS_V1_20260909.md)
的有界首诊断：$p=3,a=m=1,q=1+\pi$，比较 $t=1$ 与 $t=1+\pi$，
计算原 $\alpha=(1/3)dI_3$ 在光滑超奇异小阶能级附近的真实两方向局部理想。
作者诊断与必要来源包含核查并行，仍未预设其为新候选或全参数定理。
五篇目标、原验收要求及旧失败保持；无项目、PDF、投稿、上传或其他外部效力。
