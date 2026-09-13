# Paper31 discovery：高度二完整模型的直接消元推论 V1

日期：2026-09-09。作者：`/root`。
状态：`PROVABLE AS STATED`（作者证明，待非作者核查）；不是独立论文准入。
本件接上另一席发现的两生成元消元与 Paper30 已接受的全模型形式级接口。
不改 Paper30 原稿的保守截断声明，不将后来的推论追记为原验收时已声称。

## Claim、Assumptions 与 Notation

保留 Paper30 特征二几何定理的全部假设：$m$ 奇数、$a=2$、有限剩余域 $k$，
原圆分环 $\mathcal O_2=\mathcal O_0[\zeta_4]$、$\pi=\zeta_4-1$、原 $s=\widetilde\eta\zeta_4$、任意允许单位时间提升。
在原八中心完整开放曲面上，$\alpha_{4m}=4^{-1}d_{\rm state}I_{4m,s}$，
$J=I_{m,\eta}(x,y;\bar t)$、$T=\bar t^m\ne0$。
对每个原完整光滑有限纤维的每个点 $P$，包括四条末端线上这些点，准确有

$$\mathfrak c(\alpha_{4m})_P=(\pi^2,j^3+\pi\widetilde T,\pi j^2)_P.$$

右端 $j$ 是任意原局部 $J$ 的提升，$\widetilde T$ 是任意常数单位提升。
这是原完整理想，不再需要在左边另外加 $(\pi^2)$。
在 $X=(J=0)$ 的闭点，经允许无分歧扩张及完成，完整商为

$$\widehat R/\mathfrak c(\alpha_{4m})
\simeq k(P)[[w,z]]/(z^5),\qquad \pi\longmapsto z^3/T.$$

所以完整局部商的横向长度是五，$\pi\ne0$ 而 $\pi^2=0$；仍不是闭点总 Artin 长度。
不扩到高度至少三、奇素数、奇异完整能级或额外分歧状态的精确阶。

## Proof Strategy 与 Dependency Map

输入一：[P30 V4 §5](../../papers/30-qpi-vertical-critical-ideals/paper/v4/sections/05-integral-trace.tex)，
原一形式在整个原开放模型的正则性及原相对余切模的局部自由性。
输入二：[P30 V4 §8](../../papers/30-qpi-vertical-critical-ideals/paper/v4/sections/08-two-jets.tex)，
每个完整光滑 $J=0$ 点的实际截断形式与单位切向系数，特别是 411–532 行。
输入三：[高度二 torus 诊断](PAPER31_QPI_HEIGHT_TWO_DIAGNOSTIC_V1_20260909.md) Step 4 的初等消元；
本件在下文重给整个引理证明，不以其仅 $m=1$ 的原矩阵计算代替全模型输入二。
输入四：P30 §8 的完成坐标论证只在取得本件新 $\pi^2$ 包含之后使用。

证明顺序：已接受实际截断形式 → 提升局部余切基和可逆行变换 → 原两系数 → 单位消元 → 完整商。

## Proof

### 1. 在每个原点提升实际形式级接口

先设 $J(P)=0$，令 $R=\mathcal O_{\mathcal U_2,P}$，$\bar R_2=R/(\pi^2)$。
由 P30 §8 的每点除法引理及实际切向类，存在 $\bar R_2$ 上局部基 $(dj,\theta)$ 和元素 $A,B$，$B$ 为单位，使

$$\alpha_{4m}\bmod\pi^2
=(j^3+\pi\widetilde T+\pi j^2 A)dj+\pi j^2B\theta.$$

这是已接受的完整形式级等式，不是仅知道一个抽象理想的两生成元。
原余切模为自由秩二模，可把 $j,\theta,A,B$ 提升到 $R$。
所提升基的行列式模极大理想非零，因而仍是原余切基；所提升 $B$ 仍为单位。
记原 $\alpha_{4m}$ 在此基中的准确两系数为 $f,g$，并令

$$G=B^{-1}g,\qquad F=f-AG.$$

这个行变换的行列式为 $B^{-1}$，在原 $R$ 中可逆，因此 $(F,G)=(f,g)$。
实际截断式直接给某些 $a,b\in R$ 使

$$F=j^3+\pi\widetilde T+\pi^2a,\qquad G=\pi j^2+\pi^2b.$$

整个提升只使用局部商映射满射和单位提升；不要求把剩余谱曲线同构提升成混合特征曲面同构。
原输入二已逐个包含四末端点，本步骤没有额外反演终端坐标或将环面稠密性当作非约化相等。

### 2. 原局部环的精确消元

因为 $\pi,j\in\mathfrak m_R$ 且 $\widetilde T$ 是单位，

$$\pi F-jG=\pi^2(\widetilde T+\pi a-jb),\qquad
\widetilde T+\pi a-jb\in R^\times.$$

所以 $\pi^2\in(F,G)$。减去 $F,G$ 的两个 $\pi^2$ 余项后得
$(F,G)=(\pi^2,j^3+\pi\widetilde T,\pi j^2)$，两个方向的包含均由这些明确等式给出。
这条局部引理本身不需任何正则性；正则性只在前一步确保原正确的两系数与框架。
改变 $j$ 为 $j+\pi c$ 时，模 $(\pi^2)$ 的立方差为 $3\pi j^2c$，已在第二生成元中；
改变 $\widetilde T$ 为另一个提升仅加 $(\pi^2)$ 项。因此任意提升的声明成立。
若所选完整光滑纤维满足 $J(P)\ne0$，原剩余式 $\bar\alpha_{4m}=J^3dJ$ 在该点有单位系数。
故原系数理想是单位理想，所列右端也有单位 $j^3+\pi\widetilde T$；这包括其余全部光滑有限层。

### 3. 在新包含已证明之后求完整商

在 $X=(J=0)$ 的闭点，以 $z$ 提升 $J$，$w$ 为沿曲线的另一参数。
原相对光滑性给局部完成坐标；$\mathcal O_2/(\pi^2)$ 是特征二双数环，故

$$\widehat R/\mathfrak c(\alpha_{4m})
\simeq k(P)[[w,z,\epsilon]]/(\epsilon^2,z^3+\epsilon T,\epsilon z^2).$$

消去 $\epsilon=z^3/T$ 得 $(z^5,z^6)=(z^5)$，从而得到命题中的完整商及原基参数作用。
它是 $k(P)[[w]]$ 上以 $1,z,z^2,z^3,z^4$ 为基的自由模；$z^3/T$ 非零、其平方为零。
正是新步骤 2 使完整商等于旧截断商，并非从旧“横向长度五”一句直接推原完整性。证毕。

## Corrections、Open Risks 与用途

没有必要改变原科学假设或旧源；本件严格消费原有限域／完整光滑纤维范围，不宣布更广完美域版本。
高度二 $\pi^2$ 以上项对原完整理想均已被吸收；因此该窄“完整厚度升级”是直接推论，不足以单独成为第31篇的新问题。
旧首 jet、原特殊基参数作用和完整模型证明仍是关键输入；本引理不是对其工作的替代或新意重评分。
待非作者核查本件的实际框架提升、单位消元和完整商边界；不重开不变的 P30 上游完整证明。
仅新增本地发现记录，未建项目、修改接受稿、编译或产生外部效力。
