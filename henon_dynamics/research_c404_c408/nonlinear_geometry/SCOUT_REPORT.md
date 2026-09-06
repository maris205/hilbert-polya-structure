# 非线性几何线：两项有界侦察，零项准入

日期：2026-09-06。基线：`5b2a654c4f0b82b0e2d5158146b377ee6bf4e804`。
状态：`SCOUT_COMPLETE / 2 SCREENED / 0 RETAINED / 0 NEW PAPERS`。
本记录不是论文、全族不可能性定理或形式评价；没有分配 C 编号。

本线仅考察两个本质类型：正熵有理曲面的孤立回返，以及有限域正熵曲面的
Frobenius–自同构联合计数。没有把“最多三个”解释成必须凑足三个。
没有展开 C402 坐标权重、C108 修补、Boole、Möbius、Lattès、环面或 Lüroth 参数变体。
依照本地批次工作流及 research-lit、novelty-check、idea-creator、proof-writer 的
来源和证明边界，实际采取的是原始正文核验与一个低成本精确反例检查。
ARS 仅用于有界来源检索/核验；未调用外部模型、API 审稿、GPU 或上传手稿。

## 结论表

| 类型 | 所需新增量 | 本轮实际发现 | 决定 |
|---|---|---|---|
| Hietarinta–Viallet / Bedford–Kim 正熵有理曲面 | 全周期的仿射普通点数，或独立闭合的局部指数修正定理 | 已有几何熵/Picard 所有者；三周期点数 9 与循环理想长度 18 不同；紧化存在周期固定曲线 | `REJECT_NO_CLOSED_NEW_LEMMA` |
| 有限域曲面的熵方向与 Frobenius 耦合 | 非经典的全族联合谱约束或回返计数关系 | 极化轨道张成空间上 Frobenius 是纯 Tate 标量；余空间上自同构有限阶已由 Esnault–Srinivas 给出 | `REJECT_CLASSICAL_COROLLARY` |

第一项的拒绝是“本轮没有完整新契约”，不是证明所有可能的回返公式不存在。
第二项只拒绝下面具体的分离/相对 zeta 提案，不能推出其他曲面算术动力学均无新内容。

## 1. 正熵有理曲面：不能把局部交数当作普通回返点数

### 1.1 候选契约及实际所有者

对象为复数域上的整个非零参数族

\[
H_a(x,y)=(y,-x+y+a/y^2),\qquad a\in\mathbb C^*.
\]

离散时钟是迭代次数 \(m\ge1\)。仿射 observable 原拟取
\(N_m(a)\)：所有中间迭代均有定义、坐标均非零的不同复周期点数。
周期坐标满足 \(x_{i+1}=-x_{i-1}+x_i+a/x_i^2\)，下标按 \(m\) 循环；
因此普通点数、这个有限循环代数的长度、以及紧化曲面的 Lefschetz 数，是三个
必须分开的对象。若改取 \(1/\det(I-DH_a^m)\) 的稳定性权重，则只能先在
非退化点定义；本族在 \(m=3\) 已不满足这一条件，不能不声明延拓便直接求和。

