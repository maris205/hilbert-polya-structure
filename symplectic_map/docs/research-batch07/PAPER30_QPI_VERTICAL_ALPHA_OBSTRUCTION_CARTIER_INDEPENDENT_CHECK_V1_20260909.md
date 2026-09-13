# Paper30 qPI：抽象能级提升障碍—Cartier 比较引理的独立核查 V1

日期：2026-09-09。核查者：/root/p30_qpi_nonunit_tau_layer1_v1。
类型：抽象 OC1/OC2 条件引理的非作者检查，不是 qPI 实际 A3/A4 的接受。
route_applicability: NOT_APPLICABLE。0 GPU。唯一新增文件是本报告。

## Claim Under Review

核查原作者在 A1–A4 下的两项结论：

1. 原局部函数 $G_i=(I-F(j_i))/(p\pi)$ 的微分给首切向形式 $\nu$，其连接类准确为
   $$\partial\nu=\operatorname{Fr}_*(\kappa_J)
   \quad\text{in }H^1(X,\mathcal O_X^p).$$
2. $\nu$ 在完整光滑射影亏格一曲线上处处非零，并在原两状态余切模中给
   $$\mathfrak c(p^{-1}dI)_P=(\pi,\widetilde{\mathcal H(J)})
   \qquad(P\in X).$$

其中 A3 必须是实际整数 $p\pi$ 同余，A4 必须是在该完整 $X$ 上定义的非零障碍类。
不以只在剩余环中的 $\bar I=J^p$ 替代 A3。

## Status

**PASS / PROVABLE AS STATED，作为具有 A1–A4 明确前提的抽象条件引理。**

全文核查没有发现硬数学缺口。
特别是 A4 对类的定义足够，特征二的 Taylor 商有效，两个不同的 Frobenius 箭头没有混淆。
没有请求修改作者件；下文记录两处不影响逻辑的记号笔误。

该判断不说明任何实际 qPI 模型已经满足 A3 或 A4，也不由本报告预先接受其他正在撰写的桥接证明。

## Identity Disclosure and Read Scope

本核查者不是本次 OC 引理的作者。
核查前已收到主控对 Čech 思路的概要，所以这不是未接触思路的盲审；本次仍以冻结原文逐条核对推理。
本核查者曾编写旧纯四次曲线配对引理及有限端点诊断。
这些旧结果不是本次 OC 证明的前提，本报告也没有借它们证明 A3/A4 或首切向非消失。

唯一实际研究输入是：

| 输入 | 实读范围 | SHA-256 |
|---|---|---|
| [OBSTRUCTION_CARTIER_LEMMA_V1](PAPER30_QPI_VERTICAL_ALPHA_OBSTRUCTION_CARTIER_LEMMA_V1_20260909.md) | 全文 177 行；A1–A4、OC1/OC2、全部五步证明及边界 | 81ce1c934e80f0c37e425499b8e3f3f3a5b04b19d6e66efa7f9223eaab7913aa |

该哈希在本次阅读时实际核对。另完整读取 proof-writer 的技能说明。
未读取其他新审查报告、qPI 实际桥接作者件或旧配对证明；没有外部文献检索或数值计算。

## Normalized Assumptions and Dependency Map

本报告将原文记号 $\widehat{mathcal H}$ 按其明确定义读作
$$\widehat{\mathcal H}(H)=F'(H)/p=\lambda H^{p-1}+Q'(H),
\qquad \mathcal H=\overline{\widehat{\mathcal H}}.$$
这一记号整理不改变作者的函数。

- A1：$\mathcal O$ 是混合特征 DVR，$v_\pi(p)=p-1$，常数单位 $\lambda$ 满足所给剩余规范。
- 几何前提：$\mathcal U/\mathcal O$ 相对光滑二维；$X=(J=h)$ 是概形意义上的完整光滑射影几何整亏格一曲线，且 $\mathcal H(h)=0$。
- A2：$F=\lambda H^p+pQ$ 的所有系数都来自底环，状态微分不作用于它们。
- A3：所选正则提升 $j_i$ 满足实际函数整除 $I-F(j_i)\in(p\pi)$。
- A4：$f_{ij}=\overline{(j_j-j_i)/\pi}|_X$ 的类在实际 $H^1(X,\mathcal O_X)$ 中非零。

