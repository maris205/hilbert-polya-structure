# Paper30 qPI：一般 tame-block 完整首 jet 独立核查 V1

日期：2026-09-09。类型：有界非作者证明核查与独立有限精确排错。
唯一写入对象是本报告；不修改作者件、索引、此前冻结产物。

## Claim

固定奇素数 $p$、$m\ge1$ 且 $p\nmid m$，有限剩余域 $k$ 中精确 $m$ 阶元 $\eta$。
令 $\widetilde\eta$ 为无分歧 $p$-进系数环内的唯一 $m$ 阶提升，
$\mathcal O_a$ 为添入 $\zeta_{p^a}$ 后的圆分 DVR。
系数环和允许的完成／有限无分歧扩张保持作者原范围；不另作有分歧基变换。
令 $a\ge2$，
$$N=p^a,\qquad \sigma=1+p+\cdots+p^{a-1},\qquad \ell=\sigma-1,$$
$$q_a=\zeta_{p^a},\quad \pi_a=q_a-1,\quad
s_a=\widetilde\eta q_a,\quad t_a\in\mathcal O_a^\times.$$
原八截面模型取参数 $q=s_a,\tau=t_a$，不另换谱矩阵或能级规范。
原一形式的归一化是
$$\alpha_{mN}=N^{-1}d_{\rm state}I_{mN,s_a},$$
不是 $(mN)^{-1}dI_{mN,s_a}$；除法先在特征零中完成。

通过指定参数同构将首层和第 $a$ 层的二阶商识别为
$$B=k[\epsilon]/(\epsilon^2),\qquad \pi_1,\pi_a\longmapsto\epsilon,$$
并使首层时间 $t_1$ 与 $t_a$ 在 $B$ 上相同。
这给同一完整开放模型 $\mathcal U_B$，共同剩余曲面记为 $U_0$。
在 $U_0$ 上定义
$$T=\bar t_a^m,\qquad J=I_{m,\eta}(x,y;\bar t_a),\qquad
\varepsilon_m=(-1)^{m+1},$$
$$f(Z)=(T+JZ+Z^2)^2-4\varepsilon_m Z^3,\qquad
H=[Z^{p-1}]f(Z)^{(p-1)/2}.$$
$J,H$ 为原 $U_0$ 上的正则函数。
因 $p\mid\ell$，$H$ 的任意局部提升的 $\ell$ 次幂粘成同一全局函数，
记为 $H^{\langle\ell\rangle}$。

所核查的原结论为
$$\boxed{\quad
\alpha_{mp^a}^{[2]}=
H^{\langle\ell\rangle}\alpha_{mp}^{[2]}
\quad\text{于 }\Gamma(\mathcal U_B,\Omega^1_{\mathcal U_B/B}).
\quad}$$
这包含环面及全部四条末端线，并比较完整两状态一形式，而非切向商类。
作者附带的 $a=1$ 情形仅为乘数一的恒等边界，也正确。

## Status

**PROVABLE AS STATED / PASS（严格限于模 $\pi^2$）。**

接受 TB.1 与 TB.2。未发现硬缺口；原指数、归一化及时间提升条件无须修改。
本轮是非作者检查，不是 fresh-eyes 检查：核查者曾参与本方向查新及此前有限审查，
但未参与本作者件编写，也未读取其他新评审结论。
本轮接受不包含一般 $m$ 的首层单位配对、系数理想、局部厚度或更高 jet。
proof-writer 用于分离准确 Claim、输入身份、全称证明、实际测试和未完成范围；
未使用 Route A/B 评价。

## Assumptions and Actual Read Boundary

作者主件全文读 1–335 行、20,679 字节：
[TAME_BLOCK_FIRST_JET_LEMMA_V1](PAPER30_QPI_VERTICAL_ALPHA_TAME_BLOCK_FIRST_JET_LEMMA_V1_20260909.md)。
其冻结 SHA-256 为
6546720ecf39f667f09d45235dc0c7be340032b4c3f7c809e9d1cb60257396e9。

