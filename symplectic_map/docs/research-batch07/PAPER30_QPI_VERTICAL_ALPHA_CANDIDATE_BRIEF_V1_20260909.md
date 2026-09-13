# Paper30 qPI Vertical Alpha V1：首层垂直临界理想与全素数首 jet

日期：2026-09-09。组织者：主控 `/root`。
类型：新垂直理想问题的首次完整候选简报；不是论文稿、准入或产物锁。
状态：`COMPLETE_BRIEF_FROZEN`；两项同对象复用已获数学合取，尚无正式四门票或准入。
拟题：*Vertical critical ideals and cyclotomic first jets of q-Painlevé I*。
`route_applicability: NOT_APPLICABLE`；纯证明、本地效力，Batch07 仍3/5。

## 1. 中心问题与准确的新旧差别

原根单位积分在坏素数约化后成为幂，先除后约化的状态微分满足已知剩余式
$\bar\alpha=H^\sigma dJ$。该式在超奇异能级上为零，却没有决定
原微分的另一个状态方向、首切向类、完整临界理想或沿闭点提升的准确阶。
本件要确定的是这些缺失的垂直信息：首层完整理想，以及全部高层的完整首 jet。

整个问题由 V1–V3 组成，不按素数或推论拆篇。
V1 的实际箭头把原 $L_m$ 提升障碍、原矩阵迹同余与原完整能级上的 Cartier 类连接；
V2 给全部奇素数的首 jet 乘数；V3 给特征二不同基准和真实混合项。
首层完整理想与高层截断理想不混同，所有高层全厚度仍未解决。

[来源预审](PAPER30_QPI_VERTICAL_ALPHA_PREFLIGHT_DISPOSITION_V1_20260909.md)为
7.2/10、PROCEED_WITH_CAUTION，V1–V3 均 method LOW／finding MEDIUM，V1 为概念中心。
主控不自评新意、不把7.2进位，也不将数学正确性换算成独立新意。
准备本简报只表明完整问题值得受约束地接受判断，不是任何一门通过。

旧整数 C1–C3 两票新意7.3 FAIL、旧 qPI T1–T7 完整 V2 双份 FAIL 及此前失败全部保留。
本件不是同一旧包重抽票，也不继承它们的有利分项。
旧通用上同调、谱模和完整模型等在此仅是实际必要的基础；不重复宣传为新发现。

## 2. 原对象与唯一规范

### 2.1 八中心及开放模型

在 $R=\mathbb Z[q^{\pm1},\tau^{\pm1}]$ 上，原曲面是
$\mathbb P^1_R\times\mathbb P^1_R$ 的同一八截面顺序吹起。

| 簇 | 原中心次序 | 最后局部图 |
|---|---|---|
| 1 | $(x^{-1},y-1)=(0,0)$ | $x=u^{-1},\ y=1+uv$ |
| 2 | $(x,y^{-1})=(0,0)$，随后 $xy=\tau$ | $x=u(\tau+uv),\ y=u^{-1}$ |
| 3 | $(x,y)=(0,0)$，第一次例外与 $y=0$ 的交点，随后 $x^2/y=\tau$ | $x=u(\tau+uv),\ y=u^2(\tau+uv)$ |
| 4 | $(x^{-1},y^{-1})=(0,0)$，随后 $y/x=q$ | $x=[u(q+uv)]^{-1},\ y=u^{-1}$ |

总次数为 $1+2+3+2=8$。也可按已证明的相同构造，先吹起四个节点，
再在四个不同边界分量的单位坐标 $1,\tau,\tau,q$ 处吹起。
参数相等不合并不同分量上的中心。
反典范边界 $D=-K_{S/R}$ 是八环，$D^2=0$，$L_n=\mathcal O_S(nD)$。
$\mathcal U=S\setminus D$ 包括原环面及四条完整末端仿射线；末端线不得删掉。

### 2.2 原矩阵、积分与微分

