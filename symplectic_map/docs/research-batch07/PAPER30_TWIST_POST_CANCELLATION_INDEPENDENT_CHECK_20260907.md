# 固定消失参数次项：非作者独立核查

日期：2026-09-07。审查者：`p30_twist_leading_structure_probe`，未参与被审
$Q$ 次项稿的推导或代码编写。使用本轮完整读取的 `proof-writer` 技能：
独立推导必须支持实际结论，并把有限分母结果与全分母 OPEN 分开。
本次只写本报告，未修改作者文件或任何状态文件。

## Claim and status

审查对象是固定 SUM action 及固定 $\lambda$ 下的完整正负 Fourier 递推、
$Q_{r,s}=-2G_{s+2,s}$、分母 $3,4$ 的精确非消失结果、余项、真实局部
primitive 周期恢复及线性稳定类型。不是全分母根分类或共同根排除定理。

**所述有界命题：`PROVABLE AS STATED`；下表 11 项全部 PASS。**
没有需要作者改动的实质缺口。全分母 $C,Q$ 共同根问题仍 OPEN。

## Inputs and assumptions

已全文读取以下三个实际文件：

| 输入 | SHA256 |
| --- | --- |
| [作者证明](PAPER30_TWIST_POST_CANCELLATION_PROBE_V1_20260907.md) | `342d37697b4a7b564c2a9805251c3dccaefec2cac50a12cfabf1e11a032d88ae` |
| [完整 Fourier 代码](PAPER30_TWIST_POST_CANCELLATION_PROBE_V1_20260907.py) | `5cda0186d39b87d4a067ca2c7bac56b57ed3c7a2171c7b97550f43d52a48bed9` |
| [保存的精确结果](PAPER30_TWIST_POST_CANCELLATION_PROBE_V1_20260907_RESULTS.json) | `b9cd4f532f313944fd8df45134e32c4fcab0373049685fa55d8e2935cfbcc92b` |

固定互素 $0<r<s$、$s\ge3$，参数 $\lambda$ 位于固定紧集；所有小参数阈值
允许依赖固定分母及参数，不作分母一致结论。实际解析零均值消元及其精确
对称性作为已通过、输入未变的前置引理使用，不重新审查旧包。

## Itemized verdicts

| 项目 | 结论 | 独立证据 |
| --- | --- | --- |
| 1. 正负模完整力及投影符号 | PASS | 从原驻值方程乘以 $i$ 重推；共振模式投影掉，不除零 |
| 2. 三角指数递推、支撑与 $Q$ 次数上界 | PASS | 直接指数微分及节点加权计数；负一次谐波不可删 |
| 3. SUM action 到共振力系数 | PASS | 重推 $iW'=\sum G$，得 $B_{n,\ell}=-2G_{n,\ell s}/\ell$ |
| 4. $s=3$ 的 $C,Q$ | PASS | 独立单变量对称作用量消元，而非调用作者 Fourier 实现 |
| 5. $s=3$ 固定零点五阶恢复 | PASS | 精确 $Q(1/24)=-1/576$ |
| 6. $s=4$ 的 $C,Q$ 与共同根排除 | PASS | 独立一／二变量作用量差；余式、resultant 与符号全部吻合 |
| 7. 解析余项的允许阶 | PASS | 一般 $\min(s+4,2s)$；三分母六阶二倍谐波未被错误排除 |
| 8. 恰两个局部 primitive 周期 | PASS | 固定参数、非零小 $\epsilon$、基本相位圆、$C^2$ 控制及互素绕数 |
| 9. Schur 与 Hill 因子 | PASS | 独立分块及 transfer/continuant 核算；$\operatorname{tr}M-2=\det H$ |
| 10. 稳定性标签及三分母 $3/64$ | PASS | $-s^3Q$ 因子及迹符号；仅线性椭圆，未宣称 KAM／长期稳定 |
| 11. 实际运行、JSON 一致性及范围 | PASS | 运行作者精确程序成功，并核对保存摘要；另运行本报告独立实现 |

## Proof strategy and dependency map

