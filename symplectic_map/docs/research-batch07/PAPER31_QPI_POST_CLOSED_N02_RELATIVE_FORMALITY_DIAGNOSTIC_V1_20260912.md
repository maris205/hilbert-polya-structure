# Paper31／N02：原自治相对导出代数的信息限界——短证明 V1

日期：2026-09-12；作者：`/root`。
状态：`AUTHOR_PROOF_COMPLETE / INDEPENDENT_CHECK_PENDING / N01_SUBCHECK_ONLY`。
`route_applicability: NOT_APPLICABLE`。按[事前选择][SEL]执行；不是独立选题、正式四门或论文准入。

## 1. Claim：运算前对象卡与准确命题

固定代数闭特征零域 $k$，自治参数 $q=1$，单位时间 $t\in k^\times$；不把 $t=0$、正特征或整数圆分加厚包含在本命题。
$S_t$ 是[P30原曲面][G]的同一八次吹起，$D_t=-K_{S_t}$，$L_{t,n}=\mathcal O_{S_t}(nD_t)$。
标记原两个截面
$$
s_{0,t}=xy,\qquad s_{1,t}=x^2-x^2y+xy^2-ty,
\qquad h=\frac{s_{1,t}}{s_{0,t}}=\frac{x}{y}-x+y-\frac t x.
$$
这两个多项式表示原线丛截面，不是把它们当作完整射影曲面上的正则函数。
在 $\mathcal O(D_t)$ 的有理截面表示下，同一对为 $1,I_{1,1}$；除以 $xy$ 正是两种平凡化之间的字典。
令 $B=\mathbb P^1_k$ 带固定齐次坐标 $[a:b]$，$h=b/a$，$f_t=[s_{0,t}:s_{1,t}]:S_t\to B$。
取
$$
\mathcal E_t=Rf_{t*}\mathcal O_{S_t}\in\operatorname{CAlg}(D_{\rm qc}(B)),
\qquad
\mathcal A_t=\bigoplus_{n\ge0}R\Gamma(S_t,L_{t,n}),
$$
其中 $\mathcal A_t$ 保留原分次、单位、截面乘法、标记 $s_{0,t},s_{1,t}$ 以及乘 $s_{0,t}$ 的原极阶包含。
这里的 $\operatorname{CAlg}$ 指标准导出对称张量结构中的 $E_\infty$ 代数；忘却到 $E_1$ 亦可。移位约定 $M[-1]$ 的唯一上同调在次数一。

**命题。** 对每个上述 $t$，有非规范的 $\mathcal O_B$-代数等价
$$
\mathcal E_t\simeq\mathcal O_B\oplus\mathcal O_B(-1)[-1],
\qquad \mathcal O_B(-1)[-1]\cdot\mathcal O_B(-1)[-1]=0. \tag{1}
$$
由同一个相对等价导出保分次、单位、两原截面与极阶包含的 $E_\infty$ 等价
$$
\mathcal A_t\simeq k[a,b]\oplus\xi k[a,b],\qquad
\xi^2=0,\quad d=0,\quad
\operatorname{wt}(a)=\operatorname{wt}(b)=\operatorname{wt}(\xi)=1,
\quad |a|=|b|=0,\ |\xi|=1. \tag{2}
$$
故任意 $t_1,t_2\in k^\times$ 的两个上述标记代数等价。另一方面，事先固定 $t_1=1,t_2=2$，其原泛能级 Jacobian 的 $j$ 函数在固定能量标签 $h$ 下不同。
这给原族内部的信息碰撞，不声称所有几何增强均失明。

## 2. Status、Assumptions 与依赖图

证明分诊：`PROVABLE AS STATED`，当前为作者判断，独立审查尚待执行。
本件消费已接受的原曲面和平坦铅笔，不重开它们：$S_t$ 光滑射影且为 $\mathbb P^1\times\mathbb P^1$ 的八次吹起，$D_t=-K_{S_t}$；自治完整系统 $|D_t|$ 无基点，$f_t$ 射影平坦且 $f_t^{-1}(\infty)=D_t$。
原接受亦给 $H^1(S_t,\mathcal O)=H^2(S_t,\mathcal O)=0$。这些正是[G] Proposition `geom:surface` 与 Theorem `geom:pencil` 的 $r=1$ 情形。
不另假设每个有限纤维光滑、不可约或有点；下一步的全纤维上同调直接从 Cartier 除子序列导出。

