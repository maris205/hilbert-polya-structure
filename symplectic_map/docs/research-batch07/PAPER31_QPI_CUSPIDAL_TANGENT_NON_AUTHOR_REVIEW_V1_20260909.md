# P31 原首层尖点切向诊断：非作者有界检查 V1

日期：2026-09-09 UTC。检查者：`/root/p31_qpi_portfolio_baseline_v1`。
被查作者：`/root`；目标为 [作者诊断 D] 的完整 185 行，终态 SHA 见 §10。
本检查者未参与 D 的证明、修改或写作；此前承担 qPI 组合基线盘点，接触过既有处置和接口边界。
因此是非作者独立数学检查，不冒称对方向／旧背景盲审、跨模型校验、人类评审或正式候选四门票。
本人 FULL 读取 proof-writer 技能，按其“固定量词—依赖图—逐步检查—诚实状态”组织本件；不替作者修改原稿。
唯一新写本报告，不改 D、基线、P30 接受源、旧记录、锁、索引或编译产物。

## 1. Claim：准确被查命题

固定 P30 原矩阵、降序词积、八中心模型、全部四末端线、单位时间及两个相对状态方向。
取 $p\ge5$、$p\nmid m$、$s=\widetilde\eta\zeta_p$、$\pi=\zeta_p-1$，
$J=I_{m,\eta}(x,y;t_0)$、$T=t_0^m$、$\varepsilon=(-1)^{m+1}$、$I=I_{mp,s}$、$\alpha=p^{-1}d_{\rm state}I$。
在代数闭剩余域 $k$ 上令 $T=-27/256$、$h=9\varepsilon/8$、$X=(J=h)$。
完整命题保留 D 的四项：原 $X$ 是尖点有理曲线且 $H_p(T,h;\varepsilon)=0$；实际限制类 $\kappa_J\ne0$；
原 $G_i=(I-F(j_i))/(p\pi)$ 导出的 Kähler 类 $\nu$ 在 $p=5,7$ 是非零尖点扭微分、在 $p\ge11$ 为零；
所有 $p\ge5$ 时 $\nu|_{X_{\rm sm}}=0$，且每个光滑几何点 $P$ 有 $\pi\notin\mathfrak c(\alpha)_P$。
不把“完整奇异纤维的光滑点”替成“完整光滑纤维”，也不声称尖点处原完整理想或最小包含的 $\pi$ 幂。

## 2. Status

`PROVABLE AS STATED`；有界新消费者检查结果：`PASS_BOUNDED_MATHEMATICS`。
六步在 D 的既定对象与量词下成立，未发现反例、循环依赖或必须修正的硬数学缺口；原命题不需削弱。
该判断只接受本报告实际核查的诊断推理，不重签 P30 全稿，不授 P31 新意、价值、容量、准入或产物 PASS。
P30 在完整光滑纤维上的原理想定理不受影响；D 精确排除了将其直接推广到这类奇异完整纤维之光滑点的做法。

## 3. Assumptions 与 Notation

P30 首层环及其原光滑相对曲面继续有效，$t$ 为任意允许单位提升，$\bar t=t_0$；微分固定时间与底环。
已接受 [DG] 的同基完整模型出口按精确合同使用，不重审其上游 Jacobian／最小模型整条证明。
其域上阶数在本题是 $m$，不是混合特征的 $mp$；因此 $p\nmid m$ 正好处于该旧出口的允许范围。
$L_m=\mathcal O_S(mD)$，$X$ 是剩余曲面上的完整 Cartier 纤维，原截面 $1$ 平凡化 $L_m|_X$。
$U=\operatorname{Spec}A$、$A=k[\xi,\upsilon]/(\upsilon^2-\xi^3)=k[r^2,r^3]$，$V=\operatorname{Spec}k[r^{-1}]$。
$r$ 是正规化函数域参数，通常不属于 $A$；$[r]$ 是 Čech 上同调类，$\kappa_J=b[r]$、$b\in k^\times$。
$\tau=2\xi\,d\upsilon-3\upsilon\,d\xi$；这里 $\tau$ 只是尖点扭微分，不是非单位时间参数。
$F$ 与 $\widehat H=F'/p$ 始终是 [S6] 中原 $m$-块产生的整数多项式，不替换成任意 Hasse 等价公式。

