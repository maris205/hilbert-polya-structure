# Paper31 N06：固定完整原纤维的有点性诊断 V1

日期：2026-09-12；作者席：`/root/p31_post_closed_n06_full_fibre_diagnostic_v1`。
类型：一次固定原对象的作者证明；不是独立数学验收、新意／容量票或 Route 评价。
`route_applicability: NOT_APPLICABLE`；GPU 预算与实际均为 0。

## 1. Claim 与事前对象卡

本卡先于本席任何 CAS、点搜索或局部剩余枚举写入。同一未冻结作者稿随后补充实际证书；不改参数、不换模型或原能量标签。
准确任务是判定完整原曲线 $X_{c_1}(K)$ 是否为空，其中
$$
K=\mathbb Q_3(s),\qquad s=\zeta_3,\qquad \pi=s-1,\qquad
t=1,\quad h=0,\quad c_0=-3,\quad c_1=-3+\pi^2.
$$
$c_0$ 已接受的原点不是本件新结论；不把原曲线与其 Jacobian 混同。

### 1.1 Assumptions：原整模型、完备化和固定纤维

取 $\mathcal O=\mathbb Z[s]_{(s-1)}$，其剩余域为 $\mathbb F_3$。
由于 $\pi^2+3\pi+3=0$ 为 Eisenstein 多项式，$K/\mathbb Q_3$ 全分歧次数为二，
$\mathcal O_K=\mathbb Z_3[s]=\mathbb Z_3[\pi]$，且
$\widehat{\mathcal O}=\mathcal O_K$、$v_\pi(\pi)=1$、$v_\pi(3)=2$。
原底环映射是 $\mathbb Z[q^{\pm1},\tau^{\pm1}]\to\mathcal O\to\mathcal O_K$，
$q\mapsto s$、$\tau\mapsto1$。DVR 的完备化为平坦映射。

消费[INT] §3.2 及 [G] G1：同一原八次截面吹起的 $\mathcal S/\mathcal O$ 光滑射影，
$f=I_3:\mathcal S\to\mathbb P^1_{\mathcal O}$ 射影平坦，$f^{-1}(\infty)=3\mathcal D$，
剩余态射为 $\bar f=f_1^3$。
定义 $\mathcal S_K^{\mathrm{int}}=\mathcal S\times_{\mathcal O}\mathcal O_K$，并仍记基变换后的态射为 $f$。
基变换保持光滑、射影与平坦；这些是消费已接受模型的对应，不是把 properness 留为未证前提。
令
$$
\mathscr X_{c_1}=\mathcal S_K^{\mathrm{int}}
\times_{\mathbb P^1_{\mathcal O_K},\,c_1}\operatorname{Spec}\mathcal O_K,
\qquad X_{c_1}=\mathscr X_{c_1}\times_{\mathcal O_K}K.
$$
因此 $\mathscr X_{c_1}$ 为射影平坦的整模型，其泛纤维准确是原完整能级，
并且 $\mathscr X_{c_1}(\mathcal O_K)=X_{c_1}(K)$，这里的自然双射由 properness 的 DVR 赋值判据与 separatedness 给出。
本件不更换为谱曲线或 Jacobian 的另一原点模型。
因 $c_1\equiv0\pmod\pi$，其特殊纤维为 $3f_1^{-1}(0)$；有限原纤维与 $\mathcal D$ 不交。

### 1.2 Notation：准确原方程与全部可能图

固定辅助矩阵规范，记 $P=\operatorname{diag}(1,0)$，
$$
A(z)=A_0+zA_1+z^2P,
\quad A_0=\begin{pmatrix}1+x-xy&-x\\1+x-y-2xy+xy^2&x(y-1)\end{pmatrix},
$$
$$
A_1=\begin{pmatrix}y-x+x/y-1-1/x&1\\y-2x-1+xy+x/y-1/x&1\end{pmatrix}.
$$
在原环面上纤维方程准确为
$$
I_3(x,y):=\operatorname{tr}\{A(s^2)A(s)A(1)\}-2=c_1.
$$
在其余图上用此同一正则延拓，不另挑方程的无关分量。[BR] §2 和 [P30] 式 `geom:charts` 定位全部原末端邻域：

