# Paper31 Q2：原辛测度、terminal 与逐圆投影接口 V1

日期：2026-09-13 UTC。作者：/root；纸核协作：/root/p31_q2_measure_terminal_interface（只读）。
状态：AUTHOR_PROOF_FROZEN / FRESH_MATH_REVIEW_PENDING。按 proof-writer 保存完整假设与证明。
这是 Q2 的定义与测度接口，不是相关衰减定理、长文中心、查新票或正式准入。
无数值、CAS、参数／阶数扫描。四条 terminal 均在原曲面内，没有删节点邻域改题。

## 1. 对象与既定几何输入

固定 \(T>0\)，在原完整开放实曲面 \(U=\mathcal U_T(\mathbb R)\) 上取

$$F(x,y)=\left(\frac{T}{x-y},\frac xy\right),\qquad
h=-x+y+x/y-T/x,\qquad \Omega=\frac{dx\wedge dy}{xy},\quad d\mu=|\Omega|.$$

消费已接受的 [P30 §2][P30] 与 [G]：\(F:U\to U\) 为自同构；原 torus 加四条 terminal 线组成 \(U\)；
射影曲面 \(S_T\) 上的 pencil \(\bar h:S_T\to\mathbb P^1\) 的无穷 scheme fiber 是 \(D\)，且 \(\mathcal U_T=S_T\setminus D\)。
有限正则纤维准确为完整实椭圆曲线

$$E_h:\ v^2+huv-Tv=u^3-Tu^2,\qquad P=(0,T),$$

上的 \(+P\)。两个实临界值为 \(h_-<h_+\)，由 \(T=w_\pm^3(w_\pm-1)\)、\(w_-<0<w_+-1\)、\(h_\pm=3w_\pm-2w_\pm^2\) 给出。
下区间两圆分别保持，中区间一圆，上区间两圆被 \(F\) 交换。临界点各一个，均非退化。
不由本件重新给旧全实 twist 或原曲面验收票。

## 2. Terminal 完全正则

令 \(B=T+ab\)，四图直接代入如下。

| 图 | \((x,y)\) | \(\Omega=c\,da\wedge db\) | \(h\) | \(h_b|_{a=0}\) |
|---|---|---|---|---|
| 1 | \((a^{-1},1+ab)\) | \(-da\wedge db/(1+ab)\) | \(1+ab-Ta-b/(1+ab)\) | \(-1\) |
| 2 | \((aB,a^{-1})\) | \(+da\wedge db/B\) | \(-aB+a^2B+b/B\) | \(1/T\) |
| 3 | \((aB,a^2B)\) | \(-da\wedge db/B\) | \(-aB+a^2B+b/B\) | \(1/T\) |
| 4 | \(([a(1+ab)]^{-1},a^{-1})\) | \(-da\wedge db/(1+ab)\) | \((1+b)/(1+ab)-Ta(1+ab)\) | \(1\) |

在整条 terminal 线 \(a=0\) 上各分母为 \(1,T,T,1\)，均非零，且 \(dh\ne0\)，即使该点的能量等于 \(h_\pm\)。
在 torus 上记 \(F=(X,Y)\)，有 \(\det DF=T/[y^2(x-y)]\)、\(XY=Tx/[y(x-y)]\)，故 \(F^*\Omega=\Omega\)。
代入原式亦有 \(h\circ F=h\)。由完整自同构与稠密开集上的恒等式，两式在整个 \(U\) 延拓。
因此 \(\mu\) 是完整原系统的不变测度，不是原仿射坐标下截断出的测度。

## 3. Coarea 的方向、相对微分与紧性

在正则位形 \(U^\circ=\{dh\ne0\}\) 上，存在唯一沿纤维一形式 \(\eta\)，其局部 lift \(\widetilde\eta\) 满足

$$dh\wedge\widetilde\eta=\Omega.$$

线性代数给局部存在；任意两个 lift 相差 \(q\,dh\)，故沿纤维限制唯一且可粘合。
令 \(\iota_{X_h}\Omega=-dh\)，收缩上式得 \(\eta(X_h)=1\)。用此给各圆定向。
由 [G] 的实际同构

$$u=T/y,\quad v=Tx(y-1)/y^2,\quad
\omega=\frac{du}{2v+hu-T},$$

写 \(A=x(y-1)-Ty/x\)，有 \(2v+hu-T=TA/y^2\)、\(du=-Tdy/y^2\)、\(h_x=-A/(xy)\)，所以

$$\boxed{dh\wedge\omega=+\Omega}.$$

等式先在分母非零的稠密开集成立，再以相对微分延拓；\(\eta\) 沿正则纤维就是 \(\omega\)。
不能把总空间表达式当作临界点处仍有光滑 lift：那里 \(dh=0\) 而 \(\Omega\ne0\)，上述等式自身即排除。

令 \(L_c(h)=\int_{C_h^c}\eta>0\)，取 \(\theta\in\mathbb R/\mathbb Z\) 使 \(\eta=L_c(h)d\theta\)，则

$$\boxed{d\mu=L_c(h)\,dh\,d\theta},\qquad d\nu_{h,c}=d\theta=\eta/L_c(h).$$

