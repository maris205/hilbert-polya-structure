# Paper31：素域切触充要性与原固定概形接口的数学接受 V1

日期：2026-09-12 UTC。主控：`/root`。
状态：`BOUNDED_MATHEMATICS_ACCEPTED / NO_FORMAL_CANDIDATE_AT_CURRENT_SCOPE`。
`route_applicability: NOT_APPLICABLE`。本地数学接受、研究价值与论文交付分开计量。

## 1. 本轮真正新增的接受

本轮接受以下三项实际增量，不重审或重复计功[前轮原 Manin 必要筛选][OLD]。

| 新输入 | 接受的准确输出 | 独立证据 |
|---|---|---|
| [素域作者证明][PF]，325行 | 全部 $p>3$、$T\in\mathbf F_p^\times$、有限好 $h_*\in\mathbf F_p$，同一 $N_p=0$ 当且仅当存在 prime-to-$p$ 倍点切触 | [素域及有限证书独查][PR]，374行；一般证明逐步PASS，必要修正为空 |
| [锁定F5作者排错][F5]，457行 | 全20组参数、17个好纤维；三个且仅三个好切触点，准确点阶为6、8、7，交数全为2 | [PR] 本人完整独立精确核算，不由一般证明替代表格／jet核验 |
| [原固定概形作者接口][FIX]，348行 | 原自治指定全基共轭、好纤维equalizer、全部有限半稳定原模型的准确固定理想结构式 | [固定概形独查][FR]，297行；三结构命题及全局式PASS，必要修正为空 |

主控已本人 FULL 读取三份作者稿与两份终态独查，确认实际输入哈希一致；接受范围如下。
这是两条分工互不校准的有界数学审查，不是两份完整候选四门票或跨模型认证。
Papers27–30 仍已接受，整批仍 **4/5**；P31未建立项目／锁／稿件／PDF。

## 2. 素域判据的准确量词

保持原带标记曲线和回返点

$$
W_h:\ v^2+huv-Tv=u^3-Tu^2,\qquad O=[0:1:0],\qquad P=(0,T).
$$

令 $p>3$、$T\in\mathbf F_p^\times$，
$\delta=h^4-h^3-8Th^2+36Th+16T^2-27T$。
对每个 $h_*\in\mathbf F_p$ 且 $\delta(h_*)\ne0$，令
$d=\operatorname{ord}P(h_*)$，$i_n=(nP.O)_{h_*}$，不相交时取零。
交数沿原基 $z=h-h_*$，不作分歧重标。
同一已接受多项式 $N_p=(8h-9)^p\mu(P)$ 现在具有准确意义

$$
\boxed{N_p(h_*)=0
\ \Longleftrightarrow\ p\nmid d\ \text{且}\ i_d>1
\ \Longleftrightarrow\ \exists n\ge1,\ p\nmid n:\ i_n>1.}
$$

对 $p\nmid n$，相交当且仅当 $d\mid n$；若相交，$i_n=i_d$。
这里没有把此前任意代数闭常数域的必要条件改窄：旧必要方向保持，新增充分方向只在明确的素域参数上接受。

核心新证明在 $q=8h-9\ne0$ 的好点给准确一阶式
$\mu(Q)(h_*)=(1-A_*)\gamma/\ell_0$，其中
$\lambda=\ell(z)dz$、$w(Q)=\gamma z+O(z^2)$。
$A_*\ne1$ 时由 $\#E(\mathbf F_p)\equiv1-A_*\pmod p$ 得 $p\nmid d$，一阶式可逆。
$A_*=1$ 时，代数可分提升使 $\mu$ 下降为 $\chi(X,Y)=YM(X)$；
极零次数和 Hasse 界给核大小一或二，原 $P$ 不在该核。
$p=5,\#E=10$ 与 $q=0$ 的好点均单独覆盖，特殊时间没有整体删去。

[PR] 另将短模型展开写为 $X=w^{-2}+O(w^2)$，明确核对全部系数的基方向导数均不产生额外常数项。
同态只通过包含有限多个提升的有限可分函数域使用；没有假设任意超越形式点已属于源函数域。
因此接受的是完整书面充分性证明，不是F5样本外推。

仍未接受：一般 $\mathbf F_{p^r}$／全部代数根的充分性、一般准确 $i_d$、
$\operatorname{ord}N_p=i_d-1$、$p\mid n$ 的算术分类、坏纤维或无穷远的交数。
单点 $\mu(P)(h_*)=0$ 也不等于泛有理函数 $\mu(P)$ 恒零。

## 3. 原完整固定概形的结构恒等式

