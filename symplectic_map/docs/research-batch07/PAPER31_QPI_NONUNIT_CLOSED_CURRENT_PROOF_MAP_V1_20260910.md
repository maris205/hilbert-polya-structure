# Paper31 闭合非单位时间算术候选：CURRENT_PROOF_MAP V1

日期：2026-09-10 UTC。性质：完整候选 C1–C3 的现有证明依赖与出口定位；不是论文提纲、重新证明、四门评分或正文容量判断。只新增本文件，其他输入只读。

本件依据 [新 Phase A][PA] 的三项核心及 [全次数数学处置][MATH] 的已接受范围，合并 [C1 消费者盘点][INV-C1] 与 [G 消费者盘点][INV-G]。新 [C/D][NCD] 的新意 7.0、价值 7.0、`CAUTION / NO_ADMISSION` 保持；准备完整候选不授予准入。Phase A 和各作者证明中“等待独查”的时点文字是历史记录，当前数学接受状态以 MATH 为准，本件不重新投数学票。

使用 academic-research-suite 的 claim–evidence–reasoning 可追溯方法：只把现有主张、完整证明模块、输入前提和实际出口绑定；不启动其论文提纲、写稿或试排流程。下列 PM 编号是依赖节点，不是拟定论文章节，也不表示独立新意数量。

## 1. 同一个原对象与实际复形

固定 $R=\mathbb Z[\tau]$、原动力参数 $q=1$，$X=\mathbb P^1_R\times_R\mathbb P^1_R$。原 $S/R$ 是以下四簇 $1+2+3+2$ 次截面吹起，不能以抽象同秩矩阵、未绑定 Pascal 对象或只在某个纤维上同构的模型替换：

1. 簇 1：吹起 $(x^{-1},y-1)=(0,0)$。
2. 簇 2：先吹起 $(x,y^{-1})=(0,0)$；再于 $x=u\xi,y=u^{-1}$ 中吹起 $(u,\xi)=(0,\tau)$。
3. 簇 3：先吹起 $(x,y)=(0,0)$，再吹起第一次例外与 $y=0$ 的交点；最后于 $x=u\xi,y=u^2\xi$ 中吹起 $(u,\xi)=(0,\tau)$。
4. 簇 4：先吹起 $(x^{-1},y^{-1})=(0,0)$；再于 $x=(u\xi)^{-1},y=u^{-1}$ 中吹起 $(u,\xi)=(0,1)$。

这些数据及不交簇重排见 [JET 第 67–89、111–128 行][JET]。只先做四次边界节点吹起得到 $Y\to X$；其余四个互不相交的末次截面组成 $Z\subset Y$，且原 $S=\operatorname{Bl}_Z Y$。$\tau=0$ 时末次中心仍是光滑相对曲面内的正则截面；这不宣称可逆动力延拓至零时间。令 $\mathscr L_S=\omega_{S/R}^{-1}$、$\mathscr L_Y=\omega_{Y/R}^{-1}$。JET 中曾以 $M_n$ 记 $Y$ 上线丛；本件始终以 $M_n$ 记下面的原上同调模，避免符号混用。

对 $n\ge0$，令
$$\Lambda_n=\{(i,j):0\le i,j\le2n,\ n+i-j\ge0,\ i+j\ge n,\ i+2j\ge2n,\ i+j\le3n\},$$
$$V_n=\bigoplus_{(i,j)\in\Lambda_n}R x^iy^j,\qquad W_n=\bigl(R[u,v]/(u,v)^n\bigr)^{\oplus4}.$$
$W_0=0$，$\operatorname{rank}V_n=2n(n+1)+1$，$\operatorname{rank}W_n=2n(n+1)$。这里的 fat jets 取在**末次吹起之前**，$\xi=\lambda+v$；不能换成末次吹起图的 $\xi=\lambda+uv$。

原单项式在四个反典范标架下的局部系数依次是
$$u^{2n-i}(1+v)^j,\quad u^{n+i-j}(\tau+v)^i,\quad u^{i+2j-2n}(\tau+v)^{i+j-n},\quad u^{3n-i-j}(1+v)^{2n-i}.$$
$J_n:V_n\to W_n$ 取其 $u^av^b$、$a+b<n$ 系数；整数二项系数不给任何阶乘或整数分母。见 [JET 第 14–34 行][JET]、[D05 第 53–66 行][D05]、[G 第 97–119 行][G]。PM1 证明这是原几何的实际复形，故
$$R\Gamma(S,\mathscr L_S^n)\simeq[V_n\xrightarrow{J_n}W_n],\quad M_n=H^1(S,\mathscr L_S^n)=\operatorname{coker}J_n.$$
固定原截面 $s_0=xy$、$s_1=x^2-x^2y+xy^2-\tau y$，以及
$$T_n=\ker(M_n\to M_n[\tau^{-1}]),\quad L_n=M_n/T_n,\quad E_n=L_n^{**}/L_n,\quad R^\circ=R[\tau^{-1}].$$
不预设 $L_n$ 在 $R$ 上自由，不预设 $M_n=T_n\oplus L_n$。JET 原定理在 $B=\mathbb Z[q^{\pm1},\tau]$ 上证明任意基变换；这里的 $B\to R$、$q\mapsto1$ 非平坦，必须消费其实际基变换证明，不能仅把旧 $H^0$ 张量到 $R$。

## 2. 候选三项核心的完整结论出口

### C1：原全次数相邻扩张、标记 Ext 与可恢复连接

对每个 $n\ge0$，原乘 $s_0$ 给出逐项单射链图，以及
$$H^0(S,\mathscr L_S^n)=\bigoplus_{k=0}^{n}R s_0^{n-k}s_1^k,$$
$$0\longrightarrow M_n\xrightarrow{\iota_n}M_{n+1}\longrightarrow R\oplus\bigoplus_{r=2,3}\bigoplus_{a=1}^{n}R/(\tau^{n+1-a})\longrightarrow0.$$
自由商项有原第三图常数 jet 的提升。对每个标记 $(r,a)$，置 $m=n+1-a$，原新 jet $u^a$ 的类 $y_{r,a}^{(n+1)}$ 满足
$$\tau^m y_{r,a}^{(n+1)}=\iota_n(e_{r,a}^{(n)}),\qquad e_{r,a}^{(n)}=\left[u^{a-1}\sum_{b=0}^{m-1}(-1)^b\tau^{m-1-b}v^b\right]_{r,n}.$$
$e_{r,a}^{(n)}\bmod\tau^m M_n$ 是该标记商分量的完整 $\operatorname{Ext}^1_R(R/(\tau^m),M_n)$ 类。全部 $n\ge1$ 的整列非分裂；$n=0$ 无扭子商分量，是自由例外。关系给实际递归呈示，且四边插值、兼容泛函和精确除法提供任意旧类的严格降次数恢复。

