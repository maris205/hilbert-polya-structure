# Paper30 qPI P03：$p=3,a=2$ 第一末端点的双状态精确诊断 V1

日期：2026-09-09。类型：有界作者诊断／有限精确恒等式，待非作者核查。
只取 $p=3,a=2,m=1,N=9$，$t\in\{1,q\}$，且只研究原第一末端图在 $u=v=0$ 的点评价和有限局部 jet。
此前所有作者件、检查及脚本均冻结，不作修改。

## Claim

令
$$\mathcal O=\mathbb Z[\zeta_9]_{(\zeta_9-1)},\qquad q=\zeta_9=1+\pi,
\qquad \Phi_9(q)=q^6+q^3+1=0.$$
第一末端图及相关函数固定为
$$x=u^{-1},\quad y=W=1+uv,\quad J_t=W-v/W-tu.$$
取 $t=t_\delta=1+\delta\pi$、$\delta\in\{0,1\}$，记
$$\alpha_9=\frac19d_{\mathrm{state}}I_9=A_u\,du+A_v\,dv.$$
在 $P_0:(u,v)=(0,0)$ 的完成局部环 $\widehat{\mathcal O}[[u,v]]$ 中令
$$\mathfrak m=(\pi,u,v),\qquad S=u+v,\qquad
T=A_u(J_t)_v-A_v(J_t)_u.$$
$T$ 是 $\alpha_9\wedge dJ_t=T\,du\wedge dv$ 的系数，不是预先把一个状态方向置零所得的导数。

**H2.1（准确点评价）。** 以下均为 $\mathcal O$ 中的精确等式：
$$\begin{aligned}
A_u(P_0;t=1)&=-3\pi^5-13\pi^4-21\pi^3-20\pi^2-18\pi-9,\\
A_v(P_0;t=1)&=-\pi^5-3\pi^4+\pi^2-9\pi-3,\\
A_u(P_0;t=q)&=-15\pi^5-63\pi^4-114\pi^3-116\pi^2-66\pi-24,\\
A_v(P_0;t=q)&=-11\pi^5-48\pi^4-97\pi^3-113\pi^2-66\pi-27.
\end{aligned} \tag{1}$$
每个系数的 $\pi$ 赋值都准确为二，故两种提升的点上完整系数理想均为 $(\pi^2)\subset\mathcal O$。
这里的 $(\pi^2)$ 只是沿指定零截面评价后的理想，不是保留两个状态方向的完成局部环中的理想。

**H2.2（首齐次 jet 与切向阶）。** 在 $\operatorname{gr}_{\mathfrak m}\cong\mathbb F_3[\pi,u,v]$ 中，
$$\operatorname{in}_2(\alpha_9)=\pi^2(du+dv),\qquad
\alpha_9\in\mathfrak m^2\Omega^1\setminus\mathfrak m^3\Omega^1. \tag{2}$$
其零阶和一次齐次 jet 全为零。
切向系数 $T$ 的零至三次齐次项全为零，而
$$\operatorname{in}_4(T)=(1+\delta)\pi^4+2\pi^3u+\pi^3v+2\pi S^3. \tag{3}$$
特别地，两提升的 $v_\pi(T(P_0))$ 都准确为四，四阶首常数分别为一与二。

**H2.3（只到四阶的初始理想信息）。** 令 $I=(A_u,A_v)$ 为完整双状态系数理想，并令
$$L_\delta=(1+\delta)\pi^2+2\pi u+\pi v.$$
因为 $(J_t)_u$ 在本完成局部环为单位，确有两个实际生成元
$$I=(A_u,\ T-L_\delta A_u). \tag{4}$$
它们的最低齐次式分别为 $\pi^2$ 和 $2\pi S^3$。因此
$$\bigl(\operatorname{in}_{\mathfrak m} I\bigr)_d
=\bigl(\pi^2,\pi S^3\bigr)_d\quad(0\le d\le4). \tag{5}$$
这里下标表示指定齐次度的部分。**不声称**完整的初始理想就是 $(\pi^2,\pi S^3)$，也不声称 $I=(\pi^2,\pi S^3)$。

## Status

PROVABLE AS STATED（上述有限点评价与局部 jet；作者计算与证明完成，待独立核查）。
完整局部初始理想、完整零概形、其他状态点及全高度结论均不在本件已证明内容中。

## Assumptions and Input Boundary

