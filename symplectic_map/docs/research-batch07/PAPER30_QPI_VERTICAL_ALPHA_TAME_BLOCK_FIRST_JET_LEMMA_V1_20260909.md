# qPI：保留 tame 块内变形的完整首 jet 因子分解 V1

日期：2026-09-09。作者：`/root/p30_qpi_post_integral_ideas_v1`。
类型：新的有界全称作者证明；不是非作者核查、正式候选或评分。
`route_applicability: NOT_APPLICABLE`。0 GPU；只新增本件，旧来源报告和所有旧证明冻结。
本人是首 jet 矩阵引理及数字分解引理的作者，不把本件算作这些输入的独立接受票。

## Claim

固定奇素数 $p$、整数 $m\ge1$ 且 $p\nmid m$，有限域 $k$ 中精确 $m$ 阶元 $\eta$。
取具有剩余域 $k$ 的无分歧 $p$-进系数环，令 $\widetilde\eta$ 为 $\eta$ 的唯一 $m$ 阶提升。
对 $a\ge1$，取其圆分扩张的 DVR $\mathcal O_a$，并置
$$N=p^a,\qquad \sigma=1+p+\cdots+p^{a-1},\qquad \ell=\sigma-1,$$
$$q_a=\zeta_{p^a},\qquad \pi_a=q_a-1,\qquad s_a=\widetilde\eta q_a.$$
允许完成及有限无分歧扩张，不另作有分歧再基变换。
相应未完成圆分局部 DVR 也在范围内：以下证明只使用其相同二阶商和原 D/G 正则模型接口。
固定任意单位时间 $t_a\in\mathcal O_a^\times$，使用原八截面模型
$\mathcal U_a$，参数为 $q=s_a,\tau=t_a$，原状态一形式为
$$\alpha_{mN}=N^{-1}d_{\rm state}I_{mN,s_a}.$$
除法先在特征零中作；原整除／完整模型接口保证它是全局正则相对一形式。

记 $B=\mathcal O_a/(\pi_a^2)$、$\epsilon=\pi_a\bmod\pi_a^2$。
将首层 $\mathcal O_1/(\pi_1^2)$ 与它识别为
$$B\simeq k[\epsilon]/(\epsilon^2),\qquad \pi_1\longmapsto\epsilon,$$
并选择首层单位时间 $t_1$，使其在 $B$ 中的像与 $t_a$ 相同。
两层均有 $s_i\mapsto\eta(1+\epsilon)$，故原八中心及完整开放模型的 $B$-基变换相同，记为 $\mathcal U_B$。
上标 $[2]$ 表示一形式在这个共同模型上的约化。

在 $U_0=\mathcal U_B\otimes_B k$ 上置
$$T=\bar t_a^m,\qquad J=J_m=I_{m,\eta}(x,y;\bar t_a),\qquad
\varepsilon_m=(-1)^{m+1},$$
$$f(Z)=(T+JZ+Z^2)^2-4\varepsilon_m Z^3,\qquad
H=H_p(T,J;\varepsilon_m)=[Z^{p-1}]f(Z)^{(p-1)/2}.$$
$J,H$ 是原完整 $U_0$ 上的正则函数。
当 $a\ge2$ 时，$p\mid\ell$，所以 $H$ 的任意局部提升的 $\ell$ 次幂彼此相等，
粘成全局标量 $H^{\langle\ell\rangle}$；$a=1$ 时定义 $H^{\langle0\rangle}=1$。

**TB.1：原环面的完整首 jet 比较。** 在共同原环面上有
$$\boxed{\quad\alpha_{mp^a}^{[2]}=H^{\langle\sigma-1\rangle}\alpha_{mp}^{[2]}.\quad} \tag{TB1}$$

**TB.2：同一恒等式跨全部末端线成立。** 消费原 D/G 的全局正则性及同一八中心接口，
(TB1) 在
$$\Gamma(\mathcal U_B,\Omega^1_{\mathcal U_B/B})$$
中成立。这里不附加普通性、Hasse 根简单性、光滑能级或谱可分性假设。
它仅是二阶商上的完整两状态一形式恒等式；不声称一般 $m$ 的首层理想为 $(\pi,H)$，
不求其更高 $\pi$ 阶理想、准确首非零厚度或配对单位。