完整证明出口为 PM1–PM3，尤其 [D05 Steps 1–8，第 83–208 行][D05]。所有标记 Ext 与恢复机制本身就是 C1 的结构输出；C3 的长度消费者使用原短正合列和实际格映射，完整核另由原 Fitting 分支消费，均不消费每个 Ext 值。不能由此删去 C1 的 Steps 6–8，也不能反称每个 Ext 值都是 C3 的必需前提。

### C2：原留数坐标、完整整数格与自然双对偶缺陷

对 $n\ge1$、$N=n-1$、$0\le a\le N$，令
$$I_{n,a}=\left(\binom{N-b}{a}\tau^b:0\le b\le N-a\right).$$
由原四图和反典范标架定义的 $\rho_n:W_n\to(R^\circ)^n$ 满足 $\rho_nJ_n=0$，诱导原 $M_n[1/\tau]\simeq(R^\circ)^n$，并准确给出
$$\ker\rho_n|_{M_n}=T_n,\quad\rho_n(M_n)=\bigoplus_{a=0}^{n-1}\tau^{-n}I_{n,a}e_a,\quad L_n\xrightarrow[\widetilde\rho_n=\tau^n\rho_n]{\sim}\bigoplus_a I_{n,a}.$$
原连接满足 $\rho_{n+1}\iota_n=(0,\rho_n)$；在 $\widetilde\rho$ 坐标中是 $\tau$ 倍右移。每个具体嵌入 $I_{n,a}\subset R$ 的 $I_{n,a}^{**}=R$，故
$$E_n\simeq\bigoplus_a R/I_{n,a}$$
是有限阿贝尔群。该同构是原无扭商及自然双对偶的指定坐标，不是未绑定的关联分次。

完整整数系数层也属此出口：对 $A_p=R_{(p,\tau)}$，置 $d=N-a$、$e_b=\min_{0\le j\le b}v_p\binom{N-j}{a}$，则作为 $\mathbb Z_{(p)}$-模
$$A_p/I_{n,a}A_p\simeq\bigoplus_{b=0}^{d-1}\bigl(\mathbb Z_{(p)}/(p^{e_b})\bigr)\tau^b.$$
$\tau$ 将第 $b$ 层按自然投影送到第 $b+1$ 层，最后一层送零；这不是宣称该直和的各层在 $A_p$ 上都独立。令
$$d_p(N,a)=\min\{0\le b\le N-a:p\nmid\tbinom{N-b}{a}\},\qquad D_n(p)=\sum_{a=0}^{N}d_p(N,a).$$
则 $\dim_{\mathbb F_p}(A_p/I_{n,a}A_p)[p]=d_p(N,a)$；它不等于一般的 $p$-对数群阶 $\sum_b e_b$。全格证明为 PM4–PM5，系数层为 PM7；PM4 还消费 PM2 的逆 $\tau$ 后自由秩，不把秩当成格像。

### C3：同一原模的全局 Fitting、所有特征长度与全次数数字规则

令 $B_n=\sum_{j=1}^{n-1}j^2$，$B_0=0$；$n=0$ 使用空和、空乘积及 $D_0(p)=0$。则
$$\operatorname{Fitt}_j(M_n)=0\ (0\le j<n),\qquad\operatorname{Fitt}_n(M_n)=\tau^{B_n}\prod_{a=0}^{n-1}I_{n,a}\subset R.$$
对任意域 $k$，原 $M_{n,k}=M_n\otimes_R k[[\tau]]$ 的自由秩为 $n$，且
$$\operatorname{length}\operatorname{tors}_{\tau}M_{n,k}=B_n\quad(\operatorname{char}k=0),\qquad B_n+D_n(p)\quad(\operatorname{char}k=p).$$
每个素数 $p$ 相对**同次数**的特征零长度首次严格增加于 $n=p+1$，增量为 $p-1$；这时
$$\operatorname{Fitt}_{p+1}(M_{p+1}\otimes_R A_p)=\tau^{\sum_{j=1}^{p}j^2}(p,\tau)^{p-1}$$
是非主理想。对所有 $n\ge1$，
$$D_n(p)=0\iff n/p^{v_p(n)}<p\iff E_n\otimes_R A_p=0\iff L_n\otimes_R A_p\text{ 自由}.$$
置 $H_p(N)=D_{N+1}(p)$、$H_p(-1)=0$、$Z_p(Q)=\prod_i(Q_i+1)$，其中 $Q_i$ 是基 $p$ 数字且 $Z_p(0)=1$。把整数商写为 $Q$，避免与原动力参数 $q=1$ 混淆。对 $N=pQ+r$、$0\le r<p$，
$$H_p(N)=p(r+1)H_p(Q)+p(p-1-r)H_p(Q-1)+(r+1)(p-1-r)(Z_p(Q)-1).$$
计算基底是 $0\le N<p$ 时 $H_p(N)=0$；$N=0$ 的展示等式自身是恒等式，不能作为自递归算法。$N\ge p$ 时 $Q,Q-1<N$，故终止。

长度出口为 PM7–PM8；真正原全局 Fitting 还需要 PM6、PM9–PM10；无缺陷和终止递推需要 PM11。首现、消失判据、数字递推共同消费同一全次数机制，不作为三项独立新方法重复计数。

## 3. 完整证明模块与调用边