Takenawa 已构造此映射的有理曲面自同构提升并给出 Picard 作用；本轮实际核读了
该预印本第 2 节的吹起、定理 2.1 和式 (6)，没有把重算这个矩阵或熵算作新引理。
[Takenawa 原始预印本正文](https://arxiv.org/pdf/nlin/0011037)。

还检查了 Bedford–Kim 的更大连续族

\[
f(x,y)=\left(y,-x+cy+
\sum_{\substack{2\le\ell\le k-2\\\ell\ {m even}}}a_\ell y^{-\ell}
+y^{-k}\right),
\]

其中偶数 \(k\ge2\)、任意复系数 \(a_\ell\)，以及原文 §1 定义的
\(c\in C_N\)。该参数条件不能丢掉：\(c-1/w\) 在无穷远的有限阶还须满足
原文式 (1.3) 的乘积条件。其定理 1 已给出提升及熵特征多项式。
更关键的是，v2 的定理 8.1 给出一组边界曲线，其所有点均被 \(f^{2N}\) 固定，
且导数为恒等。因此紧化上的“所有固定点数”甚至不是有限的离散 orbit census。
[Bedford–Kim v2，定理 1、§1、§8](https://arxiv.org/pdf/0804.2078)。

本拟议增量只能是：明确分类完整参数族的周期曲线/点局部指数，处理极点和
仿射开集的边界贡献，并在需要普通点数时控制每个孤立点的重数。
这部分在本轮没有完成。只引用 Picard 特征多项式不能代替它。

### 1.2 决定性低成本检查：三周期 9 个点、代数长度 18

任取 \(t^3=a\)，缩放 \(S_t(x,y)=(tx,ty)\) 给出
\(S_t^{-1}H_aS_t=H_1\)，所以 \(a\ne0\) 并不是避开下述退化的自由参数。
固定点为 \((t,t)\), \(t^3=a\)，且每个固定点处

\[
DH_a=\begin{pmatrix}0&1\\-1&-1\end{pmatrix},\qquad
(DH_a)^3=I.
\]

它们对一次迭代是简单固定点，但对三次迭代退化。对 \(a=1\)，在 \((1,1)\)
取局部坐标 \((u,v)\)，逐次展开直接得到

\[
H_1^3(1+u,1+v)-(1+u,1+v)
=\bigl(3u^2+6uv,-6uv-3v^2\bigr)+O((u,v)^3).
\]

两个二次首项分别为 \(3u(u+2v)\)、\(-3v(2u+v)\)，没有公共射影零点。
故其局部交数为 \(2\cdot2=4\)：例如在局部环使用这两个首项构成的齐次
正则序列，其商的 Hilbert 级数是 \((1+T)^2\)，长度为 4。
三次单位根缩放与 \(H_1\) 交换，所以三个原固定点均如此。

这不仅是导数退化警报；整个三周期系统也可以精确分类。令

\[
F_i=x_i^3-(x_{i-1}+x_{i+1})x_i^2+1,\qquad i\in\mathbb Z/3.
\]

任何解的每个坐标都非零，因为 \(x_i=0\) 会给出 \(F_i=1\)。因此这里没有
因清分母引入的伪解，也没有未经声明的饱和。

若两个坐标等于 \(t\)，第三个是 \(s\)，则方程给出
\(st^2=1\) 及 \((t^3-1)^2=0\)，故在点集上三者相等、\(t^3=1\)。
若三坐标互异，由

\[
F_i-F_j=(x_i-x_j)[x_i^2+x_j^2-x_k(x_i+x_j)]
\]

可先推出 \(x_0+x_1+x_2=0\)，再推出两两乘积之和为零，继而
\(x_i^3=-1/2\)。因此三个坐标正好是 \(X^3+1/2\) 三根的六种排列。
这些排列直接代回均为解。因此三周期不同点数为 \(3+6=9\)，其中有两个
真正的三周期轨道。

独立的有理数 Gröbner/商代数检查给出总长度 18，并用
\(L=x_0+2x_1+4x_2\) 的乘法算子得到

\[
\det(zI-m_L)=(z^3-343)^4\,
\frac{4z^6+40z^3+343}{4}.
\]

其无重因子部分次数为 9，和上述点集分类相符。前三个局部长度已经合计 12，
余下六个点各至少长度 1，而总长度是 18，故六个新点全部简单。
这里只得到一次和三次迭代的确证；没有据此猜一个全周期生成函数。

可复跑证据：

- [exact_probe.py](exact_probe.py)：精确有理数运算、局部 jet、循环理想、商代数特征多项式以及不同点分类代回检查。
- [EXACT_PROBE_OUTPUT.json](EXACT_PROBE_OUTPUT.json)：实际成功运行的 stdout；Python 3.12.3、SymPy 1.14.0、exit 0。
- 命令：`python henon_dynamics/research_c404_c408/nonlinear_geometry/exact_probe.py`。

### 1.3 为什么经典固定点公式还没有交付所需新增量

Iwasaki–Uehara 的预印本 §7 显式区分带重数的 `#` 和无重数的 `Card`。
在代数稳定且无 type-I 周期曲线等条件下，定理 7.2 将 Lefschetz 数写成
孤立点局部指数之和与周期曲线修正之和；它没有把每个孤立点的指数设成 1。
其定理 2.6 的保面积判据还有极点阶条件，不能仅凭保存一个亚纯二形式便
删除这个条件；Remark 6.2 正给出反例警告。
[Iwasaki–Uehara v1，定理 2.6、Remark 6.2、§7](https://arxiv.org/pdf/0710.0706)。

因此尚缺的全证明路线是：完整曲线分类 → 验证适用的局部型及极点条件 →
算出全部局部贡献并去除边界 → 若仍要普通点数，再证明/分类所有额外退化。
目前没有独立完成的统一新引理。这是拒绝此候选的具体原因，不是声称该路线
原则上永远不可完成。一个低周期反例本身也不够升格为“独立障碍论文”。

## 2. 有限域正熵曲面：拟议 Frobenius 分离已是经典推论

### 2.1 完整假设与 observable

取任意有限域 \(\mathbb F_q\) 上光滑、射影、几何连通曲面 \(X\)，
\(g\in\operatorname{Aut}_{\mathbb F_q}(X)\)，极化类 \(h\) 亦定义于
\(\mathbb F_q\)，固定 \(\ell\nmid q\)，并要求 \(b_1(X)=0\)。
选题关注正熵情形，但下述推论不需要额外使用正熵。
这里 \(\Phi\) 是实际的 \(q\) 次 Frobenius 态射，几何点坐标取 \(q\) 次幂；
用这个约定避免把 Galois 生成元及其逆的命名混淆。

时钟分别为 \(n\ge1\) 和 \(r\ge1\)，observable 是

\[
N_{n,r}=\#\operatorname{Fix}(g^n\Phi^r)(\overline{\mathbb F}_q).
\]

它确实是普通点数：\(d\Phi^r=0\)，故固定点方程的导数为恒等，固定点概形
处处零维且约化；射影性使其有限。这是源系统内在算术，但不是目标 Euler
因子或目标谱归属的证明。

### 2.2 已闭合但不新的推导

在未 Tate 扭转的 \(H^2=H^2_{\mathrm{et}}(\bar X,\mathbb Q_\ell)\) 中定义

\[
W=\operatorname{span}\{(g^*)^j h:j\in\mathbb Z\},\qquad V=W^\perp.
\]

1. 每个轨道极化类均定义于 \(\mathbb F_q\)，故 \(\Phi^*|_W=qI\)。
   \(W\) 在 Néron–Severi 的有理空间中定义，包含 ample 类；由 Hodge index，
   它的交形式非退化，因而 \(H^2=W\oplus V\)。
2. 配对的 \(g^*\)-不变性表明 \(V\) 正是包含于 \(h^\perp\) 的最大
   \(g^*\)-不变子空间：对所有 \(j\) 正交等价于对子空间所有 \(g\)-迭代
   与 \(h\) 配对均为零。Esnault–Srinivas 定理 1.1 恰好断言此空间上的
   \(g^*\) 有限阶。原文使用 \(H^2(1)\)；Tate 扭转不改变 \(g^*\) 的阶。
   [Esnault–Srinivas v2，定理 1.1](https://arxiv.org/pdf/1105.2426)。
3. 令 \(A=g^*|_W\)，并选 \(M\) 使 \((g^*)^M|_V=I\)。
   射影 Lefschetz 固定点公式与 \(b_1=b_3=0\) 给出

\[
N_{n,r}=1+q^{2r}+q^r\operatorname{Tr}(A^n)
+\operatorname{Tr}((g^*)^n(\Phi^*)^r|_V).
\]

当 \(M\mid n\) 时，和 \(\#X(\mathbb F_{q^r})\) 相减便得到

\[
N_{n,r}-\#X(\mathbb F_{q^r})
=q^r\bigl(\operatorname{Tr}(A^n)-\dim W\bigr).
\]

这里括号是整数：可在 \(W\) 的有理 Néron–Severi 子空间与整格的交中取
一个 \(g^*\)-稳定满格。对固定的 \(n\in M\mathbb Z_{>0}\)，令
\(\delta_n=\operatorname{Tr}(A^n)-\dim W\)，于是形式幂级数恒等式

\[
\frac{\exp(\sum_{r\ge1}N_{n,r}t^r/r)}{Z(X,t)}
=(1-qt)^{-\delta_n}
\]

就是上述差式逐项求和。没有新的 Salem 中心化子或复相位锁定引理需要证明。
这些等式是本轮对已有定理的短推导，不作为新论文的作者贡献申报。

### 2.3 最强审稿意见和替代边界

最直接的审稿意见是：关键有限阶结论完全属于 Esnault–Srinivas，剩余部分是
定义于基域的代数循环、正交分解和经典 Lefschetz 公式。这个短推论不够构成
独立论文。无需再用一个特定 K3 数值例子装饰它。

以下边界不能删去：若 \(g,h\) 仅在扩域定义，要明确换基域/时钟；若
\(b_1\ne0\)，必须保留奇数上同调项；若不取 \(M\mid n\)，不能删去余空间
中 \(g^n\) 的有限阶相位。这也不是“Frobenius 在整个 \(H^2\) 上纯 Tate”的
断言，更不是所有联合回返 observable 都因分离而平凡。

## 3. 原始来源和实际阅读范围

下面是与决策直接相关的来源。均于 2026-09-06 检索/核读；
“正文”仅指表中所列部分，不等于整篇逐页精读。未把搜索摘要当作完整定理。

| 来源 | 元数据核对与实际访问 | 真正核读的主文位置 | 此处作用 |
|---|---|---|---|
| T. Takenawa, *A geometric approach to singularity confinement and algebraic entropy* | [arXiv nlin/0011037](https://arxiv.org/abs/nlin/0011037)，采用 v2 正文；arXiv 页面用于元数据 | §1–2，14 次吹起、Thm. 2.1、式 (6) 的 Picard 作用 | 几何提升/Picard 所有者；不声称该文已有本报告计算的普通三周期点数 |
| E. Bedford, K. Kim, *Continuous Families of Rational Surface Automorphisms with Positive Entropy* | [arXiv 0804.2078](https://arxiv.org/abs/0804.2078)，采用 2009-02-27 v2；出版 DOI 的直连访问在本轮报错，未伪装成已读出版版 | 定理 1、§1 参数定义和部分局部提升、§8 的计算至 Thm. 8.1 | 更大非平凡参数族；固定曲线和 tangent-to-identity 障碍 |
| K. Iwasaki, T. Uehara, 预印本 *Area-Preserving Surface Dynamics and S. Saito's Fixed Point Formula*；出版名 *Periodic points for area-preserving birational maps of surfaces* | [arXiv 0710.0706 v1](https://arxiv.org/pdf/0710.0706)；[Keio 作者机构元数据](https://keio.elsevierpure.com/en/publications/periodic-points-for-area-preserving-birational-maps-of-surfaces/) 核对 Math. Z. 266(2), 289–318 (2010)，DOI 10.1007/s00209-009-0570-3 | §1–2 的公式和假设，§3 局部定义，Remark 6.2，§7 式 (33)–(37) 和 Thm. 7.2 | 带重数与无重数区别；曲线修正及适用条件 |
| H. Esnault, V. Srinivas, *Algebraic versus topological entropy for surfaces over finite fields* | [arXiv 1105.2426 v2](https://arxiv.org/pdf/1105.2426)；[作者出版目录](https://page.mi.fu-berlin.de/esnault/helene_publ.html) 与 [作者机构条目](https://researchconnect.buffalo.edu/en/publications/algebraic-versus-topological-entropy-for-surfaces-over-finite-fie/) 核对 Osaka J. Math. 50(3), 827–846 (2013) | §1 主定理/推论、§2 预备结果及 §3 部分证明；本结论只需 Thm. 1.1，不声称从头复证其深层分类步骤 | 直接覆盖候选所需有限阶引理 |

检索还覆盖了 Hietarinta–Viallet periodic points/zeta/fixed point、
birational surface Saito local index、finite-field surface automorphism
Frobenius Salem/Esnault–Srinivas，以及 2025/2026 时间词的变体。
局部历史碰撞检查针对实际 README/IDEA/BATCH 文本，而不是据一个全文搜索命中
就声称读遍旧项目。本轮没有发现能填补第 1 项缺口的已验证全周期新引理；
这句话仅说明本次检索的证据状态，不是全球文献不存在性断言。

## 4. 交付与停止边界

本线交付一份拒绝报告和一个精确反例探针，保留契约为零。
没有新论文、LaTeX/PDF、正式评价、CURRENT/全局索引修改或 Git 写入/提交。
两种类型都没有被宣告完成 A1/A2/A3；遵守 `NO_BAD_EULER_OR_ROOT_NUMBER`。
若协调者重开第一项，新增工作必须是上文缺失的全周期局部几何定理，而不能
把这份低周期检查或经典固定点公式重命名后准入。
