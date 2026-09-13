# qPI 原时间矩阵的除子与准确回返平移点 V1

日期：2026-09-08。作者：主控。
类型：冻结候选之外的族内新证明入口，不是论文稿、新意评价或完整候选修订。
本件不属于正在运行的正式四门V1共同输入，不修改该候选T1–T4或其审查依据。

## Claim

设 $k_0$ 为任意域，$s,t\in k_0^*$，$s$ 的精确阶为 $r\ge1$。
记 $K=k_0(c)$、$T=t^r$、$\varepsilon=(-1)^{r+1}$。
取已识别的原泛动力纤维 $X_t/K$、原谱曲线 $C/K$、循环谱商 $E/K$：

$$
C:\lambda^2-(T+cz^r+z^{2r})\lambda+\varepsilon z^{3r}=0,
\qquad
E:\lambda^2-(T+cZ+Z^2)\lambda+\varepsilon Z^3=0,
\qquad Z=z^r.
$$

两者均指光滑射影模型。设 $P_0,P_T\in C(K)$ 分别为 $(z,\lambda)=(0,0),(0,T)$，
$p_0,p_T\in E(K)$ 为其像。以 $p_0$ 为 $E$ 的原点。

固定 J 的谱模约定：$\lambda$ 以原矩阵 $M$ 作用在 $\mathcal O_{\mathbb P^1}^{\oplus2}$，
其对应线丛记 $L_Q$，定义 $\alpha_t(Q)=[L_Q]\in\operatorname{Pic}^{2r}(C)$。
$E$ 在 $X_t$ 上的作用准确取为

$$
\alpha_t(Q+N)=\alpha_t(Q)\otimes\pi^*\mathcal O_E(N-p_0),
\qquad \pi:C\longrightarrow E.
\tag{1}
$$

此约定固定后，成立：

1. 在原矩阵有定义的泛动力参数上，原一步时间矩阵诱导的有理谱模同态，其除子准确为
   $$D_B=P_T-P_0.$$
   因而全部 $Q\in X_t$ 上有 Picard 态射等式
   $$\alpha_{st}(F_tQ)=\alpha_t(Q)\otimes\mathcal O_C(P_T-P_0). \tag{2}$$
2. 原完整回返 $\mathcal R=F_{s^{r-1}t}\circ\cdots\circ F_t$ 在 (1) 的 $E$-torsor 上是
   $$\mathcal R(Q)=Q+p_T. \tag{3}$$
3. 在保持原 $c$ 的带原点模型
   $$W:v^2+cuv-\varepsilon Tv=u^3-Tu^2$$
   上，(3) 的准确点为
   $$P_{\mathrm{return}}=(u,v)=(0,\varepsilon T)=-(0,0)\in W(K). \tag{4}$$
   该点在 $W(K)$ 中非挠。

这里的符号取决于明确的谱模／torsor识别；未作该识别时不能把“加$p_T$”当成任意坐标下的同一符号。
结论对每个固定 $t\ne0$ 和所有允许特征成立，不排除2、3，也不假设 $X_t(K)$ 有点。
本Claim不包含全部闭纤维的具体点阶、奇异群律或全周期频率公式。

## Status

作者状态：PROVABLE AS STATED，以下给出完整推理；尚需本件自己的非作者核查。
正在评审的完整候选V1不消费此状态，不能用本件补强或重写那两份意见。

## Assumptions and accepted inputs

只消费以下已接受的数学身份，不重新证明其未变内容：

- [J 谱 Jacobian 作者稿](PAPER30_QPI_LAX_JACOBIAN_BRIDGE_ENTRY_V1_20260908.md)：
  原 $A,M$、谱模族、$\alpha_t$ 的完整陪集同构、拉回无核及按(1)定义的原域torsor作用。
- [W 共享入口 V2](PAPER30_QPI_SHARED_WEIERSTRASS_PROOF_REUSE_V2_20260908.md)：
  全特征泛谱光滑、两图、四端点与任意原定义域前提。
- [B 原基底模型作者稿](PAPER30_QPI_EXACT_BAD_VALUES_BRIDGE_ENTRY_V1_20260908.md) Step1：
  $E\simeq W$ 的带原点代换。此处不用实际坏值或临界重数定理。
- [R 真实回返作者稿](PAPER30_QPI_RETURN_TRANSLATION_ENTRY_V1_20260908.md)：
  原一步的完整曲面同构、泛回返的整数Picard增长和无限阶。

输入均保持冻结。下文不使用本轮任何正式评审意见、新意分数或正文容量估计。

## Source scope and attribution

