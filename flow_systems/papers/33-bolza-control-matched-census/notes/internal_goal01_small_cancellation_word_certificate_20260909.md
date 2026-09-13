# P33 有界理論：小消去詞問題證書與有限 owner 見證接口

日期：2026-09-09 UTC。這份筆記只新增紙面證書及條件明確的有限搜索規範；不實作或執行 Dehn 算法、automaton、枚舉、producer、checker 或實驗，不修改凍結輸入、合同、現稿、canonical bytes、回執及 Route／Stage 狀態。ARS Phase 3 的證據邊界在此是「理論 oracle」與「已實作並獨立驗證的 checker」分開。

## 1. 固定字母與實際矩陣作用的橋接

按 [CP 合同][contract]，固定有序字母表

\[
\mathcal A=(a,b,c,d,A,B,C,D)
=(g_0,g_1,g_2,g_3,g_0^{-1},g_1^{-1},g_2^{-1},g_3^{-1}).
\]

大寫只表示相應小寫的逆元，不是新生成元。[凍結矩陣 definition][input] 的關係字逐字是

\[
R=aBcDAbCd,
\qquad R^{-1}=DcBadCbA.
\tag{1}
\]

這裡使用矩陣按書寫次序相乘的慣例。Poincaré 八邊形審查中的 side-transformation cycle 乘積是 R；逐點套用坐標變換得到的是 R 的逆元，不能因此擅自重新排序 (1)。

本筆記的實際群接口需要先行幾何結論

\[
\rho:\langle a,b,c,d\mid R\rangle
\overset{\cong}{\longrightarrow}\Gamma\subset\operatorname{PSU}(1,1),
\tag{2}
\]

其中 rho 把每個字母送到同一份 exact definition 的 Möbius 作用。(2) 是實際凸八邊形、端點反向配對及半平面換側、全部有向頂點環角和與 Poincaré 定理給出的忠實表示結論；它不是由十進位 relator residual 得出。若尚未把該紙面幾何證明綁定到具體輸入版本，下文對抽象 presentation 的詞問題結論仍成立，但不能自行聲稱已完成實際矩陣／producer 的版本認證。

## 2. 全部十六個有向二字前綴：有限小消去證書

令 \(\mathcal R\) 是 R 與 R 的逆元的全部循環移位，共十六個長度八的字。以下逐一列出其二字前綴；每列按循環移位的首字母分組。

| 首字母 | R 的相應循環移位前綴 | R 的逆元的相應循環移位前綴 |
| --- | --- | --- |
| a | aB | ad |
| b | bC | bA |
| c | cD | cB |
| d | da | dC |
| A | Ab | AD |
| B | Bc | Ba |
| C | Cd | Cb |
| D | DA | Dc |

不同列的首字母不同，同列的第二字母不同，所以十六個二字前綴互異。因而兩個不同的 symmetrized relators 不可能有長度至少二的公共前綴；每個單字母又同時出現在兩欄的對應首位，所以所有非空 piece 都恰有長度一。

兩個字在 (1) 中都自由且循環約化，並且每個有向字母只出現一次。故任何循環移位都不是自由群中的 proper power：若字面等於一個循環約化字的 m 次冪，m 大於一，所有字母的出現次數都必為 m 的倍數，矛盾。

由此得到

\[
|p|/|r|=1/8<1/6,
\qquad C'(1/6),\qquad C(8)\text{--}P\Longrightarrow C(6)\text{--}P.
\tag{3}
\]

這是原有四生成元 presentation 自身的證書，沒有改用另一組標準 commutator 生成元。piece 與 P 的精確定義可見 Kapovich 作者論文 §1：P 要求 pieces 長一且 relators 不是 proper powers；不能只檢查正向 R 而漏掉逆元循環移位。[K]

## 3. 只用十六個五字規則的 Dehn 詞問題規範

對每個 \(r=e_0e_1\cdots e_7\in\mathcal R\)，設一條規則

\[
e_0e_1e_2e_3e_4
\longrightarrow e_7^{-1}e_6^{-1}e_5^{-1}.
\tag{4}
\]

共有十六條規則，左側互異；再加八條相鄰逆元消去規則 \(zz^{-1}\longrightarrow\varnothing\)，z 遍歷字母表。這就是完整有限規則集，不必再加入六、七、八字長的規則。

一個完全確定的紙面策略是：從左至右找最先能改寫的位置；同位置先做自由消去，再做 (4)；改寫後重新由左端掃描，沒有規則可用時停止。每步保留群元素並使長度減二，因此最多原長度的一半次改寫。這是改寫次數界，不是本筆記對任何程式的牆鐘、記憶體或線性時間保證。