固定辅助规范 $w=1$，记
$b=x(y-1)$、$d_0=y-1$、$J_1(t)=y-x+x/y-t/x$，原矩阵准确为
$$A(z;t)=
\begin{pmatrix}t-b&-x\\d_0(b-t)&b\end{pmatrix}
+z\begin{pmatrix}J_1(t)-1&1\\J_1(t)+b-1&1\end{pmatrix}
+z^2E,\qquad E=\begin{pmatrix}1&0\\0&0\end{pmatrix}.$$
其行列式为 $z^3$。始终用降序乘积
$$M_{r,s}(z)=A(s^{r-1}z;t)\cdots A(z;t),\qquad
I_{r,s}=[z^r]\operatorname{tr}M_{r,s}(z).$$
在 $s$ 精确阶为 $r$ 时，原恒等式为
$$\operatorname{tr}M_{r,s}=t^r+I_{r,s}z^r+z^{2r},\qquad
\det M_{r,s}=(-1)^{r+1}z^{3r}.$$
这些原矩阵、原积分、原谱恒等式及 Laurent 首项均为既有输入，不计新意。
不换成仅特征多项式相同的矩阵，不重标定能级或时间。

### 2.3 圆分参数与基变换边界

令 $p$ 为素数、$m\ge1$ 且 $p\nmid m$，$a\ge1$、$N=p^a$。
取无分歧 $p$-进 DVR $\mathcal O_0$，含精确 $m$ 阶根 $\widetilde\eta$，置
$$\mathcal O_a=\mathcal O_0[\zeta_{p^a}],\quad
\pi_a=\zeta_{p^a}-1,\quad s_a=\widetilde\eta\zeta_{p^a},\quad
t_a\in\mathcal O_a^\times.$$
在原 $q=s_a,\tau=t_a$ 的开放模型上，先于特征零中作除法，定义
$$\alpha_{mN}=p^{-a}d_{\rm state}I_{mN,s_a}.$$
微分只取原两个状态方向，固定时间、单位根与底环。
既有 D/G 已证明该一形式在完整 $\mathcal U_a$ 上正则。

首层 V1 的剩余域允许完美域；高层几何理想与奇素数 TB 使用有限剩余域。
P2 块恒等式本身允许完美剩余域，PI 几何接口仍用其有限剩余域范围。
允许完成、有限无分歧扩张及按各作者实际论证返回未完成圆分局部 DVR；
不合并成未经证明的更大量词，不允许额外分歧状态来替代原状态问题。

在同一剩余小阶模型上，令
$$\eta=\bar s_a,\quad J=I_{m,\eta}(x,y;\bar t_a),\quad
T=\bar t_a^m,\quad\varepsilon_m=(-1)^{m+1},\quad\sigma=(N-1)/(p-1).$$
原 Hasse 多项式为
$$H_p(T,h;\varepsilon)=
\begin{cases}
[Z^{p-1}]\big((T+hZ+Z^2)^2-4\varepsilon Z^3\big)^{(p-1)/2},&p\ne2,\\
h,&p=2,
\end{cases}\qquad H=H_p(T,J;\varepsilon_m).$$
它关于 $h$ 首一、次数 $p-1$；不假定根简单。
$\mathfrak c(\alpha)$ 是秩二相对余切模中全部系数生成的理想，与局部标架无关。

## 3. 完整科学合同 V1–V3

### V1. 所有首层的原完整理想及实际障碍类

对全部 $p,m$、$a=1$，在原每条完整光滑有限概形纤维 $X=(J=h)$ 的每一点 $P$，
包括四条末端线，有
$$\mathfrak c(\alpha_{mp})_P=(\pi_1,\widetilde H)_P.\tag{V1a}$$
$\widetilde H$ 为 $H$ 的任意局部提升。这是原完整理想，不只是加 $(\pi_1^2)$ 后的等式。
若 $h$ 是 $H_p$ 的 $e_h$ 重根，取 $\bar z=J-h$，完成式准确为 $(\pi_1,z^{e_h})$。