| 图 | 原坐标 | 含完整末端线的开邻域条件 |
|---|---|---|
| 环面 | $(x,y)$ | $x,y$ 可逆 |
| 1 | $x=u^{-1},\ y=1+uv$ | $1+uv$ 可逆；末端 $u=0$ |
| 2 | $x=u(1+uv),\ y=u^{-1}$ | $1+uv$ 可逆；末端 $u=0$ |
| 3 | $x=u(1+uv),\ y=u^2(1+uv)$ | $1+uv$ 可逆；末端 $u=0$ |
| 4 | $x=[u(s+uv)]^{-1},\ y=u^{-1}$ | $s+uv$ 可逆；末端 $u=0$ |

$\mathcal U=\mathcal S_K^{\mathrm{int}}\setminus\mathcal D$ 的几何点分层是环面及四条末端仿射线；
四条线本身不覆盖完整曲线，以上开邻域用于覆盖其整提升。
一旦列出特殊支撑 $f_1^{-1}(0)(\mathbb F_3)$ 的全部点，每个整提升须落在该点所属的环面图或末端开邻域，
因为 $\operatorname{Spec}\mathcal O_K$ 中含闭点的开集是全集。
图 1 的已接受限制仅为 $b_3(w)=-w^3+3w-3$、$(u,v)=(0,w+s^{-1})$，见 [L] Steps 1、2、4、6；不能用其无根代签全曲线无点。

### 1.3 方法前提、正负标准与投入边界

拟用原图中的精确代数恒等式、所有 $\mathbb F_3$ 约化点的有限完备分类及其整邻域的赋值／同余证书。
若用 Hensel，须明确在完备 DVR 上的实际方程和可逆偏导数，或核严格高阶 Hensel 不等式；不把奇异特殊点自动提升。
原有限曲线的光滑性可消费 [BR] T3：$\delta(c,1)=c^4-c^3-8c^2+36c-11$；
本例 $c_1\equiv0\pmod\pi$，故 $\delta(c_1,1)\equiv1\pmod\pi$，原泛纤维光滑。
不需要把原纤维转换为 degree-3 模型，也不调用 Fisher–Sills 算法的终止界。

有点证书必须给实际原点或严格原图提升；无点证书必须排除全部可能约化点的整个整邻域或给等价整体阻碍。
有限搜索未中、仅末端无根、Jacobian 有原点均不决定本题。
严格无点对应预定差异叙事的 `POSITIVE`；严格有点为该叙事的 `NEGATIVE`；缺口为 `INCONCLUSIVE`。
任何方向若只是标准局部证书，均触发 [DEC]／[DEVIL] 的短标准停止规则。
本件不求全盘能量像、$N_{\rm sol}$、参数分类或正式长文准入。

## 2. Status、Proof Strategy 与 Dependency Map

对象卡写入时：`NOT CURRENTLY JUSTIFIED`（本题尚未执行证书；不预定有／无点）。
完成后的作者状态：`PROVABLE AS STATED`，准确结论为
$$
\boxed{X_{-3+\pi^2}(\mathbb Q_3(\zeta_3))=\varnothing.}
$$
科学状态为 `PROVED (AUTHOR; INDEPENDENT CHECK PENDING)`；诊断信号为 `POSITIVE_FIXED_DIFFERENCE`。
与旧 $c_0$ 原点相比较得到固定原曲线的真实有点性差异；证明是短标准局部证书，投入处置为 `STOP_LONG_PAPER_STANDARD_CERTIFICATE`。

Dependency Map：

1. Step 1 消费已接受模型，列特殊支撑的全部五个剩余点；properness 将所有原 $K$ 点还原到五个整邻域。
2. Step 2 消费 [INT] §3.3／[G] G3 的原 $dI_3=3\alpha$（全部末端均包含），证明每个剩余邻域上能量模 $\pi^3$ 恒定。
3. Step 3 从同一原矩阵和四真实图计算五个代表的能量；没有用 Jacobian 或仅一条多截面替换它们。
4. Step 4 将五图必要同余与固定 $c_1$ 比较，得全曲线无点；不需要 Hensel 提升或通用算法终止界。

## 3. Proof

### Step 1. 特殊支撑恰有五点，且五个整邻域穷尽所有原点

