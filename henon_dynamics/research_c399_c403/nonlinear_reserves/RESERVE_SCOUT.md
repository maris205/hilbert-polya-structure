# C399–C403 有界备用筛选：0 个新准入合同

日期：2026-09-05。范围：恰好两个互异的内生算术入口；这是选择报告，
不是论文、冻结合同、完成证明或正式 Route-A 评估。

## 结论

**新增合格合同为 0。** 第一个入口的有意义目标落在已有明确猜想上，
本次没有找到闭合它的证明机制；第二个入口的完整可定义部分已有直接
文献所有权，而例外参数并不自动产生一个已定义、可证明的新合同。
这不是“不存在任何新问题”的断言。有限检索缺少命中不能证明新颖性，
既有论文也不能被夸大成已解决其作者明确留下的猜想。

当前有用的主要工作仍是把已完成的 Boole 与有限耦合 delta-comb 证明
整理成连贯研究稿；本报告不以备用目录、有限表或经典重述填补五篇名额。

本次遵循 `idea-creator` 的来源—碰撞—廉价准入检查，并使用本仓
`henon-route-a-batch` 的实质增量门槛。按委派边界，不调用该旧 skill
示例中的外部 GPT 接口，不扩大到 8–12 个条目，不运行 GPU。内部选择
判断不称外部审稿。只写入本文件；未执行 Git、功能图枚举、论文构建
或正式评估，保持 `NO_BAD_EULER_OR_ROOT_NUMBER`。

## 1. 固定双曲 Markoff 自同构：有实质问题，但没有本轮可闭合合同

### 对象、时钟与全参数成功门槛

对每个素数 $p>3$，取

\[
X_{-2}(\mathbb F_p)=\{(x,y,z):x^2+y^2+z^2=xyz\},\qquad
Y_p=(X_{-2}(\mathbb F_p)\setminus\{0\})/K,
\]

其中 $K$ 是同时改变偶数个坐标符号的四元群。该商和删去的原点均是
对象定义的一部分，不把它混同于整个仿射三维空间或正整数 Markoff 树。
通过 $\operatorname{Out}(F_2)\simeq\mathrm{GL}_2(\mathbb Z)$ 的标准
Fricke character 作用，固定

\[
U=\begin{pmatrix}1&0\\1&1\end{pmatrix},\quad
V=\begin{pmatrix}1&1\\0&1\end{pmatrix},\quad
g=U^2V^2UV=\begin{pmatrix}3&5\\7&12\end{pmatrix}.
\]

每一步是同一个 $g$，不是任意更换 Vieta 生成元的群轨道。
令 $L(g;p)$ 为其在 $Y_p$ 上的最长周期。足够实质、量词明确的成功
门槛是：找到并证明常数 $c>0,p_0$，使**每个素数** $p>p_0$ 都满足

\[
L(g;p)\ge c p^2.
\]

这只是待证明目标，不是本报告的新定理。若研究周期 zeta，必须用
$N_r=\#\operatorname{Fix}(g^r|Y_p)$ 与
$Z_{g,p}(u)=\exp(\sum_{r\ge1}N_ru^r/r)$；固定 $p$ 时它是有限置换
zeta，其有理性本身没有论文增量。

### 重要性、所有权与廉价决定性检查

算术来自同一个整数 character variety 的模素数约化，不是外加目标
素数权重。全素数的二次最长轨道下界会从真正非线性动力学控制占正
比例的周期结构，明显超出一个有限周期表；但它没有自动产生目标
Euler 因子或 logarithmic primitive clock。

