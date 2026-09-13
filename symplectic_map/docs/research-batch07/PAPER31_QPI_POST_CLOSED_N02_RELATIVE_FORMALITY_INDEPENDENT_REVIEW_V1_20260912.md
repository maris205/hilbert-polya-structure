# Paper31／N02：相对代数形式性短证明——独立数学审查 V1

日期：2026-09-12；独立席：`/root/p31_post_closed_n02_formality_independent_v1`。
审查对象：[作者短证明][A]，冻结 SHA-256 为 `6f2cf44f33de6c177ebd03b0806837fb74e234372781518f8156861a9e7c6b3a`。
性质：fresh 非作者、有界新增数学审查；不是正式四门、查新评分、论文准入或旧 P30 证明重审。
`route_applicability: NOT_APPLICABLE`。

## 1. Claim：原命题与解释

固定代数闭特征零域 $k$、$q=1$、$t\in k^\times$，使用原八次吹起曲面 $S_t$、$D_t=-K_{S_t}$ 及原完整铅笔，不能改换到任意同谱曲面。
原线丛截面及能量标签为
$$
s_{0,t}=xy,\qquad s_{1,t}=x^2-x^2y+xy^2-ty,\qquad
h=s_{1,t}/s_{0,t}.
$$
这里多项式是在既定平凡化中表示线丛截面；在 $\mathcal O(D_t)$ 的有理截面字典中为 $1,I_{1,1}$，不是完整曲面的全局正则函数。
令 $B=\mathbb P^1_k$，固定 $[a:b]$ 与 $h=b/a$，$f_t=[s_{0,t}:s_{1,t}]$，并令
$$
\mathcal E_t=Rf_{t*}\mathcal O_{S_t},\qquad
\mathcal A_t=\bigoplus_{n\geq0}R\Gamma(S_t,\mathcal O_{S_t}(nD_t)).
$$
要证明的是 $E_\infty$ 代数等价，而非仅导出模或上同调环同构：
$$
\mathcal E_t\simeq\mathcal O_B\oplus\mathcal O_B(-1)[-1],
$$
右侧为平方零扩张；由同一个相对等价得到
$$
\mathcal A_t\simeq k[a,b]\oplus\xi k[a,b],\qquad d=0,\quad\xi^2=0,
$$
其中 $a,b,\xi$ 的权均为一，$|a|=|b|=0$、$|\xi|=1$，且保持单位、全非负权、原两截面及乘 $s_0$ 的极阶包含。
命题只要求等价存在，不要求选择在整个 $t$ 参数族上规范相容。
最后，原泛能级 Jacobian 的 $j_1(h)$ 与 $j_2(h)$ 不同，故上述标记代数不能恢复该固定能量标签下的泛 $j$ 函数。

## 2. Status

**PROVABLE AS STATED。原命题存活，不需要削弱或增添科学假设。**

作者 Step 3 已补足真正关键的乘法步骤：全局模提升经自由交换代数泛性质给出实际 $E_\infty$ 映射，再以底层准同构判定等价。这里不是由 $\operatorname{Ext}^2=0$ 直接宣布形式性。
Step 4 可以在分次代数及其相对单位下统一执行，因此也不是拼合各权互不兼容的分裂。
本席逐项结论为：全纤维／单位余锥成立；非仿射底自由奇线成立；全分次乘法与标记成立；泛 Jacobian 身份及 $j$ 检验范围成立。

## 3. Assumptions、Notation 与依赖图

本席仅消费以下已接受几何输入，不重新验证其旧证明：$S_t$ 光滑射影、几何有理；$D_t=-K_{S_t}$；原 $|D_t|$ 完整且无基点；$f_t$ 射影平坦、有限表示，所有完整纤维为 Cartier 除子且线性等价于 $D_t$；$H^1(S_t,\mathcal O)=H^2(S_t,\mathcal O)=0$。原泛状态曲线的 Jacobian 与 [J] 的 $r=1$ Weierstrass 曲线相同，也作为已接受输入。

$D_{\rm qc}(B)$ 在这里指带标准导出对称张量结构的稳定 $\infty$-范畴；$\operatorname{CAlg}$ 指其中的交换代数对象。$M[-1]$ 将次数零的层置于上同调次数一。权是独立的外部分次，不额外改变 Koszul 符号。

依赖关系如下：

