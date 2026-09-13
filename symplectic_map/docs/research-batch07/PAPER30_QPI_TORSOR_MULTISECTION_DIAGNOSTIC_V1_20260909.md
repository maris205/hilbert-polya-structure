# Paper30：真实末端多截面与最小分裂覆盖的有界诊断 V1

日期：2026-09-09。类型：I01 的局部理论诊断；不是正式评价、查新、论文项目或全部多截面分类。
使用 proof-writer 技能；保留旧泛 torsor 预筛，不重证／重审已接受 T1。

## Claim / Status

PROVABLE AS STATED：以下显式式子与分歧结论针对一条真实末端曲线的闭包 $\overline L_1$。
在特征零、$s$ 精确阶为 $r\ge1$、$t\ne0$ 的原系统中，它给出次数最小的有理分裂覆盖。
$r=2$ 时覆盖为 $c=2t-(v+1)^2$；$r=3$ 时为 $c=-w^3+3tw-3t$，其中 $w=v-s^{-1}$。
任意 $r$ 有下述显式有限矩阵积公式；$r\ge3$ 时该覆盖自同构群平凡，特别地不是 Galois 覆盖。
I01 的“所有最小有理覆盖分类、原回返轨道与有向 Weil–Châtelet 余循环”仍为 NOT CURRENTLY JUSTIFIED。

## 实际读取范围与准确目标

- [POSTV2_IDEATION V1](PAPER30_QPI_POSTV2_IDEATION_V1_20260909.md)：全文 1–339 行；本件消费者为 I01（109–126）及 §5（290–313）。
  其目标是最小覆盖／分歧／轨道分类与实际下降类，不以 index 或无截面推论验收。
- [候选简报 V2](PAPER30_QPI_CANDIDATE_BRIEF_V2_20260909.md)：本次定向重读 36–150 行，使用原矩阵、$I_r$、四张真实图与 T1。
- [辛与极除子入口 V1](PAPER30_QPI_SYMPLECTIC_POLAR_ENTRY_V1_20260908.md)：定向读取 112–240 行；使用 116–163 的实际吹起、唯一边界交点，及 196–236 的实际图接口。
- [边界法丛入口 V1](PAPER30_QPI_BOUNDARY_NORMAL_BUNDLE_ENTRY_V1_20260908.md)：定向读取 68–110 行；尤其 83 行确认图一确为 $(\infty,1)$ 的一次真实吹起。
- 先用文件名及相关坐标关键词定向定位上述文件；未读取旧正式票或独审全文，未全扫历史。
  `proof-writer/SKILL.md` 本次重新完整读取。没有外部文献新检索，也不作先例穷尽结论。

## Assumptions / Notation

取代数闭特征零域 $k$，$s,t\in k^*$，$\operatorname{ord}(s)=r$；$t$ 保持符号，不要求一般位置。
这是 I01 的特征零首阶段；下述分歧清单不外推到正特征，尤其不能把三次式的临界点清单直接约化到特征二。
$S=S_{t,s}$、$f=I_r$ 与 $D$ 均为原对象，采用 T1 的 $f^{-1}(\infty)=rD$ 及光滑泛纤维结论。
$\overline L_1\simeq\mathbb P^1_v$ 是图 $x=u^{-1},y=1+uv$ 内 $u=0$ 的完整闭包。
其仿射部分是 $L_1\simeq\mathbb A^1_v$，唯一边界点为 $v=\infty$；交数 $D\cdot\overline L_1=1$。
令 $K=k(c)$，$w=v-s^{-1}$，$z_j=s^j$，$b_r(w)=I_r|_{\overline L_1}$。
仅改变多截面的源坐标；全文 $c$ 保持 JR 的原能级，不替换为 $(-1)^{r+1}c$。

## Proof Strategy / Dependency Map

1. 从原 $A(z)$ 的真实吹起代入出发，消去可去的矩阵极点，得到边界矩阵 $B(z)$。
2. 通过相邻因子间可抵消的显式规范变换，得到任意阶的二阶传递矩阵。
3. 二／三阶直接相乘求全式；任意阶高次项用根单位求和与矩阵路径计算，不从有限样本外推。
4. 分裂由多截面图的对角截面给出；最小次数沿用已知 index，不重开旧证明。
5. 分歧来自多项式导数与无穷远极点；覆盖自同构由保持唯一极点的分式线性变换判定。

## Proof

### Step 1. 真实图上的原矩阵限制