核心替代实现不是把作者代码换一种排版：在两个固定对称相位上直接写出
少变量的真实 SUM action，通过有理数／根式隐式 Taylor 消元求其差。
在所需阶数上只有 $\cos(s\theta)$ 这一相位谐波，所以这个差独立确定 $C,Q$。
随后单独核查解析余项、局部轨道与稳定性接口。

1. 解析唯一性和反射对称使实际小解落入下面指定的对称配置子空间。
2. 在该子空间求解正定常数 Hessian 的隐函数方程即给出实际限制分支。
3. 作用量差提取准确的 SUM-action 系数，无力积分规范或 Fourier 卷积共用代码。
4. 系数非零加前置解析余项产生局部动力结论；该步骤独立于代码运行成功。

## Proof and independent checks

### 1. 完整 Fourier 规范

原投影驻值方程是 $Lu+\Pi\{\epsilon\sin q+2\lambda\epsilon^2\sin2q\}=0$，
其中 $\Pi$ 投影到零均值空间；一般相位 $\theta$ 下尚非完整驻值。
这是主控交付读回发现的审查文本记号澄清，不改变下面的完整力定义及非共振反演。
置 $v=iu$、$z=e^{i(\theta+\omega j)}$ 后，乘以 $i$ 的力恰为

$$
G=\frac\epsilon2(ze^v-z^{-1}e^{-v})
 +\lambda\epsilon^2(z^2e^{2v}-z^{-2}e^{-2v}).
$$

因此非共振阶有 $v_{n,m}=-G_{n,m}/D_m$，共振阶 $v_{n,m}=0$。
作者程序的四个指数均保留、移位和正负系数一致。
由 $\partial_\epsilon e^{av}=a(\partial_\epsilon v)e^{av}$ 得到其三角递推。

总加权阶 $n$ 的频率绝对值不超过 $n$，并与 $n$ 同奇偶。
在 $(n,m)=(s+2,s)$ 的完全展开中，各基本标签的 $n-m$ 为 $0,2,4$；
所以恰有一个负一次谐波标签，没有负二次谐波标签，正节点总权重为 $s+1$。
这证明 $\deg Q\le\lfloor(s+1)/2\rfloor$；没有从它推断系数不抵消。

在投影驻值分支，梯度平行常数向量且 $\sum u_\theta=0$，故
$iW'=\sum_jG$。对 $\cos(\ell s\theta)$ 系数 $B$，左边正模为
$-\ell s B/2$，右边为 $sG_{n,\ell s}$。因此

$$
B=-\frac2\ell G_{n,\ell s},\qquad Q=-2G_{s+2,s}.
$$

该转换没有漏乘或多除 $s$。代码中的直接动能核也正确：对共振总模式 $m$，
$(e^{ia\omega}-1)(e^{i(m-a)\omega}-1)=D_a$，而 $u=-iv$ 产生负号。

### 2. 独立三周期作用量消元

在 $\theta=0$，对称配置为
$(q_0,q_1,q_2)=(0,2\pi/3+x,4\pi/3-x)$。
扣去固定 kinetic 常数后的真实作用量为

$$
A_3(x)=3x^2-\epsilon(1-\cos x-\sqrt3\sin x)
-\lambda\epsilon^2(1-\cos2x+\sqrt3\sin2x).
$$

其 $x$ Hessian 在零参数时为 $6$。逐阶解 $A_3'(x)=0$ 到四阶，
代回到五阶。相位 $\pi/3$ 的约化值等于相位 $0$ 在 $-\epsilon$ 的值，
由原作用量的 $q\mapsto q+\pi$ 对称及相位周期性得到。
因此 $A_3$ 消元后的三阶、五阶奇系数就是 SUM-action 的 $C,Q$。
独立计算给出

$$
C_{1,3}=\lambda-\frac1{24},\qquad
Q_{1,3}=\frac{\lambda^2}{2}-\frac\lambda8+\frac1{384}.
$$

固定 $\lambda=1/24$ 后 $Q=-1/576$，精确非零。
另代入作者二阶配置式也吻合 $u=-\epsilon\sin x/3+
\epsilon^2\sin2x/36+O(\epsilon^3)$。

### 3. 独立四周期作用量差

在 $\theta=0$，令 $u=(0,x,0,-x)$，限制作用量为

