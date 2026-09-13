# Paper31：正域四次递推的准确源对应 V1

日期：2026-09-12 UTC。作者：`/root`。
用途：本轮全实 twist 查新的窄代数接口；不重开已接受全局数学，不申报新方法。
文件所有权仅本件；当前稿待独立检查以下新接口，不是正式准入票。

## Claim

固定 $T>0$。原映射及能量为
$$F_T(x,y)=\left(\frac{T}{x-y},\frac{x}{y}\right),\qquad
h=-x+y+x/y-T/x.$$
在 $V=\{x>0,y<0\}$ 上，$D(x,y)=(-x/y,-y)=(p,q)$ 是到正象限的微分同胚，且
$$D F_T D^{-1}(p,q)=H_T(p,q):=\left(\frac{T}{qp(p+1)},p\right),\qquad
G_T(p,q)=pq+p+q+\frac{T}{pq}=-h.$$
该正象限的非平衡能级恰对应原下外区间 $h<h_-$ 的无 terminal 圆 $C^1$。
再令 $\lambda=T^{1/3}$、$R(p,q)=(\lambda/p,\lambda/q)=(a,b)$，则
$$R H_T R^{-1}(a,b)=\left(\frac{a+\lambda}{ba^2},a\right),\qquad
G_T=\lambda\left(ab+\frac1a+\frac1b+\frac{\lambda}{ab}\right).$$
这里 $a,b$ 是倒数坐标，不是下文文献的四个系数。
不主张正域论文因此已经覆盖中间、上外、完整 terminal 状态或全部严格 twist 图。

## Status

PROVABLE AS STATED（作者证明；独立审查另存，不冒充已验收）。

## Assumptions and notation

$h_-=w_-(3-2w_-)$，$w_-<0$，$T=w_-^3(w_--1)$。
采用已接受 [GEO] 的完整原曲面／实分支识别：下外两圆中 $C^0$ 含四个 terminal 点，$C^1$ 无 terminal。
本件只引用这项既有接口，不重新证明原曲面或已接受旋转分类。
$V$、正象限及全部下述变换均为实域；取唯一正实立方根。

## Proof strategy and dependency map

1. 直接代入给单步有理共轭及能量恒等式，无时间反转或平方。
2. 正象限的适当能量及唯一平衡点给能级范围；显式双曲坐标证明各正则能级仅一个圆。
3. 紧致圆嵌入完整原曲线后，用既有 terminal 分布识别为 $C^1$。
4. 再作双倒数缩放，得到常见的线性分子／平方分母递推；此为检索正常形，不计创新。

## Proof

### Step 1. 单步和能量

$D^{-1}(p,q)=(pq,-q)$。正 $p,q$ 给 $x-y=q(p+1)>0$，故原映射在 $V$ 处处有定义。
代入原式得到
$$F_T(pq,-q)=\left(\frac{T}{q(p+1)},-p\right),\qquad
D F_T(pq,-q)=\left(\frac{T}{pq(p+1)},p\right).$$
逆映射 $H_T^{-1}(p,q)=(q,T/[pq(q+1)])$ 也保正，故这是完整正域上的双向共轭。
代入能量给 $h=-pq-q-p-T/(pq)=-G_T$。
亦可独立验算：记 $r=T/[pq(p+1)]$，则
$$G_T(r,p)=\frac{T}{q(p+1)}+\frac{T}{pq(p+1)}+p+q(p+1)
=\frac{T}{pq}+p+q+pq.$$

### Step 2. 能级与唯一圆

$G_T$ 的任意非空有界上子水平集紧包含于正象限：$p+q\le K$ 且 $pq\ge T/K$ 给出两个坐标的正下界与有限上界。
在临界点，$p\partial_pG_T-q\partial_qG_T=p-q=0$，故 $p=q=c>0$，再得 $T=c^3(c+1)$。
此方程正解唯一，因为右侧在正轴严格递增。因此 $c=-w_-$，最小值为
$$K_m=G_T(c,c)=2c^2+3c=-h_-.$$
也可直接定位全部能级：置 $p=r e^t,q=r e^{-t}$，其中 $r>0,t\in\mathbb R$，则
$$G_T=r^2+2r\cosh t+T/r^2,\qquad \phi(r)=r^2+2r+T/r^2.$$
$\phi''=2+6T/r^4>0$，两端趋于正无穷，唯一极小在 $r=c$。
对每个 $K>K_m$，$\phi(r)=K$ 有两个根 $r_L<c<r_R$。
能级由 $r\in[r_L,r_R]$ 上的两条图
$$t=\pm\operatorname{arcosh}\frac{K-r^2-T/r^2}{2r}$$
在两端连接而成；内部两图分离，端点处只有 $t=0$。
因唯一临界点的能量是 $K_m$，该能级处处正则；这两条闭弧的并是一个光滑嵌入圆。
$K=K_m$ 仅平衡点；$K<K_m$ 无正域点。由 $K=-h$，非平衡范围恰 $h<h_-$。

### Step 3. 原实分支识别

Step 2 的圆通过 $D^{-1}$ 嵌入原有限 torus 图，并通过 [GEO] 的原纤维同构嵌入完整实曲线。
这是同维正则子流形，像在所在实分支中开；紧性又使像闭。
每个实分支连通，故像是一个完整实分支，而非只是一段弧。
像完全在 torus 图中，不含任何 terminal 点；[GEO] 的下外 $C^0$ 含四个这样的点。
因此像恰为下外 $C^1$。同一平移在两圆的角度相同是既有群论接口，不是本件另证的定向约定。

### Step 4. 倒数归一化与递推

