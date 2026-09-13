# Paper31：有限节点准确标量交数的 fresh 独立数学审查 V1

日期：2026-09-12 UTC。审查席：`/root/p31_nodal_scalar_independent_v1`。
类型：`FRESH_NONAUTHOR_BOUNDED_MATHEMATICAL_REVIEW`。
结论：`PASS_WITHIN_STATED_NODAL_SCOPE`；**必须修正：∅**。
`route_applicability: NOT_APPLICABLE`。

## 1. 结论与权限边界

本人独立核准[作者稿][AUTHOR]的节点标量公式，量词未缩窄：
代数闭常数域 $k$、全部 $p=\operatorname{char}k>3$、$T\in k^\times$、
全部有限节点能级 $h_0$、全部正整数 $n$。保持原模型及指定点

$$
W_h:v^2+huv-Tv=u^3-Tu^2,\qquad P=(0,T),\qquad t_O=-u/v.
$$

由原唯一奇点取得 $w$，令
$T=w^3(w-1)$、$h_0=w(3-2w)$，其中 $w\ne0,1,3/4$。
取 $(w-1)\zeta^2+(2w-1)\zeta+(w-1)=0$ 的任意根。
写 $n=p^a m$，$p\nmid m$，则准确结论为

$$
i_n(h_0)=
\begin{cases}
0,&\zeta^m\ne1,\\
2p^a,&\zeta^m=1,\ p>5,\ (T,h_0)=(3/16,-2),\\
p^a,&\zeta^m=1,\ (T,h_0)\ne(3/16,-2).
\end{cases}
$$

特征 $5$ 的所列例外参数是尖点，不属于节点域；这里没有遗漏一个节点分支。
同一核查支持作者所列特征零边界：有限阶节点回返均横截。
这不是好纤维全部交数、尖点理想或全族异常谱的结论。

本报告仅是一席有界数学审查，不是完整候选四门票，不评分新意、独立价值或长文容量。
只消费[旧接受][ACCEPT]和[旧固定接口][FIX]的实际模型、标点及固定理想，
不重新为共轭、广义群作用、Fitting 表达或标准 $p$ 倍传播记功。
不建立项目、锁、稿件或 PDF；Paper31 原22–30页约束与整批4/5状态不由本报告改变。

## 2. 审查独立性、技能与实际阅读

本人未参与本轮节点作者工作。未读取本轮其它新作者 PF/contact/p-primary 报告或其它 fresh 审查，
未联系作者、作者 helper、旧审查者校准；未自派 helper。全部关键复算由本席实际执行。
只有向主控发送工作进展，没有通过他人结论替代数学判断。

已 FULL 读取 `AGENTS.md` 1–28、`docs/WORKFLOW.md` 1–39，
以及 `/root/autodl-tmp/.codex/skills/research-review/SKILL.md` 1–106。
`BATCH_07_CONTEXT.md` 只读1–20行作背景，不加载历史总账。
research-review 技能用于固定独立批评、证据和可操作修正清单；其 GPT-5.4 Codex MCP 未配置。
实际按主控授权使用当前可用 Codex xhigh fresh 席 fallback；没有调用该未配置模型，
没有外部 MCP `threadId`、跨模型验证或多轮作者对话，不虚构这些身份。
任务限定唯一输出路径，故不采用技能建议的根目录报告或记忆更新。

| 本地输入 | 本人实读层级 | 终态 SHA-256 |
|---|---|---|
| [AUTHOR] | FULL 1–346；身份与派发一致 | `5b61cbc732fbd70d6edd1979d183d50081ea1cac3d849164422447c5c785cf27` |
| [ACCEPT] | FULL 1–176；只消费既有接受 | `8527248c907f2b8abc1c84c0b89a5623ffae5d09e5c55877d59f98ca2054522a` |
| [FIX] | FULL 1–348；只消费实际对象和理想定义 | `401db0359ad2e05456ff3ec2aa7f93e2ad7fb7136e2f815f131b02a66e762ba7` |
| [SINGULAR] | PARTIAL 1–450 / 全683行 | `64cb688c586c8a82123c998dd23275539935fd3baed9c9e0f38d98c814f2dce7` |

首次组合工具输出发生总长度截断，相关 FULL 输入随后单独／分段补读至末行。
[SINGULAR] 作者自报的1–155、290–450并不替代本席阅读；本席另读156–289，
因此实际覆盖该源 Step 1 的奇点消元、Step 2 切锥、Step 3 群律和 Step 5 的点斜率式(27)。
本报告不声称读取该源451–683，也不继承其下游来源的 FULL 身份。

