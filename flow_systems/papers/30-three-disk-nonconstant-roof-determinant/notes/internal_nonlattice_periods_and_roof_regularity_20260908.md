# P30 內部論證：無共同時間格、有效兩週期非共振與局部 roof 正則性

記錄日期：2026-09-08 UTC。本筆記是使用者確認「下一輪」後，P29–33 五篇各一輪中的 P30 bounded argument-building 增量；不是實驗、正式審查、Route 評估或稿件修訂。

[上一輪幾何筆記][previous]已在固定的等邊三圓盤 `d=6a`、單位歐氏速率、逐碰撞返回映射上，直接構造本原物理週期

\[
T_2=8a,\qquad T_3=(18-3\sqrt3)a,\qquad a>0.
\tag{1}
\]

本輪從這兩個精確輸入證明：它們生成的加法群稠密、全部物理週期不可能包含在共同的 `h Z` 時間格中，且兩個週期的頻率相位具有有效但隨頻率衰減的非同時共振下界。另外，在明列的非擦邊固定首撞分支上，物理 roof 為實解析函數，並有以下顯式導數界。現稿採用的規範仍為 `a=1`；保留 `a` 只顯示量綱，不重新選擇時間或幾何尺度。

這些是局部／有限週期資料上的直接演繹，不是 mixing、谱隙、核性、Fredholm determinant 或量子對應的證明。

## 1. 無理週期比與無共同時間格

記

\[
\theta:=\frac{T_3}{T_2}=\frac{18-3\sqrt3}{8}.
\tag{2}
\]

若 `theta` 為有理數，則 `sqrt(3)=(18-8 theta)/3` 也為有理數，矛盾。這裡 `sqrt(3)` 的無理性可由互質整數的平方等式 `p^2=3q^2` 推出：`3|p` 後又得 `3|q`，違反互質。因此 (2) 是無理數。

若存在 `h>0`，使所有本原物理週期都屬於 `h Z`，則兩個已實現的正週期必可寫成 `T_2=u h`、`T_3=v h`，其中 `u,v` 是正整數；這會令 `theta=v/u` 有理。因此

\[
\boxed{\text{不存在 }h>0\text{ 使全部本原物理週期包含於 }h\mathbb Z.}
\tag{3}
\]

本筆記的「無共同時間格／nonlattice」只指 (3) 的精確含義，不把其他文獻對 roof、測度或譜的 arithmetic 定義自動視為已驗證。全部週期集合含有這兩條見證，已足夠推出這個否定命題；不需要先枚舉其餘週期。

### 1.1 加法群的稠密性：直接鴿籠證明

令

\[
G:=\mathbb ZT_2+\mathbb ZT_3
  =T_2(\mathbb Z+\theta\mathbb Z).
\tag{4}
\]

對任意正整數 `N`，把 `0,theta,...,N theta` 的小數部分放入 `[0,1)` 的 `N` 個等長半開區間。至少兩個在同一區間，故存在 `1<=n<=N` 及整數 `m`，使

\[
0<|n\theta-m|\le N^{-1}.
\tag{5}
\]

左端非零來自 `theta` 無理。於是 `G` 含有任意小的正元素 `delta=|nT_3-mT_2|`。給定任意 `x` 及 `epsilon>0`，選 `0<delta<2 epsilon`，再取最接近 `x/delta` 的整數 `r`，即有 `r delta in G` 且 `|x-r delta|<=delta/2<epsilon`。所以

\[
\boxed{\overline G=\mathbb R.}
\tag{6}
\]

這是允許正負整數係數的**加法群**稠密，不是實際週期長度集合稠密，也不是 `uT_2+vT_3`、`u,v>=0` 的半群在原點附近稠密。後一半群的每個非零元素至少為 `T_2`；不能把 (6) 改寫為有任意短的真實週期軌道。

## 2. 二次范數給出的有效整數差下界

對 `(m,n) in Z^2\{(0,0)}`，定義

\[
p=8m-18n,\qquad q=3n,
\qquad mT_2-nT_3=a(p+q\sqrt3).
\tag{7}
\]

其二次共軛乘積為

\[
\begin{aligned}
(p+q\sqrt3)(p-q\sqrt3)
 &=p^2-3q^2\\
 &=64m^2-288mn+297n^2.
\end{aligned}
\tag{8}
\]

(8) 是非零整數：若為零，`sqrt(3)` 的無理性迫使 `p=q=0`，再由 (7) 得 `m=n=0`。故它的絕對值至少為 1。又