策略／依赖：原完整铅笔及有理曲面消失 $\Rightarrow$ 全纤维上同调 $\Rightarrow$ $Rf_*\mathcal O$ 的单位余锥为移位线丛 $\Rightarrow$ 加法分裂 $\Rightarrow$ **自由奇线代数**给真正乘法等价 $\Rightarrow$ 原全分次标记模型；另用已接受[原泛 Jacobian][J]检验时间模参数仍变化。
用到的标准工具为光滑射影曲面 Serre 对偶、proper flat 导出基变换、$\mathbb P^1$ 线丛上同调及自由交换代数泛性质；各适用点如下，不以 $\operatorname{Ext}^2=0$ 单独代替乘法论证。

## 3. Proof

### Step 1. 全部原纤维的上同调与线丛标记

任取 $z\in B(k)$，$G=f_t^{-1}(z)$ 为完整 Cartier 纤维，$G\sim D_t$。从
$$
0\longrightarrow\mathcal O_{S_t}(-G)\longrightarrow
\mathcal O_{S_t}\longrightarrow\mathcal O_G\longrightarrow0
$$
及 $\mathcal O(-G)\simeq\omega_{S_t}$，Serre 对偶给
$$
H^0(\omega_{S_t})=0,\quad H^1(\omega_{S_t})=0,
\quad H^2(\omega_{S_t})=k.
$$
长正合列因此给常数映射 $k\xrightarrow\sim H^0(G,\mathcal O_G)$ 和 $H^1(G,\mathcal O_G)\simeq k$，其余上同调为零。
该论证也覆盖 $G=D_t$ 以及任何奇异、非约化纤维；没有用仅平滑纤维的上同调去推全底。
完整无基点的标记二截面给
$$
f_t^*\mathcal O_B(1)\xrightarrow\sim L_{t,1},\qquad
a\longmapsto s_{0,t},\quad b\longmapsto s_{1,t}.
$$
张量幂给所有 $n\ge0$ 的兼容识别 $f_t^*\mathcal O_B(n)\simeq L_{t,n}$，包括次数零。

### Step 2. 相对单位余锥确实为一条移位线丛