记 $R=\mathcal O_K$、$k=\mathbb F_3$。原一阶能量是
$$
J=I_{1,1}(x,y;1)=y-x+x/y-1/x.
$$
这是将 $r=1$ 代入原矩阵迹得到的式子。环面上四个可能单位对的值为
$$
\begin{array}{c|rrrr}
(x,y)&(1,1)&(1,2)&(2,1)&(2,2)\\\hline
J&0&2&2&2
\end{array}
\quad\text{in }k.
$$
在约化后的四末端图里，令 $b=1+uv$；同一 $J$ 的精确正则表达为
$$
\begin{array}{c|c|c|c}
\text{图}&J\text{ 的图表达}&J|_{u=0}&J=0\text{ 的末端点}\\\hline
1&1+uv-u-v/b&1-v&(0,1)\\
2&v/b-ub+u^2b&v&(0,0)\\
3&v/b-ub+u^2b&v&(0,0)\\
4&(v+1)/b-ub&v+1&(0,-1)
\end{array}.
\tag{1}
$$
这里使用 $u^{-1}-(ub)^{-1}=v/b$ 消去表面上的极点；图 1 用它的负式。
图 2、3 的末端点虽然都写 $(0,0)$，但属于不同末端线，是两个不同点。
约化图 4 的 $b$ 是原整图分母 $s+uv$ 的约化，本件没有在原整图中把 $s$ 改成 $1$。

由于原有限纤维不交 $D$，而 $U_k$ 的点分层只有环面与四条末端线，(1) 与环面表给出恰好五点。
任取假设存在的 $P\in X_{c_1}(K)$，由对象卡的 properness 它唯一延拓到 $\mathscr X_{c_1}(R)$。
闭点像满足 $J^3=0$，在剩余域 $k$ 上等价于 $J=0$；三重特殊纤维不增加 $k$ 点。
因此整个整截面落在下表某一个开邻域内：含其闭点的开图逆像包含 $\operatorname{Spec}R$ 的闭点，故是整个局部谱。

| 邻域 | 精确的必要整坐标条件 | 选定的原 $R$-代表 $Q_i$ |
|---|---|---|
| $T$ | $x,y\in R^\times$，$x,y\equiv1\pmod\pi$ | $(x,y)=(1,1)$ |
| $1$ | $u\in\pi R$，$v\in1+\pi R$ | $(u,v)=(0,1)$ |
| $2$ | $u,v\in\pi R$ | $(u,v)=(0,0)$ |
| $3$ | $u,v\in\pi R$ | $(u,v)=(0,0)$ |
| $4$ | $u\in\pi R$，$v\in-1+\pi R$ | $(u,v)=(0,-1)$ |

这些图的分母自动为单位。所有邻域都允许 $u=0$；既没有删掉真正末端 $K$ 点，也没有只检查末端线上 $u=0$ 的点。
代表 $Q_i$ 是原曲面的整点，不预设在固定纤维上；它们用于比较整个剩余邻域的能量。

### Step 2. 整邻域上的三阶必要同余

消费已接受 [INT] §3.3：固定 $p=3,a=m=1,t=1$ 后，
$$
dI_3=3\alpha,\qquad \alpha\in\Gamma(\mathcal U,\Omega^1_{\mathcal U/R}),
\tag{2}
$$
该等式由原 $\mathcal O$ 模型平坦基变换到 $R$，并覆盖四条完整末端及其开邻域。
它不只是环面微分恒等式，也没有把 $3$-除法解释为临界理想的饱和。

**局部引理。** 在上述任一整开图，若正则函数 $g$ 满足 $dg\in3\Omega^1$，
两个整点 $P,Q$ 的坐标模 $\pi$ 相同，则
$$g(P)\equiv g(Q)\pmod{\pi^3}.\tag{3}$$

证明：以 $Q$ 的两个坐标平移为 $a,b$；图分母在 $Q$ 为单位，所以 $g$ 在此剩余邻域具有收敛的整形式幂级数
$$g=g(Q)+\sum_{i+j\ge1}e_{ij}a^ib^j,\qquad e_{ij}\in R.$$
因为 $dg\in3\Omega^1$，对每个 $i+j=1$ 或 $2$，至少一个非零的 $i,j$ 等于 $1$ 或 $2$，在 $R$ 中可逆。
比较相应偏导数的幂级数系数，得 $e_{ij}\in3R=\pi^2R$。
在 $P$ 处 $a,b\in\pi R$，故一次项属于 $\pi^3R$，二次项属于 $\pi^4R$；
总次数至少三的项属于 $\pi^3R$，其和在完备环 $R$ 中收敛。
这证明 (3)。此处没有假设积分求原函数可以除以 $3$，也没有从一阶导数控制忽略三次项。$\square$

由 (2)、(3)，Step 1 的任一 $P$ 必满足 $I_3(P)\equiv I_3(Q_i)\pmod{\pi^3}$。