\[
|p-q\sqrt3|
\le 8|m|+(18+3\sqrt3)|n|.
\]

將非零乘積的下界除以共軛的上界，得到

\[
\boxed{
|mT_2-nT_3|
\ge\frac{a}{8|m|+(18+3\sqrt3)|n|}
\ge\frac{a}{24(|m|+|n|)}>0.
}
\tag{9}
\]

最後一步用 `18+3 sqrt(3)<24`。對任意固定整數高度 `|m|+|n|<=H`、`H>=1`，(9) 特別给出 `a/(24H)` 的統一下界；它不給不限制整數高度時的正的統一下界，因而與 (6) 完全相容。

## 3. 有效頻率非同時共振

頻率記為 `omega in R`，量綱為時間的倒數，避免與幾何根公式中的係數混用。令

\[
d_j(\omega):=\operatorname{dist}(\omega T_j,2\pi\mathbb Z),
\quad j\in\{2,3\},\qquad
D(\omega):=\max(d_2(\omega),d_3(\omega)).
\tag{10}
\]

各 `d_j` 在 `[0,pi]` 內。選最近整數 `k,l`，寫成

\[
\omega T_2=2\pi k+\epsilon_2,\qquad
\omega T_3=2\pi l+\epsilon_3,
\qquad |\epsilon_j|=d_j(\omega)\le D(\omega).
\tag{11}
\]

在恰好等距的情形任取一個最近整數即可，以下推理不依賴此選擇。消去 `omega` 得

\[
T_3\epsilon_2-T_2\epsilon_3
=2\pi(lT_2-kT_3).
\tag{12}
\]

若 `(k,l)!=(0,0)`，由 (9) 及三角不等式，

\[
(T_2+T_3)D(\omega)
\ge\frac{2\pi a}{8|l|+(18+3\sqrt3)|k|}.
\tag{13}
\]

最近整數滿足

\[
|k|\le\frac{|\omega|T_2}{2\pi}+\frac12,
\qquad
|l|\le\frac{|\omega|T_3}{2\pi}+\frac12.
\]

所以 (13) 的分母至多為

\[
\begin{aligned}
8|l|+(18+3\sqrt3)|k|
&\le\frac{|\omega|[8T_3+(18+3\sqrt3)T_2]}{2\pi}
  +\frac{26+3\sqrt3}{2}\\
&=\frac{144a|\omega|}{\pi}+\frac{26+3\sqrt3}{2}.
\end{aligned}
\tag{14}
\]

結合 `T_2+T_3=(26-3 sqrt(3))a`，得到

\[
D(\omega)\ge
F(\omega):=
\frac{2\pi}{(26-3\sqrt3)
 [144a|\omega|/\pi+(26+3\sqrt3)/2]}
\quad\text{若 }(k,l)\ne(0,0).
\tag{15}
\]

若 `k=l=0`，則 (11) 直接給 `D(omega)=|omega|T_3`，因 `T_3>T_2`。因此不論最近整數屬於哪一情形，對全部非零頻率都有

\[
\boxed{D(\omega)\ge\min\{|\omega|T_3,F(\omega)\}>0
\quad(\omega\ne0).}
\tag{16}
\]

特別是，不存在非零頻率使這兩個週期的相位都恰好為 1。`omega=0` 當然同時共振，不能省略這個例外。

### 3.1 簡單的高頻常數

若 `|omega|>=pi/(4a)`，則 `|omega|T_2>=2pi`，最近整數 `k` 必非零，故可用 (15)。由

\[
26-3\sqrt3<26,\qquad
\frac{26+3\sqrt3}{2}<16
\le\frac{64a|\omega|}{\pi},
\]

得到較粗而明確的界

\[
\boxed{
D(\omega)\ge\frac{\pi^2}{2704a|\omega|}
\quad\left(|\omega|\ge\frac{\pi}{4a}\right).
}
\tag{17}
\]

因 `|e^{it}-1|=2 sin(dist(t,2pi Z)/2)`，且在 `[0,pi]` 上 `2 sin(d/2)>=2d/pi`，進一步有

\[
\boxed{
\max_{j=2,3}|e^{i\omega T_j}-1|
\ge\frac{\pi}{1352a|\omega|}
\quad\left(|\omega|\ge\frac{\pi}{4a}\right).
}
\tag{18}
\]

(17)–(18) 不主張常數最優；保留這組較寬鬆的常數，是為了使每一步都可由 (13)–(14) 直接核對。