最小依赖关系是：原数据经 PM1 得实际复形；PM2–PM3 关闭 C1；PM2 的秩输出与 PM4–PM5 关闭原格；PM7–PM8 从这些实际接口给长度；PM6 的真正分辨率与 PM9 合取后由 PM10 给全局 Fitting；PM11 关闭全部次数的数字结论。下列范围保留整个所列证明模块，不以某个结论行替代其证明。

### PM1：原吹起、线丛与任意基变换的实际 cone

**来源：**[JET Steps 1–4，第 111–224 行][JET]；原数据第 8–34、67–89 行；局部典范微分计算的短前置依据是 [FIRST 第 91–95 行][FIRST]。**输入：**原八个中心和 $\mathscr L_S$，先在 $B$ 上，随后任意 $B$-代数。

- Step 1 的四个互不相交簇允许交换局部吹起顺序并粘合，故重排后的 $S\to Y$ 是原构造；逐图证明正则中心和光滑射影模型。$r=vw,s=v$ 下 $dr\wedge ds=\pm v\,dv\wedge dw$ 给相对典范的例外因子，因此 $\mathscr L_S^n=\rho^*\mathscr L_Y^n(-n\sum E_r)$。
- 局部吹起被识别为 $\mathcal O_{\mathbb P^1}(-1)$ 的总空间；其两仿射图 Čech 计算给 $R\rho_*\mathcal O(-nE)=\mathcal I_Z^n$、高次像零。该证明在原系数环及任意基变换后成立，非平坦情形不是靠抽象“上同调与张量交换”。
- Step 3 从 $X$ 的 $\mathcal O(2n,2n)$ 的 Čech 消失出发，明确四个预吹起的系数投影；四块被删单项式互不重叠，各有单位右逆。由此得到 $R\Gamma(Y,\mathscr L_Y^n)=V_n[0]$ 与准确指数集，而非仅计数相等。
- Step 4 的四个末次正则中心用真正 $\xi=\lambda+v$ 的 fat jets；局部系数含已扣的例外因子，在坏图不反演 $\xi=\tau+v$。以 $0\to\mathscr L_Y^n\mathcal I_Z^n\to\mathscr L_Y^n\to\mathscr L_Y^n|_{nZ}\to0$ 的 cone 得实际 $J_n$、$H^{\ge2}=0$、任意基变换，以及 $(xy)^n$ 零列和 $n=0$ 边界。

**输出与边界：**绑定全部后续 $M_n$、原源、原目标和原截面；不输出全核、不输出高次原模直和分类。JET Step 5 的旧八组脚本复形比对和 Step 6 的二阶完整分解不被此 C1–C3 全称主干调用，不能为了保留旧章节而加入必要前提。

### PM2：原相邻商、四边整数消去与完整截面核

**来源：**[D05 Steps 1–5，第 83–160 行][D05]。**输入：**PM1 的实际 $C_n=[V_n\to W_n]$ 与固定 $s_0,s_1$。

- Step 1：四图的原 $s_0$ 系数分别是 $u(1+v)$、$u(\tau+v)$、$u(\tau+v)$、$u(1+v)$，与 $J_n$ 构成链图。坏图不能约去非单位 $\tau$；逐齐次层利用 $\tau$ 为非零因子证明目标单射，源单射直接来自原单项式。
- Step 2：完整目标商保留四个 $u=0$ 单变量部分及两坏图的循环项；$u^aR[v]/(v^m,\tau+v)\simeq R/(\tau^m)$。不能将两坏图当作好图的单位消元。
- Step 3：原受限 $V_{n+1}/s_0V_n$ 恰为四条共享顶点的边；各边的正 $u$ 次项已为目标商中的零，但共享端点须一致，不能用任意四组多项式取代原源。
- Step 4：式 (14)、(15) 的整数插值给全部边界的提升，证明 $\Psi_{n+1}=0$ 不仅必要而且充分，并以第三图常数证明自由商满射。这是商复形同伦简化的实际单位消去，不只是维数推断。
- Step 5：实际 $s_1^k$ 落在 $\ker J_k$，提升商复形的 $H^0$ 生成元并关闭连接同态；从 $n=0$ 归纳得完整核 $\bigoplus_{i=0}^n R s_0^{n-i}s_1^i$ 与原短正合列。逆 $\tau$ 后每一步新增一个可分裂自由商，故 $M_n[1/\tau]$ 自由秩为 $n$。

**输出与边界：**C1 的完整核和实际正合列；PM4 只从此取得秩，PM6 消费完整核，PM8 消费原正合列。逆 $\tau$ 自由秩不识别 G 的留数映射，更不能独自确定整数格。

### PM3：全部标记 Ext、真正递归呈示及降次数恢复

**来源：**[D05 Steps 6–8，第 162–208 行][D05]。**输入：**PM2 已证明的原链图、商生成元、插值和兼容坐标。

- Step 6：几何级数恒等式 $(\tau+v)\sum_{b=0}^{m-1}(-1)^b\tau^{m-1-b}v^b=\tau^m+(-1)^{m-1}v^m$，乘 $u^a$ 后余项在新 fat jet 的总次数为 $n+1$ 而消失，给 C1 的**完整** $e_{r,a}^{(n)}$。由 $0\to R\xrightarrow{\tau^m}R\to R/(\tau^m)\to0$ 计算 Ext，保留其模 $\tau^mM_n$ 的标记值。
- 同一步的递归呈示由旧 $M_n$、一个自由新生成元和所有 $y_{r,a}^{(n+1)}$ 加准确关系构成；先由商生成证明满射，再由已知短正合列证明无额外关系，不能只写一张候选关系矩阵。
- Step 7：$n=1$ 的非分裂基例在该段内直接计算 $M_2\simeq R^2\oplus R/(\tau)$；一般 $n$ 通过旧商中的非零 Ext 像证明整列非分裂。这里不需要把 JET 的旧二阶分解或固定素数 3 的 T3 导入作前提。
- Step 8：对任意新类先提取全部 $\Psi$ 自由坐标及坏图循环坐标，扣除标准新提升；再用四边插值提升原源并扣 $J$ 的边界，唯一逆解原 $u(1+v)$／$u(\tau+v)$ 链图回到旧 jet。除法在 $R$ 中精确完成，不反演 $\tau$；每轮次数严格下降，故恢复规则闭合。