### Step 3. 五个代表的准确原能量

下面先给可人工核验的短矩阵恒等式；CAS 只核转录，不承担全图覆盖或无限整邻域排除。
置 $J=y-x+x/y-1/x$，原矩阵满足
$$
\operatorname{tr}A_0=1,\quad\det A_0=0,\quad
\operatorname{tr}A_1=J,\quad\det A_1=x(1-y).
$$
展开三因子迹并将标量 $s$ 的幂按 $s^2+s+1=0$ 化简，得到
$$
I_3=J^3-3x(1-y)J
 +3s\operatorname{tr}(PA_0A_1)
 +3s^2\operatorname{tr}(PA_1A_0).
\tag{4}
$$
具体地，三因子中选出的 $z$ 次数总和不是 $3$ 的倍数时，循环迹的三个项带系数 $1,s,s^2$ 并相消。
总次数 $0,6$ 分别给 $\operatorname{tr}A_0^3=1$ 和 $\operatorname{tr}P^3=1$，由定义中的 $-2$ 消去。
总次数三包含 $(1,1,1)$ 和 $(0,1,2)$ 的六个排列；后六项按循环迹分为 (4) 的两个三倍项。
最后二阶矩阵 Cayley–Hamilton 给 $\operatorname{tr}A_1^3=J^3-3\det(A_1)J$，即 (4)。
这个推导在原能量标签下进行。

