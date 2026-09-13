# Paper31：两件纸面测试的 fresh 非作者有界数学审查 V1

审查日期：2026-09-13 UTC；文件版本名沿用本轮委托的 `20260912`。
审查席：`/root/p31_two_paper_tests_fresh_math_review`，未参与两份作者稿。
实际使用可用的 secondary Codex xhigh；未调用不可用的指定 GPT-5.4 MCP，不冒称跨模型验证。
本轮先 FULL 读 `research-review` 与 `proof-writer` 技能，再逐项纸推；依委托只做一次有界审查。
两件均为 **PROVABLE AS STATED**，不需要修订作者原命题；以下给出独立核验及准确消费范围。
这不是新意评分、四门票、旧 FAIL 复投、模型校准、论文准入或 Route A/B 评价。

## 1. 实际输入、读取范围与冻结对象

| 简称 | 本轮读取 | SHA-256 |
|---|---|---|
| [F] 固定行列式尾界作者稿 | FULL，1–109 行 | `d001a61719d759251598dcb6b89464d0fbb66c62f7030dfc7e5acf0ebde36023` |
| [S] 小参数 terminal 碰撞作者稿 | FULL，1–131 行 | `3965b09c332128e5afe6933d82dc6e33a4ff3cd3789ec96374cbbde4710f0f79` |
| [K] 已接受 Kummer 合取 | FULL，1–50 行 | `9db1f21b39b8e8df664fb27bd434fd02aed04b206ace4873de9834ff77d044e4` |
| [G] 原实分支／回返几何 | FULL，1–208 行 | `f0c92b3d03bc1686deb63877777d36c6297efde779d2fc02f81cde4d86e8a196` |
| [A] 旧实几何数学审查 | PARTIAL，115–145 行；只消费其中 118–142 的持续圆和角端点 | 本轮不冻结或重审旧件 |

定向检索过旧角公式的文件命中；检索片段不记作那些整份文件的 FULL 阅读。
未新读 Tate、Weil、Riemann–Hurwitz 的外部文献全文；只核这些基础定理在当前对象上的适用条件。
未浏览、未运行数值或 CAS、未作点阶枚举、未再委派；唯一写入对象为本报告。
旧 [K] 的全层几何满像与点阶读取、旧 [G] 的原模型识别作为给定依赖消费，不重新授票。

## 2. [F] 的准确命题、假设与依赖图

第一层命题固定素数 $\ell\ge5$，对每个精确 $d\in\mathbb Z_\ell^\times$、每个 $n\ge1$，
以固定行列式切片上的归一化平移 Haar 测度给出 [F] 9–14 行的尾界。
准确结论是
$$\tau_n(d):=\Pr\{v_\ell\det(I-A)\ge n\}\le\frac{2\ell^{-\lceil n/2\rceil}}{1-\ell^{-2}}+\frac{\ell^{-n}}{\ell+1}.$$
第二层应用固定同一个 $\ell$，遍历 $q=p^a$、$p\ge5$、$p\ne\ell$、$T\in\mathbb F_q\setminus\{0,-27/256\}$。
只计光滑有限能级 $h$；计数误差常数可依赖 $\ell$，不可依赖 $p,T,q,r,m$。
以 $\mu_{q,\ell}$ 表示固定精确行列式 $q$、独立 Haar 平移向量的余核阶分布，则
$$\#\{h\ {\rm good}:v_\ell\operatorname{ord}(P_h)=r\}=q\mu_{q,\ell}(r)+O_\ell(q^{21/22}),\qquad
\#\{h\ {\rm good}:v_\ell\operatorname{ord}(P_h)\ge m\}\ll_\ell q\ell^{-m/2}+q^{21/22}.$$
依赖链为：矩阵两图计数 $\Rightarrow$ 一致异常质量；[K] $+$ 局部 Tate $\Rightarrow$ 五点 tame 覆盖；
该覆盖 $+$ 曲线 Weil 界 $\Rightarrow$ 几何共轭事件计数；最后只用一个有限层截断恢复真实点阶。

### 2.1 精确 Haar 切片与二次根数：通过