### 3.2 不能把衰減下界變成固定相位間隙

由 (5)，可以取趨於無窮的正整數 `n_r`，使 `dist(n_r theta,Z)->0`：若所用的 `n_r` 始終有界，有限個非零的 `dist(n theta,Z)` 會有正的最小值，與 (5) 矛盾。選

\[
\omega_r=\frac{2\pi n_r}{T_2},
\]

則 `d_2(omega_r)=0`，而 `d_3(omega_r)=2pi dist(n_r theta,Z)->0`。因此有任意大的近似同時共振頻率；不存在對所有大頻率成立、與頻率無關的正相位間隙。這與 (17) 的 `1/|omega|` 下界不矛盾。

這一節只排除了兩個已指定週期在同一非零頻率的精確同時共振，並量化其距離；不證明任何轉移算子的高頻抵消、resolvent 界、Dolgopyat 估計或谱隙。

## 4. 明列的固定首撞分支及真实 roof

沿用[上一輪][previous] §1 的中心、圓盤與碰撞後截面，不更換返回次數或反射規則。固定不同標記 `i,j`，使用局部角座標

\[
q(\phi)=C_i+a(\cos\phi,\sin\phi),\qquad
v(\psi)=(\cos\psi,\sin\psi),\qquad
n_i(\phi)=(\cos\phi,\sin\phi).
\tag{19}
\]

這是物理碰撞點與絕對速度方向的座標，不是完整符號實現映射。置

\[
r=q-C_j,\quad b=r\cdot v,\quad
\Delta=b^2-|r|^2+a^2.
\tag{20}
\]

在角座標環面上定義開域

\[
U_{ij}:=\{(\phi,\psi):v\cdot n_i>0,\ b<0,\ \Delta>0\}.
\tag{21}
\]

每個點都向外離開 `K_i`，且其直線將非切觸地入射 `K_j`。下面直接證明 (21) 確實固定了下一次**首次**碰撞，不能只把「某個圓的根」當成物理 roof。

### 4.1 首次根與無競爭障礙

因 `|C_i-C_j|=6a`，有 `5a<=|r|<=7a`，故
`b^2-Delta=|r|^2-a^2>0`。結合 `b<0` 與 `Delta>0`，兩個交點時間都為正，較小者是

\[
\tau_{ij}(\phi,\psi)=-b-\sqrt\Delta>0.
\tag{22}
\]

令 `q'=q+tau_{ij}v`，則 `q' in boundary K_j`。對 `0<t<tau_{ij}`：

- 由出射條件，`|q+t v-C_i|^2=a^2+2at(v·n_i)+t^2>a^2`，不再碰出發圓盤。
- `|q+t v-C_j|^2-a^2=t^2+2bt+|r|^2-a^2` 在第一個根前為正，不提前碰目標圓盤。
- 線段在 `conv(K_i union K_j)` 中；上一輪已直接算得第三圓盤到該凸包距離為 `(3 sqrt(3)-2)a>0`，故無第三障礙競爭。

因此 (22) 就是這個開域上的實際物理首次飛行時間，而不是幾個分支根的非光滑最小值。端點間距還給出

\[
4a\le\tau_{ij}\le8a.
\tag{23}
\]

這裡只要求下一次碰撞存在；`U_{ij}` 中的點未必在後續所有正負時間都被困住。在真實雙向有界集上的 roof 是這個一段飛行函數的限制，不能由此斷言完整被困集的符號性質。

### 4.2 入射餘弦及非擦邊子域

令 `w=q'-C_j`，則 `|w|=a`，且由 (20)–(22)，

\[
w\cdot v=b+\tau_{ij}=-\sqrt\Delta,
\qquad
\chi:=-v\cdot\frac wa=\frac{\sqrt\Delta}{a}\in(0,1].
\tag{24}
\]

`chi` 是目標碰撞入射餘弦的絕對值。選 `0<kappa<=1`；以下的統一估計在 `U_{ij}` 中滿足 `chi>=kappa` 的部分成立。若同時需要離出射切觸有固定距離，可以再限制 `v·n_i>=kappa_0>0`。帶 `>=` 的估計集合不宣稱為開集；光滑函數本身定義在 (21) 的開域上。

上一輪二碰撞見證的出射／入射餘弦均為 1，三碰撞見證均為 `sqrt(3)/2`。故例如 `kappa=kappa_0=1/2` 時，每個見證碰撞狀態均有保持嚴格不等式、固定下一標記的開鄰域。這只證明这些具體局部域非空，不證明全部被困集有同一角度下界。