1. 原矩阵、因子次序与原 $I_9$ 不更换，微分只作用于 $u,v$，不作用于 $q,t$。
2. 使用第一末端图的正则 gauge 矩阵
   $$\widehat A(Z)=M_0+ZM_1+Z^2M_2,$$
   $$M_0=\begin{pmatrix}t-v&-1\\-v(t-v)&v\end{pmatrix},\qquad
   M_1=\begin{pmatrix}J_t-1&u\\v-t+v^2/W&1\end{pmatrix},\qquad M_2=\operatorname{diag}(1,0). \tag{6}$$
   该图保留整条 $u=0$ 的末端仿射线，但本文诊断仅在其 $\bar J=1$ 的交点 $u=v=0$。
3. 原谱乘积及循环插入识别给出
   $$\alpha_9=[Z^9]\operatorname{tr}\!\left(d\widehat A(Z)
       \widehat A(q^8Z)\widehat A(q^7Z)\cdots\widehat A(qZ)\right). \tag{7}$$
   Step 1 说明九个插入项的规范化；本件不重新证明该 gauge 与原完整 qPI 模型的全图接口。
4. 不将已冻结 height-one 的 $(\pi,H)$ 理想推广到此高度，也不把已知首 $\pi$ 切向 jet 消失当作更高阶结果。
5. 唯一辅助代码是同前缀的[有限精确脚本](PAPER30_QPI_VERTICAL_ALPHA_P3_HEIGHT2_PROBE_V1_20260909.py)。
   它不展开 $I_9$，也没有操作其他旧脚本。

## Notation

式 (1) 的整数系数和 $\pi$ 幂是混合特征环中的精确表达。
凡标为齐次 jet 或模 $\mathfrak m^r$ 的后续公式，其系数先约化到 $\mathbb F_3$；仍以 $\pi,u,v$ 记三个关联分次变量。
$O(\mathfrak m^r)$ 表示真实局部系数属于 $\mathfrak m^r$，不是浮点误差。
“切向”只指 (3) 中楔 $dJ_t$ 的商方向；原 $A_u,A_v$ 始终一并保留。

## Proof Strategy and Dependency Map

1. 圆分关系精确给 $v_\pi(3)=6$，从而总阶至五的计算可在 $\mathbb F_3[\pi,u,v]/(\pi,u,v)^6$ 内完成。
2. 对 (7) 做八因子的有序系数递推；在点上分别插入两个明确导数矩阵，得到 (1)。
3. 在同一递推中保留有限状态 jet，得到双系数至四阶的完整公式；再楔实际 $dJ_t$ 得到 (3)。
4. 用 $(J_t)_u$ 为单位作真实生成元变换，然后只判定初始理想的零至四阶部分，不越过有限截断范围。

## Proof

### Step 1. 圆分精度、正则性与插入规范化

直接展开 $\Phi_9(1+\pi)=0$ 得
$$\pi^6+6\pi^5+15\pi^4+21\pi^3+18\pi^2+9\pi+3=0,$$
即
$$3=-\pi^6/(1+3\pi+6\pi^2+7\pi^3+5\pi^4+2\pi^5). \tag{8}$$
括号内为单位，故 $v_\pi(3)=6$。
于是完成局部环模 $\mathfrak m^6$ 恰可写为
$$\mathbb F_3[\pi,u,v]/(\pi,u,v)^6,$$
没有更低阶的额外圆分关系。
矩阵 (6) 的所有分母只是 $W=1+uv$，在该局部环为单位。

对原九因子乘积作状态微分会得到九个插入项。
把任一插入项作迹的循环移位，再整体替换谱变量 $Z\mapsto q^jZ$，即可移到 (7) 的位置；
$[Z^9]$ 仅乘 $q^{9j}=1$，故九个系数相同。
所以先在特征零除以九后正是 (7)，没有在特征三中除以零，也没有交换不相邻矩阵。

### Step 2. 点上的有限精确证书

在 $P_0$，有 $J_t=1$、$(J_t)_u=-t$、$(J_t)_v=-1$，故
$$M_0(P_0)=\begin{pmatrix}t&-1\\0&0\end{pmatrix},\quad
M_1(P_0)=\begin{pmatrix}0&0\\-t&1\end{pmatrix},\quad M_2(P_0)=\begin{pmatrix}1&0\\0&0\end{pmatrix}.$$
两个完整状态插入为
$$\partial_u\widehat A(P_0;Z)=Z\begin{pmatrix}-t&1\\0&0\end{pmatrix},$$
$$\partial_v\widehat A(P_0;Z)=\begin{pmatrix}-1&0\\-t&1\end{pmatrix}
      +Z\begin{pmatrix}-1&0\\1&0\end{pmatrix}. \tag{9}$$

以下递推是点结果和状态 jet 共用的有限代数证书。
令 $P^{(0)}_0=I_2$，其他 $P^{(0)}_j=0$，对 $r=0,\ldots,7$ 定义
$$P^{(r+1)}_j=\sum_{\ell=0}^2
       P^{(r)}_{j-\ell}\,q^{(8-r)\ell}M_\ell,
       \qquad 0\le j\le9, \tag{10}$$