仅追加阅读实际依赖的定义／证明段；下表中的行数不是虚称全文范围。

| 依赖输入 | 本轮实际读取范围 | 使用边界 |
|---|---|---|
| [GLOBAL_FIRST_JET_FACTORISATION_V1](PAPER30_QPI_VERTICAL_ALPHA_GLOBAL_FIRST_JET_FACTORISATION_V1_20260909.md) | 87–118、134–146 行 | 二阶商、提升幂粘合、末端图限制单射；未消费首层理想部分 |
| [FIRST_JET_MATRIX_LEMMA_V1](PAPER30_QPI_VERTICAL_ALPHA_FIRST_JET_MATRIX_LEMMA_V1_20260909.md) | 1–43、86–164、180–238 行 | 普适带权交换子、降序正号、先除后约化与实际时间；未以其 $m=1$ 结果替代一般块证明 |
| [整数 brief V1](PAPER30_QPI_INTEGRAL_CANDIDATE_BRIEF_V1_20260909.md) | 32–85、123–192 行 | 原矩阵、八中心、小阶迹／行列式及 D/G 消费接口；不重审无关上同调结论 |
| [原整除诊断 D](PAPER30_QPI_CYCLOTOMIC_DIFFERENTIAL_DIAGNOSTIC_V1_20260909.md) | 8–53、101–193 行 | 原对象、循环插入、秩二迹递推与标量 Frobenius |
| [原完整模型 G](PAPER30_QPI_CYCLOTOMIC_GLOBAL_MODEL_DIAGNOSTIC_V1_20260909.md) | 7–63、83–149、222–234 行 | 单位时间下同一八中心、光滑图、原正则函数及整除一形式的全端延拓 |

对应输入 SHA-256：

- GLOBAL_FIRST_JET_FACTORISATION_V1：
  9d53bee5abf8026dfa09d2bcb38713e0ace28ff082d9e87b3efa595ab5955a86。
- FIRST_JET_MATRIX_LEMMA_V1：
  f3618fa1345804ce5d93acae4e6fdb2b3ee7761a87ae2de8bc453d24944971bd。
- 整数 brief V1：
  59f21705782443e9ac57aeb0f62c80f198f7fd18cec1a5ad3e496f0cf2f71f13。
- 原整除诊断 D：
  e2f032ff1197d415be611670e3d233efd7f6ead0d7dbe16b05f796ed42f43652。
- 原完整模型 G：
  59b308f605832d82e00720c5a3a7871c862698e194503ff3b289da592ced28e0。

未阅读其他新独立检查、一般首层 Čech 接口或一般 $m$ 的配对结论。
未把已核查的 $m=1$ 理想、此前有限 $N=9$ 点值或任何普通性假设作为本证明前提。
四个并行槽在开始时均已占用，本轮未另委派重叠文件的写入。

## Notation

小写 $z$ 是原谱变量；大写 $Z$ 在共振投影后代替 $z^m$。
状态微分 $d$ 固定 $B,t,s,z$，在原环面为自由模
$R\,dx\oplus R\,dy$，其中 $R=B[x^{\pm1},y^{\pm1}]$。
$[M,X]=MX-XM$；各迹表达式中只有一个一形式值因子，不涉及两个一形式相乘。
定义
$$\mathcal P_m\left(\sum b_i z^i\right)=\sum b_{mj}Z^j.$$
它不保持任意乘积；本轮只用
$$\mathcal P_m(Q(z^m)P(z))=Q(Z)\mathcal P_m(P(z)).$$
所有高层结论均只在 $\epsilon^2=0$ 内；不把平方零误差控制用于三阶商。

## Proof Strategy and Dependency Map

1. 从实际原乘积重新分出 $N$ 个 tame 块，核查除以 $N$ 的整数公式。
2. 保留全部块内扰动及实际时间，确定共振三项式和行列式。
3. 在平方零环中证明合法投影，再用秩二递推和次数界计算内部项。
4. 对完整剩余块应用普适交换子恒等式，证明一般 $m$ 的真实支持界。
5. 对允许到 $2p-1$ 的低位区间重新证明数字唯一性，比较完整两状态形式。
6. 通过共同八中心模型、提升幂粘合和模局部化单射跨过四条末端线。

