# P33 內部理論：tube packing 的線性字長界與有限 owner 見證常數

日期：2026-09-09 UTC。Goal01 的有界紙面論證；本分支只新增本文件。固定實際控制群、八字母、曲率負一、基點 `o=0`、`Lambda=21/10`、原 `abs(alpha)^2<=20000` guard、磁場、方向及 owner 約定。不運行科學／符號程序、BFS、有限字搜尋、實驗、producer、fixture 或正式 checker，不修改舊輸入、合同、canonical bytes、失敗紀錄或 Route／Stage 狀態。

本檔把先前由中心大球 packing 得到的指數型字長界，改成對線段 tube 作 packing 的線性位移界。精確主結論與便於有限搜尋指定的保守整數界是

\[
|g|_{\mathcal A}\le
\left\lfloor A_{\rm tube}s+B_{\rm tube}\right\rfloor-1
\quad\text{若 }r_o(g)\le s,
\qquad
|g|_{\mathcal A}\le47X+133
\quad\text{若 }r_o(g)\le X\in\mathbb Z_{\ge0}.
\tag{1}
\]

在原 guard 上，進一步取得根見證字長不超過 697、正規化共軛子見證字長不超過 1073、根指數不超過 25。這是理論搜尋上界，不是已運行的 census 或實用成本保證；線性字長上界也不表示有限字數線性增長。

## 1. 已綁定的幾何輸入與本檔記號

沿用[實際八邊形／Poincaré 筆記][geometry] §§2、6–7 的同一實際群作用：

- \(\Gamma\subset PSU(1,1)\) 是離散、無挠、余緊的定向保持群。
- D 是緊、凸、閉的真基本多邊形；各 hD 構成 face-to-face 鋪砌，內部互不相交。
- \(D\subset B_{\mathbb H^2}(o,3)\)，且存在 \(\rho_0>1/2\) 使 \(B(o,\rho_0)\subset\operatorname{int}D\)。
- 全部側鄰居恰為凍結對稱八字母集合 \(\mathcal A\)，鄰接寫成 \(hD\to haD\)、\(a\in\mathcal A\)。每個頂點的完整有限 star 按真實共享邊連通。

上述幾何識別不是由本檔重新執行的生產認證；它的外部多邊形定理前提仍按 [geometry][geometry] 的來源邊界保留。由基本域內部不交，球 \(hB(o,\rho_0)\) 兩兩不交，因而不同群中心滿足（亦見[內切球筆記][inradius] §3）

\[
d(ho,ko)\ge2\rho_0>1\qquad(h\ne k).
\tag{2}
\]

記 \(r_o(g)=d(o,go)\)，\(|g|_{\mathcal A}\) 是同一實際 PSU 群在八字母下的最小字長。以下 s 表示非負的中心位移上界，X 表示它的整數上界；二者都不是凍結矩陣中的參數 \(x=u^2\)。測地平移長度另記為 \(\ell(g)\)。

## 2. 閉測地線段的 tube 面積：中央條帶與兩個端帽

**引理 1。** 若 L 是長度 \(\lambda\ge0\) 的閉測地線段，\(r>0\)，則

\[
\operatorname{Area}\bigl(\operatorname{Tub}_r(L)\bigr)
=2\lambda\sinh r+2\pi(\cosh r-1).
\tag{3}
\]

**證明。** 先設 \(\lambda>0\)，把其支撐測地線參數化，使 L 對應 \(0\le v\le\lambda\)。在雙曲面模型採用 Fermi 參數化

\[
F(v,t)=(\cosh t\cosh v,\ \cosh t\sinh v,\ \sinh t).
\tag{4}
\]

對 Minkowski 二次型 \(-z_0^2+z_1^2+z_2^2\)，直接微分得

\[
ds_{\mathbb H^2}^{\,2}=dt^2+\cosh^2t\,dv^2,
\qquad dA=\cosh t\,dv\,dt.
\tag{5}
\]

F(v,t) 到支撐測地線上 F(w,0) 的距離滿足

\[
\cosh d\bigl(F(v,t),F(w,0)\bigr)=\cosh t\cosh(v-w).
\tag{6}
\]

故在閉區間 \(w\in[0,\lambda]\) 上的最近點由 v 截到該區間得到。垂足落在 L 內的中央條帶面積是

