# Paper30 qPI：全剩余阶首层与奇素数高层模平方的数学接受

日期：2026-09-09。主控 `/root`。效力：本地有界数学接受。
`route_applicability: NOT_APPLICABLE`。不是正式候选、论文准入、新意或 PDF 验收。
Batch07 仍为 3/5；Paper30 未立项，Paper31 未开展。

## 1. 本次实际完成的责任

主控已全文读取并接受下列两个独立责任包，输入身份见 §4。

| 责任 | 作者件 | 非作者检查及实际范围 |
|---|---|---|
| 所有素数、所有剩余阶的首层原理想与准确类比较 | [TH 全 tame 实际接口](PAPER30_QPI_VERTICAL_ALPHA_ALL_TAME_HEIGHT1_PROOF_V1_20260909.md)219行；[prime trace 引理](PAPER30_QPI_VERTICAL_ALPHA_PRIME_TRACE_CONGRUENCE_LEMMA_V1_20260909.md)269行 | [全文独查](PAPER30_QPI_VERTICAL_ALPHA_ALL_TAME_HEIGHT1_INDEPENDENT_CHECK_V1_20260909.md)286行，全部 PASS；实际 A1–A4 及原整数同余均核准 |
| 所有奇素数、所有高度与剩余阶的完整模平方比较 | [TB 全块首 jet](PAPER30_QPI_VERTICAL_ALPHA_TAME_BLOCK_FIRST_JET_LEMMA_V1_20260909.md)335行 | [全文独查](PAPER30_QPI_VERTICAL_ALPHA_TAME_BLOCK_FIRST_JET_INDEPENDENT_CHECK_V1_20260909.md)360行，TB.1–TB.2 PASS；未预设任何首层理想 |

TH 所消费的[抽象 OC 引理](PAPER30_QPI_VERTICAL_ALPHA_OBSTRUCTION_CARTIER_LEMMA_V1_20260909.md)
及其[条件独查](PAPER30_QPI_VERTICAL_ALPHA_OBSTRUCTION_CARTIER_INDEPENDENT_CHECK_V1_20260909.md)
也已由主控全文读取；TH 独查逐项核准其实际 A1–A4。
已接受 U/G 的使用限于同一自然复形、真实常数项、原八截面和实际完整模型，未重开不变输入。
TB 的首矩阵／原模型接口按同哈希旧接受合取，首层结果不用于其作者证明。

两位检查者均接触过本方向，并非盲审、正式四门票或人类认证。
TH 检查者写过旧纯配对结果，但这些旧结果未用于 TH 的新整数迹／障碍／Čech 链；
TB 检查者不是 TB 作者，也未读取 TH 新审查来填补其责任。
独立有限精确测试仅作排错；所有量词由正文证明承担。

## 2. 接受的首层结论：全部 p 与 p∤m

取 $\mathcal O=\mathcal O_0[\zeta_p]$，$\mathcal O_0$ 无分歧且含精确 $m$ 阶单位根
$\widetilde\eta$，$p\nmid m$，$\pi=\zeta_p-1$，$s=\widetilde\eta\zeta_p$。
时间 $t$ 为任意单位，微分只作用于原两个状态。
固定原 $I_{mp}$、原完整开放曲面 $\mathcal U$ 和原小阶 $J=I_{m,\eta}(x,y;\bar t)$。
令 $T=\bar t^m$、$\varepsilon_m=(-1)^{m+1}$、$H=H_p(T,J;\varepsilon_m)$。
对每条完整光滑有限原能级 $X=(J=h)$、每个 $P\in X$，接受
$$\boxed{\mathfrak c(p^{-1}dI_{mp})_P=(\pi,\widetilde H)_P.}$$
这包括四条末端线，不要求 Hasse 根简单；完成式为 $(\pi,z^{e_h})$。
无分歧状态提升的两系数公共阶在超奇异层准确为 $1$、普通层准确为 $0$，
未整除 $dI_{mp}$ 的准确阶分别为 $p$ 和 $p-1$。

新的实际比较不是只说两个数值相等：
$$\kappa_J=\rho_X\beta_{L_m}(J)\ne0\quad\text{in }H^1(X,\mathcal O_X),$$
$$\boxed{\partial\nu=\operatorname{Fr}_*(\kappa_J)\ne0
\quad\text{in }H^1(X,\mathcal O_X^p)}$$
在超奇异分支成立。
这里 $\beta_{L_m}$ 来自原 $L_m$ 在 $\mathcal O/(\pi^2)$ 的一阶 Bockstein，
其唯一核是真实常数；$\rho_X$ 是每条完整有限能级的实际限制同构。
原 $I$ 的整数 $p\pi$ 同余由循环词轨道证明，再经四图的非约化限制单射延拓。
局部原函数的余差准确为 $f_{ij}^p$，所以这确为原整除微分的首切向类。