依赖顺序为：A1/A2 的整数 Taylor 商、A3 的正则 $G_i$、A4 的精确连接类、
完美光滑曲线的函数层核、最后亏格一与两状态局部消元。
没有一步需要谱四次配对或把一个未证 qPI 同余当作已知。

## Itemized Conclusions

| 检验项 | 结论 |
|---|---|
| A1/A2 保证 Taylor 商整数性及 $p$ 次项的单位规范 | PASS |
| $p=2$、$v_\pi(2)=1$ 时先整数除法、后模 $\pi$ | PASS；不要求二阶商为特征二 |
| A4 的余差、三重交叠、覆盖细化与局部提升不变性 | PASS |
| $\bar G_j-\bar G_i$ 的符号及 $X$ 上 $+f_{ij}^p$ | PASS |
| $\nu$ 是原 $\alpha=p^{-1}dI$ 的首切向类 | PASS |
| $\ker(d:\mathcal O_X\to\Omega^1_X)=\mathcal O_X^p$ 的函数层证明 | PASS |
| $\operatorname{Fr}:\mathcal O_X\to\mathcal O_X^p$ 与后续包含映射的区别 | PASS |
| $\partial\nu=\operatorname{Fr}_*\kappa_J\ne0$ | PASS |
| 射影亏格一上的处处非零及全部实际局部点的两系数理想 | PASS |
| qPI 实际 A3/A4 | NOT REVIEWED；不在本报告接受范围 |

## Detailed Audit

### 1. A4 定义的是充分且规范的普通函数层类

在 $U_i\cap U_j$ 上，$j_i,j_j$ 都提升同一个全局剩余函数 $J$。
因此 $j_j-j_i$ 落在 $\pi\mathcal O_{\mathcal U}$ 中。
相对光滑蕴含 $\mathcal O$-平坦，$\pi$ 不是零因子，故除以 $\pi$ 的正则函数唯一；
这不是在函数域中任取一个商后猜测其正则性。

对任一三重交叠，除法前已有
$$(j_k-j_j)+(j_j-j_i)-(j_k-j_i)=0.$$
唯一除以 $\pi$、约化并限制到 $X$ 后，得到
$$f_{jk}+f_{ij}-f_{ik}=0.$$
所以确实是普通加法层 $\mathcal O_X$ 的 Čech 一上闭链，不需要未写出的线丛转移函数。
抽象设定中的 $j_i$ 是函数，这一点与实际应用可能先从线丛截面构造提升的责任不同。

若改为 $j_i+\pi a_i$，新余差为
$$f_{ij}+\bar a_j|_X-\bar a_i|_X,$$
只改变一个余边界。覆盖细化保留同一层上同调类。
可以选取 $\mathcal U$ 中覆盖 $X$ 的仿射邻域并细化；其与 $X$ 的交是仿射，
$X$ 分离保证这些仿射开集的有限交仍仿射，从而 Čech 计算拟凝聚层 $\mathcal O_X$ 的上同调。
即使先使用任意覆盖，也可将所给闭链映到层上同调再细化。

因此 A4 已经明确规定了需要的目标空间、代表和非零性。
它不需要额外假设一个环境 $H^1$ 类的限制自动非零；如果实际 qPI 应用从别处产生该类，那正是应用必须另证的部分。

### 2. 整数 Taylor 除法覆盖特征二

在任意 $\mathcal O$-平坦交换代数中，$F(a+\pi f)-F(a)$ 的二项式展开先在整数环进行。
对 $1\le r<p$，
$$\frac{\binom pr\pi^r}{p\pi}
=\frac1p\binom pr\,\pi^{r-1}$$
是整数系数；其中 $r\ge2$ 的项模 $\pi$ 为零。
$r=p$ 的系数是 $\lambda\pi^{p-1}/p$，由 A1 是单位且剩余为 $-1$。
另有
$$\frac{p(Q(a+\pi f)-Q(a))}{p\pi}
=Q'(a)f+\pi(\text{正则函数}).$$
所以完整剩余商是
$$\overline{\frac{F(a+\pi f)-F(a)}{p\pi}}
=\mathcal H(\bar a)\bar f-\bar f^p.$$

