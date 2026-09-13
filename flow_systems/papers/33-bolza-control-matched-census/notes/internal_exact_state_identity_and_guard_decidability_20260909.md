# P33 內部理論：精確狀態身份與 closed guard 的可判定性

日期：2026-09-09 UTC。第五次 P29–33 整輪的有界內部理論；唯一新增為本文件。固定 S01 控制矩陣、`Lambda=21/10`、`abs(alpha)^2<=20000`、曲率負一的基底測地長度、磁場、方向與 owner 規則。不執行符號程序、BFS、枚舉、producer、fixture、實驗或正式 checker，不更改舊輸入、合同、根記錄、現稿、回執及 Stage／Route 狀態。

[上輪全邊證書語義][inradius]仍要求「精確矩陣身份」與「每條 closed-guard 比較均能終止」。本輪不再重述有限容量，而對凍結八字母給出兩個具體增量：

- 指定嵌入的二次函數域提供有限代數身份判定，包含 `PSU` 的整體正負號。
- 對每一個有限字，guard 等號 `abs(alpha)^2=20000` 都不可能發生；清分母多項式的符號可由有理 Taylor 包圍有限決定。另對 hyperbolic 有限字排除幾何長度等於 `21/10`。

這些是精確有限字的判定定理，不是某個已實作的 parser、state codec、interval library 或 census 通過驗證。尤其，個別比較終止不等於已提供實用統一精度或計算成本。

## 1. 從實際八字母公式選擇數域與正分支

### 1.1 凍結定義，而非十進位欄位

[控制矩陣物件][control-input]的 `definition` 固定 `a=exp(-1/10)`、`x=exp(-1/5)`、`N=-1/sqrt((1-x)(2x-1))`，以及兩個直接生成元和旋轉共軛得到的另兩個生成元。[CP 合同][cp-contract]只使用這四者及其逆元。

令

\[
u=e^{-1/10},\qquad x=u^2,\qquad
D(U)=(1-U^2)(2U^2-1),\qquad
y=\sqrt{D(u)}>0,
\qquad N=-1/y.
\tag{1}
\]

此處 U 是形式變量，`D(U)` 是多項式，不是上輪的基本八邊形。`9/10<u<1`，故 `u^2>1/2`、`D(u)>0`；(1) 明確選擇正的平方根，保留凍結 N 的負號。

在 `Z[i][U]` 中定義

\[
\begin{aligned}
B_0(U)&=U^2+i(1-U^2),&
B_1(U)&=(1-U^2)+iU^2,\\
B_2(U)&=iB_0(U),&B_3(U)&=iB_1(U).
\end{aligned}
\tag{2}
\]

這裡的 bar 對係數取複共軛並固定 U。凍結旋轉為
`R_rot=diag(exp(i*pi/4),exp(-i*pi/4))`；其共軛把上右元素乘 i、下左元素乘 −i，所以 (2) 的方向與 `g2=R_rot*g0*R_rot^-1`、`g3=R_rot*g1*R_rot^-1` 一致。

對 `j=0,1,2,3`、`epsilon in {+1,-1}`，設

\[
H_{j,\epsilon}(U)=
\begin{pmatrix}U&\epsilon B_j(U)\\
\epsilon\overline{B_j}(U)&U\end{pmatrix},
\qquad
G_{j,\epsilon}=-\frac{H_{j,\epsilon}(u)}y.
\tag{3}
\]

`epsilon=+1` 對應 `g_j`，`epsilon=-1` 對應其逆元。直接代數給

\[
B_j\overline{B_j}=U^4+(1-U^2)^2,
\qquad
\det H_{j,\epsilon}
=U^2-U^4-(1-U^2)^2=D(U).
\tag{4}
\]

因此 (3) 的實際矩陣 determinant 恰為 1、具有 `SU(1,1)` 形式，取 adjugate 也直接驗證了 inverse 的符號。這裡沒有使用十進位 determinant residual 或舊 `PROVED` 標籤。