在每条完整光滑有限层，原 $L_m$ 的实际 Bockstein 及实际限制同构均给
$$0\ne\kappa_J=\rho_X\beta_{L_m}(J)\in H^1(X,\mathcal O_X).\tag{V1b}$$
进一步在 $H_p(T,h;\varepsilon_m)=0$ 的光滑层，由原迹构造的首切向类满足
$$\partial\nu=\operatorname{Fr}_*\kappa_J\ne0\quad\text{in }H^1(X,\mathcal O_X^p).\tag{V1c}$$
$\beta_{L_m}$ 来自同一 $\mathcal O_1/(\pi_1^2)$ 厚化，保留真实常数项；
边界斜率为 $1-s_1^m\equiv-m\pi_1$。
$\rho_X$ 用原 $1$ 平凡化 $L_m|_X$，$\nu$ 是原迹 $p\pi_1$ 同余给出的首切向类。
到像层 $\mathcal O_X^p$ 的 $\operatorname{Fr}_*$ 不等于再映入 $H^1(\mathcal O_X)$ 后的 Frobenius 算子。
这两条实际箭头不能被任意一维空间同构或未知非零标量替换。

无分歧超奇异与普通状态提升的 $\alpha_{mp}$ 公共阶分别准确为1与0；
未整除 $dI_{mp}$ 的公共阶分别准确为 $p$ 与 $p-1$。

### V2. 奇素数的完整首 jet 因子分解及准确截断理想

对全部奇 $p,a\ge2,p\nmid m$，匹配二阶商及实际时间 jet 后，整个原开放模型上
$$\alpha_{mp^a}^{[2]}=H^{\langle\sigma-1\rangle}\alpha_{mp}^{[2]}.\tag{V2a}$$
两个二阶商通过 $\pi_1\mapsto\pi_a$ 识别为 $k[\epsilon]/(\epsilon^2)$；
它不是自然圆分根嵌入。$p\mid(\sigma-1)$ 使任意局部提升的该次幂粘合为显示全局乘数。
该完整一形式恒等式保留所有块内非共振变形与实际时间 jet，
本身不要求能级光滑、ordinary 或 Hasse 根简单，且跨全部四末端线成立。

结合 V1，在原完整光滑有限能级附近准确有
$$\mathfrak c(\alpha_{mp^a})+(\pi_a^2)
=(\pi_a^2,\widetilde H^\sigma,\pi_a\widetilde H^{\sigma-1}).\tag{V2b}$$
在重数 $e_h$ 的根处，取 $\bar z=J-h$，完成式为
$(\pi_a^2,z^{e_h\sigma},\pi_a z^{e_h(\sigma-1)})$。
超奇异无分歧状态仅推出整除微分公共阶至少二，不推出准确二或全厚度。

### V3. 特征二的不同基准和实际混合理想

对全部奇 $m$、$p=2,a\ge2,N=2^a$，共同二阶商从 $a=2$ 开始：
通过 $\pi_2\mapsto\pi_a$ 将 $\mathcal O_2/(\pi_2^2)$ 与
$\mathcal O_a/(\pi_a^2)$ 识别为 $B=k[\epsilon]/(\epsilon^2)$，
并选 $t_2$ 与 $t_a$ 在 $B$ 中的完整二阶像相同。于是两个原模型及所比较的形式都在同一 $B$ 上。
这不是自然圆分根嵌入，也不可识别到 $a=1$ 的特征四商。整个原开放模型上有
$$\alpha_{mN}^{[2]}=J^{\langle N-4\rangle}\alpha_{4m}^{[2]}.\tag{V3a}$$
原环面上的四块基准为
$$\alpha_{4m}^{[2]}=(j_*^3+\epsilon T)dj_*+\epsilon J^2\chi_m.\tag{V3b}$$
$j_*$ 是原块迹的实际中间系数；不假定它有全图正则提升。
准确地，$s=\eta(1+\epsilon)$、$t=t_a\bmod\pi_a^2$，原块和剩余块为
$$\mathsf B_s(z)=A(s^{m-1}z;t)\cdots A(z;t),\quad
\mathsf B_0(z)=A(\eta^{m-1}z;\bar t)\cdots A(z;\bar t),\quad
j_*=[z^m]\operatorname{tr}\mathsf B_s(z).$$
环境环面形式不是由切向限制反定义，而是
$$\chi_m=J\,dJ+[z^{2m}]\operatorname{tr}
\bigl(d\mathsf B_0\,z\partial_z\mathsf B_0\bigr).$$
首层特征四的整数比较给 $\chi_m|_{\Omega_X}=\nu$，其中 $X=(J=0)$ 是原完整光滑概形纤维。
PI 用局部全局形式差商、素 Cartier 参数与两次整除把该切向类落实到全部点；
不声称环境 $\chi_m$ 在整个剩余曲面正则。