## 4. Proof Strategy 与 Dependency Map

本轮只重核“旧准确出口如何进入奇异新消费者”，然后在明确环内独立重算 Čech、扭元与理想消去。

| 新步骤 | 实际必要输入 | 本轮检查判定 |
|---|---|---|
| 1：原 $X$ 的尖点身份 | [DG] 同原能级完整模型；[S3] 纯 W 方程 | 同基特殊纤维同构足够；未把纯谱方程本身当作原状态识别 |
| 2：$\kappa_J\ne0$ | [S6] 45–114 的边界 Bockstein、常数层消失、完整有限除子序列 | 已核此段不使用纤维光滑性；原限制同构继续成立 |
| 3：$H(h)=0$ 与 $\nu$ 拼接 | [S6] 整数 trace/Taylor、[S5] 非约化全图注入；步骤 2 与尖点 $H^1$ | 不先假设 Hasse 为零；不调用光滑 Cartier 核层结论 |
| 4：实际 $\nu$ 的精确代表 | 原 $G_i$ 差式、实际类 $b[r]$、$H^0(X,\mathcal O_X)=k$ | 只按余边界调整剩余原函数，导数不变；符号相同 |
| 5：各素数扭性／消失 | 明确 $\Omega^1_{A/k}$ 呈示与半群环 | 已重算 $\operatorname{Ann}(\tau)$、$\operatorname{Ann}(\xi\tau)$ 及 $d_A(r^p)$ |
| 6：原 $\pi$ 非包含 | [S6] 原完整局部式、[S5] 光滑原模型，$\nu|_{X_{\rm sm}}=0$ | 在原局部环消去；不靠状态赋值、W 的混合特征替代模型或完整临界理想猜式 |

## 5. Proof check：步骤 1–2，原模型与奇异限制

### 5.1 同基模型消费与坐标核对

[S3] 24–25 明说该处 W 是纯代数模型，不能单独供应 $X\simeq W_h$；D 实际另调用 [DG] 100–106 的同原 $c$ 模型同构，责任没有混淆。
在代数闭 $k$ 上，原有限能级局部 henselization 的剩余域不变，故该同构限制到完整特殊纤维即得原 $X\simeq W_h$。
此处只识别剩余域上的曲线，没有将它提升成混合特征原曲面与某个 W 提升的同构；后面的 $\alpha$ 仍在原曲面计算。
对 D 66–70 的配方逐系数核得
$$h^2/4-T=27/64,\qquad-h\varepsilon T/2=243/4096,\qquad T^2/4=729/262144.$$
它们正是 $(u+9/64)^3$ 的三个系数；$\xi=u+9/64$、$\upsilon=v+(h/2)u-\varepsilon T/2$ 为可逆仿射线性变换，并可齐次化成射影线性变换。
分母只含 $2$，而 $T\ne0$ 还用 $p\ne3$；$p\ge5$ 足够。奇点坐标 $z=-3\varepsilon/16,u=-9/64,v=27\varepsilon/1024$ 与原能级公式吻合。
代数闭域中可取 $t_0^m=T$，故任意允许 $m$ 的参数情形非空；无穷点光滑，标准两个仿射开集覆盖完整尖点曲线。

### 5.2 Bockstein 非零未误用光滑性

