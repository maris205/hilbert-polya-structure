# P30 內部論證：雙向無限盤字的唯一實現與 roof 的指數局部性

記錄日期：2026-09-09 UTC。使用者授權第五次 P29–33 五篇整輪內部理論推進；本分支只新建本檔，不改現稿、舊筆記、程式、資料、owner 規則或正式狀態。

固定原有等邊三圓盤、中心間距 `6a`、半徑 `a>0`、單位歐氏速率和逐碰撞截面。本輪將[有限週期實現][periodic]推進到全部雙向容許盤字，並直接證明唯一性及定量連續性。關鍵是一個只用於證明的同步更新，其收縮率為

\[
\boxed{\rho=\frac1{2\kappa_*}
=\frac3{2\sqrt6-1}<1,\qquad
\kappa_*:=\cos\left(\frac\pi6+\arcsin\frac13\right)>
\frac12.}
\tag{1}
\]

若兩個雙向盤字在 `[-m,m]` 一致，則對 `m>=1`，其真實碰撞後狀態與原物理 roof 滿足

\[
\boxed{
|q_0-\widetilde q_0|\le2a\rho^m,\qquad
d_a(x_0,\widetilde x_0)\le3a\rho^{m-1},\qquad
|\tau-\widetilde\tau|\le4a\rho^{m-1}.}
\tag{2}
\]

這些是本檔自含推導的內部數學結論，不是已執行的數值收斂測試、形式化證明器結果或正式 Gate 證書。同步更新不等於物理碰撞映射，也不改變物理時鐘。

## 1. 固定物件及一個適用於盤內點的方向估計

保持

\[
C_1=(0,0),\quad C_2=(6a,0),\quad C_3=(3a,3\sqrt3a),
\qquad K_j=\overline B(C_j,a).
\tag{3}
\]

現稿仍取 `a=1`；保留 `a` 只顯示量綱。不同圓盤中的任意兩點距離在 `[4a,8a]`。三個互異標記有

\[
\operatorname{dist}\bigl(K_i,\operatorname{conv}(K_j\cup K_k)\bigr)
=(3\sqrt3-2)a>0.
\tag{4}
\]

因兩盤凸包是線段 `[C_j,C_k]` 加半徑 a 的閉球，而第三中心到該線段距離為等邊高 `3sqrt(3)a`，減去兩個半徑即得 (4)。這個 no-eclipse 間隔將用於排除第三盤首撞。

[統一非擦邊筆記][nongrazing]的方向估計實際只使用點到中心的距離不超過 a，所以也適用於閉盤內點。為使下面沿內插路徑微分不留下前提缺口，這裡重新證明。

取 `p in K_j`、`q in K_i`、`i!=j`，寫 `p-q=c+e`，其中 `c=C_j-C_i`、`|c|=6a`、`|e|<=2a`。由 `c·(c+e)>0`，向量 `p-q` 與 c 的夾角位於 `[0,pi/2)`。c 到直線 `R(p-q)` 的垂距不超過 `|e|`，故該夾角不超過

\[
\delta:=\arcsin(1/3)<\pi/6.
\tag{5}
\]

現在令 `p in K_j`、`q in K_i`、`r in K_k`，其中 `j!=i`、`k!=i`，但允許 `j=k`。定義

\[
u=\frac{p-q}{|p-q|},\qquad w=\frac{r-q}{|r-q|},\qquad S=u+w.
\tag{6}
\]

若 `j=k`，兩射線夾角至多 `2delta`；若 `j!=k`，至多 `pi/3+2delta`。兩種情形都給

\[
\boxed{|S|=2\cos\bigl(\angle(u,w)/2\bigr)
\ge2\kappa_*>1.}
\tag{7}
\]

這是對全部可行三點組態的估計，沒有先要求它們是反射點、被困點或週期點。由 `sin(delta)=1/3` 展開 (1) 可得 `kappa_*=(2sqrt(6)-1)/6`。

## 2. 無限配置上的局部同步更新及全局收縮

令

\[
\Sigma:=\{s\in\{1,2,3\}^{\mathbb Z}:s_i\ne s_{i+1}
\text{ for every }i\in\mathbb Z\},\qquad
\mathcal X_s:=\prod_{i\in\mathbb Z}K_{s_i}.
\tag{8}
\]

先固定一個 s。在 `X_s` 上使用

\[
\|q-\widetilde q\|_\infty:=\sup_{i\in\mathbb Z}|q_i-\widetilde q_i|.
\tag{9}
\]

同一配置空間中此距離不超過 `2a`。它是完備距離：一致 Cauchy 配置逐座標有極限，每個閉盤保留該極限；一致 Cauchy 條件再使收斂在 (9) 中一致。

