# P31：ambient 約化詞、循环共軛與有限正負證書

日期：2026-09-08。狀態：**內部有界數學增量；沒有 frozen-input 執行，非正式稿、非回執、非 Route 變更。**

## 0. 本輪閉合的橋與不涉及的部分

承接 [十二狀態子群共軛下降](internal_finite_coset_conjugacy_reduction_20260908.md)。該筆記在已有 ambient 共軛判定與 exact witness 後，將 \(\Gamma_0(11)\) 共軛化為至多 12 個射影狀態。本輪補上其明列未完成的 **ambient 數學決策橋**：

> 对 exact、正跡 hyperbolic \(P,Q\in\mathrm{SL}_2(\mathbb Z)\)，可經有限整數步驟得到唯一 reduced syllable words，再循環約化。兩個 projective 元素共軛，當且僅當兩個循環核心是 syllable rotation。命中可以重建 exact 共軛矩陣；完整的有限 rotation 比較無命中則證明 ambient 非共軛。

本筆記自含證明 \(\mathrm{PSL}_2(\mathbb Z)\simeq C_2*C_3\) 所需的生成性與 normal-form 唯一性，不將「矩陣可寫成生成元」誤當唯一性。再直接證明 hyperbolic 適用的循环共軛判準，並接回既有 ambient root 與 finite-coset 定理。

結論是**對 admissible exact 矩陣的一個終止數學程序及其證書充分性／完備性**。不是已實作的 verifier，也沒有綁定 frozen words、產生實際 owner bytes、解決 138 筆輸入、執行 9453 pairs，或變更 total `delta`／resolved-domain `kappa` 契約。此前筆記中的歷史 missing 項不被覆寫；本筆記只記錄這一輪新增的理論解答。