外文仅使用本人实际打开的 [Tate 原文][TATE]：PDF pp.1–6 的提取文本，
以及 p.7 的整数普适同态证明至完成同态／核的说明（工具文本至该段末）。
重点核对原式(4)、(11)、(14)、(15)、Theorem 1及其乘法同态证明。
该源允许任意完备赋值域，所需级数与清分母群恒等式具有整数系数；故可用于 $k((q))$。
没有读完其满射证明，也没有读取本轮所不需的 pp.21–23一般底环部分；证明不使用满射。
截图请求只返回定位，本席不据此冒称额外图像实读。
[NASK] 未由本席读取；下面直接证明 Frobenius 传播，不以作者的该源实读代替本人实读。
其余旧碰撞图、I03报告和下游来源未读取，本席不作全球查新或独立先例排除结论。

## 3. 逐项审查矩阵

| 核查项 | 结论 | 决定性证据 |
|---|---|---|
| 原奇点参数覆盖全部有限节点 | PASS | 原偏导消元与 $w$ 反代；切判别式 $w^2(4w-3)$ |
| 二次根确为指定点乘法值（容许取逆） | PASS | 旧交比中 $\kappa+\kappa^{-1}=-(2w-1)/(w-1)$ |
| 全部危险分母 | PASS | $\zeta,\zeta\pm1,R(\zeta)$ 为单位；二阶简式仅在 $p>5$ |
| Tate 级数、整数普适性及同态 | PASS | 实读原式及同态证明；无满射依赖 |
| 整个带点归一化与 $Q_Z=-P$ | PASS | 直接展开全部 Weierstrass 系数；不是仅匹配闭纤维 |
| 一、二阶恒等式(10)–(12) | PASS | 从源级数在 $\mathbb Q(Z)[q]/(q^3)$ 独立递推 |
| 固定 $T$ 的隐函数及原 $h$ 无分歧 | PASS | $\mathsf T'_0$ 与 $L$ 的显式单位式 |
| 唯一例外与 $\mathsf T_2=-125/81$ | PASS | $s=Z+Z^{-1}$ 的手工降次证书及精确代数复算 |
| 原 $t_O$ 的一、二阶符号 | PASS | 逆参数 $Z^{-d}$；首系数分别为作者式(17) |
| 全 $n$、非挠节点、特征零边界 | PASS | 单根阶数、Frobenius 恒等式与代数整数排除 |

没有发现需要作者改变命题、添加未声明假设或重新补证的 GAP。
下面把判定依据展开，以便核查报告自身不退化为 PASS 列表或 CAS 零输出。

## 4. 原奇点、群元素与单位核查

在旧源取其符号 $\varepsilon=1,c=h_0$，不是把源中的符号 $\varepsilon$ 与本轮基参数混同。
原奇点 $S=(a,b)$ 的偏导直接给
$a=T-z^2$、$a^2=Tz$、$h_0=T/z-3z$，$z=b/a$ 且 $az\ne0$。
令 $w=a/z$，得到 $z=w(w-1)$、$a=w^2(w-1)$，继而得到本轮 $(T,h_0)$。
反代原关系也全部成立，所除的 $a,z$ 已先证明非零。
平移到奇点后，切锥为 $Y^2+h_0XY+(3z^2-2T)X^2$，
判别式正是 $w^2(4w-3)$。故 $T\ne0$ 和节点条件准确给 $w\ne0,1,3/4$。

再核指定点的群参数。旧源切根 $\alpha,\beta$ 满足
$\alpha+\beta=-h_0$，$\alpha\beta=3z^2-2T$，
$\kappa_P=(z-\beta)/(z-\alpha)$，其倒数对应取负／交换切根。
由于 $(z-\alpha)(z-\beta)=-a$、$2z+h_0=w$，

$$
\kappa_P+\kappa_P^{-1}
 =\frac{(2z+h_0)^2+2a}{-a}
 =-\frac{2w-1}{w-1}.
$$

所以作者二次式确为原标点的准确乘法二次关系，而非任意重选点的参数。
其判别式 $4w-3\ne0$，常数项 $w-1\ne0$；代入 $Z=-1$ 得 $-1$，代入 $Z=1$ 得 $4w-3$。
由 $w=R(Z)/(Z+1)^2$，$R(Z)=Z^2+Z+1$，还排除 $R(Z)=0$。
这些排除在所有 $p>3$ 一致成立，不依赖素域、节点分裂型或抽样。

## 5. 带点模型、全部系数与原参数

对 Tate 方程代入作者变换，并除以 $\lambda^6$，各非常数系数直接成为