**输出与边界：**C1 全部标记扩张和可恢复连接是一项独立结构产出。PM8 不使用全部 $e_{r,a}^{(n)}$ 的值，但这不使其变成可随意删掉的附例；反之，C1 不由 C3 的长度或 Fitting 公式反推。

### PM4：原共同零点、全局留数定理与原自由余核识别

**来源：**[G Steps 1–4，第 137–275 行][G]，标架与假设第 89–119 行。**输入：**PM1 的原 $Y$、线丛及四图，PM2 的原 $s_0,s_1$ 与逆 $\tau$ 后自由秩。外部 GR 的具体调用见第 5 节。

- Step 1 写出两原截面在四个实际标架中的完整多项式 $F_r,G_r$，原点 Jacobian 分别为 $(-1,\tau,\tau,1)$；两好图已为 $R$ 中单位，两坏图的 $\tau$ 须在 $R^\circ$ 中才可逆。
- Step 2 检查 $Y$ 的全部八条 toric 边界射线的最低面与顶点：四个实际根为 $1,\tau,\tau,1$，其他顶点系数为单位，故 $\tau\ne0$ 时没有遗漏的共同零点或边界共同分量。这是应用紧曲面全局留数的有限相交条件，不用 ample 假设替代。
- Step 3 直接计算原反典范标架的 $\kappa=(-1,1,-1,-1)$，取 $\epsilon=-\kappa$，符号与 $n$ 无关。原 $P\in V_n$ 给 $\omega_{n,a}(P)=P\,dx\wedge dy/(s_0^{a+1}s_1^{n-a})$，其局部式是 $\kappa_r Q_{r,n}(P)\,du\wedge dv/(F_r^{a+1}G_r^{n-a})$，因而确为全局亚纯典范二形式。
- 同一步用原 $\Delta_r=\det\partial(F_r,G_r)/\partial(u,v)$ 及形式逆坐标提取 $\rho_{n,a}(w)=\sum_r\epsilon_r[F^aG^{n-1-a}](w_r/\Delta_r)(u_r(F,G),v_r(F,G))$。逆坐标保留极大理想幂，故依赖的正是原截断 jet。对每个非零复数 $\tau$，GR 给局部留数和为零；再由所有条目都是整数 Laurent 多项式，把纤维等式提升成精确 $\rho_nJ_n=0$，没有把特征零点态结论直接冒充任意特征结论。
- 原四边兼容泛函满足 $(-1)^{n-1}\tau^n\rho_{n,0}=\Psi_n$，核准自由坐标归一化。Step 4 以第三图的 $\Delta_3F_3^aG_3^{n-1-a}$ 截断 jet 命中各标准基，证明原 $\rho_n$ 的逆 $\tau$ 满射；再用 PM2 的同秩自由源得同构。原局部化核正是 $T_n$。

**输出与边界：**此处识别原 $M_n[1/\tau]$ 及其实际映射，不仅给一个抽象秩；尚未由此确定 $\rho_n(M_n)$ 的整数格，必须继续 PM5。G 作者不能以本证明图替代独立评价；本件也不追加一张独立数学票。

### PM5：全部 fat jets 的整数正规形、精确格像与移位

**来源：**[G Steps 5–8，第 277–384 行][G]。**输入：**PM4 已定义并识别的同一个 $\rho_n$，原坏图完整 $F,G$。

- Step 5 在两坏图给 $\lambda=1+u^2(u-1)(\tau+v)$、$U=u/\lambda$、$V=v+u^2(u-1)(\tau+v)^2$。其线性 Jacobian 是整数单位，故在 $R[[u,v]]$ 上为形式自同构，保留全部 $(u,v)^n$；准确恒等式 $\tau+V=(\tau+v)\lambda$ 给 $(F,G)=(U(\tau+V),V)$。体积形式的 Jacobian 单位必须随变换保留。
- Step 6 对**整个目标**任意 $h\bmod(U,V)^n$ 计算，而非只对原源的像计算；$h$ 已吸收实际体积形式的 Jacobian 单位。单项式 $U^aV^b$ 的局部留数只命中第 $a$ 个坐标，系数为 $(-1)^{N-a-b}\binom{N-b}{a}\tau^{b-n}$，第 2 图另有不改变理想的总体负号。任意 $h$ 与所有单项式生成两方向合起来给精确直和像。没有给 $M_n$ 擅加 $R[u,v]$-模结构。
- 两好图的整数形式坐标给像 $R^n$；坏图理想含末项 $\tau^{n-1-a}$，故 $R^n\subset\tau^{-n}\bigoplus I_{n,a}$，不会增加另一格。由此得到 C2 的**实际**整数像，不仅上下界或关联分次。
- Step 7 在定义 $\rho$ 的同一系数提取中乘原 $F=s_0$，得到严格右移；再乘归一化 $\tau^{n+1}$ 得 $\tau$ 倍右移。Pascal 恒等式验证 $\tau I_{n,a}\subset I_{n+1,a+1}$，但不能只靠理想包含猜原映射。
- Step 8 以 $I$ 中非零整数与末端 $\tau$ 幂互素，逐分式分母证明 UFD 中 $I^*=I^{**}=R$，自然双对偶映射就是既定包含。每个 $R/I$ 同时被某个非零整数和某个 $\tau$ 幂消灭，故有限；得到原 $L_n^{**}=R^n$ 和有限 $E_n$。

**输出与边界：**C2 与 C 的 H2–H3、DET 所需指定归一化均在同一个原 $M_n$ 上成立；形式逆函数、负二项式展开和 UFD 双对偶是所用标准机制，不各自包装成新增研究核心。

### PM6：完整原核的单位补基与长度一自由分辨率

**来源：**[A Step 1，第 69–79 行][A]，其输入完整核来自 PM2，不是从自由秩推断。**输入：**PM1 的实际源基与 PM2 的全部 $P_k=s_0^{n-k}s_1^k$。