\[
\int_0^\lambda\int_{-r}^{r}\cosh t\,dt\,dv=2\lambda\sinh r.
\tag{7}
\]

若 \(v<0\)，最近點是第一端點；其距離不超過 r 的部分，是以該端點為心的半徑 r 球被端點法測地線切出的外側半球。\(v>\lambda\) 時對另一端點亦然。端點法測地線的反射保持該球並交換兩半，故每個端帽面積恰為球面積的一半。曲率負一的極座標面積元為 \(\sinh q\,dq\,d\theta\)，球面積為 \(2\pi(\cosh r-1)\)；兩端帽合計一個球的面積，得到 (3)。條帶與端帽的交界曲線面積為零。

若 \(\lambda=0\)，L 是單點，tube 就是半徑 r 的球，(3) 仍成立。開、閉 tube 僅差面積為零的邊界，面積比較不受影響。□

## 3. 所有觸碰 tiles 的線性 packing 界

令 \(L=[o,go]\)，其長度為 \(\lambda=r_o(g)\)。定義

\[
\mathcal T(L)=\{hD:h\in\Gamma,\ hD\cap L\ne\varnothing\},
\quad
A_{\rm tube}=\frac{\sinh(7/2)}{\pi(\cosh(1/2)-1)},
\quad
B_{\rm tube}=\frac{\cosh(7/2)-1}{\cosh(1/2)-1}.
\tag{8}
\]

這裡 L 與每個 tile 都取閉集合；只在邊或頂點碰到 L 的 tiles 也列入。

**引理 2。** \(\mathcal T(L)\) 有限，且

\[
M(L):=\#\mathcal T(L)\le A_{\rm tube}\lambda+B_{\rm tube}.
\tag{9}
\]

**證明。** 若 \(z\in hD\cap L\)，則 \(d(z,ho)\le3\)，所以 \(d(ho,L)\le3\)。因而每個以 ho 為心、半徑 1/2 的開球都包含在 L 的半徑 7/2 tube 內。由 (2)，這些開球兩兩不交。

先只取任意有限個相異觸碰 tiles，個數為 m。以引理 1 比較面積得

\[
m\,2\pi(\cosh(1/2)-1)
\le2\lambda\sinh(7/2)+2\pi(\cosh(7/2)-1).
\tag{10}
\]

右端獨立於所取有限子集。若 \(\mathcal T(L)\) 無限，便可選任意大的有限子集，違反 (10)。所以 \(\mathcal T(L)\) 有限，再取其全部元素即得 (9)。這沒有以未知局部有限性作循環前提。

本證明只使用非嚴格面積不等式；不需要另外聲稱球已填滿或嚴格未填滿 tube。閉端點及沿邊重合均已由 \(hD\cap L\ne\varnothing\) 包括。若 L 經過鋪砌頂點 z，整個 incident star 的每一個 tile 都含 z，因此全部已在 \(\mathcal T(L)\) 中，亦滿足同一距離 3 的中心界。□

## 4. 觸碰集合的側鄰接連通與刪環

**定理 3。** 若 \(r_o(g)\le s\)，則有

\[
\boxed{|g|_{\mathcal A}\le
\left\lfloor A_{\rm tube}s+B_{\rm tube}\right\rfloor-1.}
\tag{11}
\]

**證明。** D 與 gD 都在 \(\mathcal T(L)\) 中。由凸性，每個 \(L\cap hD\) 是非空閉區間或單點；引理 2 給有限個這種集合覆蓋連通線段 L。它們的相交圖連通，否則兩組圖分量的有限閉集之並會把 L 分成兩個互不相交、非空的閉集。

這還不是側鄰接連通性，必須補以下橋接：若兩個區間在 z 相交，對應 tiles 都含 z。若 z 是邊的相對內點，兩側 tiles 直接共享邊。若 z 是鋪砌頂點，完整 star 的側鄰接圖連通；用其中的邊路徑替代僅在 z 相交的跳躍。所有插入 tiles 都含 \(z\in L\)，仍在 \(\mathcal T(L)\) 中，不增加 tube 半徑或另添 \(\epsilon\) 擾動。線段沿共享邊行走及閉端點的接觸由同一論證處理。

