# qPI：所有奇素数圆分层的完整首 jet 因子分解 V1

日期：2026-09-09。作者：主控 `/root`。新的有界作者证明；不是独立接受或正式候选。
`route_applicability: NOT_APPLICABLE`。仅新增本件，既有证明与失败票不修改。

## Claim

固定奇素数 $p$、$a\ge2$、$N=p^a$ 与
$$\sigma=1+p+\cdots+p^{a-1},\qquad r=\sigma-1=p+p^2+\cdots+p^{a-1}.$$
取 $q_a=\zeta_{p^a}$、$\pi_a=q_a-1$，$\mathcal O_a$ 为对应圆分 DVR
或其有限无分歧扩张，剩余域为有限域 $k$。允许完成，不另加有分歧基变换。
任取单位时间 $t_a\in\mathcal O_a^\times$，在原完整八截面模型 $\mathcal U_a$ 上取
$$\alpha_N=N^{-1}d_{\rm state}I_N.$$
记 $B=\mathcal O_a/(\pi_a^2)$、$\epsilon=\pi_a\bmod\pi_a^2$。

取首层 DVR $\mathcal O_1$，使其剩余域同为 $k$；记
$q_1=\zeta_p,\pi_1=q_1-1$。存在 $k$-代数同构
$$\mathcal O_1/(\pi_1^2)\simeq B\simeq k[\epsilon]/(\epsilon^2),\qquad
\pi_1\longmapsto\epsilon,\quad q_1\longmapsto1+\epsilon.$$
选择 $t_1\in\mathcal O_1^\times$，使其在该同构下的像等于 $t_a\bmod\pi_a^2$。
两套原八截面模型的 $B$-基变换逐中心相同，记共同完整开放曲面为 $\mathcal U_B$。
设 $\alpha_p^{[2]}$ 为首层原 $p^{-1}dI_p$ 在此共同模型上的约化，
$\alpha_N^{[2]}$ 为 $\alpha_N$ 的相应约化。

记 $U_0=\mathcal U_B\otimes_B k$，$T=\bar t_a$，
$$J=y+x/y-x-T/x,\qquad
H=H_p(T,J)=[Z^{p-1}]\bigl((T+JZ+Z^2)^2-4Z^3\bigr)^{(p-1)/2}.$$
这里 $J$ 与 $H$ 是完整 $U_0$ 上的正则函数。
对 $H$ 的任一局部提升 $\widetilde H\in\mathcal O_{\mathcal U_B}$，
$\widetilde H^{r}$ 与提升选择无关，故粘成全局函数，记为 $H^{\langle r\rangle}$。

**FJ.1：完整两状态一形式恒等式。**
$$\boxed{\quad\alpha_N^{[2]}=H^{\langle r\rangle}\alpha_p^{[2]}
\quad\text{于 }\Gamma(\mathcal U_B,\Omega^1_{\mathcal U_B/B}).\quad} \tag{F1}$$
它比较的是两个圆分环的二阶商上同一原模型，不是通过嵌入
$\zeta_p\mapsto\zeta_{p^a}^{p^{a-1}}$ 作有分歧基变换。
后者会把 $\pi_1$ 送到高阶参数，不能用于 (F1)。

**FJ.2：光滑有限能级附近的准确截断系数理想。**
对任一光滑有限 $X_h=(J=h)$ 及其任一点 $P$，在
$\mathscr A=\mathcal O_{\mathcal U_a,P}$ 中取 $H$ 的任意提升 $\widetilde H$，则
$$\boxed{\quad
\mathfrak c(\alpha_N)_P+(\pi_a^2)
=(\pi_a^2,\widetilde H^{\sigma},\pi_a\widetilde H^{\sigma-1}).\quad} \tag{F2}$$
若 $h$ 是 Hasse 根，重数为 $e_h$，完成后取 $\bar z=J-h$，有
$$\widehat{\mathfrak c(\alpha_N)}_P+(\pi_a^2)
=(\pi_a^2,z^{e_h\sigma},\pi_a z^{e_h(\sigma-1)}). \tag{F3}$$
不假定根简单。若 $H_p(T,h)\ne0$，(F2) 两边都是单位理想。

特别地，约化到光滑超奇异能级的任一无分歧 DVR 状态提升，其实际 $\alpha_N$
两个系数的公共 $\pi_a$ 赋值至少为二；普通层准确为零。
这里不将至少二写成准确二。未整除 $dI_N$ 的相应下界是
$a\varphi(p^a)+2$，普通层准确为 $a\varphi(p^a)$。

## Status、Assumptions 与范围

**PROVABLE AS STATED**（作者合成判断，仍须独立检查本件及首 jet 迭代引理）。
FJ.1 不依赖首层切向非消失；FJ.2 还消费正在独立核查的首层完整理想定理。
这些输入在下面分开列明，作者状态不替代合取接受。

本件固定 $m=1$，覆盖所有奇 $p$ 与所有 $a\ge2$，但只求模 $\pi_a^2$ 的准确结构。
它不替代发散 P03 的全厚度／全 $m$ 目标，也不主张构造稳定约化或晶体比较。
$p=2$ 不适用，因为首层 $\mathcal O_1/(\pi_1^2)$ 不具有特征二。