$$
A_{4,0}(x)=2x^2+2\epsilon\sin x-2\lambda\epsilon^2(1-\cos2x).
$$

在 $\theta=\pi/4$，写
$u=(h+k,h-k,-h+k,-h-k)$，限制作用量为

$$
A_{4,1}(h,k)=4h^2+8k^2+
2\sqrt2\epsilon\sin h(\cos k+\sin k)
+4\lambda\epsilon^2\cos2h\sin2k.
$$

零参数 Hessian 分别为 $4$ 及 $\operatorname{diag}(8,16)$，故可逐阶唯一消元。
解到五阶后取两者消元值之差的一半，其四阶、六阶系数分别是

$$
C_{1,4}=\lambda^2-\frac34\lambda+\frac5{192},\qquad
Q_{1,4}=-\frac32\lambda^2+\frac14\lambda-\frac{11}{1920}.
$$

独立精确代数给出

$$
\gcd(C,Q)=1,\quad Q\bmod C=\frac1{30}-\frac78\lambda,
\quad\operatorname{Res}(C,Q)=-\frac{761}{921600}.
$$

在 $\lambda_\pm=3/8\pm\sqrt{66}/24$ 的值及正负号与作者稿一致。
较小根处的正号确由 $35^2\cdot66-283^2=761>0$ 保证。

### 4. 余项与真实局部周期

首谐波下一未列阶为 $s+4$，二倍谐波最早为 $2s$，故作者的
$O_{C^a}(\epsilon^{\min(s+4,2s)})$ 正确；$s=3$ 必须允许六阶项。
本结论使用固定分母的解析 Taylor 余项，并没有将程序有限截断当误差估计。

固定 $C(\lambda_*)=0,Q(\lambda_*)\ne0$，归一约化势在 $C^2$ 中趋于
$Q\cos(s\theta)$。其导数在两个极值附近由非零二阶导数控制，在补集上
由极限导数离零的正距离排除新零点。偶性和 $2\pi/s$ 周期性把两点准确
固定在 $0,\pi/s$。两个相位类给出两条局部轨道，而不是 $2s$ 条互不等价轨道。
若周期真约数 $t\mid s$，提升绕数条件将迫使 $s/t$ 同时整除 $r,s$，
违背互素性，所以两轨道均为 primitive $s$ 周期。

作者正确限定了小 $u$ 分支、充分小非零 $\epsilon$、固定参数，并未排除远处轨道。

### 5. Schur、Hill 与稳定性因子

以 $e_0=\boldsymbol1/\sqrt s$ 及其正交补写
$H=\left(\begin{smallmatrix}h&b^T\\b&B\end{smallmatrix}\right)$。
投影驻值方程的相位导数在零均值正交坐标中给出
$u_\theta=-\sqrt s B^{-1}b$，故

$$
W''=s(h-b^TB^{-1}b),\qquad\det H=\frac{\det B}{s}W''.
$$

梯度与 $q_{\theta\theta}$ 的额外链式项因 $\sum q_{\theta\theta}=0$ 而消失。
在零参数时 $\det B=\prod_{k=1}^{s-1}D_k=s^2$。

实际映射变分与 $\delta q_{j+1}=a_j\delta q_j-\delta q_{j-1}$ 通过
$p_j=q_j-q_{j-1}$ 的固定线性坐标变换共轭。转移矩阵行列式为 $1$。
作者列出的两条 continuant 恒等式可从最后一行展开递推获得：周期行列式
比转移迹少两个闭环排列的贡献，故对这里的 $s\ge3$

$$\operatorname{tr}M-2=\det H.$$

因此 $W''>0$ 时迹大于 $2$，为双曲；$W''<0$ 时迹小于 $2$ 且随参数
趋于 $2$，所以充分小时仍大于 $-2$，为线性椭圆。
固定消失点后首项迹差的系数为 $-s^3Q$。三分母给出

$$-3^3(-1/576)=3/64,$$

故作者的三分母正负参数类型交换及四分母两根的类型标签都正确。
报告只称线性椭圆，没有越界声称非线性稳定或 KAM 稳定。

## Independent executable check