$$
v^2+\frac{1+2M}{\lambda}uv+\frac{B}{\lambda^3}v
-u^3-\frac{A}{\lambda^2}u^2.
$$

一次 $u$ 项由切线定义消去，常数项由点方程消去。
取 $\lambda=B/A$ 后，两个 $v,u^2$ 系数分别为 $-\mathsf T,+\mathsf T$，
其中 $\mathsf T=-A^3/B^2$，$\mathsf H=(1+2M)A/B$；这正是原方程移至左边后的符号。
$A_0,B_0$ 均为单位，因此是整个 $k[[q]]$ 上保持 $O$ 的可逆 Weierstrass 变换。
$Q_Z$ 明确落在 $(0,0)=-P$，而不是 $(0,T)$；原 $nP$ 因此对应 $Z^{-n}$。

独立递推从源级数的除数和生成 $X_j$，再用 $2Y_j=ZX'_j-X_j$ 生成 $Y_j$。
未把作者声称的 $A_j,\mathsf T_j$ 当计算输入。中间得到可核的斜率系数

$$
M_0=-\frac{Z(Z+2)}{(Z-1)(Z+1)},\quad
M_1=-\frac{(Z-1)^3(Z+1)}{Z^2},\quad
M_2=-\frac{(Z-1)^3(Z+1)R^2}{Z^4}.
$$

卷积和逆元递推随后重现作者全部 $A_0,A_1,A_2,B_0,B_1,B_2$，
$\lambda_0,\mathsf T_0,\mathsf T_1,\mathsf T_2,\mathsf H_0,\mathsf H_1$ 与 $\mathsf T'_0$。
源曲线方程的三个截断系数也全部消去。二阶商的递推自动给出作者式(12)的五项，
包括容易遗漏的 $-6A_1B_1/(A_0B_0)$，不存在少交叉项的问题。

这些恒等式在 $\mathbb Z[1/6,Z,Z^{-1},(Z-1)^{-1},(Z+1)^{-1},R^{-1}]$ 内成立。
用有理函数精确计算核它们，不等于只能在特征零成立：两侧分母的素数仅为已允许的 $2,3$，
清分母后是整数多项式恒等式，故向每个允许的 $k$ 特化合法。

独立得到

$$
\mathsf T'_0=\frac{(Z-1)^3R^2}{(Z+1)^9},\qquad
c_1=-\frac{(Z-1)(Z+1)R(3Z^2+4Z+3)}{Z^2},
$$

$$
L=\mathsf H_1+\mathsf H'_0c_1
 =-\frac{(Z-1)^6R}{Z^3(Z+1)^2}.
$$

其中 $\mathsf T'_0(\zeta)$ 与 $L$ 在每个节点均是单位；$c_1$ 允许在例外处为零。
固定 $T$ 的形式隐函数逐阶仅除以 $\mathsf T'_0(\zeta)$，不除以阶数／阶乘，适用正特征。
由 $h(q)-h_0=Lq+O(q^2)$ 得形式逆 $q(\epsilon)$，$\epsilon=h-h_0$。
于是这是原基完成环的同构，绝非 $\epsilon=q^e$、$e>1$ 的分歧换基。

## 6. 二阶例外的手工证书及全部特征边界

一阶消失当且仅当 $f(Z)=3Z^2+4Z+3=0$。
此时 $c_1=0$，二阶隐函数式确为 $c_2=-\mathsf T_2/\mathsf T'_0$；
通常出现的 $\mathsf T'_1c_1$、$\mathsf T''_0c_1^2/2$ 都已为零，不是被无理由省略。

以下证书不用 CAS 的零残差。令 $s=Z+Z^{-1}$，作者的互反八次多项式满足

$$
K(Z)/Z^4=k(s):=3s^4-12s^3-27s^2+17s+32.
$$

由 $R=Z(s+1)$、$(Z\pm1)^2=Z(s\pm2)$ 直接得到

$$
\mathsf T_0=-\frac{(s+1)^3}{(s+2)^4},\quad
\mathsf H_0=\frac{(s+1)(s+4)}{(s+2)^2},\quad
\frac{\mathsf T_2}{\mathsf T_0}=(s-2)^2k(s).
$$

$f=0$ 等价于 $s=-4/3$，此时 $k(s)=-20/27$、$(s-2)^2=100/9$。
所以准确得到

$$
\mathsf T_0=3/16,\qquad \mathsf H_0=-2,\qquad
\mathsf T_2=\frac3{16}\frac{100}{9}\left(-\frac{20}{27}\right)=-125/81.
$$