外部定理只在這一步使用：C'(1/6) presentation 的非空自由約化 identity word 含有超過半個 relator，因此 Dehn 消去可決定詞問題。Touikan 作者講義 §3.5、Corollary 3.5.8、Theorem 3.5.11 給出這個敘述及 disc／singular-disc 論證。[T] 本例 relator 長度八，超過半個至少長五，故只保留其首五字規則 (4) 已足夠。

令 red 為上述確定策略的終態，便有

\[
\operatorname{red}(w)=\varnothing
\quad\Longleftrightarrow\quad w=1\text{ in }\langle a,b,c,d\mid R\rangle.
\tag{5}
\]

在 (2) 與字到 exact matrix 的綁定成立時，

\[
\rho(u)=\rho(v)
\quad\Longleftrightarrow\quad
\operatorname{red}(uv^{-1})=\varnothing.
\tag{6}
\]

這比較的是 PSU 元素，已容許 SU lift 的整體正負號；沒有以每個矩陣 entry 各自選符號。超越參數不影響此有限字算法，因為輸入是符號字和忠實表示，不是要求算法自行從十進位矩陣還原字。[精確身份筆記][identity] 中的函數域算術仍可獨立支援 word／state 綁定。

### 不可把終態冒稱 canonical normal form

由 R=1，兩個不同字

\[
aBcD=DcBa
\tag{7}
\]

表示同一元素。但兩者都自由約化、長四、沒有 (4) 的左側，故 red 分別保持它們不變。即使固定了確定改寫策略，終態也不是群元素的唯一編碼。

所以必須把 u 與 v 的逆字串接，再檢查 \(\operatorname{red}(uv^{-1})\) 是否為空，而不是比較 red(u) 與 red(v) 的字面相等。此例同時排除「Dehn 終態就是合同 canonical state」的錯誤接口。本筆記也沒有把 cyclically Dehn-reduced 當作最短共軛代表。

## 4. 最小可證 bridge：有限規則語言縮減見證全集

令 \(\mathcal L_D\) 是不含八種相鄰逆元及十六種 (4) 左側的所有有限字，含空字。這是有限禁子字語言；記住最後至多四個字母即可判定下一字是否造成禁子字。因此它是正規語言，可用至多

\[
1+8+8^2+8^3+8^4+1=4682
\tag{8}
\]

個未最小化狀態表達，最後一項為拒絕狀態。此處只描述有限 automaton 的存在性結構，未建立任何 automaton 檔案。

**有界代表引理。** 若某群元素有長度不超過 L 的字代表，則它有 \(\mathcal L_D\) 中長度不超過 L 的代表。

**證明。** 對原代表作有限 Dehn 消去；群元素不變、長度不增加，終態屬於 \(\mathcal L_D\)。

因此給定一個已另外證明、適用於同一字母表、在所需 s 可確定有限整數值的幾何到詞長界 W，滿足

\[
d(o,zo)\le s\Longrightarrow
\exists w\in\mathcal A^*:\rho(w)=z,\ |w|\le W(s),
\tag{9}
\]

便可把所有有限字候選縮到

\[
\mathcal W_s=\{w\in\mathcal L_D:|w|\le W(s)\}.
\tag{10}
\]

每個幾何球內元素至少有一個代表在 (10)；它不是無重複列表，也不聲稱是 geodesic／automatic canonical language。本引理不推導或替換 W：全域 packing 版本或更好的管狀鄰域版本，均須由另一個實際證明提供。舊 depth 11 不是 (9) 的證明。

## 5. 與嚴格 cutoff、根及共軛見證界的接口

這一節明列幾何輸入，避免把詞問題算法當作幾何界的來源。設同一真曲面上所有非恒等元素皆 hyperbolic 且 \(\ell(z)\ge\sigma>1/12\)，並固定

\[
\Lambda=21/10,\quad
T=2\operatorname{arcosh}\sqrt{20000},\quad
Q=\operatorname{arcosh}\frac{\sinh(T/2)}{\sinh(\sigma/2)},\quad
B_{\rm conj}=2Q+\Lambda/2.
\tag{11}
\]

目前幾何候選取 \(\sigma=2\operatorname{arsinh}(\sinh(1/2)/\cosh 3)\)；其全群下界及嚴格有理估計需使用已證的基本域、中心分離與覆蓋半徑，不由 (3) 或 (5) 推出。本節以這些幾何輸入成立為前提。

令輸入 g、h 具有 exact word 綁定，並已確認
\(d(o,go),d(o,ho)\le T\) 及 \(0<\ell(g),\ell(h)<\Lambda\)。closed cutoff 本身不被修改；[精確身份筆記 §6.2][identity] 的等號排除是使用此嚴格寫法所需的另外來源。

### 根