## Status

**PROVABLE AS STATED。**

原目标恒等式无需改指数或增加 $m$ 的数值因子。
证明中的外部缩放项确有一个 $m$ 因子，但它在两层比较中相同。
块内变形不能删除；它进入下文 $j_*,c_s,d_s$ 和 $H_*$，由同一个 Frobenius 整倍数幂消去比较差异。
本状态是作者结论，仍待非作者按本件实际链核查。

## Assumptions、输入与阅读边界

所有状态微分固定基环、时间和谱变量。原矩阵没有另一个独立的 $q$ 系数依赖。
本件使用同一原矩阵，不换成只具相同迹的谱替代矩阵，也不更换原积分常数规范。

| 输入 | 本轮亲读并实际消费的接口 | SHA-256 |
|---|---|---|
| [GLOBAL_FIRST_JET_FACTORISATION_V1](PAPER30_QPI_VERTICAL_ALPHA_GLOBAL_FIRST_JET_FACTORISATION_V1_20260909.md) | 全文 185 行；仅用 Steps 1、2、4 的二阶商／提升幂／图上限制单射论证，不消费 FJ.2 的首层理想 | `9d53bee5abf8026dfa09d2bcb38713e0ace28ff082d9e87b3efa595ab5955a86` |
| [FIRST_JET_MATRIX_LEMMA_V1](PAPER30_QPI_VERTICAL_ALPHA_FIRST_JET_MATRIX_LEMMA_V1_20260909.md) | 全文 283 行；通用带权交换子恒等式、降序正号及相对微分规范 | `f3618fa1345804ce5d93acae4e6fdb2b3ee7761a87ae2de8bc453d24944971bd` |
| [整数 brief V1](PAPER30_QPI_INTEGRAL_CANDIDATE_BRIEF_V1_20260909.md) | §§2–3 原矩阵、八中心、精确小阶迹／行列式及已接受 D/G 接口 | `59f21705782443e9ac57aeb0f62c80f198f7fd18cec1a5ad3e496f0cf2f71f13` |
| [原整除诊断 D](PAPER30_QPI_CYCLOTOMIC_DIFFERENTIAL_DIAGNOSTIC_V1_20260909.md) | Steps 1–5，特别是整数循环插入与秩二迹递推 | `e2f032ff1197d415be611670e3d233efd7f6ead0d7dbe16b05f796ed42f43652` |
| [原完整模型 G](PAPER30_QPI_CYCLOTOMIC_GLOBAL_MODEL_DIAGNOSTIC_V1_20260909.md) | §§1–3 的同一八中心及 G3；Step 6 全局整除微分延拓 | `59b308f605832d82e00720c5a3a7871c862698e194503ff3b289da592ced28e0` |

另全文读既有 230 行首 jet 迭代作者件作为次数／时间规范对照；
本件重新给出所需的 $[1,2p-1]$ 数字论证，不引用其仅 $m=1$ 的次数界来代替全 $m$。
不重新审查已接受的几何、Jacobian 身份或旧候选状态；也不使用首层非消失定理。

## Notation 与 Proof Strategy

用小写 $z$ 表示原谱变量，大写 $Z$ 表示取 $m$ 倍次数后的形式变量。
对任意系数多项式／一形式多项式，定义共振投影
$$\mathcal P_m\!\left(\sum_i b_i z^i\right)=\sum_{j\ge0}b_{mj}Z^j.$$
它不是一般的乘法同态；但对任意 $Q(Z)$，有
$$\mathcal P_m(Q(z^m)P(z))=Q(Z)\mathcal P_m(P(z)). \tag{P}$$
证明直接按每个谱次数取系数，适用于标量或一形式系数。

紧凑写原矩阵为
$$u=x(y-1),\quad v=y-1,\quad J_1(t)=y-x+x/y-t/x,$$
$$A(z;t)=
\begin{pmatrix}t-u&-x\\v(u-t)&u\end{pmatrix}
+z\begin{pmatrix}J_1(t)-1&1\\J_1(t)+u-1&1\end{pmatrix}
+z^2E,\qquad E=\begin{pmatrix}1&0\\0&0\end{pmatrix}. \tag{A}$$
这是 brief 的逐项同一矩阵。特别是 $dE=0$、$\det A(z)=z^3$。
以下块符号 $\mathsf B_s$ 不与基环 $B$ 混用：
$$\mathsf B_s(z)=A(s^{m-1}z)\cdots A(sz)A(z),\qquad r=s^m.$$
降序次序始终保持。