## 5. C-infinity 與明確導數界

### 5.1 實解析性與一階界

(19)–(20) 的函數實解析，正平方根在 `Delta>0` 實解析；所以 (22) 在 `U_{ij}` 上實解析，特別為 `C-infinity`。

也可對恆等式

\[
|q+\tau_{ij}v-C_j|^2=a^2
\]

微分。因 (24) 的分母不為零，得到

\[
\partial_\phi\tau_{ij}
=-\frac{w\cdot\partial_\phi q}{w\cdot v},
\qquad
\partial_\psi\tau_{ij}
=-\frac{\tau_{ij}w\cdot\partial_\psi v}{w\cdot v}.
\tag{25}
\]

使用 `|partial_phi q|=a`、`|partial_psi v|=1`、`|w|=a`、`|w·v|>=a kappa` 及 (23)，得到

\[
\boxed{
|\partial_\phi\tau_{ij}|\le\frac a\kappa,
\qquad
|\partial_\psi\tau_{ij}|\le\frac{8a}\kappa.
}
\tag{26}
\]

這些導數對無量綱角度取值，故量綱與 `tau` 同為時間／長度。

### 5.2 每階均可算的高階常數

對二維多重指標 `alpha`、`|alpha|=k>=1`，給出一組刻意不追求最優的有效常數。記 `S(k,p)` 為把 `k` 個標記元素分成 `p` 個非空集合的方式數，並定義

\[
M_k:=49\,2^k+12,\qquad
c_p:=\left|\prod_{r=0}^{p-1}\left(\frac12-r\right)\right|,
\qquad
C_k:=7+\sum_{p=1}^{k}S(k,p)c_pM_k^p.
\tag{27}
\]

有限組合數可由 `S(1,1)=1`、`S(k,0)=0`、`S(k,p)=0` 當 `p>k`，及 `S(k+1,p)=pS(k,p)+S(k,p-1)` 計算。本輪不執行任何計算程式；(27) 已逐階指定了常數。

所需的基本界為：對任意階角導數（包括零階），`|partial^alpha b|<=7a`；若至少對 `phi` 微分一次，甚至有 `<=a`。另外

\[
|r|^2=37a^2+2a(C_i-C_j)\cdot(\cos\phi,\sin\phi),
\]

故正階導數的絕對值至多 `12a^2`（含 `psi` 微分時為零）。乘積微分的係數總和為 `2^k`，於是

\[
|\partial^\alpha\Delta|\le(49\,2^k+12)a^2=M_ka^2
\quad(k\ge1).
\tag{28}
\]

為完整核對平方根的複合導數，把 `k` 次座標微分按出現順序標記為 `1,...,k`。反覆使用普通鏈式與乘積法則，對 `f(u)=sqrt(u)` 有

\[
\partial^\alpha f(\Delta)
=\sum_{\mathcal P}
 f^{(|\mathcal P|)}(\Delta)
 \prod_{A\in\mathcal P}\partial_A\Delta.
\tag{29}
\]

和遍歷這 `k` 個標記的全部集合分割；`partial_A` 表示區塊 `A` 內所標記的座標微分。此式可逐次歸納：新增一次微分，若作用在 `f`，便新增一個單元素區塊；若作用在某個 `partial_A Delta`，便把新標記加入該區塊。每個新分割恰好生成一次，故重複座標也沒有漏掉組合係數。

在 `Delta>=a^2 kappa^2` 上，對 `p>=1` 有

\[
|f^{(p)}(\Delta)|
=c_p\Delta^{1/2-p}
\le c_pa^{1-2p}\kappa^{1-2p}.
\]

每個有 `p` 區塊的項，使用 (28) 及 `M_{|A|}<=M_k`，至多為 `c_p M_k^p a kappa^{1-2p}`。因 `p<=k`、`kappa<=1`，這又不超過 `c_p M_k^p a kappa^{1-2k}`。加入 (22) 中 `-b` 的導數後，得到

\[
\boxed{
|\partial^\alpha\tau_{ij}|
\le C_k a\kappa^{1-2k}
\qquad(|\alpha|=k\ge1).
}
\tag{30}
\]

(26) 對一階比 (30) 更精細；兩者無衝突。(30) 的 `C_k` 只依賴微分階數與已固定的 `d/a=6`，不依賴所選 `i,j`、角度、`a` 或 `kappa`。當 `kappa` 趨於零時估計退化，沒有以這個論證覆蓋擦邊奇點。

