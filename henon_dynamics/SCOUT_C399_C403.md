# C399–C403：指令优化后的第一轮候选筛选

日期：2026-09-05。研究基线：C394–C398，`34c3781c`。
指令优化提交：`b0cdadb99a1e8b56bf08b9a77e5d5e5a27a6bd1e`。
按 [批次工作流](../.agents/skills/henon-route-a-batch/references/WORKFLOW.md)
执行的只读初筛记录；不是冻结批次计划、论文、正式路线评估或发布证书。

## 当前结论与恢复位置

两个优先候选有完整问题和可检查的推导路径；一个重叠较大的备选，
一个尚无全局证明机制的算术问题。尚未形成五个合格合同，未分配单篇
C 编号、建论文包、生成 PDF 或宣称任何目标 A2/A3 进展。

| 候选 | 当前处理 | 冻结前的决定性问题 |
|---|---|---|
| A：广义 Boole 三相周期权重与共振分类 | 优先保留 | 全参数证明、相对既有 Blaschke 包的完整增量及文献归属 |
| B：谐调稠密 delta-comb 的有限耦合谱渐近 | 优先保留 | 形式比较、一致计数误差、后续文献是否已覆盖 |
| C：双曲稳定性权重的普通迹／Schatten 障碍 | 低优先备选 | 相对 symbolic P25 的剩余增量是否足够独立成篇 |
| D：固定特征非仿射几何周期 zeta | 暂存未闭合问题 | 从局部分歧到全部周期的全局恒等式与有理性判定 |

原授权仍为五篇完整论文后确认，不需要因本次维护另行批准常规续接。
当前欠缺的是完整研究合同及证明，而不是用户授权。不得以经典重述填满名额。
下一步先独立审查 A/B 的核心推导和最近文献，同时寻找其余不重叠合同。

## A. 广义 Boole：物理删轨、三相权重与共振

对象固定为 `T(x)=a*x-b/x`，`a,b>0`；相空间是删去所有未来撞极点点的
实直线，采用原始整数迭代时钟。无穷远点不属于物理周期集合。
`b` 可由实伸缩约去，不是额外子类型。

经典相图为：`a<1` 的 Cauchy 不变概率、`a=1` 的无限 Lebesgue 测度、
`a>1` 的 Cantor survivor 与外部逃逸。这些不作为新贡献。
亚临界 Cayley 表示中的内点乘子记为 `q=2a-1`。

拟闭合的统一合同是所有有限实周期、稳定性权重、整个参数族的解析类型、
全部极点消去共振，以及删去新生实固定轨道后的两侧临界极限。
初步推导为