使用 `proof-writer`，依赖链分为六步：

1. 在特征零按 $N$ 个块循环插入，先取得整数表达式，再模 $\pi^2$。
2. 保留 $\mathsf B_s=\mathsf B_\eta+\epsilon C$ 的全部块内变化，识别共振迹和行列式。
3. 用平方零误差与投影 (P) 算出内部项为 $H_*^\sigma dj_*$。
4. 用二阶矩阵恒等式算出外部缩放项；真实次数界给投影支持 $1$ 至 $5$。
5. 在允许次数中证明唯一数字选择，得到两层相同的 Hasse 因子。
6. 粘合提升幂，并用原完整模型上真正的限制单射延拓，不仅使用集合稠密性。

## Proof

### Step 1. 实际整数块循环插入

先在 $\mathcal O_a$ 的 Laurent 状态环中工作。$s=s_a$ 精确阶为 $mN$，
$r=s^m$ 精确阶为 $N$，而原降序乘积准确分成
$$M_{mN,s}(z)=\mathsf B_s(r^{N-1}z)\cdots\mathsf B_s(rz)\mathsf B_s(z).$$
对该迹求状态微分，共有 $N$ 个块插入位置。将第 $j$ 个块的微分移到迹的首位，
再置 $w=r^jz$，用 $r^N=1$ 保持其余块的降序循环次序。
这项成为
$$Q(w)=\operatorname{tr}\bigl(d\mathsf B_s(w)
\mathsf B_s(r^{N-1}w)\cdots\mathsf B_s(rw)\bigr).$$
取 $z^{mN}$ 系数时，变量替换的因子 $r^{jmN}=1$。
故先在整系数一形式中已有
$$dI_{mN,s}=N[z^{mN}]Q(z).$$
在特征零除以 $N$ 后，得到合法的整式
$$\alpha_{mN}=[z^{mN}]\operatorname{tr}\bigl(d\mathsf B_s(z)
\mathsf B_s(r^{N-1}z)\cdots\mathsf B_s(rz)\bigr). \tag{1}$$
$d\mathsf B_s$ 包含块内全部 $m$ 个插入；(1) 没有遗漏这个和，也不需再乘一个 $m$。
随后才可将 (1) 约化到 $B$。绝不从特征 $p$ 的 $d(I\bmod p)=0$ 反除 $N$。

因为 $p$ 奇，$v_{\pi_a}(p)=p^{a-1}(p-1)\ge2$，所以 $B$ 的特征为 $p$。
在共同商环中 $s=\eta(1+\epsilon)$，故
$$r=s^m=1+m\epsilon. \tag{2}$$
这里外部缩放速率是 $m$，不是一。

### Step 2. 完整保留块内变形

以下在 $R=B[x^{\pm1},y^{\pm1}]$ 及其自由状态微分模中工作，$t$ 是实际 $t_a$ 在 $B$ 中的像。
即使 $t=t_0+\epsilon t_1$，也不在本步骤把它换成 $t_0$。
令 $\mathsf A_j(z)=A(\eta^jz;t)$。逐因子 Taylor 展开给
$$\mathsf B_s(z)=\mathsf B_\eta(z;t)+\epsilon C(z),$$
$$C(z)=\sum_{j=0}^{m-1}j\mathsf A_{m-1}\cdots\mathsf A_{j+1}
(z\partial_z\mathsf A_j)\mathsf A_{j-1}\cdots\mathsf A_0. \tag{3}$$
$C$ 的选择只需确定到模 $\epsilon$；(3) 显示全部块内谱变形，未仅保留块间缩放。
记 $\delta S=\operatorname{tr}C$、$L=[z^m]\delta S$。

在 $\eta$ 精确阶为 $m$ 时，原小阶迹恒等式给
$$\operatorname{tr}\mathsf B_\eta(z;t)=t^m+j^\circ z^m+z^{2m},\qquad
j^\circ=I_{m,\eta}(x,y;t). \tag{4}$$
(4) 也在当前非约化环上成立：先将同一域上原恒等式用于 $k(t)$ 的不定时间，
得到 $k[t^{\pm1},x^{\pm1},y^{\pm1}]$ 中 Laurent 多项式恒等式，再代入实际 $t\in B^\times$。
这不假定 $j^\circ$ 在整个 $\mathcal U_B$ 有全局提升；它这里只是原环面函数。

