# Paper 30：素数幂首层内部共振结构的独立核查

日期：2026-09-07。核查者：非作者代理
`p30_twist_root_counterexample_probe`。
本轮完整读取 `proof-writer` 技能及指定作者稿后，逐项核查新的证明。

## Claim and Status

**`PASS / PROVABLE AS STATED`：十五项限定核查全部通过。**
未发现须修改输入的数学缺口；命题的量词、对象及边界均保持不变。

接受的对象是 $s=p^a$、$p$ 为奇素数、$a\ge2$ 时，
采用真实阶数 $s$ 的传播子得到的第一个内部 forcing
$\mathcal B_{p\mid s}$，以及实际内部模态 $V_p$。
具体通过的结论包括

$$
\overline{h^{-m}\mathcal B}(L)=(-1)^{m+1}(2-L^m),
\qquad
\overline{h^mV_p}(L)=\frac{(-1)^m}{2}(2-L^m),
\quad m=(p-1)/2,
$$

相应 Newton 单边、全部根简单及局部 Frobenius 因子型。

**本核查不把 $\mathcal B_{p\mid s}$ 当成完整 $C_s$。**
它不接受、也未核查完整 $C_{p^a}$ 的 Newton 多边形、平方自由性、
根实性或 $C_{p^a},Q_{p^a}$ 互素性。

## Input and Independence

唯一作者输入：
[素数幂首层局部结构作者稿 V1](PAPER30_TWIST_PRIME_POWER_LOCAL_STRUCTURE_PROBE_V1_20260907.md)。

本轮全文读取 $430$ 行，确认 SHA256 为

`f9dd643975ecbdb08a1512aacbebb692b96e84fceb8ab66fd69baecbbba6b616`。

核查者未参与该稿的构造或写作，不把作者与主控的交叉计算当作本次独审。
仅新建本报告，不改作者输入、旧稿、脚本或状态入口。
已接受的奇素数完整首项结论没有重审。

## Assumptions and Notation

固定 $s=p^a$、奇素数 $p$、$a\ge2$，$\zeta$ 为任意本原 $s$ 次单位根。
令

$$
\pi=\zeta-1,\quad h=2-\zeta-\zeta^{-1}=-\pi^2/\zeta,\quad
\rho=-h,\quad L=\rho\lambda,
$$
$$
m=(p-1)/2,\qquad M=p^{a-1}m,\qquad
K^+=\mathbb Q_p(h),\quad\mathcal O^+=\mathbb Z_p[h].
$$

赋值取 $v_h(h)=1$。本报告用 $\epsilon_m=(-1)^{m+1}$ 表示作者的符号常数，
避免与其他任务的参数中心记号混用。

作者的 $\mathcal B(H,L)$ 是独立形式变量 $H$ 下的有限整块；
$\mathcal B(h,L)$ 才是在真实圆分点取值的缩放内部 forcing。
实际 $p$ 模态满足 $p<s$，因此没有删除 $V_p$。

## Dependency Map and Check List

| 编号 | 检查内容 | 结果 |
| --- | --- | --- |
| 1 | 内部 forcing 与完整首项的对象区分 | PASS |
| 2 | 物理规范、$\rho,L$ 缩放及 $V_p$ 的符号 | PASS |
| 3 | 实局部环、均匀化元及全部本原分子 | PASS |
| 4 | 塔中的传播子估值与真实高度 $M$ | PASS |
| 5 | $d_p(H)\bmod p$ 及除以 $h^{2m}$ | PASS |
| 6 | 小于 $p$ 的递推整性与次数界 | PASS |
| 7 | 非驻值 Euler 缺陷身份 | PASS |
| 8 | 首个反射缺陷的 $H^m$ 系数 | PASS |
| 9 | 平方传播子的有限低阶解 | PASS |
| 10 | 缺陷有限和及常数 $2$ | PASS |
| 11 | 形式模 $p$ 到真实局部整除 | PASS |
| 12 | $V_p$ 极点及返回物理 $v_p$ | PASS |
| 13 | Newton 端点、度数和根赋值 | PASS |
| 14 | 剩余可分性与特征零平方自由 | PASS |
| 15 | Frobenius 轨道、Hensel 因子型及 $p=3$ 边界 | PASS |

## Independent Proof Checks

### 1–5. 对象、尺度与分歧高度

在真实物理递推中写