## Proof

### Step 1. 原矩阵、整数块归一化和共同商

将 $u=x(y-1),v=y-1$ 代入作者紧凑矩阵，逐项恢复 brief 的原 $A_0,A_1$；
两种写法没有新的独立 $q$ 系数依赖。独立精确有理计算也核得
$$\det A(z;t)=z^3,\qquad [z^2]A=E=\operatorname{diag}(1,0),\qquad dE=0.$$
令
$$\mathsf B_s(z)=A(s^{m-1}z)\cdots A(sz)A(z),\qquad r=s^m.$$
第 $j$ 块为 $\mathsf B_s(r^jz)$，其中的原因子指数是
$mj+m-1,\ldots,mj$；故块分解保持全部 $mN$ 个原因子的降序。

在特征零对迹微分，按 $N$ 个块相加。
把第 $j$ 个块插入循环移到迹的首位并令 $w=r^jz$，
剩余块仍降序为 $r^{N-1},\ldots,r$。
系数 $[z^{mN}]$ 的缩放因子为 $r^{jmN}=1$，所以已有整系数等式
$$dI_{mN,s}=N[z^{mN}]
\operatorname{tr}\left(d\mathsf B_s(z)
\mathsf B_s(r^{N-1}z)\cdots\mathsf B_s(rz)\right).$$
除以 $N$ 后右端仍整，才可约化。
$d\mathsf B_s$ 是块内 $m$ 项的完整导数和，因此不遗漏 $m$，也不额外再乘 $m$。
与单原因子归一化的等价表示是
$$\alpha_{mN}
=m[z^{mN}]\operatorname{tr}\left(dA(z)A(s^{mN-1}z)\cdots A(sz)\right).$$
后式中的 $m$ 是原 $dI_{mN}/N$ 定义带来的；它不改变块公式。

奇素数条件给 $v_{\pi_i}(p)=p^{i-1}(p-1)\ge2$，故两个二阶商特征均为 $p$。
有限剩余域 $k=\mathbb F_{p^f}$ 通过 $X^{p^f}-X$ 的唯一根提升成为商环中的系数域：
导数为 $-1$，故平方零误差可唯一修正，根在加法、乘法下封闭。
每个商元唯一写为 $c_0+c_1\pi_i$，从而有声明的共同 $B$。
唯一 tame 根在该系数域中是 $\eta$，所以
$$s=\eta(1+\epsilon),\qquad r=s^m=1+m\epsilon.$$
这是指定的一阶参数同构，不是自然分歧嵌入
$\zeta_p\mapsto\zeta_{p^a}^{p^{a-1}}$。
首层时间可由商映射满射选取；非零剩余保证其为单位。

### Step 2. 块内扰动不能删除

在 $R$ 内保持实际 $t=t_0+\epsilon t_{\rm lin}$，其中 $t_0,t_{\rm lin}\in k$；
$t_{\rm lin}$ 是时间的一阶系数，不与首层 DVR 中的提升 $t_1$ 混同。
逐因子 Taylor 展开给
$$\mathsf B_s=\mathsf B_\eta(z;t)+\epsilon C,\qquad
C=\sum_{j=0}^{m-1}j\,\mathsf A_{m-1}\cdots\mathsf A_{j+1}
(z\partial_z\mathsf A_j)\mathsf A_{j-1}\cdots\mathsf A_0,$$
其中 $\mathsf A_j=A(\eta^jz;t)$。
$C$ 可只取剩余值，但不能把 $\mathsf B_\eta(z;t)$ 中的实际时间换成 $t_0$。
小阶迹恒等式先在不定时间的 $k(t)$ 中使用，再作为 Laurent 多项式恒等式代入 $t\in B^\times$，
所以非约化系数环不会导致该输入失效：
$$\operatorname{tr}\mathsf B_\eta=t^m+I_{m,\eta}(x,y;t)z^m+z^{2m}.$$