这是全特征可检查的有理式证书，所有当前分母已证明为单位。
$p=5$ 时 $f=3(Z-1)^2$，唯一根被节点排除；同时 $w=-1/2=3/4$，
$(3/16,-2)=(-27/256,9/8)$，恰为旧已知尖点。
$p>5$ 时 $-125/81\ne0$，所以二阶非零，不能出现三阶以上隐藏接触。

由 $2w+1=f/(Z+1)^2$，例外等价于 $w=-1/2$。
反向由 $h_0=-2$ 得 $(w-2)(2w+1)=0$；另一解 $w=2$ 对应 $T=8$，
$8-3/16=125/16\ne0$（$p>5$），因此例外原参数没有第二个节点分支。
另独立从原 $\delta$ 求导得到 $\delta_h(3/16,-2)=-125/4$，与上述边界相容。

## 7. 原局部参数符号、交理想与全 $n$

在 Tate 单位参数 $V=1$ 附近，把非极点级数项写成 $qF,qG$，它们对 $V-1$ 正则。
于是 $t_E=-X/Y=(V-1)$ 乘单位，且关于 $V-1$ 的线性系数为 $1$。
这不是只比较剩余点集，而是零截面理想的局部生成元比较。
原坐标变换给

$$
t_O=-\lambda\frac{X_c-X}{Y_c-Y-M(X_c-X)}
 =\lambda t_E\cdot\mathrm{unit},
$$

其中最后单位在 $O$ 的值为 $1$，故首项缩放准确为 $\lambda$。
取原点 $dP$ 时 $V=Z(q)^{-d}$，而不是 $Z(q)^d$，所以出现
$-\lambda_0d\zeta^{-1}$ 这个符号及因子。
非例外的一阶系数独立化为

$$
-\lambda_0\zeta^{-1}c_1/L
=\frac{(Z+1)^6f(Z)}{(Z-1)^6R(Z)}
=\frac{2w+1}{w(4w-3)^3}.
$$

例外的二阶系数除以 $d$ 为

