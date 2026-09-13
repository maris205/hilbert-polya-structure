# Paper30：三点同步混合的仿射生成链与组合步骤独立数学检查

日期：2026-09-06。`INDEPENDENT_MATHEMATICAL_CHECK`。
仅检查数学，不作查新、容量、立项、Route 或产物验收评价。

## Claim

核查如下量词不变的命题：对每个整数 $d\ge2$，存在仅依赖 $d$ 的
$\delta_d>0$，使每个素数 $p\ge16d^2$ 及每个首一、次数恰为 $d$ 的
$P\in\mathbb F_p[x]$，对应
$$
H_j(x,y)=(P(x)+j-y,x),\quad j=0,1,
$$
在 $\Omega=\operatorname{Conf}_3(\mathbb F_p^2)$ 上的同词、逐点同时作用具有
$$
M=\tfrac12I+\tfrac18\sum_{j=0}^1(H_j+H_j^{-1}),\qquad
\mathcal D_M(f)\ge\delta_d\operatorname{Var}(f).
\tag{C}
$$
算子表示按下文统一约定理解。命题允许全部低阶系数随 $p$ 任意变化，
不是固定某一个整数多项式后取模的较弱结论。

## Status

`PROVABLE AS STATED`。对所绑定作者主稿，未发现定理级缺口。

中心化、差分词、固定整数剪切矩阵、两条外部谱隙定理、全表示转移、词长能量
比较及最终混合界均已独立核查。完整读取全次数商空间证明，并核对其与主稿的
转写、量词、复值函数及能量规范相匹配；本报告不复制那份已单独承担的商空间证明。

唯一发现项是外部论文标题的编辑性转写，不影响定理、参数范围或常数；见末节。
没有以三点谱隙反推整个置换群 Cayley 扩张，也没有假设特殊仿射群对三点传递。

## Assumptions and bound inputs

- $d\ge2$ 固定后选择常数；不要求这些常数在 $d\to\infty$ 时保持一致。
- $p\ge16d^2$ 为素数，故 $p>d$ 且 $p>2$。
- 配置为三个有序互异点，三个点接受同一随机动作。
- 使用均匀概率测度、复数 $L^2$ 空间、规定的懒惰对称概率律。
- 所有依赖均为数学输入，不把原文的作者状态当成独立证明。

本报告全文读取并绑定：

| 文件 | 行数 | SHA256 |
| --- | ---: | --- |
| [统一作者主稿 V1](PAPER30_UNIFORM_THREE_POINT_MIXING_PROOF_V1_20260906.md) | 554 | `1b2e03a56164f62d02fa8e11ed63b8169105be3a831d0148c3fd72b1896398ba` |
| [全次数商空间证明](PAPER30_ALL_DEGREE_THREE_POINT_QUOTIENT_PROBE_20260906.md) | 351 | `e57ea08ed8c52632ed84e9ae037be5c80633610b235a7a60a15d0b672d64c62e` |

主稿 Steps 6–7 另已给出二次商空间所需的 Jacobi 和、纤维计数与共线逃逸证明；
本报告检查该转写，不要求重开既有二次探针或重新计算数值数据。

## Notation

令 $\rho(T)f=f\circ T^{-1}$，于是 $\rho$ 是酉表示。由于所有所用概率律
对称，用 $f\circ T$ 或 $f\circ T^{-1}$ 定义相应平均算子相同。
对单个置换定义
$$
\mathcal E_T(f)=\frac12\|\rho(T)f-f\|_2^2
=\frac12\|f\circ T-f\|_2^2.
$$
对对称律 $\mu$，写 $\mathcal D_\mu(f)=\langle f,(I-\rho(\mu))f\rangle$。
设 $G=\operatorname{ASL}_2(\mathbb F_p)$，$E=|G|^{-1}\sum_{g\in G}\rho(g)$，
即 $G$-不变函数空间的正交投影。

## Proof strategy