定義紙面的同步更新 `P_s:X_s→X_s`：

\[
\begin{aligned}
S_i(q)&:=\frac{q_{i-1}-q_i}{|q_{i-1}-q_i|}
       +\frac{q_{i+1}-q_i}{|q_{i+1}-q_i|},\\
(\mathscr P_s q)_i&:=C_{s_i}+a\frac{S_i(q)}{|S_i(q)|}.
\end{aligned}
\tag{10}
\]

由跨盤距離及 (7)，全部分母均有正下界；更新後每個座標在相應盤邊界，故此式確實映回 `X_s`。它的第 i 個座標只依賴位置 `i-1,i,i+1` 的點和第 i 個盘標記。

### 2.1 直接差商，不假設端點之間仍是物理軌道

對非零向量 z，令 `nu(z)=z/|z|`。逐項微分得

\[
D\nu(z)h=\frac{(I-\nu(z)\nu(z)^\mathsf T)h}{|z|},\qquad
|D\nu(z)h|\le\frac{|h|}{|z|}.
\tag{11}
\]

取同一 `X_s` 中 q、qtilde，沿 `q(t)=(1-t)q+t qtilde`、`0<=t<=1` 內插。此路徑留在閉盤積中，雖然一般不是真實軌道。令 `b_i=|q_i-qtilde_i|`。由 (11) 及每個跨盤距離至少 `4a`，

\[
\left|\frac{d}{dt}S_i(q(t))\right|
\le\frac{b_{i-1}+2b_i+b_{i+1}}{4a}.
\tag{12}
\]

(7) 在整條內插路徑上成立，再對 (10) 的外層正規化使用 (11)，積分即得

\[
\boxed{|(\mathscr P_s q)_i-(\mathscr P_s\widetilde q)_i|
\le\frac{b_{i-1}+2b_i+b_{i+1}}{8\kappa_*}.}
\tag{13}
\]

取上確界，得到

\[
\boxed{\|\mathscr P_s q-\mathscr P_s\widetilde q\|_\infty
\le\rho\|q-\widetilde q\|_\infty,\qquad \rho<1.}
\tag{14}
\]

因此收縮常數獨立於無限盤字。這裡不把被困集上的端點導數界擴大為任意路徑界；(7) 已另外驗證全部閉盤配置和整條內插路徑。

### 2.2 存在、唯一性及中心初值誤差

令 `c(s)_i=C_(s_i)`，並在紙面定義 `q^(m)=P_s^m c(s)`。由 (10)，`||q^(1)-q^(0)||∞=a`；反覆使用 (14)，

\[
\|q^{(m+1)}-q^{(m)}\|_\infty\le a\rho^m.
\tag{15}
\]

幾何級數尾界使此序列一致 Cauchy，故收斂於 `q(s) in X_s`。由 (14) 的連續性，`P_s q(s)=q(s)`。若另外有固定點 r，則 `||q(s)-r||∞<=rho||q(s)-r||∞`，有限性與 `rho<1` 迫使兩者相等。這給出每個雙向盤字的唯一固定配置，不依賴一個未說明的無限維存在性定理。

固定點的每個座標均在盤邊界，故 `||c(s)-q(s)||∞=a`。把固定點與初始中心配置代入 (14) 的 m 次迭代，得到比級數尾和更簡潔的誤差界：

\[
\boxed{\|\mathscr P_s^m c(s)-q(s)\|_\infty\le a\rho^m,
\qquad m\ge0.}
\tag{16}
\]

(15) 先證明極限存在，之後才以固定點的邊界位置推出 (16)，次序沒有循環。

## 3. 固定配置恰好是真實雙向被困軌道

### 3.1 固定點給正確反射法則

在固定點令 `n_i=(q_i-C_(s_i))/a`，`ell_i=|q_(i+1)-q_i|`，以及

\[
v_i^-:=\frac{q_i-q_{i-1}}{\ell_{i-1}},\qquad
v_i^+:=\frac{q_{i+1}-q_i}{\ell_i},\qquad
\chi_i:=|S_i(q)|/2\ge\kappa_*.
\tag{17}
\]

(10) 的固定點條件給 `-v_i^-+v_i^+=2chi_i n_i`。兩個向外射線 `-v_i^-` 與 `v_i^+` 都是單位向量，它們各自與其和方向的內積為和長的一半。因此

\[
v_i^-\cdot n_i=-\chi_i<0,\qquad
v_i^+\cdot n_i=\chi_i>0,\qquad
v_i^+=v_i^--2(v_i^-\cdot n_i)n_i.
\tag{18}
\]

