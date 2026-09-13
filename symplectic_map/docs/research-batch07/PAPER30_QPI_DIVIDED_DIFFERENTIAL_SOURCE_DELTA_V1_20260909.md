# Paper30 qPI：整除微分与 Hasse 迭代的来源差分 V1

日期：2026-09-09。执行者：独立来源核查代理 p30_qpi_cyclotomic_prior_art_v1。
类型：有界来源比较；不是 D1–D3 非作者证明审查、新意评分或正式票。
本件只追加准确整除微分的来源边界，不修改先前 178 行圆分／q-curvature 报告。

## 1. 对象、实读范围与结论

完整读取了 [作者诊断 V1](PAPER30_QPI_CYCLOTOMIC_DIFFERENTIAL_DIAGNOSTIC_V1_20260909.md)，
尤其 D1–D3、证明 Steps 1–7 及第 5–6 节限制。
固定 $N=p^a$、$r=mN$、$p\nmid m$；$d$ 是固定 $t,s$ 的状态微分。
准确比较对象是
$$p^{-a}dI_{mp^a}\in\Omega,\qquad
\overline{p^{-a}dI_{mp^a}}
=H_p(T,J;\varepsilon)^{1+p+\cdots+p^{a-1}}dJ,$$
以及全体 Laurent 系数的最小圆分 DVR 赋值 $a\,v_\pi(p)$。
约化后的 $d(J^{p^a})=0$ 不是上述先除后约化对象。

核心结论：**Hasse 次幂乘子不仅与一般 Cartier 机制相似，它可直接识别为
Vlasenko 既有定理中的秩一 higher Hasse–Witt 系数。**
第 3 节给出这个识别所需的全部代数桥接，明确它是本次比较推断而非源文中的 qPI 定理。
现成系数定理并不自动证明原圆分积分的整性、循环插入识别或准确全局赋值。
但作者证明里的这些桥接也以一般循环矩阵积与既有 JR 规范输入为基础；
本轮没有发现额外的 qPI 专属一般机制。
未找到逐字同式的 qPI 先例，不构成新意证明。

## 2. 新检索边界与实际读取的来源

使用 research-lit 的来源分级和原文定位；按本次明确范围跳过默认 API 客户端、
本地 PDF 库扫描、下载与完整研究流水线。新增定向 search query 恰为 6 个：

1. Dickson polynomial derivative first kind second kind n characteristic p trace matrix
2. Dwork congruences constant terms Hasse Witt matrices Laurent polynomials p power Vlasenko
3. cyclotomic norm divided differential de Rham Witt trace Cartier
4. "de Rham-Witt" "ghost" "differential" Hesselholt trace
5. "q-Painlevé" "Hasse" differential
6. "Dickson" "derivative" "second kind" polynomials

后续仅打开这些结果及其准确文献链接，没有继续 q-curvature 同义搜索。
未以搜索摘要代替以下已注明的原文段落；未声称通读任何外部论文。

