# P30 內部論證：全部雙向被困碰撞的統一非擦邊界與空間 Lipschitz roof

記錄日期：2026-09-08 UTC。使用者第三次確認「下一輪」後，本筆記是 P29–33 五篇整輪中的 P30 有界內部數學增量。只新建本檔，不改現稿、前兩輪筆記、程式、owner 規則、正式狀態或實驗紀錄。

在[第一輪][geometry]固定的等邊三圓盤 `d=6a`、單位歐氏速率和碰撞後截面上，本輪證明：全部真實雙向被困碰撞的入射／出射法向餘弦均至少為

\[
\boxed{\kappa_*=
\cos\left(\frac\pi6+\arcsin\frac13\right)
=\frac{2\sqrt6-1}{6}>\frac12.}
\tag{1}
\]

因此[第二輪][regularity]的局部 roof 各階導數界，可以在全部實際被困碰撞狀態上使用同一個非擦邊常數。另外，對明列的物理相空間距離，本輪直接證明 roof 的全局 Lipschitz 性。這不是符號編碼定理、symbolic Hölder、mixing 或谱結論。

## 1. 物件及「全部被困碰撞」的量詞

保持

\[
C_1=(0,0),\quad C_2=(6a,0),\quad C_3=(3a,3\sqrt3a),
\qquad K_i=\overline B(C_i,a),\qquad a>0.
\tag{2}
\]

自由飛行在三個圓盤外部，速度長度為 1；每次物理碰撞返回一次，並按外法向 `n=(q-C_i)/a` 作鏡面反射。现稿的規範仍是 `a=1`，保留 `a` 只顯示量綱。

以 `T_coll` 記全部真實雙向被困軌道的碰撞後狀態 `(q,v)`。此處「雙向被困」指完整物理軌道在正、負時間皆保持有界；不是先假定某個形式符號序列可實現。為避免用「非擦邊」作為循環前提，下面的幾何排除甚至允許先把切觸接觸作為候選碰撞：入射 `v^-·n<=0`，出射 `v^+·n>=0`，且反射公式在等號時令速度不變。最後的結論排除雙向被困軌道上的這種等號情形，並回到原有非切觸截面。

若雙向被困軌道在某一時間方向只有有限次接觸，最後一次之後就是無限長的單位速率直線，必離開每個有界集合，矛盾。因此每個碰撞都有前一個與後一個碰撞。

### 1.1 相鄰標記必不同，且沒有零時間累積

從 `q in boundary K_i` 以 `v·n_i>=0` 出發時，对 `t>0`，

\[
|q+tv-C_i|^2=a^2+2at(v\cdot n_i)+t^2>a^2.
\tag{3}
\]

所以同一直線在下一次碰撞前不可能再次接觸出發圓盤，包括切向出射。每兩次相鄰碰撞的標記不同。兩個不同圓盤的任意邊界點間距位於 `[4a,8a]`，故每段實際首次飛行時間滿足

\[
4a\le\tau\le8a.
\tag{4}
\]

下界亦排除有限物理時間內無限次碰撞的累積。因此可對每個真實被困碰撞使用前／當下／後三個點，不需額外的符號存在性假设。`T_coll` 非空已有第一輪二碰撞與三碰撞見證支持，但本輪估計不侷限於它們。

## 2. 任意跨盤線段的方向錐

**方向引理。** 若 `q in boundary K_i`、`p in boundary K_j`、`i!=j`，則從 `q` 指向 `p` 的單位方向，與中心方向

\[
e_{ij}:=\frac{C_j-C_i}{6a}
\]

的較小夾角至多為

\[
\delta:=\arcsin\frac13<\frac\pi6.
\tag{5}
\]

證明。寫

\[
p-q=c+e,\qquad c=C_j-C_i,\qquad
e=(p-C_j)-(q-C_i),
\quad |c|=6a,\quad |e|\le2a.
\tag{6}
\]

置 `s=|c+e|>0`、`z=(c+e)/s`。因

\[
c\cdot(c+e)\ge |c|(|c|-|e|)>0,
\]

所以 `z` 與 `c` 的夾角 `theta` 在 `[0,pi/2)`。向量 `c` 到直線 `R z` 的垂直距離為 `|c| sin(theta)`；該直線上的點 `s z=c+e` 距離 `c` 至多 `2a`，故

\[
6a\sin\theta\le|c-sz|=|e|\le2a.
\]

在這個銳角範圍內即得 `theta<=arcsin(1/3)`。最後因 `1/3<sin(pi/6)=1/2`，得到 (5) 的嚴格上界。證畢。

這裡用的是中心向量到線的垂距，而不是把偏差除以最短飛行長；後一種較粗估计不是 (5) 的推導。引理甚至適用於任意跨盤邊界點對，對真實自由飛行自然成立。