$P_k$ 的最高 $y$ 次数为 $n+k$，相应原单项式 $x^ny^{n+k}$ 的系数为 $1$。用这些相异单项式列，按三角单位变换将全部 $P_0,\ldots,P_n$ 补成 $V_n$ 的一个整数基。抽象“核自由”不保证商自由，必须保留这项原系数级证明。删去**完整**核的 $n+1$ 个零列后，得真实单射
$$0\longrightarrow R^{n(2n+1)}\xrightarrow{\Phi_n}R^{2n(n+1)}\longrightarrow M_n\longrightarrow0.$$
$n=0$ 两个自由模均零。**输出与边界：**为 DET 提供实际长度一自由分辨率；不由此给 $M_n$ 自由或完整直和。旧单位补基机制可作为既有基线扣除，不需导入旧 W3 的整套材料作新证明前提。

### PM7：具体整数理想的全部系数层、Lucas 规则与首现

**来源：**[C Steps 1–3，第 67–104 行][C]。**输入：**明确的 $I_{n,a}$；作为原模结论时还必须有 PM5 的原格绑定。

Step 1 再核对自然归一化。Step 2 证明 $\tau^b$ 的系数理想准确是 $\binom Na,\ldots,\binom{N-b}{a}$ 生成的整数理想，且各层独立取模 $p^{e_b}$；被 $p^{e_0},\tau^d$ 消灭的商局部化到 $A_p$ 不改变，$\tau$ 作用为自然投影。非零循环层的 $p$-核各一维，得到 $d_p$ 而不是把 $\sum e_b$ 当成 $d_p$。

Step 3 在 $\mathbb F_p[X]$ 中从 $(1+X)^m=\prod_i(1+X^{p^i})^{m_i}$ 比较系数，给 Lucas 数字条件及
$$d_p(N,a)=N-\max\{m\le N:\ a_i\le m_i\text{ 对每个基 }p\text{ 数字成立}\}.$$
当 $N<p$ 全部为零；$N=p$ 的两个端点理想为单位，中间恰 $p-1$ 个 $I=(p,\tau)$，每个 $d_p=1$，包括 $p=2$。**输出与边界：**C2 的完整系数层、C3 的首现代数输入及 PM11 的全数字基础；本模块本身不证明原相邻映射或原 Fitting。

### PM8：实际专门化像、格指数扣除与所有特征扭长

**来源：**[C Steps 4–6，第 106–164 行][C]。**输入：**H1 是 PM2 的原短正合列；H2 是 PM4–PM5 的逆 $\tau$ 同构及完整格像；H3 是 PM5 的严格原连接。

- Step 4 的相邻商 $Q_n=R\oplus2\bigoplus_{j=1}^{n-1}R/(\tau^j)$ 无整数素数扭子，故 $\operatorname{Tor}_1^R(Q_n,R/(p))=Q_n[p]=0$；特征零的有理化、随后域扩张和 DVR 完成都平坦，保留原相邻短正合列。
- 定义 $F_{n,k}$ 为原 $M_{n,k}$ 在 $k((\tau))^n$ 中的实际像，$T_{n,k}$ 为其实际局部化核。通过 $M_n\twoheadrightarrow L_n$ 的右正合张量并随后映入 Laurent 向量空间，得 $F_{n,k}=\bigoplus_a\tau^{-n+d_{n,a}(k)}k[[\tau]]$；其中 $d_{n,a}(k)=0$ 在特征零、$d_{n,a}(k)=d_p(n-1,a)$ 在特征 $p$，以下 $D_n$ 也取相应特征的总和。不假定 $L_n\otimes k[[\tau]]$ 自身无扭，更不假定取扭子与张量交换。
- Step 5 用原移位求 $F_{n-1,k}\to F_{n,k}$ 的各指数 $h_{n,a}=1+d_{n-1,a}-d_{n,a+1}\ge0$，新第零坐标给自由商。实际格商扭长为 $\kappa_n=(n-1)+D_{n-1}-D_n$；非负性由 Pascal 包含核对。
- Step 6 的蛇形引理给 $0\to T_{n-1,k}\to T_{n,k}\to Q_{n,k}\to F_{n,k}/F_{n-1,k}\to0$。后两模自由秩均为一，满射在其无扭商上乘单位，故其扭子间也是满射；由此才可扣去 $\kappa_n$。得到长度增量 $(n-1)^2+D_n-D_{n-1}$，从 $M_0=0$ 望远镜相加为 $B_n+D_n$。

**输出与边界：**所有特征的原长度、逆 $\tau$ 自由秩与特征零 $B_n$。不把相邻商扭长直接累加，不在这里消费全部标记 Ext，也不需要 PM6 的自由分辨率；PM6 的必要性属于 Fitting 分支。

### PM9：互补最大子式、自然行列式理想与高度一扭结因子

**来源：**[DET 假设第 13–87 行及 Steps 1–7，第 110–277 行][DET]。**输入：**对每个 $A_p=\mathbb Z[\tau]_{(p,\tau)}$，真实单射自由分辨率、$M[1/\tau]$ 在整个 $A_p[1/\tau]$ 上自由、自然 $L=M/T$、自由 $L^{**}$、有限长 $E=L^{**}/L$，以及稍后应用乘积时的指定 $I^{**}=A_p$。

- Step 1：$A_p$ 是二维正则局部 UFD，高度一局部化为 DVR；逆 $\tau$ 自由使 $T$ 是全部扭结。通过到环的泛函识别 $L\hookrightarrow L^{**}$ 的**自然**嵌入，有限 $E$ 在高度一处消失。
- Step 2：由自由生成模 $A_p^{r+n}\twoheadrightarrow M\twoheadrightarrow L\hookrightarrow L^{**}\simeq A_p^n$ 形成矩阵 $P$，像准确为 $L$，$P\Phi=0$，其最大子式理想为自然 $\operatorname{detideal}(L)$。仅在分式域中有 $\ker P=\operatorname{im}\Phi$；在 $A_p$ 上不能忽略中间的扭子。互补交替顶次形式证明全部互补最大子式由同一个分式标量 $\delta$ 相连，故 $I_r(\Phi)=\delta I_n(P)$ 是准确分式理想等式。
- Steps 3–4：每个高度一处 $P$ 满射，可取单位基化为 $[I,0]$；$\Phi$ 的对应块以 DVR Smith 计算 $v_{\mathfrak q}(\delta)$ 等于该处扭长。所有 $\mathfrak q\ne(\tau)$ 因全开集 $M[1/\tau]$ 自由而赋值为零；$(\tau)$ 处经 $\mathbb Q[[\tau]]$ 的平坦完成将赋值与 PM8 的 $B_n$ 准确对应。UFD 因而给 $\delta=\text{单位}\cdot\tau^{B_n}$；返回原理想后仍保留 $I_n(P)$ 的高度二非主因子，不只留下除子类。
- Step 5 单独处理零秩／无关系边界。Step 6 保留已修正的归一化要求：抽象 $L\simeq\bigoplus I_a$ 不足以直接写原乘积；若 $I_a^{**}=g_aA_p$，自然双对偶中的正确理想为 $\prod g_a^{-1}I_a$。例如 $A_p\simeq(p)$ 说明未归一化乘积会出错。只有各指定 $I_a^{**}=A_p$，才可直接写 $\prod I_a$。
- Step 7 以二项式理想的非零整数和末端 $\tau$ 幂互素核对这一条件，但不替代 G 证明原 $L$ 就是该具体直和。

