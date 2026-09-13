# Proof Package：根单位反函数／循环芽规约的非作者核查

日期：2026-09-07。角色：非作者数学核查；审查者未参与本次被审 V3 的
根单位 germ／反函数作者构造。本报告不审查审查者自己的 $Q$ 或 Ward 响应稿。
使用本轮已完整读取的 proof-writer 技能；唯一新增文件为本报告。

## Claim

完整阅读 287 行
[Root-preserving probe V3](PAPER30_TWIST_ROOT_PRESERVING_PROBE_V3_20260907.md)，
审查其归一化、反函数提取、循环芽有限射流条件的双向等价、
群平均线性化、共振规范及真实五分母参数仿射障碍。

本次实际所读输入 SHA-256：

```text
d2901b6c419635673813e62cf6702dae91e86258d9823c09f8db6e678291f167
```

## Status

上述明确的代数及有限射流命题：`PROVABLE AS STATED`。
没有发现需修改作者公式、反向证明或射流阶数的错误；本报告不修改作者文件。
全分母实根数量、重数和简单性并未由这些规约证明，仍保持 OPEN。

## Assumptions

- 固定互素 $0<r<s$、$s\ge3$，$\zeta=e^{2\pi ir/s}$ 为本原单位根。
- 使用正树权规范 $a=-4\lambda$、$t=-X/2$，$X$ 是未缩放物理正频变量。
- 截断 $v$ 到 $s-1$ 阶；$R_s$ 不除以零的共振分母 $D_s$。
- germ 的复合恒等式 $\mathcal G^{\circ s}=\mathrm{id}$ 是准确恒等式，
  对数式仅要求指定有限阶。解析与形式两个版本分别按其原文含义理解。
- 对数用于常数项为 $1$ 的单位级数；原点附近解析对数也由该规范唯一选定。

## Notation

$\mathcal D_\zeta=2-S_\zeta-S_{\zeta^{-1}}$，
$H_a(y)=y+ay^2$，$Y=t e^v$，$T=Y^{-1}$，$w=\log(y/T)$。
$Y^{-1}$ 表示复合逆。$R_s=[t^s]H_a(Y)$。

## Proof Strategy

先从物理正频驻值式重新检查尺度和符号；再独立用留数分部积分检查提取式。
双向 germ 证明分别核对存在性构造和群平均反演，特别检查共振自由度没有影响首障碍。
第四阶反函数系数用另一条 Lagrange 系数式核算，并作有限精确符号自验。

## Dependency Map

1. $\mathcal D_\zeta t^n=D_nt^n$ 与非共振递推给出首障碍。
2. 可逆 $Y'(0)=1$ 与形式留数换元给出反函数系数式。
3. 有限阶旋转共轭给出正向循环芽；群平均给出反向线性化。
4. 共振规范变化与旋转交换，故不改变同一个 germ。
5. 反函数四阶公式加上 $D_2,D_4$ 的真实值，否定指定参数仿射表示。

## Proof

### Step 1. 规范与根单位差分

令 $\Pi$ 删除共振频率。对被审截断，物理正支的投影方程为
$\mathcal D_\zeta v=-\Pi(X e^v/2+\lambda X^2e^{2v})+O(X^{s+1})$。
代入 $X=-2t$ 得
$\mathcal D_\zeta v=\Pi H_a(Y)+O(t^{s+1})$，其中
$H_a(Y)=t e^v-4\lambda t^2e^{2v}$，
所以作者正树权递推的符号正确。
物理系数为 $-2[X^s]$ 的共振力，变换后得到

$$C_{r,s}(\lambda)=2(-1/2)^sR_s(-4\lambda).$$

低于 $s$ 阶的差分系数逐项由递推抵消；第 $s$ 阶左侧为零，
而 $H_a(Y)$ 的该阶只依赖 $v_1,\ldots,v_{s-1}$。
故作者式 (1) 的 $-R_st^s$、式 (2) 的对数分子方向均正确。

### Step 2. 反函数 Lagrange 公式

独立换元 $t=T(y)$，再对 $H_a(y)T(y)^{-s}$ 的导数取零留数，有

$$
\begin{aligned}
R_s
&=\operatorname{Res}H_a(y)T'(y)T(y)^{-s-1}\,dy\\
&=\frac1s\operatorname{Res}(1+2ay)T(y)^{-s}\,dy\\
&=\frac1s[y^{s-1}](1+2ay)e^{s w(y)}.
\end{aligned}
$$

因此 $1/s$、$1+2ay$ 和指数 $sw$ 三个规范均准确。
该式仅需 $w$ 到 $y^{s-1}$，亦即 $Y$ 到 $t^s$；没有暗中使用 $v_s/D_s$。
$w$ 仍依赖原非线性消元，作者也未将“指数系数”本身当作保根定理。

### Step 3. 正向存在性及复合阶

对任意固定复 $a$，截断 $v$ 为多项式，$Y=t e^v$ 满足 $Y'(0)=1$，
所以存在解析局部逆。定义
$\mathcal F=Y\circ(\zeta\,\cdot)\circ T$ 后，
$\mathcal F^{\circ s}=\mathrm{id}$；若存在更小正整数 $m$ 使
$\mathcal F^{\circ m}=\mathrm{id}$，则线性部强制 $\zeta^m=1$，与本原性矛盾。
因此阶数恰为 $s$。

把作者式 (2) 换回 $y$，并注意对数取了相反的比值方向，得到

$$\log\frac{\mathcal F(y)\mathcal F^{-1}(y)}{y^2}
=-y-ay^2+R_s y^s+O(y^{s+1}).$$

$T(y)^s=y^s+O(y^{s+1})$ 确保障碍系数不变。
所以 $R_s=0$ 的确给出满足指定射流条件的解析循环芽，
而不是只给出一个未证收敛的形式构造。

