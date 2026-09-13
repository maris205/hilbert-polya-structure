# Proof Package：共同根问题的响应规约与一个导数闭包反证 V2

日期：2026-09-07。角色：有界作者机制研究，不是旧稿审核。
接续[上一轮处置](PAPER30_TWIST_POST_CANCELLATION_AND_BRIDGE_DISPOSITION_20260907.md)。
只新增本文件；不修改已接受的次项、脚本、结果或审查文件。

## Claim

仍固定原双谐波映射、SUM action 和互素 $0<r<s$、$s\ge3$。
研究是否能在每个简单实根 $C_{r,s}(\lambda_*)=0$ 上证明
$Q_{r,s}(\lambda_*)\ne0$，其中 $\lambda_*$ 固定、不随 $\epsilon$ 调谐。

本轮具体处理三项：

1. 将单负节点缺陷写成一个严格线性响应，说明它与参数／传播子导数使用同一个响应算子。
2. 给出传播子灵敏度的无响应未知量公式及其齐次恒等式。
3. 检验非平凡低复杂度闭包
   $Q=a_sC+(b_s\lambda+c_s)C'$，其中系数可以依赖 $r,s$，但不依赖 $\lambda$。

## Status

原全分母共同根排除：`NOT CURRENTLY JUSTIFIED`，仍为 OPEN。

下文线性响应／灵敏度恒等式：`PROVABLE AS STATED`。
上述三常数导数闭包：在实际 $(r,s)=(1,6)$ 严格不成立。
这不是原映射的共同根反例，也不排除更复杂但需要另证的身份。
没有把事后令 $h=Q/C'$ 或 Bézout 逆元称为非消失机制。

## Assumptions and notation

保持[已接受次项稿](PAPER30_TWIST_POST_CANCELLATION_PROBE_V1_20260907.md)的规范。
令 $t$ 为正频形式变量，$N=t\partial_t$，$\zeta=e^{2\pi ir/s}$，

$$D_m=2-\zeta^m-\zeta^{-m},\qquad L(t^m)=D_mt^m.$$

$\Pi$ 删除全部 $s$ 的整数倍频率。正支 $v(t)=\sum_{n\ge1}v_nt^n$
满足 $v_n=0$ 当 $s\mid n$，以及

$$Lv+\Pi g=0,\qquad
g=\frac t2e^v+\lambda t^2e^{2v},\qquad
A=\frac t2e^v+2\lambda t^2e^{2v}.\tag{1}$$

本轮只需有限截断，但以形式 Laurent 级数书写更简洁。
传播子导数指把 $D_1,\ldots,D_{s-1}$ 作为成对相等的代数变量，
最后在实际正弦值上求值；这只是检查身份的参数记账，不引入另一动力系统族。

## Proof strategy and dependency map

单负节点源由已接受的完整 Fourier 式抽出。相位导数向量
$w=1+Nv$ 给出一个离散 Ward 恒等式；利用共振系数双线性配对，
将响应未知量从输出中消去。这个推导与主控的作用量 envelope 证明不同，
但计算同一个 $Q$，不将二者计为不同科学结果。

随后用同一响应公式计算传播子导数，并以真实六分母作一条过定导数身份的
最小偶分母检验；不增加根扫描或低分母非消失清单。

## Proof

### Step 1. 单负节点线性响应

在完整展开中，阶数减频率为 $2$ 的项恰含一个负一次谐波节点。
写该缺陷位移为 $\epsilon^2h(t)$，其中
$h(t)=\sum_{m\ge-1}h_mt^m$、$h_m=0$ 当 $s\mid m$。
保留缺陷一次项，正支力的线性化为 $Ah$，负一次源为

$$b=\frac1{2t}e^{-v}.$$

所以完整 Fourier 方程严格等价于

$$\bigl(L+\Pi A\bigr)h=\Pi b.\tag{2}$$

$A$ 始于一次，因此式 (2)在删除共振频率后的 Laurent 级数上三角可解，
从 $h_{-1}=1/(2D_1)$ 开始。它不是把原映射改成纯正频映射：
负节点的全部位移响应仍包含在 $h$ 中。输出为

$$Q=-2[t^s](Ah-b).\tag{3}$$

### Step 2. 一个共同的响应泛函

