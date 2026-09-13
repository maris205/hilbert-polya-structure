# P30 qPI：首层 prime-block 迹同余与整数 Taylor 引理 V1

日期：2026-09-09。状态：`AUTHOR_LEMMA_PROVED_AS_STATED`；待非作者检查。

本件只证明原环面上的整数多项式同余，覆盖所有素数（包括 $p=2$）和所有 $p\nmid m$。
不据此自行宣称全局延拓、Čech 类非零、光滑能级首层理想或更高分歧层结论。
本件作者曾写 tame-block first-jet 稿；本件不是该稿的盲审或独立新意投票。

## 1. 参数、原对象与准确结论

设 $p$ 为素数、$m\ge1$、$p\nmid m$。设 $\mathcal O_0$ 为含精确 $m$ 阶单位根 $\widetilde\eta$ 的无分歧 $p$-进 DVR，
置
$$\mathcal O=\mathcal O_0[\zeta_p],\qquad
\pi=\zeta_p-1,\qquad k=\mathcal O/(\pi),\qquad
s=\widetilde\eta\zeta_p,\qquad r=s^m.$$
于是 $r$ 是精确 $p$ 阶单位根；$p=2$ 时 $\pi=-2$、$m$ 为奇数。
可取不定单位时间 $t$，令
$$R_0=\mathcal O[t^{\pm1}],\qquad R=R_0[x^{\pm1},y^{\pm1}].$$
以下结论随后可代入任意实际 $t\in\mathcal O^\times$。横线表示模 $\pi$ 约化。

原矩阵及乘积次序固定为
$$A(z)=A_0+zA_1+z^2 E,\qquad E=\operatorname{diag}(1,0),$$
$$A_0=\begin{pmatrix}
t+x-xy&-x\\
t+x-ty-2xy+xy^2&x(y-1)
\end{pmatrix},\quad
A_1=\begin{pmatrix}
y-x+x/y-1-t/x&1\\
y-2x-1+xy+x/y-t/x&1
\end{pmatrix}.$$
直接有 $\det A(z)=z^3$、$\operatorname{tr}A_0=t$、$\det A_0=0$。置
$$B_s(z)=A(s^{m-1}z)\cdots A(sz)A(z),\qquad
S_s(z)=\operatorname{tr}B_s(z),\quad D_s(z)=\det B_s(z),$$
$$I_{mp}=[z^{mp}]\operatorname{tr}\bigl(B_s(r^{p-1}z)\cdots B_s(rz)B_s(z)\bigr). \tag{1}$$
(1) 中展开每个块，正是原长度 $mp$ 的降序乘积；没有调换矩阵因子。

记
$$T=t^m,\quad C=s^{m(m-1)},\quad
\delta=s^{3m(m-1)/2},\quad j_t=[z^m]S_s(z),\quad
\varepsilon_m=(-1)^{m+1},$$
其中 $\delta$ 是题设状态常数 $d$ 的改名，避免与微分记号混淆。再记
$$\lambda=\begin{cases}1,&p\ne2,\\-1,&p=2.\end{cases}$$
定义整数迹幂多项式
$$L_0(S,D)=2,\quad L_1(S,D)=S,\quad
L_n(S,D)=S L_{n-1}(S,D)-D L_{n-2}(S,D),$$
以及单变量多项式
$$F(h)=\lambda[Z^p]L_p(T+hZ+CZ^2,\delta Z^3)\in R_0[h]. \tag{2}$$

**引理。** 在上述参数范围内：

1. 原积分满足准确理想同余
   $$\boxed{I_{mp}-F(j_t)\in p\pi R.} \tag{3}$$
