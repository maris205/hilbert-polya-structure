# Paper30：单插入、系数变分与循环芽规约的本轮处置

日期：2026-09-07。
状态：`TWIST_SINGLE_INSERTION_VARIATIONAL_GERM_REDUCTIONS_ACCEPTED_GLOBAL_ROOTS_OPEN`。

接续用户“继续”，本轮在原双谐波模型内获得几种精确的全分母系数规约，
并严格否定两条新提出的具体捷径。四份限定核查已经完成，主控全文读取。
**全分母全部根实、根简单及固定首项零点处次项非零，仍是三个未关闭的义务。**
本轮没有把规约、有限身份核算或非作者检查冒称为全问题证明。
Paper30 未立项、Paper31 未开展，Batch07 仍为3/5；这不是权限阻塞。

## 1. 同一实际模型及本轮新系数公式

保持映射
$p'=p+\epsilon\sin q+2\lambda\epsilon^2\sin2q$、$q'=q+p'$，
总作用量不除以 $s$，固定互素 $0<r<s$、$s\ge3$、固定 $\lambda$。
小参数邻域依赖固定分母与预定参数紧集，不作分母一致性或参数调谐替换。

令 $D_n=4\sin^2(\pi rn/s)$。在物理正频变量 $t$ 中，
正支 $v(t)$ 满足

$$v_n=-\frac{E_{n-1}/2+\lambda F_{n-2}}{D_n}\quad(s\nmid n),
\qquad v_{ks}=0,\qquad E=e^v,\quad F=e^{2v}.$$

两个准确的总作用量系数身份为

$$\boxed{C'_{r,s}(\lambda)=-s[t^{s-2}]e^{2v(t)},\qquad
Q_{r,s}(\lambda)=-s[t^{s+1}]e^{-v(t)}.}$$

第一式是对包括消元响应在内的总参数导数，不能冻结 $v$ 后直接求导。
第二式只需正支算到 $s+1$ 阶；$v_s=0$，但 $E_s,F_s$ 及
$[t^s]e^{-v}$ 不必为零。它没有删掉物理负谐波：对独立负幅度求导后，
一次负谐波插入保留在势项中，隐含位移响应因投影驻值而消失。
证明见 [190行单插入作者稿](PAPER30_TWIST_ONE_INSERTION_ENVELOPE_PROOF_V1_20260907.md)
及 [参数导数／系数变分作者稿](PAPER30_TWIST_ROOT_SIMPLICITY_PROBE_V1_20260907.md)。

进一步置 $Y(t)=te^{v(t)}$、$T=Y^{-1}$ 为复合反函数，
$A_k=[y^k]T(y)^{-s}$，则

$$Q=A_1,\qquad C=-\frac{A_{-1}+4\lambda A_{-2}}s.$$

所以 $C=Q=0$ 等价于同一反函数的
$A_{-1}+4\lambda A_{-2}=0$ 与 $A_1=0$。
这是精确系数条件，仍没有证明这些条件不可能同时成立。

## 2. 首项简单性的有限系数变分规约

为表述此节，单独使用正树权规范 $a=-4\lambda$、缩放变量 $\tau=-t/2$，
记相应系数为 $\widehat v,\widehat E,\widehat F$。
临时驱动参数 $b$ 取权重一，$a$ 取权重二；实际取 $b=1$。
有限系数泛函为

$$\Phi_s=[\tau^s]\left(
\frac12\widehat v\mathcal D\widehat v
-b\tau e^{\widehat v}-\frac a2\tau^2e^{2\widehat v}\right).$$

其唯一临界点恰好满足正频三角递推；临界值 $G_s$ 和首项阻碍满足