使用 ARS academic-paper 的 argument-builder 角色組織命題、證明與限制；沒有啟動正式研究／論文 pipeline。生成元與 normal form 的背景以 Keith Conrad 作者數學講義作普通公開來源核對，實際邏輯由下文逐項證明。[Conrad，*SL(2,Z)*，Theorem 1.1 與 Appendix C](https://kconrad.math.uconn.edu/blurbs/grouptheory/SL(2,Z).pdf)

## 1. 群、固定 lifts 與 syllable 字母表

設

\[
\widetilde G=\mathrm{SL}_2(\mathbb Z),\qquad
G=\widetilde G/\{\pm I\},\qquad
S=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\quad
T=\begin{pmatrix}1&1\\0&1\end{pmatrix},\quad
U=ST=\begin{pmatrix}0&-1\\1&1\end{pmatrix}.
\tag{1}
\]

令 \(\sigma=[S]\)、\(u=[U]\)。精確矩陣關係是

\[
S^2=-I,\qquad U^3=-I,\qquad
\sigma^2=1,\quad u^3=1,\quad [T]=\sigma u.
\tag{2}
\]

用 U 而不用 R 表示 order-three lift，避免與前筆記的 ambient primitive root R 混淆。兩個有限因子及非單位 syllables 為

\[
A=\{1,\sigma\},\qquad B=\{1,u,u^2\},
\qquad\mathcal A=\{\sigma,u,u^2\}.
\tag{3}
\]

一個 **reduced word** 是相鄰 syllables 來自不同因子的有限序列；空詞表示單位。遇到同因子相鄰項時，用 \(\sigma\sigma=1\) 或 \(u^i u^j=u^{i+j\bmod3}\) 合併，並刪除 exponent 0。每次使長度嚴格下降，所以 stack reduction 終止。這先給出合法 reduction 操作，尚未假定所得 normal form 唯一。

word 的矩陣 evaluation 固定使用 lifts S、U、\(U^2\)，由左至右相乘。此 evaluation 的 **projective** 值尊重 (2)，但精確矩陣值在合併後可能差 \(-I\)。後文的矩陣 replay 不得忽略該符號。

## 2. 矩陣到詞：帶終止界的歐幾里得證明

**引理 1（有限生成元分解）。** 任意 \(M\in\widetilde G\) 均可由有限整數 row operations 得到 S、T 的詞和一個 central sign，且有逐步 exact matrix replay。

**證明。** 寫當前矩陣為

\[
M_i=\begin{pmatrix}a_i&b_i\\c_i&d_i\end{pmatrix}.
\]

若 \(c_i\ne0\)，取唯一的 \(0\le r_i<|c_i|\) 滿足 \(r_i\equiv a_i\pmod {|c_i|}\)，並令

\[
q_i=\frac{a_i-r_i}{c_i}\in\mathbb Z,
\qquad L_i=ST^{-q_i},
\qquad
M_{i+1}=L_iM_i
=\begin{pmatrix}-c_i&-d_i\\r_i&b_i-q_i d_i\end{pmatrix}.
\tag{4}
\]

即使 \(c_i<0\)，q 的定義仍是整數。新的 lower-left 絕對值嚴格小於 \(|c_i|\)，所以過程有限停止。若停止於 \(c_m=0\)，determinant 1 強迫兩個對角 entry 同為 \(\varepsilon\in\{1,-1\}\)，因此

\[
M_m=\varepsilon T^{e},\qquad e=\varepsilon b_m.
\]

回代得到精確等式

\[
M=\varepsilon L_0^{-1}L_1^{-1}\cdots L_{m-1}^{-1}T^e,
\qquad L_i^{-1}=T^{q_i}S^{-1}.
\tag{5}
\]

各步的 q、r、矩陣與終端值均為有限整數記錄；m=0 時 product 為 I。□

將 (5) projectivize，用

\[
[S^{-1}]=\sigma,\qquad [T]=\sigma u,
\qquad [T^{-1}]=u^2\sigma
\tag{6}
\]

展開有符號整數冪，再執行 §1 reduction，得到某個 reduced word。因所有整數有限，此程序终止；这里不聲稱 polynomial complexity 或實務效率。

所以 S、T 生成 G，且 \(\sigma,u\) 亦生成 G。但這一步**沒有排除額外關係**；唯一性需下一節的独立論證。

### 2.1 精確 lift replay 的最低要求

若 reduced word 為 w，應保留或重建 \(\eta\in\{\pm1\}\)，驗證

\[
M=\eta\,\operatorname{Eval}(w).
\tag{7}
\]

例如 exact \(T=-SU\)、\(T^{-1}=-U^2S\)、\(S^{-1}=-S\)，而 syllable 合併也可引入負號。可以逐步追蹤 central sign，或以 exact multiplication 在末端確認 (7)；不能從 projective substitution 推出同號矩陣等式。

後面對 P、Q 使用唯一正跡 hyperbolic lifts，但中間 normal-form evaluation 和共軛子自身不必正跡，亦不必 hyperbolic。特别是零跡的 S 是合法共軛子。

## 3. 不存在非空 reduced identity：normal form 唯一性

稱 reduced word **cyclically reduced**，若其長度至多 1，或首、尾 syllables 來自不同因子。

**引理 2（非空循環核心）。** 任意非空 reduced word w，均可有限地共軛為非空 cyclically reduced word a，且可追蹤詞 C 使 \(w=C a C^{-1}\) 在 G 中成立。

**證明。** 若首尾同因子且長度大於 1，長度必為奇數且至少 3。寫 \(w=a_1\cdots a_n\)，以 \(a_1^{-1}\) 共軛得到

\[
a_1^{-1}wa_1=a_2\cdots a_n a_1.
\tag{8}
\]

合併末尾同因子的 \(a_n a_1\)：乘積為 1 時減少兩個 syllables，否則減少一個，所得仍 reduced。前者最短留下長度 1，後者最短留下長度 2，均不為空。每次嚴格減長，終必停止。若已記錄原詞 \(w=C\,w_{\rm current}\,C^{-1}\)，本步更新 \(C\leftarrow C a_1\)，即可維持共軛等式。□

**引理 3（無非空 reduced 關係）。** 非空 reduced word 不會在 G 中表示單位。

**證明。** 由引理 2，可改看非空 cyclically reduced 核心。長度 1 時為 \(\sigma,u,u^2\)，其矩陣 lifts S、U、\(U^2\) 均不是 \(\pm I\)，所以非單位。

若核心長度至少 2，兩因子交替及首尾不同強迫長度為偶數。必要時循環移動一個首 syllable，可使它寫成

\[
(\sigma u^{e_1})(\sigma u^{e_2})\cdots(\sigma u^{e_r}),
\qquad e_j\in\{1,2\},\quad r\ge1.
\tag{9}
\]

循環移動是共軛，不影響是否表示單位。令

\[
V=\begin{pmatrix}1&0\\1&1\end{pmatrix}.
\]

直接乘法給出

\[
SU=-T,\qquad SU^2=-V.
\tag{10}
\]

所以 (9) 的 exact evaluation 是 \((-1)^r\) 乘上一個非空 T、V 乘積。T、V entrywise 非負且均 entrywise 大於或等於 I。其乘積因而 entrywise 大於或等於首因子，至少有一個正的 off-diagonal entry，故不可能為 I 或 \(-I\)。projective 核心亦非單位。□

**定理 4（唯一 reduced normal form）。** 每個 G 元素恰有一個 §1 意義下的 reduced word；尤其 \(G\simeq C_2*C_3\)。

**證明。** 存在性由引理 1 與 reduction 得到。若兩個 reduced words w、v 不同，考察 \(w^{-1}v\)：先消去 w、v 的共同初始 syllables。若其中一詞已盡，另一詞留下非空 reduced 尾部；否則第一對不相等項來自不同因子時無法合併，來自同因子時合併為非單位 syllable，且其外側相鄰项均屬另一因子，無法再跨過它消去。因此 \(w^{-1}v\) 約化後非空。引理 3 排除其表示單位，故 w、v 代表不同 G 元素。

只有 (2) 的因子內關係，沒有非空 reduced 關係，故生成元映射給出所述 free-product 同構。亦因此任何合法 reduction 路徑都得到相同 normal form；不是因為某個 stack 實作任意選擇而「定義唯一」。□

上面的非負矩陣證明與 Conrad Appendix C 的 standard normal-form 論證相關；此處完整列出非空核心、長度 1、sign 與 uniqueness 各步，避免以外部定理名稱代替必要語義橋。這是標準群論工具的本案證書化推導，不宣稱該群分解或 normal-form 定理的新穎性。[Conrad，Appendix C，Theorem C.1](https://kconrad.math.uconn.edu/blurbs/grouptheory/SL(2,Z).pdf)

## 4. Hyperbolic 的有限循環共軛判準

**定理 5。** 若 a、b 是 cyclically reduced words，且兩者 syllable 長度至少 2，則

\[
a\sim_G b
\iff b\text{ 是 a 的某個 cyclic syllable rotation}.
\tag{11}
\]

因而共軛時兩詞長度相等。此處 rotation 不含反轉或逐 syllable 取逆。

**充分性與 witness 方向。** 若 \(a=AB\)、\(b=BA\)，A 是任意可能為空的首段，則

\[
A^{-1}aA=BA=b.
\tag{12}
\]

所以把 a 共軛至 b 的共軛子是 **\(A^{-1}\)**，不是 A。

**必要性。** 取 reduced 共軛詞 h 滿足 \(b=hah^{-1}\)，對其長度歸納。h 為空則 b=a，由唯一性完成。若 \(h=h'z\)，其中 z 為末 syllable，寫 \(a=a_1\cdots a_n\)。a 首尾屬不同因子，所以 z 恰與 \(a_1,a_n\) 中一個同因子。

若 z 與 \(a_1\) 同因子而 \(za_1\ne1\)，則

\[
h'\,(za_1)\,a_2\cdots a_n\,z^{-1}\,(h')^{-1}
\tag{13}
\]

已是 reduced word：h′ 的末因子（若存在）與 z 不同，\(a_2\) 與 z 不同，\(a_n\) 亦與 z 不同。可是 (13) 的首尾屬同因子，不是 cyclically reduced；不論 h′ 是否為空皆如此。由 normal-form 唯一性，它不可能等於 cyclically reduced 的 b。因此必須 \(z=a_1^{-1}\)，此時

\[
zaz^{-1}=a_2\cdots a_n a_1
\tag{14}
\]

是一個 left rotation，仍 cyclically reduced。

若 z 與 \(a_n\) 同因子，同理，假使 \(a_nz^{-1}\ne1\)，則

\[
h'\,z\,a_1\cdots a_{n-1}\,(a_nz^{-1})\,(h')^{-1}
\tag{15}
\]

是首尾同因子的 reduced word，產生相同矛盾。故 \(z=a_n\)，而

\[
zaz^{-1}=a_n a_1\cdots a_{n-1}
\tag{16}
\]

是 right rotation。兩種情形都可移除 h 的最後一個 syllable，再對長度小一的 h′ 歸納。有限次 left/right rotations 的合成仍是 cyclic rotation，故得必要性。□

### 4.1 Hyperbolic 為何排除短核心，以及逆向為何另處理

P 的 cyclic core 若為空，則 P projectively 為單位；若長度 1，則其 projective order 為 2 或 3。正跡 hyperbolic 矩陣有一個大於 1 的實特徵值，不可能有限階。因此 admissible hyperbolic P、Q 的核心長度至少 2，完全落在定理 5 範圍，無須使用 length-one 的 factor-conjugacy 特例。

反方向不能誤用：長度至少 2 **不保證 hyperbolic**，例如 \(\sigma u=[T]\) 是 parabolic。輸入的 determinant、integrality 和 \(\operatorname{tr}P>2\) 仍須 exact 檢查。

若要比較 P 與 \(Q^{-1}\)，應將 exact inverse 另作輸入並重新運行數學判準。不能在 (11) 中默認把 inverse、reverse 或未帶證明的 orientation identification 加入 rotation equivalence。特別是 ambient 自逆與 subgroup 自逆不同；前筆記的 level-11 例已展示這個差別。

## 5. 從詞命中重建 exact 矩陣共軛子

對 exact 正跡 hyperbolic P、Q，使用 §§2–3 的分解與循環 reduction，記錄

\[
[P]=C_P a C_P^{-1},\qquad
[Q]=C_Q b C_Q^{-1},
\tag{17}
\]

其中 C 也是 G 中的詞，a、b 是唯一 normal forms 經明確有限循環步驟所得的核心。核心可以因循環 reduction 的起點選擇而不同，但定理 5 的 rotation 判定與 verdict 不受影響。

若比較到 \(a=AB\)、\(b=BA\)，則 projective 共軛子為

\[
H_0=C_Q A^{-1}C_P^{-1},\qquad
H_0[P]H_0^{-1}=[Q].
\tag{18}
\]

使用固定 lifts 評估 (18)，得到 determinant-one 整數矩陣，仍記為 \(H_0\)。projective 等式暫時只給

\[
H_0PH_0^{-1}=\pm Q.
\]

共軛保跡，而 P、Q 都有正跡，負號不可能。因此必有精確矩陣等式

\[
\boxed{H_0PH_0^{-1}=Q.}
\tag{19}
\]

證書應再用 exact multiplication replay (19)，不是只引述正跡論證或保存詞相等 hash。若 P、Q 的 trace 不同，直接是 ambient negative branch；不能為了強行取得命中而更換某個 lift 或省略某個 traversal power。

### 5.1 一個純手算方向檢查

取

\[
P_*=TV=\begin{pmatrix}2&1\\1&1\end{pmatrix},
\qquad Q_*=VT=\begin{pmatrix}1&1\\1&2\end{pmatrix}.
\tag{20}
\]

兩者 determinant 1、trace 3。其 projective cyclic words 為

\[
a=(\sigma u)(\sigma u^2),\qquad
b=(\sigma u^2)(\sigma u).
\]

取 \(A=\sigma u=[T]\)，(12) 給出共軛子 \([T^{-1}]\)，且手算

\[
T^{-1}P_*T=\begin{pmatrix}1&1\\1&2\end{pmatrix}=Q_*.
\tag{21}
\]

這只是 prefix inverse 方向與 lift 的局部紙面檢查；P_*、Q_* 不在本案 level-11 subgroup，此處也沒有把它當 subgroup fixture、frozen row 或實驗輸出。

## 6. Finite certificates 的數學內容

對每一對 admissible exact matrices，以下資料構成可有限重播的 prospective certificate；這是數學需求，不是已發布 schema 或實作。

1. **Input 與語義。** exact P、Q、determinant／trace 檢查、projective quotient 與正跡 lift 約定、(1) 的生成元版本，以及輸入綁定。若有 frozen word，word-to-matrix binding 必須另證，不能由本文替代。
2. **Matrix-to-word。** (4)–(5) 的有限整數 transcript、(7) 的 central sign replay、各 reduced words 的 alternating-factor 檢查。
3. **Cyclic reduction。** 每個 (8) 的有限步驟、C_P／C_Q 的共軛方向與 (17)、兩核心的 cyclically reduced 檢查和長度。
4. **Ambient positive。** 命中的 rotation index 與首段 A，(18) 的矩陣重建，以及 exact (19)。這個矩陣等式本身足以驗證 ambient positive，不必信任 producer 的 normal-form 正確性來接受正 witness。
5. **Ambient negative。** 若核心長度不同，記錄此不等；若同為 n，對全部 \(j=0,\ldots,n-1\) 的 rotations 記錄 exact syllable 不相等。重複 rotations 可以保留，不會傷害窮盡性。此有限排除配合定理 4、5 才給出真正的 negative certificate。

Negative branch 不是「沒有找到短共軛子」或 solver timeout；它排除了定理 5 證明足夠的所有 n 個 candidates。若某個 transcript、binding 或 theorem version 尚未驗證，pipeline 層仍應保留 typed unresolved，不可把數學上存在一個終止程序誤稱為實際已 resolved。

## 7. 接回 \(\Gamma_0(11)\) 的十二狀態下降

現在再設 \(P,Q\in\widetilde\Gamma_0(11)\)。使用本輪 ambient 判定：

- 若 ambient negative 已確證，立即得到 subgroup negative，因任何 subgroup 共軛子也是 ambient 共軛子。
- 若得 exact (19)，沿用前筆記有限 trace/root recurrence，求得並確證 **ambient** positive primitive root R 與 \(P=R^e\)。所有 ambient 共軛子恰為 \(\pm H_0R^n\)，\(n\in\mathbb Z\)。
- 在 \(\mathbb P^1(\mathbb F_{11})\) 中計算 \(v_0=\infty\)、\(v_{j+1}=\overline Rv_j\)、\(y=\overline{H_0}^{-1}\infty\)。其完整閉合 cycle 長度 \(h\le12\)。命中 \(y=v_j\) 給 exact subgroup 共軛子 \(H_0R^j\)；完整 cycle 無命中給 subgroup negative。

等價地，對本文的 exact admissible inputs，前筆記的定理與本輪 normal-form 橋合成為

\[
\boxed{
P\sim_{\Gamma_0(11)}Q
\iff
\bigl[\text{cyclic cores 有 rotation 命中}\bigr]
\quad\text{且}\quad
\bigl[\overline{H_0}^{-1}\infty
\in\langle\overline R\rangle\infty\bigr].
}
\tag{22}
\]

第二個 predicate 僅在第一個命中並由 (18) 選出 H₀ 後評估。更換有效 ambient witness 不影響判定，因所有 choices 差右乘中心化子的 R 冪；不能任意把右乘改成左乘。

此程序每一段均在數學上終止：Euclidean remainder 嚴格下降；word reduction 和 cyclic reduction 嚴格減長；rotation enumeration 長度有限；ambient root 的整數 trace 候選有前筆記所證有限上界；最後 projective orbit 至多 12 states。**12 只限制最後一段，不限制 normal-word 長度、root 候選數或總計算成本。**

若任務是 primitive-owner 等价而不是原矩陣共軛，須先以既定 **subgroup** primitive-root／traversal 契約產生待比較的 P、Q，再使用 (22)。原矩陣的冪數不能因 primitive-flow 語義而在 ambient 比較中悄悄刪除。ambient root R 僅用於完整中心化子與 finite-coset 下降，不能與 subgroup owner 根混同。

## 8. 對 finite partition 的增量，以及仍未閉合的接口

本輪對 [Attach + Separate 與 G/I/C 筆記](internal_certified_partition_and_gic_descent_20260908.md) 的增量是：對一對 exact admissible representative matrices，已有完全有限的數學正／負共軛判定來源，包含先前缺少的 ambient nonconjugacy branch。它不再以未指明的 ambient solver 為純假設。

仍然沒有完成以下工作：

- frozen IDs／words 到 exact matrices 的版本化 replay、實際 subgroup-root 與 traversal certificates；
- 上述 transcript 的正式 schema、獨立 verifier 實作與測試、全體 frozen population 的 coverage；
- 所有 pair 的實際 Attach／Separate audit 與 inverse-owner links；
- canonical owner serialization、跨人口穩定的 bytes、既有 contract 的 implementation choice；
- total `delta`、resolved `kappa` 或 G/I/C 的任何實際計算與科學回執。

唯一 reduced word 是 **G 元素**的 normal form，不是直接得到 subgroup conjugacy class 的 canonical bytes。對 cyclic core 取最小 rotation 等可成為後續設計的數學材料，但本輪不固定字母序、序列化格式、subgroup class splitting 標籤或簽發 owner bytes。已 proved 的 pairwise criterion 和已執行的 canonicalization 必須分開報告。

## 9. 來源、實際核對與保全

當輪已完整讀取 `AGENTS.md`、`docs/workflow.md`、所用 ARS router、academic-paper workflow 與 argument-builder 指令；相關前筆記只讀。普通公開 browse 核對 Conrad 作者講義 Theorem 1.1 的 Euclidean generation 與 Appendix C Theorem C.1 的 \(C_2*C_3\) normal form。來源用於標準背景及證明架構交叉核對，不證明 P31 data binding、完整 owner ledger 或本筆記的新穎性。

來源限定：主線讀取 Appendix C Theorem C.1 的 PDF 文本提取時，n=1 段出現「\(i,j\equiv0\) 時 \(y^i x y^j=1\)」的不一致句；此時該詞應為 \(x\ne1\)。這裡只記錄提取段落的問題，不斷言作者原版有誤，也不另作截圖或重新獲取。本文 §3 自含的 length-one 排除直接檢查 S、U、\(U^2\) 均非 \(\pm I\)，不依賴該句；一般生成性與 normal-form 背景引用保留。

局部數學檢查是上文的自含紙面推導：signed c 的餘數下降；(5) 的逆矩陣次序；非空 cyclic core 與長度 1 基例；(10) 的 central signs 與非負積；normal form 的消去論證；共軛詞末 syllable 的兩種情形；(12)、(18) 的 prefix inverse 方向；正跡排除負號；例 (20)–(21)；以及 (22) 對先前 right-coset target 和 ambient root 的正確接合。沒有運行矩陣／owner 科學程式或實驗。

唯一 filesystem 寫入為 `apply_patch` 新增本筆記。讀取時，前 finite-coset 筆記 SHA-256 為 `a5b6344017fb6d04ea999ff1ba311eed87e20ba13a2f455c2930e9d696c3ffd1`，certified-partition 筆記為 `4462f9f6bf88bf5de0aa4cc27da3ba7210911e812f3387adaf9a5abb324dd946`，round6 原文為 `4bc1a960b5527a5d389b5c70e29fa0dc7b3199b93a808dd3f347616dd686d1a3`。這些 hashes 只作来源身分／未修改檢查，不是科學真實性或既有鎖定回執的替代品。

舊筆記、正式稿、code、locked inputs、experiments/results 與歷史 receipts 均保持只讀。没有外部 API、資料上傳、受限通道繞行、正式編譯或 Route 狀態變更；沒有宣稱 formal proof checker 接受或實際 executable certificate pipeline 已完成。