令 $S_s=\operatorname{tr}\mathsf B_s,D_s=\det\mathsf B_s$。
最低谱系数由 $A(0)^m=t^{m-1}A(0)$ 给出；最高系数由 $E^m=E$ 给出；行列式逐因子相乘。
因此
$$[z^0]S_s=t^m,\quad [z^{2m}]\mathsf B_s=s^{m(m-1)}E,\quad
D_s=s^{3m(m-1)/2}z^{3m},\quad dD_s=0.$$
置
$$j_*=[z^m]S_s,\quad c_s=s^{m(m-1)},\quad d_s=s^{3m(m-1)/2},$$
$$S_*(Z)=t^m+j_*Z+c_sZ^2,\qquad D_*(Z)=d_sZ^3.$$
则 $\mathcal P_m S_s=S_*$、$D_s=D_*(z^m)$、$dS_*=Z\,dj_*$。
精确一阶系数是
$$c_s=1+\epsilon m(m-1),\qquad
d_s=\varepsilon_m\left(1+\epsilon\frac{3m(m-1)}2\right).$$
奇 $m$ 时 tame 行列式因子为一；偶 $m$ 时 $\eta^{m/2}=-1$，
且指数 $3(m-1)$ 为奇数，故 tame 因子为负一。
这些式子含 $m=1$ 和 $p=3$，其中模 $p$ 为零的整数系数按其实际剩余解释。

### Step 3. 平方零共振投影与内部项

非共振部分确为一阶扰动，可选择 $V$ 使
$$S_s(z)=S_*(z^m)+\epsilon V(z),\qquad \mathcal P_mV=0.$$
对任意多项式 $\Phi(S,D)$，展开 $\Phi(S_s,D_s)dS_s$，
除共振主项外仅剩
$$\epsilon\Phi_S(S_*,D_*)V\,dS_*+
\epsilon\Phi(S_*,D_*)dV,$$
这里共振因子均在 $z^m$ 处评价。
$\mathcal P_mV=\mathcal P_m(dV)=0$，利用投影的上述模线性性质，两项均被杀掉。
$V\,dV$ 项带 $\epsilon^2$ 才消失，不能由“投影是乘法同态”这样的错误理由删除。
故作者式 (9) 是合法的完整一形式恒等式，同时保留 $j_*,c_s,d_s$。

秩二 Cayley–Hamilton 和 $d\det M=\operatorname{tr}(\operatorname{adj}M\,dM)$ 给整系数递推
$$\operatorname{tr}(dM\,M^{N-1})
=U_{N-1}(S,D)dS-U_{N-2}(S,D)dD.$$
这里 $U_{-1}=0,U_0=1$，且 $U_n=SU_{n-1}-DU_{n-2}$。
在特征 $p$ 中，通用对称多项式嵌入给
$$U_{N-1}(S,D)=(S^2-4D)^{(N-1)/2}.$$
证明在形式根 $b,c$ 中使用 $(b^N-c^N)/(b-c)=(b-c)^{N-1}$ 的多项式表达，
再由对称多项式环的单射下降；不对实际矩阵作对角化，也不除其判别式。
取
$$f_*=S_*^2-4D_*,\qquad H_*=[Z^{p-1}]f_*^{(p-1)/2},$$
内部项于是为
$$F_N=[z^{mN}]\operatorname{tr}(d\mathsf B_s\,\mathsf B_s^{N-1})
=[Z^{N-1}]f_*^{(N-1)/2}\,dj_*.$$
$\deg f_*\le4$，故 $Q_*=f_*^{(p-1)/2}$ 支持在 $[0,2p-2]$。
Frobenius 展开成 $\prod_{i=0}^{a-1}Q_*^{p^i}$；
要得到次数 $p^a-1$，最低位只能为 $p-1$，去掉该位并除以 $p$ 后重复，
所以所有位均为 $p-1$。
结论是
$$F_N=H_*^\sigma dj_*,\qquad F_p=H_*dj_*.$$
仅标量多项式取 Frobenius 幂，一形式 $dj_*$ 始终线性出现。
因 $H_*\bmod\epsilon=H$ 及 $p\mid\ell$，$H_*^\ell$ 与 $H$ 的任意提升的 $\ell$ 次幂相同。
内部项已经按所需乘数比较；时间提升作用于 $j_*$ 及 $dj_*$ 的部分没有遗漏。