## 3. 反射法則的角度方向與統一非擦邊

固定任一被困碰撞：當下點 `q` 在圓盤 `i`，前一點 `p_-` 在圓盤 `j`，後一點 `p_+` 在圓盤 `k`。由 (3)，`j!=i`、`k!=i`，但允許 `j=k`。

在碰撞點向外看，定義兩條射線方向

\[
u:=\frac{p_--q}{|p_--q|}=-v^-,\qquad
w:=\frac{p_+-q}{|p_+-q|}=v^+.
\tag{7}
\]

第一個是**反向入射**，不是原來的入射速度。令

\[
\chi:=-v^-\cdot n\ge0.
\]

鏡面反射給

\[
v^+=v^--2(v^-\cdot n)n,
\qquad
u+w=2\chi n,
\qquad u\cdot n=w\cdot n=\chi.
\tag{8}
\]

若 `alpha=angle(u,w) in [0,pi]`，則兩個單位向量的和長度為 `2 cos(alpha/2)`。由 (8)，

\[
\chi=\cos(\alpha/2).
\tag{9}
\]

當 `chi>0` 時，(8) 亦明確说明外法向是這兩條射線較小夾角的內角平分線；若 `chi=0`，兩條射線相反，`alpha=pi`。下面的角度上界直接排除後者，沒有預先假設角平分線非退化。

### 3.1 前後都在同一個其他圓盤：`j=k`

由方向引理，`u,w` 都在以 `e_ij` 為中心、半角 `delta` 的方向錐內，故

\[
\alpha\le2\delta,
\qquad
\chi\ge\cos\delta=\frac{2\sqrt2}{3}.
\tag{10}
\]

不需要假設前後碰撞點相同，也不需把軌道限制為兩點往返；(10) 對此標記情形的任意實際三點段都成立。

### 3.2 前後在不同的其他圓盤：`j!=k`

此時三個標記全不同。由等邊幾何，兩個中心方向 `e_ij,e_ik` 的較小夾角是 `pi/3`。單位圓上角距的三角不等式及方向引理給

\[
\alpha
\le\angle(u,e_{ij})+\angle(e_{ij},e_{ik})
       +\angle(e_{ik},w)
\le\frac\pi3+2\delta<\pi.
\tag{11}
\]

因此

\[
\chi\ge\cos\left(\frac\pi6+\delta\right)=\kappa_*.
\tag{12}
\]

由 `sin(delta)=1/3`、`cos(delta)=2sqrt(2)/3`，展開即得 (1) 的根式；由 `delta<pi/6` 可直接得 `kappa_*>cos(pi/3)=1/2`。

### 3.3 對全部實際被困碰撞的結論

(10)、(12) 覆蓋全部可能前後標記，而且前者的常數大於 `kappa_*`。因此在每一條雙向被困軌道的每一碰撞，

\[
\boxed{-v^-\cdot n=v^+\cdot n\ge\kappa_*>0.}
\tag{13}
\]

這不僅是「沒有恰好切觸」：同一個正下界還排除了被困碰撞序列的入射餘弦趨零。證明實際只需要該碰撞有一個真實前驅與一個真實後繼；不要求週期性或任何固定有限詞長。

## 4. roof 各階界在全部被困狀態上的統一化

令 `T_ij` 為當下在盤 `i`、下一次在盤 `j` 的被困碰撞後狀態集合。六個 `i!=j` 的集合把 `T_coll` 分開。沿用第二輪的角座標及根公式，

\[
q=C_i+a(\cos\phi,\sin\phi),\quad
v=(\cos\psi,\sin\psi),\quad
r=q-C_j,\quad b=r\cdot v,
\quad\Delta=b^2-|r|^2+a^2,
\]

\[
\tau_{ij}=-b-\sqrt\Delta.
\tag{14}
\]

第二輪 §4 已在開域 `U_ij={v·n_i>0,b<0,Delta>0}` 上逐項排除更早撞到出發圓盤、目標圓盤及第三圓盤，故 (14) 在該域是真實首次 roof。這裡沒有以一個候選根取代尚未核對的最小根。

對 `x in T_ij`，(13) 分別用於當下及下一碰撞，得到

\[
v\cdot n_i\ge\kappa_*,\qquad
\frac{\sqrt\Delta}{a}\ge\kappa_*,
\qquad\Delta\ge a^2\kappa_*^2.
\tag{15}
\]

所以所有 `T_ij` 均在相應真實解析首撞域 `U_ij` 內，且第二輪 §5 的常數可統一取 `kappa=kappa_*`。特別是

\[
\boxed{
|\partial_\phi\tau_{ij}(x)|\le\frac a{\kappa_*},\qquad
|\partial_\psi\tau_{ij}(x)|\le\frac{8a}{\kappa_*}
\quad(x\in T_{ij}).}
\tag{16}
\]