对任意局部提升 $j,\widetilde T$（后者为常数单位提升），准确截断理想为
$$\mathfrak c(\alpha_{mN})+(\pi_a^2)
=(\pi_a^2,j^{N-1}+\pi_a\widetilde Tj^{N-4},\pi_a j^{N-2}).\tag{V3c}$$
特别 $a=2$ 时为 $(\pi_2^2,j^3+\pi_2\widetilde T,\pi_2j^2)$。
在闭点作允许的无分歧扩张并完成，取 $\bar z=J$，截断商准确为
$$k(P)[[w,z,\epsilon]]/(\epsilon^2,z^3+\epsilon T,\epsilon z^2)
\simeq k(P)[[w,z]]/(z^5),\qquad\pi_2\longmapsto z^3/T.\tag{V3d}$$
$w$ 为沿曲线方向，五是截断商的横向长度，不是闭点总 Artin 长度、原完整临界商长度或平坦性声明。
数字五也可见于单项式商，不能单独计功；有限无分歧扩张取 $c_0^3=T$ 可正规化单位系数，
所以 $T$ 也不是新增形式模量。真实混合项及原底参数作用仍是必须计算的内容。

### 状态阶的合取出口

下表仅沿允许的无分歧光滑超奇异状态，准确值与下界严格区分。

| 分支 | $\alpha$ 公共阶 | 未整除 $dI$ 公共阶 |
|---|---|---|
| 全部 $p,a=1$ | 准确1 | 准确 $p$ |
| 奇 $p,a\ge2$ | 至少2 | 至少 $a\varphi(p^a)+2$ |
| $p=2,a=2$ | 准确1 | 准确5 |
| $p=2,a\ge3$ | 至少2 | 至少 $a2^{a-1}+2$ |

普通光滑状态两列分别准确为0与 $a\varphi(p^a)$。
高层状态阶至少二不表示整个曲面的全局形式被 $\pi_a^2$ 整除。

## 4. 完整必要证明，不以方程同名代替几何身份

[全素数数学处置](PAPER30_QPI_VERTICAL_ALPHA_ALL_PRIME_JET_MATHEMATICS_DISPOSITION_V1_20260909.md)
已按同哈希接受 TH／prime trace／OC／TB／P2／PI 及各自实际非作者报告。
Phase A 的 V3 pending 是冻结快照，已由该处置接续。
[两项同对象改接处置](PAPER30_QPI_VERTICAL_ALPHA_PROOF_REUSE_DISPOSITION_V1_20260909.md)
已全文核准 DB173／SH242 与新非作者284行报告并合取接受；原作者待审字样是冻结快照。
DB 取代该首层 Bockstein 的 U2A 特例供应，SH 取代该光滑闭纤维的 Ffib 前提供应，
各自保留的原常数／节点计算、完整模型与原泛谱链均不删。

必要链包含原矩阵、八中心、极除子／节点单位帧、原完整小阶 pencil 及全特征泛光滑，
原整除微分与完整模型、实际首层连接、原迹同余、OC、两类全块首 jet 和完整局部理想消元。
旧矩阵引理的通用带权交换子，以及旧全局首 jet 的二阶商／提升幂／非约化限制单射必须保留。
不把仅 $m=1$ 的旧数字证明代替新的全 $m$ 支持界，也不反向调用旧配对非消失路线。

“超奇异”必须通过以下完整原对象链解释：

1. Wreuse V2 的两图／端点／任意原域 Step2a 及 W0 纯有限临界代数给谱几何前提。
2. Jspec 的实际谱模、原状态有理逆、不可分次数排除、固定 Picard 差、无核及原域 torsor 下降。
3. Hloc L(a) 的同能级 henselian 点提升、双方相对最小性与指定泛同构双向延伸。
4. 原完整光滑谱曲线指定微分的 Cartier 计算；只将零性质经几何基变换返回原域。

