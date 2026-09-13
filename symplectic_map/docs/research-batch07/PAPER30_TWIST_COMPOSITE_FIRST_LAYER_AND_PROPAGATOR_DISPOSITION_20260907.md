# Paper30：合数分母首层结构与真实传播子保根分类

日期：2026-09-07。
状态：TWIST_COMPOSITE_FIRST_LAYER_AND_PROPAGATOR_CLASSIFICATION_ACCEPTED_GLOBAL_ROOTS_OPEN。

接续用户“继续”，本轮只推进上轮保留的实际全实根和合数分母义务。
三个新作者稿均已完成；两倍素数18项、素数幂内部结构15项、
传播子分类16项非作者核查全部通过，主控已全文读取作者稿与三份独审。
本处置按以下准确范围接受新结论，不将首层结果写成完整合数分类。
原模型、固定参数、SUM action 与批次验收要求未改变。

## 1. 本轮对象不能混同

仍研究

$$p'=p+\epsilon\sin q+2\lambda\epsilon^2\sin2q,\qquad q'=q+p',$$

首项 $C_{r,s}(\lambda)$ 和次项 $Q_{r,s}(\lambda)$ 沿用已接受的物理规范。
对奇素数分母，首项全部简单且 $\gcd(C,Q)=1$ 的
[完整结论](PAPER30_TWIST_PRIME_COMPLETE_NONVANISHING_DISPOSITION_20260907.md)
保持接受，不再重审。

| 本轮对象 | 实际得到的结论 | 不能替代的原问题 |
| --- | --- | --- |
| 完整首项 $C_{r,2p}$ | 一个明确的局部首层约化、简单外部因子和唯一剩余根簇 | 尚不是全部根简单或 $C,Q$ 互素 |
| $s=p^a$ 的第一个内部 forcing $\mathcal B_{p\mid s}$ | 单边 Newton 多边形、平方自由性、明确局部因子次数和内部极点 | 不是完整首项 $C_{r,p^a}$ |
| 形式变量 $t$ 上的真实正弦传播子 $T^\pm$ | 全部分母、分子的有限保实根完整分类 | 不是参数 $\lambda$ 上的 $C_{r,s}$ 根分类 |

## 2. 两倍奇素数：分离一半以上的简单根

[偶数分母作者证明](PAPER30_TWIST_EVEN_DENOMINATOR_STRUCTURE_PROBE_V1_20260907.md)
先对全部偶数 $s=2M$ 给出精确半阶消元式。
若 $P=\sum_{n<M}v_nt^n$、
$T_M=[t^{M-1}]e^P/2+\lambda[t^{M-2}]e^{2P}$，则

$$C_{r,2M}=-2M[t^{2M-1}]e^P
-2M\lambda[t^{2M-2}]e^{2P}+\frac{2M}{D_M}T_M^2,
\qquad D_M=4.$$

高半部消去，但两个指数系数和中央平方项都必须保留。
这里的低阶传播子不等于分母 $M$ 的传播子，不能称为低分母首项的平方递推。

对每个奇素数 $p$、每个 $\gcd(r,2p)=1$，令

$$h=D_2,\qquad m=(p-1)/2,\qquad \kappa=\lambda-1/16.$$

注意本节 $h=D_2$，不是奇素数稿的 $D_1$。
在完成实分圆局部整数环 $\mathcal O^+=\mathbb Z_p[h]$ 中，已证明并接受

$$\boxed{\frac{h^{p-1}}pC_{r,2p}\in\mathcal O^+[\lambda],\qquad
\overline{\frac{h^{p-1}}pC_{r,2p}}
=2\kappa^m\left(\kappa^{m+1}+\frac18\right).} \tag{1}$$

式 (1) 保持次数 $p$。非零剩余根全部简单，所以至少
$(p+1)/2$ 个特征零根已证明为单根；其余 $(p-1)/2$ 个根按重数计
满足延拓赋值 $v_h(\lambda-1/16)>0$。这指代数闭包中的零剩余类，
不额外声称在可能的分歧扩域中赋值至少为 $1$。于是