**输出与边界：**条件性准确公式 $\operatorname{Fitt}_n(M)=\tau^{B_n}\operatorname{detideal}(L)$；同对象假设由 PM10 匹配后才是原结论。修正前的“抽象直和即可直接乘积”不复活；DVR Smith 在此是高度一证明工具，不表示已获得全部原整数 Smith 块。

### PM10：同对象前提合取、全部素理想覆盖与全局原 Fitting

**来源：**[A Step 1 的第 81–88 行、Steps 2–3 的第 90–115 行][A]。**输入：**PM2 的 H1、PM4–PM5 的 H2–H3、PM8 的原特征零扭长，PM6 的实际分辨率，以及 PM5 的自然归一化和有限缺陷。

先把 C 与 DET 的每项假设都落实到同一个原 $M_n$：分辨率局部化保持单射，$M_n[1/\tau]$ 在整个开集自由，原 $L_n^{**}=R^n$ 且 $E_n$ 有限，每个指定 $I_{n,a}^{**}=R$。DET 遂在每个 $A_p$ 给准确局部乘积。

全局化不能只检查已选的一个素数：不含 $\tau$ 的素理想处，原 $M_n$ 自由且各 $I_{n,a}$ 为单位；含 $\tau$ 的素理想在 $R$ 中恰为 $(\tau)$ 或 $(p,\tau)$，由以上局部式再局部化覆盖。两个有限生成理想在全部素理想处相等，故在整个 $R$ 相等。小于秩的 Fitting 所需子式阶数超过 $\Phi_n$ 列数，故全部为零；$n=0$ 另用空乘积。

PM7 的首现理想与 PM8 的同次数长度结合，给所有素数的首次增加及准确非主 Fitting；非主性用 UFD 中 $(p,\tau)^{p-1}$ 的公因子为一但理想真小于环。**输出与边界：**C3 的完整原全局理想和首现，而非旧全素数强直和 (P)、高于秩的其余 Fitting 或全部 Smith 指数。

### PM11：无缺陷次数的充要条件与完整数字递推

**来源：**[A Steps 4–5，第 117–157 行][A]。**输入：**PM7 的全数字最大值公式和 PM5 的原自然缺陷，不用有限样本外推。

Step 4 对 $N=n-1>0$ 证明 $D_n(p)=0$ 等价于 $N$ 的最高非零位以下全部为 $p-1$，$N=0$ 单独满足无缺陷的空条件。若不满足，以最高位 $N_h-1$、低位全取 $p-1$ 构造 $a\le N$ 但不满足逐位支配，故至少一个 $d_p>0$。加一并处理末端进位，得到 $n/p^{v_p(n)}<p$。有限 $p$-群非零必有非零 $p$-核，给 $D=0\iff E\otimes A_p=0$；自然 $L\to L^{**}$ 及 $L^{**}\simeq A_p^n$ 给与原局部格自由等价，反向也使用自由模自反性。

Step 5 将 $N=pQ+r$、$a=pb+s$ 分两种情形，覆盖所有 $a$：$s\le r$ 时以 $d_p(Q,b)$ 决定保持最高商或向下取数，零距离项数为 $Z_p(Q)$；$s>r$ 时必有 $b\le Q-1$，距离为 $p\,d_p(Q-1,b)+r+1$。分别对全部合法 $b,s$ 求和，合并常数项得到第 2 节的准确递推。$Q=0$ 的第二类为空，$0\le N<p$ 的基底单独给定；$N\ge p$ 的输入严格变小，证明算法终止。

**输出与边界：**C3 的全部 $n,p$ 无缺陷判据与有限整数规则。Lucas、首现、求和和消失不重复计作多种独立方法；该递推不输出原 $M_n$ 的全部直和块。

## 4. 两处“同对象合取”的必要接口

| 消费者前提 | 实际供应模块 | 不能偷换为 |
|---|---|---|
| C-H1：原相邻短正合列，商无整数素数扭子 | PM1–PM2；D05 Steps 1–5 | 任意同长度商、仅模 $p$ 的矩阵样本 |
| C-H2：原逆 $\tau$ 同构及完整整数像 | PM2 的秩 + PM4 的实际留数同构 + PM5 的完整像 | 仅逆 $\tau$ 秩、抽象 Pascal 格、关联分次 |
| C-H3：原 $s_0$ 连接的准确移位 | PM5 Step 7 的系数提取身份 | 仅 Pascal 理想包含，或独立选择的次数坐标 |
| DET：真正长度一自由分辨率 | PM1 原源目标 + PM2 完整核 + PM6 单位补基 | 核自由、核秩、有限域满秩 |
| DET：整个逆 $\tau$ 开集自由与泛型扭长 | PM4 的同构、PM8 特征零原长度 | 仅分式域向量空间维数或单个闭点计算 |
| DET：自然 $L^{**}$、有限 $E$ 与已归一化行列式格 | PM5 Step 8，PM7 系数层；PM10 实际匹配 | 任意抽象同构 $L\simeq\bigoplus I_a$ 后未除 $I_a^{**}$ 的乘积 |

