# Paper31：正域 QRT 新接口独立数学审查 V1

日期：2026-09-13 UTC。审查者：`/root/p31_real_positive_qrt_interface_check`；被审稿作者：`/root`。
范围仅为 [SRC] 的 Claim 与 Steps 1–4；本件不作来源、全局 twist、新意、价值或容量评价。

## Claim

固定 $T>0$，原映射与能量为 $F_T(x,y)=(T/(x-y),x/y)$、$h=-x+y+x/y-T/x$。
在 $V=\{x>0,y<0\}$ 上，$D(x,y)=(-x/y,-y)=(p,q)$ 给完整正象限上的单步共轭
$$D F_T D^{-1}=H_T,\qquad H_T(p,q)=\left(\frac{T}{qp(p+1)},p\right),\qquad G_T(p,q)=pq+p+q+\frac{T}{pq}=-h.$$
每个非平衡正域能级恰为 $h<h_-$ 的原下外无 terminal 圆 $C^1$。
令 $\lambda=T^{1/3}>0$、$R(p,q)=(\lambda/p,\lambda/q)=(a,b)$，则
$$R H_T R^{-1}(a,b)=\left(\frac{a+\lambda}{ba^2},a\right),\qquad G_T=\lambda\left(ab+\frac1a+\frac1b+\frac{\lambda}{ab}\right).$$

## Status

**PASS — PROVABLE AS STATED。** 上述 Claim 原样成立；未发现必须修正的代数、量词或分支错误。
这是一张新接口的有界数学通过意见，不是原全局结论的新验收、来源覆盖结论或论文准入票。

## Assumptions

- $T>0$；$w_-<0$ 满足 $T=w_-^3(w_--1)$，且 $h_-=w_-(3-2w_-)$。
- 按任务给定的已接受 [GEO] 接口，$h<h_-$ 的完整原实纤维有两圆；$C^0$ 含四个 terminal 点，$C^1$ 不含。
- [GEO] 提供原正则完整纤维与光滑实椭圆曲线的同构及原映射为准确平移；本轮不重证这些事实。

## Notation

$K$ 表示 $G_T$ 的能级，$K_m$ 表示其最小值；$c>0$ 满足 $T=c^3(c+1)$。
$r=\sqrt{pq}>0$、$t=\tfrac12\log(p/q)$ 为辅助坐标；$f_n=-\lambda/y_n$ 为标量递推变量。
Claim 的能量恒等式按坐标拉回理解：$G_T=-h\circ D^{-1}$，末式左边为 $G_T\circ R^{-1}$。

## Proof strategy

独立逐项代入、正域紧性与正则能级检查，最后只消费 [GEO] 的完整分支及 terminal 分布。

## Dependency map

1. 双向单步共轭与能量恒等式只依赖显式有理式和 $T>0$。
2. 唯一正域圆及能量范围只依赖适当性、唯一临界点和双曲坐标。
3. 原圆身份依赖第 2 项与 [GEO]；倒数缩放和递推只依赖第 1 项及 $\lambda^3=T$。

## Proof

### Step 1. 完整正域与单步方向：PASS

$D^{-1}(p,q)=(pq,-q)$，故 $D$ 及其逆在各自整个开域光滑。
对 $p,q>0$，$x-y=q(p+1)>0$，且
$$F_T(pq,-q)=\left(\frac{T}{q(p+1)},-p\right),\qquad D F_T(pq,-q)=\left(\frac{T}{pq(p+1)},p\right).$$
$H_T^{-1}(p,q)=(q,T/[pq(q+1)])$ 在正象限处处定义并保正，故不只是前向半轨道对应。
代入原能量得到 $-h=pq+p+q+T/(pq)$；若 $s=T/[pq(p+1)]$，则
$$G_T(s,p)=\frac{T}{q(p+1)}+\frac{T}{pq(p+1)}+p+q(p+1)=G_T(p,q).$$
这里等式对应 $F_T$ 本身，没有取逆、换时向或改成 $F_T^2$。

### Step 2. 能级范围与唯一圆：PASS