法向符號、非擦邊性與鏡面反射均由固定點方程得到，不把角平分線公式直接當成尚未驗證的物理反射。

### 3.2 每段都是首次飛行，且全部物理時間均被覆蓋

從 q_i 沿 `v_i^+` 飛行 `ell_i`。對 `0<t<ell_i`，相對出發圓盤，

\[
|q_i+t v_i^+-C_{s_i}|^2
=a^2+2at(v_i^+\cdot n_i)+t^2>a^2.
\tag{19}
\]

令 `r=ell_i-t>0`，從终點向後看，並用 `v_i^+=v_(i+1)^-`，

\[
|q_{i+1}-r v_i^+-C_{s_{i+1}}|^2
=a^2-2ar(v_i^+\cdot n_{i+1})+r^2>a^2.
\tag{20}
\]

整段在兩端圓盤的凸包內，由 (4) 避開第三圓盤。三項一起排除中途接觸或更早首撞。又有 `4a<=ell_i<=8a`，所以向正、負方向累加飛行時間均趨向無窮，沒有有限時間的無限碰撞累積。取第 0 次碰撞時間為零，逐段接合就定義了所有實數時間上的單位速率物理軌道。

全部段都在三個圓盤的共同凸包中，故軌道在兩個時間方向皆有界。令 `T_coll` 為全部真實雙向被困碰撞後狀態，則本構造給

\[
H(s):=(q_0(s),v_0^+(s))\in T_{\mathrm{coll}},\qquad
\tau(s):=\ell_0(s)\in[4a,8a].
\tag{21}
\]

### 3.3 任意真實被困軌道都是這個固定點

反向橋接不可由唯一固定點自行省略。對任意真實雙向被困軌道，任一時間方向若只有有限次接觸，其後就是無限長單位直線，與有界性矛盾。從任一圓盤向外出射的平方距離公式 (19) 也排除下一次仍撞同盤；跨盤下界 `4a` 排除碰撞累積。因此碰撞可按全部整數編號，其盤字在 Sigma 中。

在任一碰撞，鏡面反射給 `S_i=2chi_i n_i`，其中 `chi_i>=0`；此論證即使先允許候選切觸也成立。對真實鄰點使用 (7)，有 `|S_i|>=2kappa_*`，所以 `chi_i>=kappa_*>0`。於是每一點恰滿足 (10)，整個真實配置是 `P_s` 的固定點。由 §2.2，它只能等於 q(s)。

所以每個雙向容許盤字恰有一個帶碰撞索引的真實實現，且全部雙向被困碰撞狀態均被 H 覆蓋。若兩個盤字给出同一碰撞後狀態，向前的首次飛行唯一；向後则先以反射的對合公式恢復入射速度，再反向作唯一首次飛行。全部先後標記因此相同，H 也是單射。這保留原盤標記及時間方向，沒有對幾何對稱或反轉額外取商。

## 4. 有限依賴推出指數 locality 與 symbolic Hölder roof

### 4.1 迭代只看有限中心塊

由 (10) 的三點局部性和中心初值可作歸納：`(P_s^m c(s))_i` 只依賴盤字的區間 `[i-m,i+m]`。初始 m=0 只看 s_i；再作一次更新只合併三個相鄰依賴區間。此為精確的有限依賴，不是忽略遠端的近似假設。

故若兩個盤字在 `[i-m,i+m]` 一致，它們的第 i 個 m 次近似完全相同。對兩端各用 (16)，

\[
\boxed{|q_i(s)-q_i(\widetilde s)|\le2a\rho^m.}
\tag{22}
\]

特別是當兩字在 `[-m,m]` 一致時，任意 `|i|<=m` 有

\[
|q_i(s)-q_i(\widetilde s)|\le2a\rho^{m-|i|}.
\tag{23}
\]

這既是無限固定點的遠端敏感度界，也是對中心有限依賴近似的紙面誤差控制；沒有聲稱已運行該迭代或已提供浮點／區間誤差證书。

### 4.2 碰撞後速度和原時鐘 roof

對 `m>=1`，兩個實現的第 0、1 點分別在相同圓盤。內插這兩對端點時，跨盤距離始終至少 `4a`。由 (11)，

\[
|v_0^+(s)-v_0^+(\widetilde s)|
\le\frac{|q_0-\widetilde q_0|+|q_1-\widetilde q_1|}{4a}
\le\rho^{m-1}.
\tag{24}
\]

使用原[物理距離][nongrazing]

\[
d_a((q,v),(\widetilde q,\widetilde v))
:=|q-\widetilde q|+a|v-\widetilde v|,
\tag{25}
\]