下面是实际运行过的独立作用量实现。它不导入作者文件，不使用作者的
Fourier 字典／指数递推，不做浮点求根或额外分母计算。

```python
import sympy as S
e, lam = S.symbols("e lambda")
N = 7
def tr(z):
    return S.Add(*[c*e**p[0] for p,c in S.Poly(S.expand(z), e).terms()
                   if p[0] < N])
def sn(z):
    return tr(sum((-1)**j*tr(z**(2*j+1))/S.factorial(2*j+1)
                  for j in range(4)))
def cs(z):
    return tr(sum((-1)**j*tr(z**(2*j))/S.factorial(2*j)
                  for j in range(4)))
x = S.Integer(0)
for n in range(1,5):
    f = tr(6*x+e*(S.sqrt(3)*cs(x)-sn(x))
           +lam*e**2*(-2*S.sqrt(3)*cs(2*x)-2*sn(2*x)))
    x = tr(x-f.coeff(e,n)*e**n/6)
A3 = tr(3*x*x-e*(1-cs(x)-S.sqrt(3)*sn(x))
        -lam*e**2*(1-cs(2*x)+S.sqrt(3)*sn(2*x)))
C3, Q3 = A3.coeff(e,3), A3.coeff(e,5)
assert S.expand(C3-lam+S.Rational(1,24)) == 0
assert S.expand(Q3-lam**2/2+lam/8-S.Rational(1,384)) == 0
assert Q3.subs(lam,S.Rational(1,24)) == -S.Rational(1,576)
x = S.Integer(0)
for n in range(1,6):
    f = tr(4*x+2*e*cs(x)-4*lam*e**2*sn(2*x))
    x = tr(x-f.coeff(e,n)*e**n/4)
A40 = tr(2*x*x+2*e*sn(x)-2*lam*e**2*(1-cs(2*x)))
h = k = S.Integer(0)
for n in range(1,6):
    fh = tr(8*h+2*S.sqrt(2)*e*cs(h)*(cs(k)+sn(k))
            -8*lam*e**2*sn(2*h)*sn(2*k))
    fk = tr(16*k+2*S.sqrt(2)*e*sn(h)*(cs(k)-sn(k))
            +8*lam*e**2*cs(2*h)*cs(2*k))
    h = tr(h-fh.coeff(e,n)*e**n/8)
    k = tr(k-fk.coeff(e,n)*e**n/16)
A41 = tr(4*h*h+8*k*k+2*S.sqrt(2)*e*sn(h)*(cs(k)+sn(k))
         +4*lam*e**2*cs(2*h)*sn(2*k))
Delta = tr((A40-A41)/2)
C4, Q4 = Delta.coeff(e,4), Delta.coeff(e,6)
assert S.expand(C4-lam**2+3*lam/4-S.Rational(5,192)) == 0
assert S.expand(Q4+3*lam**2/2-lam/4+S.Rational(11,1920)) == 0
assert S.gcd(C4,Q4) == 1
assert S.rem(Q4,C4,lam) == S.Rational(1,30)-7*lam/8
assert S.resultant(C4,Q4,lam) == -S.Rational(761,921600)
print("INDEPENDENT_EXACT_PASS: action-derived C3,Q3,C4,Q4 and resultant")
```

作者程序另实际执行一次，退出码为零。所有六个 SUM-action-minus-force
检查均为精确零；输出的 $C,Q$、根代入、gcd、余式及 resultant 与保存摘要
相同（允许等价的因式分解／展开字符串），没有把 JSON 文本相同当数学证明。

## Corrections or missing assumptions

未发现本次输入中需要改动的结论。必须继续保留：固定参数、固定分母、
局部分支、非零小参数和仅线性椭圆的限制，不能在摘要中省略后升级结论。

## Open risks

- 本核查只证明分母 $3,4$ 的固定消失点确在 $s+2$ 阶恢复；全分母
  $C,Q$ 共同根排除依然未证。
- 形式递推可计算、作者脚本执行成功、独立有限系数核查和实际动力证明
  是不同层次；本报告逐项分别给证据，不互相替代。
- 不作新意、自然篇幅、正式候选票或 Batch07 完成数判断。