到像层 $\mathcal O_X^p$ 的 Frobenius 是加法层同构；随后映入
$H^1(X,\mathcal O_X)$ 的上同调箭头可以杀掉该类，不能把两箭头合并。
特征二分别使用 $\lambda=-1$ 的原迹同余和特征四的二阶 Bockstein，未套用奇素数双数模型。
全过程不需要尚未证明的一般 $m$ 配对数值 $m^2$，也不把结论冒称晶体模同构。

## 3. 奇素数全高度首 jet 及同模型理想合取

取任意奇素数 $p$、$a\ge2$、$N=p^a$、$\sigma=1+p+\cdots+p^{a-1}$，
保留任意 $p\nmid m$、单位时间及原圆分模型。
在指定的首层／高层二阶商同构 $\pi_1\mapsto\pi_a\bmod\pi_a^2$ 下，接受完整一形式恒等式
$$\alpha_{mN}^{[2]}=H^{\langle\sigma-1\rangle}\alpha_{mp}^{[2]},
\qquad \alpha_{mN}=p^{-a}dI_{mN}.$$
这不是自然根嵌入；两层实际 $s,t$ 的二阶 jet 匹配，八中心逐个相同。
块内共振／非共振变化及外部速率 $m$ 均保留；一般 $m$ 的交换子投影确实允许第五次项。
其支持经幂乘后仍落在 $[1,2p-1]$，唯一数字分解给准确指数。
非素域样本另排除了误把 Frobenius 当作恒等的实现错误，但不承担一般证明。

现将这一已核一形式恒等式与 §2 同一原模型的首层理想合取。
记 $B=\mathcal O_a/(\pi_a^2)$、$\epsilon=\pi_a\bmod\pi_a^2$；取任意局部余切基，
按系数定义即有 $\mathfrak c(g\omega)=g\mathfrak c(\omega)$，即使 $g$ 是零因子也成立。
所以
$$\mathfrak c(\alpha_{mN}^{[2]})
=(\epsilon\widetilde H^{\sigma-1},\widetilde H^\sigma).$$
取商环满射的原像，得到每个光滑有限能级附近的准确式
$$\boxed{\mathfrak c(\alpha_{mN})+(\pi_a^2)
=(\pi_a^2,\widetilde H^\sigma,\pi_a\widetilde H^{\sigma-1}).}$$
任意局部提升均可：$p\mid\sigma-1$ 使其乘数幂在 $B$ 上与提升无关，
而 $\sigma$ 次幂的变化已包含于另一个显示生成元。
若 Hasse 根重数为 $e_h$，完成后为
$$ (\pi_a^2,z^{e_h\sigma},\pi_a z^{e_h(\sigma-1)}).$$
这段系数消元是两份已核结论在相同模型上的直接合取，不另计一个新理论结果。

沿光滑超奇异层的无分歧状态提升只推出公共阶至少二；普通层准确零。
乘回 $p^a$ 后分别为下界 $a\varphi(p^a)+2$ 和准确阶 $a\varphi(p^a)$。
未接受完整高层理想，也没有把加上 $(\pi_a^2)$ 后的等式读成原理想等式。

## 4. 输入身份与当前后续

本次全文读取后实际核对的目标身份为：

| 文件 | SHA-256 |
|---|---|
| TH 全 tame 首层作者 | `43049d8688f59f57eb3362246d06507ff397ee9e150d18a3443ae8a18990be75` |
| prime trace 作者 | `07361a2516b8e891d037a59826e0e789119db93eb78332dc41783f075f15dca9` |
| TH／prime trace 独查 | `26b01f26f16837f6fd13c4492a46115eeab2cd5c9ac2278bc85f39d1483bf6f5` |
| TB 作者 | `6546720ecf39f667f09d45235dc0c7be340032b4c3f7c809e9d1cb60257396e9` |
| TB 独查 | `caaf7de60b9bda61db9ea413dab736aa06f71eb6e94cc2f2c939774dd8572a88` |

OC 和 U/G 的精确身份已在上述两份报告中绑定，主控已亲读必要全文／实际接口并核相同输入。
此前 $m=1$ 首层及 [N9 有限诊断接受](PAPER30_QPI_VERTICAL_ALPHA_HIGHER_JET_MATHEMATICS_DISPOSITION_V1_20260909.md)
保持，不因现在全 $m$ 包含其中而重复计功。

特征二高层尚不由 §3 覆盖：首层二阶商为特征四，不能套用该商同构。
目前已开展新的 $a=2$ 基层／高层比较与首切向接口诊断，尚无新接受。
新的 Čech／算术提升来源增量也仍在有界核查；一般机制必须扣除，实际识别价值仍待评价。
奇异能级、额外分歧状态、完整高厚度／初始理想均保持明确开放。

所有旧正式失败票、source/publication locks、冻结作者件及已接受产物不改。
本次没有立项、写稿、试排、GPU、投稿、上传或其他外部效力；原22–30页及独立完整验收标准保持。
