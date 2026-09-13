# P31：共同 Banach 模型上的聯合拋物核算子族

日期：2026-09-09。Goal 01 範圍內的有界理論筆記；只閉合兩條拋物分支的聯合核理想亞純性。不證 Fredholm determinant 的參數亞純性、全局 determinant 恆等式或任何曲線限制；不改正式稿、Route 判決或 Stage 狀態。

## 0. 輸入、來源與本筆記新增的論證

固定有限維空間 \(V\simeq\mathbb C^d\)（P31 為 \(d=12m\)）及一個不依賴參數的範數。以下使用已給定的 cusp gauge 輸入

\[
\eta_w(p_i)=D_i(w)J_iD_i(w)^{-1},\qquad
J_i=\eta_0(p_i),\qquad i=1,2,
\tag{1}
\]

其中 \(D_i:\mathbb C\to\mathrm{GL}(V)\) 全純，\(D_i^{-1}\) 亦全純；\(J_i\) 固定、半單，所有特徵值模長為一。本筆記不以逐點相似代替 (1)，也不另證 clock-period 的 cusp 消失；(1) 的實際上游證明見[尖點單值化與雙參數接口](internal_goal01_cusp_monodromy_and_bivariate_selberg_interface_20260909.md)。

來源接口為 Fedosova–Pohl, *Meromorphic continuation of Selberg zeta functions with twists having non-expanding cusp monodromy*, [arXiv:1709.00760v4](https://arxiv.org/pdf/1709.00760v4)：Property 5、§4.3、Example 4.1 式 (30)、Theorem 4.2(ii)、§4.7 及 Appendix A。來源給共同幾何域、兩條分支和固定表示的算子值亞純延拓；本文使用其 Lerch 延拓結論，另以下述顯式秩一展開證明局部核理想全純性。後者不能僅從「算子範數全純且每點 order-0 nuclear」推得。

## 1. 先選共同幾何 chart，再固定 Banach 空間

Example 4.1 的原實座標使用

\[
I_a=(0,1),\quad I_b=(1,\infty),\qquad
p_1=\begin{pmatrix}1&-1\\0&1\end{pmatrix},\quad
p_2=\begin{pmatrix}1&0\\-1&1\end{pmatrix}.
\tag{2}
\]

只有 \(P_{a,b}=\{p_1\}\)、\(P_{b,a}=\{p_2\}\)，兩個 \(g_p\) 均為 identity，沒有 finite \(C_{a,b}\) branches。原座標中 \(p_1\) 固定 \(\infty\)，且 \((p_1^{-n})'=1\)；在這個未更換的 affine 座標中不能直接宣稱權重為 \(O(n^{-2\operatorname{Re}z})\)。

依 Property 5(ii)，一次選定 \(h\in\mathrm{PSL}_2(\mathbb R)\)，使所有 \(h\overline{\mathcal E_c}\) 均在 \(\mathbb C\) 內。將**整個** strict tuple 以 \(h\) 共軛：幾何域、實區間、每個群元素均一起變換，並令

\[
\widetilde\eta_w(hgh^{-1})=\eta_w(g).
\tag{3}
\]

緊包含與映射關係保持；此後為簡化記號，仍用 \(\mathcal E_c,p_i,\eta_w\) 表示變換後的對象。於是所有 \(\overline{\mathcal E_c}\) 都是 \(\mathbb C\) 中的緊集，並固定

\[
B_c=\{f:\overline{\mathcal E_c}\to V:\ f\text{ 連續，且在 }\mathcal E_c\text{ 全純}\},
\quad \|f\|=\sup_{\overline{\mathcal E_c}}\|f(x)\|,
\qquad B=B_a\oplus B_b.
\tag{4}
\]

這些域、範數、直和與底層 \(V\) 均不依賴 \((z,w)\)。權重在此共同 chart 內按共軛後 Möbius 變換的導數定義。

為明確保留 chart 的權重變換，令 \(\phi=p^{-n}\)、\(\widetilde\phi=h\phi h^{-1}\)。在兩個 affine 座標都有限的實區間重疊上，設

\[
(W_{h,z}f)(x)=((h^{-1})'(x))^z f(h^{-1}x).
\]

鏈式律及正實導數給

\[
W_{h,z}\big[(\phi')^z\eta_w(p)^n f\circ\phi\big]
=(\widetilde\phi')^z\eta_w(p)^n(W_{h,z}f)\circ\widetilde\phi.
\tag{5}
\]

複域中的冪沿來源的 holomorphic branch 延拓。(5) 是重疊上的轉換公式，**不是**宣稱 \(W_{h,z}\) 跨越原 \(\infty\) 時在某個未定義的舊 affine supnorm 空間間為有界同構。本文直接在 (4) 的共同 chart 模型工作。

## 2. 核理想與本筆記採用的參數全純定義

對 Banach 空間 \(X,Y\) 及 \(0<q\leq1\)，記 \(\mathcal N_q(X,Y)\) 為可寫成

\[
T=\sum_{j\geq0}v_j\otimes\ell_j,
\qquad (v_j\otimes\ell_j)f=\ell_j(f)v_j,
\qquad \sum_j\|v_j\|^q\|\ell_j\|^q<\infty
\tag{6}
\]

的 \(q\)-nuclear operators，使用相應分解的 \(q\)-和取 inf 所定的核準範數 \(n_q(T)\)。特別地，

\[
n_q\!\left(\sum_jT_j\right)^q\leq\sum_j n_q(T_j)^q,
\qquad n_q(ATC)\leq\|A\|n_q(T)\|C\|.
\tag{7}
\]

以下「局部 \(\mathcal N_q\)-全純」取具體的強形式：在每點附近存在雙變量冪級數

\[
T(z,w)=\sum_{r,s\geq0}A_{r,s}(z-z_*)^r(w-w_*)^s
\tag{8}
\]

且在每個較小雙圓盤上

\[
\sum_{r,s\geq0}n_q(A_{r,s})^q\rho_z^{qr}\rho_w^{qs}<\infty.
\tag{9}
\]

亞純且沿 \(z=z_0\) 至多一階，則意指存在這個意義下的局部全純 \(H\)，使

\[
T(z,w)=\frac{R(w)}{z-z_0}+H(z,w).
\tag{10}
\]

證明會直接構造 (8)–(9)；對 \(q<1\) 不把 \(\mathcal N_q\) 當成 Banach 空間使用 Cauchy 積分定理。

## 3. 單一拋物分支引理

取一條從 \(B_b\) 到 \(B_a\) 的分支，記 \(p\)、\(J\)、\(D(w)\)。假設共同 chart 的幾何關係為

\[
p^{-n}\overline{\mathcal E_a}\subset K\Subset\mathcal E_b
\quad(n\geq1),\qquad
x_p\notin\overline{\mathcal E_a},
\tag{11}
\]

其中 \(x_p\) 是 \(p\) 的固定點，(11) 是 Property 5(iv),(v) 在 \(g_p=\mathrm{id}\) 時的形式。對任何固定 \(x\in\mathcal E_a\)，\(p^{-n}x\to x_p\)；由 \(K\) 緊閉可知 \(x_p\in K\Subset\mathcal E_b\)。因此在共同 chart 內 \(x_p\) 有限，並且 \(p^{-1}\) 的矩陣下左元素非零。

初始定義

\[
(T(z,w)f)(x)=\sum_{n\geq1}((p^{-n})'(x))^z
\eta_w(p)^n f(p^{-n}x),\qquad \operatorname{Re}z>\tfrac12.
\tag{12}
\]

**引理。** 在 (1)、(4)、(11) 下，(12) 在固定空間 \(B_b\to B_a\) 上延拓為 \(\mathbb C^2\) 的聯合亞純族。對每個 \(0<q\leq1\)，它都滿足 §2 的局部 \(\mathcal N_q\)-全純／亞純定義。唯一可能的極點是固定直線

\[
z=z_k:=\frac{1-k}{2},\qquad k\in\mathbb N_0,
\tag{13}
\]

且均至多一階；若 \(1\notin\operatorname{spec}J\)，此分支整個聯合全純。每條 (13) 上的 residue 在 \(w\) 上全純，秩不超過 \(\dim\ker(J-I)\)。

### 3.1 固定 cusp 正規形與 Taylor–Lerch 展開

因 \(p^{-1}\) 是非平凡、有限固定點的實拋物 Möbius 變換，存在固定 \(\gamma\in\mathbb R\setminus\{0\}\)，使

\[
p^{-n}x=x_p+\frac{1}{\gamma(n+u(x))},
\qquad u(x)=\frac{1}{\gamma(x-x_p)},
\tag{14}
\]

並有

\[
(p^{-n})'(x)=c(x)(n+u(x))^{-2},
\qquad c(x)=-\frac{u'(x)}{\gamma}
=\frac{1}{\gamma^2(x-x_p)^2}.
\tag{15}
\]

由 (11)，\(u,c\) 在輸出域閉包附近全純且 \(c\) 無零點。固定 \(c(x)^z\) 的 holomorphic branch，使其在所含實區間上取正實導數的冪。這與 (12) 的分支一致。令 \(M=\sup_{\overline{\mathcal E_a}}|u|\)，選

\[
\overline{D(x_p,R)}\subset\mathcal E_b,
\qquad N>M+1,
\qquad \theta:=\frac{1}{|\gamma|R(N-M)}<1.
\tag{16}
\]

因此 \(n\geq N\) 的所有像點均在該 Taylor 圓盤內，且 \(\operatorname{Re}(N+u)>0\)。令

\[
\ell_k(f)=\frac{f^{(k)}(x_p)}{k!},\qquad
\|\ell_k\|\leq R^{-k}.
\tag{17}
\]

先對純量函數與固定 \(|\lambda|=1\)，以 \(S_\lambda(z)\) 記 (12) 中將矩陣冪換成 \(\lambda^n\) 的算子。對 \(\operatorname{Re}z>1/2\)，Taylor 展開及絕對一致收斂給

\[
S_\lambda(z)=H_{\lambda,N}(z)
+\sum_{k\geq0}v_{k,\lambda}(z)\otimes\ell_k,
\tag{18}
\]

其中有限 head 為 \(1\leq n<N\) 的原加權 composition 和，而

\[
v_{k,\lambda}(z)(x)
=c(x)^z\gamma^{-k}\lambda^N
\Phi(2z+k,\lambda,N+u(x)),
\quad
\Phi(a,\lambda,b)=\sum_{j\geq0}\frac{\lambda^j}{(j+b)^a}.
\tag{19}
\]

(19) 的 \(\lambda^N\) 與 \(\gamma^{-k}\) 分別直接來自 \(n=N+j\) 的換指標及 (14) 的 Taylor 冪；不省略這兩個因子。

Appendix A 的 \(m=0\) 情形給：在 \(\operatorname{Re}b>0\)，\(\lambda\ne1\) 時 \(\Phi\) 對 \((a,b)\) 全純；\(\lambda=1\) 時只在 \(a=1\) 有簡單極點，residue 為 \(1\)。後一常數亦由初始在 \(\operatorname{Re}a>1\)、\(\operatorname{Re}b>0\) 成立的積分

\[
\Gamma(a)\Phi(a,\lambda,b)
=\int_0^\infty t^{a-1}\frac{e^{-bt}}{1-\lambda e^{-t}}\,dt
\tag{20}
\]

在 \(t=0\) 的 Laurent 展開直接得到：\(\lambda=1\) 的首項為 \(t^{-1}\)，其餘潛在非正整數極點由 \(1/\Gamma(a)\) 的零消去；\(\lambda\ne1\) 則沒有 \(t^{-1}\) 項。減去任意有限個 Taylor／Laurent 項後，積分對緊 \(b\)-集一致收斂，給所需聯合參數控制。

### 3.2 大 Taylor 階的一致指數核界

給定緊 \(z\)-集 \(Q\)，令 \(\sigma_*:=\inf_Q\operatorname{Re}z\)，取 \(k_0\) 使 \(2\sigma_*+k_0>1\)。對所有 \(k\geq k_0\)，(19) 的 Lerch 級數仍在其絕對收斂半平面，故 (15)–(17) 給

\[
\begin{aligned}
\|v_{k,\lambda}(z)\|\,\|\ell_k\|
&\leq C_Q(|\gamma|R)^{-k}
\sum_{n=N}^{\infty}(n-M)^{-2\sigma_*-k}\\
&\leq C'_Q\left(|\gamma|R(N-M)\right)^{-k}
=C'_Q\theta^k.
\end{aligned}
\tag{21}
\]

第二個常數只需乘入
\((N-M)^{k_0}\sum_{n\geq N}(n-M)^{-2\sigma_*-k_0}\)，與 \(k\) 無關。複冪的 argument 因 \(\operatorname{Re}(n+u)>0\) 而一致有界，已吸收於 \(C_Q\)。有限個 \(k<k_0\) 由 (19) 的延拓處理；離開 (13) 時是 Banach 值全純的有限秩項。於是 tail 在每個緊非極點集上具有

\[
\sum_k\big(\|v_{k,\lambda}(z)\|\|\ell_k\|\big)^q<\infty
\qquad(0<q\leq1)
\tag{22}
\]

的一致界。這是額外的核理想局部界，不只是算子範數估計。

### 3.3 有限 head 亦有明確的 order-0 展開

固定 Riemann map \(\psi:\mathcal E_b\to\mathbb D\)。由 \(K\Subset\mathcal E_b\)，存在 \(r_0<1\) 使 \(\sup_K|\psi|\leq r_0\)。對純量 \(f\in\mathcal B(\mathcal E_b;\mathbb C)\)，寫

\[
f\circ\psi^{-1}(\zeta)=\sum_{j\geq0}\beta_j(f)\zeta^j,
\qquad \|\beta_j\|\leq1.
\tag{23}
\]

不要求 \(\psi\) 延拓至 \(\partial\mathcal E_b\)：係數界來自圓盤內的 Cauchy 估計，而 \(\psi\circ p^{-n}\) 只在內部緊集 \(K\) 上取值。每一個 \(n<N\) 的加權 composition 因而有

\[
\sum_{j\geq0}
\left[\lambda^n((p^{-n})')^z(\psi\circ p^{-n})^j\right]\otimes\beta_j,
\tag{24}
\]

且方括號的 supnorm 在緊 \(z\)-集上不超過 \(C_{Q,n}r_0^j\)。故有限 head 同樣有局部一致、指數衰減的秩一展開。

(12) 的初始和也確實在 \(\operatorname{Re}z>1/2\) 局部一致收斂：由 (15) 其權重為 \(O_Q(n^{-2\sigma_*})\)，且 \(\eta_w(p)^n\) 在緊 \(w\)-集上一致有界。若要求核準範數中的初始收斂，可在所有 \(n\) 上共用 (23)，先對 \(n\) 求和，再對 \(j\) 展開；截斷餘項的第 \(j\) 係數由
\(C_Qr_0^j\sum_{n>L}n^{-2\sigma_*}\) 控制，故其 \(n_q\) 趨零。這裡沒有錯用 \(\sum_n n^{-2q\sigma_*}\) 的收斂。

### 3.4 加入有限維 gauge，並直接證明雙參數核全純

半單性給固定譜投影

\[
J=\sum_{\lambda\in\operatorname{spec}J}\lambda P_\lambda,
\qquad
\eta_w(p)^n=D(w)\Big(\sum_\lambda\lambda^nP_\lambda\Big)D(w)^{-1}.
\tag{25}
\]

常矩陣與純量 composition 交換，因此在初始半平面有精確恆等式

\[
T(z,w)=M_{D(w)}T^0(z)M_{D(w)^{-1}},
\qquad T^0(z)=\sum_\lambda S_\lambda(z)\otimes P_\lambda,
\tag{26}
\]

其中 \(M_D\) 只作用於 \(V\)，而不是移動幾何域。緊 \(w\)-集上 \(\|D(w)\|\|D(w)^{-1}\|\) 有界。

以下不用僅有的算子全純性推核全純。固定 \(V\) 的基與座標泛函，把 (18)、(24)、(25) 逐座標展開：input functional 固定不依賴參數，output vector 是

\[
v_{k,\lambda}(z)(x)\,D(w)P_\lambda D(w)^{-1}e_\mu
\tag{27}
\]

或 (24) 對應的 head expression。它们在 \(B_a\) 這個真正的 Banach 空間中全純，且在較大的閉雙圓盤
\(|z-z_*|\leq R_z, |w-w_*|\leq R_w\) 上，形成有限組一致界為 \(C\vartheta^j\)、\(\vartheta<1\) 的秩一序列。

對每一個這樣的序列，寫其 output vector 的 Banach 值 Taylor 展開

\[
v_j(z,w)=\sum_{r,s\geq0}b_{j,r,s}(z-z_*)^r(w-w_*)^s.
\]

**僅在 \(B_a\) 中**使用通常 Cauchy 估計，得到

\[
\|b_{j,r,s}\|\|\ell_j\|
\leq C\vartheta^jR_z^{-r}R_w^{-s}.
\tag{28}
\]

令 \(A_{r,s}=\sum_j b_{j,r,s}\otimes\ell_j\)。對任意
\(\rho_z<R_z,\rho_w<R_w\)，直接由秩一分解可得

\[
\begin{aligned}
\sum_{r,s\geq0} n_q(A_{r,s})^q\rho_z^{qr}\rho_w^{qs}
&\leq C^q\sum_{j,r,s\geq0}
\vartheta^{qj}(\rho_z/R_z)^{qr}(\rho_w/R_w)^{qs}\\
&<\infty.
\end{aligned}
\tag{29}
\]

有限組序列的和仍滿足此界。所有重排與截斷均由 (29) 的 \(q\)-和餘項直接控制，於是建立 (8)–(9)。沒有對準 Banach 核理想使用未经說明的 Cauchy 定理，也沒有依靠僅僅逐變量或算子範數的全純性。

### 3.5 固定極點與 residue

在 \(z=z_k\) 只有 (19) 中的 \(\lambda=1\)、Taylor 指標恰為 \(k\) 的項可能有極點。因 \(2z+k-1=2(z-z_k)\)，residue 為

\[
(R_k(w)f)(x)
=\frac12 c(x)^{z_k}\gamma^{-k}
D(w)P_1D(w)^{-1}\frac{f^{(k)}(x_p)}{k!}.
\tag{30}
\]

不存在 \(P_1\) 時令其為零。故 \(R_k(w)\) 是有限秩、\(w\)-全純族，且

\[
\operatorname{rank}R_k(w)\leq\operatorname{rank}P_1
=\dim\ker(J-I).
\tag{31}
\]

從 (19) 減去 (30) 的主部，僅改動有限個低階項；其餘項繼續满足 (21)。再使用 (28)–(29)，得到 (10) 的核理想全純 remainder。這同時排除移動極點與高階極點。引理證畢。

## 4. P31 的兩個 block 拼合，以及嚴格停止線

將引理分別用於 (2) 的兩条共軛後分支，有

\[
\mathcal L(z,w)=
\begin{pmatrix}0&T_1(z,w)\\T_2(z,w)&0\end{pmatrix}:B\to B,
\quad
T_i(z,w)=M_{D_i(w)}T_i^0(z)M_{D_i(w)^{-1}}.
\tag{32}
\]

固定的 block injection/projection 有界，故 (7) 與單分支引理立即給：\(\mathcal L\) 在每個 \(\mathcal N_q(B)\)、\(0<q\leq1\)，均為 §2 意義的聯合亞純族，候選极點仍只有 (13)，且

\[
\operatorname{Res}_{z=z_k}\mathcal L(z,w)
=\begin{pmatrix}0&R_{1,k}(w)\\R_{2,k}(w)&0\end{pmatrix},
\qquad
\operatorname{rank}\operatorname{Res}\leq
\dim\ker(J_1-I)+\dim\ker(J_2-I)\leq2d.
\tag{33}
\]

兩個 \(D_i\) 不必相同。(32) **不**宣稱整個 \(\mathcal L(z,w)\) 是 \(\mathcal L(z,0)\) 的單一全局共軛，也不宣稱其 spectrum 不依賴 \(w\)。

本文閉合的僅是共同 Banach 模型、初始分支和、局部一致 order-0 核展開、雙參數核理想亞純性及固定有限秩 residue。由此到 Fredholm determinant 參數族、其極點階、與原軌道乘積的等式、再到實際曲線 \((z,w)=(s,s)\)、\((s+1,s)\) 的合法限制，仍須分別論證；本文不把任一項當作既成結論。固定時鐘參數 \(\epsilon\) 已包含在 \(\eta_w\) 中，不再重複乘入曲線參數。沒有執行科學程式、重新生成資料或變動既有停止線。
