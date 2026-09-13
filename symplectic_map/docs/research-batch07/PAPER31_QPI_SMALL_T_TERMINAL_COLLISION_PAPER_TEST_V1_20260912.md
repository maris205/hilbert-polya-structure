# Paper31：正T趋零的三阶共振与terminal碰撞纸面测试 V1

日期：2026-09-12 UTC。作者：`/root`，并行纸核 `p31_small_t_resonance_interface`。
状态：作者有界证明；非正式候选、非论文准入。新问题来自 `p31_post_ramification_question_inventory`。
研究对象始终是原 $T>0$ 自治离散映射；零参数只作内部极限，不执行负T、非自治或独立连续流项目。

## 1. Claim / Assumptions / Status

令 $T=\varepsilon^3>0$、$x=\varepsilon^2X$、$y=\varepsilon Y$、$h=\varepsilon H$。
本件证明三个有界事实：

1. 原三步映射在任意固定紧torus域上有统一的一阶近恒等展开，含其torus内极限acnode点。
2. 缩放Weierstrass族有显式三阶扭点退化；持续实圆的旋转缺陷在acnode附近可一致短算。
3. **若极限模型要求两个碰撞terminal截面保持不同极限点，则三步映射不可能在该模型上一致趋恒等。**

三项作者状态 `PROVABLE AS STATED`，独立接受另定。第3项是条件性不可能结论，
不声称所有极限模型不存在，不否定允许截面合并的模型或非恒等边界离散正常形。
普通有限慢时间极限与短拓扑反例不能自动组成22–30页独立中心。

## 2. Notation / Strategy / Dependencies

$f_\varepsilon$ 为上述缩放共轭，$g_\varepsilon=f_\varepsilon^3$。
$\Omega=dX\wedge dY/(XY)$ 为二维辛形式；$\omega_{\varepsilon,H}$ 为纤维不变微分，
$\mathcal P_\varepsilon(H)>0$ 为其定向实完整周期，避免二者记号混同。
策略：直接三次复合；原[G]显式坐标缩放；弦切法计算 $3P$；持续圆的紧参数化；
最后只用 $g_\varepsilon(-2P)=P$ 和两个截面的不同极限给出拓扑反例。
旧[G]只消费实际+P、四terminal字典及持续圆参数化；不重复其完整几何新意。

## 3. Exact map and the compact-chart expansion

直接代入原式得
$$f_\varepsilon(X,Y)=\left(\frac1{\varepsilon X-Y},\frac XY\right),\qquad
H_\varepsilon=Y+X/Y-1/X-\varepsilon X.$$
$f_\varepsilon$ 保持 $H_\varepsilon$ 与 $\Omega$。
在 $XY\ne0$ 上
$$f_0=(-1/Y,X/Y),\qquad f_0^2=(-Y/X,-1/X),\qquad f_0^3=(X,Y).$$
写 $A=\varepsilon X-Y$、$B=XY+\varepsilon(Y-X^2)$，直接逐次代入还给
$$f_\varepsilon^2=\left(\frac{YA}{B},\frac{Y}{XA}\right),\qquad
g_\varepsilon=\left(\frac{XAB}{Y(\varepsilon XA^2-B)},\frac{XA^2}{B}\right).$$
这些式子的 $\varepsilon=0$ 分母在任意紧 $K\subset\{XY\ne0\}$ 上有正下界。
对 $\varepsilon$ 展开并对任意固定阶坐标导数求导，得到
$$g_\varepsilon=\operatorname{id}+\varepsilon V+O_{K,C^r}(\varepsilon^2),\qquad
V=(XY-X^2/Y,-X-Y/X),\quad r\ge0.$$
两坐标的一阶系数可由上面商式求导直接验证。
又
$$\iota_V\Omega=\left(\frac1Y+\frac1{X^2}\right)dX+
\left(1-\frac X{Y^2}\right)dY=dH_0.$$
这里的Hamiltonian符号约定已显式固定，不以不同惯例改变一阶符号。

若初始紧集的 $V$ 轨道在固定慢时间 $0\le t\le L$ 内留在一个紧torus域的内部，
则 $g_\varepsilon^k$ 与该流在 $k\varepsilon\le L$ 上的误差为 $O(\varepsilon)$。
证明：流的一步Taylor误差也是 $O(\varepsilon^2)$；在该紧域 $V$ 的Lipschitz常数为 $M$，
误差满足 $e_{k+1}\le(1+M\varepsilon)e_k+C\varepsilon^2$，求和为
$e_k\le C_L\varepsilon$。先取带正余量的紧邻域，再用此界归纳确保离散轨道未离域。
这只是Euler一致性与离散Gronwall，不是新长时理论；不覆盖任意增长的 $L$。

## 4. Scaled elliptic family and the true three-step displacement

在旧原Weierstrass坐标置 $u=\varepsilon^2U,v=\varepsilon^3W$，得到
$$\mathcal E_{\varepsilon,H}:\ W^2+HUW-W=U^3-\varepsilon U^2,\qquad P=(0,1).$$
原torus到该族的式子为
$$U=1/Y,\qquad W=X(\varepsilon Y-1)/Y^2.$$
原四terminal的标记为
$$O,\quad -P=(0,0),\quad P=(0,1),\quad Q=-2P=(\varepsilon,1-\varepsilon H),$$
另 $2P=(\varepsilon,0)$。在 $\varepsilon=0$ 光滑纤维，$P$ 的切线 $W=1-HU$
与曲线三重交于 $P$，故 $3P=O$ 且 $P\ne O$，准确阶三。
当 $\varepsilon\ne0$，连结 $P$ 与 $2P$ 的直线斜率 $-1/\varepsilon$；弦切公式给
$$3P=\left(\frac{1-\varepsilon H}{\varepsilon^2},
\frac{(1-\varepsilon H)^2}{\varepsilon^3}\right).$$
在 $O$ 的正规参数 $z=-U/W$ 因而为
$$z(3P)=-\frac{\varepsilon}{1-\varepsilon H}=-\varepsilon+O(\varepsilon^2).$$
$\omega_{\varepsilon,H}=dU/(2W+HU-1)=(1+O(z))dz$ 在 $O$ 邻域解析，
故局部Abel位移 $\delta_\varepsilon(H)=\int_O^{3P}\omega_{\varepsilon,H}
=-\varepsilon+O(\varepsilon^2)$，对有界 $H$ 一致。
这也与 $\omega_{0,H}(V)=-1$ 相符；不是仅凭“近恒等”猜测位移方向。