2. 存在 $Q(h)\in R_0[h]$，使
   $$F(h)=\lambda h^p+pQ(h),\qquad F'(h)/p\in R_0[h]. \tag{4}$$
   并且
   $$\overline{F'(h)/p}=H_p(\overline T,h;\varepsilon_m), \tag{5}$$
   其中
   $$H_p(T,h;\varepsilon)=
   \begin{cases}
   [Z^{p-1}]\bigl((T+hZ+Z^2)^2-4\varepsilon Z^3\bigr)^{(p-1)/2},&p\ne2,\\
   h,&p=2.
   \end{cases}$$
3. 在通用多项式环 $R_0[a,f]$ 中先作精确整除，有
   $$\mathscr T_F(a,f):=\frac{F(a+\pi f)-F(a)}{p\pi}\in R_0[a,f],$$
   且
   $$\boxed{\overline{\mathscr T_F(a,f)}
   =H_p(\overline T,\overline a;\varepsilon_m)\overline f-\overline f^{\,p}.} \tag{6}$$
   因而 (6) 可代入任意 $R_0$-代数中的 $a,f$。若该代数有 $p\pi$-挠，
   商的含义是上述通用整系数多项式的取值，不能将其重新定义为不唯一的数值除法。

## 2. 原块的首尾系数、行列式与非共振项

由 Cayley–Hamilton，$A_0^m=t^{m-1}A_0$（$m=1$ 同样成立），故
$$[z^0]S_s=T.$$
每个因子的最高项为 $s^{2j}z^2E$，而 $E^m=E$，故
$$[z^{2m}]B_s=s^{m(m-1)}E,\qquad [z^{2m}]S_s=C.$$
行列式逐因子相乘给出
$$D_s(z)=\delta z^{3m}. \tag{7}$$
三个系数 $T,C,\delta$ 均与 $x,y$ 无关。

设 $\eta=\overline s$，其在 $k$ 中精确阶为 $m$。模 $\pi$ 后，循环迹恒等式给
$$\begin{aligned}
\operatorname{tr}B_\eta(\eta z)
&=\operatorname{tr}\bigl(A(z)A(\eta^{m-1}z)\cdots A(\eta z)\bigr)\\
&=\operatorname{tr}\bigl(A(\eta^{m-1}z)\cdots A(\eta z)A(z)\bigr)
=\operatorname{tr}B_\eta(z).
\end{aligned}$$
当 $m=1$ 时，被循环移位的剩余乘积为空乘积，取单位矩阵；上述等式仍成立。
若 $m\nmid i$，则 $\eta^i-1\ne0$ 是域 $k$ 中的单位，所以约化迹的 $z^i$ 系数为零。
这直接证明非共振项的整除性，包括 $p=2$；不调用只限奇素数的 first-jet 公式。
从而置
$$S_*(Z)=T+j_t Z+CZ^2,\qquad E_s(z)=S_s(z)-S_*(z^m),$$
便有
$$E_s(z)\in\pi R[z],\qquad [z^{im}]E_s(z)=0\quad\text{对所有整数 }i. \tag{8}$$
这里 $E_s$ 是标量多项式，不是矩阵 $E$。

此外
$$\overline C=1,\qquad \overline\delta=\varepsilon_m,\qquad
\overline\lambda=1. \tag{9}$$
第二式可逐奇偶核准：$m$ 奇时 $3m(m-1)/2$ 是 $m$ 的倍数；
$m$ 偶时必有 $p\ne2$，且 $\eta^{m/2}=-1$，故其该次幂为 $-1$。

## 3. 循环词轨道：取得第一个 $p\pi$ 同余

写 $B_s(z)=\sum_{i=0}^{2m}B_i z^i$。对指数词
$$\boldsymbol i=(i_0,\ldots,i_{p-1}),\qquad \sum_{\ell=0}^{p-1}i_\ell=mp,$$
定义权重及循环迹
$$w(\boldsymbol i)=\sum_{\ell=0}^{p-1}\ell i_\ell,\qquad
\tau(\boldsymbol i)=\operatorname{tr}(B_{i_{p-1}}\cdots B_{i_0}).$$
于是原 (1) 的该词贡献为 $r^{w(\boldsymbol i)}\tau(\boldsymbol i)$，
而 $[z^{mp}]\operatorname{tr}B_s(z)^p$ 的该词贡献为 $\tau(\boldsymbol i)$。

令循环移位为 $i'_\ell=i_{\ell-1\bmod p}$。迹在该操作下不变，且
$$w(\boldsymbol i')-w(\boldsymbol i)
=\sum_\ell i_\ell-pi_{p-1}=p(m-i_{p-1}).$$
由于 $r^p=1$，带权贡献也在每个循环轨道内不变。
轨道大小因 $p$ 为素数只能为 $1$ 或 $p$。

大小 $1$ 的词全部指数相同；总次数条件强制 $i_0=\cdots=i_{p-1}=m$。
其相位为
$$r^{mp(p-1)/2}=\lambda. \tag{10}$$
当 $p$ 奇时指数是 $p$ 的倍数；当 $p=2$ 时 $r=-1$、$m$ 奇，相位是 $-1$。
因此常值词在原迹与 $\lambda\operatorname{tr}B_s^p$ 的差中准确抵消。

每个大小 $p$ 的轨道在这个差中的贡献为
$$p\bigl(r^{w(\boldsymbol i)}-\lambda\bigr)\tau(\boldsymbol i)\in p\pi R,$$
因为 $r\equiv\lambda\equiv1\pmod\pi$。相加得到
$$I_{mp}-\lambda[z^{mp}]\operatorname{tr}B_s(z)^p\in p\pi R. \tag{11}$$
这里没有将矩阵因子交换，也没有在剩余特征中约去零元素 $p$。

## 4. 整数迹递推与非共振消去

任意二阶矩阵 $M$ 由 Cayley–Hamilton 满足
$$\operatorname{tr}M^n=L_n(\operatorname{tr}M,\det M).$$
在通用对称变量 $u,v$ 中，递推给
$$L_n(u+v,uv)=u^n+v^n.$$
模 $p$ 后 $u^p+v^p=(u+v)^p$，而
$\mathbb F_p[S,D]\hookrightarrow\mathbb F_p[u,v]$、$S\mapsto u+v,D\mapsto uv$ 单射。
故存在 $V_p(S,D)\in\mathbb Z[S,D]$，使
$$L_p(S,D)=S^p+pV_p(S,D). \tag{12}$$
这是通用多项式恒等式，不需要矩阵可对角化或判别式可逆。

利用 (7)、(8)，先处理 $pV_p$ 部分：多项式之差
$$p\bigl(V_p(S_s(z),\delta z^{3m})-V_p(S_*(z^m),\delta z^{3m})\bigr)$$
逐项带因子 $p\pi$。再处理 $S_s^p-S_*(z^m)^p$ 的 $z^{mp}$ 系数。
把 $S_s=\sum_i c_i z^i$ 作交换变量的多项式展开：

- 纯 $p$ 次项 $c_i^p z^{pi}$ 只有 $i=m$ 能贡献 $z^{mp}$；这一项在两边同为 $j_t^p$，已经抵消。
- 其余混合项的多项式系数为 $p!/(e_0!\cdots e_{2m}!)$，其中至少两个 $e_i>0$、每个 $e_i<p$，故该整数被 $p$ 整除。
- 两个展开之间没有抵消的项，至少使用一个 $m\nmid i$ 的系数；该 $c_i\in\pi R$，故同时带因子 $\pi$。

因此
$$[z^{mp}]\bigl(L_p(S_s(z),\delta z^{3m})
-L_p(S_*(z^m),\delta z^{3m})\bigr)\in p\pi R. \tag{13}$$
再由 $Z=z^m$ 换写共振系数，(11)、(13) 正给出 (3)。
本步骤不把共振投影误作环同态；多次非共振项相乘能回到共振次数，正由上述整数 $p$ 因子控制。

## 5. $F\bmod p$、整数导数及 Hasse 多项式

由 (12)，模 $p$ 后
$$F(h)\equiv\lambda[Z^p](T+hZ+CZ^2)^p=\lambda h^p,$$
故 (4) 中 $Q\in R_0[h]$ 存在。

为核准导数的准确因子，定义
$$U_{-1}=0,\quad U_0=1,\quad U_n=SU_{n-1}-DU_{n-2}\quad(n\ge1).$$
取通用伴随矩阵 $M=\begin{pmatrix}S&-D\\1&0\end{pmatrix}$。
在特征零整数多项式环中微分迹幂，并使用循环迹，有
$$\partial_S L_p(S,D)
=\sum_{j=0}^{p-1}\operatorname{tr}(M^jE_{11}M^{p-1-j})
=p(M^{p-1})_{11}=pU_{p-1}(S,D). \tag{14}$$
最后一式由同一递推及 $n=0,1$ 的初值成立。因此准确地
$$\frac{F'(h)}p
=\lambda[Z^{p-1}]U_{p-1}(T+hZ+CZ^2,\delta Z^3)\in R_0[h]. \tag{15}$$

模 $p$ 后，在对称变量中
$$U_{p-1}(u+v,uv)=\sum_{j=0}^{p-1}u^{p-1-j}v^j=(u-v)^{p-1}.$$
这是多项式式子，包括 $u=v$；由对称多项式单射可降回 $S,D$。
奇 $p$ 时它等于 $(S^2-4D)^{(p-1)/2}$；$p=2$ 时直接 $U_1=S$。
结合 (9)、(15) 即得 (5)，其中 $p=2$ 的系数为 $h$，没有半整数表达式。

## 6. 分歧整数 Taylor 商：Frobenius 项及 $p=2$ 符号

由 $\Phi_p(1+\pi)=0$，准确地
$$p+\sum_{j=2}^{p-1}\binom pj\pi^{j-1}+\pi^{p-1}=0.$$
因为中间二项式系数均被 $p$ 整除，故
$$\rho:=\frac{\pi^{p-1}}p
=-1-\sum_{j=2}^{p-1}\frac{\binom pj}{p}\pi^{j-1}\in\mathcal O^\times,
\qquad \overline\rho=-1. \tag{16}$$
因此对所有素数都有
$$\overline{\lambda\pi^{p-1}/p}=-1. \tag{17}$$
$p=2$ 必须单独注意：此时和式为空、$\rho=\pi/2=-1$、$\lambda=-1$，
所以 $\lambda\rho=+1$ 是特征零中的准确值，但在特征二剩余域中 $+1=-1$，仍是 (17)。
不能把 (17) 错写成所有 $p$ 上的特征零等式 $\lambda\rho=-1$。

用 $F=\lambda h^p+pQ$ 展开，通用商准确写为
$$\begin{aligned}
\mathscr T_F(a,f)
={}&\lambda a^{p-1}f
+\lambda\sum_{j=2}^{p-1}\frac{\binom pj}{p}\pi^{j-1}a^{p-j}f^j
+\lambda\rho f^p\\
&+\frac{Q(a+\pi f)-Q(a)}\pi.
\end{aligned} \tag{18}$$
(18) 的每项都在 $R_0[a,f]$ 中；最后一个差商因多项式差的整除性也是整系数多项式。
模 $\pi$ 后，中间和式消失，最后一项成为 $\overline{Q'}(\overline a)\overline f$。
再由 (4)、(5)、(17)，得到
$$\begin{aligned}
\overline{\mathscr T_F(a,f)}
&=\bigl(\overline\lambda\,\overline a^{p-1}+\overline{Q'}(\overline a)\bigr)\overline f
-\overline f^{\,p}\\
&=H_p(\overline T,\overline a;\varepsilon_m)\overline f-\overline f^{\,p},
\end{aligned}$$
这就证明 (6)。这里最后一项是系数环中的 Frobenius 幂；本件没有对一形式取 $p$ 次幂。

## 7. 原 $p=2,m=1$ 的精确交叉核准

置 $b=x(y-1)$、$J_t=\operatorname{tr}A_1=y-x+x/y-t/x$。此时
$s=-1$、$T=t$、$C=\delta=1$、$j_t=J_t$、$\lambda=-1$。
由 $L_2=S^2-2D$，准确得到
$$F(h)=-h^2-2t.$$
原矩阵直接给
$$I_2=[z^2]\operatorname{tr}(A(-z)A(z))
=\operatorname{tr}(A_0E+EA_0-A_1^2)
=2t-4b-J_t^2.$$
所以
$$I_2-F(J_t)=4(t-b)\in(2\pi)R=(-4)R. \tag{19}$$
对应通用 Taylor 商准确为
$$\frac{F(a+\pi f)-F(a)}{2\pi}=-af+f^2,$$
模二即 $\overline a\,\overline f-\overline f^2$，与 $H_2(\overline t,\overline a)=\overline a$ 一致。
这同时核准原迹乘积次序、$\lambda$、$p\pi$ 和 Frobenius 项的符号。

## 8. 有界精确排错与适用边界

本次仅运行内存中的 `python -B` / SymPy 检查，退出码 0，未写脚本或改动旧件。
检查不代替第 2–6 节的一般证明：

| 检查对象 | 准确检查内容 | 结果 |
|---|---|---|
| 通用 $p=2,3,5$ | $L_p-S^p\in p\mathbb Z[S,D]$、$\partial_SL_p=pU_{p-1}$、(4)、(5)；(18) 乘回 $p\pi$ 后模 $\Phi_p(1+\pi)$ 恢复原差，并核对模 $\pi$ 的 (6) | 全部通过 |
| 原矩阵 $p=2,m=1$ | 保留符号 $t,x,y$，直接乘 $A(-z)A(z)$，核对 (19) | 通过 |
| 原矩阵 $(p,m)=(2,3)$ | $t=3,x=1,y=3$；在 $\mathbb Q[s]/\Phi_6(s)$ 精确求差除以 $p\pi$，其系数分母均与 $p$ 互素 | 通过，商非零 |
| 原矩阵 $(p,m)=(3,2)$ | $t=2,x=1,y=2$；同上，使用 $\Phi_6$ | 通过，商非零 |
| 原矩阵 $(p,m)=(5,1)$ | $t=2,x=2,y=3$；同上，使用 $\Phi_5$ | 通过，商非零 |

后三项采用 $s$ 精确 $mp$ 阶，取 $\zeta_p=s^{m(m^{-1}\bmod p)}$（$m=1$ 时即 $s$），
故与正文 $s=\widetilde\eta\zeta_p$、$\pi=\zeta_p-1$ 的约定一致。
各状态和时间特化在相应 $p$ 处都是单位；这些有限点只排错，不承担任意参数量词。

本引理交付的是 (3)–(6) 及其原对象识别，不交付以下步骤：

- $j_t$ 或任何局部提升在原完整曲面上的拼接；
- 由 (6) 构造并识别 Čech 类、证明其非零，或证明微分的全局正则性；
- 所有光滑／奇异能级的首层系数理想及其重数；
- $a>1$ 的整数同余、更多 $\pi$-厚度，或额外分歧底变换后的准确赋值。

上述后续步骤即使使用本件，也仍需分别证明。没有新增新意评分、Route 评价或实验计划。

## 9. 已读输入、哈希与文件所有权

本件使用 `proof-writer` 的“准确命题—整数推导—边界／有限检查”结构；
没有把有限代数检查记为独立数学验收。实际读取的依赖范围如下，其他结论不由本件追认。

| 本地输入 | 本件读取／使用范围 | SHA-256 |
|---|---|---|
| `PAPER30_QPI_INTEGRAL_CANDIDATE_BRIEF_V1_20260909.md` | §2.2 原矩阵、降序乘积、原对象系数定义；原块非共振性在本文另由循环迹证明 | `59f21705782443e9ac57aeb0f62c80f198f7fd18cec1a5ad3e496f0cf2f71f13` |
| `PAPER30_QPI_CYCLOTOMIC_DIFFERENTIAL_DIAGNOSTIC_V1_20260909.md` | 原对象与 Hasse 记号；证明 Steps 2–5 的循环迹、$U_n$ 递推与特征 $p$ 多项式恒等式；本文重新给出所用证明 | `e2f032ff1197d415be611670e3d233efd7f6ead0d7dbe16b05f796ed42f43652` |
| `PAPER30_QPI_VERTICAL_ALPHA_TAME_BLOCK_FIRST_JET_LEMMA_V1_20260909.md` | §3 Step 2 原块 $S,D$、首尾系数的定义；未借用其奇素数模 $\pi^2$ 结论覆盖 $p=2$ | `6546720ecf39f667f09d45235dc0c7be340032b4c3f7c809e9d1cb60257396e9` |
| `PAPER30_QPI_VERTICAL_ALPHA_ALL_PRIME_HEIGHT1_PROOF_V1_20260909.md` | Step 4 的原 $I_2$ 公式，已在本文重新符号核算；未消费其几何、理想或非消失结论 | `ffdcfc37860477e990f836721898fc654537bb3254b7335876581990c2da4f74` |

仅新增本文件；旧输入、冻结稿和账本均不修改。定稿全文回读并向主控交付最终 SHA 后停止修改。
