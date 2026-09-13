# P33 内部理论：固定截止值的几何分离与两个控制端原始见证

记录日期：2026-09-08 UTC。本轮只推进固定 `Lambda=21/10` 的数学证明链，不运行 BP／CP、普查或旧 fixture，不修改论文、合同、输入、正式回执或状态。本文中的曲面长度始终是曲率负一、单位速率的基底测地长度；不将它改成磁周期，原 `b=1/2` 等模型锁保持不变。

本轮的实质增量是：把锁定矩阵与实际核读的公开几何构造对应后，给出 Bolza 端的严格排除，以及控制端两个不同的逆元配对原始 owner 的显式短字见证。控制端原始性来自整数同调，不依赖继承的“已知精确 systole”标签或有限球普查结果。结论属于来源支持的内部数学推导，并经主线对核心推导作只读复核；该复核不属于独立科学认证，也不自动满足现有生产证书合同。

## 1. 固定对象与输入边界

当前依据是[第四轮稿][current-draft]的 B0014、B0020、B0025、B0027、B0070–B0073，以及 [BP 合同][bp-contract]和 [CP 合同][cp-contract]。一个 owner 是

\[
\{[g]_\Gamma,[g^{-1}]_\Gamma\},\qquad
g\text{ 本原},\quad \ell(g)\le\Lambda,\quad \Lambda=21/10.
\]

反向有向共轭类在外部配对后只计一个 owner。恒等元不计；幂是重复而非新 owner。

本轮只读核对了合同指向的三个对象，其实际 SHA-256 与合同所列值一致：

- [Bolza 精确对象][bolza-input]：`e3e6c486c66116dc6fe9fdd054c2fce9d4b1a58318f56d1656f6db168c807eca`。
- [控制精确矩阵][control-input]：`a900749b6905a5f324c2e2670363ec1bc9480481f3f5aa1240ed0ebbee55e6ca`。
- [继承有限球对象][finite-input]：`c1bf68a8a1485665680dba01d0012fb691c7ca1a795e36334639e34bbbdbcb1f`。

这些散列只绑定读取的字节。第三项中的状态、状态数、systole 和覆盖标签不作为本轮证明前提；没有重跑其遍历、符号判定或历史生产程序。

## 2. 实际核读的外部几何输入

### 2.1 Bolza 对象的对应

Ebbens、Iordanov、Teillaud、Vegter 的公开作者稿 *Delaunay triangulations of generalized Bolza surfaces*，arXiv:2103.05960v1，§2.4、作者页 5 的 Eq. (5)，给出正则 `4g` 边形的对边配对矩阵；其后的 Poincaré 定理段落给出 Fuchsian 群及基本域，作者页 6 识别 `g=2` 为 Bolza 曲面。作者页 2 的 Theorem 2 给出该模型的 systole。这里采用这些外部陈述，不声称本轮重新证明了 Poincaré 多边形定理或完整 systole 定理。[实际核读的作者稿 PDF][bolza-source]

将 `g=2` 代入 Eq. (5)，前四个生成元恰为锁定对象的

\[
A_j=\begin{pmatrix}
\cot(\pi/8)&e^{ij\pi/4}\sqrt{\cot^2(\pi/8)-1}\\
e^{-ij\pi/4}\sqrt{\cot^2(\pi/8)-1}&\cot(\pi/8)
\end{pmatrix},\qquad j=0,1,2,3.
\]

源 Eq. (6) 在 `g=2`、使用后四个边配对为前四个的逆元后，也与锁定 relator 相同。因此应用的是同一精确模型，而非仅因文件名含 Bolza 就转用定理。Theorem 2 的 `g=2` 专门化为

\[
\operatorname{sys}(S_B)=2\operatorname{arcosh}(1+\sqrt2).
\tag{1}
\]

### 2.2 控制曲面的几何与标记，不由矩阵关系倒推忠实性