## Inputs and Dependency Map

1. 已接受[原完整模型 G](PAPER30_QPI_CYCLOTOMIC_GLOBAL_MODEL_DIAGNOSTIC_V1_20260909.md)
   的八截面构造、G3 的 $\alpha_N$ 全局正则及小阶 $J$ 完整正则性。
   逐截面光滑吹起与移去相同边界可在本件明确的商环上基变换。
2. [首 jet 矩阵引理](PAPER30_QPI_VERTICAL_ALPHA_FIRST_JET_MATRIX_LEMMA_V1_20260909.md)，
   SHA-256 `f3618fa1345804ce5d93acae4e6fdb2b3ee7761a87ae2de8bc453d24944971bd`：
   原降序插入、先除 $N$ 后约化、任意奇素数幂的首阶公式及时间提升约定。
3. [数字分解引理](PAPER30_QPI_VERTICAL_ALPHA_FIRST_JET_ITERATION_V1_20260909.md)，
   SHA-256 `b304378b32bbd481a86b2416528797378d04a3f0050bdd6b52d5aa251ad064f4`：
   原矩阵上的 $\beta_N=H^{\sigma-1}\beta_p$ 及零阶系数 $H^\sigma dJ$。
   本件不消费其未证明的整片光滑开集切向正则延拓假设；用 (F1) 单独闭合完整原模型接口。
4. [所有素数首层理想证明](PAPER30_QPI_VERTICAL_ALPHA_ALL_PRIME_HEIGHT1_PROOF_V1_20260909.md)，
   SHA-256 `ffdcfc37860477e990f836721898fc654537bb3254b7335876581990c2da4f74`：
   只为 FJ.2 消费 $\mathfrak c(\alpha_p)=(\pi_1,\widetilde H)$。
   该件的全素数证明与本件的全层首 jet 证明是不同责任范围。

策略：识别两个二阶商及实际模型；用 $p\mid r$ 粘出典范乘数；
在原环面应用两条已写出的系数公式；由局部自由模的限制单射延到全部末端线；最后计算理想的像。

## Proof

### Step 1. 二阶商及时间提升的实际识别

圆分 Eisenstein 多项式给
$$v_{\pi_a}(p)=p^{a-1}(p-1),\qquad v_{\pi_1}(p)=p-1\ge2.$$
因此两个商环都具有特征 $p$，最大理想平方为零，且其 $k$-维数为二。
在任一这样的商环中，有限剩余域 $k=\mathbb F_{p^f}$ 通过
$X^{p^f}-X=0$ 的唯一根提升嵌入：导数为 $-1$，而任意剩余元素的两次提升
相差的平方零元可唯一修正。根的集合在加法、乘法下封闭，给与约化互逆的系数域。
于是每个元素唯一写成 $c_0+c_1\pi_i$，$c_0,c_1\in k$。
这证明上述指定参数同构，不依赖并不存在的圆分 DVR 非分歧嵌入。

商映射满射，所以所需 $t_1$ 存在，且因 $T\ne0$ 为单位。
首层 $t_1$ 的更高阶提升不影响 $B$ 上的原八中心或一形式 $\alpha_p^{[2]}$：
在环面该一形式由整数循环插入多项式给出，完整模型上的唯一延拓也随相同商基变换确定。

八中心只使用原单位坐标 $1,t,t,q$ 及固定吹起顺序。
两个模型的 $t,q$ 在 $B$ 上完全相同；中心是光滑截面，其局部理想由相对坐标正则列给出，
吹起各标准图即相同坐标代换。故不需要把任意非平坦吹起基变换当作通用定理，
本模型可逐个标准图直接识别。边界严格变换和所移去的八分量也相同。
这给共同光滑相对曲面 $\mathcal U_B$ 及同一秩二微分模。

### Step 2. Hasse 乘数的全局粘合

任意两个 $H$ 的局部提升相差 $\epsilon f$。因为 $p\mid r$，在特征 $p$ 的 $B$-代数中
$$ (\widetilde H+\epsilon f)^p=\widetilde H^p+(\epsilon f)^p=\widetilde H^p.$$
将此式提升到整数幂 $r/p$，得到
$$(\widetilde H+\epsilon f)^r=\widetilde H^r.$$
因此各提升的 $r$ 次幂在重叠处完全相等，粘为 $H^{\langle r\rangle}$。
这里既没有假定 $J$ 存在一个全局整提升，也没有除以 Hasse 函数。
这一步是将环面公式移到完整厚化所需的关键：单独的 $\widetilde H$ 可以不全局存在，
但其上述 Frobenius 整倍数幂确实存在。

### Step 3. 环面上的完整首 jet 恒等式