所以 D 到 gD 有一條完全在 \(\mathcal T(L)\) 中的側鄰接路徑。刪去重複頂點之間的迴路，得到至多 \(M(L)-1\) 條邊的簡單路徑。每一步都是 \(hD\to haD\)、\(a\in\mathcal A\)，其字乘積恰表示 g。因此

\[
|g|_{\mathcal A}\le M(L)-1
\le\lfloor A_{\rm tube}\lambda+B_{\rm tube}\rfloor-1
\le\lfloor A_{\rm tube}s+B_{\rm tube}\rfloor-1.
\tag{12}
\]

當 g 是恆等元時可直接取空字，結論仍成立。□

注意：這條路徑的中間中心只保證距 L 不超過 3，未必留在 \(C_s=\{h:r_o(h)\le s\}\)。故本定理不推出 \(C_s=C_s^0\)。它是群字長界，不是原 guard 的連通性證書；與[軸到中心筆記][coverage] §4 的閉線段／star 論證相容。

## 5. 有理粗界及沒有未知實數 floor 的版本

有限搜尋的字長上限必須可以明確指定。數學上的 (11) 雖成立，卻不應把任意可計算實數表達式的 floor 無條件當作已可直接判定；若表達式恰為整數，單純細化區間並不自行認證這件事。

這裡改用明確有理界。由 \(n!\ge2\cdot3^{n-2}\)（n≥2），且部分項嚴格，有

\[
e=2+\sum_{n=2}^\infty\frac1{n!}
<2+\frac12\sum_{j=0}^\infty3^{-j}=\frac{11}4,
\quad e^{1/2}<\frac53,
\quad \cosh(1/2)-1>\frac18.
\tag{13}
\]

第二式用 \(11/4<25/9\)，第三式用 cosh 的正項展開。因 \(\pi>3\)，

\[
e^{7/2}<\left(\frac{11}4\right)^3\frac53=\frac{6655}{192},
\quad
A_{\rm tube}<\frac{6655/384}{3/8}=\frac{6655}{144}<47.
\tag{14}
\]

另一方面 \(e^{-7/2}<1\)，所以

\[
\cosh(7/2)-1<\frac{6655/192-1}{2}=\frac{6463}{384},
\qquad B_{\rm tube}<\frac{6463}{48}<135.
\tag{15}
\]

若 X 是已認證的非負整數上界，\(r_o(g)\le X\)，則由 (9)、(14)–(15)，

\[
M(L)<47X+135.
\]

因 M(L) 為整數，\(M(L)\le47X+134\)；刪環後得到

\[
\boxed{|g|_{\mathcal A}\le47X+133.}
\tag{16}
\]

這個少一的整數步驟來自嚴格的有理粗界，不依賴引理 2 的 packing 是否嚴格。

## 6. 全局平移長度下界與根指數 25

這一節固定同一控制群，不將其下界移植到 Bolza。對 hyperbolic g，令 \(A_g\) 為其軸，\(\rho=d(o,A_g)\)。[軸到中心筆記][coverage] §2.2 的位移恆等式等價於

\[
\boxed{\sinh\frac{r_o(g)}2=\cosh\rho\,\sinh\frac{\ell(g)}2.}
\tag{17}
\]

任取軸上一點，藉基本域鋪砌將它共軛入 D，得到共軛代表 h，其軸距不超過 3。對此非恆等 h，(2) 給 \(r_o(h)\ge1\)。共軛不改變平移長度，所以每個 hyperbolic g 都滿足

\[
\ell(g)\ge\sigma:=2\operatorname{asinh}
\frac{\sinh(1/2)}{\cosh3}>0.
\tag{18}
\]

這裡先共軛入 D，不能把任意原代表的軸距直接設為不超過 3。

由 (13)，

\[
\cosh3<\frac{(11/4)^3+1}{2}=\frac{1395}{128}<11,
\qquad\sinh(1/2)>1/2.
\]

又對 \(z>0\)，積分式給 \(\operatorname{asinh}z>z/\sqrt{1+z^2}\)。因此

\[
\boxed{\sigma>2\operatorname{asinh}(1/22)
>\frac2{\sqrt{485}}>\frac1{12}.}
\tag{19}
\]