### Step 4. 外部缩放、正号与一般 $m$ 的支持

令 $\mathsf B_0=\mathsf B_\eta(z;t_0)$。
外部缩放的完整展开是
$$\mathsf B_s(r^jz)=\mathsf B_s(z)+\epsilon mj\,z\partial_z\mathsf B_0.$$
外部项已带 $\epsilon$，所以其余块及微分插入只取剩余值；内部变化已全部计入 $F_N$。
对任何二阶矩阵 $M,X$，
$$\sum_{j=1}^{N-1}jM^{N-1-j}XM^{j-1}
=\Delta_M^{(N-3)/2}[M,X],\qquad
\Delta_M=(\operatorname{tr}M)^2-4\det M.$$
实读矩阵引理的证明通过左右乘算子将左端化为 $\operatorname{ad}_M^{N-2}(X)$，
再用整系数恒等式 $\operatorname{ad}_M^3=\Delta_M\operatorname{ad}_M$。
形式求导中的 $-(N-1)=1$ 给正号；降序位置恰为左边 $N-1-j$、右边 $j-1$ 个矩阵。
这在含零因子或判别式为零时仍成立，$p=3,N=3$ 的零指数也合法。

定义
$$\Gamma_m=\operatorname{tr}\left(d\mathsf B_0
[\mathsf B_0,z\partial_z\mathsf B_0]\right),\qquad
\gamma_m=\mathcal P_m\Gamma_m.$$
因为 $\Delta_{\mathsf B_0}=f(z^m)$，得到
$$\alpha_{mN}^{[2]}=F_N+\epsilon m\beta_N,\qquad
\beta_N=[Z^N]\gamma_m(Z)f(Z)^{(N-3)/2}.$$
这里 $\beta_N$ 只是外部缩放项，不是完整的一阶系数。

真实剩余块的最高矩阵系数是 $E$，故 $\deg d\mathsf B_0\le2m-1$。
交换子的 $z^{4m}$ 系数为 $[E,2mE]=0$，故其次数至多 $4m-1$；
常数项为零，因为 $z\partial_z\mathsf B_0$ 没有常数项。
因此
$$\operatorname{supp}_z\Gamma_m\subset[1,6m-2],\qquad
\operatorname{supp}_Z\gamma_m\subset
\begin{cases}[1,4],&m=1,\\[1,5],&m\ge2.\end{cases}$$
本证明实际使用一般 $m$ 的界，并未继承 $m=1$ 的四次界。
独立原矩阵计算还在 $m=2,3,4$ 的样本中发现非零五次投影项，验证该区别不可删略。

### Step 5. 允许第五项后的数字唯一性与完整比较

令 $Q=f^{(p-1)/2}$、$G=\gamma_m f^{(p-3)/2}$。
上述界给
$$\operatorname{supp}Q\subset[0,2p-2],\qquad
\operatorname{supp}G\subset[1,2p-1].$$
$p=3$ 时 $G=\gamma_m$，同一界仍有效；不需额外删掉第五次项。
对 $a\ge2$，
$$\beta_N=[Z^{p^a}]G\prod_{i=1}^{a-1}Q^{p^i}.$$
可能贡献的谱次数满足
$$n_0+pn_1+\cdots+p^{a-1}n_{a-1}=p^a,$$
其中 $1\le n_0\le2p-1$，$0\le n_i\le2p-2$。
取模 $p$ 时唯一可能的 $n_0$ 是 $p$；
减去 $p$、除以 $p$ 后目标为 $p^{a-1}-1$，其各位只能取 $p-1$。
所以
$$\beta_N=\left(\prod_{i=1}^{a-1}H^{p^i}\right)\beta_p=H^\ell\beta_p.$$
必须保留系数的 Frobenius：有限域 $k$ 不一定等于 $\mathbb F_p$，不能把 $H^{p^i}$ 换成 $H$。