本人读完 [S6] 原 obstruction 命题及证明：边界节点消元、$1-s^m\equiv-m\pi$、$\ker\beta_L=k\langle1\rangle$ 发生在 $S,D,L_m$，未选光滑纤维。
$p\nmid m$ 保证边界 Bockstein 非零；原 $J$ 非常值，故 $\beta_L(J)\ne0$，不需要随意归一化边界系数。
对本尖点纤维，$J-h\cdot1$ 仍定义完整 Cartier 除子且不遇 $D$；D 85–86 的序列与 [S6] 98–113 完全对应。
原 $1$ 在 $X$ 处无零点，$H^1(S,\mathcal O_S)=H^2(S,\mathcal O_S)=0$ 使限制 $\rho_X$ 为同构；没有对 $X$ 本身使用光滑消失定理。
Čech 约定 $c_j-c_i$ 固定了 $f_{ij}=\overline{(j_j-j_i)/\pi}|_X$；因此非零的是原实际 $\kappa_J$，不是任取一个非零 $H^1$ 元素。

## 6. Proof check：步骤 3–4，Frobenius 与实际原函数

### 6.1 原 trace／Taylor 的全图适用性

本人 FULL 读 [S6] 的 prime-trace 与 ramified Taylor 引理、完整证明及 $G_i$ 延拓段；它们的假设没有光滑能级或 $H(h)=0$。
[S6] 262–274 用 [S5] 的图注入在 $\mathcal O/(p\pi)$ 上延拓，而非用非约化底的点集稠密性；[S5] 211–229 对该商环有效，故四条末端线无缺失。
更早的 [S5] 165–205 给 $I$ 与 $\alpha$ 的原完整正则性、底上光滑性与几何整剩余曲面；没有换用谱等价一形式。
由 $G_i$ 定义及 [S6] 224–260，在任意重叠上确有
$$\bar G_j|_X-\bar G_i|_X=-H_p(T,h;\varepsilon)f_{ij}+f_{ij}^p.$$
这里负号来自 $G_j-G_i=-(F(j_j)-F(j_i))/(p\pi)$；Taylor 的 $-f^p$ 因而变成 $+f^p$。

### 6.2 先求 Hasse 值，不存在循环

上式左边是实际零链的余边界，在 $H^1(X,\mathcal O_X)$ 中为零，因此 $F_{\mathcal O,*}\kappa_J=H(h)\kappa_J$ 无需先假设 $H(h)=0$。
$U,V,U\cap V$ 均仿射，$U\cap V=\operatorname{Spec}k[r,r^{-1}]$，故 Čech 商只剩单项式 $r$ 的类：$H^1(X,\mathcal O_X)=k\cdot[r]$。
Frobenius 是半线性的，准确为 $b[r]\mapsto b^p[r^p]$；$r^p\in A$ 对 $p\ge5$ 成立，所以这个目标为 $H^1(\mathcal O_X)$ 的算子是零。
步骤 2 已独立给 $\kappa_J\ne0$，因此 $H(h)=0$。这并未把尖点称为光滑超奇异曲线，也未调用光滑闭 Hasse 识别反推该值。
此后原重叠式化为 $\delta\bar G=f^p$，Kähler 微分杀掉 $p$ 次幂，即可定义全曲线 $\nu$。
[S6] 318–343 的正规／光滑核层及非零微分处处不消失论证没有被消费；这正是新旧结论的关键分界。

### 6.3 Čech 代表更换与符号

取公共仿射细化；相同上同调类意味着 $f-f^{\rm std}=\delta c$，其中标准双开集代表 $f^{\rm std}_{UV}=br$。
令 $G'_i=\bar G_i-c_i^p$，则 $dG'_i=d\bar G_i$，且 $\delta G'=(f^{\rm std})^p$；这只用特征 $p$ 的 Frobenius 加法性，不需 $\ker d=\mathcal O_X^p$。
标准零链 $g_U=-b^pr^p,g_V=0$ 有 $g_V-g_U=b^pr^p$，与指定约定一致；$r^p\in A$ 保证 $g_U$ 正则。
$G'-g$ 在公共细化上拼成 $X$ 的全局正则函数。完整几何整射影曲线的该函数为 $k$ 中常数，故其 $k$-微分为零。
因此实际 $\nu|_U=-b^pd_A(r^p)$、$\nu|_V=0$；不是通过任取同支撑的扭微分替代原迹所生的形式。

## 7. Proof check：步骤 5，尖点扭元及素数分支