Nazarenko 的公开作者稿 *Two-parametric hyperbolic octagons and reduced Teichmueller space in genus two*，arXiv:1301.5446v1，§2、作者页 3 直接说明所述 Fuchsian 群与曲面基本群同构；作者页 4 的 Eq. (10) 给出参数域，Eq. (11) 给出另一组顶点半径，随后的粘合段落及 Eq. (12) 陈述闭亏格二曲面、四个生成元和单一关系；作者页 5 的 Eqs. (16)–(18) 给出生成元及旋转。[实际核读的作者稿 PDF][control-source]

本轮采用的外部输入是该完整几何构造及标记对应，不是“矩阵满足一个 relator，所以表示忠实”这一错误推理。具体地，取

\[
u=a=e^{-1/10},\quad \alpha=\pi/4,\quad
\widetilde\alpha=0,\quad x=u^2=e^{-1/5}.
\]

源参数域在此要求 `1/sqrt(2)<u<1`，下一节将以有理数界验证。Eqs. (16)–(18) 随即逐项化为稿件和锁定矩阵的公式；源中的旋转 `R_(pi/2)` 就是这里的 `diag(e^(i pi/4),e^(-i pi/4))`。

因此，在采用上述外部几何构造的意义下，锁定矩阵所生成的 `PSU(1,1)` 群与带标记群

\[
G=\langle g_0,g_1,g_2,g_3\mid
g_0g_1^{-1}g_2g_3^{-1}g_0^{-1}g_1g_2^{-1}g_3=1\rangle
\tag{2}
\]

对应。这一对应是后文把抽象词同调转成实际曲面原始性的必要输入。若未来对该源构造或字节对应提出实质反证，几何转用必须随之重审，不能保留结论却删除前提。本轮没有重新证明控制的非算术性，也没有补填 S02 的一手访问缺口。

## 3. 固定截止值的有理数比较

Taylor 公式的四阶正余项给

\[
x=e^{-1/5}
>1-\frac15+\frac1{50}-\frac1{750}
=\frac{307}{375}>\frac{13}{16}>\frac12,
\qquad x<1.
\tag{3}
\]

其中 `307/375-13/16=37/6000>0`。因 `u>0` 且 `u^2=x`，(3) 同时验证了 S01 的 `1/sqrt(2)<u<1`；另一顶点半径 `b=1/(sqrt(2)u)` 也在 `(0,1)`。这里的几何参数 `b` 不替换项目原有的磁场参数。

令 `q=Lambda/2=21/20`。正项级数给

\[
\cosh q>
1+\frac{q^2}{2}+\frac{q^4}{24}
=\frac85+\frac{7281}{3840000}>\frac85.
\tag{4}
\]

另一方面，`(2n)!>=2^n` 且从 `n=2` 起为严格不等式，所以

\[
\cosh q<\sum_{n=0}^{\infty}(q^2/2)^n
=\frac{800}{359}<\frac94<1+\sqrt2.
\tag{5}
\]

最后两步分别等价于 `3200<3231` 和 `25/16<2`。没有使用浮点长度或舍入的 `2.1`。

由 (1)、(5) 及 `arcosh` 的严格单调性，

\[
\boxed{\Lambda<\operatorname{sys}(S_B).}
\tag{6}
\]

因此该精确 Bolza 模型的 `ell<=Lambda` 非平凡闭测地线集合为空，原始 inverse-paired owner 集当然也为空。这里使用全局 systole 定理，不是把生成元都长于截止值误当成所有群元素都长于截止值。

## 4. 两个控制端短字：同迹，但不是同一个 owner

为免与其他项目的层数记号混淆，只把控制矩阵中的归一化标量重记为

\[
\Delta=(1-x)(2x-1)>0,\qquad \nu=-\Delta^{-1/2},\qquad
A=x+i(1-x).
\]

这只是符号重命名，不改变输入。固定公式为

\[
g_0=\nu\begin{pmatrix}u&A\\\bar A&u\end{pmatrix},\qquad
g_1=\nu\begin{pmatrix}u&i\bar A\\-iA&u\end{pmatrix},
\]

\[
g_3=\nu\begin{pmatrix}u&-\bar A\\-A&u\end{pmatrix},\qquad
g_2^{-1}=\nu\begin{pmatrix}u&-iA\\i\bar A&u\end{pmatrix}.
\]