[F] 34–36 行正确：$|\mathrm{SL}_2(\mathbb Z/\ell^n)|=\ell^{3n}(1-\ell^{-2})$。
光滑约化逐层核大小为 $\ell^3$，固定精确 $d$ 的切片是该群的平移，故有限约化确实均匀。
这是直接定义的纤维测度，不是在全 $\mathrm{GL}_2$ Haar 测度中对零测事件做未定义条件化。
在 [F] 40–48 行，$a$ 可逆时 $e=(d+bc)/a$，目标准确等价于
$$a^2-(1+d)a+d+bc\equiv0\pmod{\ell^n}.$$
配方后若 $D\equiv0$，平方根数为 $\ell^{\lfloor n/2\rfloor}$；若 $v_\ell(D)=2k<n$，
每个约去 $\ell^{2k}$ 的单位平方根有 $\ell^k$ 个原根提升，至多两个单位平方根，故至多 $2\ell^k$。
奇数赋值无根；这些情况合给作者使用的 $2\ell^{\lfloor n/2\rfloor}$，没有缺失重根质量。
对每个 $(b,c)$ 用此上界、再放松 $a$ 可逆条件，质量至多 $2\ell^{-\lceil n/2\rceil}/(1-\ell^{-2})$。
在 [F] 50–52 行，$a$ 非单位强迫 $b$ 为单位，且目标只要求 $e=1+d-a$。
因此准确矩阵数是 $\ell^{n-1}(\ell^n-\ell^{n-1})$，除以上述切片大小恰得 $\ell^{-n}/(\ell+1)$。
两图不交且穷尽；这证明 [F] (1)，并统一覆盖 $d=1$ 及任意接近 $1$ 的 $d$。
$B_n$ 递减且其测度趋零，故 $\det(I-A)=0$ 的集合零测；有限余核上的阶赋值分布总质量为一。

### 2.2 Tame、亏格与几何 Frobenius 扭曲：通过

[K] 21–39 行给出所需全部层几何群及非异常读取；[K] 27 行给五个乘法坏点。
[F] 58–62 行的几何完成局部域具有代数闭剩余域，乘法约化因而 split，适用 Tate 一致化。
截面代表元 $z$ 与 Tate 参数 $Q$ 的 $\ell^n$ 次根连同已在常数中的单位根生成包含共同塔的局部扩张。
这是 $\ell$ 幂次扩张，因 $p\ne\ell$ 而 tame；不要求整个几何仿射群的阶素于 $p$。
几何 Galois 群 $G_n=(\mathbb Z/\ell^n)^2\rtimes\mathrm{SL}_2(\mathbb Z/\ell^n)$ 的阶为
$$D_n=(1-\ell^{-2})\ell^{5n}.$$
在五个分支点中，每点的 tame 分歧贡献至多 $D_n$，故 $2g_n-2\le3D_n$，正是 [F] 63–64 行。
对 [F] 66–76 行，$\Gamma_{n,q}$ 是大小恰为 $D_n$ 的单个几何群陪集，而不是整个算术群。
选择几何连通分量后，$c^{-1}\mathrm{Frob}_q$ 给同亏格、同次数的下降扭曲；其好底点纤维固定点数为
$|C_{G_n}(c)|$，当且仅当底点 Frobenius 属于 $c$ 的 $G_n$ 共轭类，否则为零。
这是几何 torsor 上的共轭方程计数；中心化子必须在 $G_n$ 内，作者确实这样使用。
扭曲曲线的射影点数与 $q+1$ 相差至多 $2g_n\sqrt q$；删去边界最多损失 $5D_n$ 点。
故作者单类误差分子 $1+2g_n\sqrt q+5D_n$ 正确，而且
$$\sum_{[c]\subset C}|C_{G_n}(c)|^{-1}=|C|/D_n\le1.$$
求和后没有多乘共轭类数或算术常数域次数；例如粗取绝对常数 $K=11$ 已足以支持 [F] (2)。
好点条件、异常条件与余核类阶条件均为 $G_n$ 共轭不变：平移共轭只给 $b$ 加入 $(A-I)$ 的像。

### 2.3 全部阶赋值、整体尾事件与小 $q$：通过

记 $E_{r,n}$ 为第 $n$ 层上非异常且余核类阶赋值等于 $r$ 的事件。
由 [K] 37–39 行，此事件准确读取真实阶；在 Haar 分布中也读取每个非异常提升的同一个阶。
真实计数与 $N_{E_{r,n}}$ 的差至多 $N_{B_n}$，相应概率差至多 $\tau_n(q)$。
分别对 $E_{r,n}$ 和 $B_n$ 用 (2)，得到 [F] 82–84 行，且常数同时适用于全部 $r\ge0$。
若 $r\ge n$，有限余核的大小小于 $\ell^n$，故 $E_{r,n}$ 为空；真实大阶质量仍在 $B_n$，并未遗漏。
对整体事件 $v_\ell\operatorname{ord}(P_h)\ge m$ 重复同一次分解，而不对单阶误差求和。
当 $1\le m\le n$，Haar 质量至多 $\tau_m(q)$，另有截断误差 $O_\ell(D_n\sqrt q+q\ell^{-n/2})$。
当 $m>n$，目标全部属于 $B_n$，同一误差足够；$m=0$ 直接由好点总数至多 $q$ 处理。
取 $n=\max(1,\lfloor\log_\ell(q)/11\rfloor)$ 后，$D_n\sqrt q$ 与 $q\ell^{-n/2}$ 均为 $O_\ell(q^{21/22})$。
对 $q\ge\ell^{11}$ 直接代入；对 $5\le q<\ell^{11}$，取 $n=1$，同样可用仅依赖 $\ell$ 的常数统一控制。
因此 [F] 86–93 行的全 $r$ 误差与全 $m$ 尾界成立；没有交换无限层极限，也没有将固定 $\ell$ 偷换成全素数联合结论。