$$R_s=-sG_s,\qquad R_s'(a)=\frac s2\widehat F_{s-2},\qquad
\gcd(R_s,R_s')=\gcd(\widehat E_{s-1},\widehat F_{s-2}).$$

最后是包括重数的首一 gcd 等式，不只是零点集合相同。
尚未证明右边对全部实际 $r,s$ 恒为 $1$。

此泛函的系数 Hessian $\mathscr H$ 对全部系数与参数恒反三角，满足

$$\det\mathscr H=(-1)^{(s-1)(s-2)/2}\prod_{n=1}^{s-1}D_n,
\qquad\operatorname{inertia}(\mathscr H)
=(\lfloor s/2\rfloor,\lfloor(s-1)/2\rfloor,0).$$

这是非退化鞍点，不是实际相位配置中已知正定的横向 Hessian。
常数非零行列式不能推出临界值关于参数的零点一定简单。
二阶响应 $R_s''=s\beta^T\mathscr H^{-1}\beta$ 也不具有自动正号。

## 3. 真正根单位结构：循环芽的有限射流等价

[287行反函数／循环芽作者稿V3](PAPER30_TWIST_ROOT_PRESERVING_PROBE_V3_20260907.md)
在上述正树规范下，用真实算子
$\mathcal D=2-S_\zeta-S_{\zeta^{-1}}$、$\zeta=e^{2\pi ir/s}$
证明 $R_s(a)=0$ 当且仅当存在复合阶恰为 $s$、线性部为 $\zeta$ 的解析芽
$\mathcal F$，满足

$$\log\frac{\mathcal F(y)\mathcal F^{-1}(y)}{y^2}
=-y-ay^2+O(y^{s+1}).$$

这里 $\mathcal F^{-1}$ 是复合逆，分子是两个函数值的普通乘积。
复合阶是完整恒等式，对数式只要求指定射流；不把它解释为原实映射的可积性。
反向证明用有限群平均线性化，共振规范与旋转交换；
对数到 $y^s$ 所需的芽到 $y^{s+1}$ 阶已经明确处理。

相应 Lagrange 系数式精确成立，但反函数指数不是参数仿射族。
真实五分母的反函数对数 $\widehat w$ 满足

$$[a^2y^4]\widehat w=\frac{2(D_2-D_4)}{D_2^2D_4},$$

两个互素代表的值分别为 $(\sqrt5-1)/5$、$-(\sqrt5+1)/5$。
所以 $\widehat w=\widehat w_0+a\widehat w_1$ 这个具体捷径失败。
它不是实际首项的非实根反例，也不排除其他保根机制。

## 4. 响应、传播子灵敏度及另一条严格方法边界

[共同根响应作者稿V2](PAPER30_TWIST_COMMON_ROOT_PROBE_V2_20260907.md)
以原物理规范的相位 Ward 配对消去响应未知量，得到

$$\mathscr R_s(f)=-[t^s](1+t\partial_t v)f.$$

对最低次数至少为 $-1$ 的源，此公式严格成立；不同源上的非零性仍不能相互推出。
成对传播子变分进一步给出

$$\delta C=-s\sum_{k=1}^{s-1}\delta D_kv_kv_{s-k},\qquad
-s\sum_{k=1}^{s-1}D_kv_kv_{s-k}=(1-s)C+\lambda C'.$$

在简单实根处后一卷积非零，但它不是非负平方和，尚未与 $Q$ 建立非零比例关系。

只为检验一条明确身份，实际六分母精确计算严格否定

$$Q=a_0 C+(b_0\lambda+c_0)C',$$

其中三常数可依赖 $r,s$，但不能依赖 $\lambda$。
系数矩阵秩为三、增广秩为四，四阶行列式为 $76011797/1161216\ne0$。
这也排除模 $C$ 的同类仿射导数闭包，不排除需要另证的更复杂表示。
六分母 $Q$ 由完整正负 Fourier 与单插入两种方法精确吻合；没有求它的根。

## 5. 实际核查、重叠及证据边界

四份限定核查均完成，主控全文读取新作者稿与非作者报告：

- [单插入核查：9项通过](PAPER30_TWIST_ONE_INSERTION_INDEPENDENT_CHECK_20260907.md)。
  非作者独立计算实际六分母正支并直接反演 $Y(T)=y$，验证两条 Laurent 身份。
- [系数变分核查：8项通过](PAPER30_TWIST_COEFFICIENT_VARIATIONAL_INDEPENDENT_CHECK_20260907.md)。
  非作者直接构造四分母新泛函，核对梯度、Hessian、gcd 理想及响应。
- [循环芽核查](PAPER30_TWIST_Q_GERM_INDEPENDENT_CHECK_20260907.md)。
  非作者检查双向证明，并以自由参数和自由共振规范作有限精确射流自验。
- [响应／闭包限定核查：5项通过](PAPER30_TWIST_RESPONSE_CLOSURE_INDEPENDENT_CHECK_20260907.md)。
  主控作为该响应证明与闭包的非作者核查；明确不把主控自己撰写的同一个
  $Q$ envelope 输出公式计为自我“独立认证”。

这些材料的共享留数、参数导数及同一个 $Q$ 不按多份新主结果重复计数。
没有作者结论修正或新根扫描；精确小算例只验证本轮新身份，未重开旧根证明。
旧 $63$ 例及上一轮六例高精度结果未重算，也未改变其非认证标签。

## 6. 接续与项目边界

后续仍须针对真实三角传播子解决：

1. 全部 $C$ 根的实性及数量，而不是从指数式、循环芽可解性或鞍点非退化性直接推断。
2. 精确排除或识别 $\gcd(\widehat E_{s-1},\widehat F_{s-2})$ 的非平凡因子。
3. 在首项零点上排除或识别 $A_1=0$，不能用已失败的三常数导数闭包代替。

此前[低分母固定消失点恢复与真实Jacobi桥接](PAPER30_TWIST_POST_CANCELLATION_AND_BRIDGE_DISPOSITION_20260907.md)
及[首项部分性质](PAPER30_TWIST_ROOT_STRUCTURE_DISPOSITION_20260907.md)继续按原范围接受。
先前背景检索未重开；本轮的规约不自动构成全球新意或新的谱根定理。
没有自然正文估页、正式四门票、试写测页、论文/PDF或 Route 评价。
22–30页正文、完整证明、独立验收及本地效力边界不变；
其他已闭合支线不重开、不补模块或拼篇，五篇目标没有标为完成。

## 7. 本轮新输入身份

| 文件 | SHA256 |
| --- | --- |
| 单插入作者稿 | `8e8d54b4f08c59a444de54308ef0d67794729535fafa9138e60c874869276431` |
| 系数变分作者稿 | `eb332a74bcfed71f2f7d14ab73e5b0851a48eb9bb40e1c9c9b1176c4457e9ede` |
| 响应／闭包作者稿 | `6d2aaeb7a13773730a06e0985b84950f7e54f79dcd1440e0cf9a8f4be44b4b22` |
| 反函数／循环芽V3 | `d2901b6c419635673813e62cf6702dae91e86258d9823c09f8db6e678291f167` |
| 单插入独立核查 | `a5707c83dad0c83db713e813a9a524a28d894ef2af5b606040f52db0807b4582` |
| 系数变分独立核查 | `182dad0b1954a30eb11e19bc8d7a9bb52b90add30eef77c6ea39f47bfa39877f` |
| 循环芽独立核查 | `859074c4df8241d0d374b35119b555f6a09bc9316fbcd49122b9aa2424d7f2bc` |
| 响应／闭包限定核查 | `0f220f05ac00fd681d7f87e7d839c35baf3fec1324b68abc45dfaf032d0507bc` |
