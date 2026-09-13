# P30 goal01：同一物理 primitive 軌道的經典 zeta 延拓接口

日期：2026-09-09 UTC。範圍：主線明確授權將已完成的有限理論／來源核對保存為本獨占新檔；只作紙面論證，不修改舊筆記、程式、資料、現稿、鎖定輸入或正式狀態。

## 0. 結論、來源層級與停止線

**對固定真實等邊三盤，當前正一側 roof 的週期 zeta 與物理 primitive-orbit zeta 在明確右半平面逐項相同；因此可引用 Stoyanov 的既有 Corollary 6.4，取得一個越過物理流熵的半平面延拓及簡單極點結論。**

這是既有經典 zeta 定理的本案應用，不是新 zeta 定理、完整文獻新穎性判定、外部獨立再現或正式 Stage 結論。本文不把幾何 Markov 空間上的高頻估計搬成指定完整符號 `C^beta` 空間的算子估計，也不建立 Fredholm／quantum determinant。

論證分工如下：來源定理放在 §2；§1、§3–4 使用已落盤物理編碼及共邊界逐項識別；§5 明列同一來源的計數結論如何與物理 roof 界共同給出熵的正性及粗界；§6 才作解析延拓的本案轉接。ARS 有限 argument-builder 指引在此用於分開來源、推導、反對意見與不能升級的事項，沒有啟動完整研究／寫作／審查流水線。

## 1. 固定物件與真正使用的上游輸入

保持半徑 `a>0`、圓心

\[
C_1=(0,0),\qquad C_2=(6a,0),\qquad
C_3=(3a,3\sqrt3a),\qquad K_j=\overline B(C_j,a),
\tag{1}
\]

單位歐氏速率、原盤標記及逐碰撞截面。現稿 `a=1` 是此式的特例；保留 a 只顯示物理時間量綱，沒有重新縮放時鐘。

令 `Lambda` 是全部雙向有界物理軌道的相狀態集合，反射點使用通常的入射／鏡面出射識別；`phi_t` 是該集合上的連續流。令 `T_coll` 是其碰撞後截面。固定

\[
\Sigma=\{x\in\{1,2,3\}^{\mathbb Z}:x_i\ne x_{i+1}\},
\qquad
\Sigma^+=\{x\in\{1,2,3\}^{\mathbb N_0}:x_i\ne x_{i+1}\}.
\tag{2}
\]

雙側／一側左移分別記 `sigma`、`sigma+`，`pi` 保留非負座標。已落盤輸入的確切責任是：

- [雙向編碼筆記][coding] §1 式 (4)、§3、§5：no-eclipse 間隙為 `(3sqrt(3)-2)a>0`；每個雙側容許盤字恰有一個真實雙向被困實現；`H_phys:Sigma→T_coll` 是同胚並與原碰撞映射共軛；全部碰撞一致 nongrazing，所有飛行都是首次飛行。
- 同筆記式 (21)、(28)–(29)：原物理 roof 是正 Hölder 函數，並有
  \[
  \tau(x)=|Q_1(x)-Q_0(x)|\in[4a,8a].
  \tag{3}
  \]
- [正一側 roof 筆記][roof] §3 式 (11)、(14)–(15)：固定 `g in C^beta(Sigma+)`、`2a<=g<=10a`，以及雙側連續函數 U，使
  \[
  g\circ\pi=\tau-U+U\circ\sigma.
  \tag{4}
  \]
  這個 g 不隨複參數 s 改變；它一般不逐點等於單次物理飛行時間。

正一側化沒有省略過去來改造物理軌道；它由已證共邊界 (4) 保留週期資料。本文不把上游內部論證另標成形式化證書。

## 2. 已核讀的經典來源：精確陳述範圍

使用 Luchezar Stoyanov, *Non-integrability of open billiard flows and Dolgopyat-type estimates*, *Ergodic Theory and Dynamical Systems* **32** (2012), 295–313，DOI [10.1017/S0143385710000933][doi]。實際定理內容核讀版本為 [arXiv:0911.5000v4][stoyanov]（2010-10-28），定位採章節／定理而不是本地 PDF 頁碼證書。出版身份沿用[既有來源接口][source-interface] §2；定理段落在本次及前一只讀輪由遠端 PDF 文字層核對。

以下緊湊列出本頁使用的來源內容；其餘步驟是本案推導。

