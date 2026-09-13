# P31 Goal01：真實物理時間的 flat supertrace 與 Euler 全導數

日期：2026-09-09 UTC。這是既有 P31 流的內部紙面證明。
只新增本筆記，不改變時鐘、owner、舊輸入、正式稿、Route 或 Stage。

**結論。** 對同一真實換時流與固定酉局部系，三個橫向外冪傳播子
均有合法的正時間 distributional flat trace。它們的負交替和是
\[
\mathcal T_{\varepsilon,\nu}
=\sum_{P\ {\rm primitive,oriented}}\sum_{r\ge1}
 T_\varepsilon(P)\operatorname{tr}(\nu(P)^r)
 \delta_{rT_\varepsilon(P)}.
\tag{1}
\]
在 \(\Re s>2/c_0\)，其絕對 Laplace 變換等於
\(D_\varepsilon'(s)/D_\varepsilon(s)=-\zeta_\varepsilon'(s)/\zeta_\varepsilon(s)\)。
這裡必須使用本原物理時間作分子、測地長度作橫向返回指數，
並在雙參 determinant 上取兩條曲線各自的全導數。

本筆記採用 [P29 正時間機制][p29flat]與[橫向外代數機制][p29alt]
的局部思路，但重新證明本案的非恆定時鐘、rank-two 符號、
非緊推送與無窮時間界。P29 的正號及常數時鐘推送不能原樣搬用。

## 1. 固定同一流、局部系及既有输入

令
\[
Y=Y_0(11),\qquad M=S_gY,\qquad
\alpha=\operatorname{Re}(2\pi i f(z)\,dz),\qquad
\rho_\varepsilon=1+\varepsilon\alpha(u).
\tag{2}
\]
\(g\) 是曲率 \(-1\) 的完整雙曲度量；
\(\varepsilon\in\mathbb R\) 固定，且對所有 \(g\)-單位向量
\[
0<c_0\le\rho_\varepsilon\le C_0:=2-c_0,\qquad
X:=X_\varepsilon=X_{\rm geo}/\rho_\varepsilon.
\tag{3}
\]
上界來自將原正性條件同時用於 \(u\) 與 \(-u\)，不是新的假設。
[Contact/Randers 筆記][contact]已證明 \(X\) 完整、無零點，並且是
\[
\lambda_\varepsilon=\lambda_{\rm geo}+\varepsilon\pi^*\alpha
\tag{4}
\]
的 Reeb 場。以 \(\Phi^t\) 記其物理時間流，以 \(\phi_0^\tau\)
記原來的單位速度測地流。

令 \(\mathcal V_\nu\to Y\) 是[自然 holonomy 筆記][holonomy]中的
固定 rank-\(m\) 酉平坦局部系，\(m\ge1\)，再拉回至 \(M\)。
沿一條正向閉流圈 \(P\) 的平行移動，按同一既定 convention 記為
\(\nu(P)\)，起點改變只作共軛。係數及 connection 不依賴
Laplace 參數 \(s\)。
下文不把 \(\eta_s\) 或 \(\nu e^{-s\varepsilon I}\) 放入傳播子；
時鐘已由 \(X\) 與真實時間 \(t\) 承擔。

以 \(\mathcal P_\Gamma\) 記同一有向本原流軌道集合，並置
\[
\ell_P=\ell_g(P),\quad T_P=T_\varepsilon(P)
 =\ell_P+\varepsilon I(P),\quad
c_0\ell_P\le T_P\le C_0\ell_P.
\tag{5}
\]
不額外取 inverse quotient，也不把不同 owner 的同數值周期合併。
[Euler 收斂筆記，§3][euler]已證
\[
\ell_P\ge\ell_*:=2\operatorname{arcosh}(3/2)>0,\qquad
N_\Gamma(L):=\#\{P:\ell_P\le L\}\le192e^{2L}.
\tag{6}
\]
這是所有有向本原類的紙面上界，並非 frozen population 的枚舉。

## 2. 非恆定換時不改變 Poincaré 返回映射

取 \(x\) 在本原軌道 \(P\) 上，選同時橫截 \(X_{\rm geo}\) 與
\(X\) 的局部截面 \(\Sigma\)。兩場逐點正比例，故軌道路徑及方向相同。
若 \(\tau(y)\) 是靠近 \(\ell_P\) 的測地返回時間，則物理返回時間為
\[
t(y)=\int_0^{\tau(y)}\rho_\varepsilon(\phi_0^u y)\,du,
\]
而截面返回映射逐點相等：
\[
\mathcal R_\varepsilon(y)=\Phi^{t(y)}y
 =\phi_0^{\tau(y)}y=\mathcal R_0(y).
\tag{7}
\]
這不是把 \(t(y)\) 誤當常數；兩個返回時間一般不同且依賴 \(y\)。

