# P31：有限 owner 分割的憑證閉合與 G/I/C 下降

日期：2026-09-08。狀態：**內部有界理論增量；未執行 owner 分類，非正式複審、非科學回執、非 Route 判定。**

## 0. 問題、依據與本輪邊界

本筆記以 [stage4_prime_revision_round6.tex](stage4_prime_revision_round6.tex) 的 §§4.1–4.4 為語義契約：owner 是保持方向的本原 `Gamma_0(11)` 共軛類；`delta` 是可回傳 unresolved 的總處置，`kappa` 僅定義於 resolved 域；完整 G/I/C 仍以全部輸入閉合為前提。固定流、正時間變換、時鐘、Hecke 正規化、互反 log-zeta 慣例及 period coordinate 均不改變。

以下 `n=|X|` 是有限集合的一般參數。原文指定的目標人口為 138 個 input IDs、55 個 source-word/prime groups；本輪沒有讀取並重新驗證這 138 筆實例，沒有產生任何真實 owner bytes、分割、9453 列結果或 G/I/C 表。

核心增量不是重述「需要雙條件」，而是給出：

1. 同一區塊的正 witness、區塊間的語義分離、全體 input-ID 覆蓋，分別承担什麼邏輯義務，以及何時足以、何時必要。
2. 在明確限制的純等價關係證據模型中，`n-k` 條正邊與 `binom(k,2)` 條負邊的尖銳下界；一般分類定理可壓縮負證據，故此不是通用演算法下界。
3. 具體的 level-11 代數引理：本原根檢查可化為有限整數遞迴；一個 primitive 代表加精確正冪共軛式即可覆蓋整塊；hyperbolic owner 不自逆共軛。
4. 從正確有限商到 G/I/C 的精確映射，尤其 C 是同時保留 cell 與 owner 的細商，不是從 G 單獨決定的表。

本輪使用 ARS academic-paper 的 argument-builder 角色，限於自含命題、證明與反例；沒有啟動 full pipeline、writer/evaluator panel 或既有 producer。這些命題不自動註冊為原文所要求的 theorem/schema 版本。

## 1. 固定語義與三種不同的閉合

記

\[
\widetilde\Gamma=\left\{\begin{pmatrix}a&b\\c&d\end{pmatrix}\in
\mathrm{SL}_2(\mathbb Z):c\equiv0\pmod {11}\right\},
\qquad \Gamma=\widetilde\Gamma/\{\pm I\}.
\]

所有 hyperbolic 類使用跡大於 2 的唯一正跡 lift。這排除了把中心符號、負跡 lift 與流的方向混為一談。下文的「本原」指在 \(\Gamma\) 中不是大於 1 次的正冪；取正跡 lift 後，正冪等式也可按精確矩陣等式驗證。

`X` 是帶唯一 input ID 的有限實例集合，不是去重後的矩陣集合。不同 ID 即使帶相同矩陣，仍是不同 incidence occurrence。輸入 exact decoding 成功時得到正跡 hyperbolic \(A_x\in\widetilde\Gamma\)；若 decoding、membership 或 hyperbolicity 未確證，该列仍未解，不能假設已進入以下數學域。

對 admissible 輸入，令 \(p(x)\) 為其保持正向的本原根，並定義

\[
x\sim y\quad\Longleftrightarrow\quad
p(x)\text{ 與 }p(y)\text{ 在 }\Gamma\text{ 中共軛}.
\tag{1}
\]

§4 將直接證明此根的存在及唯一性。owner 的相等是 (1)，不是 trace、長度、homology、字串相等或「搜尋尚未找到共軛子」。

給定 resolved 集合 \(R\subseteq X\) 及函數 \(\kappa:R\to B\)，需分清：

| 義務 | 精確內容 | 不提供什麼 |
| --- | --- | --- |
| 資料域覆蓋 | 每個 frozen input ID 恰有一個處置；完整閉合另需 \(R=X\) | 不證明任何 owner 相等或不等 |
| 區塊內語義正確 | \(\kappa(x)=\kappa(y)\Rightarrow x\sim y\) | 不排除同一 owner 被分成多塊 |
| 區塊間語義分離 | \(x\sim y\Rightarrow\kappa(x)=\kappa(y)\) | 不覆蓋被遗漏的輸入 |