置 $S_s=\operatorname{tr}\mathsf B_s$、$D_s=\det\mathsf B_s$。
最低谱系数不依赖 $s$：$\mathsf B_s(0)=A(0;t)^m$，$\operatorname{tr}A(0;t)=t$、$\det A(0;t)=0$。
Cayley–Hamilton 给 $A(0;t)^m=t^{m-1}A(0;t)$，故其迹为 $t^m$。最高谱系数是
$$[z^{2m}]\mathsf B_s=s^{m(m-1)}E,$$
因每个因子最高项为 $s^{2j}z^2E$ 且 $E^m=E$。
原行列式则准确给
$$D_s=d_s z^{3m},\quad d_s=s^{3m(m-1)/2},\qquad d_{\rm state}D_s=0. \tag{5}$$
于是，定义
$$j_*=[z^m]S_s=j^\circ+\epsilon L,\qquad c_s=s^{m(m-1)},$$
便有
$$\mathcal P_m S_s=T_*+j_*Z+c_sZ^2=:S_*(Z),\qquad T_*=t^m,$$
$$\mathcal P_m D_s=d_sZ^3=:D_*(Z),\qquad dS_*=Z\,dj_*,\quad dD_*=0. \tag{6}$$
两个最高／行列式系数虽然对状态为常数，却不可以从首 jet 中先验删除：
$$c_s=1+\epsilon m(m-1),$$
$$d_s=\varepsilon_m\left(1+\epsilon\frac{3m(m-1)}2\right). \tag{7}$$
分数 $m(m-1)/2$ 指整数；奇特征也允许除以二。
这里使用 $\eta^{m(m-1)}=1$ 及 $\eta^{3m(m-1)/2}=(-1)^{m+1}$。
对后一等式，$m$ 奇时指数为 $m$ 的倍数；$m$ 偶时 $\eta^{m/2}=-1$，直接得到负号。

### Step 3. 共振投影精确计算内部项

先定义内部项
$$F_N=[z^{mN}]\operatorname{tr}\bigl(d\mathsf B_s\mathsf B_s^{N-1}\bigr).$$
二阶 Cayley–Hamilton 的整系数递推给
$$\operatorname{tr}(dM\,M^{N-1})=U_{N-1}(S,D)dS-U_{N-2}(S,D)dD,$$
其中 $S=\operatorname{tr}M,D=\det M$，$U_{-1}=0,U_0=1,U_n=SU_{n-1}-DU_{n-2}$。
对 $N=p^a$，特征 $p$ 的通用多项式恒等式是
$$U_{N-1}(S,D)=(S^2-4D)^{(N-1)/2}. \tag{8}$$
证明可在独立变量 $u,v$ 中用
$U_{N-1}(u+v,uv)=(u^N-v^N)/(u-v)=(u-v)^{N-1}$，
再通过对称多项式环的单射下降；等式随后适用于含平方零元的 $R$，不要求实际矩阵可对角化。
由 (5)，$dD_s=0$，故 $F_N=[z^{mN}](S_s^2-4D_s)^{(N-1)/2}dS_s$。

由 (4)、(6)，可写
$$S_s(z)=S_*(z^m)+\epsilon V(z),\qquad \mathcal P_mV=0,$$
而 $D_s(z)=D_*(z^m)$ 完全没有非共振项。
对任意多项式 $\Phi(S,D)$，平方零 Taylor 公式及 (P) 给
$$\mathcal P_m\bigl(\Phi(S_s,D_s)dS_s\bigr)=\Phi(S_*,D_*)dS_* . \tag{9}$$
具体地，两边之差的候选项只有
$$\epsilon\,\Phi_S(S_*(z^m),D_*(z^m))V(z)dS_*(z^m)
+\epsilon\,\Phi(S_*(z^m),D_*(z^m))dV(z).$$
$\mathcal P_mV=\mathcal P_m(dV)=0$，其余系数只含 $m$ 倍次数，故两项投影都为零。
这一步仅删除不会进入目标次数的部分，没有把 $L,c_s,d_s$ 删除。