$$
v_n=-\frac{E_{n-1}/2+\lambda F_{n-2}}{D_n}.
$$

缩放 $t=\rho x$ 后，$V_n=\rho^nv_n(L/\rho)$、
$d_n=-D_n/h=D_n/\rho$，因此同样有
$V_n=-(E_{n-1}/2+LF_{n-2})/d_n$。
内部 forcing 的定义
$\mathcal B=-E_{p-1}-2LF_{p-2}$ 正好给出

$$
V_p=\frac{\mathcal B(h,L)}{2d_p(h)}.
\tag{A}
$$

这里的正号与因子 $2$ 均核对正确。
$D_p\ne0$，所以这不是共振规范 $V_p=0$ 的应用。

本轮在作者官网核对
[Milne，Algebraic Number Theory，命题 6.2](https://www.jmilne.org/math/CourseNotes/ANT.pdf#page=98)：
其结论确实覆盖任意素数幂阶，
给出整数环、完全分歧以及剩余域。
因此 $v_\pi(p)=\varphi(p^a)$，由 $h=-\pi^2/\zeta$ 得 $v_h(p)=M$。
实子域次数为 $M$，$h$ 在其中赋值为 $1$，所以是均匀化元；
其整数环为 $\mathbb Z_p[h]$，剩余域为 $\mathbb F_p$。
没有把完整圆分环按 $h$ 的商当作域。

若 $n=p^bj$、$p\nmid j$，则 $\zeta^{p^b}$ 生成阶数 $p^{a-b}$ 的下层。
塔的相对分歧指数为 $p^b$，所以

$$
v_\pi(1-\zeta^n)=p^b,\qquad
v_\pi(D_n)=2p^b,\qquad v_h(d_n)=p^b-1.
$$

这些论证对任意本原 $\zeta$ 成立，不依赖某个固定互素分子。

Chebyshev 多项式在特征 $p$ 中满足
$B_p(H)=(2-H)^p=2-H^p$：
这也可由 $z^p+z^{-p}=(z+z^{-1})^p$ 和整数递推直接推出。
因此 $d_p(H)\equiv-H^{p-1}\pmod p$。
这里

$$
M=p^{a-1}m\ge pm>2m=p-1
$$

对全部奇素数及 $a\ge2$ 均严格成立。
代入真实 $H=h$ 后，$p$ 项除以 $h^{2m}$ 仍至少含一个 $h$，
从而

$$
d_p(h)/h^{2m}\equiv-1\pmod h.
\tag{B}
$$

这一估值比较保留了真实 $p$，不是提前设 $p=0$。

### 6–7. 整性与非驻值 Euler 缺陷

低于 $p$ 阶时，$d_n(0)=-n^2$ 是 $p$-单位，
所需有限指数只使用小于 $p$ 的阶乘。
因此 $V_n(H,L)$、$\mathcal B(H,L)$ 及有限 action
均属于 $\mathbb Z_p[L][[H]]$，且 $L$ 次数有一致有限界。
给一步幅度权重 $1$、$L$ 权重 $2$ 后，
$\deg_L\mathcal B\le m$。

对作者的有限 $\Phi$ 直接求导，
并用实际三角分支在指标 $p-i$ 的方程消去势项，可得

$$
\Phi_{v_i}
=\frac{d_i(H)-d_{p-i}(H)}2V_{p-i}.
$$

所以 off-$H$ 分支一般不是临界点；作者没有把它当作临界点。
把 $v_i,b,L$ 的权重分别取为 $i,1,2$，Euler 恒等式给出

$$
p\Phi=\sum_{i=1}^{p-1}iV_i\Phi_{v_i}
+b\Phi_b+2L\Phi_L.
$$

在 $b=1$ 时，最后两项之和为 $-\mathcal B/2$。
故

$$
\mathcal B=-2p\Phi+
\sum_{i=1}^{p-1}i(d_i-d_{p-i})V_iV_{p-i}.
\tag{C}
$$

输入式 (11) 的符号和因子完全正确。
此推导保留了总变量权重项，不依赖错误的 $p$ 周期反射假设。
在已知整性后再模 $p$，也是合法顺序。

### 8. 首个反射缺陷在 $H^m$

在 $\mathbb F_p[[\eta]]$ 中置
$z=1+\eta$、$H=-\eta^2/(1+\eta)$。
若一个非零 $H$ 级数的最低次数是 $k$，代入后的 $\eta$ 阶为 $2k$，
故该代入是单射。

作者的因式分解

$$
d_i-d_{p-i}
=\frac{(z^p-1)(z^{i-p}-z^{-i})}{H}
$$

逐项展开正确。
模 $p$ 后，第一因子是 $\eta^p$，
第二因子的线性项是 $2i\eta$，分母首项为 $-\eta^2$。
因此总首项是 $-2i\eta^{p-1}$。
与 $H^m$ 的首项 $(-1)^m\eta^{p-1}$ 比较，得到

$$
d_i-d_{p-i}
=2\epsilon_m iH^m+O(H^{m+1}).
\tag{D}
$$

不存在更低的 $H$ 项。
去掉首项后剩余表达式仍来自 $H$ 的多项式；
由单射及其偶数赋值，余项确实从 $H^{m+1}$ 开始，
不是只得到一个不够精确的 $\eta$ 余项。
此论证也覆盖 $p=3$ 的 $m=1$。

### 9–10. 有限和独立重算与常数 $2$

在 $H=0$，平方传播子解

$$
W=-\log(1-x/2+(1-4L)x^2/16)
$$

直接满足低阶三角方程。
将二次多项式写为 $(1-r_1x)(1-r_2x)$，
便有 $W_i=(r_1^i+r_2^i)/i$，$i<p$。
这些系数的 $p$-整性不需要 $W_p$ 整。

令 $\delta=r_1-r_2$，$\delta^2=L$。
在特征 $p$ 中

$$
r_1^p+r_2^p=\frac12,\qquad
r_1^p=\frac14+\frac{\delta L^m}{2},\qquad
r_2^p=\frac14-\frac{\delta L^m}{2}.
$$

独立计算交叉几何和得到

$$
\sum_{i=1}^{p-1}r_1^ir_2^{p-i}
=\frac{r_1^pr_2-r_1r_2^p}{\delta}
=\frac{L^m-1}{4}.
$$

另一个交叉和相同；纯项的和为
$(p-1)(r_1^p+r_2^p)=-1/2$。
又 $i^2/[i(p-i)]=-1$，故

$$
\sum_{i=1}^{p-1}i^2W_iW_{p-i}
=\frac12-\frac{L^m-1}{2}
=\frac{2-L^m}{2}.
\tag{E}
$$

该总和原本就是 $L$ 的多项式；
中途在 $\delta\ne0$ 的局部化计算，最后由单射返回，
所以 $L=0$ 没有被遗漏。
式 (D)、(E) 代入式 (C)，恰好给出
$\epsilon_mH^m(2-L^m)$，没有多一个或少一个因子 $2$。

### 11–12. 真实整除、内部极点及物理坐标

输入的形式表达式

$$
\mathcal B(H,L)=
\epsilon_mH^m(2-L^m)+H^{m+1}R(H,L)+pT(H,L)
$$

中 $R,T$ 可取整，且 $L$ 次数一致有界。
代入拓扑幂零元 $h$ 后，余项不会因隐藏的 $1/p$ 而降阶：
低块的构造此前已保证所有系数整。
由于 $M>m$，$pT/h^m$ 至少含 $h$，得到所述首层归一化。

将它和式 (A)、(B) 合并，

$$
h^mV_p
=\frac{h^{-m}\mathcal B}{2(d_p/h^{2m})}
\equiv-\frac{\epsilon_m}{2}(2-L^m)
=\frac{(-1)^m}{2}(2-L^m).
$$

所以当 $\bar L^m\ne2$ 时极点阶恰为 $m$，
不是仅给出一个上界。
对物理整数 $\lambda$，$L=-h\lambda\equiv0$，
故 $v_h(V_p)=-m$，再由 $V_p=\rho^pv_p$ 得
$v_h(v_p)=-m-p$。
这一结论适用于实际非共振系数，不是完整共振首项的根值结论。

### 13–14. Newton 边、次数与简单性

归一化余式的常数项和 $L^m$ 项都是单位，
中间系数的余式为零。
因此 $\mathcal B(h,L)$ 两端点赋值恰为 $m$，
中间系数赋值至少为 $m+1$，Newton 下凸包确为水平边。
最高项没有消失，所以次数恰为 $m$。

坐标关系逐项给出

$$
[L^j]\mathcal B(h,L)=\rho^{p-1-j}[\lambda^j]\mathcal B_{p\mid s},
$$

其赋值差为 $2m-j$。
原坐标系数的下界因此是 $j-m$，两端取等号，
得到 $(0,-m)$ 到 $(m,0)$ 的边。
对归一化多项式，根的 $L$ 赋值若正，则常数项唯一最小；
若负，则最高次项唯一最小，两种情形都不能相消。
所以所有根满足 $v_h(L)=0$、$v_h(\lambda)=-1$。

余式 $2-L^m$ 的根非零，导数 $-mL^{m-1}$ 在根处非零；
次数保持且最高项为单位，故归一化判别式为单位。
特征零中不存在重复根。
这里的多项式始终是 $\mathcal B_{p\mid s}$，未换成完整 $C_s$。

### 15. Frobenius 与局部因子型

对每个剩余根 $\alpha^m=2$，

$$
\alpha^p=\alpha^{2m+1}=4\alpha,\qquad
\alpha^{p^k}=4^k\alpha.
$$

因为 $\alpha\ne0$，轨道长度恰好是
$f=\operatorname{ord}_{\mathbb F_p^\times}(4)$，不是仅整除 $f$。
$4^m=1$ 又给出 $f\mid m$。
故可分余式的不可约因子有 $m/f$ 个，次数全部为 $f$。

本轮另核对了
[Milne，Hensel 因子提升定理 7.33](https://www.jmilne.org/math/CourseNotes/ANT.pdf#page=123)
及所在小节的完成离散赋值环假设。
输入先除以单位最高次系数使多项式首一，
再对互素剩余因子逐个提升，条件全部满足。
提升因子若可约，首一因子的根仍整，
其系数就在整数环中，约化将与剩余因子的不可约性矛盾。
所以这些确为完成局部域上的不可约因子次数。

对 $p\ge5$，$4\ne1\pmod p$，故 $f>1$，没有 $K^+$ 根。
同时 $L^m$ 在 $\mathbb F_p$ 只能取 $0,\pm1$，不能取 $2$；
这说明每个 $L\in\mathcal O^+$ 都具有上述首层极点。
当 $p=3$ 时 $f=m=1$，例外剩余类是 $L=2$；
作者没有把“每个整数 $L$ 都有极点”套到该类。
但物理整数 $\lambda$ 给出的 $L\equiv0$ 仍在已证明的非例外范围内。

## Exact Verification Actually Run

除上面的全量词推导外，本次实际运行两项自由符号身份检查：

- 在三个系数阶的有限 action 中，以自由 $d_1,d_2,b,L$ 重新构造三角分支，
  精确验证带全部非驻值项的 Euler 缺陷，残差为零。
  传播子未指定为某个素数幂的实际数值，这不是新增分母样本。
- 用自由 $\delta,Z$，其中 $Z$ 仅代表 $L^m$，
  重新计算交叉幂和；结果严格为 $(Z-1)/4$，
  完整缺陷和严格为 $(2-Z)/2$。

输出为
`FREE_PROPAGATOR_THREE_MODE_EULER_DEFECT_PASS`、
`GENERAL_DEFECT_POWER_SUM_PASS`，
并核对坐标赋值转换为 $j-m$。
没有数值根、素数列表、实验脚本或旧根诊断重跑。
一般命题不是由这些有限身份检查外推，而由前述逐步证明核查承担。

## Corrections or Missing Assumptions

无须修改作者输入或增加科学假设。
常数 $2$ 与此前闭合素数首项的常数 $1$ 不同，原因明确：
这里 $p$ 的真实高度为 $M>m$，非驻值反射缺陷却已在 $h^m$ 出现。
不能使用错误的 off-$H$ 驻值性抹去该缺陷，
也不能把素数情形的 $p\sim h^m$ 移入当前素数幂。

## Open Risks and Acceptance Boundary

- 通过的是第一个内部 forcing、其局部因子型以及 $V_p$ 的首层极点。
- 从 $V_p$ 起出现的非整内部模式及 $p!$ 层，仍阻止直接沿用素数分母的单位递推。
- 更高内部模态、完整 $C_{p^a}$、完整 $Q_{p^a}$ 均不在本次验收范围内；
  本报告不把内部多项式的根当作完整首项根。
- 不接受新的全根实性、全部合数平方自由性或共同根排除声明。
- 仅新增本报告，不改输入、旧稿、锁、状态入口或论文／批次验收状态。