由 $\Omega^1_{A/k}=A^2/A(-3\xi^2,2\upsilon)$，$a\tau=0$ 等价于
$a(-3\upsilon,2\xi)=g(-3\xi^2,2\upsilon)$ 对某个 $g\in A$ 成立。
在 $k(r)$ 中第二坐标给 $g=a/r$，代回第一坐标一致；$2,3$ 可逆且 $A$ 是整环，未丢失零因子条件。
半群指数 $0,2,3,4,\ldots$ 说明 $a/r\in A$ 恰要求 $a$ 的常数项与 $r^2$ 项为零，故
$$\operatorname{Ann}_A(\tau)=(\upsilon,\xi^2),\qquad
\operatorname{Ann}_A(\xi\tau)=(\xi,\upsilon).$$
第二式亦可由第一式取冒号理想得到；所以 $\tau$、$\xi\tau$ 都非零，$\xi^2\tau=0$，其有限支撑均为尖点。
令 $n=(p-3)/2$，则 $r^p=\xi^n\upsilon$，且 $n=-3/2$ 在 $k$ 中成立。因此
$$d_A(r^p)=n\xi^{n-1}\upsilon\,d\xi+\xi^n\,d\upsilon
=\frac12\xi^{(p-5)/2}\tau.$$
乘以单位 $-b^p$ 不改 annihilator：$p=5$ 的实际 $\nu$ 的 annihilator 是 $(\upsilon,\xi^2)$，$p=7$ 是 $(\xi,\upsilon)$。
$p\ge11$ 时指数至少三，因此 $\nu=0$。对所有 $p\ge5$，在 $X_{\rm sm}$ 上 $\nu=0$；正规化拉回为零亦与此一致。
D 146–148 的核层警告成立：在 $p\ge11$，$d_A(r^p)=0$ 但 $r^p\notin A^p$，否则函数域中唯一的 $p$ 次根 $r$ 属于 $A$。
这说明非零 $\kappa_J$ 不能经光滑核层序列机械推出奇异曲线上的非零 $\nu$；D 没有作该错误推理。

## 8. Proof check：步骤 6，原局部环中的 $\pi$ 非包含

在光滑几何点 $P\in X$，原剩余曲面光滑，完整概形纤维在 $P$ 光滑，故相对 Jacobian 判据给 $dJ\ne0$。
将某个原局部提升 $j$ 的 $dj$ 扩充为余切基 $(dj,\theta)$；这使用 $\Omega^1$ 的局部自由性，不要求整条纤维光滑。
[S6] 295–300 的整数恒等式是先于光滑论证的精确原式，故在原局部环 $R=\mathcal O_{\mathcal U,P}$ 有
$$\alpha=A_0dj+\pi B_0\theta,\qquad A_0=\widehat H(j)+\pi A_1.$$
$H(h)=0$ 使 $A_0\in\mathfrak m_R$；$\theta|_X$ 是光滑曲线局部余切基，$d(\bar G|_X)=0$ 使 $B_0\in\mathfrak m_R$。
更具体地，任取 $h$ 的底环提升 $\widetilde h$，$B_0$ 在局部纤维环 $R/(\pi,j-\widetilde h)$ 中为零；无需只凭某条状态赋值猜出其非单位性。
$R/\pi R$ 是原剩余曲面的局部整环，且 $\bar A_0=H_p(T,J;\varepsilon)$ 非零：$H_p$ 首一非零、$J-h$ 为局部参数，不能在该整环中满足此常系数多项式恒等式。
假设 $\pi=r_0A_0+s_0\pi B_0$，约化后由整性得 $\bar r_0=0$，即 $r_0=\pi r_1$。
原 $R$ 对 $\pi$ 无挠，除去 $\pi$ 得 $1=r_1A_0+s_0B_0\in\mathfrak m_R$，矛盾。
故 $\pi\notin\mathfrak c(\alpha)_P$；此消去不假设 Hasse 根简单，也不删去末端线上属于 $X_{\rm sm}$ 的点。
这是原完整理想非包含，不只是模平方的点值；反过来它仍未确定完整理想、状态精确阶或尖点处的理想。