负指标取零。这恰是从右侧依序乘上 $\widehat A(q^{8-r}Z)$ 的卷积，不会改变因子顺序。
令 $P_j=P^{(8)}_j$，则
$$A_u(P_0)=\operatorname{tr}\!\left(\begin{pmatrix}-t&1\\0&0\end{pmatrix}P_8\right),$$
$$A_v(P_0)=\operatorname{tr}\!\left(\begin{pmatrix}-1&0\\-t&1\end{pmatrix}P_9
       +\begin{pmatrix}-1&0\\1&0\end{pmatrix}P_8\right). \tag{11}$$
只需 $Z$ 的零至九次系数；更高次不可能回流到所求系数。

为使 (1) 的整数系数还有一个可直接复核的中间证书，(10)–(11) 在 $\mathbb Z[q,t]/(q^6+q^3+1)$ 中给出
$$\begin{aligned}
A_u(P_0)=-t\bigl(&4q^5t^3-q^5t^2-2q^4t^3+2q^3t^3-3q^3t^2-q^2t^3+6q^2t^2\\
 &+5qt^3-7qt^2+6qt+t^4-3t^3+2t^2-t+1\bigr),
\end{aligned} \tag{12}$$
$$\begin{aligned}
A_v(P_0)={}&q^5t^3-2q^5t^2-5q^4t^3+7q^4t^2+7q^3t^3-6q^3t^2+q^3t\\
 &-4q^2t^3+3q^2t^2-6q^2t-3qt^3-q-t^4+5t^3+t^2.
\end{aligned} \tag{13}$$
这些式子也可不用矩阵软件而以四个标量多项式核查：若当前乘积为 $\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)$，右乘点矩阵的第 $k$ 个因子时更新为
$$\begin{aligned}
a'&=(t+q^{2k}Z^2)a-tq^kZb,& b'&=-a+q^kZb,\\
c'&=(t+q^{2k}Z^2)c-tq^kZd,& d'&=-c+q^kZd.
\end{aligned}$$
然后 (11) 分别读取 $-t a_8+c_8$ 及 $-a_9-tb_9+d_9-a_8+b_8$。
将 $t=1,q$ 代入 (12)–(13)，约去 $\Phi_9(q)$ 后代入 $q=1+\pi$，就得到 (1)。

由 (8)，每个非零整数系数 $n$ 满足 $v_\pi(n)=6v_3(n)$。
在 (1) 的四个多项式中，唯一最低赋值项都是 $\pi^2$ 项，系数模三均为一，所以赋值准确为二。
另由 $T(P_0)=tA_v(P_0)-A_u(P_0)$ 得精确值
$$\begin{aligned}
T(P_0;t=1)&=2\pi^5+10\pi^4+21\pi^3+21\pi^2+9\pi+6,\\
T(P_0;t=q)&=22\pi^5+83\pi^4+135\pi^3+135\pi^2+72\pi+30.
\end{aligned} \tag{14}$$
这两个值的最低赋值项分别是 $10\pi^4$ 与 $83\pi^4$，准确赋值均为四。

### Step 3. 完整双状态的有限 jet

在 (10) 中保留原正则矩阵 (6)，把 $W^{-1}$ 展成
$$W^{-1}=1-uv+u^2v^2-u^3v^3+\cdots.$$
先把矩阵保留到比所需导数多一阶的状态总次数，再微分；不能先丢掉会经微分下降到目标精度的项。
由 (8)，对总阶至五的所有输出都可逐项在特征三中实施这一递推。
具体地，脚本先保留矩阵状态／$\pi$ 总阶至六，微分后截到五，再对八因子做 (10)；
整数三倍项的 $\pi$ 阶至少六，即使状态微分也不会降到所求五阶内。

得到如下模 $\mathfrak m^5$ 的两个完整系数，所有右端系数均在 $\mathbb F_3$ 中解释：
$$\begin{aligned}
A_u={}&\pi^2+\pi^2u\\
 &+2(1-\delta)\pi^4+\pi^3u+\pi^2vS+\delta\pi S^3+2S^4
 +O(\mathfrak m^5),\\
A_v={}&\pi^2+\pi^2v+2\delta\pi^3\\
 &+(1+\delta)\pi^3v+2\pi^2uS+2(1-\delta)\pi S^3+2S^4
 +O(\mathfrak m^5).
