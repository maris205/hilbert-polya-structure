# D01 独立数学检查：固定奇素高度二的完整局部下降

日期：2026-09-09。这是指定作者终态的非作者、有界数学检查，不是正式新意评分、容量票、Route A/B 评价、立项或论文验收。

## Status

`PROVABLE AS STATED / PASS_FIXED_TORUS_COMPLETE_LOCAL`。

在作者明确限定的 $p=3,m=1,a=2,t=1$、指定 $\mathbb F_9$ 环面点完成邻域中，完整原两系数理想的等式、允许提升不变性、横向长度与允许无分歧状态的精确阶均成立。没有发现阻断性缺口，也不需要再加一个有限 jet 才能完成此限定证明。这里的通过不包含四末端、完整 Hasse 纤维、其他根或全奇素数的推广。

## 身份、接触与执行边界

- 本审查者没有参与 D01 作者稿或脚本的编写。此前负责 I05/I09 的 C/D 查新和 D05 作者证明包，不能为自己的 D05 出具独立数学票。
- 审查前已接触 D01 的选定命题摘要和主控列出的风险点；这不是盲审。按主控要求，作者终态 SHA 到达前只准备原矩阵及已接受出口，未读取 D01 工作稿。收到锁定终态后才全文读取作者稿和新脚本。
- 本检查由当前已配置的可用代理按既定 xhigh 审查职责完成；没有调用指定的 GPT-5.4 审查端点，不宣称指定模型复验或跨模型验证。未再委派代理。
- 沿用并再次全文读取 proof-writer、research-review 技能，前者用于逐命题/假设/依赖的证明检查，后者用于明确非作者身份、证据和剩余风险。本次不开展该技能的通用选刊、评分或新增实验流程。
- 实际仅运行锁定脚本一次；无参数扩大、GPU、浮点拟合、文献检索、项目初始化、PDF 构建或对外写入。只新增本审查文件，不修改作者稿、脚本、已接受论文源或其他冻结记录。

## 输入读取与锁定

下表的全文/部分是本审查者实际读取范围，不把文件存在或哈希匹配算作全文阅读。原输入在准备阶段已读，终态审查只核对哈希与必要新推论，不重开未变数学。

| 输入 | 阅读范围 | SHA-256 |
|---|---|---|
| [D01 作者终态](PAPER31_QPI_ODD_HEIGHT_TWO_DESCENT_DIAGNOSTIC_V1_20260909.md) | FULL，357 行，分两段读取至 EOF | `fd6f9efd18a42fa4b723fbc74a9a24b18df1a45a8d71c07389f26d0a10e77360` |
| [D01 精确脚本](qpi_odd_height_two_descent_diagnostic_v1_20260909.py) | FULL，380 行，分两段读取至 EOF | `e15f6f058409b6d19ffbeb7ce9eb9f925963731b5455041e0e1ab226293d2558` |
| [V4 引言与原矩阵](../../papers/30-qpi-vertical-critical-ideals/paper/v4/sections/01-introduction.tex) | FULL，300 行，D01 准备阶段 | `9b2876f36052d545ccf03a8309c4119f66ea06c3a9bbffa002e6228aa7610c0e` |
| [V4 整数迹与插入](../../papers/30-qpi-vertical-critical-ideals/paper/v4/sections/05-integral-trace.tex) | PARTIAL，本次准备读 1–47、165–205 行 | `925b2bedcc8e942fb92797d9080b983f53010de97bc1676053390f8a5fc70ab0` |
| [V4 首层出口](../../papers/30-qpi-vertical-critical-ideals/paper/v4/sections/06-first-layer.tex) | PARTIAL，本次准备读 348–397 行至 EOF；此前同批另读过部分段落 | `e5ba6462600b04aee4d42f6d3ef85729ee2b3e7f5e6dfead92e37008d36ce392` |
| [V4 奇素首 jet](../../papers/30-qpi-vertical-critical-ideals/paper/v4/sections/07-odd-jets.tex) | PARTIAL，本次准备读 1–80、418–468 行至 EOF | `046f8cf808cc64de570605b316bcb5b0c6970f52492a585f97f97597ae2d74f5` |
| proof-writer 技能 | FULL，223 行，本次再次全文读取 | `6d7b3094711f609814680ded62e19b8dd61801511a7d98b96c033894c939babe` |
| research-review 技能 | FULL，106 行，本次再次全文读取 `/root/autodl-tmp/.codex/skills/research-review/SKILL.md` | `62859ebaa64be9915546b0ba8fb3464110bcfe015307fc33b15c97f03dc392a5` |

