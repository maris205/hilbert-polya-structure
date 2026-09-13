# P33 內部理論：內切球、中心分離與明確 guard 容量

日期：2026-09-09 UTC。本輪只新增這份有界內部數學筆記。固定真實曲面、`Lambda=21/10`、曲率負一的基底測地長度、磁場鎖、外部逆元配對 owner 與 BP／CP 合同；不執行 BFS、枚舉、實驗、fixture、producer 或 checker，不更改現稿、舊證據、guard、狀態或 Stage 5／6 邊界。

[前輪筆記][coverage]證明：在真基本域、完整側鄰接及頂點 star 的前提下，短共軛類有代表落入固定 CP 中心 guard 的 identity-connected component；若另有中心分離下界，便能作 packing。本輪補上該分離下界的幾何來源，並取得保守容量

\[
\boxed{N_{\max}=533312,\qquad
8N_{\max}=4266496,\qquad N_{\max}-1=533311.}
\tag{1}
\]

三者分別界住 guard 內相異群元素數、完整八字母有向邊檢查數、component 內簡單路徑長。這些是下述前提下的數學上界，不是已觀測狀態數、實測成本或生產回執。

## 1. 先核對實際頂點，不從示意圖猜八邊形

本輪普通一手瀏覽讀取 A. V. Nazarenko, *Two-parametric hyperbolic octagons and reduced Teichmüller space in genus two*, arXiv:1301.5446v1 (2013)，定位在 §2 作者第 3 頁的頂點定義、第 4 頁 (10)–(11)。其頂點是

\[
a e^{ik\pi/2},\qquad
b_{\rm geom}e^{i(\vartheta+k\pi/2)},\qquad k=0,1,2,3,
\]

其中 `vartheta` 對應來源的角度 `alpha`；`b_geom=(sqrt(2) a cos(vartheta-pi/4))^-1`。`b_geom` 是頂點半徑，不是項目的磁場參數。來源也給出 admissible 參數域；上述公式與定位來自[作者 v1 原文][S01]，不是以後續數值回放代替來源內容。

[凍結控制矩陣][control-input]的 `definition` 明確固定

\[
a=u=e^{-1/10},\qquad \vartheta=\pi/4,\qquad
b_{\rm geom}=\frac1{\sqrt2u}.
\tag{2}
\]

所以本輪真正要處理的是依極角排序、相鄰角差恰為 `pi/4` 的八個頂點，而非一般角度的兩參數族。下文矩陣上左元素仍用 `alpha_g`，不要與來源的角度參數混同。

由 `e^(-1/5)>1-1/5=4/5>1/2`，得

\[
\frac1{\sqrt2}<u<1,\qquad
\frac1{\sqrt2}<b_{\rm geom}<1.
\tag{3}
\]

這也直接核對了 (2) 在來源 (10) 的 admissible 區間內。接下來用 (2)–(3) 直接證明這個幾何八邊形的內切球；不採用凍結物件的 `PASS`、`PROVED` 或任何舊狀態數作為數學論據。

## 2. Klein 直線多邊形的自含內切球證明

令 `D_C` 暫指由上述頂點依序連接雙曲測地邊所得的閉八邊形。這裡先只研究它的形狀，尚未把它宣告為已完成生產認證的群基本域。

### 2.1 模型變換與凸性

Poincaré 圓盤到 Klein 圓盤的徑向變換為

\[
K(z)=\frac{2z}{1+|z|^2},\qquad
f(r)=\frac{2r}{1+r^2},\quad 0\le r<1.
\tag{4}
\]

`f'(r)=2(1-r^2)/(1+r^2)^2>0`，所以它是保極角的徑向同胚。其將雙曲測地線送到直線，可直接檢查：與單位圓正交的圓滿足

\[
|z-c|^2=|c|^2-1
\quad\Longleftrightarrow\quad
2c\mathbin{\cdot}z=1+|z|^2
\quad\Longleftrightarrow\quad c\mathbin{\cdot}K(z)=1;
\]

過原點的直徑則仍為直徑。

記 Klein 頂點半徑為

\[
U=f(u),\qquad V=f(b_{\rm geom}).
\]

由 (3) 與單調性，

\[
\frac{2\sqrt2}{3}<U,V<1.
\tag{5}
\]

八個直線頂點依序是 `(U,0)`、`(V/sqrt(2),V/sqrt(2))`、`(0,U)` 及其旋轉。相鄰線段留在其夾角 `pi/4` 的扇區中，故這條閉折線簡單並包圍原點。它也是嚴格凸的：在半徑 `U` 和 `V` 的兩類頂點，沿逆時針行進的相鄰邊叉積為正，分別等價於