由 (23)–(24) 得 `d_a(H(s),H(stilde))<=3a rho^(m-1)`。而原 roof 就是兩個碰撞點的歐氏距離，三角不等式直接給

\[
|\tau(s)-\tau(\widetilde s)|
\le|q_0-\widetilde q_0|+|q_1-\widetilde q_1|
\le4a\rho^{m-1}.
\tag{26}
\]

於是得到開頭的 (2)。本輪直接比较端點，比先接上物理 roof 的粗 Lipschitz 常數更簡洁；原有空間 Lipschitz 結論仍然相容。

### 4.3 指定符號度量及完整常數

固定任意 `0<theta<1`。若 `s!=stilde`，令

\[
N(s,\widetilde s):=\min\{|j|:s_j\ne\widetilde s_j\},\qquad
d_\theta(s,\widetilde s):=\theta^{N(s,\widetilde s)};
\quad d_\theta(s,s):=0.
\tag{27}
\]

兩段各自在某中心塊一致，則它們首尾也在較小塊一致，這直接給 d_theta 的超距離三角不等式。若 `N>=2`，用 (2) 的 `m=N-1`；若 `N=0,1`，用全局直徑界 `d_a<=10a` 和 roof 值域差至多 `4a`。其中位置直徑至多 `8a`，速度弦距至多 2。因此令

\[
\alpha_\theta:=\frac{\log\rho}{\log\theta}>0,
\]

就有對全部兩字成立的明確估計

\[
\boxed{
d_a(H(s),H(\widetilde s))
\le\frac{10a}{\rho^2}\,d_\theta(s,\widetilde s)^{\alpha_\theta},\qquad
|\tau(s)-\tau(\widetilde s)|
\le\frac{4a}{\rho^2}\,d_\theta(s,\widetilde s)^{\alpha_\theta}.}
\tag{28}
\]

常數不追求最優。特別是 `theta=1/2` 給通常中心塊度量下的正 Hölder 指數；`theta=rho` 時在該符號度量下為 Lipschitz。符號度量的選擇不是時鐘重參數化，也不意味著所有不同度量下都具有同一指數。

## 5. 雙向編碼的拓撲及逐碰撞共軛

在 (27) 的度量中，Sigma 緊致：任意盤字序列可依位置 `0,1,-1,2,-2,...` 逐次抽取每個字母固定的子序列，再取對角子序列；每個有限中心塊最終固定，極限保留相鄰不等條件，因而在 Sigma 中收斂。

(28) 給 H 連續，§3.3 給 H 到 `T_coll` 的雙射。其逆也連續：若 `H(s^(n))→H(s)` 但 `s^(n)` 不收斂於 s，則可取一個始終留在 s 某個固定度量鄰域外的子序列；緊致性再給收斂子序列，極限 t 不等於 s，但 H 的連續性迫使 `H(t)=H(s)`，與單射矛盾。故 H 是以物理距離 (25) 賦予 `T_coll` 拓撲時的同胚；也由此得到 `T_coll` 緊致。

令左移位為 `(sigma s)_i=s_(i+1)`。將固定配置 q(s) 的座標整體移一格，便滿足盤字 sigma s 的固定點方程；唯一性給 `q_i(sigma s)=q_(i+1)(s)`。由已證首次飛行，若 B 是原逐碰撞映射，

\[
\boxed{B\circ H=H\circ\sigma,\qquad
\tau(s)=|q_1(s)-q_0(s)|.}
\tag{29}
\]

這是全部真實雙向被困碰撞上的雙向拓撲編碼及原 roof 的 Hölder 正則性，不只是週期點上的有限對應。週期盤字在此構造下必給同樣週期的固定配置，且依[上輪唯一性][periodic]與既有有限實現一致；本輪不重新枚舉有限計數。

逐段以 (21) 的正時長懸掛，可恢復 §3 所構造的所有被困物理軌道及其原時間參數。這句只使用已證的實際飛行接合，不另聲稱跨反射的環境相空間光滑性。

## 6. CER、反對意見與未完成邊界