$$\boxed{\deg\gcd(C_{r,2p},C'_{r,2p})\le\frac{p-3}{2}.} \tag{2}$$

这些是代数根和局部剩余类的陈述，不是实根坐标。
对于外部剩余根 $\alpha^{(p+1)/2}=-1/8$，
$\alpha^p=1/(64\alpha)$，所以全部位于 $\mathbb F_{p^2}$；
对应外部因子在完成局部域上的不可约因子次数只有 $1$ 或 $2$。
原全局数域上的因子次数不由此自动确定。

证明的关键新问题是跨过 $p!$ 的指数项。
低于半阶的分支本身整，并不允许删除高阶指数中的这一层；
它精确产生 $\kappa^m/4$，排除了只剩 $2\kappa^p$ 的错误聚簇猜测。
该失败猜测与修正机制均在作者稿保留。

## 3. 奇素数幂：定位第一个内部共振

[素数幂作者证明](PAPER30_TWIST_PRIME_POWER_LOCAL_STRUCTURE_PROBE_V1_20260907.md)
适用于每个奇素数 $p$、每个 $a\ge2$、每个本原 $s=p^a$ 次单位根。
本节改用 $h=D_1$、$\rho=-h$、$L=\rho\lambda$、$m=(p-1)/2$。
真实阶数 $s$ 的低阶分支定义内部多项式

$$\mathcal B_{p\mid s}(\lambda)=-E_{p-1}-2\lambda F_{p-2},\qquad
\mathcal B(h,L)=\rho^{p-1}\mathcal B_{p\mid s}(L/\rho).$$

第 $p$ 模态在这个系统中不是真正共振，因此不能把 $v_p$ 设为零。
已证明并接受

$$\boxed{h^{-m}\mathcal B(h,L)\in\mathcal O^+[L],\qquad
\overline{h^{-m}\mathcal B}=(-1)^{m+1}(2-L^m).} \tag{3}$$

这给内部多项式的单边 Newton 多边形、全部简单根及
所有根的 $v_h(\lambda)=-1$。
若 $f=\operatorname{ord}_{\mathbb F_p^\times}(4)$，其完成局部域上的因子
恰有 $m/f$ 个，每个次数 $f$。理由是剩余根满足
$\alpha^p=4\alpha$，再对互素因子作 Hensel 提升。
特别对 $p\ge5$，该内部多项式在 $\mathbb Q_p(h)$ 中没有根。

同一证明还给出实际内部系数

$$\boxed{\overline{h^mV_p}(L)=\frac{(-1)^m}{2}(2-L^m),
\qquad V_p=\rho^p v_p(L/\rho).} \tag{4}$$

对 $p\ge5$ 的所有 $L\in\mathcal O^+$，$V_p$ 的极点阶恰为 $m$。
这解释了原素数整分支为何不能直接递推至 $p^a-1$。
式 (3) 的常数是 $2$，不是奇素数闭合公式中的 $1$：
此时 $p$ 的 $h$ 赋值为 $p^{a-1}m$，原来的常数层被推到更高阶；
有限作用量的非驻值反射缺陷必须保留。

上述每条根结论都只属于内部 $\mathcal B_{p\mid s}$，
没有证明完整 $C_{r,p^a}$ 的 Newton 多边形、简单性或次项非零性。

## 4. 全实根方向：完成算子分类，明确非线性缺口

[真实传播子作者证明](PAPER30_TWIST_REAL_ROOT_STRUCTURE_NEXT_PROBE_V1_20260907.md)
在 $N=s-2$、$T^\pm(t^k)=D_{k+1}^{\pm1}t^k$ 的完整空间
$\mathbb R_N[t]$ 上证明

$$\boxed{T^+\text{ 保实根}\iff r\equiv\pm1\pmod s,}$$
$$\boxed{T^-\text{ 保实根}\iff s=3
\ \text{或}\ (s=5,\ r\equiv\pm2\pmod5).} \tag{5}$$

同样的分类对全非正实根输入成立；零根、重复根、常数与次数边界均已处理。
失败情形还可以取严格负的简单输入根，不依赖根扫描。
关键是实际三角身份
$D_{n-1}D_{n+1}=(D_n-D_1)^2$，使正、逆方向的二次判别式符号相反。
正向充分性来自正弦乘子的辐角计数；五分母逆向例外有完整三次稳定符号。

有限线性保根准则属于经典工具，已按
[本轮定点来源检查](PAPER30_TWIST_PROPAGATOR_PRESERVER_PRIOR_20260907.md)扣除。
本轮未完成该具体应用或整体研究的全球新意排除。
式 (5) 不反驳 $C_{r,s}(\lambda)$ 全实根猜想：它作用于相位变量 $t$，
而真实 forcing 是受限的非线性像，尚未证明一个能在该递推下保持的保根类。

## 5. 新核查与证据状态

- 传播子完整分类：[16项非作者独审](PAPER30_TWIST_REAL_PROPAGATOR_CLASSIFICATION_INDEPENDENT_CHECK_20260907.md)
  已全部通过，主控全文读取；无作者修订要求。
- 两倍素数首层及半阶消元：[18项非作者独审](PAPER30_TWIST_EVEN_DENOMINATOR_STRUCTURE_INDEPENDENT_CHECK_20260907.md)
  已全部通过，主控全文读取；根簇按正延拓赋值解释，无待修复项。
- 素数幂内部多项式及极点：[15项非作者独审](PAPER30_TWIST_PRIME_POWER_LOCAL_STRUCTURE_INDEPENDENT_CHECK_20260907.md)
  已全部通过，主控全文读取；无作者修订要求。

作者稿含主控协作的有限分类补充及局部 Frobenius 推论；
由未参与对应作者稿的另一代理核查，不以主控交叉计算充当独立认证。
本轮只检查新恒等式；已有六分母输入只用于新约化式的定点一致性，
没有新增素数／分母根列表，没有重跑旧63／6例诊断或未变的接受证明。

## 6. 下一项准确缺口

1. $s=2p$ 的 $v_h(\lambda-1/16)>0$ 根簇：先求实际下一条 Newton 边，
   不预设它只是重根，也不预设任意选定的平移尺度足够分开全部根。
   次项 $Q$ 的共同根排除仍需另外证明。
2. $s=p^a$ 的后续内部层：保留非整 $V_p$、阶乘与其他同阶模态，
   建立合法的分层消元；不能把一个内部多项式当成全系统结果。
3. 全部实根：需要作用于参数根的真正非线性保根结构，
   不能重复无条件逆传播子、辅助平方传播子或旧路径／Hermitian 捷径。

没有正文估页、正式候选票、试写测页、立项、PDF、Route评价或对外操作。
Paper30 未立项，Paper31 未开展，Batch07 仍为3/5；
22–30页实质正文、完整证明与独立验收要求保持不变。

## 7. 新输入身份

| 新输入 | SHA256 |
| --- | --- |
| 两倍素数与半阶消元 | 2fc421fe37d923c5b87bcd76fcafd9ba160dacd6c7951139d1226036e7b9967a |
| 素数幂首层内部多项式 | f9dd643975ecbdb08a1512aacbebb692b96e84fceb8ab66fd69baecbbba6b616 |
| 真实传播子有限分类 | 511b71912bbe553ed9d3b7095efbc1826ce7956b312cfdf4e1a3c8ba6a79cc99 |
| 两倍素数18项独审 | a69a06d417dfc7379da4e353df1065c356a313077a78ef154e7f633122e8a5a2 |
| 素数幂15项独审 | 9fa0a3ff664cdbd68497354d71694606b6475c91fbebe3326514943f5b5ed01e |
| 传播子16项独审 | 56fccc0654b6283a8f9488daa7a295b593e9f50ef768c8158ee8d70f60d4c5e7 |
| 有限保根工具定点来源检查 | 7eed4ff44e174d98cd0d7526fc8bd0d0c19adbd678ed8f6865a1c4fd48d61b6d |