若 \(a^m=g\)、\(m\ge2\)，則 a 是 hyperbolic，與 g 同軸且 \(\ell(a)=\ell(g)/m\)。故對 \(\ell(g)\le\Lambda=21/10\)，

\[
m\le\frac\Lambda\sigma<\frac{21}{10}\,12=25.2,
\qquad\boxed{m\le25.}
\tag{20}
\]

無挠、定向保持條件也排除了軸端点互換的二階半轉；其餘軸穩定子是離散平移子群，因而循環。這與 primitive-root 結構相容，但 (20) 的有限指數界另有上述長度理由。

## 7. 原 guard 的 T<12 及共軛子位移界小於 20

原 guard 寫為

\[
T=2\operatorname{arcosh}\sqrt{20000},
\qquad\sinh(T/2)=\sqrt{19999}<142.
\tag{21}
\]

沿用[軸到中心筆記][coverage] §6.2 已明列的有限 Taylor 下界，

\[
e^3>\sum_{j=0}^{9}\frac{3^j}{j!}=\frac{22471}{1120}>20.
\tag{22}
\]

最後一個有理比較只需 \(22471>22400\)。從而

\[
\cosh6>\frac{e^6}{2}>200>\sqrt{20000},
\qquad\boxed{T<12.}
\tag{23}
\]

对任意 hyperbolic \(g\in C_T\)，由 (17)–(18)，其軸距滿足

\[
d(o,A_g)\le Q:=\operatorname{arcosh}
\frac{\sinh(T/2)}{\sinh(\sigma/2)}.
\tag{24}
\]

\(\sigma>1/12\) 給 \(\sinh(\sigma/2)>1/24\)，故 \(\cosh Q<24\cdot142=3408\)。因 \(\operatorname{arcosh}z<\log(2z)\)（z≥1），且 (22) 給 \(e^9>8000>6816\)，

\[
\boxed{Q<\log6816<9.}
\tag{25}
\]

如改採備用有理比較，\(e>8/3\) 及
\(6816\cdot19683=134159328<134217728=8^9\)
也給 \(e^9>6816\)；此處採用 (22) 的較短證明，不需大整數比較作主鏈。

若 hyperbolic \(g,h\in C_T\)、\(\ell(g),\ell(h)\le\Lambda\)，並有
\(cgc^{-1}=h^\varepsilon\)、\(\varepsilon\in\{+1,-1\}\)，令 p、q 分別為 o 到 \(A_g,A_h\) 的垂足。c 把 \(A_g\) 送到 \(A_h\)；取整數 n，使 \(h^ncp\) 沿 \(A_h\) 到 q 的距離不超過 \(\ell(h)/2\)。左乘 \(h^n\) 不改變該共軛關係，而且

\[
\begin{aligned}
r_o(h^nc)
&\le d(o,q)+d(q,h^ncp)+d(h^ncp,h^nco)\\
&\le Q+\ell(h)/2+Q
\le2Q+\Lambda/2=:\mathcal B.
\end{aligned}
\tag{26}
\]

因此若有任何共軛子，必有位移不超過 \(\mathcal B\) 的共軛子；不要求 g 或 h 已本原。由 (25)，

\[
\boxed{\mathcal B<18+21/20=381/20<20.}
\tag{27}
\]

## 8. 根 697、共軛子 1073：有限見證界的精確含義

**推論 4。** 對原 guard 內、\(\ell(g)\le21/10\) 的 hyperbolic g：

1. 若 \(a^m=g\)、\(m\ge2\)，則存在該根 a 的字表示，其字長不超過 697，且 \(2\le m\le25\)。
2. 對另一個同樣在 guard 內且 \(\ell(h)\le21/10\) 的 hyperbolic h，若 \(g\sim_\Gamma h^\varepsilon\)，則存在字長不超過 1073 的共軛子見證。

**證明。** 根 a 與 g 同軸。在 (17) 中固定軸距，右端對平移長度嚴格遞增，因此

\[
r_o(a)\le r_o(g)\le T<12.
\]

以 X=12 代入 (16)，並用 (20)，得

\[
\boxed{|a|_{\mathcal A}\le47\cdot12+133=697,
\qquad m\le25.}
\tag{28}
\]

共軛子先按 (26) 正規化至位移小於 20，再以 X=20 代入 (16)，得