不得只写谱多项式相同、同亏格或未知核同源；不得把几何选点或同构擅自下降。
W 的当前纯临界有限性证明保留，但不把旧实际临界 Artin 长度和乘法特征多项式反灌为新结果。
本题特有必要证明未来全部进入正文，本地报告链接不是正文证明的替代。
具体原稿、实际消费者及同字节接受由[当前证明图](PAPER30_QPI_VERTICAL_ALPHA_CURRENT_PROOF_MAP_V1_20260909.md)定位，
共同清单统一绑定正式两席的完整科学输入；不以本简报摘要代替作者证明全文。

## 5. 来源扣除、组合比较与未解决边界

完整共同输入必须包括新 Phase B、C/D、Portfolio、两份垂直来源差分、旧整除微分来源、
相关原 qPI 来源和旧失败处置；不只给出有利摘要。
已读范围内，Vlasenko 的模 $p$ Hasse 迭代、非ordinary形式群整性，
Dwork／higher Hasse、算术提升障碍／Cartier、Lubin–Tate 的具体特征二高度二提升族均是明确先例。
一般 Bockstein、Čech、Taylor、Cayley–Hamilton、数字分解、局部消元和最小模型是工具，
不能各计一个一般理论创新；限制某个先例的前提不等于排除整个理论。

组合仅在实际实读范围内未见 V1–V3 被直接包含。
P18 的微分／Fitting 基变换、P29 的差分与数字工具、P11 的完整群循环包含均扣除。
未对 Papers1–29 或全球文献逐篇全文排除；系统名不同不是无碰撞证据。
Scholar/S2 六次入口访问失败、旧 Ohyama／GRT11 全文缺口及未穷尽引文图继续披露。
不把数据库失败绕过、无搜索命中或必要段实读写成全球首创证明。

本件明确不含：奇异能级局部理想、额外分歧状态准确阶、高层全厚度／全初始理想、
稳定约化、晶体模同构、通用形式群比较、跨系统族推广或 RH／Route A/B 主张。
旧 N9 有限高阶诊断保持但不单计新发现，不用它替代全称证明。

## 6. 不变的双份完整四门合同

两位全新非作者分别本人读取同一冻结完整包，各自评价全部四门，即使首门失败也继续：

1. 新意0–10，至少7.5，逐项扣除先例并解释准确剩余。
2. 独立科学价值0–10，至少7.5，评价一个完整问题，不以证明数量或投入代替价值。
3. 完整证明信心0–10，至少9，覆盖 V1–V3 及全部实际必要依赖。
4. 匿名英文单栏11pt、letter、四边1 inch、标准行距、必要证明全部正文且参考文献另计时，
   对自然22–30页实质正文给可信 PASS/FAIL。

容量按必要证明块给低／中／高预测与总和，并报告低于22和高于30的风险。
预测不是实测或严格界，不从文件行数、数量、投入推算，不另加 central 必须落窗的规则。
不删量词、末端线或实际 Jacobian／闭 Hasse，不拆篇、缩版、灌水、移必要证明至附录或试写测页。
两位各自四门合取，再取两票合取；不平均、进位或拼接旧票。

research-review 规定的 xhigh 与 ARS 证据锚定、反对意见保真用于执行；
用户既定完整双份数值合同优先于默认五席、期刊或 ML 流程。
GPT-5.4 MCP 当前未配置，若实际用可用 Codex 新上下文须如实披露；
`cross_model_verification: NOT_PERFORMED`、`NOT_CALIBRATED`、`criteria_binding_unavailable`。
彼此新票提交前互不可见；旧失败和预审意见共同可见，不冒称对历史盲审或独立错误分布。

当前没有正式四门票或准入，不建 Paper30、source/publication locks、正文或 PDF。
Paper31 与跨论文统一审查未开展；不投稿、上传、托管、push、对外发信或动用付费外部评审资源。