从规定的两个非线性生成元精确提取固定的仿射概率律。先以正则表示定理控制
$I-E$ 部分，再用单独证明的商空间能量界控制 $E$ 部分。逐个核对归一化系数，
最后由得到的全局 Poincaré 不等式推导不可约性，而非预先假设不可约性。

## Dependency map

1. 中心化 $\Rightarrow$ 高阶差分的常数项只依赖 $d$。
2. 差分词 $\Rightarrow$ 四个仿射动作的长度仅依赖 $d$。
3. BG 固定整数矩阵定理 $+$ 有限例外素数连通性 $\Rightarrow$ 线性顶谱隙。
4. 线性投影的正性 $+$ 精确点转移原子 $\Rightarrow$ LV 正则表示范数隙。
5. 有限群表示分解 $+$ 词长比较 $\Rightarrow$ $\|f-Ef\|_2^2$ 控制。
6. 全系数商空间界 $+$ 正交分解 $\Rightarrow$ (C)。
7. 懒惰正性与状态空间大小 $\Rightarrow$ TV 上界；支持计数 $\Rightarrow$ 对数下界。

## Proof and independent verification

### 1. 中心化没有隐藏的长词或系数限制

若 $a_{d-1}$ 为次高项系数，取 $s=-a_{d-1}/d$ 和
$C_s(x,y)=(x+s,y+s)$，则
$$
C_s^{-1}H_jC_s=(Q(x)+j-y,x),\qquad Q(x)=P(x+s)-2s.
\tag{1}
$$
直接展开得到 $[x^{d-1}]Q=ds+a_{d-1}=0$。$p>d$ 保证可以除以 $d$。
同一个 $C_s$ 同时共轭两个生成元、逆元和恒等动作；它在 $\Omega$ 上是保均匀测度
置换，故这是酉重标记，不需要把 $C_s$ 表示成短词。
它没有把任意首一多项式的量词改成预先中心化的子族。

以下在中心化坐标工作，并将 $Q$ 记为 $P$。

### 2. 差分词及整数常数完全吻合

取复合顺序从右到左。逆映射为 $H_j^{-1}(x,y)=(y,P(y)+j-x)$，所以
$$
X=H_1H_0^{-1}=(x+1,y),\qquad
Y=H_1^{-1}H_0=(x,y+1).
\tag{2}
$$
令 $H=H_0$，将坐标逐项代入得
$$
Y^{-1}HXH^{-1}=(x+P(y+1)-P(y),y).
$$
对任意剪切 $S_R=(x+R(y),y)$，又有
$$
Y^{-1}S_RYS_R^{-1}=(x+R(y+1)-R(y),y).
\tag{3}
$$
因此作者的 $S_r$ 确为 $(x+\Delta^rP(y),y)$。词长递推为
$\ell_1\le6$、$\ell_{r+1}\le2\ell_r+4$，解为
$\ell_r\le10\,2^{r-1}-4$。

中心化后，除了最高项 $x^d$，全部项的次数至多 $d-2$，会被 $d-1$ 次差分消去。
为独立验证常数，采用下降阶乘基：
$$
x^d=(x)_{\underline d}+\binom d2(x)_{\underline{d-1}}
+\text{次数至多 }d-2\text{ 的项},\qquad
\Delta(x)_{\underline r}=r(x)_{\underline{r-1}}.
$$
于是
$$
\Delta^{d-1}P(x)=kx+c_d,\qquad
k=d!,\qquad c_d=\binom d2(d-1)!=\frac{d!(d-1)}2.
\tag{4}
$$
这里 $c_d$ 为固定的非负整数；使用其整数词长，不选随系数或素数变化的指数代表。
这给出
$$
U=X^{-c_d}S_{d-1}=(x+ky,y),\quad
V=H^{-1}U^{-1}H=(x,y+kx),
\tag{5}
$$
$$
\ell(U)\le L_d=10\,2^{d-2}-4+2c_d,\qquad
\ell(V)\le L_d+2.
\tag{6}
$$
$V$ 的公式由 $P(x)-(P(x)-y-kx)=y+kx$ 精确相消。
特别地 $d=2$ 给出 $k=2,c_d=1,L_d=8$，递推没有越界或空下标问题。