\[
\boxed{|c_{\rm normalized}|_{\mathcal A}
\le47\cdot20+133=1073.}
\tag{29}
\]

根不必屬於原 guard 的 identity component \(C_T^0\)，正規化共軛子也不必在原 guard 中；以上字長界沒有作這些假設。□

[精確狀態筆記][exact]給有限字的 actual PSU 身份與有限判等方法。因此，在紙面上若完整考慮所有長度至多 697 的八字母字及指數 2–25，便不會漏掉真正的 proper root；完整考慮所有長度至多 1073 的字，也不會漏掉經 (26) 正規化的共軛子。這是有界搜尋能支撐否定結論的覆蓋理由，不是「程序可判定」四字本身。

判定等式仍須是實際 PSU 等式：SU 矩陣表示中容許整體 ±，不能逐 entry 任選符號。原 g、h 和候選字均須有 exact binding。完整群共軛及外部逆元分支分別檢查 \(cgc^{-1}=h\) 或 \(h^{-1}\)，不以同 trace、同長度或有限 component 內找不到見證代替它。

這些輔助字的考慮不更改 CP 的輸出域或 `20000` guard，也不需要把原 guard 宣告為連通。字數至多按 \(\sum_{j=0}^{L}8^j\) 增長；即使把無約簡詞或重複矩陣去除，本文也沒有提供可行牆鐘成本、儲存量、統一實用精度或可運行規模的證明。

## 9. CER、反對意見與未完成邊界

| 本輪主張 | 紙面依據 | 反對意見／邊界 |
| --- | --- | --- |
| 線段 tube 面積為 (3) | 雙曲面 Fermi 微分、最近點截斷、中央條帶及兩端帽 | 端點不可忽略；長度零另處理 |
| 全部觸碰 tiles 有線性數量界 | 半徑 1/2 分離球，包含於半徑 7/2 tube | 先對有限子集比較，不能預設有限性；只觸頂點的 tiles 亦列入 |
| 線性 tile 數給線性字長 | 閉區間交圖、完整 vertex-star 側連通及刪環 | 有限性不推出連通；不假設原中心 guard 連通 |
| 明確 697／1073／25 見證界 | 有理粗界、T<12、Q<9、同軸根及正規化共軛子 | 有界且可判等不等於已遍歷，更不等於運行可行 |

本輪沒有運行根或共軛搜尋、BFS、owner quotient、FIFO／canonical-stream／digest 檢查，也沒有產生 observed count 或正式回執。它不更新舊普查數字，不替代 BP 的 strict-systole gate，不建立 determinant、Route 或 Stage 5／6 的新結論。

## 10. 方法、實際動作與来源

使用 ARS academic-paper 的有界 argument-builder 指引，把幾何前提、主公式、整數化及見證覆蓋分開，並明列端點、vertex-star、guard 連通性與成本反對意見；不是 full pipeline、正式 reviewer 或稿件修訂。已讀實際 repo 指南、相應 router／workflow／role，以及下列相關筆記。新增 tube、粗界與算術鏈均在本文直接推導，沒有新增外部文獻主張、網頁查詢或材料上傳。

唯一文件寫入為 `apply_patch` 新建本檔；寫前檢查目標不存在。其他動作限於文件定位、讀取、SHA-256 及純文字檢查；其實際結果在交接中報告，不冒稱科學程序、形式化驗證或生產認證。

首次純文字檢查發現 (13) 的一個 LaTeX 反斜線在寫入字串時被轉成 form-feed 控制字元；只在本新檔以 `apply_patch` 更正為 `\frac`，沒有改變數學公式或任何舊檔。

[geometry]: /root/autodl-tmp/flow_systems/papers/33-bolza-control-matched-census/notes/internal_goal01_exact_polygon_and_poincare_certificate_20260909.md
[coverage]: /root/autodl-tmp/flow_systems/papers/33-bolza-control-matched-census/notes/internal_axis_to_center_coverage_and_finite_guards_20260908.md
[inradius]: /root/autodl-tmp/flow_systems/papers/33-bolza-control-matched-census/notes/internal_inradius_separation_and_explicit_guard_capacity_20260909.md
[exact]: /root/autodl-tmp/flow_systems/papers/33-bolza-control-matched-census/notes/internal_exact_state_identity_and_guard_decidability_20260909.md