对任意最低次数不小于 $-1$ 的源 $f$，令 $h_f$ 为
$(L+\Pi A)h_f=\Pi f$ 的唯一投影解，定义

$$\mathscr R_s(f)=[t^s](Ah_f-f).\tag{4}$$

定义双线性配对 $\langle p,q\rangle_s=[t^s]pq$。
由于 $D_{s-m}=D_m$，$L$ 对这一配对自伴；乘以 $A$ 也自伴。
由 $Ng=A(1+Nv)$，式 (1)给出

$$ (L+A)w=(I-\Pi)Ng,\qquad w=1+Nv.\tag{5}$$

右边只含正的共振次数 $s,2s,\ldots$。
$h_f$ 没有零次项，且最低次数为 $-1$，故
$[t^s]((L+A)w)h_f=0$。
另一方面 $(L+A)h_f=f+(I-\Pi)(Ah_f-f)$。
$w_0=1$、$w_{ks}=0$ 对非零整数 $k$ 成立，故配对后得到

$$\boxed{\mathscr R_s(f)=-[t^s](1+Nv)f.}\tag{6}$$

这对所有 $\lambda$ 成立，不要求 $C=0$。
取 $f=b$，用 $N(e^{-v})=-(Nv)e^{-v}$，得

$$\mathscr R_s(b)=\frac s2[t^{s+1}]e^{-v},\qquad
Q=-s[t^{s+1}]e^{-v}.\tag{7}$$

式 (7)与主控本轮 envelope 候选式一致；这里给出的是从真实负缺陷响应到该式的
直接代数消元。不是再次运行旧 $s=3,4$ 的结果验证。

参数导数也有同样结构。令 $B=t^2e^{2v}$，则
$(L+\Pi A)v_\lambda=-\Pi B$。从 $C=-2[t^s]g$ 和式 (6)得到

$$C'=2\mathscr R_s(B)=-s[t^{s-2}]e^{2v}.\tag{8}$$

因此在简单根上，已知的是 $\mathscr R_s(B)\ne0$；
目标则是 $\mathscr R_s(b)\ne0$。这两个非零条件不能因响应算子相同就相互推出。
源 $B$ 始于 $t^2$，源 $b$ 有非零 $t^{-1}$ 项；
一个是改变第二谐波幅度，一个是插入负一次谐波。
这一源空间区别也说明原始 $h$ 不可能直接等于纯正支参数导数的常数线性组合。
但它不排除输出系数层面存在另一条需要独立证明的身份。

### Step 3. 传播子导数的精确卷积身份

取任意成对变分 $\delta D_m=\delta D_{s-m}$，保持零共振分母。
正支变化满足

$$ (L+\Pi A)\delta v=-\Pi(\delta L)v.$$

也可直接对式 (1)微分，再用 (5)配对，得到

$$\delta C=-2[t^s](1+Nv)(\delta L)v.$$

由于 $v_s=0$，常数 $1$ 的贡献为零。对 $k$ 与 $s-k$ 配对求和，
$k+(s-k)=s$，因此

$$\boxed{\delta C=-s\sum_{k=1}^{s-1}\delta D_k\,v_kv_{s-k}.}\tag{9}$$

这里求和按全部 $1\le k<s$ 计数；若改为独立的成对变量，
非中心项必须合并两次，不能漏因子 $2$。

同时，将所有 $D$ 乘以 $\eta$，式 (1)的变量替换
$t\mapsto t/\eta$、$\lambda\mapsto\eta\lambda$ 给出

$$C(\eta D,\lambda)=\eta^{1-s}C(D,\eta\lambda).$$

在 $\eta=1$ 微分，并代入 (9)，得到