前兩個語義箭頭合起來才有 \(R/\!\sim\cong\kappa(R)\)。只有另外證明 \(R=X\)，才有全體商 \(X/\!\sim\)。空 resolved 域上的雙條件真空成立，不能替任何非空人口提供閉合。

## 2. 有限憑證分割定理

### 2.1 最小的語義骨架

先固定 \(R\subseteq X\)，假設其中每列的 root/admissibility 已按契約證明。提出非空、兩兩不交的 blocks \(B_1,\ldots,B_k\)，其並為 \(R\)；每塊選一個 anchor \(r_j\in B_j\)。選互異 labels \(b_1,\ldots,b_k\)，設

\[
\kappa(x)=b_j\quad(x\in B_j).
\tag{2}
\]

令 \(\mathsf{Attach}\) 和 \(\mathsf{Separate}\) 為下列**語義命題**，不是 producer 自報的 Boolean：

\[
\begin{aligned}
\mathsf{Attach}:&\quad x\sim r_j &&(x\in B_j),\\
\mathsf{Separate}:&\quad r_i\not\sim r_j &&(i\ne j).
\end{aligned}
\tag{3}
\]

**定理 1（有限分割的必要充分條件）。** 在上述集合分割、anchors 與 label injectivity 已確定的前提下，(2) 滿足

\[
\forall x,y\in R,\qquad \kappa(x)=\kappa(y)\iff x\sim y
\tag{4}
\]

當且僅當 (3) 的兩個命題成立。

**證明。** 若 labels 相等，\(x,y\) 同屬 \(B_j\)，由 \(x\sim r_j\sim y\) 得 soundness。反之，若 \(x\sim y\)，而它們分屬 \(B_i,B_j\)，則 \(r_i\sim x\sim y\sim r_j\)，與 separation 矛盾，故兩者同塊。必要性則直接把 (4) 用於 \((x,r_j)\) 與 \((r_i,r_j)\)。□

其內容不是「把雙條件改名」：原來 \(O(|R|^2)\) 個輸入間語義主張，可由區塊內的連通 witness 與 quotient 層的 separation 生成。這也指出不能刪掉的兩個相反方向：positive attachment 防止誤合併；negative separation 防止誤拆分。

### 2.2 Witness graph、正共軛子的合成與可重播性

每塊不必逐列直接連至 anchor。可以給一棵以 \(r_j\) 為根的 spanning tree；每條定向邊 \(u\to v\) 附精確 \(H_{uv}\in\widetilde\Gamma\)，使

\[
H_{uv}p(u)H_{uv}^{-1}=p(v).
\tag{5}
\]

沿唯一 tree path 乘起共軛子，並在反向邊取逆，即得任意成員到 anchor 的 witness。子群對乘法、取逆封閉，故不會把 ambient conjugator 偷換成 subgroup conjugator。每塊 \(|B_j|-1\) 條邊足夠，合計 \(|R|-k\) 條。

跨塊可以逐對給 anchor 的 lawful nonconjugacy 證書，亦可由一個已證明並綁定的分類不變量 \(\nu\) 提供 separation。此處只需

\[
P\sim Q\Longrightarrow\nu(P)=\nu(Q),
\qquad \nu(p(r_i))\ne\nu(p(r_j))\ (i\ne j).
\tag{6}
\]

因此 coarse invariant 在**值不同**時可以提供負證據；在值相同時不能推斷同 owner。若採全域 normal form 來處理 invariant collisions，則仍需該 normal form 的正確性定理，而不是把不同 bytes 當成 (6) 的證明。

「必要充分」在定理 1 是語義層的 iff。給定 proof language 與 verifier 後，soundness 僅保證「接受憑證 \(\Rightarrow\) (3) 成立」。要反向聲稱每個正確有限分割都存在可接受憑證，還須對所需 root、正共軛與負共軛命題另證**相對完備性**；有限輸入本身不會使一個不完備的負證據語言變完備。本文没有聲稱已建立 P31 全部負共軛證據的完備語言。

