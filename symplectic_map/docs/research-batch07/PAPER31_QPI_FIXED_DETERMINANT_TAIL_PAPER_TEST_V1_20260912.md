# Paper31：逐精确行列式统一尾界的有界纸面测试 V1

日期：2026-09-12 UTC。作者：`/root`，合并独立纸面代理 `p31_kummer_uniform_tail_paper_test` 的完整推演。
这不是新问题生成、正式候选票或论文准入；它实际完成旧[I08]§6所留的单次近单位尾界诊断。
旧满像接受、旧4.0/CAUTION及原22–30页合同不回写。无数值、CAS、阶数枚举或GPU。

## 1. Claim / Status / Assumptions

主引理：固定素数 $\ell\ge5$，$R=\mathbb Z_\ell$，对每个 $d\in R^\times$，令
$S_d=\{A\in\operatorname{GL}_2(R):\det A=d\}$ 带归一化SL₂平移测度。则对所有 $n\ge1$，
$$
\tau_n(d):=\Pr_{S_d}\{v_\ell\det(I-A)\ge n\}
\le \frac{2}{1-\ell^{-2}}\ell^{-\lceil n/2\rceil}+\frac{\ell^{-n}}{\ell+1}.
\tag{1}
$$
作者状态：`PROVABLE AS STATED`；这里只是作者自足证明，独立接受状态由后续审查另定。
常数对 $d=1$ 和任意近单位 $d$ 也一致；不声称最优阶、常数或准确余核质量表。

应用范围明确为旧[K]的有限域自治接口，而非给有限域参数赋实数正性：
$q=p^a$，$p\ge5$，$\ell\ne p$，$T\in\mathbb F_q\setminus\{0,-27/256\}$，
$$E_h:\ v^2+huv-Tv=u^3-Tu^2,\qquad P_h=(0,T).$$
只计光滑 $h\in\mathbb F_q$。下文使用旧[K]全部层几何仿射满像与非异常有限层点阶读取，
以及其已接受的五个乘法坏点 $I_8+4I_1$；不重证、不扩大这些范围。

## 2. Notation / Dependency map

$R_n=R/\ell^nR$；$D_n=(1-\ell^{-2})\ell^{5n}$ 是几何共同分点塔次数。
$\mu_{d,\ell}$ 是 $A\in S_d$、$b\in R^2$ 独立均匀时，$[b]\in\operatorname{coker}(A-I)$ 的阶赋值分布。
策略：两个不交矩阵坐标图证明(1)；Tate局部描述证明tame；Riemann–Hurwitz控亏格；
曲线Frobenius扭曲＋Weil界控任意共轭不变事件；最后一次截断平衡，而非无限层交换极限。

## 3. Proof of the fixed-determinant lemma

模 $\ell^n$ 固定行列式切片有 $\ell^{3n}(1-\ell^{-2})$ 个元素。
SL₂约化满射，逐层每点恰有 $\ell^3$ 个提升；因此精确 $d$ 的测度推到这个切片是均匀分布。
没有把全GL₂中的零测度条件事件作朴素条件化。

写 $A=\left(\begin{smallmatrix}a&b\\c&e\end{smallmatrix}\right)$。因行列式是单位，分成如下两图。

**图一：$a$ 是单位。** 自由取 $a,b,c$，$e=(d+bc)/a$。
由 $\det(I-A)=1-a-e+d$，目标条件等价于
$$a^2-(1+d)a+d+bc=0\pmod{\ell^n}.$$
对每组 $b,c$，这是首一二次同余，根数至多 $2\ell^{\lfloor n/2\rfloor}$。
证明该根界：$2$ 可逆，配方化为 $z^2=D$。若 $D=0\bmod\ell^n$，根数为
$\ell^{\lfloor n/2\rfloor}$；否则只有 $v_\ell(D)=2k<n$ 才可能有根，
除去 $\ell^{2k}$ 后单位平方根至多两个且唯一提升，原根数至多 $2\ell^k$。
忽略 $a$ 的单位限制只增大上界。因此图一质量至多
$2\ell^{2n+\lfloor n/2\rfloor}/[\ell^{3n}(1-\ell^{-2})]$。

**图二：$a$ 非单位、$b$ 是单位。** 自由取 $a,b,e$，$c=(ae-d)/b$。
目标条件准确为 $e=1+d-a\bmod\ell^n$；矩阵数为
$\ell^{n-1}(\ell^n-\ell^{n-1})$，质量恰为 $\ell^{-n}/(\ell+1)$。
两图互斥且穷尽，相加证明(1)。特别地 $\tau_n(d)\to0$，
所以 $\det(I-A)=0$ 的测度为零，$\mu_{d,\ell}$ 确有总质量一。∎