## 3. [S] 的准确命题、假设与依赖图

参数始终为 $T=\varepsilon^3>0$；$\varepsilon=0$ 仅作局部解析极限，$H$ 在指定有界邻域中。
内部展开固定紧集 $K\subset\{XY\ne0\}$ 及固定导数阶 $r$；流逼近另固定慢时间上界 $L$ 并要求轨道留在紧域内部。
旋转声明只涉及 $(\varepsilon,H)=(0,-3)$ 附近的持续光滑实圆，不把孤立 node 也算作圆上点。
依赖链为：三次有理复合 $\Rightarrow$ 内部向量场；[G] 的原 $+P$ 字典 $\Rightarrow$ 准确 $3P$；
持续圆及 [A] 定向 $\Rightarrow$ 标量旋转缺陷；最后仅用 $g_\varepsilon(-2P)=P$ 得条件性拓扑障碍。

### 3.1 三次复合、辛号与有限慢时间：通过

从 [G] 145 行原式代入缩放，准确得到 [S] 32–33 行的 $f_\varepsilon,H_\varepsilon$；不变性及辛形式保持由原式直接继承。
独立逐次代入得到 [S] 38–39 行两式；特别是第二次第一坐标分母为 $B=\varepsilon Y-XA$，无符号遗漏。
$\varepsilon=0$ 时，$A=-Y$、$B=XY$、$\varepsilon XA^2-B=-XY$，在固定紧 torus 域一致非零。
故有理式在其邻域解析，任意固定 $C^r$ 阶 Taylor 余项均可一致控制；所得一阶系数准确为
$$V=(XY-X^2/Y,-X-Y/X).$$
直接收缩 $\Omega=dX\wedge dY/(XY)$ 给 $\iota_V\Omega=dH_0$，与 [S] 46–48 行约定完全一致。
[S] 50–55 行先要求固定有限慢时间内有紧域余量，离散 Gronwall 再以归纳保证迭代不离域；逻辑不循环。
这只证明其声明的 $O(\varepsilon)$ 有限时间误差，不提供增长时间或越过 torus 边界的控制。

### 3.2 缩放 Weierstrass、三阶退化与 Abel 符号：通过

原式除以 $\varepsilon^6$ 得 $W^2+HUW-W=U^3-\varepsilon U^2$；[G] 153 行缩放给
$U=1/Y$、$W=X(\varepsilon Y-1)/Y^2$，所以 [S] 59–64 行没有丢失 $W$ 的缩放因子。
广义 Weierstrass 的取负为 $(U,W)\mapsto(U,1-HU-W)$，故 $2P=(\varepsilon,0)$、$Q=-2P=(\varepsilon,1-\varepsilon H)$。
当 $\varepsilon=0$ 且纤维光滑，切线 $W=1-HU$ 使交点方程化为 $U^3=0$，故 $P$ 准确三阶。
当 $\varepsilon\ne0$，连接 $P$ 与 $2P$ 的斜率为 $-1/\varepsilon$；弦切公式准确给 [S] 68–69 行的 $3P$。
在有界 $H$、充分小 $\varepsilon$ 下，$1-\varepsilon H$ 一致非零，$3P$ 位于 $O$ 的固定正规参数邻域。
该处 $z=-U/W$ 给 $z(3P)=-\varepsilon/(1-\varepsilon H)$，且不变微分的首项为 $+dz$，所以 $\delta=-\varepsilon+O(\varepsilon^2)$。
也可在极限 torus 直接算得 $dU(V)=(X^2+Y)/(XY^2)$，而 $2W+HU-1=-(X^2+Y)/(XY^2)$。
因此在极限纤维的光滑部分 $\omega_{0,H}(V)=-1$；坐标表达式的可去点用非零纤维微分延拓，不能把负号翻成正号。
这不是在孤立 node 上给普通非零纤维微分赋值；可包含 node 的是第 3 节二维映射展开。