### 3. Bourgain–Gamburd 的准确适用性

实际直接读取出版 PDF 的定义段及 Theorem 1，定位为印刷页 626。
其适用对象是固定整数矩阵生成的非初等子群的模素数 Cayley 图扩张族。
本题使用固定的对称集合
$$
\left\{\begin{pmatrix}1&k\\0&1\end{pmatrix}^{\pm1},
\begin{pmatrix}1&0\\k&1\end{pmatrix}^{\pm1}\right\},\qquad k=d!.
$$
这与可能随 $p$ 变化的 $P$ 的系数无关。
[Bourgain–Gamburd, Theorem 1, p.626](https://annals.math.princeton.edu/wp-content/uploads/annals-v167-n2-p07.pdf)。

作者的两个锥 ping-pong 证明成立，包含不同首尾生成元的共轭处理。
另一个直接核查是：在上半平面作用中，$U_k,V_k,U_kV_kU_k^{-1}$ 分别是
固定 $\infty,0,k$ 的抛物元。这三个互异边界点均为该群的极限点，
所以满足原定理的非初等定义。没有把仅“两个矩阵不交换”当作充分条件。

由于 $p>d$，$k\ne0$，两种剪切的幂给出所有上下初等幺幂矩阵，
它们通过行消元生成 $\operatorname{SL}_2(\mathbb F_p)$。这一步只用于确认
每个有限例外素数的图连通，不把长度可能依赖 $p$ 的幂加入统一词长比较。

设 $\sigma_d$ 为上述四元均匀律。BG 的渐近顶谱隙与有限例外的正顶谱隙取最小值，
得到仅依赖 $d$ 的 $\epsilon_d>0$，对每个 $p>d$ 都成立。
这里要求的是 $1-\lambda_{\max}$，不是未经处理的双侧范数隙。
主稿随后的懒惰线性投影正好处理了这一差别。

### 4. Lindenstrauss–Varjú 的范数、维数及原子均匹配

取
$$
\nu_d=\tfrac12\delta_e+
\tfrac1{16}\sum_{T\in\{X,Y,U,V\}}(\delta_T+\delta_{T^{-1}}).
\tag{7}
$$
其线性投影是 $\tfrac34\delta_I+\tfrac14\sigma_d$。
由于 $\sigma_d$ 自伴且谱在 $[-1,1]$，投影算子的谱在 $[1/2,1]$，
零均值空间的范数隙因此至少为 $\epsilon_d/4$。没有以 BG 的顶谱隙直接
冒充一个可能受负特征值影响的范数隙。

实际直接读取 LV 出版 PDF 的表示定义与 Theorem 2（印刷页 975–976）。
定理对 $\mathbb F_p^r\rtimes\operatorname{SL}_r(\mathbb F_p)$ 的概率律给出
$$
1-\|L_0(\nu)\|\ge c_r
\min\{1-\|L_0^\theta(\nu)\|,\,1-\alpha\},
\qquad
\alpha=\max_{a,b}\mathbb P_{g\sim\nu}(ga=b).
\tag{8}
$$
此处代入的仿射维数是 $r=2$，不是多项式次数 $d$；$\alpha$ 属于自然平面
作用，不是 $\Omega$ 上的原子，也不是群上最大单个测度质量。
[Lindenstrauss–Varjú, Theorem 2, p.976](https://www.numdam.org/item/AFST_2016_6_25_5_969_0.pdf)。

对 $a=b$，四个非零平移均不固定 $a$，总质量 $1/4$ 被排除，概率至多 $3/4$。
对 $a\ne b$，恒等项质量 $1/2$ 被排除，概率至多 $1/2$。原点被四个线性
剪切固定，达到概率 $3/4$，故 $\alpha=3/4$ 精确成立。
由 (8) 得到
$$
\gamma_d=c_2\min\{\epsilon_d/4,1/4\}>0.
\tag{9}
$$
原文使用计数测度，主稿使用均匀概率测度；在同一有限空间上二者仅相差全局正标量，
不改变算子范数或正交于常数的空间。没有归一化障碍。

### 5. 从正则表示到全部仿射轨道，而非错误地假设传递性

有限群的每个不可约酉表示均出现于正则表示。去掉所有平凡表示分量后，
任何酉表示的 $\nu_d$ 范数至多 $1-\gamma_d$。对配置表示，相应补空间就是
$\ker E$；$E$ 的像一般有多个轨道常数分量，并不只有全局常数。
于是
$$
\gamma_d\|f-Ef\|_2^2\le\mathcal D_{\nu_d}(f).
\tag{10}
$$
$E$ 是群平均正交投影，故这一步对实际轨道质量自动成立，不需假定所有轨道等大。
它不把一、二点表示的谱隙误用于三点张量表示中的新不变量。

### 6. 词长能量比较中的每个系数

归一化给出
$$
\mathcal D_M=\frac14(\mathcal E_{H_0}+\mathcal E_{H_1}),\qquad
\mathcal D_{\nu_d}=\frac18(\mathcal E_X+\mathcal E_Y+\mathcal E_U+\mathcal E_V).
\tag{11}
$$
对长度 $\ell$ 的词 $W$，酉表示的望远镜和及 Cauchy–Schwarz 不等式给出
$$
\mathcal E_W(f)\le\ell\sum_{i=1}^{\ell}\mathcal E_{T_i}(f)
\le\ell^2(\mathcal E_{H_0}(f)+\mathcal E_{H_1}(f))
=4\ell^2\mathcal D_M(f).
\tag{12}
$$
逆元能量等于原元能量；各中间词是保均匀测度置换，故望远镜项的范数保持。
代入长度 $2,2,L_d,L_d+2$，得到
$$
\mathcal D_{\nu_d}(f)\le C_d\mathcal D_M(f),\qquad
C_d=\frac{8+L_d^2+(L_d+2)^2}{2}.
\tag{13}
$$
作者没有遗漏两种逆动作的权重，也没有把词长线性界误写成适用于任意词的上界。

### 7. 商空间输入的精确范围及转写核对

完整读取 351 行商空间文件，其命题为：$d\ge3$、每个首一 $P$、
$p\ge16d^2$、每个仿射不变复函数 $g$，有
$\operatorname{Var}(g)\le18\mathcal E_H(g)$，故可用安全常数 $24$。
它不要求 $P$ 中心化，因而适用于步骤 1 的全部中心化多项式。

核对主稿 Steps 4–7 与该文件后，以下接口一致：

- 非共线轨道质量 $p/(p^2-2)$、共线轨道质量 $1/(p^2-2)$ 均相对于完整配置空间。
- 面积增量关于独立基点坐标的次数是 $d-2$，首项
  $\binom d2uv(u-v)$ 不依赖任何低阶系数。
- 非对称增量分布用 $1-\operatorname{Re}\widehat\eta$ 控制；删去零状态损失是
  $\max\eta$ 乘范数平方，前向和后向已含在能量中的 $1/2$ 内。
- 共线实际逃逸率可以随轨道标签变化，只用了共同下界 $1/2$。
- 最后一项利用平稳入流不等式，不以未经证明的细致平衡替代。
- 深输入为 $1\le d-2<p$ 时适用的加性 Weil 界。原文件已明确该条件；
  这里不重证这一深定理，也未把它应用到次数为零的二次情况。

二次情形由主稿 Step 6 单独处理：非零三次纤维的下界是
$p-2-2\sqrt p\ge p/2$（$p\ge29$），零纤维为 $3p-3$。
Jacobi 和的两个角色均非平凡，乘积角色也非平凡，故主稿给出的 Gauss–Jacobi
绝对值推导成立。由此 $V_N\le3\mathcal E_H(g)$，再结合共线逃逸得到
$\operatorname{Var}(g)\le23\mathcal E_H(g)$。原阈值 $p\ge16d^2$ 在 $d=2$
更强，因此两种次数范围合在一起确实给出
$$
\operatorname{Var}(g)\le24\mathcal E_H(g)
\quad(g=Eg),
\tag{14}
$$
没有把仅二次的旧命题当作全次数前提，也没有把完整函数空间的谱隙循环用来证明 (14)。

### 8. 最终常数、不可约性与混合阶

令 $g=Ef$、$h=f-g$。正交性及常数包含于 $\operatorname{im}E$ 给出
$$
\operatorname{Var}(f)=\operatorname{Var}(g)+\|h\|_2^2,
\qquad \|h\|_2^2\le(C_d/\gamma_d)\mathcal D_M(f).
$$
由酉性，$\mathcal E_H(h)\le2\|h\|_2^2$。因此
$$
\mathcal E_H(g)\le2\mathcal E_H(f)+4\|h\|_2^2
\le8\mathcal D_M(f)+4\|h\|_2^2.
$$
代入 (14) 后得到作者的精确安全分母
$$
\operatorname{Var}(f)\le
\left(192+97\frac{C_d}{\gamma_d}\right)\mathcal D_M(f),\qquad
\boxed{\delta_d=\left(192+97C_d/\gamma_d\right)^{-1}>0.}
\tag{15}
$$
$192=24\cdot8$、$97=24\cdot4+1$，不存在常数误算。

由于每个动作都是配置空间置换，均匀测度平稳。若有多个连通类，取其中一类的
指标函数会与 (15) 矛盾。因此不可约性是已经证明的后果，不是隐含前提。
懒惰算子是 $\tfrac12I$ 加一个范数至多 $1/2$ 的自伴算子，故谱在 $[0,1]$，
(15) 也给出零均值空间的范数隙。

配置数为 $N=p^2(p^2-1)(p^2-2)<p^6$。初始点质量相对于均匀测度的密度减一
具有平方范数 $N-1$，于是
$$
\|\mathcal L(Z_n)-u_p\|_{\rm TV}
\le\tfrac12\sqrt{N-1}(1-\delta_d)^n
\le\tfrac12p^3e^{-\delta_dn}.
\tag{16}
$$
反之，至多五个动作选择使时间 $n$ 的支持不超过 $5^n$，所以到达 TV 距离
$\varepsilon\in(0,1)$ 必须满足
$$
n\ge\frac{\log((1-\varepsilon)N)}{\log5}.
\tag{17}
$$
不要求不同随机词给出不同点。结合 $N\asymp p^6$，得到
$\Theta_{d,\varepsilon}(\log p)$，且对全部系数统一。∎

## Corrections or missing assumptions

没有需要改变科学结论的修正，也没有额外系数、传递性、可逆商链或固定整数提升假设。

一个编辑性发现：主稿的 Wan–Wang 题名写成 “Index bounds for character sums
of polynomials over finite fields”；所绑定商空间报告的准确题名为
“Index bounds for character sums with polynomials over finite fields”。应在获准后继文本
中将题名的 `of` 改为 `with`。作者、链接、使用的第一页式 (1) 及数学条件没有改变，
该题名修正不触发重证明。本报告没有编辑冻结主稿。

## Open risks and actual execution

- 对绑定主稿的上述数学链未留下开放义务；BG 与 LV 是明确使用的外部深定理，
  本报告核查其原文陈述和适用条件，不声称重新证明它们。
- 没有得到数值最优或显式可计算的 $\epsilon_d$；作者也没有作此主张。
- 不涵盖更高点数、扩域、非首一输入、较小素数或非懒惰单向概率律。
- 实际全文重读 `proof-writer/SKILL.md`，采用其量词、依赖及退化条件核查要求。
  BG 和 LV 原文均直接在线读取；LV 页图工具报内部错误，但该页完整正文和
  表示定义已由 PDF 文本成功读取，不影响已核验的定理内容。
- 未进行数值实验、矩阵拟合、外部写入、子代理派生或模型变更。
  仅新增本报告，未改作者稿、商空间稿、项目状态或任何已接受论文。
- 本结论仅为独立数学检查，不构成新意/价值/容量 PASS、正式立项或论文完成。
