# 非作者独立审查：JR qPI 全阶实际临界四次与准确有限坏值

日期：2026-09-08。审查范围：有界数学证明检查；不作新意、价值、容量、Route 或产物评分。

## 结论

整体判定：`PASS`，以本轮主控已接受且哈希未变的 J/F/G 数学合同为输入。
目标稿的强等式

$$
R_{r,t,s}(C)=\delta(C,t^r)
$$

成立，包括实际临界概形的非约化长度；准确有限坏值判据及 henselian 同基底模型桥也成立。
量词保持为：任意特征的代数闭域、每个非零固定 $t$、每个精确有限阶 $s$，以及每个有限原基底点 $c_0$。
没有发现需要修订的硬错误、遗漏分支或新增数学假设；不因未发现错误而制造修订。

这是新建 Codex 独立实例对指定作者稿的非作者审查，不是作者自查、人工审查或跨模型审查。
本实例没有参与目标稿或 J/F/G 的写作，没有读取其他非作者报告或审查票。
按 `research-review` 技能的有界独立、深入审查要求执行；该技能已全文读取。
本轮未配置可调用的 GPT-5.4 Codex MCP，因此没有声称使用该模型，也没有 MCP `threadId`。
未另行生成作者证明稿；没有触发论文写作、Route 评价或实验工作流。

## 输入身份与审查边界

唯一被审作者稿：
[PAPER30_QPI_EXACT_BAD_VALUES_BRIDGE_ENTRY_V1_20260908.md](PAPER30_QPI_EXACT_BAD_VALUES_BRIDGE_ENTRY_V1_20260908.md)。

- 实际全文读取：第 1–488 行，包括全部七个证明步骤、边界检查和验证记录。
- 行数：`488`。
- SHA256：`1e7ade432e62b1e116270d2588d0d798accbf482fcc6edd46dca12b76be42bb1`。
- 始终区分实际函数 $f=I_r$、原基底坐标 $c$、特征多项式形式变量 $C$，以及 $T=t^r$、$\varepsilon=(-1)^{r+1}$。

下表哈希均由本实例重新核对吻合。这里只检查契约匹配，未重新审理已接受的证明。

| 输入 | SHA256 | 本轮消费的合同 |
|---|---|---|
| [J](PAPER30_QPI_LAX_JACOBIAN_BRIDGE_ENTRY_V1_20260908.md) | `a6aa5e30ea0795b05790b058dfd4debc6431de1918090b9a6add88351a1eb63f` | 原 $K=k(c)$ 上 $X$ 是所列 $E$ 的 torsor；$\operatorname{Jac}(X)\simeq E$；原谱方程及零点 $(0,0)$；全特征、全部 $t\ne0$ |
| [F](PAPER30_QPI_ACTUAL_SINGULAR_FIBRE_ENTRY_V1_20260908.md) | `3b7a495b723d9ba45003fe767431c4420053c0b3de6656a2335c3aad01307003` | 全部有限纤维几何整约化、算术亏格一；坏纤维唯一奇点、有理正规化；原 $Z(df)$ 长度四及 $R$ 的定义和坏值判据 |
| [G](PAPER30_QPI_PRIMITIVE_GENUS_ONE_BRIDGE_V1_20260908.md) | `0d7a3e2d37eb7218feddfe5c85bf244a0be358bfcc880279d5f14afd5cb77ace` | 原模型为八次光滑点吹起；$f$ proper、flat；原几何泛纤维光滑几何整、射影亏格一；有限模型为 $U=S\setminus D$ |

本地实际补充读取：J 第 1–56 行，F 第 1–56 行，G 第 7–33、95–100 行；
另在这三个作者文件内作过标题、契约和相关数学术语的定向定位检索。
这不构成对它们的全文重审或独立接受签字。
工作流文件与 `research-review/SKILL.md` 已全文读取。
未读取任何其他 `NON_AUTHOR`、`REVIEW`、`DISPOSITION` 文件、轨道稿、查新稿，
也未读取 README/BATCH 中的投票信息。

若主控还需要登记 J/F/G 的正式接受记录，那是主控的既有职责，不是本报告新增的数学条件。
在本次已传达的接受合同下，不能把本结论另降为“等待输入独审”的 `CONDITIONAL`。

## 逐项判定

下列行号均对应上述冻结作者稿。