## 3. 有限等價關係證據的尖銳下界

這一節刻意採取弱而清楚的模型：已知 \(n\) 個 admissible、已取根的 tokens；未知關係僅受等價關係公理約束；可用證據只有 pair assertions \(u\sim v\) 與 \(u\not\sim v\)。沒有群的分類定理、已知 class count、完備不變量或其他多點公理。先要求所有 assertions 都與所聲稱的目標分割相容，尤其沒有 block 內的負邊；assertions 的真實語義仍須另有證書，並非以下圖檢查自行證明。

**定理 2（pair-evidence 模型）。** 若目標分割有 \(k\) 個非空 blocks，僅憑上述證據唯一確定該分割，充要條件為：

1. positive-edge graph 的連通分量恰是目標 blocks；
2. 每兩個不同分量間至少有一條 negative edge。

因而至少需要 \(n-k\) 條 positive edges 及 \(\binom{k}{2}\) 條 negative edges；每塊一棵 tree、每對 anchors 一條 negative edge 同時達到兩個下界。

**證明。** 正邊的等價閉包就是其連通分量。若一個目標 block 的正邊不連通，把它拆成其正邊分量仍滿足全部已給負證據，故原 block 不被強制成立。反之，若兩個目標 blocks 間沒有負邊，把它們合併，其他 blocks 不動，仍滿足全部正負 assertions。這證明兩項必要性。兩項俱備時，任何相容的等價關係不得拆 positive component，又不得合併不同 components，因此只能是目標分割。連通的 \(m\)-vertex graph 至少有 \(m-1\) 條邊；每條負邊只跨一對 quotient vertices，故得兩個下界。□

**限制。** 不等關係不具遞移性：\(a\not\sim b\) 與 \(b\not\sim c\) 不推出 \(a\not\sim c\)。負邊的 spanning tree 因而不夠。另一方面，(6) 或群特有定理能一次證明許多分離命題，故 \(\binom{k}{2}\) 不是所有 P31 證明系統的必要 certificate row 數，更不是時間或 byte-length 下界。對已原始 rooted 的 tokens 得出的 \(n-k\)，也不包括下一節的 input-to-power/root bindings。

## 4. 對 Gamma_0(11) 的 root 層作具體壓縮

### 4.1 Hyperbolic 中心化子與唯一正向本原根

**引理 3。** 若 \(A\in\Gamma\) hyperbolic，則 \(C_\Gamma(A)\) 是無限循環群。存在唯一沿 \(A\) 正方向的本原元素 \(P\) 及唯一 \(m\ge1\)，使 \(A=P^m\)。

**證明。** 把 \(A\) 的两个實特徵線作基底。\(\mathrm{PSL}_2(\mathbb R)\) 中與 \(A\) 交換的元素必保持每條特徵線，正規化中心符號後形如

\[
\operatorname{diag}(e^{t/2},e^{-t/2}),\qquad t\in\mathbb R.
\]

因此其中心化子與加法群 \(\mathbb R\) 同構。\(\Gamma\) 離散：它是整數矩陣離散群對有限中心的商。其交集是 \(\mathbb R\) 的非零離散子群，必為 \(\tau\mathbb Z\)，\(\tau>0\)；非零性由 \(A\) 本身提供。取與 \(A\) 同方向的生成元便得 \(P\)。任何 \(A\) 的正根都與 \(A\) 交換，故在此循環群中；存在性、本原性與唯一性皆隨之成立。□

特別地，若一塊有一個已確證本原的正跡代表 \(P_j\)，每列攜帶

\[
A_x=H_xP_j^{m_x}H_x^{-1},\qquad
H_x\in\widetilde\Gamma,\quad m_x\in\mathbb Z_{\ge1},
\tag{7}
\]

便可同時證明其 owner 為 \([P_j]\)、其 maximal traversal exponent 恰為 \(m_x\)。確實 \(H_xP_jH_x^{-1}\) 仍本原；若 \(A_x=Q^r\)，則在由该本原元素生成的中心化子內，\(Q\) 必為其整數次冪，故 \(r\mid m_x\) 且 \(r\le m_x\)。