\[
U>\frac V{\sqrt2},\qquad V>\frac U{\sqrt2}.
\]

這兩式都由 (5) 推出，因為 `2sqrt(2)/3>1/sqrt(2)`。一條簡單、各轉角嚴格同向的八邊折線是凸多邊形。因此 `K(D_C)` 是這八個頂點的凸包，且原點在其內部。

### 2.2 每條支撐直線距原點都大於 2/3

取任何相鄰頂點，兩半徑記為 `p,q`，夾角為 `pi/4`。交換兩端點後可設 `p>=q`。連線長度及原點到整條直線的距離 `h` 為

\[
L=\sqrt{p^2+q^2-\sqrt2pq},\qquad
h=\frac{pq\sin(\pi/4)}{L}.
\tag{6}
\]

由 `q<=p<sqrt(2)p`，有 `q^2-sqrt(2)pq<0`，故 `L<p`。於是

\[
\boxed{h>\frac q{\sqrt2}>\frac23.}
\tag{7}
\]

這裡使用的是整條支撐直線的距離，不需假定垂足落在邊段內。凸多邊形等於其八個含原點側半平面的交；(7) 因而給出

\[
\overline B_{\rm Eucl}(0,2/3)\subset\operatorname{int}K(D_C).
\tag{8}
\]

現在 `f(1/4)=8/17<2/3`。將 (8) 透過徑向同胚 (4) 拉回，得到所需的較保守圓盤包含關係

\[
\boxed{\{|z|\le1/4\}\subset\operatorname{int}D_C.}
\tag{9}
\]

這一結論只用頂點公式、測地邊與初等代數，沒有矩陣數值計算、取樣或圖像估測。

### 2.3 雙曲內切半徑大於 1/2

曲率負一的圓盤徑向距離由線元直接積分：

\[
d(0,z)=\int_0^{|z|}\frac{2\,dt}{1-t^2}
=\log\frac{1+|z|}{1-|z|}.
\]

因此 (9) 對應

\[
\overline B_{\mathbb H^2}(0,\rho_0)
\subset\operatorname{int}D_C,
\qquad \rho_0=\log\frac53.
\tag{10}
\]

以下同時準備 packing 所需的有理數上界。對 `n>=2`，`n!>=2*3^(n-2)`，從 `n=4` 起嚴格。因此

\[
e=2+\sum_{n=2}^{\infty}\frac1{n!}
<2+\frac12\sum_{j=0}^{\infty}3^{-j}
=\frac{11}{4}<\frac{25}{9}.
\]

所以

\[
\boxed{e^{1/2}<\frac53,\qquad \rho_0>\frac12.}
\tag{11}
\]

## 3. 從內切球到群中心分離：基本域前提不可省略

**一般命題。** 若群 `Gamma` 等距作用於雙曲平面，`D` 是其閉基本域，不同群元素的 `gD` 內部互不相交，且

\[
B(o,r)\subset\operatorname{int}D,
\]

則對不同 `g,h in Gamma` 有

\[
\boxed{d(go,ho)\ge2r.}
\tag{12}
\]

**證明。** `B(go,r)=gB(o,r)` 在 `int(gD)` 內，故這些開球兩兩不交。若 `d(go,ho)<2r`，連接二中心的測地線中點同時在兩開球中，矛盾。□

將此命題應用於 (10) 的 `D_C`，必須另有**同一個真實群作用與八邊形的基本域識別**：它的 translates 覆蓋平面，且不同群元素對應的 tile 內部不重疊。局部包含關係 (9) 自己並不證明這項識別，更不能僅從抽象 relator 或十進位矩陣殘差推出它。

在這項前提下，(10)–(12) 給出

\[
d(go,ho)\ge2\rho_0>1\quad(g\ne h),
\qquad \boxed{\delta=1\text{ 是有效的保守中心分離界。}}
\tag{13}
\]

特別地 `d(o,go)>=1` 對所有非恒等元成立。這是固定基點的群軌道分離，不是對所有軸的平移長度或整個曲面 systole 的新下界。不能用 (13) 取代 BP 的 strict-systole gate，也不能將控制群的這一條件性結果移植成 Bolza 回執。

## 4. 固定 20000 guard 的明確整數容量

對作用於同一圓盤、同一基點 `o=0` 的 `SU(1,1)` lift，記上左元素為 `alpha_g`。[前輪][coverage]由圓盤作用公式得到