在共同原环面上取实际 $t\in B^\times$，记 $J_t=y+x/y-x-t/x$，
并以整数系数提取式定义 $\widetilde H=H_p(t,J_t)$ 于 $B$。
首 jet 矩阵引理与数字分解引理给
$$\alpha_N^{[2]}=\widetilde H^\sigma dJ_t+
\epsilon H(T,J)^{\sigma-1}\beta_p,$$
$$\alpha_p^{[2]}=\widetilde H dJ_t+\epsilon\beta_p.$$
乘 $\epsilon$ 的系数只取剩余值；两式的零阶参照项都使用同一个实际 $t$。
因此任意 $t=T+\epsilon t'$ 引起的 $J_t,dJ_t$ 变化已全部保留，未将其错删为固定剩余时间。
从这两式直接得到
$$\alpha_N^{[2]}=\widetilde H^{\sigma-1}\alpha_p^{[2]}.$$
它是完整一形式恒等式，不仅是将两边投到 $dJ$ 的商模后的切向等式。
Step 2 将此处的乘数识别为 $H^{\langle r\rangle}$。

### Step 4. 从环面延到全部四条末端线

两边已在共同 $\mathcal U_B$ 上正则：左边与 $\alpha_p^{[2]}$ 来自原全局整除证明，
乘数由 Step 2 给出。其差是局部自由微分模中的截面，并在原环面为零。

为避免在非约化 $B$ 上仅用集合稠密作错误推论，逐末端图检查限制单射。
四图均为 $B[u,v]$ 在一个剩余为单位的因子处的局部化，
原环面由再反演 $u$（以及原已可逆单位）得到。
$u$ 在多项式环上是非零因子，即使 $B$ 含平方零元仍如此；局部化保持这一性质。
微分模自由，所以它到反演 $u$ 后的模的映射也是单射。
故在环面为零的截面在每个完整末端图为零；这些图与环面覆盖 $\mathcal U_B$。
于是 (F1) 在整个原开放曲面成立，不引入未证明的 $\beta_p$ 全局正则性假设。

### Step 5. 系数理想的准确像

在 $P\in X_h$ 的局部秩二模中，取任意基。
对任一标量 $g$ 与一形式 $\eta$，系数定义直接给
$$\mathfrak c(g\eta)=g\,\mathfrak c(\eta).$$
这里无需 $g$ 为非零因子或单位。
首层 V1 的理想等式取模 $\pi_1^2$，在共同模型上得到
$$\mathfrak c(\alpha_p^{[2]})=(\epsilon,\widetilde H).$$
由 (F1) 有
$$\mathfrak c(\alpha_N^{[2]})
=(\epsilon\widetilde H^{\sigma-1},\widetilde H^\sigma).$$
原局部环到模 $\pi_a^2$ 局部环的满射，其上述理想的原像恰好是 (F2)。
换 $H$ 的提升不会改变这一原像；也可由 Step 2 和已显示的两个生成元直接核准。

在 Hasse 根 $h$ 附近，$H=(J-h)^{e_h}U(J)$，其中 $U(h)\ne0$。
选择 $\widetilde H=z^{e_h}\widetilde U$，$\widetilde U$ 为单位提升，
从 (F2) 删除两个生成元中的单位因子，再取有限模完成，得到 (F3)。
闭点在需要时作有限剩余域／无分歧扩张来定义 $h$ 与光滑完成坐标；
非闭点直接用局部自由模及理想等式，不对它作有限域定义要求。

若一个无分歧 DVR 状态提升约化到超奇异层，$\widetilde H$ 的评价属于 $(\pi_a)$。
由于 $\sigma\ge p+1\ge4$，(F2) 右边沿该提升的像为 $(\pi_a^2)$。
这只推出 $\mathfrak c(\alpha_N)$ 的评价包含于 $(\pi_a^2)$，不推出它等于 $(\pi_a^2)$。
普通层的原约化 $H^\sigma dJ$ 非零，至少一个系数为单位。
最后乘 $N=p^a$ 并用 $v_{\pi_a}(N)=a\varphi(p^a)$ 给出未整除形式的陈述。证毕。

## Verification and Open Risks

- 本件使用代数恒等式与原模型标准图作全称证明，没有从有限 $p,a$ 样本推断全层结果。
- 原数字分解作者件已由主控全文读取，但截至本件写入仍待非作者检查；
  首层完整理想及其两份基础引理也应按实际独立报告状态合取接受，不由本件预授。
- $\alpha_p^{[2]}$ 是另一个首层对象在同构二阶商下的比较量；
  不是高层圆分环中 $p^{-1}dI_p$ 的自然根嵌入拉回。
- 所有末端线都在 (F1) 范围内；没有用仅有环面正则性的 $\beta_p$ 冒充全局一形式。
- (F2) 是模 $\pi_a^2$ 的准确理想，不是完整理想或完整 initial ideal；
  不能读成 $\mathfrak c(\alpha_N)=(\pi_a^2,\widetilde H^\sigma,\pi_a\widetilde H^{\sigma-1})$。
- 更高首非零阶及其状态／时间依赖仍 OPEN；$p=3,a=2$ 的有限端点 probe 单独记录，
  不能替代全状态全层证明。$p=2$ 与 $m>1$ 均未由本件处理。
- 不新增正式候选或容量判断，不创建论文、锁、PDF，不产生外部效力。