令 $G=\operatorname{diag}(1,u)$。在 $u\ne0$ 上用 $G^{-1}A(z)G$ 不改变任意乘积的迹。
代入 $x=u^{-1},y=1+uv$ 后，所有矩阵元在 $u=0$ 正则，唯一出现的非平凡分母为 $1+uv$。
因此虽然 $G$ 本身在边界不可逆，其共轭矩阵可在边界取值；该值为
$$
B(z)=\begin{pmatrix}
t-v-vz+z^2&-1\\
v(v-t)+z(v^2+v-t)&v+z
\end{pmatrix}.
$$
例如原 $A_0$ 的四个条目分别成为 $t-v,-u^{-1},uv(v-t),v$，共轭后即消去负极阶。
对有限个因子的乘积逐项取值有效，且与 T1 给出的原积分正则延拓一致，故
$$
b_r=\operatorname{tr}\{B(s^{r-1})\cdots B(1)\}-(t^r+1).
$$

### Step 2. 任意阶的显式覆盖方程

置 $R=\begin{pmatrix}1&0\\-v&1\end{pmatrix}$、$H(z)=\begin{pmatrix}1&0\\-z/s&1\end{pmatrix}$。
直接相乘给出
$$
R^{-1}B(z)R=\begin{pmatrix}t-vz+z^2&-1\\vz^2-tz&z\end{pmatrix},\qquad
H(sz)^{-1}R^{-1}B(z)RH(z)=T(z):=\begin{pmatrix}t+z^2-wz&-1\\z^3&0\end{pmatrix}.
$$
相邻 $H$ 因子抵消，且 $H(s^r)=H(1)$，所以原能级上的显式最小分裂覆盖为
$$
\boxed{\quad c=b_r(w):=\operatorname{tr}\{T(s^{r-1})\cdots T(1)\}-(t^r+1).\quad}
$$
这是任意指定 $r,s,t$ 的有限多项式公式；等价递推为 $Q_0=\operatorname{id}_2$、$Q_{j+1}=T(s^j)Q_j$、$b_r=\operatorname{tr}Q_r-t^r-1$。
本节 $T(z)$ 是矩阵，不是标量参数 $T=t^r$。
$r=1$ 给 $b_1=-w=1-v$。以下不把该递推称作全部分支碰撞的闭式分类。

### Step 3. 任意阶高次项的独立计算

设 $r\ge3$，记 $a_j=t+z_j^2-wz_j$、$q_j=z_j+t/z_j$，下标按模 $r$ 解释。
迹的矩阵路径展开中，全程停留在第一状态给 $\prod a_j$；
一次访问第二状态必须连续使用下左元 $z_j^3$ 与下一步上右元 $-1$，给 $-z_j^3\prod_{i\ne j,j+1}a_i$。
两次以上这种访问至多贡献次数 $r-4$。利用 $\prod z_j=(-1)^{r-1}$，全第一状态的项是 $-\prod(w-q_j)$。
根单位求和给 $\sum q_j=0$、$\sum q_j^2=2rt$；当 $r\ge4$，还给 $\sum q_j^3=0$。
当 $r\ge4$ 时，由初等对称函数恒等式，它在次数 $r$ 至 $r-3$ 的部分为 $-w^r+rtw^{r-2}$，另两项系数为零。
单次访问路径的 $w^{r-2}$ 系数之和为 $s^{-1}\sum z_j=0$；其 $w^{r-3}$ 系数之和为
$$
\frac1s\sum_j z_j(q_j+q_{j+1})=rt(s^{-1}+s^{-2}).
$$
于是对全部 $r\ge4$、全部 $t\ne0$，有严格多项式系数恒等式
$$
b_r(w)=-w^r+rtw^{r-2}+rt(s^{-1}+s^{-2})w^{r-3}+O(w^{r-4}).
$$
这里 $O$ 只表示次数不超过 $r-4$ 的多项式；常数减项 $t^r+1$ 已包括其中。
$r=3$ 的完整式在下一步单独计算，因此没有把 $\sum q_j^3=0$ 错用于三阶。

### Step 4. 二阶及三阶：准确分歧与 Galois 性

$r=2$ 时 $s=-1$、$w=v+1$。两个矩阵相乘的迹为 $(t+1-w)(t+1+w)$，故
$$
\boxed{c=2t-w^2=2t-(v+1)^2.}
$$
覆盖的源分歧点为 $w=0,\infty$，像为 $c=2t,\infty$，各分歧指数均为 $2$。
函数域扩张 $k(w)/k(c)$ 为二次 Galois 扩张，其唯一非平凡自同构是 $w\mapsto-w$，即 $v\mapsto-v-2$。
它的射影式为 $[W:Z]\mapsto[2tZ^2-W^2:Z^2]$；$t$ 未作数值特化。