代入四个原图并取消可去的 $u$ 极点，得到完整末端多项式
$$
\begin{array}{c|l}
i&I_3|_{L_i}=b_i(v)\\\hline
1&-(v-s^2)^3+3(v-s^2)-3\\
2&v^3-3sv-3s^2\\
3&v^3-3v-3s\\
4&(v+s)^3-3(v+s)-3
\end{array}.
\tag{5}
$$
第一行与 [L] 的原 $b_3(w)$（$w=v-s^{-1}=v-s^2$）完全一致。
为额外说明后三行的代入为何保持原图，而非猜测同型多项式，可用 [P30] 极除子证明中的实际末端时间图复核：
源时间记作辅助符号 $t$ 时，前三条末端的目标坐标依次为 $st(1-sv)$、$sv$、$s(sv-t)/t$，目标时间为 $st$，且原 $I_3$ 不变。
将目标时间记为 $t'$，从第一行一般式 $-(v-s^2)^3+3t(v-s^2)-3t$ 依次代入得到
$$
b_2(v;t')=v^3/(t')^3-3sv-3s^2t',\quad
b_3(v;t')=v^3/(t')^3-3v-3st',\quad
b_4(v;t')=(v+s)^3-3t'(v+s)-3t'.
$$
例如第一步源坐标为 $s^2(1-v/t')$，第二步源坐标为 $s^2v$，第三步为 $t'(v+s)$；源时间均为 $s^2t'$。
取 $t'=1$ 正是 (5)。这些辅助符号仅校验固定图的限制，不另做其他参数的有点性诊断。

在环面代表 $(1,1)$，$J=0$、$\operatorname{tr}(PA_0A_1)=0$、$\operatorname{tr}(PA_1A_0)=-1$，故 $I_3(Q_T)=-3s^2$。
(5) 对其余代表给出
$$
\begin{array}{c|rrrrr}
Q_i&Q_T&Q_1&Q_2&Q_3&Q_4\\\hline
I_3(Q_i)&-3s^2&-3s&-3s^2&-3s&-3s^2
\end{array}.
\tag{6}
$$
因此五个值都满足
$$I_3(Q_i)\equiv-3\pmod{\pi^3},\tag{7}$$
因为 $s-1=\pi$、$s^2-1=\pi(s+1)$ 且 $3R=\pi^2R$。

### Step 4. 固定原纤维的全排除

若 $P\in X_{c_1}(K)$，Step 1 的 proper 延拓及五点完整覆盖、Step 2 的邻域引理与 (7) 联合给出
$$c_1=I_3(P)\equiv-3\pmod{\pi^3}.$$
但固定 $c_1=-3+\pi^2$ 满足 $v_\pi(c_1+3)=2$，不满足该同余。
矛盾。因此 $X_{c_1}(K)=\varnothing$。$\square$

等价算术核对是 $\pi^2=-3s$ 与 $c_1=3s^2$；本证明没有将 $c_1$ 偷换为另一个能量。
已知 $c_0=-3$ 的实际原点位于图 1 的 $(u,v)=(0,s^{-1})$；这里只引用旧接受事实作比较，不将其重新计为本件新结果。

## 4. Corrections or Missing Assumptions / Open Risks

本固定有点性任务没有剩余作者证明缺口；没有暗加分裂假设或改变曲线。
本件未证明完整能量盘的充分可解条件、准确像、最小决定精度、共同预定光滑紧盘或一般素数分类。
模 $\pi^3$ 的必要阻碍不是对原全盘 $N_{\rm sol}$ 的锐界；两固定值异可解也不自动代签该问题。
原特殊纤维具有三重结构；本证明没有将所有特殊点 Hensel 提升，也不需要把整纤维模型称为相对光滑。
后续针对本新增证书的独立检查由主控另行安排；作者自检及局部协助不是最终非作者接受。

## 5. 来源扣除与执行记录

本人 FULL 读取 [DEC]、[DEVIL]、[PA]、[S06]、[CD]，不继承这些件的外文 FULL 身份。
[S06] 与 [CD] 中 Fisher–Sills 全图递归、Hensel、局部常值、properness／紧致性均属标准机制；本诊断不重跑查新。
本件没有实际调用 Fisher–Sills 递归算法；其全图方法的已知性仍须扣除。
新增的对象级事实是固定原 $X_{c_1}$ 无点；实际证明只由旧整除微分、五点初等枚举和低阶 Taylor 同余组成。
因此虽是固定对真实整体差异的 `POSITIVE`，仍按事前规则停止以此标准实例为独立长文中心；不以补上 properness、加紧致性或重命名精度继续增厚。
本人 FULL 读取 `AGENTS.md`、`docs/WORKFLOW.md` 和 `proof-writer/SKILL.md`，批次入口只读 1–16 行。
原模型 [G] 1–100 行、[INT] §3.2／3.3、[BR] §2及 T1／T3、[P30] 原图／极除子段按需消费；[L] Steps 1、2、4、6 的原多截面公式按需消费。
合并输出中无关论文后段曾被截断，未对论文完整章节声明 FULL；实际依赖的原图及末端时间映射另定向读回。
只读子席 `reduction_coverage_check` 独立手算 (1) 和五邻域覆盖，未判定 $c_1$、未写文件、未看本席新增证明；其结果与本席一致。
它不是本完整证书的 fresh 非作者终审，更不是新意或容量票。
未动旧稿、索引、锁、PDF、外部状态；Papers27–30 接受、Batch07 为 4/5、P31 正文 22–30 页及正式双独审合同保持。

### 5.1 实际 CAS 命令及支持范围

对象卡成功写入后，实际执行两次本地内联 SymPy 命令，无脚本文件、无 GPU、无数值点搜索。
第一次直接展开原矩阵并查看四末端限制；其中 `b(1)` 是统一诊断值，不误当作全部代表的值，真正代表按第二次的 $1,0,0,-1$ 核对。

```bash
python - <<'PY'
import sympy as S
x,y,z,s=S.symbols('x y z s')
A0=S.Matrix([[1+x-x*y,-x],[1+x-y-2*x*y+x*y**2,x*(y-1)]])
A1=S.Matrix([[y-x+x/y-1-1/x,1],[y-2*x-1+x*y+x/y-1/x,1]])
A=A0+z*A1+z**2*S.diag(1,0)
def red(e):
    n,d=S.fraction(S.cancel(e))
    return S.cancel(S.rem(n,s*s+s+1,s)/d)
M=(A.subs(z,s*s)*A.subs(z,s)*A.subs(z,1)).applyfunc(red)
I=red(S.trace(M)-2)
print('I3 =',S.expand(I))
print('I3(1,1) =',red(I.subs({x:1,y:1})))
u,v=S.symbols('u v')
charts=[(1/u,1+u*v),(u*(1+u*v),1/u),(u*(1+u*v),u*u*(1+u*v)),(1/(u*(s+u*v)),1/u)]
for j,(xx,yy) in enumerate(charts,1):
    J=S.cancel(I.subs({x:xx,y:yy},simultaneous=True))
    n,d=S.fraction(J)
    n=S.rem(n,s*s+s+1,s)
    d=S.rem(d,s*s+s+1,s)
    J=S.cancel(n/d)
    b=red(J.subs(u,0))
    print('chart',j,'b(v) =',S.factor(b))
    print('chart',j,'b(1) =',red(b.subs(v,1)))
PY
```

命令成功退出，原环面代表输出为 `3*s + 3`，四个多项式与 (5) 等价。
此处前段 `red` 的分母只含 $x,y$，末端段已分别约化分子／分母；所有运算均在 $\mathbb Q(s)(x,y)$ 或相应原图函数域进行。
这些有限恒等式输出本身不证明无点，故没有将 CAS 正常退出当作科学验收。

第二次核 (4) 残差、四图 (5) 残差、五个正确代表及固定能量恒等式，实际完整命令为：

```bash
python - <<'PY'
import sympy as S
x,y,z,s,u,v=S.symbols('x y z s u v')
P=S.diag(1,0)
A0=S.Matrix([[1+x-x*y,-x],[1+x-y-2*x*y+x*y**2,x*(y-1)]])
A1=S.Matrix([[y-x+x/y-1-1/x,1],[y-2*x-1+x*y+x/y-1/x,1]])
A=A0+z*A1+z*z*P
phi=s*s+s+1
def red(e):
    n,d=S.fraction(S.cancel(e))
    return S.cancel(S.rem(n,phi,s)/S.rem(d,phi,s))
J=y-x+x/y-1/x
C=J**3-3*x*(1-y)*J+3*s*S.trace(P*A0*A1)+3*s*s*S.trace(P*A1*A0)
raw=S.trace(A.subs(z,s*s)*A.subs(z,s)*A.subs(z,1))-2
print('matrix identity residual:',red(raw-C))
I=red(C)
coords=[(1/u,1+u*v),(u*(1+u*v),1/u),(u*(1+u*v),u*u*(1+u*v)),(1/(u*(s+u*v)),1/u)]
claims=[-(v-s*s)**3+3*(v-s*s)-3,v**3-3*s*v-3*s*s,v**3-3*v-3*s,(v+s)**3-3*(v+s)-3]
values=[1,0,0,-1]
for i,((xx,yy),claim,v0) in enumerate(zip(coords,claims,values),1):
    expr=red(I.subs({x:xx,y:yy},simultaneous=True))
    b=red(S.cancel(expr).subs(u,0))
    print('terminal',i,'identity residual:',red(b-claim),'representative value:',red(b.subs(v,v0)))
print('torus representative:',red(I.subs({x:1,y:1})))
pi=s-1
c1=-3+pi*pi
print('c1 - 3s^2 residual:',red(c1-3*s*s))
print('pi^2 + 3s residual:',red(pi*pi+3*s))
PY
```

实际输出（退出码 0）：

```text
matrix identity residual: 0
terminal 1 identity residual: 0 representative value: -3*s
terminal 2 identity residual: 0 representative value: 3*s + 3
terminal 3 identity residual: 0 representative value: -3*s
terminal 4 identity residual: 0 representative value: 3*s + 3
torus representative: 3*s + 3
c1 - 3s^2 residual: 0
pi^2 + 3s residual: 0
```

它支持本件 (4)–(6) 的有限原坐标恒等式，不承担 Step 1 的完整性、Step 2 的无限邻域引理或新意判断。
本件写后由作者 FULL 读回，并执行定向的直接本地引用存在性检查、`wc -l` 与 `sha256sum`；终态行数／SHA 交主控，不把自哈希写入本件造成循环。

[DEC]: PAPER31_QPI_POST_CLOSED_IDEA_REPORT_V1_20260912.md
[DEVIL]: PAPER31_QPI_POST_CLOSED_DEVILS_ADVOCATE_V1_20260912.md
[PA]: PAPER31_QPI_POST_CLOSED_SURVIVOR_CLAIMS_PHASE_A_V1_20260910.md
[S06]: PAPER31_QPI_POST_CLOSED_DEEP_SOURCES_N06_V1_20260910.md
[CD]: PAPER31_QPI_POST_CLOSED_NOVELTY_CD_N06_N10_V1_20260910.md
[INT]: PAPER30_QPI_INTEGRAL_MATHEMATICS_DISPOSITION_V1_20260909.md
[G]: PAPER30_QPI_CYCLOTOMIC_GLOBAL_MODEL_DIAGNOSTIC_V1_20260909.md
[BR]: PAPER30_QPI_CANDIDATE_BRIEF_V2_20260909.md
[P30]: ../../papers/30-qpi-vertical-critical-ideals/paper/v4/sections/02-surface-pencil.tex
[L]: PAPER30_QPI_TORSOR_MULTISECTION_DIAGNOSTIC_V1_20260909.md