本项取代数闭 $k$、$\operatorname{char}k=p>3$、固定 $T\in k^\times$、全部 $n\ge1$，
原自治完整 $\mathcal U=S\setminus D$ 及四末端线均保留。
实际有理坐标

$$
\phi(x,y)=\left(\frac Ty,\frac{Tx(y-1)}{y^2}\right),\qquad
\phi F_T=\tau_{P}\phi
$$

由指定泛同构及最小正则模型唯一性延拓为全有限基 $\mathcal U\simeq W$。
[FR] 另直接核定四末端像依次为 $-2P,-P,O,P$。
这只是在自治 $r=1$ 上的完整相对识别，不把一般有限域点集拼合升级成全部 $r$ 的曲面共轭。
旧henselian模型式本来已经是相对同构，不再把这一旧接口记为完全缺失。

令 $C^{\rm ss}=\mathbb A^1_h$（若 $T\ne-27/256$），
或 $C^{\rm ss}=\mathbb A^1_h\setminus\{9/8\}$（若 $T=-27/256$）。
令 $D_n=(nP)^{-1}(O)$ 为准确截面交除子，$f:\mathcal U\to C$。
在好纤维上有 $\operatorname{Fix}(F_T^n)=\mathcal U\times_C D_n$；在整个半稳定有限模型上有

$$
\boxed{\mathcal I_{\operatorname{Fix}(F_T^n)}
=(\mathcal I_{D_n}\mathcal O_{\mathcal U})\,
\operatorname{Fitt}_1(\Omega^1_{\mathcal U/C})
\quad\text{on }f^{-1}(C^{\rm ss}).}
$$

尤其在有限节点的完成环 $k[[\xi,\eta]]$、原基参数 $\tau=\xi\eta$ 中，

$$
\widehat{\mathcal I}_{\operatorname{Fix}(F_T^n)}
=\tau^{i_n(h_0)}(\xi,\eta).
$$

无交点时 $i_n=0$，固定概形是约化孤立节点；$i_n\ge1$ 时，厚纤维之外有长度一的节点嵌入部分。
广义椭圆作用供应相对形式群参数，UFD论证给完整理想，不只给切空间线性化或Tate对角化猜测。
式子对 $p\mid n$ 仍成立，但未算其标量阶 $i_n$；尖点不由节点式处理。
全基共轭本身包含尖点，与节点式的半稳定限制没有冲突。

将此好纤维equalizer与§2合取，可立即解释原动力：对素域好能级，存在 prime-to-$p$ 迭代使
该完整纤维出现大于一的基向固定厚度，当且仅当 $N_p(h_*)=0$。
这是两个已核定接口的直接逻辑推论，不另记新定理或独立价值。
它不求全部 $D_n$，也不声称已完成旧特征零全阶异常谱。

## 4. F5完整有限证书的接受范围

预先固定 $p=5,T=1,2,3,4,h_*=0,1,2,3,4$，没有因未见反例而加质数、扩域或挑点。
全部20行分为3坏、4个点阶被5整除、10个prime-to-5横截、3个二阶切触。
三个且仅三个好切触参数为

| $(T,h_*,d)$ | 原 $w=-u/v$ 的首项，$z=h-h_*$ | 准确交数 |
|---|---|---:|
| $(1,4,6)$ | $3z^2+O(z^3)$ | 2 |
| $(3,2,8)$ | $z^2+O(z^3)$ | 2 |
| $(3,4,7)$ | $3z^2+O(z^3)$ | 2 |

[PR] 本人独立重算四个 $N_5$、全部20行、17个完整点集和有序循环、
32个函数域乘法坐标恒等式、全部13行的division-polynomial单位及局部jet，以及三条完整有理式。
其短模型算法与原作者广义式算法分别执行；所有最终证书均为精确有限域算术。
分母规范的非零常数差异已解释，不误作函数不一致；计算调用层排错没有计入成功证据。
只读helper不代替审查者本人验证，也不另计票。

## 5. 来源扣除、价值边界及后续

[来源边界][S]已由主控FULL核对，包含本轮18条实际查询与各一手源的实际读取层级。
Voloch的 $YM(X)$ 下降同态、UV的局部Manin机制、经典Hasse界与形式群均须扣除；
Conrad的广义椭圆作用、最小模型及节点局部代数也不作为原族新理论。
Duistermaat周期纤维目录线索不替代未读正文；Miranda–Persson全局挠截面假设不转给非挠截面特化。
主控在作者稿冻结之后补读Voloch1990的所需文本，不回写作者稿当时的读取快照或添加未经审查的新依赖。