## Claim

设 $k=\mathbb F_3[a]/(a^2+a+2)$，$\mathcal O=W(k)[\zeta_9]$，$q=\zeta_9$、$\pi=q-1$，$P=(a,2)$。令 $S$ 为原环面在 $P$ 的完成局部环，并保留原函数

$$
j=y-x+x/y-1/x,\qquad z=j-1,\quad w=y-2,\quad u=j+1=z+2,\quad H=j^2-1=zu.
$$

对原降序九因子迹的整除形式 $\alpha_9=(1/9)dI_{9,q}$，以原连续相对余切模的完整两系数理想记为 $C$。被接受的限定结论是

$$
S\simeq\mathcal O[[z,w]],\quad B=\mathcal O[[z]],\qquad
C=(\pi^2-z^4,\pi z^3)S=QS.
$$

此外，$z'=z+\pi f$ 对每个 $f\in S$ 给出同一理想正规式；$\dim_k B/Q=10$；对作者定义的每个允许无分歧状态，$v_\pi(\alpha_9)=2$、$v_\pi(dI_{9,q})=14$。作者关于导子保持的必要条件也成立，但不是以上完整等式的充分性依据。

## Assumptions 与 Notation

$\mathcal O$ 已完成，且 $v_\pi(3)=6$、$v_\pi(9)=12$。记 $\Omega=S\,dx\oplus S\,dy$ 为连续相对余切模。在 $P$ 有 $j=1$、$j_x=a\ne0$、$u=2\ne0$，因此 $(dj,dy)$ 是 $S$ 上的正则余切框架。允许状态是保持 $\mathcal O$ 的连续局部映射到有限无分歧扩张 $\mathcal O'$，故 $z,w\in\pi\mathcal O'$。不包括任意额外分歧状态。

这些是实质性范围限制：$u$ 和首切向系数的单位性、$3\in(\pi^6)$ 以及状态的无分歧条件分别进入不同步骤，不能删除。所有谱次数的提取使用 $Z$，不与 $z$ 混用。

## Proof Strategy 与 Dependency Map

审查链条是：原四矩阵项逐项转录及整数圆分商运算 → 完整 Laurent 系数证书 → $S$ 内的可逆余切框架和完整两生成元 → 单位关系给出真正的 $\pi^3\in C$ → 保持原 $z$ 的理想等式 → 提升不变性、横向长度及状态阶。

已接受首 jet 原来只保证 $C+(\pi^2)=(\pi^2,z^4,\pi z^3)$ 及状态阶至少为 $2$。新增的二阶证书和完整两生成元关系承担全部精确结论；有限维平台的五次通过不承担完整下降证明。

## Proof：独立逐步检查

### 1. 原矩阵、词序和整除没有改变

将脚本 `original_matrix()` 的四个稀疏字典逐项合并，确为

$$
\begin{aligned}
A_{00}&=1-x(y-1)+(j-1)Z+Z^2, & A_{01}&=-x+Z,\\
A_{10}&=(y-1)\bigl(x(y-1)-1\bigr)+(j+x(y-1)-1)Z,
& A_{11}&=x(y-1)+Z.
\end{aligned}
$$

尤其左下常数项为 $xy^2-2xy+x-y+1$，一次项为 $xy+y-2x+x/y-1/x-1$，均与原输入一致。此人工转录检查不可用“迹与行列式相同”替代；脚本另外验证迹及行列式，是补充交叉检查。

`left_factor_multiply(factor,product,k)` 确实左乘 $A(q^kZ)$，最终词序是 $A(q^8Z)\cdots A(Z)$。中途只删谱次数大于 $9$ 的项，其余因子没有负谱次数，故不丢失目标系数。相位先按 $q^9=1$ 取模合法；随后对 $r=6,7,8$ 用 $q^r=-q^{r-3}-q^{r-6}$，得到整数自由基 $1,q,\ldots,q^5$ 下的唯一系数。