$r=3$ 时 $s^2+s+1=0$。迹为 $a_0a_1a_2-(a_0+a_1+a_2)$，
其中 $\prod a_j=t^3+1-w^3+3tw$、$\sum a_j=3t$；所以
$$
\boxed{c=-w^3+3tw-3t,\qquad w=v-s^{-1}.}
$$
选择 $\alpha\in k$ 满足 $\alpha^2=t$。全部分歧为
$$
w=\alpha\mapsto c=-3t+2t\alpha\ (e=2),\quad
w=-\alpha\mapsto c=-3t-2t\alpha\ (e=2),\quad
w=\infty\mapsto c=\infty\ (e=3).
$$
因 $t\ne0$ 且特征零，两个有限分歧点及其像分别互异；导数 $-3(w^2-t)$ 已穷尽有限分歧。
该三次覆盖不是 Galois；其 Galois 闭包可显式取 $k(q)$，其中
$$
w=q+t/q,\qquad c=-3t-q^3-t^3/q^3.
$$
此六次覆盖具有 $q\mapsto sq$、$q\mapsto t/q$ 生成的六个自同构，群为 $S_3$。
它包含原三次扩张；原扩张不是正规扩张，故该六次正规扩张就是 Galois 闭包。
独立核验：$w^3-3tw+c+3t$ 的判别式为 $27\{4t^3-(c+3t)^2\}$，两个有限零点均为单零点，因而不是平方。

### Step 5. 任意阶的分歧边界与覆盖自同构