- §1 的開放台球類別：至少三個互不相交的緊緻嚴格凸障礙物、`C^2` 邊界、no-eclipse 條件 (H)。Theorem 6.3 假設 pinching (P)；§1 明列平面情形自動滿足。
- §2.1 的 `Lambda` 是雙向有界軌道集；反射識別在同一碰撞點把鏡面入／出速度接合。
- Corollary 6.4 前的定義：
  \[
  \zeta_{\rm phys}(s)=
  \prod_{\gamma\ \mathrm{primitive}}
  (1-e^{-s\ell(\gamma)})^{-1},\qquad
  h_T=h_{\rm top}(\phi_t|_\Lambda).
  \tag{5}
  \]
  `gamma` 是相流的 primitive closed orbit，`ell(gamma)` 是最小週期。
- Corollary 6.4：在 Theorem 6.3 的假設下，存在 `c0<hT`，使 (5) 在 `Re s>c0` 延拓，除 `s=hT` 的簡單極點外解析且不消失；並存在另一常數 `c in (0,hT)`，使
  \[
  \Pi(T):=\#\{\gamma:\ell(\gamma)\le T\}
  =\operatorname{li}(e^{h_TT})+O(e^{cT}),
  \qquad
  \operatorname{li}(x)\sim\frac{x}{\log x}.
  \tag{6}
  \]

來源只寫 `c0<hT`，**沒有寫 `c0>0`**。(6) 的 c 是計數誤差指數，不能與 c0 混同。[來源定位：§1、§2.1、Theorem 6.3、Corollary 6.4][stoyanov]

本案 (1) 有三個不相交光滑嚴格凸障礙物，(3) 前所列幾何間隙驗證 no-eclipse，且維度是 2；因此符合上述類別及 (P)。不另加高維充分分離不等式，也不以同步更新的收縮常數冒充物理切向 pinching 證明。本頁使用的是來源明列的平面適用性。

## 3. primitive 軌道、方向、邊界及 suspension 的逐項識別

### 3.1 一側週期點與雙側週期延拓

若 `sigma+^n y=y`，則令 `x_j=y_r`，其中 `r in {0,...,n-1}` 是 j 模 n 的代表，得到唯一滿足 `sigma^n x=x`、`pi x=y` 的雙側週期延拓。不同可能的週期長不改變此延拓，因其所有負座標已由週期性和 y 決定。

最小符號週期保持不變：双側的更短週期會限制為一側的更短週期；一側的更短週期也會延拓為雙側的同一更短週期。因此 primitive 一側移位循環與 primitive 雙側移位循環自然雙射。

對任意 `sigma^n x=x`，由 (4) 望遠鏡相消，

\[
S_ng(\pi x)=S_n\tau(x)+U(\sigma^nx)-U(x)=S_n\tau(x).
\tag{7}
\]

式 (7) 對每個 n 成立，不要求 n 是正性平均長度的倍數；也不把總物理週期除以平均長度。

### 3.2 primitive 符號循環恰對應 primitive 物理流軌道

取最小符號週期為 n 的 x。由 `H_phys` 的碰撞共軛，對應狀態恰在 n 次碰撞後返回；其飛行總時間是

\[
T_{[x]}=S_n\tau(x)=S_ng(\pi x)>0.
\tag{8}
\]

若該物理狀態存在更短正流週期 `0<T'<T_[x]`，從第 0 次碰撞後狀態出發，返回時必仍為同一碰撞後狀態。因每段飛行時間至少 4a，途中碰撞數是某個 `1<=k<n`，所以碰撞共軛給 `sigma^k x=x`，與 n 最小矛盾。故 (8) 正是物理軌道的最小流週期。

反之，任何閉物理軌道皆雙向有界，且必有碰撞；若沒有碰撞，單位速率直線不可能閉合。從任一碰撞後狀態開始，在一個最小流週期內有有限個碰撞，由 `H_phys` 取得週期盤字。若其盤字不是 primitive，更短符號週期會給更短物理流週期，矛盾。

同一物理流軌道上改選起始碰撞只改變盤字的循環移位；反過来，若兩個編碼循環表示同一流軌道，兩個起始點都是其碰撞，沿正向流經有限次碰撞即可連接，故它們必為循環移位。於是

\[
\{\text{primitive 一側移位循環}\}
\longleftrightarrow
\{\text{primitive 雙側移位循環}\}
\longleftrightarrow
\{\text{primitive 物理流軌道}\}
\tag{9}
\]

是保最小週期的雙射。

### 3.3 方向不能一律 double；沒有隱藏的邊界 multiplicity

