# Paper30：固定消失点次项与真实 Jacobi 桥接的本轮处置

日期：2026-09-07。
状态：`TWIST_LOW_DENOM_POST_CANCELLATION_AND_BRIDGE_ACCEPTED_GLOBAL_ROOTS_OPEN`。

本轮接续用户“继续”，在同一双谐波辛映射中完成固定消失点的完整次项算法、
分母 $3,4$ 的真实恢复定理，以及实际约化 Hessian 的精确矩阵接口。
**全分母根／重数分类及全分母固定消失点的次项非消失性仍未解决。**
Paper30 未立项、Paper31 未开展；Batch07 仍为3/5。这是新部分证明已接受，
不是全问题完成、正式候选通过或权限阻塞。

## 1. 同一对象、未改变的科学范围

仍研究固定互素 $0<r<s$、$s\ge3$ 下的

$$p'=p+\epsilon\sin q+2\lambda\epsilon^2\sin2q,\qquad q'=q+p'.$$

采用未除以 $s$ 的总作用量，以及
$q_j=\theta+2\pi rj/s+u_j$、$\sum_j u_j=0$ 的真实解析小解消元。
$\lambda$ 属于预定紧集，所有阈值与余项常数允许依赖固定 $r,s$ 及紧集。
没有分母一致小参数域的主张，也没有把固定 $\lambda$ 改成调谐曲线。

[上轮部分证明及辅助反例](PAPER30_TWIST_ROOT_STRUCTURE_DISPOSITION_20260907.md)
继续保留：首项 $C$ 次数恰为 $\lfloor s/2\rfloor$、系数严格交替，
所有实根因此为正；分母 $3$–$6$ 的实际正实单根已精确证明。
这不等于所有分母的根均实。旧已接受证明和旧 $63$ 例诊断未重开或重跑。

## 2. 新完成：固定首项零点后真正恢复分裂

[250行次项作者证明](PAPER30_TWIST_POST_CANCELLATION_PROBE_V1_20260907.md)
同时保留正负 Fourier 模式，给出完整三角递推及
$Q_{r,s}=-2G_{s+2,s}$ 的总作用量规范。对每个固定分母，严格得到

$$W-\overline W=\epsilon^s C_{r,s}(\lambda)\cos(s\theta)
+\epsilon^{s+2}Q_{r,s}(\lambda)\cos(s\theta)
+O_{C^a}(\epsilon^{\min(s+4,2s)}),$$

其中任意固定有限相位导数阶 $a$ 均可取，
$\deg Q_{r,s}\le\lfloor(s+1)/2\rfloor$。
递推可计算不替代所有消失点处 $Q\ne0$ 的证明；本轮只在下列点完成该义务。

| 分母及固定参数 | 实际首次非恒定项 | 相位余项 |
| --- | --- | --- |
| $s=3,\ \lambda=1/24$ | $-\epsilon^5\cos(3\theta)/576$ | $O_{C^a}(\epsilon^6)$ |
| $s=4,\ \lambda_-=3/8-\sqrt{66}/24$ | $\epsilon^6Q(\lambda_-)\cos(4\theta)$，$Q(\lambda_-)>0$ | $O_{C^a}(\epsilon^8)$ |
| $s=4,\ \lambda_+=3/8+\sqrt{66}/24$ | $\epsilon^6Q(\lambda_+)\cos(4\theta)$，$Q(\lambda_+)<0$ | $O_{C^a}(\epsilon^8)$ |

分母 $3,4$ 的全部互素分子由相同传播子覆盖。准确多项式为

$$Q_{1,3}=\frac{\lambda^2}{2}-\frac\lambda8+\frac1{384},\qquad
Q_{1,4}=-\frac32\lambda^2+\frac14\lambda-\frac{11}{1920}.$$

四分母中 $Q\bmod C=1/30-7\lambda/8$，
$\operatorname{Res}_\lambda(C,Q)=-761/921600\ne0$。
三分母六阶可能含 $\cos(6\theta)$，没有错误跳过该允许谐波。

所以各上述固定参数在充分小非零 $\epsilon$ 下，小 $u$ 分支内恰恢复两条
不同的实际 primitive 周期，代表相位为 $0,\pi/s$。这不排除远处其他轨道。
它们一条双曲、一条线性椭圆，不声称非线性或 KAM 稳定。
三分母还严格得到

$$\operatorname{tr}M-2=\frac3{64}\epsilon^5\cos(3\theta)+O(\epsilon^6),$$

因此 $\epsilon>0$ 时相位 $0$ 双曲、$\pi/3$ 线性椭圆，负参数时交换。
作者代码直接代入总作用量与从共振力积分提取两种方法完全一致；
保存的是精确代数结果，不是浮点根拟合。

## 3. 新完成：实际矩阵接口及两个明确方法边界

[167行 Jacobi–Schur 证明](PAPER30_TWIST_JACOBI_BRIDGE_PROOF_V1_20260907.md)
在真实消元配置上定义循环 Hessian $H$、零均值正交压缩 $B$，证明

$$\det H=\frac{\det B}{s}W'',\qquad
\det B\big|_{\epsilon=0}=s^2,\qquad
[\epsilon^s\cos(s\theta)]\det H=-s^3C_{r,s}(\lambda).$$

第一式对非驻值相位也成立；梯度只需平行常数向量，
与零均值曲线加速度的内积就为零。$B$ 是正交压缩，不是固定端点主子矩阵。
这是变分消元的 Schur 机制在当前规范的精确接口，不计作未知的新谱定理。
$H$ 通过真实位移 $u$ 非线性依赖 $\lambda$，$C$ 又只是 Fourier–Taylor 系数；
所以实对称性仍不能推出 $C$ 关于 $\lambda$ 的全实根性。