`R_rot` 本身不是字母；其 entries 含八次單位根，不必放入下面的最小工作域。凍結物件中的角度、`b_geom` 等幾何 metadata 也不在「八字母矩陣 entries 落在此域」的量詞內。這是精確消去旋轉共軛的常數，不是改變曲面或擴充生成元。

### 1.2 唯一使用的外部超越性定理

Hermite–Lindemann 定理說：非零代數數的指數是超越數。本輪在作者公開的 Michel Waldschmidt, *Elliptic Functions and Transcendence*, §1.1、Theorem 4、印刷頁 144 核對此敘述；取代數數 `-1/10`，得到 u 超越。[作者章節原文][HL]

實際所需的最小外部前提還可以更弱：同頁 Theorem 1 給出 e 超越，而 `u^-10=e`，所以若 u 代數，e 也會代數，矛盾。下面只使用「u 超越」這個結論，不需要完整 Lindemann–Weierstrass 定理。

本輪把這個經定位的經典定理作為外部前提，不聲稱在此重證它，也沒有使用 Schanuel 猜想、兩個獨立指數值的代數獨立性或任何未給出的有效超越測度。

## 2. 指定嵌入的二次函數域與有限判零

令

\[
K=\mathbb Q(i)(U),\qquad
E=K[Y]/\bigl(Y^2-D(U)\bigr),
\qquad
\iota:U\mapsto u,\quad Y\mapsto y>0,\quad i\mapsto i.
\tag{5}
\]

**命題 1。** E 是 K 的二次擴張，且 (5) 定義單射 `E -> C`。

**證明。** `D(U)` 在 `U=1` 恰有一階零點：因子 `1-U^2` 在此有單零，`2U^2-1` 在此非零。任何非零有理函數平方的零／極點階數均為偶數，所以 D 不是 K 中的平方。故 `Y^2-D` 不可約，E 是域，每個元素唯一寫成 `r(U)+s(U)Y`，其中 `r,s in K`。

u 超越使每個非零 `Q[U]` 多項式在 u 非零。對 Gaussian 有理係數，分別取實、虛部即可得到相同結論，所以 `K -> C` 的代入單射，所有非零有理函數分母均可代入。

若 `r(u)+s(u)y=0` 且 `s!=0`，平方後得到
`D(u)=(r/s)(u)^2`；由 K 的單射，必有形式有理函數等式 `D=(r/s)^2`，與非平方性矛盾。若 `s=0`，則 `r(u)=0` 強迫 `r=0`。因此

\[
\boxed{\iota(r+sY)=0\quad\Longleftrightarrow\quad r=s=0.}
\tag{6}
\]

這既建立指定嵌入，也證明它單射。□

在 E 中加、乘只需用 `Y^2=D` 降次。對非零 `r+sY`，逆元為
`(r-sY)/(r^2-Ds^2)`；分母非零仍由 D 非平方得出。把 K 中每個有理函數寫成互質多項式分子／首一分母，Gaussian 有理數運算、多項式除法及 gcd 都是有限精確代數操作。因此 E 中的零、相等與合法除法有有限判定，不需要靠小數接近猜等號。

複共軛固定 u、y，故在形式域中正是 `i -> -i`、`U,Y` 不變。不能把 Y 視為另一個與 U 代數獨立的變量；其二次關係是判零不可省略的一部分。

## 3. 精確 word replay 與實際群元素身份

令 w 是合同八字母的有限字，長度為 n，允許空字 `n=0`。按原次序相乘，定義

\[
P_w(U)=\prod_{a\text{ 依次出現在 }w}H_a(U)
\in\operatorname{Mat}_2(\mathbb Z[i][U]),
\qquad
\mathcal M_w=(-1)^nY^{-n}P_w(U),
\qquad M_w=\iota(\mathcal M_w).
\tag{7}
\]

空乘積為 I。這個乘法方向與實際字序一起綁定；(7) 是 (3) 的直接串接，不涉及抽象群 normal-form 猜測。當 n 為偶數時，`Y^-n=D^(-n/2)`；當 n 為奇數時，`Y^-n=Y D^(-(n+1)/2)`，所以矩陣 entries 都有 §2 的有限表示。