為使高階界可直接追蹤，沿用明確常數

\[
M_s=49\,2^s+12,\qquad
c_p=\left|\prod_{r=0}^{p-1}\left(\frac12-r\right)\right|,
\qquad
C_s=7+\sum_{p=1}^s S(s,p)c_pM_s^p,
\tag{17}
\]

其中 `S(s,p)` 為 `s` 個標記元素分成 `p` 個非空區塊的方式數。第二輪的乘積微分及集合分割鏈式法則已逐項證明，因而對 `|alpha|=s>=1`，

\[
\boxed{|\partial^\alpha\tau_{ij}(x)|
\le C_s a\kappa_*^{1-2s}
\quad(x\in T_{ij},\ i\ne j).}
\tag{18}
\]

此處導數是環境角座標開域上解析分支的導數，在實際被困狀態處取值。不是宣稱 `T_coll` 本身是光滑流形，也不是宣稱一個 roof 解析公式能跨過所有逃逸／擦邊分支邊界。統一的 jet 界已成立，但若要沿兩點間路徑積分，仍須證明路徑留在受控域內；不能僅由端點位於被困集就假定這一點。

## 5. 明確物理距離下的全局 Lipschitz 性

本節不依賴分支域凸性，也不對被困集內部是否存在連接路徑作假設。對碰撞後狀態定義

\[
d_a((q,v),(\widetilde q,\widetilde v))
 :=|q-\widetilde q|+a|v-\widetilde v|.
\tag{19}
\]

速度用普通歐氏弦距，`a` 使兩項都有長度量綱；這是既有物理狀態的距離選擇，不是時間重參數化。

### 5.1 同當下標記且同下一標記：直接根差商

設 `x,xtilde in T_ij`，並用波浪號表示第二點的根公式資料。由 `|r|,|rtilde|,|b|,|btilde|<=7a`，有

\[
|b-\widetilde b|
\le |q-\widetilde q|+7a|v-\widetilde v|,
\tag{20}
\]

\[
\begin{aligned}
|\Delta-\widetilde\Delta|
&\le14a|b-\widetilde b|+14a|q-\widetilde q|\\
&\le28a|q-\widetilde q|+98a^2|v-\widetilde v|.
\end{aligned}
\tag{21}
\]

兩端點都滿足 (15)，所以恆等式

\[
|\sqrt\Delta-\sqrt{\widetilde\Delta}|
=\frac{|\Delta-\widetilde\Delta|}
       {\sqrt\Delta+\sqrt{\widetilde\Delta}}
\le\frac{|\Delta-\widetilde\Delta|}{2a\kappa_*}
\tag{22}
\]

給出

\[
\begin{aligned}
|\tau(x)-\tau(\widetilde x)|
&\le\left(1+\frac{14}{\kappa_*}\right)|q-\widetilde q|
   +\left(7+\frac{49}{\kappa_*}\right)a|v-\widetilde v|\\
&\le\left(7+\frac{49}{\kappa_*}\right)d_a(x,\widetilde x).
\end{aligned}
\tag{23}
\]

這個比較只用兩個端點的合法首撞根及非擦邊界，不把受控端點間的線段默認為合法首撞分支。

### 5.2 同當下標記、不同下一標記：速度錐有正間隔

設 `x in T_ij`、`xtilde in T_ik`、`j!=k`。由方向引理，`v` 與 `vtilde` 分別在以 `e_ij`、`e_ik` 為軸的半角 `delta` 錐中。故

\[
\angle(v,\widetilde v)\ge\gamma_*:=\frac\pi3-2\delta>0,
\]

\[
|v-\widetilde v|\ge
\epsilon_*:=2\sin(\gamma_*/2)
=\frac{2\sqrt2-\sqrt3}{3}>\frac13.
\tag{24}
\]

最後的不等式可由 `2sqrt(2)>1+sqrt(3)` 核對；平方後等價於 `2>sqrt(3)`。結合 (4)，

\[
|\tau(x)-\tau(\widetilde x)|\le4a
\le\frac4{\epsilon_*}d_a(x,\widetilde x).
\tag{25}
\]

所以不同下一盤的切換在實際碰撞後狀態中有可控制的速度間隔，不能用一般分段函數可能跳躍的疑慮代替這裡的具體幾何檢查。

### 5.3 當下標記不同

若 `q`、`qtilde` 位於不同圓盤，則 `|q-qtilde|>=4a`。再次由 (4)，

\[
|\tau(x)-\tau(\widetilde x)|\le4a\le d_a(x,\widetilde x).
\tag{26}
\]

### 5.4 全局結論及常數

上述三種情形覆蓋任意 `x,xtilde in T_coll`。因此令

\[
L_*:=\max\left\{1,\ 7+\frac{49}{\kappa_*},\
                         \frac4{\epsilon_*}\right\},
\]