[271行真实正弦结构 V2](PAPER30_TWIST_SINE_STRUCTURE_PROBE_V2_20260907.md)
另外严格关闭两条指定捷径：

- 真实 $r/s=1/4$ 的树多项式与直接一步／两步路径多项式，即使允许总体尺度
  和参数乘法重标也不相同；二次系数不变量为 $108/5$ 与 $16$。
- 循环／固定端点 Green 核确有精确公式及正定性，但实际复解析收缩不是
  Hermitian 收缩：纯 Fourier 模满足 $f^TKf=0$、$f^*Kf=s/D_1>0$。

这些是指定身份证明失败，不是实际模型反例，也不排除其他更深保根结构。
不能把它们与旧辅助反例拼成另一篇论文。

## 4. 实际独立核查与六例诊断的证据级别

[次项非作者核查](PAPER30_TWIST_POST_CANCELLATION_INDEPENDENT_CHECK_20260907.md)
11项全部通过。核查者没有参与该作者推导，采用独立的对称相位总作用量消元：
三分母单变量、四分母一／二变量，精确重得 $C,Q$、余式与 resultant。
完整正负递推、解析余项、固定参数真实局部轨道和 Schur–Hill 稳定性接口均被核对。
主控全文读取后要求澄清审查文本中的投影符号及零均值坐标；审查者已修正，
主控定点读回确认。不是作者结论修正，也未重运行已通过且输入未变的代数计算。

[Jacobi及有限身份非作者核查](PAPER30_TWIST_JACOBI_AND_SINE_IDENTITY_INDEPENDENT_CHECK_20260907.md)
7项全部通过。核查者不是两份被审文稿作者；独立构造非驻值且加速度非零的
消元例，又从原三周期方程展开实际 Hessian，得到
$[\epsilon^3]\det H=9/8-27\lambda=-27C_{1,3}$，低阶为零。
主控已全文读取两份完整核查，不以代理摘要或作者自行核算代替非作者检查。
这两份报告均不是正式候选票、Route 评价或 PDF 验收。

[新增六例诊断](PAPER30_TWIST_SINE_TARGETED_DIAGNOSTIC_V2_20260907.md)
仅取 $(1,24),(5,24),(11,24),(1,30),(7,30),(13,30)$。
在 $100$ 与 $180$ 位精度各自重算系数和递归导数符号括区，每种精度得到
$81$ 个正实括区，12次运行无异常标记；归一根差小于 $4.49\times10^{-81}$。
主控读取脚本并定点检查保存结果的范围、计数、端点异号及非认证标志；
没有重跑六例或扩大扫描。
**这些不是有向区间／精确 Sturm 证书，连六例精确全实根性也不据此宣布已证明。**
本轮没有找到值得转入认证的实际反例线索。

## 5. 下一项及保持的边界

仍在原模型中处理两个未关闭的全分母义务：

1. 从真实正弦小除数及完整树递推建立严格保根表示，或给出实际模型的精确反例。
   不重复已否定的直接路径身份、Hermitian 替换或按根拟合 Jacobi 矩阵。
2. 在实际首项零点上证明 $Q\ne0$，或精确识别 $C,Q$ 共同根并继续更高阶。
   有限 $s=3,4$ 非零 resultant 不是全分母共同根排除机制。

已有 Lindstedt 树、线性 Hill 谱隙和 Suris 背景检查继续有效，见
[定点文献检查](PAPER30_TWIST_ROOT_STRUCTURE_PRIOR_20260907.md)；本轮不重做未改变背景，
也不把新公式直接标为全球原创。全球新意仍有待核对边界。
本轮未进行篇幅估计、正式四门票、试写测页或新 Paper30 项目。
22–30页正文及完整证明、独立验收要求不变；旧随机 Hénon、共轭面积、AS和链谱
保持原处置，不重开、不补模块或拼篇。没有新 PDF、Route 评价或任何对外操作。

## 6. 本轮输入身份

| 新产物 | SHA256 |
| --- | --- |
| 次项作者证明 | `342d37697b4a7b564c2a9805251c3dccaefec2cac50a12cfabf1e11a032d88ae` |
| 次项精确脚本 | `5cda0186d39b87d4a067ca2c7bac56b57ed3c7a2171c7b97550f43d52a48bed9` |
| 次项精确结果摘要 | `b9cd4f532f313944fd8df45134e32c4fcab0373049685fa55d8e2935cfbcc92b` |
| 次项非作者核查（记号澄清后） | `153c75c79ce4908b1c262f11efc4e0ba5c8a1b00215eb26a5fc77f77827926de` |
| Jacobi桥接证明 | `0ade8082e78575a9306087b2d8d7b38b980acb424963344a08bd9b58a36d1a52` |
| 真实正弦结构V2 | `47b4ba9b09d37122bfbcaa6f4680d162a054eed2714b002595f3f9b8fa82f3b9` |
| Jacobi及有限身份独立核查 | `9234074ecf8f4a0c4d868b65f379f67b7c30dd606950abde2f6123f734850c99` |
| 六例诊断报告 | `63aff80e651de4dd4fb73751f807c0cf9261022b72bb1be57a502c956c736662` |
| 六例诊断脚本 | `90abb8908ef899471e5051f9c641bc217779ae1084f6b2d6000302d619bcd2db` |
| 六例诊断结果 | `2821ac33217ae378be63f81f05078d95b59062124756de9030ec4e2873a8dd25` |