式 (9) 只按起始碰撞的循環移位取商，**不再按速度反轉、盤標記置換或幾何對稱取商**。這是相流軌道定義與本案編碼的對接，不假稱來源另外定義了一個名為 oriented zeta 的物件。

反轉通常給另一条相流軌道，但不是一律如此。例如兩碰撞盤字 `12` 與 `21` 已在同一循環移位類，因此往返軌道不應重複計兩次；`123` 與 `132` 不是循環移位，依唯一編碼表示不同方向的兩條相流軌道。因此不能用全局乘二或開平方修正 (5)。

圓盤互不相交，碰撞點所屬盤唯一；已有 nongrazing 與首次飛行驗證排除切觸編碼分叉。入／出速度在同一反射事件的識別只是讓物理流連續，選 postcollision 代表後不多出第二個碰撞狀態。§3.2 的單射性則排除了除起始碰撞移位外的全部重複。

此處沒有把任意有限對一 Markov 編碼當成雙射，也不需要把來源的 Markov 矩形算子與當前 `Sigma+` 算子識別。因此沒有由未知 Markov 邊界計數導入的修正因子。

### 3.4 時間保持共軛是在兩個雙側 suspension 之間

在雙側懸掛中，識別 `(x,r+tau(x))` 與 `(sigma x,r)`。由 (4)，

\[
\Phi:[x,r]_\tau\longmapsto[x,r-U(x)]_{g\circ\pi}
\tag{10}
\]

相容於懸掛邊界，逆映射加回 U；兩者與 `r→r+t` 交換。正 roof 的連續性保證這是兩個雙側 suspension 的時間保持同胚。雙側 tau 懸掛再由真實首次飛行接合識別為物理流。

一側基底 `sigma+` 非可逆；本文**沒有**稱其 suspension 與全部雙向物理狀態共軛。用一側表示的只是 (7)–(9) 的週期點／primitive 循環資料；物理流熵與時間保持共軛的敘述均置於雙側懸掛或原物理流。

## 4. 明確收斂半平面內的完全相等

定義當前正一側 roof 的週期 zeta，而不是先定義算子 determinant：

\[
Z_g(s):=\exp F_g(s),\qquad
F_g(s):=\sum_{n\ge1}\frac1n
\sum_{\sigma_+^ny=y}e^{-sS_ng(y)}.
\tag{11}
\]

令 `t=Re s`。每個一側 n 週期点由 §3.1 的唯一延拓及 (3)、(7) 滿足 `S_n g>=4an`。總點數粗界為 `3*2^n`，所以

\[
\sum_{n\ge1}\frac1n
\sum_{\sigma_+^ny=y}|e^{-sS_ng(y)}|
\le3\sum_{n\ge1}\frac{(2e^{-4at})^n}{n}<\infty
\quad\text{if }\quad
\Re s>\frac{\log2}{4a}.
\tag{12}
\]

同一界在該開半平面的每個緊集上一致。因此 (11) 定義解析且不消失的函數。這比單用 `g>=2a` 的粗半平面更寬；改進來自精確週期和，而非宣稱 g 的所有點值都至少 4a。

令 p 是最小符號週期 m 的一個 primitive 循環，物理週期為 T_p。它在第 n 層固定點和中恰於 `n=km` 出現，共有 m 個起始點，且每點權重為 `exp(-skT_p)`。因此它對 F_g 的總貢獻為

\[
\sum_{k\ge1}\frac{m}{km}e^{-skT_p}
=\sum_{k\ge1}\frac{e^{-skT_p}}k.
\tag{13}
\]

由 (12) 的絕對收斂，可先按 primitive 循環分組，再將 (13) 指數化。使用 (9)，

\[
\boxed{
Z_g(s)
=\prod_{p\ \mathrm{primitive}}(1-e^{-sT_p})^{-1}
=\prod_{\gamma\ \mathrm{primitive}}(1-e^{-s\ell(\gamma)})^{-1}
=\zeta_{\rm phys}(s),
\quad\Re s>\frac{\log2}{4a}.
}
\tag{14}
\]

兩個 product 是同一組因子的重索引，不只具有相同零極點，也不是相差某個未定常數、整函數或邊界因子。

## 5. 熵正性與物理 roof 界：完整推導責任

此節沒有把碰撞移位熵 `log 2` 直接命名為物理流熵。

### 5.1 最短的嚴格正性依據

§2 已核驗本案符合来源推論。該推論的 (6) **同時斷言存在 `c in (0,hT)`**，所以直接得到 `hT>0`。這是已引用定理結論的邏輯後果，不是來源前提核驗中預先假設 hT 正，也不是把 c 當 c0。