脚本对该完整积分先作状态微分，逐基底断言分子能被 $9$ 整除，再展开 $q=1+\pi$，最后模 $3$。负 Laurent 指数的微分和两个方向的指数移动均正确。没有先在特征 $3$ 微分 $j^9$ 后作非法除法。由于 $3\in(\pi^6)$，所得 $\pi^0,\pi^1,\pi^2$ 系数是原形式模 $\pi^3$ 的准确系数。

### 2. 新增证书是全 Laurent 恒等式

记 $\alpha_9\bmod\pi^3=\sum_{\nu=0}^2\pi^\nu(A_\nu dx+B_\nu dy)$。原稿 (E2)–(Q2) 中

$$
L=(y-1)x^2-y(y-1)x+y=-xyz
$$

及两个完整短商与脚本 `expected` 的表达式逐项一致。脚本从原九词重新产生 $A_2,B_2$，清除各自单项式分母后进行精确多项式除法，同时检查零余式、单项式移位和完整商相等。这不是把同一商先作为输入再输出它，也不是有限 $w$ 展开的整除测试。

一次实际运行验证了

$$
A_2-u j_x=x^{-5}y^{-7}L^3Q_x,\qquad
B_2-u j_y=x^{-4}y^{-8}L^3Q_y,
$$

两商展开项数分别为 $16,12$。由于 $L^3=-x^3y^3z^3$，第一项余项除以 $H^3$ 为 $-x^{-2}y^{-4}u^{-3}Q_x$，第二项为 $-x^{-1}y^{-5}u^{-3}Q_y$；它们均属于所选局部环的剩余环，而不需倒置 $z$ 或 $H$。因此二阶形式 $\alpha_2=A_2dx+B_2dy$ 满足 $\alpha_2=u\,dj+H^3\beta$，其中 $\beta\in\Omega/\pi\Omega$；这是模 $\pi$ 的全局部恒等式。

脚本还直接从同一原迹核对零阶 $H^4dj$ 和一阶两项的 $L^3$ 整除。切向检验使用的是 $j_xB_1-j_yA_1$，不是只看 $A_1$ 或某个法向非零值。其清分母商 $R$ 满足 $R(a,2)=2$。因此

$$
b_1(P)=\left.\frac{j_xB_1-j_yA_1}{j_xH^3}\right|_P
=-a^{-6}=2a^2=2+a\ne0.
$$

这里 $a^2+a=1$、$a^8=1$；独立计算 $j_x(P)=-1+2+(a+1)^2=a$，也核对了此框架和单位判定。

### 3. 从模系数到完整 $S$ 生成元没有遗漏尾项

对上一节的剩余 Laurent 恒等式取整数提升。其差是 $3$ 的倍数，故在 $S$ 中属于 $(\pi^6)$。再用 $j_x$ 的逆将 $(dx,dy)$ 换成 $(dj,dy)$，不会降低 $\pi$ 阶。因此存在 $a_1,a_2,b_1,b_2,r,s\in S$，其中 $b_1$ 是单位，使完整系数为

$$
\begin{aligned}
U&=H^4+\pi H^3a_1+\pi^2(u+H^3a_2)+\pi^3r,\\
V&=\pi H^3b_1+\pi^2H^3b_2+\pi^3s.
\end{aligned}
$$

提升选择的改变可吸收到后阶的 $H^3$ 倍数和尾项中；它不要求对 $\alpha_9$ 的无限尾项再作计算。此处 $C=(U,V)$ 是实际完整理想，而非其有限商的像。

令 $B_1^*=b_1+\pi b_2\in S^\times$。变换 $G=V/B_1^*$、$F=U-(a_1+\pi a_2)G$ 的矩阵行列式为单位，故不改变系数理想，并且精确得到

$$
G=\pi H^3+\pi^3b,\qquad F=H^4+\pi^2u+\pi^3a.
$$

直接相减给出完整等式

$$
\pi F-HG=\pi^3(u+\pi a-Hb).
$$

括号在闭点的值为 $2$，因此在 $S$ 中可逆。由此确有 $\pi^3\in C$。任意尾项 $a,b$ 的切向依赖均已受这条关系控制；这不是对有限长度稳定性的推断。两方向的生成元包含随即给出

$$
C=(\pi^3,H^4+\pi^2u,\pi H^3).
$$

