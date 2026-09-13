# Paper30 qPI：圆分降阶整除微分 D1–D3 非作者数学检查 V1

日期：2026-09-09。检查者：`/root/p30_qpi_cyclotomic_diff_check_v1`，Codex AI；不是作者 `/root`。
类型：独立、有界的数学证明检查；不是四门票、查新、Route A/B 评分或论文准入。
输入作者稿未改动；本报告是检查者唯一新建文件。

## 1. Claim：准确受审主张与输入身份

受审对象是 [作者诊断 V1](PAPER30_QPI_CYCLOTOMIC_DIFFERENTIAL_DIAGNOSTIC_V1_20260909.md) 的 D1–D3，
包括其全部量词、相对微分规范、准确全局赋值及含重数理想结论。
固定矩阵、原积分、迹／行列式／Laurent 首项采用
[brief V2 §2](PAPER30_QPI_CANDIDATE_BRIEF_V2_20260909.md) 的已接受输入；
光滑原能级与实际临界位置采用该 brief 的 T1–T3。
没有重新审查旧九对数学模块、47 件共同输入或旧评分。

| 输入 | SHA-256 |
|---|---|
| 作者诊断 V1，268 行 | `e2f032ff1197d415be611670e3d233efd7f6ead0d7dbe16b05f796ed42f43652` |
| 固定 brief V2，550 行 | `b8f1ca66927b977b05a2996e42d299390d6a895d1a3378119d1be5415d70a00f` |

两个哈希均在初读后及建立本报告前复核一致。
实际阅读范围如下；“读取依赖的声明”不冒充重新核验其全部旧证明。

- 作者诊断 V1：第 1–268 行，全文，包括 §5 动力学边界与 §6 来源声明。
- brief V2：实际读取第 1–260 行；本次核心使用 §2 第 35–112 行及 T1–T3 第 121–186 行。
- `docs/WORKFLOW.md` 与 `/root/autodl-tmp/.codex/skills/proof-writer/SKILL.md`：全文。
  proof-writer 用于明确假设、独立重推、边界检查与如实分类，不触发论文修改。