这些逆元及旋转式可直接检查；例如
`u^2-|A|^2=x-[x^2+(1-x)^2]=Delta`，故每个原始矩阵的行列式为一。

取两个固定词

\[
w_1=g_0g_3,\qquad w_2=g_1g_2^{-1}.
\]

直接乘法给

\[
w_1=\frac1\Delta
\begin{pmatrix}
x-A^2&2iu(1-x)\\
-2iu(1-x)&x-\bar A^2
\end{pmatrix},\qquad
w_2=\frac1\Delta
\begin{pmatrix}
x-\bar A^2&2u(1-x)\\
2u(1-x)&x-A^2
\end{pmatrix}.
\tag{7}
\]

因为 `Re(A^2)=2x-1`，二者的迹精确相同：

\[
\boxed{\operatorname{tr}(w_1)=\operatorname{tr}(w_2)
=\frac{2(1-x)}\Delta=\frac2{2x-1}.}
\tag{8}
\]

由 (3)，

\[
1<\frac1{2x-1}<\frac85<\cosh(21/20).
\]

所以二者都是双曲元。使用固定曲率负一的标准迹—平移长度公式（也见 Bolza 来源作者页 4 的 Eq. (3)），得到

\[
\boxed{
0<\ell(w_1)=\ell(w_2)
=2\operatorname{arcosh}\!\left(\frac1{2e^{-1/5}-1}\right)
<\frac{21}{10}.}
\tag{9}
\]

这证明的是两个显式词的长度及严格 cutoff admission，并没有证明该共同长度等于控制曲面的 systole。

## 5. 同调给出原始性和 owner 分离

先记录一个无需普查的群论判据。若 `h:G->Z^d` 是同态，而 `h(w)` 是非零本原整数向量，则 `w` 不可能为 `v^m`、`m>=2`：否则 `h(w)=m h(v)`，每个坐标都被 `m` 整除。共轭保持 `h`，取逆元把 `h` 变号。因此：

- `h(w)!=0` 可排除 `w` 与 `w^-1` 共轭；
- 若 `h(w')` 不等于 `h(w)` 或 `-h(w)`，则二者不可能属于同一个外部逆元配对 owner。

判据是一条充分证据路线，不是完整共轭／根算法：相同同调不推出共轭，非本原同调也不推出 proper power。

在源支持的标记群 (2) 中，单一 relator 的每个生成元指数和均为零。因此其交换化为 `Z^4`，四个 `g_j` 对应标准基。由此

\[
h(w_1)=(1,0,0,1),\qquad
h(w_2)=(0,1,-1,0).
\tag{10}
\]

两个向量均本原、非零，且互不等于对方或其负向量。通过 §2.2 的几何／标记对应转用上述判据，两个实际双曲元均为本原，各自不与其逆元在完整表面群内共轭，且它们的两个 owner 不同。因此，若以 `mathcal O_C(Lambda)` 表示固定控制的数学 owner 集，