對兩個有限字 w、v，單射 (6) 給出 `M_w=M_v` 當且僅當四個 E entries 相等。實際定向雙曲等距作用使用 `PSU(1,1)=SU(1,1)/{+I,-I}`，因此

\[
\boxed{
[M_w]=[M_v]
\quad\Longleftrightarrow\quad
\mathcal M_w=\mathcal M_v\quad\text{或}\quad
\mathcal M_w=-\mathcal M_v.
}
\tag{8}
\]

兩個 determinant-one 矩陣給出同一 Möbius 作用時彼此成比例，而 determinant 迫使比例為 ±1；這是 (8) 的中心符號來源。每一個候選符號必須同時適用於全部四個 entries，不能逐 entry 任選正負。

所以對這個實際矩陣生成群，word identity、duplicate、相鄰乘積與候選目標是否相等都能有限精確決定。它**不**證明某份舊 state encoding 已正確實作這個判定，也不把矩陣群自動識別成已認證的抽象曲面群、離散群或基本域鋪砌。這些幾何／版本綁定仍是[前輪覆蓋定理][coverage]的另外前提。

本輪沒有選擇新的 canonical bytes 或修改合同中的 exact normalized-state deduplication 語義。判定兩個已綁定矩陣是否相同，也不同於判定其完整群共軛類、根或 owner 是否相同。

## 4. Closed guard 等號對所有有限字均不可能

取 `p_w(U)=(P_w(U))_11`。由 (7)、正的 y 及複共軛規則，

\[
|\alpha_w|^2
=\frac{p_w(u)\overline{p_w}(u)}{D(u)^n},
\qquad
\Phi_w(U):=p_w(U)\overline{p_w}(U)-20000D(U)^n
\in\mathbb Z[U].
\tag{9}
\]

多項式 `p_w bar(p_w)` 的係數既是 Gaussian integers 又被共軛固定，因此確實是整數。分母 `D(u)^n>0`，所以 guard 的差值與 `Phi_w(u)` 同號。

**命題 2。** 對任何有限字 w，`Phi_w` 都不是零多項式。

**證明。** 純粹在多項式層面代入 `U=0`。由 (2)–(3)，每個 `H_a(0)` 都是反對角矩陣，其兩個非零 entries 都在 `{+1,-1,+i,-i}`。這類矩陣相乘時，偶數個因子的乘積為對角 Gaussian-unit 矩陣，奇數個則仍為反對角 Gaussian-unit 矩陣。因此 n 偶數時 `p_w(0)` 是 Gaussian unit，n 奇數時 `p_w(0)=0`。又 `D(0)=-1`，故

\[
\boxed{
\Phi_w(0)=
\begin{cases}
1-20000=-19999,&n\text{ 偶數},\\
20000,&n\text{ 奇數}.
\end{cases}}
\tag{10}
\]

兩者皆非零；空字也在偶數情形內。□

`U=0` 不在物理 admissible 區間；此處沒有對實際生成元的平方根分支作物理代入，也沒有改變 u。它只為整數多項式提供一個非零係數見證。

由 u 超越，命題 2 立即給出

\[
\boxed{|\alpha_w|^2\ne20000
\quad\text{對每一個凍結八字母的有限字 }w.}
\tag{11}
\]

這比「等號發生時另需一個未知的數值流程」更強：對本輪精確對象，等號已被排除。closed guard 仍保持原來的 `<=20000`，沒有改成新的 cutoff；只是在這些真實矩陣值上，`Phi_w(u)<0` 恰表示接納，`Phi_w(u)>0` 恰表示拒絕。

若候選狀態只是任意實數矩陣或小數表，而沒有 (7) 的 exact word／表示綁定，不能直接使用 (10)–(11)。

## 5. 有理比較的終止證明與精度界的精確含義

### 5.1 一個自含、可核查的多項式符號規則