\[
N_n=\begin{cases}2^n-2,&0<a\le1,\\2^n,&a>1,\end{cases}
\qquad
\tau_n=\sum_{T^n(x)=x,\ x\in\mathbb R}
\frac1{(T^n)'(x)-1}
=\begin{cases}
\dfrac2{1-q^n}-\dfrac1{1-a^n},&a<1,\\
\dfrac{n-1}{2n},&a=1,\\
\dfrac1{a^n-1},&a>1.
\end{cases}
\]

这里所有有限周期点须证明简单且正向排斥。拟证路径：亚临界用 Blaschke
内盘收缩；`a>=1` 用 `Im T(z)=Im z*(a+b/|z|^2)` 排除非实有限周期，
再计入无穷远点的正确代数重数。临界局部坐标 `w=1/x` 给出

\[
g^n(w)=w+nbw^3+\tfrac12n(3n-1)b^2w^5+O(w^7),
\]

对应无穷远 holomorphic index 为 `(3n-1)/(2n)`，不能套简单固定点公式。
由这些权重定义的源生成函数 germ 为

\[
D_a(u)=\exp\left(-\sum_{n\ge1}\frac{\tau_nu^n}{n}\right)
=\begin{cases}
(1-u)\dfrac{\prod_{j\ge1}(1-q^ju)^2}
{\prod_{k\ge1}(1-a^ku)},&a<1,\\[4pt]
\sqrt{1-u}\exp(\operatorname{Li}_2(u)/2),&a=1,\\[4pt]
\prod_{k\ge1}(1-a^{-k}u),&a>1.
\end{cases}
\]

root 与该方向作者分别核过以下候选分类，但尚无完整发布证明：

- `1/2<=a<1` 的首极点 `u=1/a` 不可消去。
- `0<a<1/2` 时 entire 当且仅当 `a=(1-2a)^(2m)`，某整数 `m>=1`；
  每个 `m` 唯一解，首例 `a=1/4`。必要性看首极点，充分性用全部幂匹配。
- 共振时抽象对角 trace-class 实现的谱为 `1` 一重，以及 `q^j` 重数
  `2-1_{2m|j}`。这不证明它是原实直线 Perron 算子的自然实现。
- 临界 `(u-1)D_1'/D_1 -> 1/2` 排除穿过 `u=1` 的亚纯延拓。
- 亚临界 `D_a -> D_1`；超临界需先除去两条新生实固定 primitive 的因子
  `prod_{j>=1}(1-q^(-j)u)^2`，再有相同极限。局部一致域为 `|u|<1`；
  须给出权重的统一支配界，不以有限系数检验替代极限证明。
- 超临界 `I=[-sqrt(b/(a-1)),sqrt(b/(a-1))]`，逆分支导数和恒为 `1/a`，
  故候选精确生存律为 `|T^(-n)I|=a^(-n)|I|`。

经典归属：三相测度／Lyapunov 见
[Umeno–Okubo](https://arxiv.org/abs/1510.08569)，Cauchy 参数闭包见
[Goto–Umeno](https://arxiv.org/html/1707.03607v3)，Cantor 动力学见
[Mendoza–Ruiz](https://revistas.utm.edu.ec/index.php/Basedelaciencia/article/view/4408)，
临界混合见 [Bonanno–Giulietti–Lenci](https://arxiv.org/html/1802.00397v2)。
本轮访问这些主来源；有限检索未发现直接覆盖上述整个合同的文献，
不等于新颖性认证。

仓库最近碰撞是
[C380 的完整射影圈 Blaschke 谱](henon_finite_blaschke_ruelle_spectrum_route_a/THEOREM_PACKAGE.md)，
另有 LSV 诱导 Fredholm 与 quadratic Newton–Cayley 包。
若只剩 Cauchy 密度、经典相图、二符号编码或有限根表，则淘汰本候选。
当前没有内生素数机制或目标零除子桥。

## B. 谐调 delta-comb：有限耦合与奇异 Dirichlet 端点

令 `x_n=pi*H_n`，`H_n=sum_{j=1}^n 1/j`。在半直线上取 Dirichlet 起点、
固定 `0<kappa<infinity` 的闭形式

\[
q_\kappa[f]=\int_0^\infty|f'|^2dx+
\kappa\sum_{n\ge1}|f(x_n)|^2.
\]

这是实际无限稠密接触链，能量为 `E`、正频率为 `k=sqrt(E)`，
不输入 prime table、目标零点或人为 `log p` 边长。
拟闭合有限耦合两项计数律及其热迹、谱 zeta 与奇异极限：

\[
N_\kappa(k^2)=2k\log k+C_\kappa k+O_\kappa(\log k),
\quad C_\kappa=\log(4\pi/\kappa)+\gamma-2,
\]
\[
\operatorname{Tr}e^{-tH_\kappa}
=\frac{\sqrt\pi}{2\sqrt t}\log\frac{\pi}{\kappa t}
+O_\kappa(\log(1/t)).
\]

若计数律被证明，Stieltjes 积分将给出谱 zeta 在 `Re s>0` 的续接，
`s=1/2` 主部为
`(1/2)/(s-1/2)^2+(1+C_kappa/2)/(s-1/2)`，以及
`H_kappa^(-1) in S_p iff p>1/2`。它们不是独立的五篇论文。

证明入口：在 `I_n=(x_(n-1),x_n)` 置 `V_kappa=kappa*n/pi`，先对紧支撑
`H^1` 函数证明

\[
\left|\kappa\sum_n|f(x_n)|^2-\int V_\kappa|f|^2\right|
\le2\kappa\|f\|_2\|f'\|_2,
\quad V_\kappa(x)=\frac{\kappa e^{-\gamma}}\pi e^{x/\pi}+O_\kappa(1).
\]

再闭合形式域为 `H_0^1(0,infinity) intersect L^2(e^(x/pi)dx)`，用 Young
不等式和 `epsilon=1/k` 作 min–max 比较。比较指数势的计数需对动能系数
`a` 在固定正紧区间上一致成立。可借用
[C398 的 Bessel 相位方法](henon_exponential_wall_bessel_determinant_route_a/proof/ANALYTIC_PROOF.md)，
但其冻结文本只写固定参数估计；一致性必须新证明。
root 独立检查过作用量二项常数和热迹换算，尚不构成全论证独立审查。

该模型、有限正耦合的离散性、强 resolvent Dirichlet 极限以及端点
divisor／Voronoi 理论均属于
[Egger né Endres–Steiner 原文](https://arxiv.org/abs/1104.1364)。
原文 §2 末将有限耦合高能渐近留作后续研究；这不能证明截至今日仍未解决。
本轮作者名、题名及 finite coupling／harmonic numbers／Weyl 组合检索
未找到上述有限耦合两项公式，仍须检查作者学位论文和后续引用链。

经典端点 `kappa=infinity` 有
`N_infinity(k^2)=sum_{n<=k} floor(k/n)`、主项 `k log k` 和
`zeta_infinity(s)=zeta(2s)^2`。若有限耦合合同闭合，将得到高能／强耦合
两个极限的主系数分别为 `2` 与 `1`，说明端点算术不自动稳定延续。
点态计数极限需处理阈值 convention。不能以共同的 `T log T` 形状宣称目标
对应，也不能把本候选 `O(log T)` 余项套入 C398 的有界余项排除论证。
仓库近邻为 C398 光滑指数势、C288 单点相互作用和 C133/C138 有限图，
不是同一无限稠密链；A4 至多是源系统自然量子实现。

## C. 普通迹障碍：先判增量，再决定是否保留

拟对象为任意实可逆双曲 `d x d` 矩阵 `M`，`d>0`，原始重复 `M^r`。
问题限于逐条带标记轨道的普通迹修补
`Tr B^r=|det(I-M^r)|`，不是所有轨道汇总后的任意表示。

把 orientation 符号并入外代数特征值乘积后，
`|det(I-M^r)|=sum_j c_j alpha_j^r`；合并相同非零 `alpha_j`，
整数 `c_j` 非全零且总和为零，故存在负系数。
拟用 `prod_j(1-alpha_j*z)^c_j` 的不可消去极点排除 trace-class 普通迹，
以及 `B in S_p`、全部 `r>=p` 的尾迹：regularized determinant 所增的
零点自由指数多项式不消除极点。还拟分类最小有限 graded 维数
`sum_j |c_j|`，处理 Jordan、orientation 与乘法共振。

关键碰撞：
[C22](henon_time_ordered_ruelle_cocycle/T4_T5_DERIVATION.md) 的标量障碍不是
全仓最新边界；[symbolic P25 §3](../symbolic_dynamics/papers/25-holomorphic-lefschetz-code-collapse/DERIVATION_PACKAGE.md)
已经证明 `Tr B^r=1-q^r` 的 trace-class 普通 tensor-fiber 排除。
因此“从标量到迹类”不算新机制。剩余全双曲／Schatten 尾迹／最小超秩
是否足够成篇尚待独立判断；不足则淘汰。外代数／交替 determinant
归属 [Ruelle 1976](https://www.ihes.fr/~ruelle/PUBLICATIONS/%5B45%5D.pdf)。
不得扩展为 graded、广义迹、跨轨道消去或所有非局部实现的 no-go。

## D. 固定特征二次几何 zeta：保留问题，不承诺论文

对象为 `f(x)=x^2+1` 作用于 `A^1(Fbar_7)`，整数迭代时钟，
`N_n` 按不同几何固定点计数，`Z_7(z)=exp(sum N_n*z^n/n)`。
真正足够大的合同是判定其有理性并给出全迭代证明；自然边界不得预先承诺。

[Bridy 2012，Question 2](https://www.impan.pl/shop/en/publication/transaction/download/product/83489)
和 [Byszewski–Cornelissen–Houben 2019 §1.4](https://arxiv.org/html/1904.04942v1)
明确讨论该非仿射缺口。本次定向检索未找到解答，不称其“目前已认证公开未解”。
C393 的同多项式是 `Q(t)` 上泛逆像树；C384 是 additive map，均不能直接
提供这里的全局答案。

初筛精确数据 `N_1,...,N_9=(2,2,8,14,27,56,128,254,512)`；概形长度为
`2^n`。在 `F_7[x]` 中 `f^2-x=(x-3)^3*(x-5)`。
更有不可约 `Q=x^5+x^4-2*x^2-2*x-2`，满足 `Q^2 | f^5-x`，
`gcd(Q,Q')=gcd(Q,f-x)=1`、`(f^5)'=1 mod Q`：出现新五周期共振，
不能只修正两个固定点闭合全部 zeta。

最低成本续接是用 `Q` 商环计算局部 `f^5` jet，再截断复合到 `f^35`，
不构造次数 `2^35` 的全局多项式。局部最小分歧工具已有
[Lindahl–Rivera-Letelier](https://arxiv.org/abs/1311.4478) 的经典所有权。
真正未完成的是全部真周期的乘子阶／分歧塔控制、收敛汇总和全局消去。
只证明一条局部塔不完成有理性合同；当前保持暂存，不分 C 编号。

## 已淘汰的当前版本

| 子类型／合同 | 淘汰依据 |
|---|---|
| McMillan 全参数椭圆图谱 | C115 虽仅局部，但 [2024 原文](https://arxiv.org/html/2405.05652v2) 已覆盖 action–angle／相图；又与 C390 椭圆旋转机制重合 |
| 代数群 Frobenius／Steinberg 周期公式 | [BCH 原文](https://arxiv.org/html/2209.00085v2) 已覆盖全类；换群或增秩不构成合同增量 |
| 正特征自动机命中时间当周期 zeta | [Derksen 的经典例子](https://sites.lsa.umich.edu/hderksen/wp-content/uploads/sites/614/2018/05/A.I.a.24.pdf) 已有所有权，且 torus 映射无周期点，命中生成函数不是其周期 zeta |
| p-adic Laplacian shell 热迹／谱 zeta | 本仓 conductor-shell 包已完成相邻完整合同；[经典原文](https://arxiv.org/abs/1511.02146) 进一步覆盖主要公式 |
| Sierpinski 无限谱 zeta 延伸 | C184 有限 decimation 谱系，加上 [Teplyaev](https://arxiv.org/abs/math/0508315) 与 [Derfel–Grabner–Vogl](https://arxiv.org/abs/1202.4126) 的经典全局结果，尚未识别独立增量 |
| 预量子 cat map 全共振带 | [Faure](https://www-fourier.univ-grenoble-alpes.fr/~faure/articles/prequantum_reson_paper_07.pdf) 已有二维结果，[2026 高维原文](https://www.aimsciences.org/article/doi/10.3934/dcds.2026016?viewType=HTML) 继续覆盖一般维数 |

这些判定只淘汰表中的现有合同，不证明整个子类型没有别的问题可做。

## 初筛证据的实际级别

三名工作代理仅做只读检索与内存算例；未创建科研包或写入历史证据。
本记录转录其工具运行后提交的结果，不是附有脚本、环境与哈希的复现证书：

- A：五个有理参数、`n=1..4`，有理迭代、平方自由／Sturm 与商环 residue，
  作者报告 40 项计数／权重断言通过；只审有限公式，不证明全参数命题。
- B：`kappa=0.5,1,2`、`k=10,20,40` 的 Prüfer 浮点传播，每例两个截断。
  作者报告九例截断计数一致，两项公式最大绝对差约为 `0.44`；
  非认证浮点结果，不是尾部完备性或渐近证明。
- D：有限域平方自由计数与五周期共振检验为作者报告的精确有限结果，
  不推出全局 zeta 的解析类型。

正式采用时须保存并独立核验相关证据；未执行论文发布、外部模型审稿或
完整 Route-A 评估。本轮使用 ARS 的来源／论证边界及新仓库技能的先筛选规则。
本会话工具目录未提供 `idea-creator` 指定的旧 GPT-5.4 外部审稿接口；
本轮未执行该调用，已向用户说明采用当前团队内部独立筛选。
不冒称旧工具运行，也不为纯理论候选安排无关 GPU 试验。

交接文本另经算术方向代理只读复核：状态区分、D 段事实及未做事项无阻断问题。
该检查不包含 A/B/C 的完整证明复核、网页复查或论文发布验收。
协调者检查本记录与当前状态中的 14 个本地 Markdown 链接，全部可解析。

保持 `NO_BAD_EULER_OR_ROOT_NUMBER`。源计数、源行列式、算术端点或自然源算子，
均不自行建立目标 Euler 因子、root number、automorphy 或 Hilbert–Pólya 对应。