这组接受目前仍是原族的短数学接口，不自行触发完整候选、改名重投旧包、source/publication locks或试写测页。
[独立增量批评][CR]终态101行已由主控FULL核准：承认素域充分性和完整原理想的真实增量，但扣除直接先例后，三件合并仍不足以支持独立22–30页的非标准中心，故本轮只冻结数学输入。
该席本人FULL读取七件共1591行，并按报告所列范围核对指定一手来源，未读取两份数学独查或与其校准；没有正式分数、页数硬预测或第三数学票。
主控接受这一当前证据判断，不把数学PASS自动充候选PASS，也不作永久禁研或要求全部未决方向同时关闭。
准确 $D_n$、一般接触厚度及其他非标准算术输出仍未供应；它们是研究缺口，不是本次已接受定理内部的缺证。
旧特征零I03、扩域统计、尖点或一般q问题不因此自动解决或晋级；也不以本轮结果宣布家族耗尽。
Paper31仍遵守22–30页及完整准入，五篇目标没有改成若干短报告；继续族内实质研究，不需再次确认已授权本地动作。

## 6. 终态合取身份与效力

以下均由主控本人FULL读取；哈希绑定实际终态，而非代理阅读层级的继承。

| 本轮文件 | 行数 | SHA-256 |
|---|---:|---|
| [PF] | 325 | `de9cdb5ee8fef26b50365e6794e148f7206c4c167738143fc28e77159b0debef` |
| [F5] | 457 | `30ba24affbcea9ac65b892aa1e31311fe0ba2140c776249f06e316b9b759fcd9` |
| [PR] | 374 | `22e5f5038100c98f42bed300d0f71794c0da0bcea18229585f0cbb9eb11d212d` |
| [FIX] | 348 | `401db0359ad2e05456ff3ec2aa7f93e2ad7fb7136e2f815f131b02a66e762ba7` |
| [FR] | 297 | `6f6a358d537be253809cf55be9b7fa64069a006f5cb205ab6a2fc1c88f119a77` |
| [S] | 85 | `5004d141f21699d01499ef428c585a9eda364fba4ecf4d50fe4c17160108d33c` |
| [CR] | 101 | `cb94ad908083fda9418cb681985c079d5cdc09636944569c7bdf8e0b9d3a8943` |

旧[Manin作者446行][M]及[接受148行][OLD]本人FULL读取并准确消费；
原模型旧[C]只定向读至245行，含Step1–3；[F]350–405、[R]295–345用于核对新应用条件，不冒称主控重读其全文。
本轮主控亦FULL读取121行组合基线与107行碰撞图，只消费已有结果及旧指纹的明确边界。
外文主控／作者／各非作者的实际读取分别按[S]与各报告记录，不以整响应哈希升级实读范围。

proof-writer固定全称量词、依赖及例外；research-lit识别直接旧机制；research-review对实际新证明作fresh非作者核查。
实际使用可用Codex xhigh代理，不虚构技能所列但未配置的GPT-5.4 MCP或跨模型结论。
作者辅助属于作者侧；两数学独查没有彼此或作者校准，结果增量批评另行计量，不充第三数学票。
仅本地新增研究报告及当前索引更新；冻结原稿、旧锁、失败与已接受论文不改。
无投稿、上传、托管、push、发信、付费云资源、GPU实验或论文编译；整批统一审查仍待第五篇实际完成。

[PF]: PAPER31_QPI_MANIN_PRIMEFIELD_EXACTNESS_V1_20260912.md
[F5]: PAPER31_QPI_MANIN_F5_EXACT_SCREEN_V1_20260912.md
[PR]: PAPER31_QPI_MANIN_PRIMEFIELD_INDEPENDENT_V1_20260912.md
[FIX]: PAPER31_QPI_MANIN_FIXED_SCHEME_INTERFACE_PROBE_V1_20260912.md
[FR]: PAPER31_QPI_MANIN_FIXED_SCHEME_INDEPENDENT_V1_20260912.md
[S]: PAPER31_QPI_MANIN_PRIMEFIELD_SOURCE_BOUNDARY_V1_20260912.md
[CR]: PAPER31_QPI_MANIN_INTERFACE_INCREMENT_CRITIQUE_V1_20260912.md
[M]: PAPER31_QPI_NEW_INPUT_MANIN_INTERFACE_V1_20260912.md
[OLD]: PAPER31_QPI_NEW_INPUT_MANIN_DISPOSITION_V1_20260912.md
[C]: PAPER30_QPI_CLOSED_FIBRE_RETURN_CONJUGACY_ENTRY_V1_20260908.md
[F]: PAPER30_QPI_ACTUAL_SINGULAR_FIBRE_ENTRY_V1_20260908.md
[R]: PAPER30_QPI_RETURN_TRANSLATION_ENTRY_V1_20260908.md