### 3.3 Acnode 附近的统一旋转缺陷：通过

[S] 79–83 行由隐函数定理给 $a=1-\varepsilon/3+O(\varepsilon^2)$、$H_c=-3-\varepsilon+O(\varepsilon^2)$。
独立求导得到所列 $DV(1,-1)$ 及特征值 $\pm i\sqrt3$；该点在 torus 内，局部映射展开可以包含它。
完成平方的 cubic 在中心准确为 $(U+1)^2(U+1/4)$，node 与持续圆的 simple root 有正距离。
在小固定参数矩形中，有限 $U$ 段用正下界、无穷端用二次首项保证 $G(U)>0$。
参数 $U=r+s^2$、$Z=s\sqrt{G}$ 给 $\omega=ds/\sqrt{G(r+s^2)}$；在 $t=1/s$ 图微分为非零解析的 $-dt/\sqrt{t^4G}$。
因此整个紧圆、微分和周期联合解析，周期具有统一正下界；中心周期准确为 $2\pi/\sqrt3$。
[A] 135–141 行的正向是 $s$ 从 $-\infty$ 到 $+\infty$，正是此处微分的正向。
代入 $w_-=-\varepsilon a$ 得 [S] 96 行的角端点，极限为 $2/3$；没有换成互补角 $1/3$。
群加法先给 $3\rho-\delta/\mathcal P\in\mathbb Z$，连续性与该端点固定该整数为 $2$。
再用 $\mathcal P_\varepsilon(H)=\mathcal P_0(H)+O(\varepsilon)$ 得 [S] 97–100 行的一致缺陷公式。
$$\frac{\rho_\varepsilon(H)-2/3}{\varepsilon}=-\frac1{3\mathcal P_0(H)}+O(\varepsilon).$$
中心系数为 $-\sqrt3/(6\pi)$，亦等于直接微分该端点角所得的系数，符号与倍数相互吻合。
正则时第二圆可由群平移与持续圆识别，故平移角相同；这不提供收缩 oval 的统一坐标。

### 3.4 保持 terminal 分离的条件性障碍：通过

代入 $U=\varepsilon\xi,W=1+\varepsilon\zeta$ 后除去公共因子 $\varepsilon$，准确得到 [S] 109 行的严格变换方程。
$P$ 与 $Q$ 的边界值分别为 $(0,0)$ 和 $(1,-H)$，对所有有限 $H$ 均不同。
旧准确 $+P$ 字典给 $g_\varepsilon(Q_\varepsilon)=Q_\varepsilon+3P_\varepsilon=P_\varepsilon$，不需要全图提升的未证公式。
在任意固定相容度量中，若沿这两个截面声称趋恒等，就有 $d(P_\varepsilon,Q_\varepsilon)\to0$，与不同极限点矛盾。
一般 Hausdorff 表述使用 [S] 118 行的联合连续极限：$g_0=\mathrm{id}$ 与极限唯一性直接迫使 $P_0=Q_0$。
这里不把 Hausdorff 自动等同于可度量，也不允许用依赖 $\varepsilon$ 的退化度量偷换所称一致性。
故 [S] 12–17、114–120、124–128 行的条件 NO-GO 没有越称所有极限模型不存在。

## 4. 必要修正、未消费风险与处置

必要数学修正：两件均无；上述展开只是补明其证明中压缩的计数、量词与定向步骤，不是追加科学假设。
[F] 没有证明精确余核质量表、全素数联合分布或原状态权重合并；本次通过不解除这些未做事项。
[S] 没有构造完整匹配理论、增长时间极限或边界全图提升；条件反例不以这些未证事项为前提。
本席没有核新意、可支撑正文篇幅或外源强包含性；两项短数学资产不能据此自动升级独立长文中心。
不修两作者源，不回写旧接受件、锁、FAIL、入口或索引；本报告完成后以单独 SHA-256 回报冻结。

[F]: PAPER31_QPI_FIXED_DETERMINANT_TAIL_PAPER_TEST_V1_20260912.md
[S]: PAPER31_QPI_SMALL_T_TERMINAL_COLLISION_PAPER_TEST_V1_20260912.md
[K]: PAPER31_QPI_KUMMER_MATHEMATICS_DISPOSITION_V1_20260909.md
[G]: PAPER31_QPI_REAL_COMPONENT_RETURN_GEOMETRY_V1_20260912.md
[A]: PAPER31_QPI_REAL_GEOMETRY_TWIST_MATH_REVIEW_V1_20260912.md