1. 完整纤维的 Cartier 序列、$D=-K$、有理曲面消失及 Serre 对偶给全部纤维的 $H^0,H^1$。
2. proper flat 基变换与 perfect 复形的局部判据给单位余锥 $\mathcal L[-1]$；曲面 Euler 特征与 $\mathbb P^1$ 线丛分类给 $\mathcal L\simeq\mathcal O(-1)$。
3. $\operatorname{Ext}^2_B(\mathcal L,\mathcal O_B)=0$ 只给生成元的全局模提升；特征零、秩一与自由代数泛性质进一步给 $E_\infty$ 等价。
4. 原 $f^*\mathcal O(1)$ 标记、相容投影公式及非负权线丛的上同调消失给原全分次等价。
5. 已接受的原泛 Jacobian 身份与独立不变量展开给 $j_1\ne j_2$，与第 4 项构成同一原族的信息碰撞。

## 4. Proof／逐项独立核查

### 4.1 全纤维、泛点与单位余锥

对任意闭点 $z\in B(k)$，完整纤维 $G=f_t^{-1}(z)$ 满足
$$
0\longrightarrow\omega_{S_t}\longrightarrow\mathcal O_{S_t}
\longrightarrow\mathcal O_G\longrightarrow0.
$$
Serre 对偶与已接受的有理曲面消失给
$$
H^0(\omega_{S_t})=H^1(\omega_{S_t})=0,\qquad H^2(\omega_{S_t})=k.
$$
长正合列因而给常数映射 $k\xrightarrow{\sim}H^0(G,\mathcal O_G)$ 及 $H^1(G,\mathcal O_G)\simeq k$。其余次数为零。该推导依赖完整 Cartier 除子而不依赖光滑、不可约或约化，故覆盖无穷纤维和奇异纤维；也不需要先找有限纤维上的点。

作者“域扩张后也适用于泛点”的压缩句可严格展开：先把整曲面、铅笔和上述消失基变换到 $K=k(h)$，然后在 $B_K$ 上取坐标值为 $h\in K$ 的 $K$-有理点。它的纤维就是原泛纤维，仍线性等价于 $D_{t,K}$，所以同一序列给 $K$ 与 $K[-1]$。这里不是把原 $S_t$ 的非闭泛纤维直接冒称为闭 Cartier 除子。