微分 \(\mathcal R_\varepsilon(y)=\Phi^{t(y)}y\)，在周期點得
\[
D\mathcal R_\varepsilon(x)w
 =D\Phi^{T_P}(x)w+X_x\,dt_x(w).
\tag{8}
\]
在 normal quotient \(T_xM/\mathbb RX_x\) 中，第二項消失。
因此兩個流的 normal return 都與同一 \(D\mathcal R_0(x)\) 共軛。

由 Reeb 不變性，\(\xi_\varepsilon:=\ker\lambda_\varepsilon\)
是一個光滑、流不變的 rank-two 平面束，
\[
TM=\mathbb RX\oplus\xi_\varepsilon.
\]
它向 normal quotient 的投影為同構。以下明定正時間返回
\[
Q_P:=D\Phi^{T_P}(x)|_{\xi_{\varepsilon,x}}.
\tag{9}
\]
沿曲率 \(-1\) 的測地線，標量法向 Jacobi 方程為 \(J''-J=0\)；
在 \((J,J')\) 資料上，一次測地返回的矩陣為
\[
\begin{pmatrix}\cosh\ell_P&\sinh\ell_P\\
                \sinh\ell_P&\cosh\ell_P\end{pmatrix}.
\]
這裡 \(Y\) 有向，法向框架可由正向單位切向量旋轉九十度給出；
閉路返回時該框架也返回，不另生負號。結合 (7)--(9)，
\[
\operatorname{Spec}Q_P=\{e^{\ell_P},e^{-\ell_P}\},\qquad
\det Q_P=1.
\tag{10}
\]
特別地，第 \(r\) 次 normal return 沒有特徵值 \(1\)。
其指數是 \(r\ell_P\)，不是 \(rT_P\)。

對 \(L=r\ell_P>0\)，直接計算
\[
\det(I-Q_P^{-r})
=(1-e^{-L})(1-e^L)
=-4\sinh^2(L/2)<0,
\tag{11}
\]
\[
\mathcal D_{P,r}:=|\det(I-Q_P^{-r})|
=e^L(1-e^{-L})^2
=|\det(I-Q_P^r)|.
\tag{12}
\]
這個確切負號是本案負 supertrace 的來源。

## 3. 固定係數的三個實際傳播子

令
\[
E_0^*=\operatorname{ann}(X)\subset T^*M,\qquad
\mathcal E_k=\Lambda^k(E_0^*\otimes\mathbb C)\otimes\pi^*\mathcal V_\nu,
\quad k=0,1,2.
\tag{13}
\]
因 \(X\) 與 \(X_{\rm geo}\) 正比例，兩者的 annihilator 相同。
這裡不是完整 \(\Lambda^*T^*M\)：完整外代數含流方向的返回特徵值
\(1\)，其交替跡會額外乘 \(1-1\) 而成為零。

對 \(y=\Phi^{-t}x\)，定義
\[
(U_{k,\nu}(t)a)(x)
=\left(\Lambda^k(D\Phi^{-t}_x)^{\mathsf T}
       \otimes\mathcal P^+_{y\to x}\right)a(y).
\tag{14}
\]
\({}^{\mathsf T}\) 指代數對偶 pullback，不是 Hermitian adjoint。
\(\mathcal P^+\) 沿 \(v\mapsto\Phi^{v-t}x\)、\(0\le v\le t\)
平行移動；對 \(t>0\)，這是從過去點沿正方向到現在點。
負時間以反向路徑定義。

由 \(D\Phi^{-t}_x X_x=X_y\)，covector pullback 保持
\(\operatorname{ann}(X)\)，故 (14) 的束型正確。
流的群律及平行傳输的路徑拼接給 \(U(t+s)=U(t)U(s)\)。
每個 \(U(t)\) 合法作用於 \(C_c^\infty(M;\mathcal E_k)\)；
有限時間區間與緊支撐的流像仍是緊集。
此處不以 trace-class 性定義任何跡。

在 \(t=rT_P\) 的周期點，橫向 covector 因子是
\((Q_P^{-r})^{\mathsf T}\)，而局部系因子是正向 \(\nu(P)^r\)。
故纖維跡為
\[
b_{k,P,r}
=\operatorname{tr}(\Lambda^k Q_P^{-r})
 \operatorname{tr}(\nu(P)^r).
\tag{15}
\]
代數對偶不改跡。沿完整周期圓周換起點，兩個因子各自被共軛，
所以 (15) 不變。逆向 covector pullback 不反轉此處正向平行移動。
若採用不同 loop/deck 慣例，須先與 [holonomy][holonomy] 的
正向約定對齊，不能靜默把 \(\nu(P)^r\) 改成 \(\nu(P)^{-r}\)。

## 4. 正時間聯合核的合法對角拉回

選任意光滑正密度 \(dm\)，例如 (4) 的 contact 密度。
令 \(K_{k,m}(t,x,y)\) 是 (14) 相對 \(dm(y)\) 的聯合 Schwartz 核。
它是支撐在光滑圖形
\[
\mathcal G=\{(t,x,y):t>0,\ y=\Phi^{-t}x\}
\]
上的 delta 核，乘上一個光滑有限維束映射。
局部 \(dm(y)=m(y)\,dy\) 時，scalar 部分是
\(m(y)^{-1}\delta(y-\Phi^{-t}x)\)。

圖形的非零 conormal covector 具有形式
\[
\bigl(\eta(X_y),-(D\Phi^{-t}_x)^{\mathsf T}\eta,\eta\bigr),
\qquad 0\ne\eta\in T_y^*M.
\tag{16}
\]
光滑密度及束因子不擴大這個 wavefront 包含關係。
聯合對角嵌入 \(i(t,x)=(t,x,x)\) 的非零 conormal 為
\((0,\zeta,-\zeta)\)。可能的相交因此必須滿足
\[
\Phi^{-t}x=x,\quad \eta(X_x)=0,\quad
(D\Phi^{-t}_x)^{\mathsf T}\eta=\eta.
\tag{17}
\]
周期點的 \(\eta\) 已在 \(E_0^*\)；(10) 排除該返回的固定非零
covector，因此 (17) 強迫 \(\eta=0\)，矛盾。
標準 wavefront pullback 判準遂給合法的 \(i^*K_{k,m}\)。
取對角纖維跡，記所得 scalar 分佈為 \(W_{k,m}(t,x)\)。

這個計算直接使用 \(X\ne0\) 及週期 normal return 非退化；
不另假設一個全局 Anosov splitting 或非緊空間上的一致微局部估計。
時間變量必須保留：不能先在某個周期時間取 fixed-time 對角跡，
再聲稱得到了本節的聯合分佈。
局部拉回與後述 delta 換元的來源接口是
[Dyatlov--Zworski Appendix B，(B.2)--(B.6)][dz]；
其緊流形全局結論不代替下一節本案的非緊推送。

## 5. 有限物理返回包與非緊 proper 推送

令 \(J=[a,b]\Subset(0,\infty)\)。若 \(rT_P\in J\)，則由 (5)--(6)
\[
\ell_P\le b/c_0,\qquad r\le b/(c_0\ell_*).
\tag{18}
\]
前者只容許有限個 \(P\)，後者只容許有限個正整數 \(r\)。
每個 \(P\) 的全部相狀態構成一個緊的本原流圓周。
於是固定點集合在本窗口中恰為
\[
\{(t,x):t\in J,\ \Phi^t x=x\}
=\bigcup_{rT_P\in J}\{rT_P\}\times P,
\tag{19}
\]
是有限緊並。底面的閉測地線可以自交，但其完整相狀態圓周
不因此增添起點或 owner 重数；重複返回仍使用同一圓周。

固定點集合在 \((0,\infty)\times M\) 內閉，
\(\operatorname{supp}W_{k,m}\) 包含於該集合。
因此投影到時間在此支撐上 proper。
不要求所有周期軌道跨全部時間都留在同一個緊集。

具體地，對 \(h\in C_c^\infty(0,\infty)\)，選略大窗口 \(J\)，
並選 \(\chi_J\in C_c^\infty(M)\)，使它在 (19) 的全部相圓周
投影之開鄰域恆為 \(1\)。定義
\[
\langle\Theta_{k,\nu},h\rangle
:=\langle W_{k,m},h(t)\chi_J(x)\rangle_{dt\,dm(x)}.
\tag{20}
\]
兩個合格 cutoff 之差在有關分佈支撐附近為零，故 (20) 不變。
不同窗口可放進更大共同窗口比較。
對固定緊時間支撐，\(\chi_J\) 可固定，
\(h\mapsto h\chi_J\) 在測試函數拓撲連續；
因此 (20) 確實給出 \(\mathcal D'(0,\infty)\) 分佈。

cutoff 必須在整個周期相圓周的鄰域形成 plateau；
僅在圓周點上等於 \(1\)，或只在每條軌道與某截斷核的交點等於
\(1\)，都不是上述支撐證明。合格的 compact-plateau exhaustion
對每個 \(h\) 最終精確穩定，不需要交換無窮時間與空間極限。

若 \(dm'=q\,dm\)，則
\[
K_{k,m'}(t,x,y)=q(y)^{-1}K_{k,m}(t,x,y),\qquad
W_{k,m'}=q(x)^{-1}W_{k,m}.
\tag{21}
\]
(20) 的積分密度同時乘 \(q(x)\)，所以抵消。
由此 \(\Theta_{k,\nu}=\operatorname{tr}_+^\flat U_{k,\nu}\)
與所選光滑正密度無關。

## 6. 局部 delta 係數及本原物理分子

固定 \(x_0\in P\)、\(t_0=rT_P>0\)。取物理 flow-box 座標
\((u,w)\in\mathbb R\times\mathbb R^2\)，使 \(X=\partial_u\)、
周期弧為 \(w=0\)，並令截面在 \(x_0\) 與
\(\xi_{\varepsilon,x_0}\) 相切。寫
\[
\Phi^{-t_0}(0,w)=(f_0(w),A_0(w)),\qquad f_0(0)=0,\ A_0(0)=0.
\]
在足夠小的聯合鄰域內，流的群律給
\[
\Phi^{-t}(u,w)
=(u-t+t_0+f_0(w),A_0(w)).
\tag{22}
\]
可用 (21) 選座標 Lebesgue 密度。scalar 對角核是
\[
\delta(w-A_0(w))\,\delta(t-t_0-f_0(w)).
\tag{23}
\]
\(dA_0(0)\) 是反時間 normal return 的截面表示，與
\(Q_P^{-r}\) 共軛。因此 \(I-dA_0(0)\) 可逆，
在足夠小鄰域中 \(w=A_0(w)\) 的唯一解是 \(0\)。
先對 \(w\) 作 delta 換元，再用 \(f_0(0)=0\)，得到
\[
\frac{1}{\mathcal D_{P,r}}\delta(w)\delta(t-t_0).
\tag{24}
\]
這是零階 delta density，沒有附帶 delta 導數。
束因子在 (24) 上取值為 (15)。

對緊時間窗內的有限相圓周作有限 flow-box 覆蓋與
partition of unity，局部係數合成後沿每個本原圓周積分一次。
\(u\) 是物理時間，故該積分長度是 \(T_P\)，不是
\(\ell_P\)、\(rT_P\) 或另外再乘一個 \(\rho_\varepsilon\)。
因而
\[
\boxed{\displaystyle
\Theta_{k,\nu}
=\sum_{P\in\mathcal P_\Gamma}\sum_{r\ge1}
\frac{T_P\,\operatorname{tr}(\nu(P)^r)\,
      \operatorname{tr}(\Lambda^k Q_P^{-r})}
     {\mathcal D_{P,r}}\,
\delta_{rT_P}
 \quad\text{於 }\mathcal D'(0,\infty).}
\tag{25}
\]
所有方向及重複均由 \(P,r\) 計入，不另乘 \(2\) 或 \(r\)。
式 (25) 現在是真實聯合核的跡，而不只是所指定的 formal 軌道和。
有界時間窗的有限性也表明它是局部複 Radon 測度。

## 7. rank-two 的負 supertrace

對二維線性映射 \(Q\)，外代數恆等式為
\[
\sum_{k=0}^2(-1)^k\operatorname{tr}(\Lambda^kQ)=\det(I-Q).
\tag{26}
\]
結合 (11)、(12)、(25)，定義
\[
\mathcal T_{\varepsilon,\nu}:=
-\sum_{k=0}^2(-1)^k\Theta_{k,\nu}.
\tag{27}
\]
則每個返回項的橫向係數恰為
\(-\det(I-Q_P^{-r})/|\det(I-Q_P^{-r})|=1\)，得到 (1)。
這是三個合法分佈的有限線性組合，沒有無窮 degree 重排。
對平凡 rank-one 局部系，(1) 是正測度；
一般固定酉 \(\nu\) 時允許其跡及同時間包發生相消。
scalar \(k=0\) 的跡本身仍保留 (12) 的完整分母。

## 8. 每一 degree 與物理導數的共同絕對 Laplace 域

令 \(q_*=e^{-\ell_*}<1\)、\(L=r\ell_P\)。由 (10)--(12)，
\[
\frac{|\operatorname{tr}\Lambda^kQ_P^{-r}|}{\mathcal D_{P,r}}
=
\begin{cases}
\dfrac{e^{-L}}{(1-e^{-L})^2},&k=0,2,\\[5pt]
\dfrac{1+e^{-2L}}{(1-e^{-L})^2},&k=1.
\end{cases}
\tag{28}
\]
因此可統一取
\[
a_0=a_2=(1-q_*)^{-2},\qquad a_1=2(1-q_*)^{-2}
\tag{29}
\]
作逐 degree 上界。特別是 \(k=1\) 分子的 \(e^L\) 已被分母的
\(e^L\) 抵消，不需再損失一個測地指數。

對 \(\sigma>2/c_0\)，置 \(A=c_0\sigma>2\)。先估計
\[
S_1(A):=\sum_P\ell_Pe^{-A\ell_P}.
\]
因
\(\ell e^{-A\ell}\le A\int_\ell^\infty x e^{-Ax}\,dx\)，
非負 Tonelli 與 (6) 給
\[
\begin{aligned}
S_1(A)
&\le A\int_{\ell_*}^{\infty}xN_\Gamma(x)e^{-Ax}\,dx\\
&\le
192A e^{-(A-2)\ell_*}
\left(\frac{\ell_*}{A-2}+\frac{1}{(A-2)^2}\right)
=:C_1(A)<\infty.
\end{aligned}
\tag{30}
\]
此推導保留 \(\ell_*\) 處可能的原子，不先假定該和有限。
再用 \(T_P\le C_0\ell_P\)、\(T_P\ge c_0\ell_P\)
及 \(|\operatorname{tr}\nu(P)^r|\le m\)，得到
\[
\begin{aligned}
H(\sigma)
&:=\sum_{P,r\ge1}T_P|\operatorname{tr}\nu(P)^r|
                  e^{-\sigma rT_P}\\
&\le\frac{mC_0}{1-e^{-A\ell_*}}S_1(A)
\le\frac{mC_0C_1(A)}{1-e^{-A\ell_*}}<\infty.
\end{aligned}
\tag{31}
\]
這是物理導數所需的額外 \(T_P\) 因子界，不能只引用未微分的
\(1/r\) log 級數收斂。

由 (25)、(28)--(31)，
\[
\int_0^\infty e^{-\sigma t}\,d|\Theta_{k,\nu}|(t)
\le a_k H(\sigma),\qquad
\int_0^\infty e^{-\sigma t}\,d|\mathcal T_{\varepsilon,\nu}|(t)
\le H(\sigma).
\tag{32}
\]
第一個不等式允許同時間項相消，故以逐返回絕對和支配總變差即可。
所有 degree 都有共同充分域 \(\Re s>2/c_0\)；
不宣稱這是它們各自的精確收斂邊界。
固定 \(\sigma_0>2/c_0\) 後，(31)--(32) 一致支配
\(\Re s\ge\sigma_0\)，所以相應級數局部正常收斂且其 Laplace
變換全純，並可有限相加。

## 9. 同一 Euler 函數及雙參曲線的全導數

沿用既有 inverse-product convention，於 \(\Re s>2/c_0\) 有
\[
D_\varepsilon(s)
=\prod_{P\in\mathcal P_\Gamma}
\det(I_m-e^{-sT_P}\nu(P)),\qquad
\zeta_\varepsilon=D_\varepsilon^{-1}.
\tag{33}
\]
[Euler 筆記][euler]已證其非零全純性與規範 trace-log：
\[
\log D_\varepsilon(s)
=-\sum_{P,r\ge1}\frac{\operatorname{tr}\nu(P)^r}{r}
                         e^{-srT_P}.
\tag{34}
\]
式 (31) 合法支配 (34) 的逐項導數。由 (1)、(27)、(32)，
\[
\boxed{\displaystyle
\frac{D_\varepsilon'(s)}{D_\varepsilon(s)}
=-\frac{\zeta_\varepsilon'(s)}{\zeta_\varepsilon(s)}
=\int_0^\infty e^{-st}\,d\mathcal T_{\varepsilon,\nu}(t)
=-\sum_{k=0}^2(-1)^k
  \int_0^\infty e^{-st}\,d\Theta_{k,\nu}(t).
}
\tag{35}
\]
這個等式先是已構造的時間分佈之絕對 Laplace 變換，
不交換時間積分與未經定義的普通算子跡。

[聯合 determinant 筆記][joint]已證同一解析芽及全平面亞純身份
\[
D_\varepsilon(s)=\frac{\Delta(s,s)}{\Delta(s+1,s)},\qquad
\Delta(z,w)=\det(I-\mathcal L(z,w)).
\tag{36}
\]
右域中兩項都非零；鏈式法則把 (35) 寫成
\[
\boxed{\displaystyle
\frac{D_\varepsilon'}{D_\varepsilon}(s)
=
\frac{(\partial_z+\partial_w)\Delta(s,s)}{\Delta(s,s)}
-
\frac{(\partial_z+\partial_w)\Delta(s+1,s)}{\Delta(s+1,s)}.
}
\tag{37}
\]
兩條曲線 \((s,s)\)、\((s+1,s)\) 的切向量都是 \((1,1)\)。
分母 coefficient parameter 仍是 \(w=s\)，不是 \(s+1\)。
只取 \(\partial_z\) 會漏掉閉形式時鐘的 \(\varepsilon I(P)\)，
不能得到 (35) 的本原物理分子。
式 (37) 沒有額外再乘 \(\varepsilon\)：它已包含在既定
\(\eta_w=\operatorname{Ind}(\nu e^{-w\varepsilon I})\) 中。

由已證 (36)，(35) 的全純 Laplace 函數具有 (37) 指定的亞純
延拓；這不是聲稱原 Laplace 積分在右域外收斂。
本頁也不把 \(\mathcal L(z,w)\) 與 (14) 當作同一算子：
它们的接口是精確相同的物理閉軌道函數及 (35)--(37)。

## 10. 邊界、來源及實際檢查

本頁閉合的是同一固定 \(\nu\)、同一 \(X_\varepsilon\) 的正時間
聯合核、非緊 proper 推送、負橫向 supertrace 與 Euler 全導數。
未構造零時間項、普通 Hilbert 空間跡、resolvent flat trace、
共振／scattering 展開或量子算子；不改任何 Route 或 Stage。
Reeb/Randers 與上述跡公式也不推出額外曲率或自伴谱結論。

本輪完整讀取 [P29 positive-time][p29flat]與[外代數筆記][p29alt]
的局部機制，並讀取本案的 [contact][contact]、[holonomy][holonomy]、
[計數/Euler][euler]與[聯合 determinant][joint]相關輸入。
另直接核讀 Dyatlov--Zworski 作者稿 arXiv:1306.4203v4
Appendix B 的 (B.2)--(B.6)、Lemma B.1 及其局部 delta 換元。
來源原文以緊流形為背景；本案非緊步驟是 §§4--6 的自含補充，
不是引用一個未核查的非緊全局定理。

ARS 的有界論證寫作規範用於分離：真實傳播子、局部拉回、
非緊支撐、無窮時間收斂及 scalar determinant 身份。
這是 AI 輔助內部證明，不是形式驗證或新穎性認證。
另一同模型席只核對返回符號、逐 degree 比值、(30)--(31)
和全導數；其同意不是外部獨立科學證據。

本輪唯一授權寫入是以 apply_patch 新增本文件，隨後對新文件作
一次全文靜態回讀。沒有執行科學、符號、枚舉、census、producer、
實驗、正式 verifier 或稿件 build；不改舊文件與歷史失敗紀錄。
靜態文字檢查不認證數學正確性。

[contact]: internal_goal01_same_clock_contact_and_randers_realization_20260909.md
[holonomy]: internal_goal01_natural_holonomy_and_induced_transfer_20260909.md
[euler]: internal_goal01_induced_euler_product_absolute_convergence_20260909.md
[joint]: internal_goal01_joint_classical_determinant_and_clock_continuation_20260909.md
[p29flat]: ../../29-bianchi-ideal-owner-refinement/notes/internal_goal01_positive_time_flat_trace_realization_20260909.md
[p29alt]: ../../29-bianchi-ideal-owner-refinement/notes/internal_goal01_transverse_supertrace_and_classical_ruelle_interface_20260909.md
[dz]: https://arxiv.org/pdf/1306.4203v4