由 `c<hT` 和 (6)，誤差相對於主項趨向零，故

\[
\Pi(T)\sim\frac{e^{h_TT}}{h_TT},\qquad
\lim_{T\to\infty}\frac{\log\Pi(T)}T=h_T.
\tag{15}
\]

以下再把 (15) 與本案 roof 界接上，給出明確量綱；這不是獨立於經典計數定理的一般 suspension 熵證明。

### 5.2 primitive 盤字的紙面增長

令 `A=J_3-I_3` 為相鄰不等的鄰接矩陣。常數向量上 A 的特徵值為 2；座標和為零的二維空間上為 -1。因此 n 週期點數為

\[
N_n=\operatorname{tr}(A^n)=2^n+2(-1)^n.
\tag{16}
\]

這是有限矩陣的紙面恆等式，沒有執行字詞枚舉。令 b_n 是最小符號週期恰為 n 的點數。非 primitive 的 n 週期點有某個真因數 d 的週期；`d<=floor(n/2)`。允許重複計數只會放寬上界，故

\[
0\le N_n-b_n
\le\sum_{1\le d\le\lfloor n/2\rfloor}N_d
\le3\sum_{1\le d\le\lfloor n/2\rfloor}2^d
<6\,2^{\lfloor n/2\rfloor}.
\tag{17}
\]

所以 primitive 循環數 `p_n=b_n/n` 滿足

\[
p_n\sim\frac{2^n}{n},\qquad
\lim_{n\to\infty}\frac{\log p_n}{n}=\log2.
\tag{18}
\]

只在足夠大 n 使用 log；此時 (16)–(17) 保證 p_n 正。

### 5.3 碰撞數到物理時間的兩側比較

每條有 n 次碰撞的 primitive 物理軌道，由 (3)、(8) 有

\[
4an\le\ell(\gamma)\le8an.
\tag{19}
\]

於是 `Pi(8an)>=p_n`。结合 (15)、(18)，

\[
h_T=\lim_{n\to\infty}\frac{\log\Pi(8an)}{8an}
\ge\frac{\log2}{8a}.
\tag{20}
\]

反過來，若 `ell(gamma)<=T`，則碰撞數 `n<=floor(T/(4a))`。由 (16) 的粗界，對足夠大 T，

\[
\Pi(T)\le\sum_{n\le\lfloor T/(4a)\rfloor}p_n
\le\sum_{n\le\lfloor T/(4a)\rfloor}N_n
<6\,2^{\lfloor T/(4a)\rfloor}.
\tag{21}
\]

取 log、除以 T，再用 (15)，得到

\[
\boxed{0<\frac{\log2}{8a}\le h_T\le\frac{\log2}{4a}<\infty.}
\tag{22}
\]

式 (22) 的證據鏈明確是「既有物理 prime-orbit 計數定理 → (15)；紙面 primitive 字增長 + 真實 roof 界 → (20)–(21)」。本文沒有另引未核讀的 Abramov／suspension-pressure 定理，也沒有藉 (22) 宣稱當前算子的 `lambda_h=1` 或整個 pressure 介面已被證明。

## 6. 將來源延拓轉接到當前週期 zeta

來源提供某個 c0，滿足 `c0<hT`。由 (22)，`hT<=log(2)/(4a)`，因此 (14) 的整個初始半平面都位於來源延拓域 `Re s>c0` 中。即使不使用這一熵上界，只取兩者的共同充分右半平面也足以作唯一解析延拓的識別。

以 (14) 識別解析芽，當前 Z_g 便有來源所給的延拓：

\[
\boxed{
Z_g\text{ 在 }\Re s>c_0\text{ 亞純；}
s=h_T\text{ 是唯一極點且為簡單極點；}
Z_g\text{ 在此域沒有零點。}
}
\tag{23}
\]

「解析且不消失」適用於刪掉該極點後的半平面；在極點本身談的是亞純延拓。式 (23) 不給 c0 的數值，也不宣稱此域最優。

如需明寫正的左邊界，因 §5.1 已有嚴格正性，可定義

\[
c_1:=\frac{h_T+\max\{c_0,0\}}2,
\qquad 0<c_1<h_T,\qquad c_1>c_0.
\tag{24}
\]

故 (23) 可限制到 `Re s>c1`；這是本頁縮小區域的推論，**不是**把來源原句改寫為 `0<c0<hT`。c1 也不是可計算數值常數。