原 $f_t$ proper、flat、有限表示，$\mathcal O_{S_t}$ perfect，满足 [Stacks Lemma 36.30.4](https://stacks.math.columbia.edu/tag/0A1G) 的条件；于是 $\mathcal E_t$ perfect，且导出基变换识别各纤维的导出函数。其 Noetherian 仿射版本亦见 [Lemma 30.22.1](https://stacks.math.columbia.edu/tag/07VJ)。
令 $C_t$ 为单位映射的余锥。由于上面的 $H^0$ 同构正是常数单位，得到
$$
C_t\otimes^{\mathbf L}k(z)\simeq k(z)[-1]
$$
对所有底点成立，且 $C_t$ perfect。
在任意底点取其有界有限自由代表，消去微分中的单位矩阵项。所得极小代表模剩余域的微分为零，而剩余域上只有次数一的一维上同调，因此只剩次数一的秩一项。这些消去及秩描述可延伸到该点的开邻域，给 $C_t\simeq\mathcal L_t[-1]$，其中 $\mathcal L_t$ 是线丛。
这不是从纤维维数表未经局部判据直接推断层分裂。

单位三角与 Leray 的 Euler 特征给
$$
1=\chi(S_t,\mathcal O)=\chi(B,\mathcal O_B)-\chi(B,\mathcal L_t)
=1-\chi(B,\mathcal L_t).
$$
写 $\mathcal L_t\simeq\mathcal O_B(d)$ 后，$\chi(\mathcal L_t)=d+1=0$，所以 $d=-1$。移位的负号正确；没有反转成 $\mathcal O(1)$。

结论：作者 Step 1–2 成立。

### 4.2 非仿射底上的自由奇线与全部高乘法

单位三角的连接类属于
$$
\operatorname{Hom}_{D_{\rm qc}(B)}(\mathcal L_t[-1],\mathcal O_B[1])
=\operatorname{Ext}^2_B(\mathcal L_t,\mathcal O_B)
=H^2(B,\mathcal L_t^\vee)=0.
$$
所以存在全局模映射 $\eta:M\to\mathcal E_t$，其中 $M=\mathcal L_t[-1]$，且商映射复合在导出范畴中为恒等。选择该映射的一个 $\infty$-范畴代表即可使用自由代数泛性质；不需要另证明该模映射本身已满足乘法关系。

$D_{\rm qc}(\mathbb P^1_k)$ 有所需余极限，其张量逐变量保余极限。自由交换代数存在，底层为
$$
\operatorname{Sym}(M)=\bigoplus_{m\geq0}(M^{\otimes m})_{h\mathfrak S_m}.
$$
上述普遍构造适用于对称幺半 $\infty$-范畴而不要求底 scheme 仿射；其对称幂及自由代数公式见 [Lurie, Higher Algebra，Construction 3.1.3.9、Notation 3.1.3.10、Proposition 3.1.3.13、Example 3.1.3.14，印刷页 345–346](https://www.math.ias.edu/~lurie/papers/HA.pdf)。

关键消失也可完全层局部验证。对 $m\geq2$，$M^{\otimes m}=\mathcal L_t^{\otimes m}[-m]$，置换的作用是符号表示。因为特征零，$m!$ 在所有局部环可逆，有限群取余不变量的函子由平均幂等元给出且正合，其导出版本无额外高群同调。符号表示中一个换位作用为 $-1$，所以余不变量中 $v=-v$；二可逆使其为零。
这是在准凝聚层／复形中取群同伦余不变量，没有把非仿射底上的 $R\Gamma$ 错换成普通 $\Gamma$。

为把“底层只剩两项”与“平方零代数”明确连接，可令 $Q=\mathcal O_B\oplus M$ 为标准平方零 $E_\infty$ 代数。生成元包含 $M\to Q$ 诱导
$$
\operatorname{Sym}(M)\longrightarrow Q.
$$
它在自由权零及一上为恒等，其他自由权的源均为零，故底层为等价，进而为 $E_\infty$ 等价。这给作者第 110–113 行的平方零识别一个显式实现，不遗漏高运算。
另由 $\eta$ 的自由泛性质得到实际代数映射
$$
\operatorname{Sym}(M)\longrightarrow\mathcal E_t.
$$
它在 $\mathcal H^0$ 上是单位同构，在 $\mathcal H^1$ 上是 $\eta$ 的同构，其他上同调皆零。忘却函子检测等价，故得到 $Q\simeq\mathcal E_t$ 为 $E_\infty$ 代数等价。
这同时处理全部高乘法；无需另以 Massey 积逐项检验替代已有的代数映射。

结论：作者 Step 3 成立。若删去自由代数这一步，仅保留 $\operatorname{Ext}^2=0$，则论证会不足；实际作者稿没有删去它。

### 4.3 全分次乘法、原标记与 $n=0$

无基点标记二截面给一个确定的线丛识别
$$
f_t^*\mathcal O_B(1)\simeq\mathcal O_{S_t}(D_t),\qquad
a\mapsto s_{0,t},\quad b\mapsto s_{1,t}.
$$
只对这一识别取张量幂，就同时保持全部权的乘法，不产生逐权重选的自由度。
令 $\mathcal T=\bigoplus_{n\geq0}\mathcal O_B(n)$ 为外部分次层代数。相对单位及投影公式给同一个分次代数比较
$$
\mathcal T\otimes\mathcal E_t\longrightarrow Rf_{t*}(f_t^*\mathcal T).
$$
在每一权上它是投影公式同构。原态射 proper 因而 quasi-compact、quasi-separated，满足 [Stacks Lemma 36.22.1](https://stacks.math.columbia.edu/tag/08EU)；所有线丛还是 perfect。乘法兼容性来自同一伴随单位及 $Rf_*$ 的 lax symmetric monoidal 结构，局部平凡化各线丛时就是恒等比较，因此不是额外选择一张只在上同调交换的图。

把上一节的同一个 $\mathcal O_B$-代数等价张量 $\mathcal T$，再逐权取导出全局截面，得到作者的模型
$$
\bigoplus_{n\geq0}R\Gamma\bigl(B,\mathcal O_B(n)\oplus\mathcal O_B(n-1)[-1]\bigr).
$$
可始终在非负分次对象范畴逐权操作；不需要未经论证交换无限乘积与 $R\Gamma$。

普通截面到导出截面的乘法比较可以用 $B$ 的标准两开集覆盖 $D_+(a),D_+(b)$ 显式实现：先对分次平方零层代数取乘法型 Čech 余单纯对象，再取其 $E_\infty$ 同伦全化。普通全局截面有兼容全部乘法的增广映射进入该全化；其底层计算 $R\Gamma$。
对所有 $n\geq0$，$\mathcal O(n)$、$\mathcal O(n-1)$ 均无正次上同调，因此此映射逐权为准同构。所需线丛计算及齐次截面乘法可见 [Stacks Lemmas 30.8.1–30.8.2](https://stacks.math.columbia.edu/tag/01XS)。
特别地，
$$
R\Gamma(B,\mathcal O(-1))=0,\qquad R\Gamma(B,\mathcal O)=k,
$$
所以权零确实只有单位 $k$，没有多出一个权零的奇生成元。权一的奇项为 $H^0(\mathcal O(0))[-1]$，从而 $\xi$ 的权必须为一。
通常权 $n\geq1$ 的奇项为 $\xi k[a,b]_{n-1}$，恰与 $H^0(\mathcal O(n-1))[-1]$ 相同。

整个比较是相对 $\mathcal T$ 的，取截面后为 $k[a,b]$ 下的等价。因此同时保持两原截面及其所有多项式，而非仅保两个偶向量的维数。原极阶包含在 $\mathcal O(nD)\to\mathcal O((n+1)D)$ 上乘标准边界截面，在原多项式字典中就是乘 $s_0$，对应模型中的乘 $a$。
这里“保持”采用作者已经声明的导出代数／标记截面意义；不另声称任意预选链代表之间有逐字相同的严格链映射。

结论：作者 Step 4 成立，得到任意两个单位时间之间保持原二标记的全非负分次等价，不只是有限权观察。

### 4.4 原泛 Jacobian 与 $j$ 函数

[J] 第 4–13 行先固定原泛状态曲线；第 181–185 行在 $r=1$ 识别谱曲线与 Weierstrass 泛曲线；第 399–435 行的已接受结论识别原泛状态曲线的 Jacobian。故这里使用的不是仅与原曲线有相似方程的旁支对象。
取 $r=1$ 后 $T=t$、$\varepsilon=1$，模型为
$$
v^2+huv-tv=u^3-tu^2.
$$
从 $a_1=h,a_2=-t,a_3=-t,a_4=a_6=0$ 独立计算得到
$$
b_2=h^2-4t,\quad b_4=-ht,\quad b_6=t^2,\quad b_8=-t^3,
$$
$$
c_4=h^4-8th^2+24th+16t^2,
$$
$$
\Delta=t^3(h^4-h^3-8th^2+36th+16t^2-27t),\qquad j_t=c_4^3/\Delta.
$$
这里使用 $\Delta=-b_2^2b_8-8b_4^3-27b_6^2+9b_2b_4b_6$；作者没有误加 $1728$ 分母。
由于 $t\ne0$，$\Delta$ 作为 $h$ 的多项式非零，泛曲线非奇异。
对事前固定的两个时间，独立展开和精确求值得到
$$
(c_4(0),\Delta(0),j_1(0))=(16,-11,-4096/11),
$$
$$
(c_4(0),\Delta(0),j_2(0))=(64,80,16384/5).
$$
两分母在特征零域非零，两有理数不同。因此两个 $k(h)$ 中的有理函数不相等。该一步只是以一个共同有定义点分辨泛有理函数，不需要本次另证明所有有限纤维与 Weierstrass 模型的同构。

结论：作者 Step 5 成立。原二标记固定了 $h=b/a$，因而不允许为了比较这两个函数另作底上的 Möbius 重参数化；本票也不评价忘掉能量标记后的曲面分类。

## 5. Corrections or Missing Assumptions

**必须修：无。** 未发现需要新几何假设、弱化结构等级、缩小非负权范围或改换参数的硬缺口。

可选表达改进，均不构成降级条件：

1. 作者第 80 行可补写先扩底到 $k(h)$、再取 $B_{k(h)}$ 的有理点，从而把泛点句展开成本文 §4.1 的论证。
2. 作者第 110–113 行可补上 $\operatorname{Sym}(M)\to\mathcal O\oplus M$ 的显式代数等价，帮助读者区分底层两项分解与平方零 $E_\infty$ 模型。
3. 作者第 135 行可补一行“使用乘法型 Čech 增广并逐权取同伦全化”；第 137 行可写为“在 $k[a,b]$ 下的等价，故保持标记截面”，避免把导出保持误读成特定链模型的严格相等。
4. 作者对 $D_{\rm qc}(B)$ 已给出 $E_\infty$ 解释；若转写正式文本，可显式称其为稳定 $\infty$-范畴，而非仅使用通常指三角范畴的记号。

## 6. Open Risks 与准确结论边界

本命题范围内没有尚未闭合的证明义务；本票以指定且已接受的 P30 几何／原泛 Jacobian 结果为依赖，不替代其旧验收。
结论只说明给定 $\mathcal A_t$ 及其原 $s_0,s_1$、单位、乘法和极阶包含，不足以恢复固定 $h$ 下的原泛 $j_t(h)$。
它不声称所有几何增强失明，不保存原曲面态射、谱线丛、回返点、联络、Hodge／de Rham 数据或其它导出范畴对象，也不对这些增强能否恢复几何作判断。
它不要求在全部时间上规范地选取等价，不扩展至 $t=0$、正特征或整数圆分平方商。
本票不推出 N01 的整数 $q$-de Rham 比较为真或为假，不判其低权混合运算／标记消费者，也不把本结果转换为正式四门、论文接受或研究投入评分。

## 7. 独立性、实际阅读、验证与身份绑定

本席没有参与作者稿写作，也没有修改作者稿、索引、历史记录或原 P30 输入。入席后本人读取了作者完整证明，因此独立性是 fresh 非作者的论证检查，不是对作者结论或历史背景盲化。没有另派子代理。
本人全文读取 `AGENTS.md` 28 行、`docs/WORKFLOW.md` 39 行、`proof-writer/SKILL.md` 223 行及 `research-review/SKILL.md` 106 行。按 proof-writer 组织准确命题、假设、依赖、完整证明核查与边界；research-review 指定的 GPT-5.4 Codex MCP 在本席可用工具中未配置，依任务采用可用 Codex xhigh 独立席替代，不声称 GPT-5.4 实调或跨模型验证。

本地科学输入的本人实际读取范围与哈希为：

| 输入 | 实际阅读范围 | SHA-256 |
|---|---|---|
| [A：作者短证明][A] | FULL，1–193 行 | `6f2cf44f33de6c177ebd03b0806837fb74e234372781518f8156861a9e7c6b3a` |
| [SEL：事前选择][SEL] | FULL，1–66 行 | `1c899e1a7c3793c24ed568f843ff56e5cb337e391fea049edf265c9ea3163840` |
| [PA：幸存主张][PA] | PARTIAL，§2，第 25–36 行 | `8a8b9ba44f5e98e9ea6c31820c299dc69b81fe76b4f0ff8f67850f09a048a0a3` |
| [G：原曲面／铅笔][G] | PARTIAL，第 1–150、336–446 行；文件共 446 行，所请求 336–455 的有效范围止于 EOF | `573a521e07117dc43b9291417469fa429701c67d711ec150a578b22c54205f8f` |
| [J：原泛 Jacobian][J] | PARTIAL，第 1–185、390–435 行；文件共 438 行 | `38e52e45513c51e9365d9bd0453776d09351fb1ca48b5d86233581112f95434f` |

以上五输入的哈希均由本席实际计算并与指定值／作者记录核对一致。一次工具输出受限后，已重新完整读取被截断的 PA 指定段与 G 前段；没有继承作者的 FULL 阅读身份，也没有冒称全文读过 G、J。

外部一手来源核查日期为 2026-09-12，仅服务本次新增证明：Stacks 36.30.4 及其所在页的相关证明、30.22.1 正文／证明、36.22.1 正文／证明、30.8.1–30.8.2 的相关计算；Higher Algebra 由官方 URL 流式转文本，取印刷页 343–348，重点读取 345–346 的指定自由代数构造与命题。浏览器直接打开该 PDF 超时后使用同一官方 URL 成功取得；不声称读完整书，也未把网页评论作为数学依据。
本席另以一次不落盘的 SymPy 精确展开复核全部 $b_i,c_4,\Delta$ 及固定两点值，输出与 §4.4 一致；符号工具只验证转录，证明仍是本报告显示的代数恒等式及逻辑链。

本席本人 FULL 读回本件终稿 233 行；输出 SHA-256 在最终交付消息中给出，以避免把文件自身哈希写入自身造成自引用。只交付本指定新审查记录。

[A]: PAPER31_QPI_POST_CLOSED_N02_RELATIVE_FORMALITY_DIAGNOSTIC_V1_20260912.md
[SEL]: PAPER31_QPI_POST_CLOSED_IDEA_REPORT_V1_20260912.md
[PA]: PAPER31_QPI_POST_CLOSED_SURVIVOR_CLAIMS_PHASE_A_V1_20260910.md
[G]: ../../papers/30-qpi-vertical-critical-ideals/paper/v4/sections/02-surface-pencil.tex
[J]: ../../papers/30-qpi-vertical-critical-ideals/paper/v4/sections/03-spectral-jacobian.tex