$$
\frac{\lambda_0\mathsf T_2}{Z\mathsf T'_0L^2}
=\frac{(Z+1)^8K(Z)}{(Z-1)^{12}R(Z)^2}
=\frac{(s+2)^4k(s)}{(s-2)^6(s+1)^2}
\bigg|_{s=-4/3}=-3/3125.
$$

因此作者式(17)的两个原参数首项与负号均正确。
取二次式的另一个根只是相应取逆，最终两个首系数在 $w$ 上不变。

若 $\zeta^n\ne1$，Tate 级数在该剩余单位参数处给有限光滑点而非 $O$，故交数为零。
若 $\zeta$ 的阶为 $d$，则 $p\nmid d$；$Z^d-1$ 在 $\zeta$ 处的导数 $d\zeta^{-1}$ 非零，
故首次交数就是 $\operatorname{ord}_q(Z-\zeta)$，并由无分歧性等于原 $\epsilon$ 阶。
当 $n=p^a m$、$p\nmid m$ 且 $\zeta^m=1$ 时，
$(Z^m-1)^{p^a}=Z^n-1$，准确放大阶数 $p^a$，得§1的全 $n$ 公式。
这一步是标准乘法群传播，不是新的原族机制。

一般代数闭 $k$ 中 $\zeta$ 可以非根单位；此时所有正整数 $n$ 的交数为零。
例外 $f$ 的根却在 $\overline{\mathbb F}_p^\times$，故 $p>5$ 时具有有限阶，确实实现交数2。
特征零时，若 $\zeta$ 为根单位，则 $\zeta+\zeta^{-1}$ 是代数整数，不能等于非整数有理数 $-4/3$。
所以唯一二阶候选不能产生有限阶回返；全部有限阶节点回返横截。
该论证没有假设一般代数闭域的乘法群全挠，也没有外推为好纤维 I03 的解答。

## 8. 可重复的精确代数方法

实际执行环境为 Python 3 / SymPy 1.14.0；两个纯内存计算及下列内嵌脚本回放均 exit code 0。
没有读写辅助脚本／数据文件、浮点计算、有限域采样或扩展冻结F5表。
以下核心脚本从源级数构造截断环，再输出中间系数；它不把待核系数放进断言中：

```python
import sympy as S
from sympy.polys.fields import field
from sympy.polys.domains import QQ
F, Z = field('Z', QQ)
zero = F.zero
def const(c): return [F(c), zero, zero]
def add(a,b): return [a[i]+b[i] for i in range(3)]
def neg(a): return [-x for x in a]
def mul(a,b):
    return [sum((a[j]*b[i-j] for j in range(i+1)),zero)
            for i in range(3)]
def inv(a):
    b = [1/a[0]]
    for i in (1,2):
        b.append(-sum((a[j]*b[i-j] for j in range(1,i+1)),zero)/a[0])
    return b
def powr(a,n):
    b = const(1)
    for _ in range(n): b = mul(b,a)
    return b
X = [Z/(1-Z)**2]
Y = [Z**2/(1-Z)**3]
a4 = [zero]; a6 = [zero]
for j in (1,2):
    ds = [int(d) for d in S.divisors(j)]
    xj = sum((d*(Z**d+Z**(-d)-2) for d in ds),zero)
    X.append(xj); Y.append((Z*xj.diff(Z)-xj)/2)
    a4.append(F(-5*sum(d**3 for d in ds)))
    a6.append(F(-sum(S.Rational(7*d**5+5*d**3,12) for d in ds)))
B = add(X,mul(const(2),Y))
M = mul(add(add(mul(const(3),powr(X,2)),a4),neg(Y)),inv(B))
A = add(add(mul(const(3),X),neg(M)),neg(powr(M,2)))
lam = mul(B,inv(A))
TT = neg(mul(powr(A,3),powr(inv(B),2)))
HH = mul(mul(add(const(1),mul(const(2),M)),A),inv(B))
Tp = TT[0].diff(Z)
c1 = -TT[1]/Tp
L = HH[1]+HH[0].diff(Z)*c1
for name,a in [('X',X),('Y',Y),('M',M),('A',A),('B',B),
               ('T',TT),('H',HH[:2])]:
    print(name,[S.factor(x.as_expr()) for x in a])
for name,x in [('Tprime',Tp),('c1',c1),('L',L),
               ('linear',-lam[0]*c1/(Z*L)),
               ('quadratic_exception',lam[0]*TT[2]/(Z*Tp*L**2))]:
    print(name,S.factor(x.as_expr()))
```

另一次独立原多项式展开逐项输出归一化的七个系数，核对常数／切线消去与所有符号。
例外余式另用有理多项式模 $f$ 的精确逆元法得到
$(\mathsf T_0,\mathsf H_0,\mathsf T_2,t_{O,2}/d)=(3/16,-2,-125/81,-3/3125)$。
这些计算与§6–7的互反变量手工证书相互核对；结论不以有限参数运行成功代替全称证明。

## 9. 允许的消费者、未覆盖范围与最终处置

允许将本轮准确 $i_n$ 代入已接受节点理想
$\epsilon^{i_n}(\xi,\eta)$；若改用同原基相差单位的节点参数，生成理想不变。
这是旧完整理想的直接消费者，不新授旧群作用／全基共轭一票。
作者写明的新增计算是固定原 $T$ 切片的首阶、唯一二阶例外及准确二阶首项；本报告核准其数学。
标准 Tate 方法、形式逆函数与 Frobenius 传播均须扣除，不借审查 PASS 推出研究价值分数。

仍未覆盖：有限好纤维的一般准确 $D_n/i_d$、扩域 Manin 充分性、
好纤维 $p$-primary 算术分类、尖点全形式理想、无穷边界、$T=0$／非单位时间、
一般非自治返回、例外根单位阶随素数的分布、全球直接先例和完整长文准入。
这些不是本轮节点定理内部的缺证，不要求本轮同时解决。

最终逐项结果全部 PASS，必须修正集合为空；不存在需主控先作新权限决策的节点数学 blocker。
唯一新增本报告；作者原稿、旧接受、失败、锁、README、批次入口均未修改。
无投稿、上传、托管、push、外发消息、付费资源、实验或 PDF 构建。
交付前本人 FULL 自读本报告并确认输入身份；终态行数及 SHA-256 在交付消息报告，
文件不自载递归哈希。报告冻结后不把未读材料或其它审查结论回填为本席独立证据。

[AUTHOR]: PAPER31_QPI_MANIN_NODAL_SCALAR_PROBE_V1_20260912.md
[ACCEPT]: PAPER31_QPI_MANIN_PRIMEFIELD_AND_FIXED_SCHEME_DISPOSITION_V1_20260912.md
[FIX]: PAPER31_QPI_MANIN_FIXED_SCHEME_INTERFACE_PROBE_V1_20260912.md
[SINGULAR]: PAPER30_QPI_SINGULAR_CUBIC_GROUP_ENTRY_V1_20260908.md
[TATE]: https://web.ma.utexas.edu/users/voloch/Preprints/nonarch-ams.pdf