## 4. Tame geometry and finite-layer counting

在好约化开集，挠点与截面分点塔有限étale。在每个几何乘法坏点，完成局部域具有代数闭剩余域，
Tate一致化写作 $K^\times/Q^{\mathbb Z}$；若截面由 $z\in K^\times$ 表示，共同塔包含于
$$K(Q^{1/\ell^n},z^{1/\ell^n}).$$
单位根已在几何常数中，该扩张为 $\ell$ 幂次，故tame。
理由不是“整个仿射群阶素于 $p$”；那一说法一般不成立。
几何连通覆盖的tame Riemann–Hurwitz给
$$2g_n-2\le-2D_n+5D_n=3D_n,\qquad g_n\le1+3D_n/2.$$

令 $G_n$ 为几何仿射群，$\Gamma_{n,q}$ 为Frobenius陪集（线性部分行列式为 $q$）。
对任意 $G_n$-共轭不变集合 $C\subset\Gamma_{n,q}$，有
$$\left|N_C(q)-q|C|/D_n\right|\le K D_n\sqrt q\tag{2}$$
且 $K$ 绝对一致。具体证明：对一个 $G_n$-共轭类代表 $c$，以 $c^{-1}\mathrm{Frob}_q$
扭曲所选几何连通分量，得到同亏格、同覆盖次数的 $\mathbb F_q$ 曲线。
属于该共轭类的每个好有理底点贡献 $|C_{G_n}(c)|$ 个扭曲有理点。
Weil界与至多 $5D_n$ 个边界几何点给
$$\left|N_{[c]}-q/|C_{G_n}(c)|\right|
\le[1+2g_n\sqrt q+5D_n]/|C_{G_n}(c)|.$$
对类求和并用 $\sum_{[c]\subset C}|C_{G_n}(c)|^{-1}=|C|/D_n\le1$ 即得(2)。
这不额外乘算术常数域次数或事件共轭类数。

## 5. Uniform truncation consequence

定义异常事件 $B_n=\{v_\ell\det(I-A)\ge n\}$。
非异常部分由旧[K]准确读取 $[b]$ 的真实 $\ell$ 阶；异常部分用(1)、(2)控制。
对所有 $r\ge0$，于是
$$\left|\#\{h\text{ good}:v_\ell\operatorname{ord}(P_h)=r\}
-q\mu_{q,\ell}(r)\right|\ll_\ell D_n\sqrt q+q\ell^{-n/2}.$$
$r\ge n$ 时非异常事件为空，仍由同一异常上界控制，故没有遗漏大阶质量。
取 $n=\max(1,\lfloor(\log_\ell q)/11\rfloor)$ 得误差 $O_\ell(q^{21/22})$；
有限的小 $q$ 可吸入只依 $\ell$ 的常数。常数不依 $p,T,q,r$。

尾事件必须整体应用同一截断，不逐 $r$ 求和。因
$v_\ell\operatorname{ord}([b])\le v_\ell\det(I-A)$，对所有 $m\ge0$ 有
$$\#\{h\text{ good}:v_\ell\operatorname{ord}(P_h)\ge m\}
\le C_\ell q\ell^{-m/2}+C_\ell q^{21/22}.$$
当 $m$ 超过截断层时，全部目标在异常集合内，右侧误差项仍足够。
这是单个固定 $\ell$ 的统计，不是全部素数联合点阶、原始点密度或精确循环数分布。

## 6. Corrections / Open risks / Disposition

矩阵引理自足；应用调用Tate一致化、曲线Weil界和Riemann–Hurwitz基础定理。
代理本轮FULL读proof-writer、[K]与138行作者源；旧[I08]仅指定§6–7邻接局部；未新读外源全文。
主控FULL读[K]、本文并核上述数学；没有将旧源阅读冒称本轮重新完成。
逐精确余核质量表与文献[G]的逐项比对本轮未做，不能记录“准确表已核同”。
原状态权重完整合并未做；旧Hasse加权短链也不另计原创。

按[I08]原停止准则，这个已经写出的尾界只需要首一二次根计数，随后为成熟几何计数与截断平衡。
保存为短数学资产，**不作为独立Paper31长文中心，不重开正式评分**。
本件与新的小参数实动力问题分开：不同构造不拼成一个高分候选。

[K]: PAPER31_QPI_KUMMER_MATHEMATICS_DISPOSITION_V1_20260909.md
[I08]: PAPER31_QPI_NOVELTY_CD_I08_V1_20260909.md