记
$$f_*(Z)=S_*(Z)^2-4D_*(Z),\qquad H_*=[Z^{p-1}]f_*(Z)^{(p-1)/2}.$$
于是由 (8)–(9)、(6)，
$$F_N=[Z^{N-1}]f_*(Z)^{(N-1)/2}\,dj_* . \tag{10}$$
因为 $\deg f_*\le4$，$Q_*=f_*^{(p-1)/2}$ 只支持 $0$ 至 $2p-2$。
特征 $p$ 给
$$f_*^{(N-1)/2}=\prod_{i=0}^{a-1}Q_*^{p^i}.$$
要贡献 $Z^{p^a-1}$，最低位在 $[0,2p-2]$ 中须模 $p$ 等于 $p-1$，故只能取 $p-1$；
减去该位再除以 $p$ 后，目标成为 $p^{a-1}-1$，重复至所有位均为 $p-1$。
所以
$$F_N=H_*^\sigma dj_*,\qquad F_p=H_*dj_* . \tag{11}$$
此论证在整个非约化 $R$ 中成立；Frobenius 作用于标量系数，不对一形式取幂。
$H_*$ 约化为 Claim 的 $H$，因此若 $a\ge2$，$p\mid\ell$ 给
$$H_*^\ell=\widetilde H^\ell$$
对 $H$ 的任意提升 $\widetilde H$ 都成立。
由此内部项本身已满足 $F_N=H^{\langle\ell\rangle}F_p$。
实际时间对 $T_*,j_*,dj_*,H_*$ 的影响全部留在 (6)、(11)，没有遗漏 $t_1\partial_t(dJ)$ 项。

### Step 4. 外部缩放项与真实次数界

令 $\mathsf B_0=\mathsf B_\eta(z;\bar t_a)$ 为完整剩余块。
对任意交换特征 $p$ 系数环上的二阶矩阵 $M,X$，首 jet 矩阵引理给
$$\sum_{j=1}^{N-1}jM^{N-1-j}XM^{j-1}
=\bigl((\operatorname{tr}M)^2-4\det M\bigr)^{(N-3)/2}[M,X]. \tag{12}$$
该式的全称机制是：几何级数多项式的形式导数把左边变成 $\operatorname{ad}_M^{N-2}(X)$，
而二阶 Cayley–Hamilton 给 $\operatorname{ad}_M^3=\Delta_M\operatorname{ad}_M$，$\Delta_M=(\operatorname{tr}M)^2-4\det M$。
$N-2$ 为奇数，迭代即得 (12)；正号绑定原降序次序。
没有除以判别式、行列式或特征根，故可在任意退化状态使用。

根据 (2)，每个外部块满足
$$\mathsf B_s(r^jz)=\mathsf B_s(z)+\epsilon mj\,z\partial_z\mathsf B_0(z).$$
在 (1) 中展开所有这些项，内部变形全部已计入 $F_N$；
外部修正因已乘 $\epsilon$，其中 $d\mathsf B_s$ 及其他块只需剩余值。
置
$$\Gamma_m(z)=\operatorname{tr}\bigl(d\mathsf B_0[\mathsf B_0,z\partial_z\mathsf B_0]\bigr),\qquad
\gamma_m(Z)=\mathcal P_m\Gamma_m(z).$$
由 (12) 及 $\Delta_{\mathsf B_0}=f(z^m)$，得到
$$\alpha_{mN}^{[2]}=F_N+\epsilon m\,\beta_N,$$
$$\beta_N=[z^{mN}]\Gamma_m(z)f(z^m)^{(N-3)/2}
=[Z^N]\gamma_m(Z)f(Z)^{(N-3)/2}. \tag{13}$$
这里 $\beta_N$ 仅指块间谱缩放项；没有把它与完整首系数混同。