$f_t$ 为 proper、flat、finite presentation 且 $\mathcal O_{S_t}$ perfect，故 $\mathcal E_t$ perfect，导出拉回到任意底点等于该纤维的导出函数。
这是[Stacks Lemma 36.30.4](https://stacks.math.columbia.edu/tag/0A1G)的直接适用；Noetherian仿射底版本及证明亦见[30.22.1](https://stacks.math.columbia.edu/tag/07VJ)。
令 $C_t$ 为单位 $\mathcal O_B\to\mathcal E_t$ 的余锥。Step 1说明 $C_t\otimes^{\mathbf L}k(z)\simeq k(z)[-1]$；相同计算在域扩张后成立，亦适用于泛点。
perfect 复形在各局部环可表示为有限自由复形，并消去微分中所有单位矩阵项；剩下的最小复形模极大理想后微分为零。
其剩余域上同调只在次数一且维数一，故最小复形只有次数一的一个自由项。于是 $C_t$ 在每点邻域为秩一线丛移到次数一，粘成
$$
C_t\simeq\mathcal L_t[-1],\qquad
\mathcal H^0(\mathcal E_t)=\mathcal O_B,\quad
\mathcal H^1(\mathcal E_t)=\mathcal L_t.
$$
Leray 的 Euler 特征等式给
$$
1=\chi(S_t,\mathcal O)=\chi(B,\mathcal O_B)-\chi(B,\mathcal L_t)
=1-\chi(B,\mathcal L_t).
$$
每条 $B=\mathbb P^1_k$ 上的线丛为 $\mathcal O_B(d)$ 且 Euler 特征为 $d+1$，所以 $\mathcal L_t\simeq\mathcal O_B(-1)$。

### Step 3. 先取加法分裂，再证明它延伸为代数等价

单位三角为
$$
\mathcal O_B\longrightarrow\mathcal E_t\longrightarrow
\mathcal L_t[-1]\xrightarrow{\delta}\mathcal O_B[1].
$$
$\delta$ 属于 $\operatorname{Ext}^2_B(\mathcal L_t,\mathcal O_B)=H^2(B,\mathcal L_t^\vee)=0$。
故存在导出模映射 $\eta:\mathcal L_t[-1]\to\mathcal E_t$，使它与商映射的复合为恒等。
截至此处只获得模分裂，尚未获得代数形式性。

在 $\mathbb Q$-线性的导出对称张量范畴 $D_{\rm qc}(B)$ 中，自由交换代数的底层对象为 $\bigoplus_{m\ge0}(M^{\otimes m})_{h\mathfrak S_m}$。
取 $M=\mathcal L_t[-1]$。因为所有 $m!$ 可逆，有限群的同伦余不变量由平均投影计算，无额外高群同调；又因 $M$ 是移位奇线，一个换位对 $M^{\otimes m}$ 作用为 $-1$。
当 $m\ge2$ 时，余不变量中同一元素等于其负，且二可逆，故该整个对称幂为零。于是
$$
\operatorname{Sym}_{\mathcal O_B}(\mathcal L_t[-1])
\simeq\mathcal O_B\oplus\mathcal L_t[-1]
$$
为平方零的 $E_\infty$ 代数。
自由代数泛性质将原 $\eta$ 延伸为唯一对应的代数映射（映射空间意义）
$$
\operatorname{Sym}_{\mathcal O_B}(\mathcal L_t[-1])
\longrightarrow\mathcal E_t.
$$
它在 $\mathcal H^0$ 上是单位同构，在 $\mathcal H^1$ 上是 $\eta$ 所给同构；两边其余上同调均零，因而为代数等价。这证明(1)。
自由代数的上述存在与底层对称幂公式使用[Lurie, Higher Algebra, Proposition 3.1.3.13／Example 3.1.3.14，印刷页346](https://www.math.ias.edu/~lurie/papers/HA.pdf)；此处范畴有可数余极限且张量保余极限，故条件满足。奇线消失计算已在本文展开，不从单椭圆形式性引用相对结论。

### Step 4. 一次性得到全分次代数，并保留原标记

Step 1的张量幂识别及投影公式在所有权上一致给
$$
Rf_{t*}L_{t,n}\simeq\mathcal O_B(n)\otimes^{\mathbf L}\mathcal E_t.
$$
它们与截面乘法兼容：两项的线丛因子按 $\mathcal O(m)\otimes\mathcal O(n)=\mathcal O(m+n)$ 相乘，导出函数因子使用 $\mathcal E_t$ 的同一乘法。
故把(1)张量上述分次线丛代数，再取导出全局截面，给原全分次代数的模型
$$
\bigoplus_{n\ge0}R\Gamma\bigl(B,
\mathcal O_B(n)\oplus\mathcal O_B(n-1)[-1]\bigr). \tag{3}
$$
所有 $n\ge0$ 中，$\mathcal O_B(n)$ 与 $\mathcal O_B(n-1)$ 的高阶全局上同调皆零；$n=0$ 时 $\mathcal O_B(-1)$ 的零阶上同调也为零。
因此从这些零微分平方零 sheaf 代数的普通全局截面到导出全局截面的自然乘法映射为逐权准同构。
$\bigoplus_{n\ge0}H^0(\mathcal O(n))=k[a,b]$，而 $H^0(\mathcal O(n-1))$ 为权 $n$ 的 $\xi k[a,b]$，$\xi$ 权一、上同调次数一。这正是(2)。
偶部映射来自相对单位，故严格在所标记的截面类上送 $a,b$ 到 $s_{0,t},s_{1,t}$；乘 $a$ 也就是原极阶包含。
奇线的识别及分裂不规范，但存在性足以给任意两时间的保原二标记等价。没有选择或要求一个额外规范的 $H^1$ 生成元。

### Step 5. 同一原族的模参数并未恒定

[J]在原泛能量 $h$ 上识别 Jacobian；$r=1$ 时 $T=t$、$\varepsilon=1$，其 Weierstrass 模型为
$$
v^2+h uv-tv=u^3-tu^2.
$$
设 $a_1=h,a_2=-t,a_3=-t,a_4=a_6=0$，直接代入 Weierstrass 不变量定义得到
$$
\begin{aligned}
b_2&=h^2-4t,&b_4&=-ht,&b_6&=t^2,&b_8&=-t^3,\\
c_4&=h^4-8th^2+24th+16t^2,\\
\Delta&=t^3(h^4-h^3-8th^2+36th+16t^2-27t),
\qquad j_t(h)=c_4^3/\Delta.
\end{aligned}
$$
此处 $\Delta=-b_2^2b_8-8b_4^3-27b_6^2+9b_2b_4b_6$，没有再除以 $1728$。
对运算前固定的 $t=1,2$，在 $h=0$ 的两个有定义的有理函数值为
$$
\begin{array}{c|ccc}
t&c_4(0)&\Delta(0)&j_t(0)\\\hline
1&16&-11&-4096/11\\
2&64&80&16384/5.
\end{array}
$$
所以 $j_1(h)\ne j_2(h)$ 于 $k(h)$。这是原泛 Jacobian 的模函数差异：用 $h=0$ 检验两个有理函数不相等，不额外把泛 Jacobian 的识别冒称为本件新证明的全部有限纤维同构。
Step 4却给 $\mathcal A_1\simeq\mathcal A_2$ 保 $s_0,s_1$。故此标记代数不能恢复原泛能级的 $j$ 函数，命题得证。$\square$

## 4. Corrections、Open Risks 与诊断处置边界

没有加强原N02限定假设；特征零、自治、单位时间、代数闭底及原二标记均从事前对象继承。相对形式性已由Step 3的真正代数映射证明，不只逐个椭圆曲线或逐权加法同构。
这里不要求等价在整个 $t$ 参数族上规范相容，不保额外 Gauss–Manin 联络、Hodge／de Rham、导出范畴的其它生成元、谱线丛、原态射本身或回返点。加入这些资料后可能恢复信息，本件不判。
本件不能证明N01的整数 $q$-de Rham比较成立或不成立，不能推正特征／圆分平方商的乘法刚性，也没有计算任何N01积表。
作者诊断为 `N02_INFORMATION_BLINDNESS / SHORT_STANDARD_MECHANISM`：只记录N01几何解释力限界并扣除这一短标准机制，不单立N02、不提高新意或容量。
独立席应重点检查全纤维余锥、自由奇线步骤、投影公式的同一乘法及原标记，以及原泛 $j$ 的使用边界。作者尚未收到其票，不预发数学接受。

## 5. 实际工作与输入范围

原矩阵／截面定义、Step 5的表达曾以CPU SymPy符号展开核对；固定 $(t,h)=(1,0),(2,0)$ 在求值前确定，没有改参数寻碰撞。该脚本未持久化，本件显示完整代数计算供手验；运行成功不代证明。
作者本次FULL读取[SEL]66行与[PA]92行；[G]为PARTIAL精确范围1–120、120–150、336–455；[J]为PARTIAL1–180及原接受的泛 Jacobian识别结论。没有把部分原稿说成整稿FULL，也不重审P30接受。
基础来源在2026-09-12定向核：Stacks 30.22.1正文及36.30.4陈述／证明；Lurie原官方PDF的指定两条（公开页面读取超时后由同一URL流式PDF转文本取得）。没有改用替代第三方摘要，没有借此重跑全面查新；未声称读完整部 Higher Algebra。

| 本件直接本地输入 | SHA-256 |
|---|---|
| SEL | `1c899e1a7c3793c24ed568f843ff56e5cb337e391fea049edf265c9ea3163840` |
| PA | `8a8b9ba44f5e98e9ea6c31820c299dc69b81fe76b4f0ff8f67850f09a048a0a3` |
| G | `573a521e07117dc43b9291417469fa429701c67d711ec150a578b22c54205f8f` |
| J | `38e52e45513c51e9365d9bd0453776d09351fb1ca48b5d86233581112f95434f` |

只新增本证明记录；GPU0，无P31项目、锁、稿件、PDF或对外写入。原P31完整候选FAIL与22–30页合同不变。

[SEL]: PAPER31_QPI_POST_CLOSED_IDEA_REPORT_V1_20260912.md
[PA]: PAPER31_QPI_POST_CLOSED_SURVIVOR_CLAIMS_PHASE_A_V1_20260910.md
[G]: ../../papers/30-qpi-vertical-critical-ideals/paper/v4/sections/02-surface-pencil.tex
[J]: ../../papers/30-qpi-vertical-critical-ideals/paper/v4/sections/03-spectral-jacobian.tex