這把「每列一份 no-proper-root 證書」壓成「每個 proposed owner 代表一份 primitive 證書，加每列一份精確 (7)」。沒有刪掉每列的 root powering、membership、正方向或 traversal metadata。Hecke degree 仍不是 \(m_x\)。

### 4.2 不借浮點對數的有限 primitive 證書

可進一步為上一節的 primitive 謂詞給出一個明確而有限、但不宣稱高效的 exact 方法。令

\[
\begin{aligned}
s_0(t)&=2,&s_1(t)&=t,&s_{m+1}(t)&=t\,s_m(t)-s_{m-1}(t),\\
q_0(t)&=0,&q_1(t)&=1,&q_{m+1}(t)&=t\,q_m(t)-q_{m-1}(t).
\end{aligned}
\tag{8}
\]

對 determinant-one、trace \(t\) 的矩陣 \(R\)，Cayley–Hamilton 給

\[
\operatorname{tr}(R^m)=s_m(t),\qquad
R^m=q_m(t)R-q_{m-1}(t)I.
\tag{9}
\]

固定正跡 hyperbolic \(P\in\widetilde\Gamma\)，令 \(T=\operatorname{tr}P\ge3\) 且

\[
M(T)=\max\{m\ge1:s_m(3)\le T\}.
\tag{10}
\]

此集合有限且非空：\(s_m(3)\) 嚴格增加且無界。若 \([P]=[R]^m\) 在 projective 群中為正向 proper power，\([R]\) 必為 hyperbolic。若原矩陣 lift 為負跡，先取 \(-R\)；這不改變 projective 元素或 subgroup membership。正跡 lift 的特徵值均為正，其任意正冪亦為正跡，故 projective 等式此時必提升為精確等式 \(P=R^m\)，而不是 \(-P=R^m\)。這涵蓋偶次冪原本可能使用負跡根的情形。於是 \(R\) 是正跡整數 hyperbolic 矩陣，\(t=\operatorname{tr}R\ge3\)。其擴張特徵值 \(\lambda(t)=(t+\sqrt{t^2-4})/2\) 隨 \(t\ge3\) 增加，而 \(s_m(t)=\lambda(t)^m+\lambda(t)^{-m}\)，所以

\[
2\le m\le M(T),\qquad 3\le t\le T,\qquad s_m(t)=T.
\tag{11}
\]

**命題 4（有限 root obstruction）。** 對每個 (11) 的整數候選 \((m,t)\)，形成唯一可能矩陣

\[
R_{m,t}=\frac{P+q_{m-1}(t)I}{q_m(t)}.
\tag{12}
\]

其中 \(q_m(t)>0\)。逐候選精確檢查：四個 entries 皆整數、determinant 為 1、左下 entry 是 11 的倍數、trace 為 \(t>2\)、以及 \(R_{m,t}^m=P\)。則 \(P\) 本原，當且僅當沒有候選通過全部檢查。

**證明。** 通過的候選顯然給出 lawful proper root。反之，任何 proper root 必滿足 (11)，且由 (9) 被強制等於 (12)，因此不可能漏掉。所有範圍與運算皆為有限整數或有理數運算；(10) 可直接遞迴至首次超過 \(T\)，毋須用近似對數決定截止。□

這個 obstruction 的 verifier 應自行重建完整候選範圍與每個拒絕原因，不能信任 producer 聲稱「列表已窮盡」。它處理 exact matrix representation 的本原性，不解決一般兩個不同代表之間的 \(\Gamma_0(11)\) 非共軛，也沒有替 frozen words 建立 decoding 證書。

## 5. 逆向政策：可證的 level-11 排除與仍未閉合的連結

### 5.1 一個不需要搜尋共軛子的排除引理

**引理 5（level-11 hyperbolic 不自逆）。** 對任意正跡 hyperbolic \(P\in\widetilde\Gamma\)，不存在 \(W\in\widetilde\Gamma\) 使 \(WPW^{-1}=P^{-1}\)。同樣的非共軛結論在 \(\Gamma\) 中成立。