双圆的周期相同：椭圆群的实平移将 identity 圆送至另一陪集圆，并保持 \(\omega\) 与方向。
因此同能级可统一写 \(L(h)\)。特别地，\(F\) 即使交换圆也保持这些条件概率测度。

紧性来自 proper 映射而不是仅从纤维紧猜出：
\(\mathcal U_T=\bar h^{-1}(\mathbb A^1)\)，所以 \(h\) 是 proper 映射的基变换。
实拓扑上 \(S_T(\mathbb R)\) 紧，任意闭有限区间 \(J\subset\mathbb R\) 在 \(\mathbb RP^1\) 仍闭，
故 \(h^{-1}(J)=\bar h^{-1}(J)\subset U\) 紧，且有有限 \(\mu\) 体积。开能窗只相对紧，不称紧。
临界纤维去掉有限临界点后局部是一维子流形，所以两个临界纤维都是 \(\mu\)-零集，coarea 可按三个正则能区间求和。

## 4. 必须减逐圆均值，而非整纤维均值

对 \(f\in L^2(\mu)\) 定义正则圆上的条件期望

$$\Pi f|_{C_h^c}=\int_{C_h^c}f\,d\nu_{h,c}.$$

临界纤维上定义值不影响 \(L^2\) 对象。由 coarea、Fubini 与圆上常数的正交投影，
\(\Pi\) 是投影到逐连通圆常值子空间的正交投影。
对 \(f\in C_c^r(U)\)，\(|\Pi f|\le\|f\|_\infty\)，且在
\(h^{-1}(h(\operatorname{supp}f))\) 外为零；此饱和集紧，所以 \(\Pi f\in L^2(\mu)\)。
不声称 \(\Pi f\) 跨临界能级仍为 \(C^r\)。

写 Koopman 算子 \(\mathsf U f=f\circ F\)。若 \(F(C_h^c)=C_h^{\sigma(c)}\)，则

$$\Pi\mathsf U f|_{C_h^c}=\int_{C_h^{\sigma(c)}}f\,d\nu
=\mathsf U\Pi f|_{C_h^c},\qquad \boxed{\Pi\mathsf U=\mathsf U\Pi}.$$

但 \(\Pi\) 不等于到 \(F\)-不变子空间的投影，其像在上区间包含 \(-1\) 本征函数。
确取非零 \(\chi\in C_c^\infty((h_+,\infty))\)，在两圆上分别置
\(f_\chi=+\chi(h)\)、\(-\chi(h)\)，在其余能级置零。
分支在远离临界值的能窗内是分离的光滑开闭部分，且 \(h\) proper，故 \(f_\chi\in C_c^\infty(U)\)，包括 terminal。
两圆条件体积相同，整纤维均值为零；但 \(\mathsf U f_\chi=-f_\chi\)，于是

$$\langle\mathsf U^n f_\chi,f_\chi\rangle=(-1)^n\|f_\chi\|_2^2.$$

若改取 \(\chi\in C_c^\infty((-\infty,h_-))\)，同法给整纤维均值为零的 \(+1\) 本征函数。
这证明整纤维中心化连趋零都不够，而逐圆投影消除这两种零模。
Q2 的正确定义为

$$C_n(f,g)=\left\langle\mathsf U^n(I-\Pi)f,(I-\Pi)g\right\rangle_{L^2(\mu)},
\qquad f,g\in C_c^\infty(U).$$

内积在第一槽线性。紧性与 Cauchy–Schwarz 保证定义良好；这里尚无衰减结论。

## 5. Terminal 的有限阶范数接口及边界

在 terminal 紧子邻域，\(h_b\) 有非零下界，故 \((h,a)\) 是局部坐标，并有

$$\Omega=-\frac c{h_b}dh\wedge da,\quad
\eta=-\frac c{h_b}da,\quad
D_h=h_b^{-1}\partial_b,\quad
D_a|_h=\partial_a-\frac{h_a}{h_b}\partial_b.$$

在 \(a=0\) 四图的 \(\eta\) 依次为 \(-da,-da,+da,+da\)。
这些微分算子及所需有限阶导数在所选紧子邻域有界；反向变换亦然，
故原图与 \((h,a)\) 图的 \(C^r\) 范数等价，常数只依赖固定 \(T\)、紧邻域和 \(r\)。
在避开临界值的闭有限能带，proper submersion 与非零 Hamiltonian 场同理给逐分支光滑能量—角度平凡化及有界范数转换。

terminal 不产生新的局部坐标或测度奇性；但归一化周期与 \(\Pi f\) 可在临界能级退化，
即使 \(f\) 的空间支撑远离临界点。因此不能声称所有此类振幅跨节点一致光滑。
此外，正则能级上的 twist 驻点亦影响衰减；本件未判断其阶数、Fourier 求和或最优主项。
所有结论仅为同一个 Q2 的必要短接口，不以短引理拼接获得22–30页容量票。

[P30]: ../../papers/30-qpi-vertical-critical-ideals/paper/v4/sections/02-surface-pencil.tex
[G]: PAPER31_QPI_REAL_COMPONENT_RETURN_GEOMETRY_V1_20260912.md