最廉价检查是先比较既有定理与猜想，而不是重新枚举几个小素数。
Cerbu–Gunther–Magee–Peilen 的原文 Theorem 1.5 已证明任意固定双曲
$g$、所有整数 $\kappa$ 的最长轨道至少为
$\log p/\log|\lambda_g|+O_g(1)$，且常数不依赖 $\kappa$。同文
Conjecture 1.10 明确提出非 ambiguous 字的二次最长轨道下界，并把
上面的 $g$ 作为数值例子；因此这里连目标猜想也不是新提出的。
[主文献 PDF，Theorem 1.5、Conjecture 1.10](https://arxiv.org/pdf/1610.07077)

仓库已在
`symbolic_dynamics/docs/papers162_166_sequence/scouting/replacement_arithmetic_hybrid/OWNER_SEARCH_LOG.md`
的 `CerbuEtAl2016` 条目记录这篇直接周期所有者；
`symbolic_dynamics/docs/papers157_161_sequence/phase1/combinatorial_gate/REPLACEMENT_SCOUT.md`
§3 已拒绝另一个固定 Markoff–Vieta 字的全周期入口。它们不是本次
所列二次下界的仓库证明，但足以否定“换一个确定性字就是新机制”。
C193 只处理正整数下降树，不能被援引为已解决本题。

### 精确未解决环节与决定

目前没有控制 $g^r$ 在 $r$ 达到 $p$ 的幂规模时的全局固定点分布，
也没有导出一个长度 $\gg p^2$ 轨道的结构性不变量。已有固定点方程
次数估计在对数迭代尺度给出信息；将同一估计多算几个 $r$ 不能跨过
这个障碍。生成元群的连通性／大置换群结论也不直接约束其中一个
固定元素的最长周期。

本次未证明该猜想，也未认证其截至今日仍全球未解；没有运行新的
周期枚举。**`PARKED_KNOWN_CONJECTURE / NO_NEW_PROOF_MECHANISM`**。
如果剩余成果只有现成对数下界、置换行列式或低素数表，就停止，不冻结。

## 2. 超奇异 isogeny 非回溯动力学：直接所有权与闭路约定缺口

### 对象与原拟统一定理

取不同素数 $q,\ell$，$q\equiv1\pmod{12}$，以及
$N\ge1$、$\gcd(N,q\ell)=1$。顶点是
$\overline{\mathbb F}_q$ 上带循环 $N$ 阶子群的超奇异椭圆曲线的
同构类；边是保持该 level structure 的 $\ell$-isogeny，保留重边、
环与对偶边。普通 Ihara 比较还须限制在**对偶边 involution 没有固定
边**的参数子族；单凭 $q\equiv1\pmod{12}$ 不保证这一点。
动力学是可衔接且不立即沿对偶边返回的有向边移位，原始时钟是边数。
primitive 闭路按循环移位取商，不把反向闭路合并。

令 $Z_I(G,u)=\prod_{[P]}(1-u^{|P|})^{-1}$，$W(C/\mathbb F_\ell,u)$
是曲线的 Hasse–Weil zeta。拟证明的全参数恒等式原是

\[
W(X_0(qN)/\mathbb F_\ell,u)\,
W(X_0(N)/\mathbb F_\ell,u)^{-2}\,Z_I(G,u)
=(1-u^2)^{\chi(G)}.
\]

这里模曲线的计数域是 $\mathbb F_\ell$，不能把承载超奇异顶点的
特征 $q$ 与该 Hasse–Weil 局部因子的素数 $\ell$ 混用。

### 廉价检查、所有权与碰撞

这个对象确有内生 isogeny／Hecke 算术，且所拟结果是真正的源闭路
与代数几何局部因子恒等式，原本值得优先检查。然而无需先计算任何
Brandt 矩阵：Lei–Müller 的 Theorem A 已明确发表同样的 zeta 恒等式，
$N=1$ 归于 Sugiyama；其写出的参数甚至未加上面额外的固定边限制。
本报告仅在约定兼容的子族使用其直接所有权，不替原文补作全例外证明。
原文使用 Hecke 模块对应，不是通过谱图相似或拟合得到。
[Lei–Müller v2，Theorem A](https://arxiv.org/html/2307.01001v2)

仓库 `henon_dynamics/nonabelian_voltage_zeta_obstruction/IDEA_REPORT.md`
的 `C15-I` 已把 supersingular isogeny／Hecke nonbacktracking 作为
文献饱和的正控制；C375 的 LPS–Hashimoto 包则占据另一种 quaternionic
有限图的 Bass 机制。两者不应夸大为已证明所有 isogeny 图结论，但
表明只把图换名、再写一次 Bass determinant 不是新的独立问题。

### 为什么例外参数尚不构成新合同

先有一个不依赖枚举的警报：$q=13,\ell=2,N=1$ 时，按经典顶点数
$(q-1)/12$ 只有一个顶点，却有 $\ell+1=3$ 条出边。因此所有边上的
对偶 involution 不可能没有固定边。这说明即使顶点自同构都是
$\{\pm1\}$，也不能把该对象不加说明地视为每个无向环贡献两个
有向边的普通图。固定对偶边／half-loop 的 primitive 规则及 determinant
修正需要单独核对；“原文有公式”不免除这一步。

自然尝试是允许所有 $q$，处理额外曲线自同构。Codogni–Lido 的最新
v5 已对一般 level structure 给出按目标自同构取商的有向图、加权
Hermitian 形式与 Hecke 对应；§1.2.1 还明确警告 $j=0,1728$ 处的
对偶边可能依赖代表元选择。不能把这些都当成未被发现的例外。
[Codogni–Lido v5，§1.2.1、§2.2](https://arxiv.org/html/2308.13913v5)

本轮**没有**固定一个同时处理固定对偶边与额外顶点自同构、代表元
无关的 primitive 闭路
商及其权重，继而证明它与某个明确非回溯算子的迹逐项一致，更没有
证明所得修正的模形式因子公式。改用更细 level 结构或 groupoid 是
重新定义对象的选择，不是可以略过的技术字句；它仍须与既有理论
逐项比较。当前访问的文献不足以证明“所有可能修正均已覆盖”，也
不足以使尚未定义的修正晋升为待写论文。

**`KILL_DIRECT_OWNER`** 对上述干净全参数合同成立；全特征扩张保持
**`NO_FIXED_ORBIT_CONVENTION / NO_NEW_INCREMENT`**。不运行图普查，
不把已知源 automorphic correspondence 宣称为目标 Riemann zeta
或 Hilbert–Pólya 实现。

## 实际检查与停止条件

执行了定向 `rg` 碰撞检索与主来源网页核查；阅读 Markoff 原文相关
定理／猜想、Lei–Müller 完整定理参数，以及 Codogni–Lido 最新 v5
相关定义和例外说明。部分早期网页用于定位；最后判断以上述明确
版本为准。AMS 会议页面仅返回 JavaScript 占位内容，未用它冒充完整
论文证据。本次未下载新 PDF 到工作树，也未声称独立验证各主文献
全部证明。

筛选到此结束：两个互异入口，零个新冻结合同，零个新编号论文，
零项目标 A1/A2 晋级证据。不追加第三个目录或重复已淘汰子类型。