非空有限上子水平集 $G_T\le K$ 有 $K>0$，且 $T/K^2\le p,q\le K$；由连续性它是正象限内的紧集。
临界点满足 $p\partial_pG_T-q\partial_qG_T=p-q=0$，继而 $T=c^3(c+1)$；右边在正轴严格递增。
极小值存在且临界点唯一，故 $c=-w_-$、$K_m=2c^2+3c=-h_-$。
在全局辅助坐标中 $G_T=r^2+2r\cosh t+T/r^2$；令 $\phi(r)=r^2+2r+T/r^2$。
$\phi''(r)=2+6T/r^4>0$，两端趋于正无穷，唯一极小为 $\phi(c)=K_m$。
每个 $K>K_m$ 恰有两根 $r_L<c<r_R$，且实能级准确由
$$t=\pm\operatorname{arcosh}\frac{K-r^2-T/r^2}{2r},\qquad r\in[r_L,r_R]$$
组成。两图内部不交、仅在两个端点相接；能级无临界点，故连接处也光滑，整体恰为一个嵌入圆。
$K=K_m$ 只有平衡点，$K<K_m$ 为空；非平衡圆的量词准确是全部 $K>K_m$，即全部 $h<h_-$。

### Step 3. 完整原圆与 terminal 接口：PASS

第 2 项的紧圆经 $D^{-1}$ 落在原有限 torus 图，其上 $h=-K<h_-$ 是正则值。
这个像局部就是原正则能级，因而在完整实纤维中开；紧性及完整曲线的 Hausdorff 性又使它闭。
它连通，故恰为所在的整个实连通分支，不能只是单圆上的真弧段。
它全部留在 torus 内，不含 terminal 点；[GEO] 的两圆中只有 $C^1$ 具有此属性，故身份准确。
不包括端点孤立平衡点，也不包括中间、上外或含 terminal 的下外 $C^0$；本稿未作这些越界声称。

### Step 4. 参数缩放与递推方向：PASS

由 $p=\lambda/a$、$q=\lambda/b$ 得 $H_T$ 第一坐标为 $\lambda ba^2/(a+\lambda)$；施加 $R$ 即得 Claim。
能量四项分别为 $\lambda^2/(ab)$、$\lambda/a$、$\lambda/b$、$\lambda ab$，整体因子与参数均正确。
原轨道有 $x_n=y_ny_{n+1}$，故 $y_{n+2}y_n=T/[y_{n+1}(y_{n+1}-1)]$。
代入 $y_n=-\lambda/f_n$ 并消去 $\lambda^2$，得到 $f_{n+2}f_n=(f_{n+1}+\lambda)/f_{n+1}^2$。
准确状态对应为 $(a_n,b_n)=R D(x_n,y_n)=(f_{n+1},f_n)$，更新仍为 $(f_{n+1},f_n)\mapsto(f_{n+2},f_{n+1})$。
因此正确缩放是 $-T^{1/3}/y_n$；被审稿已明确排除的早期倒置缩放不是本件证明的一部分。

## Corrections or missing assumptions

无必须修正项。可选最小澄清：在原 Step 4 添上上述状态索引等式，以预防将坐标次序误读为时间反转。
固定 $T$ 时两次变换都固定；若只对照被审稿显示的四参数公式，$(T,0,0,1)$ 与 $(\lambda,1,0,0)$ 均逐项匹配。

## Open risks and actual read scope

单步共轭不自动对齐另行指定的圆定向；旋转角与文献角仍可能相补，且 $K=-h$ 会反转能量导数符号。
本轮未读任何外文来源正文，故不认证 BR2005 的定理条件、单调性、端点、特殊参数节或实际覆盖范围。
来源正文缺读不影响上述自足代数证明；反过来，代数 PASS 也不填补来源缺读或证明全局严格 twist 图。
实际 FULL 读 proof-writer 技能、[SRC] 全部 140 行 / 8737 bytes、[GEO] 全部 208 行 / 11847 bytes。
未做来源检索、CAS、数值、全族扫描、构建、再委派；未改主稿、冻结稿、锁、索引或既有接受产物。

[SRC]: PAPER31_QPI_REAL_GLOBAL_TWIST_SOMOS_QRT_SOURCE_PROBE_V1_20260912.md
[GEO]: PAPER31_QPI_REAL_COMPONENT_RETURN_GEOMETRY_V1_20260912.md