若 \(z^m=g\)、整數 m 至少二，則 z 與 g 同軸，\(\ell(z)=\ell(g)/m\)。同軸公式
\(\sinh(d(o,zo)/2)=\sinh(\ell(z)/2)\cosh d(o,\operatorname{Axis}(z))\)
給出 \(d(o,zo)\le d(o,go)\le T\)。又
\(m/12<m\sigma\le\ell(g)<21/10\)，故 \(m\le25\)。

於是有限紙面規範為：對 \(m=2,\ldots,25\) 及全部 \(v\in\mathcal W_T\)，測試

\[
\operatorname{red}(v^m w_g^{-1})=\varnothing.
\tag{12}
\]

存在陽性等價於 g 有 proper root；若全集均陰性則本原。對 g 的任何共軛元素存在根，也等價於 g 自己存在根，因此這沒有把本原性限縮到某個有限 component。根落在完整中心球，不是自動落在 CP 的 identity-connected component。

### 共軛與外部逆元配對

若 \(cgc^{-1}=h^\epsilon\)、\(\epsilon\in\{1,-1\}\)，令兩軸距 o 的垂距為 q_g、q_h。上述位移公式及 \(\ell\ge\sigma\) 給 \(q_g,q_h\le Q\)。左乘 c 一個 h 的整數冪，使 c 送來的軸垂足距 h 軸上 o 的垂足不超過 \(\ell(h)/2\)。三角不等式給新共軛子 \(c'\) 的中心位移不超過 \(B_{\rm conj}\)。此調整不改共軛等式。

故對所有 \(v\in\mathcal W_{B_{\rm conj}}\) 與兩個 epsilon 測試

\[
\operatorname{red}(v w_g v^{-1}w_h^{-\epsilon})=\varnothing
\tag{13}
\]

就是完整群的有限見證判定，而不只是有限 component 中找共軛子。兩個符號仍須按照原 owner 合同作外部逆元配對。

**候選超集可省去額外幾何比較。** (10) 可能包含中心位移超過 s 的字，無須先排除它們：陽性 (12)／(13) 是真實群等式，陰性結論只依賴見證全集包含性。這避免為每個共軛子另開一個 \(B_{\rm conj}\) 邊界的超越比較問題，但不取消原 CP state 的固定 guard 和 cutoff 檢查。

## 6. 一手算法來源的適用性與不能跳過的實作

Kapovich 的 Theorems 0.4–0.5／Corollary 4.9 對 C(6)–P presentation 給出固定指數開根及最大根指數的算法存在性；(3) 確實滿足其組合輸入條件。[K] 然而其構造經過有效嵌入、biautomatic structure、equality／multiplier automata 及最短共軛代表；這些物件沒有因 (3) 自動成為本專案已提供的檔案。特別不能把另一 presentation 的 geodesic language 直接當成本例原八字母的最短字語言。

本筆記選取的最小 bridge 只需要 (5) 的詞問題、(9) 的外部幾何詞長界，以及 (11)–(13) 的有限見證界，不主張新 root／conjugacy 線性時間算法。尚未完成者包括：exact parser 與 word／state 綁定、規則表與策略實作、全候選覆蓋記錄、陽性改寫證書及陰性終態檢查、實際 W 常數的版本綁定、owner 商排序、canonical bytes、digest、FIFO 與獨立 replay。

沒有把任何紙面陰性宣稱為某次搜索的實測陰性；沒有產生 census、observed digest、舊狀態數或深度的重播信用。

## 7. 來源與本次動作範圍

本筆記新增使用的算法文獻依賴只有兩項：Touikan 作者講義中已直讀的 Dehn 定理，以及 Kapovich 作者論文中已直讀的 piece／P 定義及開根算法敘述。前者是作者教學材料，不偽稱 Greendlinger 原始論文；後者使用 arXiv 作者版本，不宣稱重播任何舊來源雜湊。來源中的定理與本例十六前綴檢查是不同的證據層；先行幾何結論 (2)、(9)、(11) 的依賴不因此被取消。

本次只以只讀 shell 定位和閱讀現有文本、普通瀏覽核對來源，並以 apply_patch 新增本文件。十六前綴、規則、反例及見證橋接均為紙面推導；未運行符號程序、枚舉或科學測試。AI 輔助審查及同伴覆核均不被當作獨立科學實證。

[input]: /root/autodl-tmp/flow_systems/papers/28-bolza-magnetic-flow/results/round7_nonarithmetic_control_matrices.json
[contract]: /root/autodl-tmp/flow_systems/papers/33-bolza-control-matched-census/notes/stage4_prime_round5_support/cp_enumeration_contract.json
[identity]: /root/autodl-tmp/flow_systems/papers/33-bolza-control-matched-census/notes/internal_exact_state_identity_and_guard_decidability_20260909.md
[T]: https://ntouikan.ext.unb.ca/MATH6022/IntroCGGT/html_output/section-18.html
[K]: https://arxiv.org/pdf/math/9611203