- `BATCH_07_CONTEXT.md`：第 1–230 行用于定位；旧算术段不是本次数学输入。
- [Achter–Howe 作者 v5](https://arxiv.org/html/1710.10726v5)：实际读取并使用 §§1.2–1.3、2.2–2.4、3.1 的半线性、伴随、Cartier 定义和奇特征公式；未声称通读论文。
- [Voloch 1990](https://www.numdam.org/article/CM_1990__74_3_247_0.pdf)：实际读取公开 PDF 的 Conventions and notation（印刷页 247–248）的文本提取，使用印刷页 248 对指定微分的 Hasse 规范和普通／超奇异区分；未声称通读其下降论证或完成该 PDF 的视觉验收。

外部来源的使用仅为标准工具核准，不是查新或全球先例排除。

## 2. Status

**PROVABLE AS STATED。D1、D2、D3 数学 PASS；没有发现必须修改的作者字节错误或新增量词条件。**

该判断消费上述明确的已接受对象输入与标准 Cartier／椭圆曲线事实。
它不表示本轮独立重证 T1–T3，也不将正确性转换为独立论文价值、新意分数或页数结论。

| 主张／脆弱接口 | 判断 | 核验所得 |
|---|---|---|
| 剩余根单位阶准确为 $m$ | PASS | 圆分约化与 $X^m-1$ 可分性闭合 |
| D1 | PASS | 重复矩阵块与迹的 Frobenius |
| 循环插入顺序 | PASS | 只循环迹，不交换矩阵；移位指数准确 |
| $N^{-1}dI_r$ 整性 | PASS | 先证明特征零中 $dI_r=r[z^r]Q_r$ |
| 降阶后的插入位置与因子 $m$ | PASS | 恰求和 $m$ 个插入，不除以剩余为零的 $N$ |
| Cayley–Hamilton 系数 | PASS | 正确系数是 $U_{N-1}dS-U_{N-2}dD$ |
| Hasse 数字提取 | PASS | 支撑上界 $2p-2$ 排除进位替代项 |
| $p=2$、$p=3$、$m=1$、全部 $a\ge1$ | PASS | 证明均覆盖；小特征显式核对见下 |
| 相对微分 | PASS | 固定 $t,s,z$；确有 $dD=0$、$dT=0$ |
| 非零性与全局最小赋值 $ae$ | PASS | 另有原 Laurent 首项的直接独立交叉证明 |
| D3 全环系数理想 | PASS | 两个分量的精确乘积理想，不仅根集 |
| 光滑层 Hasse 解释及重数 | PASS | 固定微分的 Cartier 系数准确，光滑层临界理想为单位理想 |

## 3. Assumptions 与 Notation

取任意素数 $p$，整数 $a,m\ge1$ 且 $p\nmid m$；设
$$N=p^a,\qquad r=mN,\qquad s=\zeta_r,\qquad L=\frac{N-1}{p-1}.$$
设 $\mathcal O=\mathbb Z[\zeta_r]_{\mathfrak p}$，其中 $\mathfrak p\mid p$；
取参数 $\pi$、剩余域 $\kappa$、$e=v_\pi(p)$，并设 $\eta=\bar s$。
圆分整数环在非零素点的局部化是特征零 DVR；这里不另假设 $p$ 为奇数。

设
$$\mathcal B=\mathcal O[t^{\pm1},x^{\pm1},y^{\pm1}],\qquad
\Omega=\Omega^1_{\mathcal B/\mathcal O[t^{\pm1}]}=\mathcal B\,dx\oplus\mathcal B\,dy.$$
约化状态环记为 $R=\kappa[t^{\pm1},x^{\pm1},y^{\pm1}]$，其相对微分模为 $\bar\Omega$。
相对微分 $d$ 只作用于 $x,y$；谱变量及底参数不参与微分。
在剩余环写 $T=t^m$、$J=I_{m,\eta}$、$\varepsilon=(-1)^{m+1}$。

固定来源输入为作者 §1／brief §2 的实际 $A(z)$，及
$$M_{n,\xi}=A(\xi^{n-1}z)\cdots A(z),\qquad
\operatorname{tr}M_{n,\xi}=t^n+I_{n,\xi}z^n+z^{2n},$$
$$\det M_{n,\xi}=(-1)^{n+1}z^{3n},\qquad
I_{n,\xi}=-t^nx^{-n}+O(x^{-n+1}).$$
它们分别用于特征零的 $(r,s)$ 和剩余特征的 $(m,\eta)$。
原光滑能级声明仅在最后将 $(J_x,J_y)$ 限制为单位理想时调用。

受审结论准确为
$$\bar I_r=J^N,\qquad
\alpha_r=N^{-1}dI_r\in\Omega,\qquad
\bar\alpha_r=H_p(T,J;\varepsilon)^L dJ,$$
以及原稿的 Hasse 多项式定义、非零性、最小系数赋值 $ae$ 和
$$\operatorname{coeffideal}(\bar\alpha_r)
=(H_p(T,J;\varepsilon)^L)(J_x,J_y).$$
这里的整除是 $\pi$-进统一整除；不是关于某个闭点取值的统一等式。

## 4. Proof Strategy 与 Dependency Map

本次重推不从 $d(J^N)=0$ 推测首项，而保留完整乘积中的一个导数插入。

1. 圆分约化确定 $m$ 阶重复块，从而证明 D1。
2. 特征零循环迹证明 $r$ 整除，再将已整表达式约化为长度 $m$ 的导数求和。
3. 无需矩阵可逆的 Cayley–Hamilton 恒等式，将其化为一个精确系数提取。
4. 对称多项式恒等式与唯一数字展开给出 Hasse 的第 $L$ 次幂。
5. 原 Laurent 首项独立钉住全局赋值；该步骤不依赖逐点数值。
6. 两张谱曲线图验证指定微分，再核准 Cartier 规范。
7. 由分量理想的精确相等取得 D3；只有光滑层简化消费 T1–T3。

## 5. Proof：独立重推

### Step 1. 剩余阶与 D1

在 $p\nmid m$ 时，圆分恒等式约化给
$$\bar\Phi_{mp^a}(X)=\bar\Phi_m(X)^{p^{a-1}(p-1)}.$$
由于 $X^m-1$ 在特征 $p$ 可分，其不同圆分因子的根不相交，
所以 $\bar\Phi_m$ 的根的阶恰为 $m$，不是只知道该阶整除 $m$。
于是
$$\overline{M_{r,s}}=B^N,\qquad B=M_{m,\eta}.$$
通用两个特征根 $u,v$ 满足 $u^N+v^N=(u+v)^N$。
经对称多项式恒等式下降，这给任意特征 $p$ 交换系数环中的
$\operatorname{tr}(B^N)=(\operatorname{tr}B)^N$，不要求可对角化。
比较 $z^{mN}$ 的系数得 $\bar I_r=J^N$。
此处只有函数的纯不可分复合，不说明任何一阶微分信息。

### Step 2. 循环插入及合法整除

暂记 $A_j=A(s^jz)$，并设
$$Q_r(z)=\operatorname{tr}(dA_0A_{r-1}\cdots A_1).$$
第 $j$ 个因子的导数项，经循环迹成为
$$\operatorname{tr}(dA_j A_{j-1}\cdots A_0 A_{r-1}\cdots A_{j+1}).$$
令 $w=s^jz$，余下的相对指数依次为
$$-1,-2,\ldots,-j,r-1-j,\ldots,1\pmod r,$$
即准确的 $r-1,r-2,\ldots,1$ 次序。因此该项等于 $Q_r(s^jz)$。
其余因子为零形式；循环迹不产生微分符号，也没有交换非交换矩阵。
因为 $s^{jr}=1$，所有插入项的 $z^r$ 系数相等，故
$$dI_r=r[z^r]Q_r(z).$$
$Q_r\in\Omega[z]$，且 $\Omega$ 无 $\mathcal O$-挠元，故在特征零分式模中定义的
$$N^{-1}dI_r=m[z^r]Q_r\in\Omega$$
已得到合法的整代表。此后才作模 $\pi$ 约化；从未在特征 $p$ 除以 $N$ 或 $r$。

### Step 3. 重复块与 $m$ 次求和

现在 $A_j=A(\eta^jz)$，令
$$C_j=A_{m-1}\cdots A_{j+1}\,dA_j\,A_{j-1}\cdots A_0,
\qquad dB=\sum_{j=0}^{m-1}C_j.$$
循环移回后，已约化整代表为
$$\bar\alpha_r=m[z^{mN}]\operatorname{tr}(B^{N-1}C_0).$$
$\operatorname{tr}(B^{N-1}C_j)$ 是完整长度 $mN$ 乘积在最右一块内第 $j$ 个位置的导数插入。
上一步同一循环计算及 $\eta^{jmN}=1$ 证明其目标系数与 $j=0$ 相同。
恰相加这 $m$ 项可得
$$\bar\alpha_r=[z^{mN}]\operatorname{tr}(B^{N-1}dB). \tag{A}$$
没有相加 $N$ 个重复块再非法消去 $N$；$m=1$ 时空乘积约定使式子原样成立。

### Step 4. Cayley–Hamilton 与相对微分

设 $S=\operatorname{tr}B$、$D=\det B$，并取 $U_{-1}=0,U_0=1$、
$U_n=SU_{n-1}-DU_{n-2}$。对 $N\ge2$，
$$B^{N-1}=U_{N-2}B-DU_{N-3}\operatorname{id}.$$
又由 $\operatorname{adj}(B)=S\operatorname{id}-B$ 和行列式的多项式微分公式，
$$dD=S\,dS-\operatorname{tr}(B\,dB).$$
代入即得
$$\operatorname{tr}(B^{N-1}dB)=U_{N-1}\,dS-U_{N-2}\,dD. \tag{B}$$
对于最小边界 $N=2$，上述只用已定义的 $U_{-1}$，给出 $S\,dS-dD$。
所有式子是多项式恒等式；没有隐藏的 $B^{-1}$ 或 $z\ne0$ 假设。

设 $Z=z^m$。在本题的相对微分模中，
$$S=T+JZ+Z^2,\qquad D=\varepsilon Z^3,\qquad dS=Z\,dJ,\quad dD=0.$$
于是 (A)、(B) 变为
$$\bar\alpha_r=[Z^{N-1}]U_{N-1}(T+JZ+Z^2,\varepsilon Z^3)\,dJ. \tag{C}$$
若改作关于 $t$ 的全微分，此处会出现 $dT$；作者没有作这种改换。

### Step 5. 对称恒等式和无进位歧义的系数提取

在多项式环中，
$$U_{N-1}(u+v,uv)=\sum_{j=0}^{N-1}u^{N-1-j}v^j
=\frac{u^N-v^N}{u-v}.$$
右侧表示左侧的多项式，不要求 $u-v$ 可逆。
在特征 $p$，该多项式为 $(u-v)^{N-1}$。
由 $\mathbb F_p[S,D]\hookrightarrow\mathbb F_p[u,v]$ 的单射，得
$$U_{N-1}(S,D)=
\begin{cases}(S^2-4D)^{(N-1)/2},&p\ne2,\\ S^{N-1},&p=2.\end{cases}$$

奇特征令 $f=((T+hZ+Z^2)^2-4\varepsilon Z^3)^{(p-1)/2}$，其次数为至多 $2p-2$。
由于 $(N-1)/(p-1)=\sum_{i=0}^{a-1}p^i$，目标多项式为 $\prod_i f^{p^i}$。
若 $\sum_i n_i p^i=p^a-1$ 且 $0\le n_i\le2p-2$，模 $p$ 强制
$n_0\equiv p-1$。允许范围中唯一这样的整数为 $p-1$，因为下一项 $2p-1$ 已越界。
减去 $p-1$ 再除以 $p$，对剩余 $a-1$ 位重复，得每个 $n_i=p-1$。
因此目标系数恰是
$$\prod_{i=0}^{a-1}([Z^{p-1}]f)^{p^i}=H_p(T,h;\varepsilon)^L.$$
特征二取 $f=T+hZ+Z^2$；每位只允许 $0,1,2$，奇数位只能为 $1$，
同一论证给出 $h^{2^a-1}$，而 $L=2^a-1$。
代入 (C) 即证明 D2 的准确标量公式。

显式小特征核验为
$$H_2(T,h;\varepsilon)=h,\qquad H_3(T,h;\varepsilon)=h^2+2T=h^2-T.$$
所以 $p=2$ 时是 $J^{2^a-1}dJ$；$p=3$ 时是 $(J^2-T)^{(3^a-1)/2}dJ$。
没有任何“大 $p$”步骤，也没有在 $a=1$ 时丢失端点项。

### Step 6. 非零性与准确全局赋值：两条独立核准

奇特征的 $h^{p-1}$ 系数只有选取所有 $h^2Z^2$ 项这一种来源，故 $H_p$ 关于 $h$ 首一、次数 $p-1$；
特征二结论由 $H_2=h$ 给出。固定 $t$ 为单位后，
$$J=-T x^{-m}+O(x^{-m+1}),\qquad J_x=mT x^{-m-1}+O(x^{-m}).$$
由于 $p\nmid m$，$mT\ne0$。首一性又给出
$$H_p(T,J;\varepsilon)^L J_x
=mT^N x^{-mN-1}+O(x^{-mN}),$$
其中 $(-1)^{N-1}=1$ 在奇特征成立，在特征二也没有符号差异。
所以 $\bar\alpha_r\ne0$，证明作者的非零性论证有效。

另有不使用 Hasse 公式的直接核准：从特征零原首项得
$$dI_r=r t^r x^{-r-1}\,dx+\text{具有更高 }x\text{-次数的项}.$$
Step 2 已证明所有 $\alpha_r$ 系数整，且上述 $dx$ 系数除以 $N$ 后恰为 $m t^r$，是 $\pi$-单位。
于是以自由基 $dx,dy$ 和 Laurent 单项式展开，$\alpha_r$ 的全体系数的最小赋值准确为零，
$$\min v_\pi(\text{全部 }dI_r\text{ 的 Laurent 系数})=v_\pi(N)=ae.$$
任意 $\mathcal O$-单位 $t$ 的特化均保留该唯一首项，故不会因特化发生全局系数取消。
该结论不赋予每个状态点相同的取值赋值。

### Step 7. 指定谱微分与 Hasse 规范

固定几何参数 $T\ne0,h$，并假设谱曲线光滑。
可不用除以二而将原仿射曲线补为两张图：
$$F=\lambda^2-(T+hZ+Z^2)\lambda+\varepsilon Z^3=0,$$
$$G=\mu^2-(Tw^2+hw+1)\mu+\varepsilon w=0,
\qquad w=Z^{-1},\quad \mu=\lambda/Z^2.$$
它对 $\mathbb P^1$ 是有限平坦二重覆盖，直接像为
$\mathcal O_{\mathbb P^1}\oplus\mathcal O_{\mathbb P^1}(-2)$；故算术亏格为一且几何连通。
光滑时即几何整的亏格一曲线，且有 $(Z,\lambda)=(0,0)$ 这一有理点。

在有限图，指定微分为 $\omega=dZ/F_\lambda$，在 $F_Z$ 为单位处改写为 $-d\lambda/F_Z$。
光滑性保证至少一项偏导为单位，故这些表达式给出正则非零微分。
在无穷远图它为
$$\omega=-\frac{dw}{2\mu-(Tw^2+hw+1)}.$$
$w=0$ 时的两个点为 $\mu=0,1$，分母分别为 $-1,1$，在特征二也均为单位。
因此没有漏掉无穷远的零或极，也没有为特征二额外要求 $h\ne0$。

奇特征令 $Y=2\lambda-(T+hZ+Z^2)$。则 $Y^2=(T+hZ+Z^2)^2-4\varepsilon Z^3$，
且 $\omega=Y^{-p}Y^{p-1}dZ$。在完美底域上，Cartier 的
$\mathcal C(g^p\nu)=g\mathcal C(\nu)$ 及指数提取规则给出
$$\mathcal C(\omega)=H_p(T,h;\varepsilon)^{1/p}\omega.$$
因 $\deg(Y^{p-1})\le2p-2$，可贡献的指数只有 $p-1$。
特征二令 $S=T+hZ+Z^2$，则 $\omega=S^{-2}(T+hZ+Z^2)dZ$，直接得
$$\mathcal C(\omega)=h^{1/2}\omega.$$
这里 $Z$ 是可分变量：二次方程的 $\lambda$ 偏导不在函数域中恒为零，特征二时该偏导为非零多项式 $S$。
故使用 $Z$ 的 Cartier 系数提取合法，随后作为正则微分恒等式延拓。

在固定 $\omega$ 的平凡化下，Hasse 标量是 $H_p$，Cartier–Manin 一维矩阵是 $H_p^{1/p}$；
两者不混同。该规范与上述 [Achter–Howe §§2.2–2.4、3.1](https://arxiv.org/html/1710.10726v5)
及 [Voloch，p.248](https://www.numdam.org/article/CM_1990__74_3_247_0.pdf) 的标准定义一致。
不完美函数域上的统一结论用相对 Frobenius／Cartier 表示；完美基变换中出现的 $1/p$ 次方不要求原参数环包含这些根。
$H_p$ 本身是原参数环中的多项式，因而定义实际 Hasse 截面；基变换的精确标量公式并非只给零点集合。
对光滑亏格一曲线，Hasse 为零等价于超奇异；不将奇异曲线加入此术语。

### Step 8. D3 的概形与重数

在自由基 $dx,dy$ 中，已证明的等式是两个准确分量恒等式，故直接得到
$$\operatorname{coeffideal}(\bar\alpha_r)
=(H_p(T,J;\varepsilon)^L J_x,H_p(T,J;\varepsilon)^L J_y)
=(H_p(T,J;\varepsilon)^L)(J_x,J_y).$$
这一步对整个剩余环成立，不假设原能级光滑，亦不取根理想。
在原光滑能级开集，T1–T3 与光滑纤维的相对 Jacobian 判据给出
$(J_x,J_y)=R$ 的局部化等式。故那里零概形的理想恰为 $(H_p(T,J;\varepsilon)^L)$。
在以 $\omega$ 平凡化的谱族中，Hasse 零除子的拉回理想为 $(H_p(T,J;\varepsilon))$；
取第 $L$ 次幂准确地将其已有重数乘以 $L$。
不需要也未证明该 Hasse 多项式在每种参数特化下都无重根。
坏能级上仍保留完整乘积理想，不可换成两个根集的无重数并。至此 D1–D3 得证。

## 6. 实际精确代数检查与反例搜索

以下只是新构造的有限边界检查，不能替代上面的全量词证明。
本次使用 SymPy 在 $t=x=y=1$ 对作者实际矩阵及其 $x,y$ 偏导作特征零精确乘积，
在 $\mathbb Q[s]/(\Phi_r)$ 中逐步约简，先取 $z^r$ 系数并除以 $N$，
确认得到整数 $s$-系数，再在 $\mathbb F_p[s]/(\Phi_m)$ 中比较 D1 及 D2 两个分量。
后一个环可分但不必为域；其中相等同时覆盖其每个素因子，不把 $s$ 随意设为一。

| $(p,a,m)$ | $r$ | $\bar\alpha_r$ 的 $(dx,dy)$ 分量，位于该商环 | D1／已取值整性／D2 |
|---|---:|---|---|
| $(2,1,1)$ | 2 | $(0,0)$ | PASS |
| $(2,2,1)$ | 4 | $(0,0)$ | PASS |
| $(2,3,1)$ | 8 | $(0,0)$ | PASS |
| $(2,1,3)$ | 6 | $(s+1,0)$ | PASS |
| $(2,2,3)$ | 12 | $(1,0)$ | PASS |
| $(3,1,1)$ | 3 | $(-1,0)$ | PASS |
| $(3,2,1)$ | 9 | $(1,0)$ | PASS |
| $(3,1,2)$ | 6 | $(0,0)$ | PASS |
| $(5,1,1)$ | 5 | $(1,0)$ | PASS |
| $(5,1,2)$ | 10 | $(0,2)$ | PASS |

此外完整展开 $r=2,s=-1$ 得
$$I_2=-t^2/x^2+2t/y+2ty/x-x^2+2x^2/y-x^2/y^2-2xy+2x-y^2.$$
在 $t=x=y=1$，有
$$J=0,\qquad dJ=(1,0),\qquad \alpha_2=(0,-2),\qquad dI_2=(0,-4).$$
因此对 $p=2$，全局最小赋值为一，而这个点的实际微分赋值为二。
该点所属的剩余谱能级光滑：brief 的判别式在特征二、$T=1,h=0$ 取值为一。
这是一项对“每点同值”错误加强的真正反例，不是 D2 的反例，且与 $H_2=J=0$ 一致。

检查过程的一次草算预期被纠正：补充 $r=2$ 脚本曾未经推导预设取值分量为 $(-2,0)$，断言失败；
直接精确展开得到上述 $(0,-2)$。失败来自检查者的分量预设，不是作者公式；
该预设没有用于任何 PASS 判断。十组商环比较均独立通过。

## 7. Corrections or Missing Assumptions

没有发现需要作者修订的数学错误，也不需要添加 $p\ge5$、一般 $t$、$m>1$、$a>1$ 或普通能级等条件。
证明中已经给明的“相对微分”“先除后约化”“全局系数最小赋值”“仅在光滑层称超奇异”均不可删去。
本报告补写的双图／有限平坦覆盖说明和原首项赋值交叉证明是检查证据，不是对原主张的弱化或换题。

## 8. Open Risks 与结论边界

- D1–D3 中未发现未关闭数学缺口；这仍是非作者 AI 检查，不是人类或跨模型认证。
- 旧 JR 输入和 T1–T3 的已接受状态作为依赖消费，本轮没有重做九对或 47 件包，也没有声称其全部内容由本报告再次接受。
- 作者 §5 的重复时间块可直接给 $\bar{\mathcal R}_r=\mathcal R_m^N$ 于共同定义域。
  将其写成平移 $[N]P_m$ 仍明确依赖已有 torsor 动力身份；本次不新增该旧身份或全闭纤维延拓的审查结论。
- 超奇异层上 $\bar\alpha_r$ 消失，不推出任意状态提升的下一项精度、完整混合特征几何、野导子、消失循环或全部 ramified jets。
- 新意、最近包含关系、独立论文价值、自然正文容量、V3／立项和 Paper30 验收状态均不由本报告判定。

最终结论：**原 D1–D3 原样存活，全部 $p$（含 $2,3$）、$p\nmid m$、$a\ge1$ 数学 PASS。**