\[
\cosh^2\!\left(\frac{d(o,go)}2\right)=|\alpha_g|^2.
\]

因此[現有 CP 合同][cp-contract]及[凍結 guard][finite-input]中的 `abs(alpha_g)^2<=20000` 恰是閉中心球

\[
C_T=\{g:d(o,go)\le T\},\qquad
T=2\operatorname{arcosh}\sqrt{20000},\qquad
\boxed{\cosh T=39999.}
\tag{14}
\]

本輪沒有調整 guard 或把平移長度 cutoff 與中心位移混為一談。

由 (13)，以 `C_T` 的各中心為圓心、半徑 `1/2` 的開雙曲球兩兩不交，且均包含於 `B(o,T+1/2)`。曲率負一的極座標面積元是 `sinh(r) dr dtheta`，所以半徑 `r` 的球面積為 `2pi(cosh r-1)`。對任意有限中心子集比較面積便有

\[
N\le\frac{\cosh(T+1/2)-1}{\cosh(1/2)-1}.
\tag{15}
\]

該界與子集無關，故也直接證明 `C_T` 有限，(15) 可取 `N=#C_T`，不必以未知有限性作循環前提。又因 `sinh T<cosh T`、`sinh(1/2)>0`，

\[
\begin{aligned}
\cosh(T+1/2)
&=\cosh T\cosh(1/2)+\sinh T\sinh(1/2)\\
&<\cosh T\,e^{1/2}
<39999\cdot\frac53=66665.
\end{aligned}
\tag{16}
\]

另一方面，雙曲餘弦的正項展開給出

\[
\cosh(1/2)-1>\frac{(1/2)^2}{2}=\frac18.
\]

代入 (15)，