令 $p=\lambda/a,q=\lambda/b$ 并用 $T=\lambda^3$，直接计算
$$\frac{\lambda}{T/[qp(p+1)]}=\frac{a+\lambda}{ba^2},\qquad \frac{\lambda}{p}=a.$$
能量逐项变为 $\lambda^2/(ab)+\lambda/a+\lambda/b+\lambda ab$，即 Claim 的式子。
若原轨道以 $y_n$ 记，则 $x_n=y_ny_{n+1}$，从原映射得
$$y_{n+2}y_n=\frac{T}{y_{n+1}(y_{n+1}-1)}.$$
令 $f_n=-\lambda/y_n$，便得到
$$f_{n+2}f_n=\frac{f_{n+1}+\lambda}{f_{n+1}^2}.$$
这里正确缩放是 $-T^{1/3}/y_n$；先前给来源代理的首条探索消息曾误写为 $-1/(T^{1/3}y_n)$，已即时更正，错误写法不作证据。∎

## Source match and limits

[BR2005] 的官方开放摘要明确研究
$$\mathcal F_{A,B,C,D}(p,q)=\left(\frac{A+Bp+Cp^2}{q(C+Dp+p^2)},p\right)$$
的非负系数正域族。Step 1 给 $(A,B,C,D)=(T,0,0,1)$，Step 4 给 $(\lambda,1,0,0)$。
这是固定原 $T$ 的固定参数对应，不受旧“固定 $T$ 未必固定 Lyness 参数”的排除理由保护。
本文贡献仍只是经典族的精确识别；正域圆共轭、持久有界等已有背景必须扣除。
主代理实际读了官方摘要；Phase B 代理另外实际读到原文开头式(1.2)、(1.5)、(1.6)和 Theorem 3.2。
本件不以代理后段未读的信息声称该文有或没有完整单调性定理。
原正向 $\omega$ 的 $\rho$ 与文献主值角可能相补，能量又为 $K=-h$；未核原方向前不能直接比较极大／极小。
更不能把其他来源的 $5/8$ 数值猜想直接宣称为本原族已解决的公开猜想：尚需证明那个两周期 Lyness 边界与这里同一。

## Actual retrieval record

主代理本轮另外实际使用 11 条查询，独立于 Phase B 的36条，不作日期覆盖替代：

| # | 实际 query | 用途／结果 |
|---|---|---|
| R1 | `"Somos-4" "rotation number"` | 正常形检索；未取得直接分类定理 |
| R2 | `"Bastien" "Rogalski" "elliptic quartics" 2005` | 官方 BR2005 元数据、摘要与公开 PDF 索引 |
| R3 | `"QRT" "3/16" "rotation"` | 无直接原族定理命中；无关命中排除 |
| R4 | `"Somos" "twist" "monotonicity"` | 无直接原族定理命中 |
| R5 | `"Bastien" "2005" "3/8" rotation quartics` | 同一 BR2005 索引及不同的2014 homographic 族；后者不当成本族 |
| R6 | `"10.1155/ADE.2005.227" monotonic` | 京都 EMIS 的948567.pdf 原文首页索引 |
| R7 | `"Bastien" "Rogalski" "c = d = 0"` | BR2005表8.1所在p257的索引片段；不是已读该节正文 |
| R8 | `site:math.ethz.ch/EMIS/journals/HOA/ADE/Volume2005_3/261.pdf "monotonic"` | 搜索引擎仍返回他文，不能当精确全文阴性 |
| R9 | `site:math.ethz.ch/EMIS/journals/HOA/ADE/Volume2005_3/261.pdf "3/8" "7."` | 同上，没有取得目标节正文 |
| R10 | `site:math.ethz.ch/EMIS/journals/HOA/ADE/Volume2005_3/261.pdf "conjecture"` | 同上，未排除猜想／定理 |
| R11 | `"Bastien" "Rogalski" quartics "16" rotation` | 同上，无足够主定理覆盖证据 |

已实际打开 [BR2005] 官方 landing，确认作者、2005-09-27出版日期、开放许可及摘要。
原出版物为 Advances in Difference Equations 2005:3, pp.227–261；不把现网页栏目改名反写成2005刊名。
ETH EMIS `.../Volume2005_3/261.pdf` 直接 open 得404；`www.emis.de` 同尾址 Internal Error。
京都 RIMS `.../Volume2005_3/948567.pdf` 索引可见首页，但 open 得 non-retryable safety error，未重试该路径。
Springer PDF 的两张指定页 screenshot 均解析失败，未看见图像；eudml 52828 open 超时。
这些失败不是数学阴性结果；未绕访问控制、调用其他网络下载器、下载文件或开展数值／CAS工作。
BR2005 后段、BC1998全定理、Duistermaat强章节仍为正文缺读；C/D必须保留这一来源风险。

## Corrections or missing assumptions

原全局分类的声明未修改；本件只新增正域共轭说明。
上述口头缩放错误已在本稿代入与原递推两条路径一致纠正，不修改冻结旧数学稿。

## Open risks and handoff

新接口需一次独立检查；已接受全局证明没有输入改变，不因此重审。
最强新风险是 BR2005 的特殊参数节可能直接给出下外严格图；目前没有足够正文判断。
即便下外全部已知，中间／上外仍须逐量词核对，不能据正域先例直接宣告全表重合或全表新颖。
准确对应不是新意加分，反而缩小了可宣传范围。正式价值、容量和双门票本件均不评价。

[GEO]: PAPER31_QPI_REAL_COMPONENT_RETURN_GEOMETRY_V1_20260912.md
[BR2005]: https://link.springer.com/article/10.1155/ADE.2005.227