## 5. Acnode: what is actually uniform

令 $a(\varepsilon)>0$ 为 $a^3(1+\varepsilon a)=1$ 在 $a(0)=1$ 附近的解析根。
原固定点缩放后为 $(X_c,Y_c)=(a^2,-a)$，坏值
$$H_c=-3a-2\varepsilon a^2=-3-\varepsilon+O(\varepsilon^2).$$
$(1,-1)$ 在torus内部；$DV$ 在此点为
$\left(\begin{smallmatrix}1&2\\-2&-1\end{smallmatrix}\right)$，特征值 $\pm i\sqrt3$。
因此第3节的局部映射展开可包含该点，不存在仅由acnode名称引起的局部Euler障碍。

完成平方写 $Z=W+(HU-1)/2$，则
$$Z^2=U^3+(H^2/4-\varepsilon)U^2-HU/2+1/4.$$
在 $(\varepsilon,H)=(0,-3)$，右侧为 $(U+1)^2(U+1/4)$。
simple root $r=-1/4$ 与node $U=-1$ 正分离。写右侧 $(U-r)G(U)$，
用 $U=r+s^2,Z=s\sqrt{G(r+s^2)}$、$s\in\mathbb{RP}^1$ 参数化持续identity圆。
对充分小的固定参数矩形，$G$ 在这条圆上保持正；无穷图用 $1/s$。
故该圆、其非零微分以及完整周期 $\mathcal P_\varepsilon(H)$ 解析，周期正且有统一下界。
在中心 $\mathcal P_0(-3)=\int_{-\infty}^{\infty}ds/(s^2+3/4)=2\pi/\sqrt3$。

取与原已接受实角一致的提升 $\rho_\varepsilon(H)$；在acnode边界原角
$1/2+\pi^{-1}\arctan(1/\sqrt{3+4\varepsilon a})$ 趋于 $2/3$，固定其整数枝。
群加法因而给 $3\rho_\varepsilon-2=\delta_\varepsilon/\mathcal P_\varepsilon$，于是
$$\frac{\rho_\varepsilon(H)-2/3}{\varepsilon}
=-\frac1{3\mathcal P_0(H)}+O(\varepsilon)$$
在该矩形一致。奇异能级仅在持续光滑圆定义这个角；正则时第二圆的平移角相同。
这不提供收缩oval的统一角坐标，更不声称含孤立node的整条坏纤维是圆。
有限参数矩形内的这个标量缺陷同样是短消费者，不能笼统登记为一个未闭合长文难题。

## 6. The separated-terminal obstruction

在 $(\varepsilon,U,W-1)=(0,0,0)$ 碰撞中心的 $\varepsilon$-chart置
$$U=\varepsilon\xi,\qquad W=1+\varepsilon\zeta.$$
约去曲面方程公共因子后为
$$ (\zeta+H\xi)(1+\varepsilon\zeta)=\varepsilon^2\xi^2(\xi-1).$$
在 $\varepsilon=0$，该图的边界为 $\zeta=-H\xi$；两个截面的极限分别是
$$P_0:(\xi,\zeta)=(0,0),\qquad Q_0:(\xi,\zeta)=(1,-H).$$
它们不同，而准确原动力恒等式始终是 $g_\varepsilon(Q_\varepsilon)=P_\varepsilon$。

因此在任何Hausdorff极限模型中，只要这两个截面趋向不同点，且所声称的
一致近恒等足以使 $d(g_\varepsilon z,z)\to0$ 对这两个截面成立，就必有矛盾：
$$d(P_\varepsilon,Q_\varepsilon)
=d(g_\varepsilon Q_\varepsilon,Q_\varepsilon)\longrightarrow0,$$
但左侧趋向 $d(P_0,Q_0)>0$。等价地，联合连续极限 $g_0=\operatorname{id}$ 迫使 $P_0=Q_0$。
这是拓扑性的条件反例，对诱导该拓扑的任意固定度量成立，不是选取发散度量制造的障碍。
形式边界位移也与 $\xi\mapsto\xi-1$ 相符；本反例只需截面恒等式，不依赖全图提升已构造。

## 7. Corrections / Open risks / Disposition

强目标“保terminal分离并全域一致近恒等”已被上述短反例排除。
第3–5节不构成该强目标的弱化后准入；弱版只保存为明确的研究资产。
允许标记合并的模型、非恒等边界层与内部流的匹配、增长时间及外匹配区域仍未构造完整理论。
不得将其未证自动视为高新颖性、正文容量或下一篇立项依据；若再研究，先提出准确且不同的匹配命题。
本件没有把原 $T>0$ 的合法terminal删去：碰撞只是所研究的参数极限现象。
没有数值、CAS、N扫描、试排、PDF或外部效力。

[G]: PAPER31_QPI_REAL_COMPONENT_RETURN_GEOMETRY_V1_20260912.md