$b_r$ 为次数恰为 $r$ 的多项式，故 $w=\infty$ 是 $c=\infty$ 的唯一原像，分歧指数为 $r$。
在特征零，有限分歧除子由 $b'_r(w)=0$ 给出，含重数总次数为 $r-1$；
一个根的重数为 $e_w-1$。有限分歧值的带重数消去式为 $\operatorname{Res}_w(b_r(w)-c,b'_r(w))$，差一个非零标量。
对于 $r\ge4$，本件没有给出该消去式的因子分类或全部特殊 $t$ 的分支碰撞清单。

若 $\sigma$ 是覆盖自同构，则它保持唯一无穷点，故在源上为 $w\mapsto aw+b$。
对 $r\ge3$，比较 $b_r(aw+b)=b_r(w)$ 的首项及 $w^{r-1}$ 项，得到 $a^r=1$、$b=0$。
非零的 $rtw^{r-2}$ 项又给 $a^{r-2}=1$。若 $r$ 为奇数，则 $a=1$。
若 $r\ge4$ 为偶数，则再用 $rt(s^{-1}+s^{-2})\ne0$ 的 $w^{r-3}$ 项，得到 $a^{r-3}=1$，仍有 $a=1$。
这里非零性来自 $t\ne0$、$s\ne-1$ 和特征零。故全部 $r\ge3$ 的覆盖自同构群平凡，不可能 Galois。
这不等于证明其 Galois 闭包群为 $S_r$；本件只在 $r=3$ 确定了闭包群。

### Step 6. 为什么确实分裂且次数最小

$\overline L_1\to S$ 的图在 $S\times_{\mathbb P^1_c}\mathbb P^1_w\to\mathbb P^1_w$ 中给出截面；
其泛点是原光滑曲线 $X$ 在 $k(w)$ 上的实际点，位置为真实图中的 $(u,v)=(0,w+s^{-1})$。
这不是只消去无穷远局部类，而是全局基变换上实际存在的截面。
由已接受的交数／index 推论，任意有限分裂扩张次数都被 $r$ 整除；本覆盖次数恰为 $r$，所以最小。
未据此声称所有最小分裂扩张的定义域都为 $\mathbb P^1$，也未声称所有最小有理分裂覆盖都由四条末端曲线给出。∎

## 标准包含检验：已经能扣除什么

对任何同样满足 $f^{-1}(\infty)=rD$、$D\cdot L=1$ 且 $L\simeq\mathbb P^1$ 的 Halphen 配置，
$f|_L$ 只有一个极点，极阶为 $r$；选此点作源无穷点后，限制必为次数 $r$ 的多项式。
所以“最小有理分裂、单极点、无穷远全分歧”是立即几何后果，不是新的 qPI 机制。
二阶式经配方就是任何二次多项式覆盖的形式；二次 Galois 性和两个分歧点均无独立差额。
三阶式在 $w=\alpha z$、目标仿射改名后为 $-z^3+3z$，即标准三次 Dickson／Chebyshev 型多项式覆盖；
上述六次闭包正是其根式参数化。此处目标改名仅用于比较覆盖类型，不更改前面的原 $c$ 公式。
任意阶的具体矩阵积与高次系数是本件完成的原坐标计算；平凡自同构群却仍是普通多项式覆盖的常见现象。
没有新文献核查，不能声称所有这些坐标公式已发表于某文；但这些局部结果本身没有实现 I01 要求的分类差额。

## Corrections / Open Risks / 未证下一步

- 本诊断只计算 $\overline L_1$。其余三条曲线的限制可沿真实时间图比较，但尚未执行；不预设四条曲线穷尽轨道。
- 尚未分类全部最小有理多截面、其原回返轨道或覆盖同构类；也未检验 Picard 格分类是否直接覆盖全部该量词。
- 显式 $k(w)$-点给出可用的分裂域，但尚未在指定 Tate Jacobian 坐标计算共轭点的有向差；没有实际 Weil–Châtelet 余循环。
- 公式出现 $s,t$ 而不只出现 $T=t^r$，本身不证明它们在允许的覆盖同构／时间作用下给出新的不变量。
- 真正下一步若继续 I01，必须先固定覆盖同构与原回返轨道的等价关系，再找不能被一般 Halphen 格理论代签的分类问题。
  本件未证明该差额存在，不能据这次局部计算升级为新候选。

## CAS 诊断记录：命令与边界

使用本地 `python - <<'PY'` 内联 SymPy，共三次；没有生成脚本文件或外部 API 调用。
第一次从简报原 $A_0,A_1$ 代入真实图，经 $G$ 共轭取 $u=0$：所得 $B$ 如 Step 1，$\det B-z^3=0$；
并计算二／三阶迹、三阶导数及 resultant。第一次完整命令为：

```bash
python - <<'PY'
import sympy as S
v,t,z,u=S.symbols('v t z u')
x,y=S.symbols('x y')
A0=S.Matrix([[t+x-x*y,-x],[t+x-t*y-2*x*y+x*y**2,x*(y-1)]])
A1=S.Matrix([[y-x+x/y-1-t/x,1],[y-2*x-1+x*y+x/y-t/x,1]])
A=A0+z*A1+z*z*S.diag(1,0)
G=S.diag(1,u)
Au=(G.inv()*A.subs({x:1/u,y:1+u*v})*G).applyfunc(S.cancel)
B=Au.applyfunc(lambda a:S.cancel(a).subs(u,0))
print('B(z) =',B)
print('det B - z^3 =',S.factor(B.det()-z**3))
b2=S.factor(S.trace(B.subs(z,-1)*B.subs(z,1))-t**2-1)
print('b2(v) =',b2)
s=S.symbols('s')
poly=S.Poly(s**2+s+1,s)
rem=lambda a:S.rem(S.Poly(S.expand(a),s),poly).as_expr()
b3=rem(S.trace(B.subs(z,s*s)*B.subs(z,s)*B.subs(z,1))-t**3-1)
print('b3(v) mod Phi3 =',S.factor(b3))
print('b3 derivative =',S.factor(S.diff(b3,v)))
print('b3 finite branch values equation =',S.factor(S.resultant(b3-S.Symbol('c'),S.diff(b3,v),v)))
PY
```

第二次命令如下；辅助查看阶数实际为 $2,3,4,5,6$，均保留符号 $t$。
这些有限阶输出仅用于发现系数模式，不承担 Step 3 的任意阶证明，也不充作所有分歧的分类证据。

```bash
python - <<'PY'
import sympy as S
v,t,z,s,w=S.symbols('v t z s w')
B=S.Matrix([[t-v-v*z+z*z,-1],[v*(v-t)+z*(v*v+v-t),v+z]])
for r in (2,3,4,5,6):
    cyc=S.Poly(S.cyclotomic_poly(r,s),s)
    def red(a): return S.rem(S.Poly(S.expand(a),s),cyc).as_expr()
    prod=S.eye(2)
    for j in range(r): prod=(B.subs(z,s**j)*prod).applyfunc(red)
    b=red(S.trace(prod)-t**r-1)
    dep=red(b.subs(v,w+s**(r-1)))
    print('r =',r)
    print('b_r(v) =',S.collect(b,v))
    print('b_r(w+s^(-1)) =',S.collect(dep,w))
PY
```

第三次直接核对两次规范变换、三阶式和判别式，命令如下；前两个 residual 均为零。

```bash
python - <<'PY'
import sympy as S
v,t,z,u,s,w,c=S.symbols('v t z u s w c')
B=S.Matrix([[t-v-v*z+z*z,-1],[v*(v-t)+z*(v*v+v-t),v+z]])
R=S.Matrix([[1,0],[-v,1]])
H=lambda q:S.Matrix([[1,0],[-q/s,1]])
T=S.Matrix([[t+z*z-w*z,-1],[z**3,0]])
print('two gauge residual =',(H(s*z).inv()*R.inv()*B*R*H(z)-T.subs(w,v-1/s)).applyfunc(S.factor))
print('cubic product residual =',S.rem(S.Poly(S.expand(S.trace(T.subs(z,s*s)*T.subs(z,s)*T.subs(z,1))-t**3-1-(-w**3+3*t*w-3*t)),s),S.Poly(s*s+s+1,s)).as_expr())
p=w**3-3*t*w+c+3*t
print('cubic discriminant =',S.factor(S.discriminant(p,w)))
PY
```