当 $p=2$ 时中间二项式区间为空，$r=1$ 与 $r=2$ 分别贡献
$\lambda\bar a\,\bar f$ 和 $\overline{\lambda\pi/2}\,\bar f^2$；
同一 A1 正好给后者所需规范。
没有一步先将 $2$ 置零后再除以它，也没有使用 $\mathcal O/(\pi^2)$ 的双数环同构。
因此特征四的二阶商不是此证明的障碍。

此外，该 Taylor 整除式说明若一组 $j_i$ 满足 A3，则任何 $j_i+\pi a_i$ 仍满足 A3。
所以后续对局部提升任意改变的论证确实留在假设范围内。

### 3. 粘合符号、原首切向身份与提升不变

A3 及平坦性给唯一正则 $G_i$，且在原相对微分模中
$$\alpha=\widehat{\mathcal H}(j_i)dj_i+\pi dG_i.$$
相对微分模局部自由，故这一正则表达式在泛纤维相等后于重叠上相等，给真正整的 $\alpha$。

按 $j_j=j_i+\pi\widetilde f_{ij}$ 及作者规定的 Čech 符号，
$$G_j-G_i=-\frac{F(j_j)-F(j_i)}{p\pi}.$$
所以约化后的余差是
$$-\mathcal H(J)\bar{\widetilde f}_{ij}
+\bar{\widetilde f}_{ij}^{\,p}.$$
限制到 $\mathcal H(J)|_X=\mathcal H(h)=0$ 后正是 $+f_{ij}^p$。
连接类中的正号因此准确，不是靠忽略常数单位得到。

在 $X$ 上求微分，$d(f_{ij}^p)=0$，所以 $d(\bar G_i|_X)$ 粘合成正则形式。
它逐图也是
$$\left[\overline{\frac{\alpha-\widehat{\mathcal H}(j_i)dj_i}{\pi}}\Big|_X\right]
\quad\text{in }\Omega^1_{U_0/k}|_X/\mathcal O_XdJ=\Omega^1_{X/k}.$$
这确认了与原两状态整除微分首切向类的身份，没有另外挑选一条局部恰当形式。
若改变 $j_i$，$G_i$ 在 $X$ 上的改变量为一个 $p$ 次幂，其微分为零；故 $\nu$ 本身也不变。

### 4. 函数域核确实下降为正则函数层核

光滑曲线的函数域 $K$ 具有分离超越变量 $z$；设 $[K:k(z)]=n$。
完美 $k$ 使 Frobenius 把该扩张同构到 $K^p/k(z^p)$，因此
$$[K^p:k(z^p)]=n,\qquad[K:k(z^p)]=pn,\qquad[K:K^p]=p.$$
因 $dz\ne0$，$z\notin K^p$，所以 $1,z,\ldots,z^{p-1}$ 是相对于 $K^p$ 的基。
按此基展开后逐项微分，指数 $1,\ldots,p-1$ 的系数可逆，准确得到函数域核 $K^p$。

若一个开集上的正则函数 $g$ 满足 $dg=0$，则 $g=a^p$，$a\in K$。
在该开集每个闭点的局部 DVR 中，
$$p\,v_P(a)=v_P(g)\ge0.$$
所以 $a$ 无极点；光滑曲线正规，故 $a$ 在该开集上正则。
因此这里得到的是 $\ker d=\mathcal O_X^p$ 的层等式，而不只在泛点成立。
唯一性还保证局部 $p$ 次根在重叠上自动粘合。

### 5. 连接类的目标没有被偷偷换成 $H^1(\mathcal O_X)$