首层与高层的 $s,t,\mathsf B_s$ 在 $B$ 上相同，因此同一 $H_*,dj_*,\beta_p$ 给
$$\alpha_{mN}^{[2]}=H_*^\sigma dj_*+\epsilon mH^\ell\beta_p,\qquad
\alpha_{mp}^{[2]}=H_*dj_*+\epsilon m\beta_p.$$
由 $H_*^\ell=H^{\langle\ell\rangle}$，且乘 $\epsilon$ 后只使用乘数的剩余值，得到 TB.1。
外部速率的 $m$ 在两式中相同，不在最终比较中产生额外数值因子。
从始至终没有约去 $H$，所以其零点及谱退化状态均不必排除。

### Step 6. 全局乘数、模型识别与全部末端线

原 D/G 的八中心是四个不同边界分量上的单位坐标 $1,t,t,s$，并保持固定吹起顺序。
两层的这些参数在 $B$ 上完全相同；各步中心由相对坐标正则列描述，
标准吹起图、边界严格变换和所移去的八分量逐图相同。
这给真正的共同 $\mathcal U_B$，而非仅相同的剩余点集。
不需要援引任意非平坦基变换与吹起可交换的错误通则。
允许的完成和无分歧系数扩张不改上述图；原 G 的正则性证明所用的光滑、正常、
唯一竖直分量及局部自由微分接口仍适用。

局部提升之差为 $\epsilon h$，在特征 $p$ 中
$$(\widetilde H+\epsilon h)^p=\widetilde H^p.$$
再取 $\ell/p$ 次幂，证明提升幂在重叠处完全相等，粘成全局 $H^{\langle\ell\rangle}$。
无需原 $J$ 有全局整提升，也未假设 $H$ 是单位。
原 G3 和其 Step 6 提供两层实际 $\alpha$ 的全局正则性；因此所比较的差是
$\Omega^1_{\mathcal U_B/B}$ 的全局截面。

四个末端图分别可写为 $B[u,v]$ 在
$1+uv,t+uv,t+uv,s+uv$ 处的局部化，其环面部分进一步反演 $u$。
即使 $B$ 含平方零元，乘以多项式变量 $u$ 仍为单射，局部化后也保持；
微分模自由，故其到反演 $u$ 后的模的限制映射单射。
差已在环面为零，因而在每个完整末端图也为零。
这四图和环面覆盖 $\mathcal U_B$，故得 TB.2。
本论证没有把集合稠密当作模单射，也没有假定单独的 $\beta_p$ 已全局正则。证毕。

## Actual Independent Verification

所有下列测试均为本轮实际执行的内存代码，未导入作者计算函数，未新增脚本或数据文件。
独立有限计算只是排错；所有 $p,m,a$ 的接受责任仍由上述全称证明承担。

1. 精确符号核对原矩阵和作者紧凑矩阵逐项相同，并断言 $\det A(z)=z^3$；退出码零。
2. 在 $\mathbb Z[q]/(q^6+q^3+1)$ 中取 $s=-q,m=2,N=9,x=y=1,t=2$，
   独立传播完整 18 因子的点值及两个状态导数。
   原导数的目标系数全部可被九整除，并验证
   “完整微分除九”＝“原单因子插入乘二”＝“完整二因子块插入”。
   两个规范化系数在基 $1,q,\ldots,q^5$ 中分别为
   $$(70028,49384,-55776,47808,116480,37808),$$
   $$(91210,82770,9284,21980,-6440,-48208).$$
   这是特征零整系数核查，不是在特征三中反除九；退出码零。
3. 独立实现有限域双数系数运算，直接对原有理矩阵求两个状态导数，
   保留 $\epsilon\,dx,\epsilon\,dy$ 的时间交叉项，分别形成原单因子插入、完整块插入、
   无外部缩放的内部项和交换子外部项。
   下表六组全部逐个比较四个一形式系数并通过；同时核对块迹非共振项、最高矩阵导数、
   行列式、$H_*^\sigma dj_*$、$\epsilon m\beta_N$ 及两个层间因子分解。