原块次数为 $2m$，且最高矩阵系数恰为 $E$，故
$$\deg d\mathsf B_0\le2m-1.$$
交换子 $[\mathsf B_0,z\partial_z\mathsf B_0]$ 的 $z^{4m}$ 系数是 $[E,2mE]=0$，
所以其次数至多 $4m-1$。其常数项为零，因为第二槽至少含 $z$。
相乘取迹得到
$$\operatorname{supp}_z\Gamma_m\subset[1,6m-2]. \tag{14}$$
于是
$$\operatorname{supp}_Z\gamma_m\subset
\begin{cases}[1,4],&m=1,\\[1,5],&m\ge2.\end{cases} \tag{15}$$
对 $m=2$，(14) 允许原谱次数十；必须在投影前保留，不能沿用原单矩阵的四次界。

### Step 5. 全 $m$ 外部项的唯一数字分解

置
$$Q(Z)=f(Z)^{(p-1)/2},\qquad G(Z)=\gamma_m(Z)f(Z)^{(p-3)/2}.$$
由 (15) 及 $\deg f=4$，对所有 $m\ge1$ 都有
$$\operatorname{supp}Q\subset[0,2p-2],\qquad
\operatorname{supp}G\subset[1,2p-1]. \tag{16}$$
$m=1$ 时第二个上界可改善为 $2p-2$，但无需这项改善。
$p=3$ 时指数 $(p-3)/2=0$，$G=\gamma_m$ 的范围是 $[1,5]$，仍满足 (16)。

$a=1$ 的比较是恒等式。设 $a\ge2$；指数拆分给
$$\beta_N=[Z^{p^a}]G(Z)\prod_{i=1}^{a-1}Q(Z)^{p^i}.$$
任一可能贡献项的次数满足
$$n_0+pn_1+\cdots+p^{a-1}n_{a-1}=p^a,$$
$$1\le n_0\le2p-1,\qquad0\le n_i\le2p-2\ (i\ge1).$$
模 $p$ 后 $n_0$ 必为 $p$ 的倍数；区间 $[1,2p-1]$ 中唯一候选是 $p$。
减去 $p$ 再除以 $p$，剩余目标为 $p^{a-1}-1$。
其每个低位均模 $p$ 等于 $p-1$，而 $[0,2p-2]$ 中只有 $p-1$ 满足，故
$$n_0=p,\qquad n_1=\cdots=n_{a-1}=p-1.$$
读取系数即得
$$\beta_N=\left(\prod_{i=1}^{a-1}H^{p^i}\right)\beta_p=H^{\sigma-1}\beta_p. \tag{17}$$
只有标量 $Q$ 被取 Frobenius 幂，$G$ 及其一形式系数始终线性出现。
结合 (11)、(13)、(17)，在原环面上
$$\alpha_{mN}^{[2]}=H_*^\sigma dj_*+\epsilon mH^\ell\beta_p,$$
$$\alpha_{mp}^{[2]}=H_*dj_*+\epsilon m\beta_p.$$
首层和高层的 $t,s,\mathsf B_s$ 在 $B$ 上完全相同，所以两式确在同一系数环比较。
由于 $H_*^\ell$ 是 $H^{\langle\ell\rangle}$，且乘 $\epsilon$ 后只消费其剩余值，
两式直接给 (TB1)。这也说明外部的 $m$ 不产生主恒等式右端的额外 $m$ 因子。

### Step 6. 二阶商、乘数及完整原模型

先说明 Claim 的商环识别。两个首／高层商环均特征 $p$，最大理想平方为零，长度为二。
若 $k=\mathbb F_{p^f}$，方程 $X^{p^f}-X=0$ 的导数为 $-1$，
故每个剩余元在二阶商中有唯一根提升；这些根在加法、乘法下封闭，构成系数域 $k$。
因此每个元素唯一写为 $c_0+c_1\pi_i$，给指定的 $k$-代数同构及共同 $\epsilon$。
唯一 tame 根提升在该系数域中就是 $\eta$；$t_1$ 由商映射满射选取。
这不是 $\zeta_p\mapsto\zeta_{p^a}^{p^{a-1}}$ 的自然分歧嵌入；后者不保持一阶参数。

原四组单位截面坐标是 $1,t,t,s$。两层这些坐标在 $B$ 上相同，
逐个相对坐标图的吹起及边界严格变换相同，给原共同 $\mathcal U_B$。
本步只用原 D/G 已接受的八中心／光滑图接口，不用一般非平坦吹起基变换断言。