若只討論標量倒數，可由 (23) 得 `1/Z_g` 在該半平面解析，並只在 hT 有一個簡單零點。但本文沒有把這個標量倒數命名或識別為任何算子行列式。

## 7. 確切未推出的事項

- 沒有全平面亞純／整延拓，沒有任意左半平面的零點、極點或共振描述；(23) 只管指定存在性半平面。
- 沒有完整固定 `C^beta(Sigma+,d_theta+)` 空間上的統一高頻相消估計，也沒有透過一側化自動移植來源的幾何 Lipschitz 范數結論。
- (11) 的固定點和沒有被寫成 `Tr L_s^n`；沒有核性、trace-class、Fredholm determinant、正則化 determinant 或 dynamical determinant 的算子身份。
- 沒有 quantum determinant／Dirichlet Laplacian determinant／自伴量子生成元的域、trace identity 或全局 determinant equality，更沒有 Hilbert–Pólya 結論。
- 沒有以算子譜半徑的既有記號 lambda 取代物理熵 hT；若要壓力零點或算子主特徵值身份，需獨立列出所用定理及假設。
- 沒有把相同因子重索引的內部論證當成投稿新穎性、外部獨立認證或正式 Route／Gate 通過。

原 `A0_FAIL / A2_NOT_ELIGIBLE / NO_ROUTE_PROMOTION`、Gate 6 `NOT_ACTIVATED`、Stage 5／6 停止條件及失敗歷史均不變。本文只補充經典物理 flow-zeta 在本案上的已知解析結論，不改任何正式狀態。

## 8. 實際操作、保全與可再核對範圍

本次重新讀取所選 ARS router、academic-paper workflow、argument-builder 指引和 `docs/workflow.md`；完整重讀 [coding][coding]、[roof][roof]，沿用前一只讀輪已完整讀取的 [source-interface][source-interface]，並重新讀其身份／前提段落。只使用有限紙面論證，不建立 Material Passport、審查分數、實驗計畫或正式 receipt。

對 [Stoyanov 作者稿][stoyanov] 重新核對 §1、§2.1、Theorem 6.3、Corollary 6.4 的遠端 PDF 文字內容。來源定位是章節／定理；沒有下載本地 PDF、執行本地 PDF preflight 或冒稱頁面視覺核驗。另有一個唯讀同模型席檢查 §5.1 的來源量詞；其同意不算獨立科學證據。曾對既有 Dougall–Sharp 作者稿作有界補充查找，未取得本頁需要的新段落，未用作熵主張的證據。

寫前確認本目標不存在，只以 `apply_patch` 建立本新檔；沒有執行科學程式、字詞／軌道枚舉、數值迭代、實驗、producer、稿件 build 或正式驗證器。兩次有界 `git status` 查詢回報所在工作樹無可用 Git repository；因此不聲稱 Git diff／Git 狀態驗證通過，以明確檔案讀取和雜湊作局部保全。

寫前主要只讀輸入 SHA-256：

- [coding][coding]：`55d4f7a0cdbfc654a7707850787c76903faa04f02fb74f20e9d617197b3549e5`。
- [roof][roof]：`a770842c22c1b3164a8d0cf37ff1603e2aaebdfe52c082ccab4d0135df4ebe27`。
- [source-interface][source-interface]：`747e16336d1c393659b1940302e2aae75447812e2f03191d39154dc5016c658e`。

最初新檔寫入時三處 LaTeX 字型指令的跳脫造成 CR 控制字元；發現後只修正本新檔，保留本句作失敗／修正記錄。交接另報上述雜湊是否保持、新檔行數與雜湊，以及公式分隔符、控制字元和引用路徑的最小只讀文字檢查。這些是檔案完整性檢查，不是數學正確性或外部再現證書。

[coding]: /root/autodl-tmp/flow_systems/papers/30-three-disk-nonconstant-roof-determinant/notes/internal_biinfinite_coding_and_roof_locality_20260909.md
[roof]: /root/autodl-tmp/flow_systems/papers/30-three-disk-nonconstant-roof-determinant/notes/internal_goal01_one_sided_roof_and_transfer_bounds_20260909.md
[source-interface]: /root/autodl-tmp/flow_systems/papers/30-three-disk-nonconstant-roof-determinant/notes/internal_goal01_geometric_high_frequency_source_interface_20260909.md
[stoyanov]: https://arxiv.org/pdf/0911.5000v4
[doi]: https://doi.org/10.1017/S0143385710000933