## 9. Corrections or Missing Assumptions；Open Risks

必要修订：无。新增科学假设：无。六步全部原量词保持；未发现需要作者补大段证明的硬缺口。
仅有非阻断记号建议：D 105 的右端已在 107 明说是一维类空间，若未来转写可直接写 $k\cdot[r]$，避免视觉上与多项式环 $k[r]$ 混同；不影响本次判断。
本件接受的是代数闭剩余域上的几何命题及文中允许的完美扩域表述，不额外声称每个未扩域底场上存在同一正规化坐标／有理选点。
仍开放的原尖点完整理想、光滑部分厚度、参数变形及自然塔关系不由本诊断补齐；本报告不判断它们能否产生独立论文。
没有联网、检查 D 所列外部文献或授予全球查新结论；那两篇文献也不是本六步证明的必要黑箱。
技能要求的最终一致性检查已针对实际命题、量词、非平滑使用点与边界完成；不启动新正式四门或重审不变的旧数学。

## 10. Actual reading and identities

本人本次实读如下；FULL 包含所列完整证明。局部文件 SHA 绑定整文件字节，不冒称整篇阅读。
前次组合盘点接触不并入本次 FULL 清单。三个 P30 源的实际 SHA 均与接受的 V4 清单相应条目相同；未重扫其余源或构建树。

| ID／实际文件 | 本次阅读范围 | SHA-256 |
|---|---|---|
| [作者诊断 D] | FULL 1–185，两次终态身份核对 | `d65cfa7c4a219b313a2c5b72fc6c215f7feee2a8084bf1d9ee91d99f1535cf28` |
| [DG] | 本轮局部 32–114；前次任务曾 FULL，不在本轮冒称重读全文 | `0bfbde8003d049d80523a2001d410dfa4f38ab2f14838d2dbbe4c1363f7155a7` |
| [S3] | 局部 1–114，含纯 W 完整引理与证明；另同基关键词定位 | `38e52e45513c51e9365d9bd0453776d09351fb1ca48b5d86233581112f95434f` |
| [S5] | 局部 165–246，含正则性及非约化图注入完整命题／证明 | `925b2bedcc8e942fb92797d9080b983f53010de97bc1676053390f8a5fc70ab0` |
| [S6] | FULL 1–397，所有本次新消费者及光滑限制的位置均亲读 | `e5ba6462600b04aee4d42f6d3ef85729ee2b3e7f5e6dfead92e37008d36ce392` |
| [M4] | FULL 1–11；仅比对 S3/S5/S6 的接受源条目 | `f57b18fdd0549183ec4250350158ffa721a82a351c15f3b4b792de51043655a9` |
| [PW] | FULL 1–223，proof-writer 技能 | `6d7b3094711f609814680ded62e19b8dd61801511a7d98b96c033894c939babe` |

[作者诊断 D]: PAPER31_QPI_CUSPIDAL_TANGENT_DIAGNOSTIC_V1_20260909.md
[DG]: PAPER30_QPI_DYNAMICS_GEOMETRY_DISPOSITION_V1_20260908.md
[S3]: ../../papers/30-qpi-vertical-critical-ideals/paper/v4/sections/03-spectral-jacobian.tex
[S5]: ../../papers/30-qpi-vertical-critical-ideals/paper/v4/sections/05-integral-trace.tex
[S6]: ../../papers/30-qpi-vertical-critical-ideals/paper/v4/sections/06-first-layer.tex
[M4]: ../../papers/30-qpi-vertical-critical-ideals/notes/SOURCE_V4_20260909.sha256
[PW]: /root/autodl-tmp/.codex/skills/proof-writer/SKILL.md

## 11. 终态

只新增本报告；未改作者稿、组合基线或任何已接受／冻结对象，未运行实验或编译，未外传。
报告提交前本人全文自读，核对直接链接和以上七个输入 SHA；最终报告 SHA 在交付消息单独给出。提交后停写。