\[
\boxed{
\mathcal O_B(21/10)=\varnothing,\qquad
\#\mathcal O_C(21/10)\ge2.}
\tag{11}
\]

每个见证 owner 含两个不同的有向共轭类。特别地，(8)、(10) 是同一固定几何中“同迹、同长度并不等于同 owner”的明确例子；这里的区别有整数同调证明，不是仅因两个词写法不同。

## 6. 这条证明链完成什么，不完成什么

数学层面的分离比完整普查所需信息少。Bolza 的全局严格 systole 界可以排除整个短轨道宇宙；控制的一条或两条正面存在性见证不需要先证明控制的精确 systole。对于本节两个词，同调还可直接承担各自的无 proper power、非自互反及彼此 owner 分离义务。

但 (11) 不是一个已经运行且通过独立 checker 的 BP／CP 生产回执：

- BP 合同仍要求另行冻结并 replay 的源／定理／算法版本、绑定摘要及空输出覆盖证书。本轮提供其数学 antecedent 的来源与推导，不填写任何 observed coverage digest，也不运行 empty stream producer。
- CP 的两个见证不覆盖其他 admissible owners。其中心 guard、FIFO 连通分量、所有边分类、规范共轭、输出流与零 unresolved ledger 均未在本轮证明或执行。尤其不能把下界 `>=2` 改写为恰有两个，也不使用历史有限球的 equality-state 数推测 owner 数。
- 一般候选之间同调可能相等；这些情形仍需要真正的完整群共轭判定。本文的充分判据没有提供统一 producer、parser、proof adapter 或独立 validator。

故本轮可以把固定 cutoff 的几何推理从未定位的继承方向推进到明确的来源—公式—同调链，但不把这一内部理论成果记为完整 census、P33-RC-1 的生产实现或正式晋级。该对照仍受 systole 差异影响，不能据此识别算术性、推广到非算术曲面族、给予 Route 分数或解除 Stage 5／6 边界。

## 7. 来源范围、失败记录与实际动作

本轮按 ARS 论证构建方式分开外部几何陈述、项目代数推导、量词和生产限制。实际普通浏览成功读取两个作者稿的 arXiv 摘要页及 PDF 文本，重点为上述节、页和公式；没有声称逐页复证全文，亦未将人类授权当作人类已读确认。

Bolza 作者稿在当前 PDF 文本提取中存在一处需保留的表述不一致：作者页 13、Lemma 9 的局部计算显示 `1+cos(pi/(2g))`，而 Theorem 2 的定义为 `1+2cos(pi/(2g))`。本轮请求该页截图返回 `Internal Error`，未获得图像，故只记录文本提取不一致，不判断是作者错误还是提取问题。本轮不使用那条局部计算；使用的是 Theorem 2 的明示陈述、同一矩阵模型，以及本笔记独立的 cutoff 比较。正式定理版本绑定时应保留此来源限制。

`https://doi.org/10.20382/jocg.v13i1a5` 的一次打开也返回 `Internal Error`；没有把它登记为成功访问出版页，没有重试或换 transport。实际支持来自此前已成功打开的作者稿。不请求或补填原 S02 一手访问缺口，不把 Nazarenko 稿的构造段落扩展成非算术性、数域或完整谱结论。

本地实际动作限于 `rg`／`sed` 的只读定位与读取、上述输入和保护文本的 SHA-256 快照、`node -e` 的只读文本结构检查，以及用 `apply_patch` 新增和修订本文件。一次对本文件的 `git status` 查询因工作目录不在 Git 仓库内失败；没有修改 Git 配置或换目录重试，也不把它作为成功的变更清单检查。写后比对中，稿件、BP／CP 两合同和三个冻结输入共六项散列与写前一致；本笔记的引用定义／使用、本地链接目标、显示数学分隔符、连续公式标签及控制字符检查均通过。这些是字节保全与文本结构检查，不是科学认证。

没有运行数值矩阵、长度、积分、枚举或 scientific experiment；没有重跑旧 fixture、历史 producer 或 artifact writer；没有修改任何既有输入、合同、稿件、源使用账本、冻结 cutoff 或历史失败记录。主线负责批次入口和复核。本文不刷新正式 `FAIL / BLOCK`、Route 状态或 Stage 5／6 停止条件。

[current-draft]: /root/autodl-tmp/flow_systems/papers/33-bolza-control-matched-census/notes/stage4_prime_revision_round4.tex
[bp-contract]: /root/autodl-tmp/flow_systems/papers/33-bolza-control-matched-census/notes/stage4_prime_round5_support/bp_enumeration_contract.json
[cp-contract]: /root/autodl-tmp/flow_systems/papers/33-bolza-control-matched-census/notes/stage4_prime_round5_support/cp_enumeration_contract.json
[bolza-input]: /root/autodl-tmp/flow_systems/papers/28-bolza-magnetic-flow/results/round4_bolza_group_certificate.json
[control-input]: /root/autodl-tmp/flow_systems/papers/28-bolza-magnetic-flow/results/round7_nonarithmetic_control_matrices.json
[finite-input]: /root/autodl-tmp/flow_systems/papers/28-bolza-magnetic-flow/results/round8_control_finite_ball_certificate.json
[bolza-source]: https://arxiv.org/pdf/2103.05960
[control-source]: https://arxiv.org/pdf/1301.5446