\end{aligned} \tag{15}$$
其中第一行最低项为二次，紧随的一次状态倍数和 $2\delta\pi^3$ 为三次，余下显示项均为四次。
$S^3=u^3+v^3$、$S^4=u^4+u^3v+uv^3+v^4$ 都是特征三中的准确展开。
式 (10)、矩阵 (6) 与插入 $\partial_uM_\ell,\partial_vM_\ell$ 构成 (15) 的有限卷积证书；辅助脚本逐个输出零至五阶，包含比 (15) 多一阶的可复算余项检查。

式 (15) 证明 (2)，也直接展示纯状态四阶项 $2S^4$：它不能被点上的 $\pi^2$ 公共因子取代。
为计算 $T$，只需原状态导数至二阶：
$$ (J_t)_u=-1-\delta\pi+v+v^2+O(\mathfrak m^3),\qquad
(J_t)_v=-1+u+2uv+O(\mathfrak m^3).$$
更高导数项乘 $A_u,A_v\in\mathfrak m^2$ 后不影响四阶结果。
把 (15) 代入 $T=A_u(J_t)_v-A_v(J_t)_u$，二次与三次项分别相消，余下四次项恰为 (3)。
这也独立复核 (14) 在 $u=v=0$ 的首四阶。

### Step 4. 实际生成元变换及其可证明的边界

在本完成局部环，$(J_t)_u\equiv-1\pmod{\mathfrak m}$ 为单位。
由 $A_v=(A_u(J_t)_v-T)/(J_t)_u$，得到 $I=(A_u,T)$；再作一次三角生成元变换，即为 (4)。
由 (3)、$\operatorname{in}_2(A_u)=\pi^2$，确有
$$\operatorname{in}_4(T-L_\delta A_u)=2\pi S^3.$$
这并不是把原状态一形式拉回一维能级，而是在同一个二生成元理想内作可逆操作。

下面只证明 (5)。记 $F=A_u$、$G=T-L_\delta A_u$，则 $\operatorname{ord}_{\mathfrak m}F=2$、$\operatorname{ord}_{\mathfrak m}G=4$。
对任意 $aF+bG$，若 $a$ 的首阶为零或一，则其二／三次首式是 $\pi^2$ 的倍数，不能被从四阶才开始的 $bG$ 消去。
若其最低阶不小于四，则 $a\in\mathfrak m^2$，四次项必为
$$\pi^2 a_2+2b_0\pi S^3,$$
其中 $a_2$ 是 $a$ 的二次齐次项、$b_0$ 是 $b$ 的常数剩余项。
反向包含由 $F,G$ 及其低阶倍数给出。因此零至四次齐次部分正是 (5)。
更高阶组合可能取消这两个首式并产生新的初始生成元；本文没有计算足够信息来排除它们。
H2.1–H2.3 证毕。

## Interpretation and Explicit Nonclaims

- 在指定点，两提升的完整双系数公共 $\pi$ 阶从 height-one 诊断中的一变为二；本件只是两份独立有限计算之间的比较，不是全高度递推定理。
- 同一点的切向楔积到 $\pi^4$ 才非零；两提升的四阶首常数不同。该方向信息不等于两个完整局部零概形具有不同厚度。
- 真正的首齐次式是 $\pi^2(du+dv)$，而非凭 height-one 外推得到的 $\pi(du+dv)$。
  同时，(15) 的纯状态四阶项说明 $\alpha_9$ 在完整局部环中并不被 $\pi^2$ 整除。
- (4) 是准确的实际二生成元表示；(5) 是截断初始理想信息。未声称完整初始理想、完整形式正规形、沿全部 $X$ 的常厚度或其他末端点的结果。
- 不把本件推广到 $a>2$、其他素数、$m>1$、其他 Hasse 根或奇异能级。任何更广的迭代解释仍只是待独立证明的线索。

## Actual Verification and Open Risks

- 按 proof-writer 完整区分精确 Claim、输入、有限递推证明和未完成范围。
- 新辅助脚本的点计算使用 $\mathbb Z[q,t]/\Phi_9(q)$；状态 jet 使用不同的截断表示 $\mathbb F_3[\pi,u,v]/\mathfrak m^6$。
  脚本断言两种表示在点上的零至五阶输出完全一致，包括 $T$；不使用浮点数。
- 本件只做当前有限恒等式的作者验证，不启动未来的证明审查或泛化任务。没有展开高次 $I_9$，没有调用 GPU。
- 唯一新产物是本文件及同前缀 `.py`；未修改任何已冻结作者件、检查或旧脚本。
- 待非作者核查的重点是有序递推 (10)、两导数插入 (9)、精确点多项式 (12)–(14) 及混合特征截断精度。
- 高阶 syzygy 对完整初始理想的影响尚未判断；点理想 $(\pi^2)$ 不可替代这一缺口。未评分、立项、建锁、写稿或承诺论文。