$\mathcal O_X^p$ 和 $B_X^1$ 在该短正合列中首先作为加法层解释；
不要求它们按原乘法成为 $\mathcal O_X$-子模。
完美 $k$ 保证 $\mathcal O_X^p$ 对常数数乘封闭，Frobenius 按该常数作用为半线性。
因为 $X$ 约化，$f\mapsto f^p$ 单射；按像层定义及唯一根粘合，它是
$$\operatorname{Fr}:\mathcal O_X\xrightarrow{\sim}\mathcal O_X^p$$
的加法层同构。因而它在层上同调上给加法群同构。
同一仿射覆盖也可用于此像层的 Čech 计算，因为它作为加法层与 $\mathcal O_X$ 同构。

局部原函数 $\bar G_i|_X$ 的余差已经确认为 $f_{ij}^p$，所以
$$\partial\nu=[(f_{ij}^p)]
=\operatorname{Fr}_*[(f_{ij})]=\operatorname{Fr}_*(\kappa_J)\ne0.$$
非零性直接来自 A4 和这一个层同构，所以 $\nu\ne0$。

另一方面，连接列精确性恰迫使该类在随后映射
$$H^1(X,\mathcal O_X^p)\longrightarrow H^1(X,\mathcal O_X)$$
下为零。这并不与前一箭头可逆矛盾。
虽然函数层包含映射是单射，它诱导的 $H^1$ 映射未必单射；
作者没有声称超奇异情形下通常的 $H^1(\mathcal O_X)$ Frobenius 可逆。
这是该证明能成立的关键区分，原文保留得准确。

### 6. 亏格一及原两系数理想

在光滑射影几何整亏格一曲线上，$\deg\Omega^1_X=0$。
非零正则一形式的零除子有效，故不能有正次数的零点；于是 $\nu$ 处处非零。
不需要 $X$ 具有一个预先选定的 $k$-有理点。

这里 $X$ 是光滑的概形纤维而不只是奇异或非约化纤维的光滑支撑，故环境法向 $dJ$ 非零。
在任一点的原局部自由秩二模中，$dj_i$ 因而可补为一组基。
将 $dG_i=A\,dj_i+B\theta$ 代入，得到
$$\alpha=(\widehat{\mathcal H}(j_i)+\pi A)dj_i+\pi B\theta.$$
$\nu$ 在该点非零说明 $B$ 是实际局部单位，所以
$$\mathfrak c(\alpha)_P
=(\widehat{\mathcal H}(j_i)+\pi A,\pi B)
=(\pi,\widehat{\mathcal H}(j_i)).$$
任意别的 $\mathcal H(J)$ 提升只改变一个 $\pi$ 倍数，右端理想不变。
该局部证明对非闭点同样适用，也不要求 $\mathcal H$ 在 $h$ 是简单根。
没有把向一维曲线的微分拉回当作完整双系数理想。

## Nonblocking Editorial Notes

原文有两处可识别的记号笔误，后续如另行版本修订时可整理；本次未改作者文件：

1. $\widehat{mathcal H}$ 和 $\widetilde{mathcal H(J)}$ 中的文字 mathcal 应排成 $\mathcal H$。
2. Step 2 式 (3) 的 $\bar{\widetilde f}_{ij}^{,p}$ 应读作 $\bar{\widetilde f}_{ij}^{\,p}$。

定义、紧随的函数等式和 OC1 的证明已经唯一确定这些符号的含义，所以它们不构成结论的硬缺口。

## Remaining Responsibilities and Handoff

- A3 的模数为 $p\pi=\text{unit}\cdot\pi^p$。仅有 $\bar I=J^p$ 通常只给模 $\pi$ 信息，不能产生这里正则的 $G_i$ 或单位系数的 $p$ 次余差。
- A4 必须在该完整 $X$ 的 $H^1(\mathcal O_X)$ 中实际非零；环境空间、其他线丛或其他模型上的非零类不能未经限制映射证明就替代它。
- 因而本报告不接受 qPI 实际 A3/A4；这些应用责任需要各自作者证明及对应非作者检查。
- 没有借用旧纯配对结果或任何尚未核准的桥接路线；没有把条件引理扩大成全 $p,m$ 的 qPI 定理。
- 本次只有读原文和逐步数学核查，不需要额外文献、计算或脚本；没有读取其他新审查，作者件保持冻结。

**终态结论：抽象 OC1/OC2 在 A1–A4 下通过；实际 qPI 前提未由本报告代签。**