此表只突出易错接口，不替代上节任何完整证明模块。尤其 PM3 的全部标记 Ext 没有伪造到 C-H1/H2/H3 中；其必要性属于完整 C1 自身。

## 5. 标准工具的准确调用范围

**外部 GR。** 所用命题是紧复流形上的全局 Grothendieck 留数和为零：在复维数二的紧光滑 $Y_\tau$ 上，将亚纯典范形式的极点分成两组有效极除子，两组仅在有限集相交；各局部以两组局部定义函数取留数，其总和为零。允许带重数的极点，不要求 ample。具体出处为 Griffiths, *Variations on a Theorem of Abel*, §III(a)，定义与坐标解释见印刷页 368–371，式 (3.7) 及 Stokes 证明见印刷页 372–373（所存 70 页 PDF 的第 48–53 页，第 52–53 页含式 (3.7) 及证明）。[官方 IAS 原件](https://publications.ias.edu/sites/default/files/variationsonatheorem.pdf)；[本地归档][GR]。

PM4 中紧光滑由 PM1 的射影光滑 $Y$，有限相交与无漏点由 G Step 2，亚纯典范形式与极点分组由 G Step 3 的原标架及 $s_0,s_1$ 的幂提供；局部留数用同一步的 $(F,G)$ 逆坐标和 Jacobian 系数式。这里只使用 GR 的留数和零方向，不使用要求正性的逆留数／Cayley–Bacharach 结论，不要求把 GR 全文或其余 64 页纳入候选正文。

| 标准工具 | 本候选中的实际作用及适用条件 | 现有证明位置 |
|---|---|---|
| 正则中心吹起、相对典范公式、投影公式与 Čech | 原八截面重排、$R\rho_*\mathcal O(-nE)=\mathcal I^n$、原 $Y$ 消失及实际 cone；局部证明覆盖任意基变换 | PM1；JET Steps 1–4；FIRST 第 91–95 行仅局部典范计算 |
| 整数单位插值、长正合列与一次关系分辨率的 Ext | 四边兼容的充分性、实际 $s_1^k$ 提升、所有标记 $e\bmod\tau^m M_n$ | PM2–PM3；D05 Steps 3–8 |
| 全局留数、局部 Cauchy 系数公式及 Laurent 恒等原则 | 在原四个共同零点消去原 $J_n$，从全部非零复时间提升到整数 Laurent 身份 | PM4；G Steps 2–4；GR 的上述相关段落 |
| 整数形式逆函数与负二项式展开 | Jacobian 常数为单位，保存每个 fat-jet 截断；计算整个目标的实际格像 | PM5；G Steps 5–6 |
| UFD 分母约分与自然双对偶 | 非零整数和 $\tau$ 幂互素，给具体 $I^{**}=R$；禁止未归一化抽象乘积 | PM5、PM7、PM9；G Step 8、C Step 1、DET Step 6 |
| $\operatorname{Tor}_1$、平坦域扩张／完成、蛇形引理 | 先用原商无整数素数扭子保正合，再在实际像上计算格指数和扭长 | PM8；C Steps 4–6 |
| 互补最大子式的交替代数、DVR Smith 与 UFD | 全部最大子式有同一分式比例；各高度一赋值确定 $\tau^{B_n}$，高度二行列式理想保留 | PM9；DET Steps 1–7 |
| 有限生成理想的全素理想局部检测 | 覆盖 $(\tau)$、全部 $(p,\tau)$ 和逆 $\tau$ 开集，恢复整个 $R$ 的准确理想 | PM10；A Step 2 |
| Frobenius/Lucas 数字系数、有限 $p$-群与分位求和 | 完整系数层的 $p$-核、首现、无缺陷充要条件及严格缩小输入的递推 | PM7、PM11；C Step 3、A Steps 4–5 |

这些工具大多已在指定证明中给出所需短证明或实际适用核对，不因名称标准便省去原曲面特有接口，也不因引用它们而新增“所有外文全文均须进正文”的要求。G 的整数坐标 Jacobian 是该正规形的必需工具，不是旧单位时间 Jacobian／Hasse 旁支。

## 6. 必须保留与不得添入的边界

- 必须保留原四簇定义、实际标架、$S\to Y$ 的层论链、全部四边兼容与恢复、原共同零点穷尽、留数符号与同一对象的整数格像，以及完整核的单位补基、自然双对偶归一化、实际专门化像和全数字终止证明。这些不能以“标准工具”一词抹去。
- D05 的 T3、固定 $n=4\to5$ 的素数 3 类及指定 $P_r$／旧 $P_m$ 拉回推出，仅在 [D05 Steps 9–11，第 210–271 行][D05] 作为既有旁支消费者；不是上述全称 C1–C3 的证明前提，不能冒称原 $M_{n+1}$ 的直和块。
- 固定四阶真块化 M4 仅是既有核对锚点，不为全次数定理供给量词证明；不把该锚点及 T3/$P_m$ 的材料加入必要主干凑正文。这里也不借它们的样本结果倒证 PM8 或 PM10。
- 旧 UNIT 全次数结论、旧 Jacobian／Hasse 内容、其他族结果、旧 W1/W2 块、特殊纤维 Harbourne 公式与 JET 二阶脚本诊断不补入必要主干；若仅需解释历史基线，其身份是已知或旁支，不能重复计功。
- 完整原模强直和 (P)、全部 Smith 指数、高于秩的其他 Fitting 理想、跨系统族统一推广均不在现有闭合结论内。C1 的完整 Ext 与 C2 的完整格／缺陷也不能被这些未证强目标替代。
- 本件不按文件行数、字数、证明段数量或既有 PDF 页数估计正文容量，不给页数区间，不写稿试排，不将数学接受等同于新意、价值或可发表性通过。正式新一轮评价应消费冻结后的共同完整候选包；本件不是该评价的预判。

在本次**依赖定位**范围内，没有发现必须另造一条新引理才可连接当前 C1–C3 既有证明出口的明确缺口。此结语只报告图中前提与出口可追溯，不构成新数学 PASS、容量 PASS 或准入。须保留的真实风险边界包括：外部 GR 仅相关段落阅读而非全文、作者身份不独立、原整数格与其基变换实际像不能混同、行列式归一化修正不能丢失，以及现有 C/D 的 CAUTION。

## 7. 实际阅读、输入身份与未读边界

本次准备中本人 FULL 读取 PA（83 行）、MATH（117 行）、NCD（236 行）、INV-C1（177 行）、C（176 行）、DET（297 行）、A（180 行）。INV-G（185 行）、G（429 行）、D05（318 行）、JET（358 行）已在本人紧邻前任务以相同 SHA FULL 阅读；本次核对身份并刷新原模型、实际消费者、G 留数定义与标准工具调用、D05 Ext／恢复及 JET 层论链相应段落。此处“FULL”指所列本地 Markdown 文件全文，不外推成其引用论文或整个旧项目全文。

FIRST 仅本人此前 PARTIAL 阅读第 1–101 行；本件只消费第 91–95 行的局部典范微分计算，不声称其余内容已读或必需。GR 本人此前在 G 作者任务中读取官方原件的相关定义、坐标解释及式 (3.7) 的证明，范围为 PARTIAL；本次只核对新本地归档 SHA，**未重新读取本地 PDF**。主控另行报告已全文读取 PDF 第 48–53 页的文本，不转记为本人的 FULL 阅读，也不把六页相关段落称为整篇 70 页全文。没有依赖未读旧章节取得本图的证明出口。

| 输入 | SHA-256 | 本件实际消费范围 |
|---|---|---|
| [PA][PA] | `07b658e0e6a07fece0db86d85face58a852646760a6e8d185f7715800dd2ae5f` | 本次 FULL；核心定义与历史边界 |
| [MATH][MATH] | `a0d1c880f45462721f78366234d0d5796d04f95c46428c05caacdb90ce75fdd3` | 本次 FULL；当前数学接受范围，不新增投票 |
| [NCD][NCD] | `4f3f186d7e2c2b4dc8d1d733358d6c849d03c6ba3542b287d8207a4c5bb62737` | 本次 FULL；7.0/7.0 CAUTION 保留 |
| [INV-C1][INV-C1] | `ca5fe99e671cedaf7ae5f92115a5fe346eea648390ed1dbc0cef2a17fabb19a2` | 本次 FULL；C1 全部输出与实际消费边 |
| [INV-G][INV-G] | `6b75b13ee4421fd55b2ed93e11cc89945d53d7eed5952afb10c62531baf38801` | 本人紧邻前任务同 SHA FULL；本次合并 |
| [G][G] | `d872b731423107412631a9834b639229b2578e0084afef752c6a94d6e90f7c6a` | 本人同 SHA FULL；本次刷新实际接口与留数调用；本人是作者 |
| [C][C] | `25bb87a365eaf5a9d37c192a47f99d454007aa14e265668c34465cc3e2154e10` | 本次 FULL；整数层、Tor、实际像、格指数与蛇形引理 |
| [DET][DET] | `913e701986e540a59476a9f64bf890bf3bbdc300596ef9db9514ebe784dcb250` | 本次 FULL；全部工具及归一化修正 |
| [A][A] | `f214e2e14d065e778d752f15855995d0a66df4c115d7aa72e14af5695e153260` | 本次 FULL；完整核补基、合取全局化、数字证明 |
| [D05][D05] | `9c87c8570065deba6dd14e33e7a27382a2d3d6ba34f01a883ee7faff92fb60d0` | 本人同 SHA FULL；本次刷新 Ext／恢复；Steps 9–11 仅旁支 |
| [JET][JET] | `0acbfc4866b0cf944c84f88c8db3e7c535fdbff366ead4f166c3d8f01e3e2005` | 本人同 SHA FULL；本次刷新 Steps 1–4 实际层论链 |
| [FIRST][FIRST] | `ef975ded12f7263842e208f6eda87df213e210e9dbf7ef3c08fbd8724fe6270d` | 此前 PARTIAL 1–101；仅消费 91–95 |
| [GR 本地归档][GR] | `517692faba4fb281bb78b2f129fde7dabe6a3625e5dcb4f75cfdad37fc521fb1` | 本次仅 hash；本人此前官方相关段落 PARTIAL，未宣称本地 PDF FULL |

本件不新增 CPU/GPU 数学实验、参数扫描、浮点数据、外文全文精读、编译或外部上传。已对本文件全文自读，并对转录澄清处读回；13 个直接本地链接均存在，13 项输入 SHA 均与上表相符，引用标签均有定义。终态消息单独报告本件 SHA，文件本身不写自引用哈希。

[PA]: PAPER31_QPI_NONUNIT_CLOSED_ARITHMETIC_PHASE_A_V1_20260909.md
[MATH]: PAPER31_QPI_NONUNIT_ALL_DEGREE_MATHEMATICS_DISPOSITION_V1_20260910.md
[NCD]: PAPER31_QPI_NONUNIT_CLOSED_NOVELTY_CD_V1_20260910.md
[INV-C1]: PAPER31_QPI_NONUNIT_C1_PROOF_CONSUMER_INVENTORY_V1_20260910.md
[INV-G]: PAPER31_QPI_NONUNIT_G_PROOF_CONSUMER_INVENTORY_V1_20260910.md
[G]: PAPER31_QPI_NONUNIT_LATTICE_CONTROL_LEMMA_V1_20260909.md
[C]: PAPER31_QPI_NONUNIT_BINOMIAL_CONSUMERS_LEMMA_V1_20260909.md
[DET]: PAPER31_QPI_NONUNIT_DETERMINANT_IDEAL_LEMMA_V1_20260909.md
[A]: PAPER31_QPI_NONUNIT_ALL_DEGREE_ARITHMETIC_THEOREM_V1_20260909.md
[D05]: PAPER31_QPI_NONUNIT_ADJACENT_EXTENSION_DIAGNOSTIC_V1_20260909.md
[JET]: PAPER30_QPI_NONUNIT_TAU_ALL_DEGREE_JET_COMPLEX_V1_20260909.md
[FIRST]: PAPER30_QPI_NONUNIT_TAU_FIRST_LAYER_PROOF_V1_20260909.md
[GR]: primary-sources/griffiths-1976-variations-on-a-theorem-of-abel.pdf