**證明。** \(P\) 的特徵值為相異正數 \(\lambda,\lambda^{-1}\)。若此等式成立，\(W\) 必交換兩條特徵線；在該基底下是 off-diagonal 矩陣，故 \(\operatorname{tr}W=0\)。寫

\[
W=\begin{pmatrix}a&b\\c&-a\end{pmatrix},\qquad
c\equiv0\pmod {11},\qquad -a^2-bc=1.
\]

便得到 \(a^2\equiv-1\equiv10\pmod {11}\)。但模 11 的平方剩餘為 \(\{0,1,3,4,5,9\}\)，矛盾。在 projective 群中的等式提升後只可能是 \(WPW^{-1}=\pm P^{-1}\)；兩側的正跡迫使正號，故同一證明適用。□

這是本筆記的直接代數證明，不是從「沒有找到 inverse witness」推斷非共軛。它與 Sage 官方 `Gamma0(N).nu2()` 文件給出的 order-2 elliptic-point 公式相符：含有一個 \(p\equiv-1\pmod4\) 的 prime divisor 時數目為零；\(11\) 滿足此條件。該文件只作此背景交叉核對，並不提供 P31 owner 或 canonical bytes 的正確性證明。[Sage 官方 Gamma0 文件，nu2](https://doc.sagemath.org/html/en/reference/arithgroup/sage/modular/arithgroup/congroup_gamma0.html#sage.modular.arithgroup.congroup_gamma0.Gamma0_class.nu2)

### 5.2 不把排除自逆誤寫成 inverse ledger 已完成

若將引理 5 正式註冊並綁定到 exact subgroup/lift/hyperbolicity predicates，它可為所有符合前提的 roots 提供 `inverse_separated` 的語義 obstruction。未驗證的 membership 或 theorem binding 仍須 unresolved；原有三分支 schema 不應被本筆記靜默改寫。本輪不填任何真實列，也不刪除原文的 self-reciprocal branch。

此外，\([P]\ne[P^{-1}]\) **不決定** \([P^{-1}]\) 是否等於另一個觀測代表 \([Q]\)。若 inverse link 宣稱指向某個已觀測 owner，仍需 \(P^{-1}\sim Q\) 的正 witness，或相應完整分類證明。

全 owner 空間有無固定點的 involution \([P]\mapsto[P^{-1}]\)，但觀測商 \(X/\!\sim\) 未必在此 involution 下封閉。若 finite-local labels 必須同時序列化所有 inverse targets，可在**輔助證明域** \(X^{\pm}=X\times\{+,-\}\) 上對 \(A_x\) 與 \(A_x^{-1}\) 重用定理 1，並驗證 induced inverse links。這不是擴大或改寫真實人口：G 仍只能取原 \(X\) 的 image，不能把僅作逆向輔助的 owner 計入 G。只要此 extension 尚未驗證，就不可聲稱完整 canonical inverse-link bytes 已存在。

## 6. 由憑證到 total delta：閉合、接受與 determinism

### 6.1 邏輯最小骨架不等於完整序列化 schema

一份足夠的 prospective witness ledger 可分層承載：

| 層 | 必需數學/資料內容 | 可由 verifier 得出的結論 |
| --- | --- | --- |
| Input binding | frozen manifest、所有唯一 IDs、exact payload 與版本、cell/provenance | 定義的是指定的 X，不是有相同 row count 的另一集合 |
| Root/attachment | 每塊 primitive 代表證書；每輸入 (7)，或已 rooted 的 tree 證書 | 每塊內沒有誤合併，traversal exponent 正確 |
| Quotient separation | 代表間負證書，或適用於全部代表的 theorem-backed separation | 不同塊不是同 owner 的誤拆分 |
| Inverse | 引理 5 的前提/版本；如需 canonical links，另有 §5.2 的連結證據 | 不把正反方向默認合併；連結不越出已驗證域 |
| Encoding | 固定、injective、可重播的 serialization 規則 | bytes 正確標記已證的 blocks，而不是只碰巧相等 |

此表是數學依賴介面，不宣稱已有 schema bytes、theorem registry、producer 或 independent verifier。雜湊可綁定輸入，但雜湊一致性不證明語義；數學上需要 exact binding 或另陳述 collision-resistance 假設，不能把任意 finite digest 當成無條件 injective encoding。

### 6.2 可實現的 fail-closed 總處置

假設各 proof check 使用固定版本、可終止的 verifier；超出已登記資源上限回傳 typed unresolved。對每個 frozen ID 產生一個處置，missing、duplicate、malformed、stale 或未通過的相關證據都不能回傳 `Resolved`。

尤其「單列通過 (7)」不等於可以單獨發放互不相同的 owner bytes：它尚未排除與另一個已發 bytes 的代表共軛。保守而確定的策略是：先驗證整份 proposed resolved-domain ledger 的 root、attachment、separation、inverse 與 encoding 義務；若其中任何全域義務失敗，該候選域不發放 resolved owner labels，回傳帶失敗證據的 unresolved 處置。有效的部分域可另明示為 R，但不可在閱覽結果後任選 subset 來保住偏好的 owner count。

因此

\[
\delta:X\to\mathrm{Resolved}(b,w)\sqcup
\mathrm{Unresolved}(\mathrm{code},\mathrm{evidence}),
\qquad
R=\{x:\delta(x)\text{ 是 Resolved}\}
\tag{13}
\]

可以在未證人口閉合時保持 total。對任一成功驗證的 R，定理 1 保證其 \(\kappa\) 的雙條件。完整 owner 結論另需

\[
\mathsf{Closed}=\bigl(R=X\bigr),
\tag{14}
\]

且以精確 ID 集合比對，不是僅比較 cardinality。給每列一個 unresolved code 已使 delta total，卻沒有使 kappa total。

### 6.3 有限商的 canonical labels 與全域 canonical form 不同

存在一個簡單的有限域標記規則：對固定排序的 immutable IDs，為每個 true block 使用最小 ID，配以固定 scope/version namespace 及 injective encoding。由定理 1 可知，一旦接受的分割都等於真實有限商，這些 labels 在同一 frozen scope 的所有合法重播中相同，不依賴 tree、anchor matrix 或 witness 選擇。

但是這只是 **dataset-local canonical labeling**。換一份人口、加入同 owner 的較小 ID 或改變 scope namespace，bytes 可以改變。它不證明在所有 \(\Gamma\) 輸入上的普遍 deterministic canonical form，不保證跨 manifest 的 owner-byte 穩定，也不是對既有 `owner_bytes` 規格的授權替換。

反之，任意一次執行滿足 (4)，並不足以證明 determinism：第二次執行可把每個 label 全部加同一 fresh prefix，仍滿足 (4)，但 bytes 已不同。因此 repeatability 的固定 serialization 義務不能由 partition correctness 省略。

## 7. 從已閉合 quotient 精確下降到 G/I/C

只在 (14) 成立且所有上述契約接受後，令

\[
\Omega=X/\!\sim,\qquad q:X\twoheadrightarrow\Omega,
\qquad b:\Omega\xrightarrow{\cong}B=\kappa(X),
\qquad \kappa=b\circ q.
\tag{15}
\]

令 frozen cell map 為

\[
c:X\to K,\qquad
c(x)=(\mathrm{source\_word},\mathrm{prime},\mathrm{hecke\_degree})(x).
\tag{16}
\]

**定理 6（incidence-first construction）。** 若每個 \(x\) 的 frozen metadata 與 root/traversal/inverse 證據均有唯一 binding，則以下構造良定：

\[
\begin{aligned}
I&=\{(\mathrm{id}(x),\mathrm{payload}(x),c(x),
             \kappa(x),m_x,\mathrm{inverse/proof\ refs}(x)):x\in X\},\\
G&=\pi_{\mathrm{owner}}(I)=\{\kappa(x):x\in X\},\\
C&=\pi_{\mathrm{cell,owner}}(I)
  =\{(c(x),\kappa(x)):x\in X\}.
\end{aligned}
\tag{17}
\]

兩個 projection 都採 distinct/set semantics；I 不去掉重複 owner 的 input occurrences。故 \(|I|=n\)，\(|G|=|\Omega|\)。完整 materialization 的允許方向仍是 `I -> G,C`。

定義較細關係

\[
x\approx y\iff c(x)=c(y)\ \text{且}\ x\sim y.
\tag{18}
\]

則有自然滿射鏈及 canonical bijection

\[
X\twoheadrightarrow X/\!\approx\twoheadrightarrow\Omega,
\qquad
X/\!\approx\xrightarrow{\cong}C,\qquad
[x]_\approx\longmapsto(c(x),b([x]_\sim)).
\tag{19}
\]

**證明。** (17) 保留唯一 IDs，故 \(X\to I\) 一一對應。映射 \((c,\kappa)\) 的 fibers 恰是 (18)；因此 (19) 不依代表選擇、單射且滿射。由 \(\approx\) 蘊含 \(\sim\)，第二個 quotient map 良定。□

這裡細節重要：\(c\) 能直接下降到 \(\Omega\)，當且僅當它在每個 owner fiber 上常值，即每個 observed owner 只出現於一個 cell。一般情況下同 owner 可跨 cell，故不存在這樣的 \(\Omega\to K\)；C 需要 I 保留下來的 occurrence-to-cell 關係，不能由 G 單獨產生。

更精確地，令

\[
n_{a,g}=|\{x:c(x)=a,\ q(x)=g\}|,
\qquad d(g)=|\{a:n_{a,g}>0\}|.
\]

則

\[
\sum_{a,g}n_{a,g}=n,
\qquad |C|=\sum_{g\in\Omega}d(g),
\qquad |G|\le|C|\le n.
\tag{20}
\]

第一個等號保留 raw multiplicity；C 只記 \(n_{a,g}>0\) 的 support，每個 cell-owner 給一單位。\(|C|=|G|\) 當且僅當每個 owner 恰出現於一個 cell；\(|C|=n\) 當且僅當每個非空 cell-owner fiber 恰有一列。這些是**閉合後**的恆等式，不是用來猜未解 owner count 的估算器。

即使已知完整 input IDs、其 cells 與 n，G/C 聯合仍不重建 I：取四個抽象 IDs，前兩個在 cell a，後兩個在 cell b；各 cell 都各含 owner u、v。只交換第一個 cell 中兩個 IDs 的 owner assignments，G 與 C 不變，I 已不同。此反例是純集合論構造，不是 P31 實例。

代表不變性也要有明確域：在同一 certified encoding scope 中替換為已證同 owner 的代表，且保留 ID、cell、traversal 與其他 incidence 資料，G 與 C 的 owner keys 不變。若跨出 finite-only canonicalizer 的 scope，§6.3 不保證 literal bytes 不變；只能先聲稱商與 (17) 在一致 relabeling 下同構。

## 8. 具體失敗例與 9453 表的證據極限

下列兩個矩陣例是本筆記的手算構造，沒有納入 frozen fixtures，也未作任何人口實驗。設

\[
P=\begin{pmatrix}1&1\\11&12\end{pmatrix},\quad
U=\begin{pmatrix}1&1\\0&1\end{pmatrix},\quad
UPU^{-1}=\begin{pmatrix}12&1\\11&1\end{pmatrix}=:Q.
\tag{21}
\]

P、Q、U 都在 \(\widetilde\Gamma\)，P 與 Q 的 trace 是 13。P 本原：\(s_2(3)=7\)、\(s_3(3)=18>13\)，僅可能有平方根；但 \(s_2(t)=t^2-2=13\) 無整數解。由共軛不變性，Q 亦本原。

- **誤拆分：** 直接把不同矩陣 entries 當作不同 owner bytes，會把 P 與 Q 分開，雖然 (21) 已給 exact subgroup conjugator。
- **誤合併與方向丟失：** 把 trace 當作 owner bytes，會合併 P 與 \(P^{-1}\)，而引理 5 已證兩者不是同一 oriented owner。
- **假 root 證書：** 僅展示 \(A=R^m\) 而不證 R 本原，不能保證 m maximal；例如把 \(A=P^4\) 取為 \(R=P^2,m=2\)，powering 完全正確但 traversal exponent 應為 4。
- **覆蓋失敗：** 137 個 input IDs 各有正確 owner 與雙條件，不能閉合 138 個 IDs；把其中一個 ID 複製兩列湊足 row count 也無效。
- **跨塊分離失敗：** 所有列都附到各自合法 primitive 代表，仍可能兩個 proposed 代表正好是 (21) 的 P、Q；positive witnesses 全部成立，分割仍錯。
- **determinism 失敗：** 每次對正確 blocks 換一組 injective fresh labels，不破壞單次雙條件，卻破壞固定 bytes 的重播要求。

對 \(n=138\)，\(\binom{138}{2}=9453\)。給定已輸出的 \(\kappa\)，unordered distinct-pair 表中的 equality bit 只是

\[
T(x,y)=\mathbf1_{\{\kappa(x)=\kappa(y)\}},\qquad x<y.
\tag{22}
\]

即使每一 bit 都與原 bytes 完全一致，(21) 的誤拆分或 P/\(P^{-1}\) 的誤合併仍會被忠實地重播。9453 是 byte-pair **覆蓋數**，不是 9453 個獨立語義判定；它也不包含 self、ordered-reversal 或 triple fixtures。byte equality 的 reflexivity/symmetry/transitivity 可從字串相等的數學性質推出，但這仍不能推出它等於 (1)。

其正當用途仍是版本/輸入 binding、遺漏/重複 pairs、排序、inverse/traversal metadata、序列化與已承諾分割的一致性回歸。若另外提供 theorem-backed semantic predicates 或 target-blind adjudicator，這些新證據才可能揭露或證明語義差異；它們不能被歸功於 (22) 自己。既有契約要求的派生 audit gate 亦不因定理 1 的證書壓縮而自動取消。

## 9. 已完成的實際檢查與未完成義務

本輪實際執行：

- 只讀 `AGENTS.md`、`docs/workflow.md`、ARS skill/router、academic-paper workflow 及 argument-builder role；只讀 round6 原文的 owner、root/inverse、canonicalizer、pair audit 與 G/I/C 段落。
- 對 round6 `.tex` 執行 `sha256sum`，讀得 `4bc1a960b5527a5d389b5c70e29fa0dc7b3199b93a808dd3f347616dd686d1a3`。此為本輪讀取的來源身分，不是原有鎖定回執的重算或替換。
- 普通公開瀏覽 Sage 官方 Gamma0 文件的 `nu2()` 段落，僅交叉核對 level-11 order-2 背景；沒有執行 Sage、API resolver、producer、實驗或任何資料上傳。
- 以 `apply_patch` 新增本筆記；對新增文字作只讀結構、公式依賴與反例逐項檢查。沒有修改原文、舊 notes、科學程式、experiments、results、正式 paper 或回執。
- 嘗試 `git status --short -- papers/31-level11-conjugacy-owner-ledger` 時，工作目錄回報 `not a git repository`；故本輪不宣稱取得 git diff/status 證明，也沒有另行尋找或操作外部 git 根目錄。

已得到的是自含條件定理與 exact primitive/inverse 引理，不是 observed ledger。下一個真正需要閉合的有限義務為：

1. 逐個 input ID 的 exact decoding、membership、positive-trace hyperbolicity 與 frozen provenance。
2. 每個 proposed owner 的 primitive 證書與每輸入 (7)，及全部 proposed blocks 間的 lawful semantic separation；其中一般 \(\Gamma_0(11)\) 非共軛仍未由本文解決。
3. 若要求完整 inverse-owner bytes，則需註冊 §5 引理、驗證其適用前提，並完成實際 inverse links 或明示輔助 inverse-closed 證明域。
4. author-approved serialization scope、closed schema、theorem registry、具 soundness 的 terminating independent verifier，以及跨資料集 canonical form 所需的額外定理。本文未將 finite-local labels 偷換為原文的 owner bytes。
5. 得到 \(R=X\) 的完整憑證後，才可執行原契約的派生 audit 與 `I -> G,C`；任何 unresolved 都仍禁止報告完整 estimands。

本筆記不變更 P31 的既有實驗/發表/Route 狀態，不宣稱首次發現、正式證明驗證器通過、138-input replay、owner census 或五篇批次完成。