就有

\[
\boxed{|\tau(x)-\tau(\widetilde x)|
\le L_*d_a(x,\widetilde x)
\le105\,d_a(x,\widetilde x)
\quad(x,\widetilde x\in T_{\mathrm{coll}}).}
\tag{27}
\]

粗常數 105 來自 `kappa_*>1/2`、`epsilon_*>1/3`，不追求最優。它與 `a` 無關；時長和距離仍按同一個原有歐氏時鐘縮放。這是全體實際被困碰撞後狀態在 (19) 的**空間相距**下的 Lipschitz 結論，不是只在一條週期軌道上的估計。

## 6. 與符號／谱義務的邊界

本輪確實填補了第二輪尚未證明的「全部被困碰撞統一非擦邊」缺口，並把已證首撞 roof 的各階常數統一化。第二輪原文及其當時的未完成敘述保持不動；本檔是新的、可逐步核對的後續證明。

仍然不能省略以下義務：

- 從所有容許雙向標記序列到真實被困軌道的實現、唯一性及完整雙向編碼；本輪只對已存在的軌道作全稱證明。
- 兩個長中心碼塊相同的真實軌道，其碰撞狀態在 (19) 距離下多快接近。只有把這類編碼連續性／定量收縮與 (27) 相接，才有指定符號度量下 roof 正則性的結論。
- 各逆分支、Markov 結構、雙曲性、所需函數空間和算子有界性。統一的局部 root 導數不是完整符號轉移算子已被構造。
- mixing、定量混合、谱隙、高頻抵消、核性、跡公式、任何 dynamical／Fredholm／quantum determinant 結論。本輪沒有驗證適用這些結論的完整假設。
- 實際 owner ledger、二碰撞自反向 `reverse_id` 處理、誤差／區間證書、Gate 1 全欄位與 Gate 6 的正式啟動契約。

尤其 (27) 並不給 `tau` 在全部一次可返回但可能隨後逃逸的狀態上的同一全局常數，因為那個更大集合未必在下一次碰撞有後繼，(13) 的兩邊幾何前提可能失效。也不把碰撞後截面的距離直接當成跨碰撞流相空間或任意其他截面的距離。

原有 `A0_FAIL / A2_NOT_ELIGIBLE / NO_ROUTE_PROMOTION`、Gate 6 `NOT_ACTIVATED`、Stage 5／6 停止條件全部保持不變。沒有生成 PASS、正式 nontransfer 證書、material passport 或投稿就緒狀態。本輪不是 Route 評估。

## 7. 實際動作與核對範圍

已完整讀取當輪 `AGENTS.md`、`docs/workflow.md`、ARS router、academic-paper workflow 和 argument-builder role，只使用有界論證建構，不啟動完整寫作／審查流水線。ARS 的 claim–evidence–reasoning 要求在本檔具體落為三條分立證明：方向錐加反射、首撞根上的統一導數、端點根差與分支間隔上的全局 Lipschitz。反例風險及尚缺的編碼橋接均另外列明。

重新讀取前兩輪的幾何與首撞／導數段落並核對輸入雜湊；本輪全部新数学都在上文直接證明，未新增外部來源主張，因此沒有作普通網頁搜尋或外部 API 呼叫。未運行既有專案程式、科學／符號計算、軌道枚舉、數值積分、artifact writer、論文構建或正式驗證器。也未重跑已知不適用的 Git 檢查。

寫前以 `test ! -e` 確認本目標不存在，唯一寫入操作為 `apply_patch` 新建本檔。主要只讀輸入 SHA-256 為：

- [第一輪幾何筆記][geometry]：`ec3e3a868a300a0f3a684e00c5db9f29dbb6e3e036f16a1773bfe0e899255ef2`。
- [第二輪非格點／局部 roof 筆記][regularity]：`916b5f622ac0e3b4fc250bd0f4568cbe21e2412a0288a1baa4051e96a7fbdebd`。
- 現有 `notes/stage4_prime_revision_round5.tex`：`21092904a33dd9e044d01cb2b0b55ff49bc5d24f0840161a2b30ded9afe407e3`。

主線已在本次五篇整輪寫入前保存全批舊檔案清單／摘要，本分支不另建或重寫一套歷史回執。交接時回報上述輸入的只讀重核對、本檔實際摘要、文本／公式檢查與數學交叉檢查結果；機械保全與同伴復核均不等同獨立科學認證。沒有文獻窮盡或發表新穎性主張。

[geometry]: /root/autodl-tmp/flow_systems/papers/30-three-disk-nonconstant-roof-determinant/notes/internal_geometric_period_witnesses_20260908.md
[regularity]: /root/autodl-tmp/flow_systems/papers/30-three-disk-nonconstant-roof-determinant/notes/internal_nonlattice_periods_and_roof_regularity_20260908.md