已实际读取 [Joshi–Roffelsen 作者 v2 §3.1](https://arxiv.org/html/2508.18578v2)，
尤其式(3.4)–(3.7)及其前后的完整时间矩阵、规范更新和原矩阵恒等式。
原 $B(z)$、Lax相容性及不变量归属JR，不计为本件发现。
下面只在代数矩阵／谱模上使用这些恒等式，不假设根单位下存在可逆基本解 $Y$。
原作者证明在圆分特征零函数域陈述；本件使用的是清分母后的有理矩阵恒等式，
其直接代数验证仅涉及 $s,x,y,t,w$ 的允许单位及实际时间分母，不除以2、3或$r$。

[Stacks, Henselian local rings](https://stacks.math.columbia.edu/tag/04GE)
用于两简单谱根的唯一提升。下文也明确写出本处递推和单位条件，不依赖底域完美。
本件没有对“准确平移点”作新的全球查新，也不声称该谱变换机制一般而言新颖。

## Notation

原一步为

$$F_t(x,y)=\left(\frac{st}{sx-y},\frac{sx}{y}\right),\qquad t\longmapsto st.$$

暂保留非零辅助规范 $w$，令 $\bar w=(1-sx/y)w$。
上横线只表示这个实际一步时间变换，不是常数域共轭。
$Q$ 表示实际泛动力曲线上的点；$\mathscr F=K(X_t)$ 是其函数域。
形式局部参数 $z$ 与原基底 $c$ 不混用。

## Proof strategy and dependency map

$$
\text{原时间矩阵}
\longrightarrow
\text{两个零端点的谱格赋值}
\longrightarrow
D_B=P_T-P_0
\longrightarrow
rD_B=\pi^*(p_T-p_0)
\longrightarrow
\text{按既定torsor作用的准确点}.
$$

同态方向、端点赋值、规范回返、任意域及符号分别核定。
非挠性最后才消费R的实际无限阶，不用该性质猜平移点。

## Proof

### Step 1. 原有理矩阵及其单位性质

在 $\mathscr F$ 上取 $Q$ 为泛点。原矩阵恒等式为

$$
\bar M(z)B(z)=B(z)M(z),\qquad
B(z)=I+\frac{B_0}{z},
$$

$$
B_0=s
\begin{pmatrix}
x(1-y^{-1})&wxy^{-1}\\
-w^{-1}xy(1-y^{-1})^2&-x(1-y^{-1})
\end{pmatrix}.
\tag{5}
$$

直接乘法给

$$B_0^2=0,\qquad\operatorname{tr}B_0=\det B_0=0,\qquad
\det B(z)=1,\qquad B(z)^{-1}=I-B_0/z. \tag{6}$$

其中 $(B_0)_{12}=swx/y\ne0$，故 $B_0$ 秩为一，包括特征二和 $y=1$。
原 $A_0$ 是

$$
A_0=\begin{pmatrix}
t+x-xy&-wx\\
w^{-1}(t+x-ty-2xy+xy^2)&x(y-1)
\end{pmatrix}.
$$

置 $e_T=(w,1-y)^{\mathsf T}$，直接计算为

$$A_0e_T=te_T,\qquad B_0e_T=0. \tag{7}$$

由 $A_0^2=tA_0$，

$$M(0)=A_0^r=t^{r-1}A_0, \tag{8}$$

其两个特征值为 $0,T$，互异。因此 $\ker B_0$ 准确是 $M(0)$ 的 $T$-特征线；
$B_0$ 在 $0$-特征线上非零。这一步不依赖 $r=1$。

泛点处原一步各分母与 $\bar w$ 非零：原曲面环面坐标具有函数域 $k_0(x,y)$，
原积分是其非恒定元素 $c=I_r$，而 $y-sx$ 并非零函数。
R的曲面同构使有限个后续时间变换仍是函数域同构，故可在共同稠密开集逐次工作。

### Step 2. 真正谱模同态及非端点的可逆性

按J的推下约定，(5)使 $B$ 成为谱代数模的有理同态

$$b_Q:L_Q\dashrightarrow L_{F_tQ}. \tag{9}$$

方向是“源$M$到目标$\bar M$”，因为 $\bar M B=B M$，不是反向。
对 $z\ne0,\infty$，(6)给出正则可逆矩阵；
连同谱代数相容性，它在全部这些点都是线丛同构，包括双覆盖的分歧点。
无穷远以 $a=z^{-1}$ 作参数，$B=I+aB_0$ 正则可逆。
它也与无穷远生成元 $\mu=\lambda z^{-2r}$ 的作用相容，故两无穷远谱点均无零极。
所以(9)的除子仅可能支撑在 $P_0,P_T$。

### Step 3. 零端点的两个准确赋值

在 $A=\mathscr F[[z]]$ 上，谱多项式模 $z$ 为 $\lambda(\lambda-T)$。
两根之差 $T$ 为单位，故唯一提升为 $\lambda_0(z),\lambda_T(z)\in A$，
分别模 $z$ 等于 $0,T$。具体地，逐次已解到模 $z^m$ 后，
下一系数由导数模 $z$ 的单位 $\mp T$ 唯一确定，完备性给出实际幂级数根。
整个论证不需要 $\mathscr F$ 可分闭、代数闭或完美。

对源与目标矩阵分别用幂等投影

$$
\frac{M-\lambda_T I}{\lambda_0-\lambda_T},
\qquad
\frac{M-\lambda_0 I}{\lambda_T-\lambda_0}
\tag{10}
$$

及 $\bar M$ 的相同表达式，将 $A^2$ 分成两个自由秩一谱格。
分母为单位；投影的模 $z$ 秩为一，故两格各有本原基，合成 $A^2$ 的基。
这些格正是(9)在两谱端点完备局部环中的线丛格。

相容性使 $B$ 在源／目标谱基间为对角标量 $b_0(z),b_T(z)\in\mathscr F((z))^*$。
在源$0$-谱格的本原向量 $e_0(z)$ 上，$B_0e_0(0)\ne0$，
因此

$$B e_0(z)=z^{-1}B_0e_0(0)+O(1),\qquad
\operatorname{ord}_z b_0=-1. \tag{11}$$

源／目标两谱基的行列式都是 $A^*$。由 $\det B=1$，

$$\operatorname{ord}_z b_0+\operatorname{ord}_z b_T=0. \tag{12}$$

于是 $\operatorname{ord}_z b_T=1$，不是只得到一个下界。
结合Step2，(9)作为 $L_{F_tQ}\otimes L_Q^{-1}$ 的有理截面，其准确除子为

$$\operatorname{div}(b_Q)=P_T-P_0. \tag{13}$$

有理截面的除子约定给 $L_{F_tQ}\otimes L_Q^{-1}\simeq\mathcal O_C(P_T-P_0)$，
所以符号与(2)一致。

### Step 4. 规范不变性、全部点及完整回返

不同非零 $w$ 只通过常数对角矩阵共轭改变 $M$。
即使该常数依赖动力参数，只要在参数开集为单位，其谱线丛族仍同构，
所以 $\alpha_t$ 及(13)在Picard中的等式与 $w$ 无关。
不要求经过$r$步后 $w$ 恢复初值。

每个时间切片的 $T=(s^jt)^r$ 相同，故所有 $\alpha_{s^jt}$ 取值于同一个 $\operatorname{Pic}^{2r}(C)$。
(2)已在泛点成立；两边均为 $X_t$ 到该分离Picard方案的态射，
其中 $F_t:X_t\to X_{st}$ 是已知曲线同构。
整曲线上两个态射在稠密开集相等则全局相等，故(2)覆盖全部 $Q$。
逐步合成并用 $s^rt=t$ 得

$$
\alpha_t(\mathcal RQ)=\alpha_t(Q)\otimes\mathcal O_C\bigl(r(P_T-P_0)\bigr).
\tag{14}
$$

两个端点局部参数的商映射均为 $Z=z^r$，因而

$$\pi^*(p_0)=rP_0,\qquad \pi^*(p_T)=rP_T. \tag{15}$$

$r=1$ 时这些是恒等覆盖的相同等式，不需要额外例外。
由(1)、(14)、(15)及 $\alpha_t$ 的闭嵌入，
得到 $\mathcal RQ=Q+p_T$，既无剩余$r$倍因子，也无未知同源核。
所有构造在原 $K$ 上定义；并未通过任意选择的几何同构下降。

### Step 5. Weierstrass坐标与非挠性

B的带原点代换为

$$u=\frac{\varepsilon TZ}{\lambda},\qquad
v=\frac{\varepsilon T^2}{\lambda}. \tag{16}$$

在 $p_T=(0,T)$ 处分母为单位，因此(16)直接给 $(u,v)=(0,\varepsilon T)$；
$p_0$ 映到无穷远原点。
长Weierstrass方程的负元为

$$-(u,v)=(u,-v-cu+\varepsilon T). \tag{17}$$

故 $(0,\varepsilon T)=-(0,0)$，包括特征二。
在代数闭常数域扩张后，R的整数Picard增长排除泛回返有限阶。
若 $p_T$ 在原 $E(K)$ 中挠，则(3)会使同一幂的回返恒等，扩域后仍恒等，矛盾。
因此(4)中的点非挠。$\square$

## Corrections or missing assumptions

本作者证明没有增加 $X_t(K)$ 有点、特征不为2或3、一般$t$等假设。
几何对象仍是超越$c$上的原泛曲线；没有把当前Claim换成闭纤维点阶定理。
具体符号只能与(1)的谱模约定一起引用，不能与未经核对的自治坐标识别拼接。

## Open risks and handoff boundary

- 新消费者待非作者核查：谱模方向、两个谱格、(12)的行列式单位、$r$步规范独立、
  原域作用及(4)的符号。既有J/R独审不自动给本件PASS。
- 要推出每个光滑闭纤维的准确点阶公式，仍须明确验证指定Jacobian识别和指定点的相对延拓；
  本件未把泛等式自动当成全部特化结论。
- 奇异闭纤维的广义群律、具体乘法／加法参数与完整周期统计不在本证明内。
- 本件未作新意或独立价值判断，未加入本次正式V1候选的共同清单；
  当前两票无论结果如何，都必须按原冻结T1–T4独立处置。
- 原 $\bar A(z)B(z)=B(sz)A(z)$ 相容性及(6)–(8)另以精确符号矩阵乘法核对，
  输出零矩阵／非零秩一见证；从一步相容性循环相乘即得(5)；
  该检查只防代数转录错误，不替代Steps2–5证明。