$$\boxed{-s\sum_{k=1}^{s-1}D_kv_kv_{s-k}=(1-s)C+\lambda C'.}\tag{10}$$

特别在简单实根处，旧已证明的实根正性给出 $\lambda_*>0$，故
该卷积等于 $\lambda_*C'(\lambda_*)\ne0$。
这是确实新增的导数规约，但尚非 $Q$ 的共同根排除：
$v_kv_{s-k}$ 不是 $|v_k|^2$，因此不能把左边当作非负能量，
也未取得它与式 (7)的非零比例关系。

### Step 4. 指定三常数导数闭包在实际六分母失败

检验

$$Q=aC+(b\lambda+c)C',\qquad a,b,c\ \text{与}\ \lambda\ \text{无关}.\tag{11}$$

此式有真实内容：对偶分母六，$C,Q$ 至多三次，但右边只有三个自由常数。
此前三、四分母不能提供这一最小过定检验。
实际 $(r,s)=(1,6)$ 的 $D=(1,3,4,3,1)$，既有精确首项为

$$C=-\frac43\lambda^3+\frac{39}{8}\lambda^2
-\frac{127}{96}\lambda+\frac{99}{2560}.$$

本轮仅为检查 (11)，在已接受完整 Fourier 程序中使用该精确 $D$ 到八阶，得到

$$Q=\frac{163}{8}\lambda^3-\frac{3251}{192}\lambda^2
+\frac{3581}{1536}\lambda-\frac{72343}{1290240}.\tag{12}$$

程序同时验证直接代入 SUM action 与力法的系数差为零。
没有求这个 $Q$ 的根、没有扩大共同根列表，也未据此授予新的全分母结论。
比较 (11)的四个系数，系数矩阵及右侧的增广矩阵为

$$
\left[\begin{array}{ccc|c}
4/3&4&0&-163/8\\
-39/8&-39/4&4&3251/192\\
127/96&127/96&-39/4&-3581/1536\\
-99/2560&0&127/96&72343/1290240
\end{array}\right].
$$

其四阶行列式为 $76011797/1161216\ne0$，系数矩阵秩为 $3$，增广秩为 $4$。
因此不存在这样的 $a,b,c$。
等价地，$Q\bmod C$ 不能等于仿射函数 $(b\lambda+c)C'\bmod C$：
因被除多项式次数至多三，若可整除，其商必为常数 $a$。
这也否定了更窄的 $Q\bmod C=\gamma C'$，但不否定任意更高次或其他传播子导数身份。$\square$

## Minimal exact reproducibility

本轮唯一新增精确案例是上述六分母**身份**，而非新的根扫描。
没有重跑旧三、四分母。下面命令只打印结果；`-B` 避免在旧作者脚本旁生成缓存。

```bash
python -B - <<'PY'
import runpy
import sympy as sp
ns=runpy.run_path('docs/research-batch07/PAPER30_TWIST_POST_CANCELLATION_PROBE_V1_20260907.py')
x=ns['LAM']; a,b,c=sp.symbols('a b c')
D={1:sp.Integer(1),2:sp.Integer(3),3:sp.Integer(4),4:sp.Integer(3),5:sp.Integer(1)}
_, coefficients, _=ns['compute'](6,D,8)
C=coefficients[(6,6)]; Q=coefficients[(8,6)]
equations=sp.Poly(Q-a*C-(b*x+c)*sp.diff(C,x),x).all_coeffs()
M,rhs=sp.linear_eq_to_matrix(equations,[a,b,c])
assert M.rank()==3 and M.row_join(rhs).rank()==4
assert M.row_join(rhs).det()==sp.Rational(76011797,1161216)
print('EXACT_FAILURE_OF_AFFINE_DERIVATIVE_CLOSURE')
PY
```

## Corrections or missing assumptions

式 (9)允许传播子成对代数变分，不声称真实 $r/s$ 可连续变化而保持同一问题。
式 (11)的系数不依赖 $\lambda$ 是被检验命题的定义；
如果允许任意参数多项式或事后有理系数，可能仅是在运用 Bézout 恒等式，
不自动给出非零因子或动力学机制。

## Open risks

共同根问题现在可以严格表述为：在同一正支与同一响应泛函下，
$\mathscr R_s(B)\ne0$ 是否强制 $\mathscr R_s(b)\ne0$，并需结合 $C=0$。
本稿没有得到该蕴含；式 (9)–(10)也没有提供它。
主控本轮的反函数／留数规约是另一种输出表达，未经额外非消失论证同样不能当作矛盾。
全分母固定消失点后的共同根义务仍 OPEN。
本稿不改科学范围、不作容量票、PDF、新项目或跨族拼接；
proof-writer 技能用于明确成立的身份、被反驳的具体闭包和剩余证明义务。