| ID | 被审主张及位置 | 判定 | 核心理由 |
|---|---|---|---|
| B1 | Step 1，第 138 行起：原谱商到长 Weierstrass 方程 | PASS | 双向函数域代换成立，原点极阶为 $2,3$；不改 $c$，不除以 $2,3$ |
| B2 | Step 2，第 168 行起：$\Delta_W=T^3\delta(c,T)$ | PASS | $b_i$ 和整系数判别式逐项正确 |
| B3 | Step 2：每个有限原 DVR 及其 henselization 上整方程最小 | PASS | $T$ 为单位，$0\le\nu(\Delta)\le4<12$；可容许变换差值为整数 $12\nu(a)$ |
| B4 | Step 3，第 217 行起：全部射影三次纤维整约化、$p_a=1$ | PASS | 唯一无穷远点相对光滑，排除不同分量和重分量；CM 排除嵌入分量 |
| B5 | Step 3：$W$ 总曲面正则、proper、flat | PASS | 相对奇点处 $uv\ne0$，于是 $F_c\ne0$；射影性和平坦性均有依据 |
| B6 | Steps 3–4：原 DVR 及 henselization 后总模型正则 | PASS | 原 DVR 为局部化；henselization 为无分歧 ind-étale，特殊局部完成环不变，泛纤维光滑 |
| B7 | Step 4，第 253 行起：每个有限点可选 henselian 局部截面 | PASS | 几何整约化纤维在完美域上有光滑 $k$-点；flat 加纤维光滑，继而 étale 提升 |
| B8 | Step 4：截面平凡化原 torsor | PASS | 只对 $L=\operatorname{Frac}(\mathcal R)$ 使用所得 $L$-点，不擅自给 $k(c)$ 全局截面 |
| B9 | Steps 3–4：双方无竖直第一类例外曲线 | PASS | 唯一重数一整特殊纤维为主 Cartier 除子，法丛平凡、自交为零 |
| B10 | Step 4，式 (12)：同基底模型同构 | PASS | 同一光滑射影几何整亏格一泛曲线，$H^0=L$；双方为正则 proper 极小模型，唯一性定理适用 |
| B11 | Step 5，第 293 行起：Fitting 理想等于实际 $df$ 零理想 | PASS | 实际光滑曲面与 $W$ 的两种微分表示给出相同内禀 $\operatorname{Fitt}_1\Omega$ 定义 |
| B12 | Step 5：基变换保留 Artin 块及原 $c$ 算子 | PASS | 相对微分及 Fitting 理想任意基变换相容；henselization 的全部有限阶商保持不变 |
| B13 | Step 6，第 329 行起：单位局部化及 $k[z]/(q)$ 概形身份 | PASS | 开集包含整个临界概形；正反代换合法，商环中 $z,u,v$ 都为单位，无遗漏分支 |
| B14 | Step 6，式 (17)–(19)：四维矩阵与特征多项式 | PASS | 原 $c$ 的四列乘法和三个余子式均正确；整系数恒等式不需要 squarefree 假设 |
| B15 | Step 7，第 410 行起：全阶实际 $R=\delta$ | PASS | 逐有限支撑 Artin 块的 $k[c]$-同构，给出完整特征多项式等式，不是仅零集比较 |
| B16 | Step 7 及边界检查：准确坏值、亏格与好约化 | PASS | F 的实际坏值判据、同基底特殊纤维身份及极小模型的好约化判据闭合；覆盖特征 $2,3$ 与碰撞 |

新增主张中：`CONDITIONAL = 0`，`FAIL = 0`。这不是重新给 J/F/G 投票。

## 关键数学审查记录

### 1. Weierstrass 身份与最小整方程

谱方程在 $(Z,\lambda)=(0,0)$ 对 $\lambda$ 的导数为 $-T\ne0$。
因此 $Z$ 是该点局部参数，而
$\lambda(T+cZ+Z^2-\lambda)=\varepsilon Z^3$ 给出 $\operatorname{ord}\lambda=3$。
作者所列 $u,v$ 极阶及原点对应正确，且变换没有涉及基底坐标替换。