\[
\boxed{\#C_T<\frac{66665-1}{1/8}=533312.}
\tag{17}
\]

我們取 (1) 的 `N_max=533312` 作保守整數上界；(17) 是嚴格不等式，這個選擇刻意不利用最後一步整數取整的改善，也不聲稱最優。恒等元已計入 `#C_T`。

若完整鄰接字母表恰為合同中的四個生成元及其逆元，則 `q=8`。其 identity-connected component `C_T^0` 是 `C_T` 的子集，故每個頂點恰處理一次時，完整有向邊分類的項數至多 `8N_max=4266496`；component 中任意兩點間可刪去環路，得到至多 `N_max-1=533311` 條邊的簡單路徑。

這裡的「狀態數」是相異 `PSU` 群元素數，不是未去重字串、所有共軛代表、所有詞或 outside-guard 拒絕項的儲存數。若實作反覆擴展同一元素，這個邊數上界不約束其重複工作。即使精確去重成立，上界仍不約束每次判定所需精度、位元長度、記憶體配置或牆鐘時間。

## 5. 有限完整邊展開證書的語義，不是本輪實作

上述容量可協助界定未來有限證書，但不能自己證明隊列曾被完整處理。若一個候選記錄提供有限列表 `L`，以下語義條件足以證明它恰為 `C_T^0`：

1. `L` 中各狀態與同一真實 `PSU` 群元素有可驗證綁定；去重當且僅當元素相同；包含恒等元；每個列入元素均精確滿足閉 guard。
2. 每個非恒等列入元素都有一條從恒等元出發、完全留在 `L` 內的實際字母路徑，或等價的已驗證發現樹。這排除憑空把其他 component 混進來。
3. 對每個 `h in L` 及全部八個有序字母 `a`，都有一個完備分類：`ha` 精確等於 `L` 中某元素，或有精確證明 `d(o,hao)>T`。不能把區間跨越邊界、找不到 duplicate 或 unresolved 當成排除證明。乘法方向須與版本合同一致。

由第 1–2 項，`L subseteq C_T^0`。反之，若有從恒等元到遺漏元素的域內字母路徑，取沿路第一個遺漏者；其前驅在 `L` 中，第 3 項不能合法排除這條仍在閉 guard 內的邊，只能把其目標指向 `L`，矛盾。故

\[
\boxed{L=C_T^0.}
\tag{18}
\]

若真基本域還具有[前輪定理][coverage]要求的完整側／頂點 incidence，則前輪的 `R=3`、`T>Lambda+3R=111/10` 已使每個短 owner 有代表進入 `C_T^0`。本輪 (17) 只為這個有限 universe 補上保守容量；從候選元素到精確 owner 商所需的 cutoff、本原性、完整群共軛及逆元配對判定仍未實作。

以上只描述集合完整性的充分語義，不是現有合同的替代品。合同仍要求 FIFO 次序、規範 bytes、排序流、全部 digest 綁定、零 unresolved ledger 及獨立 replay。也未證明任一特定 interval-only guard 判定對所有狀態都會終止：閉 guard 上的等號情形仍須精確處置。本輪不寫 verifier、不產生新 canonical receipt、不填版本或 observed digest 空槽。

## 6. 論證責任與仍未閉合之處

| 主張 | 本輪證據或推理 | 明確保留的反對意見／邊界 |
| --- | --- | --- |
| 固定八邊形含有 `rho_0=log(5/3)>1/2` 的中心球 | S01 頂點與凍結參數對應；(3)–(11) 的自含幾何證明 | 不把一般角度族或不同模型套入固定公式 |
| `delta=1` 可用於所有相異群中心 | 真基本域內部不交前提加一般命題 (12) | 局部八邊形幾何本身不認證實際群鋪砌 |
| 固定 CP guard 的容量不超過 (1) | 精確中心位移公式、面積與有理數界 (14)–(17) | 不是舊 `18533` 狀態／最深 `11` 層的 replay，也不是計算成本保證 |
| 有限全邊證書可刻畫 `C_T^0` | 第 5 節三項語義及首個遺漏者反證 | 未生成此證書；完整幾何 incidence、owner 商、合同 replay 仍另需證據 |

[BP 合同][bp-contract]仍只走另行 passage-adequate strict-systole 證明及精確 replay 後的 conditional empty-stream 路線。本輪的中心 packing 既不取代該路線，也不賦予新枚舉權限。沒有新的 BP／CP producer 運行、普查結果、Route 判定、正式審稿或階段解鎖。

## 7. 方法、來源動作與文件保全

本輪使用 ARS academic-paper 的 argument-builder 單一論證階段，將幾何命題、群作用前提、容量推論與實例證書分開；不啟動 full pipeline，不產生 venue-fit 或正式 integrity-PASS 宣告。已完整讀取當輪 `AGENTS.md`、`docs/workflow.md`、安裝中的 ARS router、academic-paper workflow 與 argument-builder role，再讀前輪覆蓋筆記、兩份合同、凍結矩陣定義及 guard 相關欄位。

唯一新增外部來源動作是普通瀏覽 `https://arxiv.org/pdf/1301.5446v1`，讀取 §2 對本輪所需頂點、admissible 區間及半徑公式的支持。使用的是瀏覽器可讀作者 v1 內容，不是本輪下載的本地 PDF，不宣稱遠端讀取已重播舊來源檔案 SHA。之前 DOI／截圖失敗不重試，既有失敗記錄不改寫；沒有 bibliographic API client、外部模型或未公開內容上傳。

新推論均在本文給出紙面證明，沒有矩陣數值 replay、枚舉或科學實驗。只用 `apply_patch` 寫本文件；其他動作限於只讀定位、讀取、SHA-256 與文本結構檢查。文件保全與任何同伴覆核只報告實際範圍，不構成獨立科學認證。

寫後檢查：三份前輪筆記、現稿、兩份合同與三份凍結輸入共九個受保護舊檔，SHA-256 全部與寫前一致。`node -e` 的只讀文本檢查通過六個引用定義、八處引用使用、所有本地引用目標、27 對顯示數學分隔符及連續 (1)–(18) 標籤；控制字元、行末空白、衝突標記及末尾換行檢查亦通過。`git diff --check` 與 `git status --short` 因當前目錄不是 Git repository 而不可用；沒有重設 Git 發現邊界，改用上述直接文本檢查，不宣稱 Git 檢查通過。

[coverage]: /root/autodl-tmp/flow_systems/papers/33-bolza-control-matched-census/notes/internal_axis_to_center_coverage_and_finite_guards_20260908.md
[control-input]: /root/autodl-tmp/flow_systems/papers/28-bolza-magnetic-flow/results/round7_nonarithmetic_control_matrices.json
[finite-input]: /root/autodl-tmp/flow_systems/papers/28-bolza-magnetic-flow/results/round8_control_finite_ball_certificate.json
[cp-contract]: /root/autodl-tmp/flow_systems/papers/33-bolza-control-matched-census/notes/stage4_prime_round5_support/cp_enumeration_contract.json
[bp-contract]: /root/autodl-tmp/flow_systems/papers/33-bolza-control-matched-census/notes/stage4_prime_round5_support/bp_enumeration_contract.json
[S01]: https://arxiv.org/pdf/1301.5446v1