對任意整數多項式 f，先有限檢查全部係數是否為零。若是，回傳精確等號。若不是，超越性給 `f(u)!=0`。

定義有理數

\[
S_N=\sum_{k=0}^{N}\frac{(-1)^k}{10^k k!},
\qquad
I_m=[S_{2m+1},S_{2m}],\qquad m\ge1.
\tag{12}
\]

交錯級數各項的絕對值嚴格下降到零，故這些閉區間均含 u 並嵌套，且在 `[9/10,181/200] subset [0,1]` 內。其寬度及中點為

\[
\eta_m=\frac1{10^{2m+1}(2m+1)!}\longrightarrow0,
\qquad c_m=\frac{S_{2m+1}+S_{2m}}2.
\tag{13}
\]

寫 `f(U)=sum_k f_k U^k`，令 `B_f=sum_(k>=1) k abs(f_k)`，則在 `[0,1]` 有 `abs(f')<=B_f`。若 `B_f=0`，f 是已知非零常數，直接決定符號。否則平均值定理給出

\[
|f(u)-f(c_m)|\le B_f\eta_m/2.
\]

所以以下全為有理運算的測試足以作符號判定：

\[
\boxed{
|f(c_m)|>B_f\eta_m/2
\quad\Longrightarrow\quad
\operatorname{sgn}f(u)=\operatorname{sgn}f(c_m).
}
\tag{14}
\]

從 `m=1` 依次增加 m，必在有限一步通過，因為 `c_m -> u`、`f(u)!=0`、右端誤差趨零。更明確地，`eta_m<abs(f(u))/B_f` 是通過 (14) 的充分條件，但這個含未知間隔的式子本身不是可直接填入的精度預算。實際可核查的是 (14) 的有理數證書。

對 guard 使用 `f=Phi_w` 時，命題 2 已先排除零多項式，故不會在等號上無限細化。這不需要數值近似 y；根式已在 (9) 的模平方中精確消去。Y 的正分支仍是矩陣表示和指定嵌入所必需的條件。

### 5.2 有代數大小界，不冒稱有實用固定精度

對 Gaussian-integer 多項式，把各係數實、虛部絕對值之和再對全部係數求和，記為 `norm_1`。它對乘法次乘性。每個 `H_a` 的每行多項式範數總和不超過 `1+3=4`；乘積矩陣的最大行和範數亦次乘。因此

\[
\deg p_w\le2n,\qquad \|p_w\|_1\le4^n,
\qquad
\boxed{\deg\Phi_w\le4n,\quad
\|\Phi_w\|_1\le16^n+20000\,6^n.}
\tag{15}
\]

這裡 `norm_1(D)=6`。由此也得到 `B_(Phi_w)<=4n(16^n+20000*6^n)`。這些界約束有限代數表達的大小，不是 `abs(Phi_w(u))` 的下界。

「本文沒有指定數值精度上限」並不等於「不存在任何可計算的統一上界」。對給定整數 `d>=0,H>=1`，考慮有限集合

\[
\mathcal F_{d,H}=
\{f\in\mathbb Z[U]\setminus\{0\}:\deg f\le d,\ \|f\|_1\le H\}.
\tag{16}
\]

若在同一 m 對此有限集合中的所有非常數 f 作 (14) 測試，逐次增加 m，則每個測試最終通過，故存在一個共同有限停止步數。集合本身可由有限整數係數列表描述、每步測試皆為精確有理運算，所以此處也給出一個可計算的統一細化步數函數 `M(d,H)`；常數多項式直接處理。

這是存在且可計算的紙面上界構造，不是建議執行巨大的全多項式列表。未枚舉 (16)，未算出任何 `M(d,H)` 數值，沒有給出其可用性或位元複雜度保證。對字長不超過 L 的 guard，可把 (15) 的 `d=4L,H=16^L+20000*6^L` 代入此構造；仍不能據此聲稱固定 110 位或 140 位小數足夠。

## 6. 附帶推論：hyperbolicity 等號與固定幾何 cutoff