| 来源／版本与状态 | 实际读取 | 支持与不支持 |
|---|---|---|
| M. Vlasenko, *Higher Hasse–Witt matrices*, arXiv:1605.06440v3，2018-04-17；作者页另给期刊 DOI 10.1016/j.indag.2018.07.004 | §1 的定义 (1)–(4)、Theorem 1(i)–(iii)、半线性解释；§3 Lemma 7 及证明 | 系数序列的模 $p$ Frobenius 乘积；第 3 节将其直接用于本谱多项式。不是原圆分 $I_r$ 的定理。[作者原文](https://arxiv.org/html/1605.06440v3) |
| J. D. Achter–E. W. Howe, *Hasse–Witt and Cartier–Manin matrices: A warning and a request*, Contemp. Math. 722 (2019), 1–18；实读订正版 v5，2020-02-07 | §§1.2、2.2、2.4–2.5、3.1、3.3 | 一次与迭代 Cartier 的系数公式、正反 Frobenius 半线性规范；奇特征四次亏格一直接适用。v5 修正了已发表版 §2.5 的错误。[订正版原文](https://arxiv.org/html/1710.10726v5) |
| A. Mellit–M. Vlasenko, *Dwork's congruences for the constant terms of powers of a Laurent polynomial*, arXiv:1306.5811v1，2013-06-24；此处只按实读预印本使用 | §1 Theorem 1 及其数字展开推论 | 唯一内部整点条件下的常数项同余；不把原 $I_r$ 序列自动变成其常数项序列。[作者原文](https://arxiv.org/html/1306.5811v1) |
| L. Hesselholt–I. Madsen, *On the de Rham–Witt complex in mixed characteristic*；实读作者 final PDF，本轮未另核出版年／卷页 | 引言、§1.1 ghost 多项式与 Dwork 判据、§1.2 Lemma 1.2.1 | Witt 微分的除 $p$ 机制；未构造 qPI 的 Witt lift。该文所读框架取奇素数。[作者 PDF](https://web.math.ku.dk/~larsh/papers/013/final.pdf) |
| J.-C. Pain, *A derivation of Dickson polynomials using the Cayley–Hamilton theorem*, arXiv:2406.07322v2，2024-06-13；预印本 | 引言及 §2 的 Dickson 递推、Cayley–Hamilton／低次矩阵迹展开 | 一般秩二迹幂属于 Dickson 结构；所读处没有本题完整整除导数式。[作者原文](https://arxiv.org/html/2406.07322v2) |

Achter–Howe §3.3 指向 Garcia–Tafazolian, *Certain maximal curves and Cartier operators*,
Acta Arith. 135(3) (2008), 199–218，p.212；该原论文链接未成功打开。
因此这里只报告 Achter–Howe 对该结果的明确表述，不冒称已读 Garcia–Tafazolian 原文。
Mellit–Vlasenko HTML 的自动 Date 字段显示 2026，但 arXiv 提交记录明确是 2013；
未将其误当作 2026 新结果。

## 3. 最强直接包含：谱多项式的秩一 higher Hasse–Witt 系数

以下是**本报告的透明代数识别**，用于比较来源覆盖，不替代 D1–D3 的独立检查。
在通用环 $R=\mathbb Z[T,h]$ 固定 $\varepsilon=\pm1$，令
$$F(Z,\lambda)=\lambda^2-(T+hZ+Z^2)\lambda+\varepsilon Z^3.$$
其 Newton 多边形顶点为
$$(0,1),(3,0),(2,1),(0,2),$$
面积为 2，边界整点数为 4，唯一内部整点是 $(1,1)$。
因此 [Vlasenko §1 定义 (2)](https://arxiv.org/html/1605.06440v3) 的矩阵是秩一标量
$$G_a(T,h):=[Z^{N-1}\lambda^{N-1}]F(Z,\lambda)^{N-1},
\qquad N=p^a.$$

为与作者诊断式 (7) 对齐，先在 $\mathbb F_p[S,D]$ 中看
$P(\lambda)=\lambda^2-S\lambda+D$。
局部化使 $D$ 可逆后，
$$P(\lambda)^{-1}=\sum_{k\ge0}U_k(S,D)D^{-k-1}\lambda^k.$$
又有 $P(\lambda)^N=\lambda^{2N}-S^N\lambda^N+D^N$。
比较 $P^{N-1}=P^N/P$ 的 $\lambda^{N-1}$ 系数得到
$$[\lambda^{N-1}]P(\lambda)^{N-1}=U_{N-1}(S,D). \tag{A}$$
两边都是未局部化环中的多项式，故 (A) 下降为通用模 $p$ 恒等式。
代入 $S=T+hZ+Z^2$、$D=\varepsilon Z^3$ 可得
$$\overline{G_a}
=[Z^{N-1}]U_{N-1}(T+hZ+Z^2,\varepsilon Z^3). \tag{B}$$
尤其 $\overline{G_1}=H_p(T,h;\varepsilon)$，包括 $p=2$ 的 $H_2=h$。

在 $R$ 上取 $\sigma(T)=T^p,\ \sigma(h)=h^p$，整数不动。
[Vlasenko Theorem 1(i)](https://arxiv.org/html/1605.06440v3) 直接给出
$$G_a\equiv G_1\,\sigma(G_1)\cdots\sigma^{a-1}(G_1)\pmod p,$$
故
$$\overline{G_a}=H_p(T,h;\varepsilon)^{1+p+\cdots+p^{a-1}}. \tag{C}$$
该部分不要求 $G_1$ 可逆，也不要求谱曲线光滑；先在通用参数环成立再特化，
不因某次特化改变实际支集而丢失多项式恒等式。

所以作者诊断式 (7) 已经接到 (B) 后，其式 (1) 的整个乘子就是 (C)。
这一覆盖强于“半线性指数看起来相同”，但准确未覆盖部分仍是
$$\overline{p^{-a}dI_{mp^a}}
\stackrel{\text{原循环积识别}}{=}\overline{G_a}(T,J)\,dJ.$$
Vlasenko 没有在所读原文中讨论这个 qPI 圆分积分，也未替本题建立该箭头。

## 4. 其余一般机制的扣除与适用限制

### 4.1. 矩阵迹导数

秩二的迹幂递推是 Dickson／Cayley–Hamilton 结构。
作者诊断的
$$\operatorname{tr}(B^{N-1}dB)
=U_{N-1}(S,D)dS-U_{N-2}(S,D)dD$$
属于该一般代数框架，不依赖具体 qPI 的矩阵条目。
这是对作者 Step 4 的分类，不是声称 Pain 已写了该微分恒等式。
Pain HTML 的部分闭式排版出现可疑的二项式位置，故未拿那些闭式替代核准，
只用其明确的递推和 Cayley–Hamilton 说明背景归属。

同样，$dI_r=r[z^r]Q_r$ 的循环插入论证只用乘积规则、迹循环性、
$s^r=1$ 及选定 $z^r$ 系数；这些是一般循环矩阵积操作。
本次未定位到一篇原文逐字陈述该完整 qPI 桥接引理，
故“它是一般操作”与“已找到完全相同发表定理”须严格分开。

### 4.2. Cartier 的系数及指数

对光滑奇特征四次 $Y^2=f(Z)$，Achter–Howe §3.1 给出
$\mathcal C(dZ/Y)=([Z^{p-1}]f^{(p-1)/2})^{1/p}dZ/Y$ 的亏格一情形。
其 §3.3 明确记录 $a$ 次 Cartier 使用
$[Z^{p^a-1}]f^{(p^a-1)/2}$ 的 $p^a$ 次根；
结合逆 Frobenius 半线性，所得系数恰是 $H_p^{(1+p+\cdots+p^{a-1})/p^a}$。
这是现成几何解释，不是另一个独立 qPI 指数发现。
这份超椭圆公式限定奇特征；特征二仍须用诊断的残差微分／局部 Cartier 规则，
不能把 $Y=2\lambda-S$ 的奇特征换元照搬过去。
相关规范以 [Achter–Howe 订正版 §§2.2、2.4、3.1、3.3](https://arxiv.org/html/1710.10726v5) 为准。

### 4.3. Dwork 与 de Rham–Witt 不自动补全高阶退化

将 $F$ 平移为 Laurent 多项式 $\Lambda=F/(Z\lambda)$ 后，
$G_a=[\Lambda^{p^a-1}]_0$；其 Newton 多边形的唯一内部整点是原点。
这解释了与 Mellit–Vlasenko 常数项机制的准确接点。
但该文 Theorem 1 的已读陈述取 $\mathbb Z_p$ 系数；
保留通用参数及 Frobenius 扭曲时，第 3 节已读的 Vlasenko 版本更直接。
不能跳过圆分积分识别，直接给 $I_r$ 加上 Dwork 高阶同余。
[Mellit–Vlasenko §1](https://arxiv.org/html/1306.5811v1)

Hesselholt–Madsen 的 ghost 多项式为
$w_a=\sum_{i=0}^a p^i a_i^{p^{a-i}}$，故形式求微分产生统一因子 $p^a$；
其 Lemma 1.2.1 另给 $dF=pFd$。
这说明“Frobenius 后微分需先除 $p^a$”本身有成熟的一般背景。
但原 $I_{mp^a}$ 尚未被识别为一个兼容 Witt 向量的 ghost 序列；
缺少 lift／兼容同余时，这个类比既不能证明本题整性，也不能推出 Hasse 因子。
所读文中的拓扑 cyclotomic trace 亦不是本题谱矩阵的普通迹。
[Hesselholt–Madsen §§1.1–1.2](https://web.math.ku.dk/~larsh/papers/013/final.pdf)

Vlasenko Theorem 1(ii)–(iii) 的逆矩阵同余与导数极限要求 $\overline{G_1}$ 可逆，
不能拿来宣布已解决 $H_p=0$ 的超奇异层下一阶。
该文 Lemma 7 的导数除 $p^a$ 还要求指定 Frobenius lift；
它不将本题分歧圆分 DVR 或 $I_r$ 自动识别为那个 lift 的迭代。

## 5. 对作者 D1–D3 的覆盖账目与真正剩余

| 作者内容 | 本轮来源判断 | 仍需保留的 qPI 实例工作 |
|---|---|---|
| D1：$\overline I_r=J^N$ | 重复块、矩阵迹 Frobenius 的一般结果；诊断已主动不主张新意 | 固定 JR 迹规范下的系数识别 |
| D2：特征零整性与先除后约化 | 循环插入／长度 $m$ 分组是一般矩阵积操作；未找到逐字同式 qPI 来源 | 核准原排序、谱参数旋转、投影与 $p^{-a}$ 的准确对应 |
| D2：$H_p^{(N-1)/(p-1)}$ 乘子 | 第 3 节识别后，直接落在 Vlasenko Theorem 1(i) 内 | 不再把该指数或系数因式分解单列为新一般定理 |
| D2：最小 Laurent 系数赋值 $a\,v_\pi(p)$ | 来源系数定理不给这条原积分全局锐性；诊断用 JR 首项与 $H_p$ 首一性推出 | qPI 实例的非零首项及所用赋值口径 |
| D3：系数理想、Hasse 拉回重数 | 理想乘积是 D2 的代数推论；光滑层 Cartier／Hasse 解释是现成几何 | 消费已核准的原能级光滑性；不能把奇异层也称为超奇异 |

本次真正未由外部原文直接点名覆盖的是：在 JR 固定正规化中，
把原 $I_{mp^a}$ 的整除状态微分接到既有谱曲线 Hasse–Witt 系数，
并给出准确统一系数赋值。它们可以是有价值的实例识别，
但当前没有来源证据支持将其升级为脱离一般矩阵／Cartier 机制的新理论。
这与 D1–D3 是否正确是两个问题；非作者数学检查仍由单独任务负责。

本件未证明下一阶圆分 jet、超奇异提升点赋值、完整稳定约化或野导子，
也未据普通层的可逆矩阵定理外推这些结果。
不改旧入口、作者诊断、已接受 T1–T7 或旧来源报告；不创建 V3、不重开两票、不打分。
查新结果是具体的一般机制扣除，不是“未检出即新”，也不是“有标准工具即完全无实例价值”。