### Step 4. 反向群平均的方向及障碍恢复

设 $\mathcal G'(0)=\zeta$、$\mathcal G^{\circ s}=\mathrm{id}$。
平均

$$\widetilde T(y)=\frac1s\sum_{j=0}^{s-1}\zeta^{-j}\mathcal G^{\circ j}(y)$$

的导数为 $1$。重新编号 $j+1=k$ 后，端点 $\mathcal G^{\circ s}=\mathrm{id}$
补回 $k=0$ 项，得到

$$\widetilde T(\mathcal G(y))=\zeta\widetilde T(y),$$

不是乘以 $\zeta^{-1}$。故
$\mathcal G=\widetilde Y\circ(\zeta\,\cdot)\circ\widetilde T$。
将对数射流条件代入 $y=\widetilde Y(t)$，准确恢复

$$\mathcal D_\zeta\widetilde v
=H_a(\widetilde Y)+O(t^{s+1}).$$

在 $n<s$，所有 $D_n\ne0$，三角递推强制
$\widetilde v_n=v_n$。到第 $s$ 阶，左边因 $D_s=0$ 消失；
右边系数只使用这些已经唯一确定的低阶系数，因而等于 $R_s$，必须为零。
这证明原文声称的反向蕴含；不需假定平均产生的 $\widetilde v_s$ 预先为零。

### Step 5. 共振规范与射流阶数

令 $c=\widetilde v_s$，$h(t)=t e^{-ct^s}$。因 $\zeta^s=1$，
$h(\zeta t)=\zeta h(t)$。
更换 $\widetilde Y$ 为 $\widetilde Y\circ h$，相应逆更换为
$h^{-1}\circ\widetilde T$，所以 $\mathcal G$ **准确不变**。

新的对数为
$\log(h(t)/t)+\widetilde v(h(t))$。
第一项贡献 $-ct^s$；第二项在 $s$ 阶以下与 $\widetilde v(t)$ 相同，
其合成引入的首个新误差至少为 $s+1$ 阶。
所以确实去掉 $\widetilde v_s$，保持全部低阶系数。

计算 $\mathcal F(y)\mathcal F^{-1}(y)/y^2$ 到 $y^s$，
需要分子到 $y^{s+2}$；两因子都从一次开始，因此需各 germ 到 $y^{s+1}$。
作者已明确这一阶数。完整共轭和与旋转交换的规范变化，均未丢失该射流。

### Step 6. 反函数第四阶与真实五分母系数

由 $w(y)=v(T(y))$ 的 Lagrange 公式可独立得到

$$[y^n]w=-\frac1n[t^n]e^{-nv(t)}.$$

取 $n=4$，直接展开指数，得

$$[y^4]w=v_4-4v_1v_3-2v_2^2+8v_1^2v_2-\frac83v_1^4,$$

与作者的直接反演式一致。对于 $s\ge5$，在 $a^2$ 系数中只有
$v_4$ 和 $-2v_2^2$ 贡献，分别为 $2/(D_2D_4)$、$-2/D_2^2$。
因此

$$[a^2y^4]w=\frac{2(D_2-D_4)}{D_2^2D_4}.$$

将五分母精确值
$\mathrm{lo}=(5-\sqrt5)/2$、$\mathrm{hi}=(5+\sqrt5)/2$ 代入，
两代表为 $(D_2,D_4)=(\mathrm{hi},\mathrm{lo})$ 和
$(\mathrm{lo},\mathrm{hi})$，分别化简为

$$\frac{\sqrt5-1}{5},\qquad-\frac{\sqrt5+1}{5}.$$

两者非零且异号。该阶位于 $s=5$ 的共振规范之前，不能由 Step 5 的规范变化消除。
所以作者所否定的 $w=w_0+a w_1$ 身份确实失败。$\square$

## Independent finite exact self-check

本次只在标准输入运行临时精确 SymPy 运算，不写脚本或结果文件、不求根。
与作者所附直接迭代反演不同，自验使用 Lagrange 公式生成逆函数射流。
选 $s=3$，但保留 **自由参数** $a$ 与自由共振规范 $c$：

$$v(t)=\frac t3+\left(\frac a3+\frac19\right)t^2+ct^3,$$

计算 $Y,T,\mathcal G$ 到四阶，并检查：

1. $Y(T(y))=y+O(y^5)$；
2. $\mathcal G^{\circ3}=\mathrm{id}+O(y^5)$；
3. $\widetilde T\circ\mathcal G=\zeta\widetilde T+O(y^5)$；
4. 对数式到三阶恰为
   $-y-ay^2+(a+1/6)y^3$；
5. $\mathcal G$ 的四阶射流对 $c$ 的导数为零。

另用抽象 $v_1,v_2,v_3,v_4$ 核对 Step 6 的四阶公式及五分母两值。
全部检查严格化简为零，程序输出两组精确通过标志。
这是有限身份自验，不是新的根样本或全分母数值证据。

## Corrections or Missing Assumptions

未发现需修正的作者结论。解析循环芽的**复合阶恒等式**与
其对数方程的**有限射流条件**必须继续区分；被审稿已经正确区分。
同样，该复杂芽条件不是原实辛映射的可积性、实际不变曲线或全阶正规化定理。

## Open Risks

所得反函数系数与循环芽条件未给出 $a$ 的实解个数、交错性或重数。
参数非线性障碍也不是 $C$ 的非实根反例。
本次仅接受上述精确规约与指定身份反证，不接受全实根问题已完成的推论。
没有评价其他作者的 envelope／Ward／$Q$ 共同根稿，
没有容量、PDF、正式候选票或项目状态变更。