### 6.1 `trace^2=4` 必須保留精確等號分支

`SU(1,1)` 形狀在 (3) 的多項式矩陣乘法下保持，因此
`t_w(U)=tr(P_w(U))=p_w(U)+bar(p_w)(U) in Z[U]`。由 (7)，

\[
(\operatorname{tr}M_w)^2
=\frac{t_w(u)^2}{D(u)^n},
\qquad
J_w(U)=t_w(U)^2-4D(U)^n.
\tag{17}
\]

先用係數判零檢查 `J_w`。若 `J_w=0`，則精確 `trace^2=4`；例如空字 I 確實如此，不能讓 interval-only 程序在此等待嚴格分離。若 `J_w!=0`，§5 決定其符號。因分母正，`J_w(u)>0` 恰是 hyperbolicity 判準。

若需要再區分等號中的中心矩陣與非中心情形，(8) 可檢查 `M_w=+I` 或 `-I`。本輪不從局部代數操作推論全群沒有 parabolic 或 elliptic 元素，也不讓非 hyperbolic 字自動進入下文的閉測地 owner。

### 6.2 固定 `21/10` 的平方閾值仍是同一變量的有理函數

只對 `J_w(u)>0` 的矩陣考慮曲率負一的幾何平移長度
`ell(w)=2 arcosh(abs(tr M_w)/2)`；這是[既有長度／中心區分][coverage]中的 translation length，不是字長或中心位移。`arcosh` 取非負實分支。由正性可安全平方比較：

\[
\ell(w)\le\frac{21}{10}
\quad\Longleftrightarrow\quad
(\operatorname{tr}M_w)^2
\le4\cosh^2\!\left(\frac{21}{20}\right)
=u^{-21}+2+u^{21}.
\tag{18}
\]

這只使用同一個 u 的整數冪，沒有引入另一個假定代數獨立的指數常數。清除正分母 `u^21 D(u)^n`，定義

\[
\Psi_w(U)=U^{21}t_w(U)^2
-D(U)^n\bigl(1+2U^{21}+U^{42}\bigr)
\in\mathbb Z[U].
\tag{19}
\]

直接在形式多項式中有

\[
\boxed{\Psi_w(0)=-D(0)^n=(-1)^{n+1}\ne0.}
\tag{20}
\]

故 `Psi_w(u)!=0`。對所有已綁定的 hyperbolic 有限字，得到

\[
\boxed{
\ell(w)\ne21/10,\qquad
\ell(w)\le21/10\iff\Psi_w(u)<0.
}
\tag{21}
\]

§5 的有理符號規則對 `Psi_w` 同樣終止。若要給表達大小界，(15) 的相同論證給
`deg(Psi_w)<=4n+42`、`norm_1(Psi_w)<=4*16^n+4*6^n`，亦可接到 (16) 的理論細化步數構造。

`M_w -> -M_w` 不改 `abs(alpha_w)^2` 或 `trace^2`，所以 §4、§6 的判定都與 `PSU` lift 符號相容。closed cutoff 不更改；但除非先證明 hyperbolicity，不能只憑 `Psi_w<0` 就認定該字是一條短閉測地軌道。

## 7. 對有限全邊證書真正新增了什麼

| 先前需要的語義責任 | 本輪給出的有限字判定 | 仍不可由此宣稱 |
| --- | --- | --- |
| incoming word／state 是哪個實際群元素 | 指定嵌入、有限 E 算術與 (8) 的整體 ± 身份 | 舊 state codec、abstract-surface faithfulness 或 hash 相等已驗證 |
| outgoing edge 是否在 `abs(alpha)^2<=20000` | (10) 排除等號；(14) 有理符號證書有限終止 | 固定十進位精度安全、舊 18533 狀態／深度 11 已重播 |
| 是否 hyperbolic 且在固定幾何 cutoff 內 | `J_w` 精確零／符號及 (20)–(21) | 已完成本原性、完整群共軛、inverse pairing 或 owner 商 |
| 所列有限 component 是否完整 | 可為[上輪][inradius]每條邊的身份／guard 證明提供終止判定來源 | 已生成全邊列表、FIFO transcript、規範排序流或 observed digest |