若 $a\ge2$，任意两个 $H$ 的局部提升相差 $\epsilon h$，且 $p\mid\ell$，所以
$$ (\widetilde H+\epsilon h)^\ell=\widetilde H^\ell.$$
可先取 $p$ 次幂使平方零误差消失，再取 $\ell/p$ 次幂。
故这些幂粘成全局 $H^{\langle\ell\rangle}$，不要求原 $J$ 有全局整提升。
$a=1$ 的全局乘数为一。

由 G3，两个 $\alpha^{[2]}$ 在共同模型上全局正则；乘数也已全局正则。
其差在环面为零。为在非约化 $B$ 上合法延拓，使用原四个末端图：
它们分别是 $B[u,v]$ 在 $1+uv$、$t+uv$、$t+uv$、$s+uv$ 处的相应局部化，
环面由进一步反演 $u$ 得到。$u$ 在这些环中为非零因子；
局部自由微分模向反演 $u$ 后的模的映射因此单射。
所以差在每条完整末端图也为零，而环面与这四图覆盖原 $\mathcal U_B$。
这证明 TB.2，没有把集合稠密或未知 $\beta_p$ 的全局正则性当作代替。证毕。

## 实际有限排错

另运行一次仅内存 `python -B` 双数多项式计算，正常 exit 0；未写脚本或数据文件。
从原 (A) 出发保留 $\epsilon dx,\epsilon dy$ 交叉项，直接形成每个 $m$ 块、
每个外部缩放块以及 (1) 的降序插入积，不通过在特征 $p$ 中除原迹的微分得到答案。
同时把外部缩放关掉，分别比较内部项的同一因子分解。

| $(p,m,\eta,a)$ | $t=t_0+\epsilon t_1$；状态 $(x,y)$ | 实际检查结果 |
|---|---|---|
| $(3,2,2,2)$ | $1+\epsilon$；$(1,1)$ | 完整及内部四个一形式系数比较通过；$\delta S$ 非共振三次项实际非零 |
| $(5,2,4,2)$ | $2+\epsilon$；$(1,2)$ | 同上；非共振一次、三次项实际非零 |
| $(7,3,2,2)$ | $2+\epsilon$；$(2,3)$ | 同上；非共振一次、二次、五次项实际非零 |
| $(3,2,2,3)$ | $2+\epsilon$；$(2,2)$ | 同上；非共振三次项实际非零 |

另在这些实际块中核准剩余迹只含 $0,m,2m$ 次数、最高矩阵系数无状态导数、
块内 $\delta S$ 的常数项为零及最高次系数为 $m(m-1)$。
这些只是有限点上的精确代数排错；未检查这些点所属能级的光滑性，不把它们当作几何非消失证据。
全部 $p,m,a,t$ 的证明责任由 Steps 1–6 承担，不从此表外推。

## Corrections or Missing Assumptions

- 原主恒等式保留。块内变化要放入共振三项式及 $d_s$；(9) 只允许删除其非共振平方零部分。
- 外部 $r=s^m=1+m\epsilon$ 的速率因子 $m$ 必须保留；主比较式没有额外因子。
- 一般 $m$ 的投影交换子项可有第五次项；允许到 $2p-1$ 的低位范围仍只有一个 $p$ 倍数，故无需错误地缩为四次。
- 实际时间在 $B$ 中固定但允许非零一阶提升，$dj_*$ 中的变化不能遗漏；本文没有只比较切向商类。
- 比较是二阶商的参数同构，不是首层到高层的自然分歧嵌入。
- $p=2$ 不在 Claim 内；$a=1$ 为恒等边界。没有把半整数指数或首层商环识别照搬到二。

## Open Risks 与交付范围

本件的新增作者责任是块循环除法、实际块内扰动的共振投影、$6m-2$ 次数界和完整首 jet 比较。
上述原恒等式在奇异谱状态也按多项式成立；但这不把奇异能级改称超奇异。
全局部分只消费既有原 D/G 正则模型接口，不消费一般 $m$ 首层切向单位或系数理想。
尤其不能从 (TB1) 推出 $\mathfrak c(\alpha_{mp})=(\pi,H)$，也不能推断任何高层准确厚度。
新的 $m=2$ 配对信号不作为本证明前提，未拼接成未经证明的全 $m$ 配对定理。
仍待独立检查本文件；未修改任何旧作者件、来源报告、锁、稿件或 PDF，未新作文献检索或 GPU 计算。