| $k$；$(p,m,a)$ | $\eta$；$t$；$(x,y)$ | $H$；$H^\ell$ | 结果 |
|---|---|---|---|
| $\mathbb F_3$；$(3,2,2)$ | $-1$；$2+\epsilon$；$(1,2)$ | $0$；$0$ | PASS；首层仍有非零一阶分量 |
| $\mathbb F_5$；$(5,2,2)$ | $-1$；$1+2\epsilon$；$(2,3)$ | $2$；$2$ | PASS |
| $\mathbb F_7$；$(7,3,2)$ | $2$；$3+2\epsilon$；$(1,4)$ | $5$；$5$ | PASS |
| $\mathbb F_3$；$(3,2,3)$ | $-1$；$1+2\epsilon$；$(2,1)$ | $0$；$0$ | PASS；首层仍有非零一阶分量 |
| $\mathbb F_9,\ w^2=-1$；$(3,4,2)$ | $w$；$(1+w)+\epsilon(2+w)$；$(1+w,2+w)$ | $1+2w$；$1+w$ | PASS；乘数不是 $H$ |
| $\mathbb F_{25},\ w^2+w+1=0$；$(5,3,2)$ | $w$；$(2+w)+\epsilon(1+w)$；$(3+w,4+w)$ | $2+w$；$1+4w$ | PASS；乘数不是 $H$ |

两扩域定义多项式分别在 $\mathbb F_3,\mathbb F_5$ 不可约，
实际检查 $\eta$ 的精确阶为四和三。
后两组中 $H^p\ne H$，故排除了只在素域测试造成的 Frobenius 盲区。
各组实际出现非零块内非共振迹项；一般 $m$ 的五次投影项也确实非零。
这不表示已检查对应能级光滑性，不提供几何配对非消失或单位性证据。

4. 对 $p=3,5,7,11$、$a=1,2,3,4$ 穷举有限数字范围，
   内部目标的唯一组合均为 $(p-1,\ldots,p-1)$，
   外部目标均为 $(p,p-1,\ldots,p-1)$；允许的低位上界确为 $2p-1$。退出码零。
5. 首轮内存双数测试曾因本地多项式截断后仍遍历超上界索引而抛出 IndexError。
   仅修正该内存乘法循环的上界后重跑，六组最终全部通过；
   这不是作者件失败，也没有修改作者输入来适配测试。

## Corrections or Missing Assumptions

无须修改作者结论、增添 $m$ 的系数或补入普通性／判别式非零假设。
本报告重点补展开了三项审查理由，而非修改冻结证明：
非共振项只因平方零投影消失；一般 $m$ 的第五项仍允许数字唯一；
非约化全端延拓必须用自由模的局部化单射。
原 D/G 正则模型接口继续作为明确输入，不在本轮重开已接受的全局几何和 Jacobian 身份。

## Open Risks and Explicit Nonclaims

- 不声称一般 $m$ 的首层系数理想为 $(\pi,H)$，不预设或证明任何首层单位配对。
- 不计算完整初始理想、准确非零厚度、局部长度、高阶 $\pi$ 递推或完整零概形。
- 不将二阶商恒等式解释为圆分 DVR 之间的自然分歧嵌入恒等式。
- 不用 $m=1$ 的证明、数值样本、普通能级或光滑谱状态替代一般 tame-block 的代数证明。
- 不把退化谱状态改称超奇异；本恒等式未新增几何非消失结论。
- 不扩展到 $p=2$、非单位时间或额外有分歧基变换。
- 未评分、立项、修改锁、写稿、编译或进行任何对外发布。

## Artifact State

本轮唯一新增持久化产物是本报告；无第二脚本、无 GPU。
作者主件及本轮实读的五项依赖均保持冻结身份。
最终行数、字节数、报告 SHA-256 和输入未变的复核结果在交接中提供。
最终接受：TB.1 与 TB.2 按原模 $\pi^2$ 量词成立，无待修硬缺口。