在正確 exact binding、完整字母表以及前輪真正有限中心域的幾何前提下，這些判定原理可支撐一個會終止的語義遍歷：每個有限乘積與判斷終止，相異域內元素數有限，每個元素只擴展一次。但本輪沒有建立或運行該程序，也沒有把此條件性推論寫成新的正式回執。

從中心 component 覆蓋短類仍要用[軸到中心筆記][coverage]的真基本域與完整側／頂點 incidence；本輪的代數身份定理不補這些幾何證書。本原性、完整群共軛、外部逆元 owner、排序與 canonical encoding、合同版本和獨立 replay 也仍分別需要實作及證據。

[BP 合同][bp-contract]仍維持 separately passage-adequate strict-systole gate 後的 conditional empty stream。本輪只證控制組八字母上的局部／有限字代數結論，沒有將它移植到 Bolza、替換 BP 路線、填寫 null version／observed digest 或改變 `execution_performed=false`。

## 8. 本輪方法、來源與實際動作

使用 ARS academic-paper 的 bounded argument-builder，將外部超越性前提、函數域單射、具體有限字、可核查比較與生產認證分開。已完整讀取當輪 `AGENTS.md`、`docs/workflow.md`、定位出的 ARS 0.1.28 router、academic-paper workflow 與 argument-builder role；本輪不是 full pipeline、正式 reviewer、Route review 或稿件修訂。

只讀凍結控制矩陣的 exact `definition`、兩份 producer 合同，以及前輪內切球／closure 與覆蓋筆記的相關責任。外部只作普通一手瀏覽，核對 [Waldschmidt 作者章節 §1.1、Theorems 1、4][HL] 的 Hermite 與 Hermite–Lindemann 敘述；新域與清分母推論由本文自己給出。沒有重試舊 DOI／截圖失敗、下載或替換 locked source、bibliographic API、外部模型或資料上傳。

公式展開、`U=0` 的奇偶分類、determinant、平方閾值及終止性均為紙面推導。沒有執行符號代數、矩陣數值程序、有限字／多項式枚舉、科學實驗、producer、fixture 或正式 checker。唯一文件寫入使用 `apply_patch`；來源讀取與 SHA／文本檢查不構成群論或科學認證。

寫後保全確認四份前輪筆記、現稿、兩份合同與三份凍結輸入共十個舊檔的 SHA-256 與寫前一致。只讀 `node -e` 文本檢查通過六個引用定義、十處實際引用使用、全部本地引用目標、22 對顯示數學分隔符、連續 (1)–(21) 標籤及控制字元／行末空白／衝突標記／末尾換行檢查。最初的粗略引用 regex 曾將 `Z[i][U]` 誤認為引用，修正檢查範圍時另有一次 shell 引號語法失敗；限定到非程式／非公式正文並修正調用引號後通過，沒有以改寫數學內容消除誤報。未重試已知不可用的 Git repository 檢查。

[control-input]: /root/autodl-tmp/flow_systems/papers/28-bolza-magnetic-flow/results/round7_nonarithmetic_control_matrices.json
[cp-contract]: /root/autodl-tmp/flow_systems/papers/33-bolza-control-matched-census/notes/stage4_prime_round5_support/cp_enumeration_contract.json
[bp-contract]: /root/autodl-tmp/flow_systems/papers/33-bolza-control-matched-census/notes/stage4_prime_round5_support/bp_enumeration_contract.json
[inradius]: /root/autodl-tmp/flow_systems/papers/33-bolza-control-matched-census/notes/internal_inradius_separation_and_explicit_guard_capacity_20260909.md
[coverage]: /root/autodl-tmp/flow_systems/papers/33-bolza-control-matched-census/notes/internal_axis_to_center_coverage_and_finite_guards_20260908.md
[HL]: https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/SurveyTrdceEllipt2006.pdf