## 6. 本輪解決了甚麼，沒有解決甚麼

本輪有三條分立的 claim–evidence–reasoning 鏈：精確週期與無理性給出 (3)、(6)；非零整數范數經消去頻率給出 (9)、(16)–(18)；首撞幾何及直接微分給出 (22)、(26)、(30)。每條鏈的證據都是明列演繹，不以同一代理的重算或同伴同意當成獨立科學證據。

仍未完成且不可隱含的事項包括：

- 完整逐碰撞符號實現、全域編碼唯一性、所有逆分支、符號度量下 roof 的 Hölder 界，以及整個被困集的統一非擦邊控制。
- 從週期無共同時間格到某個拓撲或測度 mixing 定理所需的精確空間、測度、編碼與其他假設，以及任何定量混合結論。
- 從兩個相位界到整族週期／轉移算子上的高頻估計、谱隙、函數空間、核性、跡公式或 determinant 等式／不等式。
- 有效 owner ledger、數值誤差／區間證書、正式 Gate-1 欄位全通過，或在結果接觸前已凍結的 Gate-6 實驗契約。
- 二碰撞自反向軌道的 `reverse_id` 序列化選擇。該邊界仍按上一輪 §6 保留；本輪不用方向倍數，也不改循環等價或 owner 計數。

現有 `A0_FAIL / A2_NOT_ELIGIBLE / NO_ROUTE_PROMOTION`、Gate 6 `NOT_ACTIVATED` 及 Stage 5／6 停止條件均不變。本筆記不生成正式 `NONTRANSFER_CERTIFIED`、PASS、material passport 或投稿就緒狀態，也不把局部 roof 正則性改寫為整個 Gate 1 的完成回執。

## 7. 來源、動作與保全檢查

本輪依照 ARS bounded argument-building，把輸入、證明、反例式邊界與未解義務分開；未啟動完整 academic-paper pipeline。已讀取當輪實際 `AGENTS.md`、`docs/workflow.md`、ARS router、academic-paper workflow、argument-builder role，以及[上一輪幾何筆記][previous]。全部新數學推導寫在本檔；沒有新增外部文獻主張或引用，也沒有重驗上一輪來源的其他定理。本輪不需要網路搜尋，實際未呼叫網頁或外部 API。

寫入前以 `test ! -e` 確認本目標不存在；唯一授權寫入是以 `apply_patch` 新建本檔。其餘操作為 `rg`、`sed`、`sha256sum`、`find`、`sort` 等本地只讀定位／內容檢查，沒有執行專案程式、artifact writer、科學或符號代數程式、軌道枚舉、數值積分或稿件構建。

寫前原有 P30 普通檔案保全摘要：對排除本新檔精確路徑的 `find -type f -print0` 結果，以 `sort -z | xargs -0 sha256sum | sha256sum` 計算，得到 `861074cd81b480dd44c37a52fc5127e43a72a451f329860c6528a757682c9076`。這個摘要的範圍是普通檔案的排序路徑與內容，不包含符號連結自身或檔案 metadata，不等同於獨立數學認證；交接前以相同只讀命令核對是否保持不變。

主要輸入的 SHA-256：

- 上一輪幾何筆記：`ec3e3a868a300a0f3a684e00c5db9f29dbb6e3e036f16a1773bfe0e899255ef2`。
- 現有 `notes/stage4_prime_revision_round5.tex`：`21092904a33dd9e044d01cb2b0b55ff49bc5d24f0840161a2b30ded9afe407e3`。
- 現有 `notes/stage4_prime_references_round3.bib`：`60a8a72aa9266b0a82fd32d25b72b2dc890019274a0071e6433937936d34437a`。

本輪 `git status --short -- papers/30-three-disk-nonconstant-roof-determinant` 再次回報此目錄不是 Git repository；未更改 Git 設定或嘗試修復。另一次只讀 `sed` 因將 ARS workflow 少寫一層 `academic-paper/` 而回報檔案不存在；以 `rg --files` 定位正確路徑後完整讀取。兩次失敗均未寫入檔案、未觸發正式驗證器，也不構成科學結果。

沒有修改現稿、舊筆記、引用檔、實驗／results、正式回執或歷史失敗記錄；檢查的實際結果與本檔摘要另向主線交接。本輪無文獻窮盡、發表新穎性或獨立科學驗證主張。

[previous]: /root/autodl-tmp/flow_systems/papers/30-three-disk-nonconstant-roof-determinant/notes/internal_geometric_period_witnesses_20260908.md