逐项重算得到 $b_2=c^2-4T$、$b_4=-\varepsilon Tc$、
$b_6=\varepsilon^2T^2$、$b_8=-\varepsilon^2T^3$；式 (7) 使用 $\varepsilon^2=1$ 后准确成立。
最小性论证比较的是同一带原点泛椭圆曲线的整长 Weierstrass 方程。
规范离散赋值以整数为值，因此即使剩余特征为 $2$ 或 $3$，正差值也不可能同时为
$12$ 的整数倍且不超过 $4$。
这是本方程的充分最小性判据，不是所有最小方程的必要估计。
长方程及变换的一般框架见 [Conrad §2](https://math.stanford.edu/~conrad/papers/minimalmodel.pdf)。

### 2. 所有有限纤维、总正则性与最小正则性

齐次三次在 $w=0$ 的限制是 $-u^3$，故唯一无穷远支撑点为 $[0:1:0]$；
在那里对 $w$ 的导数为 $1$。
任一正次数平面曲线分量都与无穷远直线相交，且 $w=0$ 本身不是分量。
所以若有两个分量，它们必同时经过该光滑点；若某分量重复，其在该点也不能光滑。
两种情况均矛盾。平面超曲面满足 CM，故没有嵌入关联点；
唯一分量在光滑点处重数一，加上无嵌入分量，给出整个纤维约化，而非仅支集不可约。
这一论证可直接在几何纤维上执行。

仿射相对奇点若 $u=0$，由 $F=0$ 只能有 $v=0$ 或 $v=\varepsilon T$，
两点的 $F_v$ 都非零；若 $v=0$ 且 $u\ne0$，只能有 $u=T$，而 $F_u=-T^2$。
因此相对奇点必有 $uv\ne0$，从而绝对偏导 $F_c=uv$ 为单位。
其余点相对光滑；无穷远已处理，故 $W$ 是光滑 $k$-曲面。
这里没有把“每个纤维奇点均孤立”误当作总曲面正则。

在有限 DVR 上，全部特殊纤维恰是一个重数一整分量 $C_0$，
并有 $C_0=\operatorname{div}(c-c_0)$、$\mathcal O(C_0)|_{C_0}\simeq\mathcal O_{C_0}$。
所以它不可能有第一类例外曲线所需的负一次法丛。
这是作者自交零论证的等价内禀表述，不是额外假设。
实际模型由 F 具有同一性质。最小模型定义只在正则 proper 模型中排除此类曲线，
作者没有把最小 Weierstrass 方程与最小正则模型混为一谈。
参见 [Stacks §54.16 的定义](https://stacks.math.columbia.edu/tag/0C2I)
及 [Definition 55.8.4](https://stacks.math.columbia.edu/tag/0C2R)。

### 3. Henselian 截面、正则性保持和模型桥

$\mathcal R_0$ 是 $k[c]$ 在原有限点的 DVR，$\mathcal R=\mathcal R_0^h$ 仍为 DVR，
剩余域为原 $k$，$c-c_0$ 仍是 uniformizer。
原 DVR 上模型局部环是原光滑曲面局部环的局部化，故正则。
再作 henselization 基变换后，泛纤维由 G 保持光滑。
在特殊闭点，若原局部环为 $A$、极大理想为 $\mathfrak m$，则
$(c-c_0)^N\subset\mathfrak m^N$；$\mathcal R_0$ 与 $\mathcal R$ 的 $N$ 阶商相同，
使基变换局部环的 $\mathfrak m^N$ 商与原者相同。
故完成局部环相同，正则性保持；特殊纤维其他点由局部化得到。
这落实了作者第 262 行的简写，并没有把“底环正则”单独当成“任意基变换总空间正则”。
所需 henselization 性质见 [Stacks §15.46](https://stacks.math.columbia.edu/tag/07QL)。

F 的几何整约化纤维在完美域 $k$ 上有非空光滑开集；其闭点是 $k$-有理点。
G 的 flat、finite presentation 配合该纤维光滑，说明结构态射在所选点附近光滑。
局部 étale 坐标拉回零截面后，henselian 性确实给出 $\mathcal R$-截面，
而不是仅给形式截面或某个有分歧扩张后的截面。
这是 [Stacks Lemma 15.9.14](https://stacks.math.columbia.edu/tag/07M7)
的提升机制配合 henselian 分裂性质的正确应用。

该截面的泛点是 $X_L(L)$ 中的一点，结合已接受的 $E_L$-torsor 结构，
才能得到 $X_L\simeq E_L$。
随后双方模型均正则、proper、flat、finite type；泛曲线光滑、射影、几何整、亏格一，
特别是 $H^0=L$、亏格严格为正；双方已排除第一类例外曲线。
因此 [Stacks Lemmas 55.10.1–2](https://stacks.math.columbia.edu/tag/0C9Y)
的全部实质假设齐备，选定的泛同构唯一延伸为 $\mathcal R$-模型同构。
模型同构具有 $\mathcal R$-线性，所以保持原 $c$。
未声称截面或实际模型同构下降到 $\mathcal R_0$；作者 Claim 也未要求这种下降。

### 4. 实际临界概形与全部非约化 Artin 块

在实际光滑曲面上，$\Omega^1_{U/k}$ 局部自由秩二，
$\mathcal O\xrightarrow{df}\Omega^1_{U/k}\to\Omega^1_{U/\mathbb A^1}\to0$
给出二生成元表示；一阶 Fitting 理想恰由 $df$ 的两个坐标生成。
因此这里的 $Z_{\mathrm{act}}$ 确实是 F 中的原临界零概形。
在 $W$ 的仿射超曲面表示中，同一 Fitting 理想为 $(F_u,F_v)$，
无穷远相对光滑点附近为单位理想。
相对微分的标准基变换身份与
[Stacks Lemma 15.8.4(3)](https://stacks.math.columbia.edu/tag/07ZA)
给出式 (13) 的概形同构，而非只给临界点的双射。

设一个实际临界块为 $B$，支撑在 $c_0$，则某个 $N$ 使 $(c-c_0)^N B=0$。
对 $\mathcal R_0/(c-c_0)^N\simeq\mathcal R/(c-c_0)^N$ 使用张量积，得到
$B\otimes_{k[c]}\mathcal R\simeq B$，并保留自然 $k[c]$-结构。
所以局部模型同构识别整个有限维 $k$-代数及原乘法算子 $m_c$。
有限多个基底支撑块的特征多项式相乘即为全局 $R$。
这一步足以确定每个指数，完全不需要用首一四次的次数去猜测重数。

### 5. 临界代数的概形级消元与四维乘法

$Z_W$ 的闭点全部位于 $uv\ne0$；其闭补集若非空，因有限型于 $k$ 必有闭点。
故整个概形已经包含在这个开集中，局部化不丢失幂零结构。
在该开集中消去 $c$ 后，$F=0$ 等价于 $v^2=u^2(T-u)$，
而 $uF_u=0$ 在前式模下等价于 $\varepsilon Tv=u^3$。
由于 $u$ 为单位，$z=v/u$ 给出

$$
u=T-z^2,\qquad v=z(T-z^2),\qquad
q(z)=(T-z^2)^2-\varepsilon Tz=0.
$$

反方向，在 $k[z]/(q)$ 中，$q(0)=T^2\ne0$ 使 $z$ 为单位；
$u^2=\varepsilon Tz$ 使 $u$ 为单位，继而 $v=zu$ 为单位。
以 $c=(\varepsilon T-2v)/u$ 定义反向映射，三个原方程都恒为零。
因此这是双向概形同构，而非只通过零点坐标找出的对应。

原函数满足 $c=T/z-3z=\varepsilon-z-z^3/T$。
由单首 $q$ 得到自由 $k$-基 $1,z,z^2,z^3$；四个乘法列分别为

$$
\begin{aligned}
c&=\varepsilon-z-T^{-1}z^3,\\
cz&=T-3z^2,\\
cz^2&=Tz-3z^3,\\
cz^3&=3T^2-3\varepsilon Tz-5Tz^2.
\end{aligned}
$$

所以作者矩阵 (18) 的每一项正确。式 (19) 第一行展开的三个余子式
$C^3-12TC+27\varepsilon T$、$C^2-3\varepsilon C-20T$、$12+C^2/T$
也全部正确；最终行列式准确等于所列 $\delta(C,T)$。
该矩阵恒等式甚至可在形式 $\varepsilon$ 下直接验证；不用约化商环或对角化乘法算子。

### 6. 小特征、碰撞和最终坏值身份

特征二时 $\varepsilon=1$，$q=z^4+Tz+T^2$、$\delta=C^4+C^3+T$；
特征三时 $\delta=C^4-\varepsilon C^3+TC^2+T^2$。
所有主论证的除法只涉及 $T,u,v,z$ 等已经证明为单位的元素，没有除以 $2$ 或 $3$。
任意固定非零 $T=t^r$ 直接代入即成立，不需要一般参数稠密性或 $t$ 族的平坦性。

为检查碰撞而额外做了一个精确压力测试：在特征零、$\varepsilon=1$、$T=-27/256$ 时，

$$
q=\frac{(16z+3)^2(256z^2-96z+81)}{65536},\qquad
\delta=\frac{(8C-9)^2(64C^2+80C+153)}{4096}.
$$

两者均非 squarefree，且 $z=-3/16$ 处的长度二局部代数仍由上述概形同构保留。
这个例子只是独立核对，主证明不依赖该特化，也不据此限制其他碰撞。

由逐块乘法身份得到强等式后，F 已接受的实际临界支撑判据立即给出准确有限坏值。
根处正规化亏格零、非根处光滑亏格一的结论正好使用 F 的几何输入。
好约化一项则因 $W$ 已是最小正则 proper 模型，使用
[Stacks Lemma 55.14.7](https://stacks.math.columbia.edu/tag/0CDI) 得到。
对 $\mathcal R_0$ 的 $E$ 好约化判据也是独立由 $W_{\mathcal R_0}$ 得到，
不需要把 henselian 实际模型同构下降。
无穷远重纤维、全局 torsor 障碍和动力映射作用不在本结论中。

## 实际一手来源读取范围

本实例公开浏览了下列来源；没有复用作者声称的阅读记录来冒充自身阅读。

| 来源 | 实际阅读内容 |
|---|---|
| [Stacks §55.8](https://stacks.math.columbia.edu/tag/0C2R) | 本章任意 DVR 与 model 定义；Definition 55.8.4；Lemmas 55.8.3、55.8.5、Proposition 55.8.6 的陈述及证明 |
| [Stacks §54.16](https://stacks.math.columbia.edu/tag/0C2I) | 第一类例外曲线的三项定义；并读所返回的 Lemmas 54.16.1–3 及 54.16.4 开头；本审查只消费定义 |
| [Stacks §55.10](https://stacks.math.columbia.edu/tag/0C9Y) | Lemmas 55.10.1–2 的完整陈述和证明；另打开 [0C6B](https://stacks.math.columbia.edu/tag/0C6B) 核对 55.10.1 |
| [Stacks 0CDI](https://stacks.math.columbia.edu/tag/0CDI) | Lemma 55.14.7 完整陈述及证明 |
| [Stacks §15.46](https://stacks.math.columbia.edu/tag/07QL) | 有限阶商、Noetherian 性、正则性、DVR 保持的陈述与证明，尤其 15.46.1、3、7、10–11 |
| [Stacks 07M7](https://stacks.math.columbia.edu/tag/07M7) | Lemma 15.9.14 完整陈述和证明；先在 §15.9 页读取，再打开独立 lemma 页核对 |
| [Stacks 07ZA](https://stacks.math.columbia.edu/tag/07ZA) | Lemma 15.8.4 完整陈述和证明，重点为 (3) 的任意基变换 |
| [Conrad, Minimal Models for Elliptic Curves](https://math.stanford.edu/~conrad/papers/minimalmodel.pdf) | §2 全节，含长方程定义、Theorem 2.8、Corollaries 2.9–2.10、判别式与十二次张量变换讨论；返回文本也读到 §3.6，不以未读的后文定理代替核心 Stacks 引用 |

不声称全文读取 Conrad 全文或 Liu–Lu 论文；本轮没有使用后者。
上述一般最小模型与 Fitting 理论均为标准输入，本报告不给予任何原创性判断。

## 验证、修正要求与交付边界

独立诊断使用内存中的 SymPy 精确运算，没有新写计算脚本或改动作者文件。
已运行并得到零残差的项目为：谱方程变换、$\Delta-T^3\delta$（模 $\varepsilon^2-1$）、
四列乘法矩阵、$\det(CI-N_T)-\delta$、逆概形映射代入 $F,F_u,F_v$ 后模 $q$ 的余式。
另核算了特征 $2,3$ 的公式约化与上述真实碰撞分解。
这些运行只是代数抄写核对，不代替前述证明检查。

硬缺口：无。强制修订：无。新增数学假设：无。新增验收门：无。
关于闭点完成环、主纤维法丛的展开是审查理由，不是要求作者补写才可通过的门槛。
没有建议为本强等式另造 $t$ 族临界有限平坦模块，没有要求全局截面或原 DVR 上实际模型同构。
不授权轨道结论、论文立项、PDF 验收或外部发布。

本轮唯一新写文件为本报告；作者目标和三份接受输入保持不变。
报告保存后全文自查，确认逐项判定、引用、量词及边界一致；最终行数和 SHA256 在交付消息中给出。