### 4. 最后相等式保持原能级坐标

只除以 $u$ 的单位幂，得到 $C=(\pi^3,z^4u^3+\pi^2,\pi z^3)$。模已在理想中的 $\pi^3$，环的特征为 $3$，故该理想准确等于

$$
(\pi^3,z^7+2z^4+\pi^2,\pi z^3).
$$

在其商中，将第二生成元乘以 $z^3$，用 $\pi^2z^3=0$ 得 $z^7(z^3+2)=0$。因 $z^3+2$ 为单位，得到 $z^7=0$，继而 $\pi^2-z^4=0$。这证明 $QS\subset C$。

反向有严格整数恒等式

$$
\pi^3=\pi(\pi^2-z^4)+z(\pi z^3),\qquad
z^7=\pi(\pi z^3)-z^3(\pi^2-z^4).
$$

于是 $QS$ 包含 $\pi^3$、$3$、$z^7$ 以及 $z^7+2z^4+\pi^2=(\pi^2-z^4)+z^7+3z^4$，从而 $C\subset QS$。没有以依赖 $w$ 的单位重定义 $z$，原指定基底 $B$ 保持不变。

### 5. 提升不变性、长度与状态消费者

对任意 $f\in S$，两个理想 $Q_z,Q_{z'}$ 都由上一节的恒等式包含 $\pi^3$。在特征 $3$ 的 $S/(\pi^3)$ 中，$z'=z+\pi f$ 满足

$$
\pi z'^3=\pi z^3,\qquad z'^4=z^4+\pi z^3f.
$$

两组生成元仅差可逆初等变换，因此完整理想相等。形式替换 $(z,w)\mapsto(z+\pi f,w)$ 保持极大理想，Jacobian 行列式 $1+\pi\partial_zf$ 为单位；完成局部环的形式逆函数定理保证它确为自同构，包括 $f$ 含非零常数项的情形。

长度计算也准确。因为 $\pi^3\in Q$，圆分关系模 $3$ 所附加的 $\pi^6=0$ 已被蕴含，故

$$
B/Q\simeq k[[\pi,z]]/(\pi^2-z^4,\pi z^3).
$$

加上由上述恒等式得到的 $z^7$ 后，字典序 $\pi>z$ 的首项为 $\pi^2,\pi z^3,z^7$。第一对交叠给出 $-z^7$；第一、第三对给出 $-z^{11}$，可被 $z^7$ 消去；第二、第三对为零。这验证了独立的标准单项式计数：$1,z,\ldots,z^6,\pi,\pi z,\pi z^2$ 共 $10$ 项。$S/C=(B/Q)[[w]]$ 不是长度 $10$ 的 Artin 环，作者已正确限定为横向长度。

允许状态中 $v_\pi(z)\ge1$，所以 $\pi^2$ 与 $z^4$ 的赋值不同，不能抵消：$v_\pi(\pi^2-z^4)=2$，而 $v_\pi(\pi z^3)\ge4$。可逆余切换基在状态上仍可逆，故完整形式的系数最小赋值为 $2$。最后加上 $v_\pi(9)=12$ 得原未整除微分的阶为 $14$。不把这些结论外推到额外分歧状态。

### 6. 导子与有限平台的逻辑边界

固定 $\mathcal O,z$ 的连续导子确实在 $B$ 上为零，因此保持任意扩张理想 $JS$。在导子稳定的截断理想下，这一必要条件会下推；严格失败可以否定指定提升的精确下降。反向不成立，特征 $3$ 中 $(w^3)$ 的例子有效。

本脚本的 $(\pi^n,z^8,w^3)$ 在 $2\le n\le6$ 时确实导子稳定：$D(w^3)=3w^2\in(\pi^n)$。局部解由原能级方程 Hensel 提升，且脚本重新检查 $J_1(x,y)=1+z$；不是任取另一状态参数。有限域理想空间包含两生成元的所有截断单项式倍数，行消元的商维数和导数余类测试有正确含义。但这些测试只记录有限必要条件，完整结论由前五步证明。

## 一次实际命令与输出

在工作区根目录执行的唯一计算命令为：

```text
python docs/research-batch07/qpi_odd_height_two_descent_diagnostic_v1_20260909.py
```

退出码为 `0`；工具返回的 `wall_time_seconds` 为 `0.446007618`。脚本自己记录的时间如下，保留两种原始计时字段，不据此作数学证据或性能主张。完整 stdout 为：

```text
factor=1 sparse_terms=25
factor=2 sparse_terms=126
factor=3 sparse_terms=541
factor=4 sparse_terms=1864
factor=5 sparse_terms=5048
factor=6 sparse_terms=10177
factor=7 sparse_terms=15704
factor=8 sparse_terms=20480
factor=9 sparse_terms=24075
integral_trace_terms=427 alpha_pi_terms=[283, 285] seconds=0.212611
EXACT_FIRST_TANGENT b1(P)=2+a NONZERO
n=2 dimension=48 ideal_rank=27 quotient_dimension=21 D_stability=PASS_BOUNDED_ONLY
n=3 dimension=72 ideal_rank=42 quotient_dimension=30 D_stability=PASS_BOUNDED_ONLY
n=4 dimension=96 ideal_rank=66 quotient_dimension=30 D_stability=PASS_BOUNDED_ONLY
n=5 dimension=120 ideal_rank=90 quotient_dimension=30 D_stability=PASS_BOUNDED_ONLY
n=6 dimension=144 ideal_rank=114 quotient_dimension=30 D_stability=PASS_BOUNDED_ONLY
TOTAL_SECONDS=0.246221
ORIGINAL_MATRIX trace_and_determinant PASS
EXACT_RESIDUE alpha[0]=H^4*dj PASS
SYMBOLIC_F1= x**2*y - x**2 - x*y**2 + x*y + y
LAURENT_DIVISIBILITY A1 monomial_shift=(-6,-7) quotient_terms=25 zero_remainder=True compact_certificate=not_needed
LAURENT_DIVISIBILITY B1 monomial_shift=(-6,-8) quotient_terms=25 zero_remainder=True compact_certificate=not_needed
FIRST_TANGENT_CERTIFICATE R(a,2)=2 PASS
LAURENT_DIVISIBILITY Jx_B1_minus_Jy_A1 monomial_shift=(-8,-9) quotient_terms=48 zero_remainder=True compact_certificate=not_needed
LAURENT_DIVISIBILITY Jx_B2_minus_Jy_A2 monomial_shift=(-6,-9) quotient_terms=32 zero_remainder=True compact_certificate=not_needed
LAURENT_DIVISIBILITY A2_minus_(j+1)_Jx monomial_shift=(-5,-7) quotient_terms=16 zero_remainder=True compact_certificate=PASS
LAURENT_DIVISIBILITY B2_minus_(j+1)_Jy monomial_shift=(-4,-8) quotient_terms=12 zero_remainder=True compact_certificate=PASS
TOTAL_WITH_SYMBOLIC_SECONDS=0.514643
```

读文件、`wc -l`、`sha256sum` 和精确目标路径检索属于只读输入确认。目标文件检索在创建前无匹配，返回码 `1`，表示没有覆盖既有审查稿，并非数学测试失败。脚本不写数据文件。本审查不把同一脚本的重跑冒充第二套独立实现；独立性来自非作者对原项转录、算法和完整代数推论的实际检查，运行只是对明确证书的复算。

## Corrections or Missing Assumptions

没有需要修改作者限定 Claim 的数学更正。特别确认以下容易越界之处均已受控：原 $z$ 未更换，首切向单位而非单一法向非零值被验证，$\pi^3$ 属于完整原理想而非仅属于截断像，横向长度未冒充三维闭点商长度。

## Open Risks 与最终交付边界

- 原 $j$ 在四末端图的正则性、末端原两系数理想和完整 Hasse 纤维覆盖均未检查，也未被本报告接受。只凭环面 Laurent 恒等式不能新增这些结论。
- 其他奇素数、高度、时间、Hasse 根以及额外分歧状态均不在输入和验证范围。没有以本例替代一般比较定理。
- 本报告不证明积分闭包与基变交换，不新增 Rees 赋值、正规化爆破或新意/容量判断。
- 已限定局部命题的新增数学门槛通过；可保存此短闭合接口。是否依原停止规则终止完整 I01 投入，由主控结合既定规则及 D05 的独立结果决定，不由本数学票产生新的研究授权。