| 本輪 claim | 可逐步核對的 evidence／reasoning | 主要反對意見及處理 |
|---|---|---|
| 全部無限盤字有唯一固定配置 | 全閉盤三點界 (7)、內插差商 (13)、幾何級數與完備性 (15)–(16) | 不從有限週期存在性或名字化編碼定理直接跳到無限詞；也不把範數泛函冒稱嚴格凸 |
| 固定配置恰為全部真實雙向被困實現 | 反射符號 (18)、三類首撞排除 (19)–(20)、雙向無限時間及真實轨道的反向固定點橋接 | 唯一固定點不自行排除其他物理軌道；§3.3 另外證明所有真實實現必為固定點 |
| 狀態和原 roof 有符號 Hölder 界 | m 步精確有限依賴、中心初值誤差 (16)、端點正規化及三角不等式 (22)–(28) | 不是把物理空間 Lipschitz 誤當符號 Hölder；兩種度量間的定量橋接已明列 |
| 編碼是全部被困碰撞的雙向拓撲共軛 | 真實先後首撞的唯一性、對角緊致性及位移固定點等變性 (29) | 不以僅向前 itinerary 取代完整狀態；明確使用兩個時間方向 |

以上是同一幾何物件上的直接證明鏈，不把多個模型或同伴的同意計為獨立科學證據。ARS argument-builder 的 CER 和反對意見要求，具體影響了本檔對「固定點→物理軌道」及反向橋接的分離書寫。

本輪填補上輪尚未建立的全部雙向盤字實現、唯一性、編碼連續性和指定符號度量下 roof Hölder 缺口。但仍未完成或授權：

- 物理微分動力系統的穩定／不穩定切束、雙曲性常數、光滑 Markov 矩形或相應算子空間構造。紙面更新 P_s 的收縮不等於物理映射 B 的收縮或切向雙曲性證明。
- 帶原 roof 的轉移算子之具體定義、有界性、譜隙、高頻抵消、混合速率、核性、跡公式以及 dynamical／Fredholm／quantum determinant 相等。有限型符號系統加 Hölder roof 不是這些結論的自動證書。
- 一個已實作並執行的有限精度演算法、舍入或區間誤差、軌道 census、owner ledger、`reverse_id` 序列化、fixture／population 或 Gate 1 全欄位。
- 投稿新穎性、文獻窮盡、外部獨立再現或正式狀態升級。

最近的可界定下一步是：在已證兩側 Hölder roof 上，明列所選一側化或雙側函數空間、實際轉移分支和權重，再逐項證明所需基本有界性；是否推進須由下一次授權決定。不能以本輪新結果提前簽發算子／譜／determinant 結論。

原有 `A0_FAIL / A2_NOT_ELIGIBLE / NO_ROUTE_PROMOTION`、Gate 6 `NOT_ACTIVATED`、Stage 5／6 停止條件和既有失敗紀錄保持不變；本輪不是 Route 評估，也不生成 PASS、nontransfer 證書、material passport 或投稿就緒狀態。

## 7. 實際讀取、來源邊界與保全

本輪完整讀取實際 `AGENTS.md`、`docs/workflow.md`，以 `rg --files` 定位當前 ARS 0.1.28 router、academic-paper workflow 及 argument-builder role，並完整讀取所選指引。只使用有界內部論證建構，未啟動完整寫作／正式審查 pipeline。

完整重讀[有限週期實現筆記][periodic]及[統一非擦邊筆記][nongrazing]。所有本輪新增命題均以上述初等向量微分、距離估計、幾何級數及緊致性直接證明；未援引未核讀的外部編碼定理，未新增外部文獻主張，也未作網頁搜尋、API 呼叫、私人材料上傳或舊失敗來源重試。沒有發表新穎性主張。

寫前以 `test ! -e` 確認新目標不存在。唯一寫入為 `apply_patch` 建立本檔；沒有運行科學程式、符號代數、軌道／字詞枚舉、數值迭代、實驗、artifact writer、稿件構建或正式驗證器。全批旧檔快照由主線預先統一保存，本分支不重建歷史回執。

主要只讀輸入 SHA-256：

- [有限週期實現筆記][periodic]：`ce70aee3b467675016f1509dee56342f9a878e32d592b6566827f9b4da1fa6fc`。
- [統一非擦邊筆記][nongrazing]：`b8bfead5e7371c9f2d42d43d8277e4f8f95db8fd4eb6e86a0a3d9b07561ad92a`。
- 現有 `notes/stage4_prime_revision_round5.tex`：`21092904a33dd9e044d01cb2b0b55ff49bc5d24f0840161a2b30ded9afe407e3`。

交接時另報新檔摘要、原輸入未變核對、局部链接與公式環境的只讀檢查；這些保全檢查與數學成立性分開，也不冒稱形式化或獨立認證。

[periodic]: /root/autodl-tmp/flow_systems/papers/30-three-disk-nonconstant-roof-determinant/notes/internal_periodic_itinerary_realization_and_primitive_counts_20260909.md
[nongrazing]: /root/autodl-tmp/flow_systems/papers/30-three-disk-nonconstant-roof-determinant/notes/internal_uniform_nongrazing_on_trapped_collisions_20260908.md
