# P31：人口無關的有向 subgroup primitive-owner 規範鍵

日期：2026-09-09。Goal 01 範圍內的有界內部理論筆記。只新增本文件；不執行 frozen decoding、矩陣／coset 枚舉、138 rows、pair audit、producer、fixture 或科學程式，不改鎖、正式稿、Route 或 Stage 狀態。

## 0. 結論、固定條件與上游接口

本筆記證明一個定義在**全部 admissible exact 正跡 hyperbolic subgroup 矩陣**上的抽象規範鍵。先取正向 subgroup primitive root，再取其正向 ambient primitive root 的最小 cyclic syllable rotation，最後以完整 coset cycle 的最小 state 標記 subgroup class splitting。所得鍵相等，當且僅當兩個輸入具有相同的有向 subgroup primitive owner。

所用上游材料為：

- [ambient normal forms 與共軛證書][normal] 的唯一 reduced normal form、cyclic conjugacy criterion，以及 §8 明列尚未完成的 canonical-owner 接口；
- [coset 周期提升與有向類分裂][cycles] 的完整提升雙射、最小返回與 subgroup primitiveness，以及 ambient reversible 的 inverse-cycle 邊界。

本筆記將這兩份既有理論拼成規範鍵定理；不回寫它們當時的歷史 missing 清單。兩個全序保持為**抽象而一次固定的數學參數**，不在此指定或版本化 serialization、bytes、owner 值域或實作。使用 ARS academic-paper 的 argument-builder 有界論證方法，沒有啟動完整研究／論文 pipeline。

## 1. 群、固定 lifts、全序與正向 primitive roots

固定

\[
\widetilde G=\mathrm{SL}_2(\mathbb Z),\quad
G=\widetilde G/\{\pm I\},\quad
\widetilde\Gamma=\Gamma_0(11),\quad
\Gamma=\widetilde\Gamma/\{\pm I\}.
\tag{1}
\]

沿用 [ambient 筆記][normal] 的生成元與 lifts，沒有重新選基：

\[
S=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\quad
T=\begin{pmatrix}1&1\\0&1\end{pmatrix},\quad U=ST,
\qquad\sigma=[S],\quad u=[U],
\tag{2}
\]

以及 reduced syllable 字母表
\(\mathcal A=\{\sigma,u,u^2\}\)，分屬 \(C_2\)、\(C_3\) 兩個因子。固定一個字母全序 \(\prec_{\mathcal A}\)，誘導有限詞的字典序。另固定

\[
\mathcal S=\mathbb P^1(\mathbb F_{11}),\qquad
\infty=[1:0],
\tag{3}
\]

上的全序 \(\prec_{\mathcal S}\)。不指定這兩個全序的具體排序，也不把它們當成已批准的 bytes 實作決策。以下結論對任意如此固定的兩個全序成立；其固定方式不依賴人口、prime／zero 目標或資料出現次序。

admissible input 指 exact 整數矩陣

\[
A\in\widetilde\Gamma,\qquad \det A=1,\qquad \operatorname{tr}A>2.
\tag{4}
\]

若輸入起初是 frozen ID 或 word，則它到 (4) 的語義與 exact matrix binding 是另一項義務，不由本文替代。

### 1.1 正向根與中心化子的自含依據

在 hyperbolic \([A]\) 的兩條實特徵線座標中，\(C_{\mathrm{PSL}_2(\mathbb R)}([A])\) 是保持各特徵線的一參數對角群，與 \((\mathbb R,+)\) 同構。它和離散 G 的交是非零離散子群，故為無限循環群。選擇生成元 \(r_0\) 的方向使

\[
C_G([A])=\langle r_0\rangle,
\qquad [A]=r_0^e,
\qquad e>0.
\tag{5}
\]

任何根都交換 \([A]\)，因此必在這個中心化子內；所以 \(r_0\) 是唯一正向 ambient primitive root。\(r_0\) 的所有正冪具有同一對特徵線及同一實中心化子，因而

\[
C_G(r_0^j)=\langle r_0\rangle\qquad(j\geq1).
\tag{6}
\]

這裡排除了交換兩條特徵線的 reverser：它把 hyperbolic 元素變成其逆，並不交換該元素。

\(\{n\in\mathbb Z:r_0^n\in\Gamma\}\) 是 \(\mathbb Z\) 的非零子群。令其正生成元為 d，則 \(d\mid e\)，並定義

\[
[P_A]=r_0^d,
\qquad A=P_A^{e/d},
\tag{7}
\]

其中所有 hyperbolic 矩陣取唯一正跡 lift。因 d 最小，\(P_A\) 在 subgroup 中本原；任何其他 subgroup 根仍由 (5) 控制，所以 \(P_A\) 亦是唯一的**正向** subgroup primitive root。

正向意指 (7) 的 traversal exponent 為正，不把 \(P_A^{-1}\) 任意視為同一根。正跡 lift 的約定也排除 exact roots 中的 central-sign 歧義。本文的 owner 等價關係是

\[
A\equiv_{\rm owner}B
\iff [P_A]\sim_\Gamma[P_B],
\tag{8}
\]

不是原矩陣 \(A,B\) 本身的共軛關係，也沒有加入 inverse 等價。

## 2. Ambient canonical word 與鍵的定義

對 \(r_0\) 求唯一 reduced normal form，再作任何合法 cyclic reduction，得 cyclically reduced 核心 w。hyperbolicity 排除長度 0 與 1 的核心。定義

\[
c=\operatorname{Can}(r_0)
:=\min_{\mathrm{lex},\prec_{\mathcal A}}\operatorname{Rot}(w),
\tag{9}
\]

其中 \(\operatorname{Rot}(w)\) 含**全部 syllable rotations**，不額外加入 inverse 或 reverse。

[ambient 筆記][normal] 的循環共軛定理保證：(9) 不依賴所取 cyclic core，且對 ambient hyperbolic 元素

\[
\operatorname{Can}(r)=\operatorname{Can}(r')
\iff r\sim_G r'.
\tag{10}
\]

令 \(r_c\in G\) 是按 (2) 的固定 lifts 評估 c 所得的 projective 元素，\(R_c\) 是其唯一正跡 lift。因 \(r_c\) 與 \(r_0\) 共軛，它亦為 ambient primitive、hyperbolic。取任一 \(H\in G\) 使

\[
[P_A]=Hr_c^dH^{-1}.
\tag{11}
\]

任何 determinant-one lift \(\widetilde H\) 都滿足 exact 等式
\(P_A=\widetilde H R_c^d\widetilde H^{-1}\)：projective 等式至多差負號，但兩邊正跡排除該負號。

整數矩陣先模 11，再作用於列向量射影點。令

\[
x_A=\overline H^{-1}\infty,
\qquad
\mathcal O_A=\langle\overline r_c\rangle x_A\subset\mathcal S,
\tag{12}
\]

並定義

\[
\boxed{
K(A)=\left(c,\min_{\prec_{\mathcal S}}\mathcal O_A\right).
}
\tag{13}
\]

本題使用 (11) 的 H；它是 [coset 筆記][cycles] 中寫成 \(h^{-1}r^dh\) 的 h 的逆。因此 (12) 必须是 \(H^{-1}\infty\)，不可改為 \(H\infty\)。矩陣 lifts 的 \(\pm\) 不影響射影 state。

## 3. 指數 d 必等於完整 coset cycle 長度

\(\Gamma\) 恰為模 11 的 \(\infty\) stabilizer，所以對每個正整數 j，

\[
\overline r_c^{\,j}x_A=x_A
\iff Hr_c^jH^{-1}\in\Gamma.
\tag{14}
\]

令 \(\delta\) 是 \(x_A\) 在 \(\overline r_c\) 作用下的最小正返回時間。由 (11)，\(\delta\mid d\)，而

\[
[P_A]=\left(Hr_c^\delta H^{-1}\right)^{d/\delta},
\qquad Hr_c^\delta H^{-1}\in\Gamma.
\tag{15}
\]

\(P_A\) 是 subgroup primitive，迫使 \(d/\delta=1\)。故

\[
\boxed{d=\delta=|\mathcal O_A|.}
\tag{16}
\]

反過來，任何完整 cycle 的首次返回元素 \(Hr_c^\delta H^{-1}\) 都是 subgroup primitive：若它等於 \(a^k\)、\(a\in\Gamma\)、\(k\geq2\)，則 \(H^{-1}aH\) 交換 \(r_c^\delta\)。由 (6)，它等於 \(r_c^j\)，且 \(jk=\delta\)。於是 \(0<j<\delta\) 給出更早的正返回，矛盾。

因此鍵中不必另存 d。第一分量 c 決定 \(r_c\) 的射影作用；第二分量決定其完整 cycle；(16) 從該 cycle 恢復 d。這裡不能使用未閉合的 partial orbit、僅有人口資料支持的 states，或用 \(\langle\overline r_c^{\,d}\rangle\) 代替 \(\langle\overline r_c\rangle\)。

## 4. 見證、循環起點與人口無關性

### 4.1 同一元素的 ambient 共軛見證

若兩個見證滿足

\[
H_1r_c^dH_1^{-1}=H_2r_c^dH_2^{-1},
\]

則

\[
H_1^{-1}H_2\in C_G(r_c^d)=\langle r_c\rangle.
\tag{17}
\]

故某個 \(n\in\mathbb Z\) 使 \(H_2=H_1r_c^n\)，進而

\[
\overline H_2^{-1}\infty
=\overline r_c^{-n}\overline H_1^{-1}\infty.
\tag{18}
\]

兩者落在同一完整 cycle，(13) 不變。這個推論使用 **centralizer**，不是 normalizer。

「共軛見證選擇無關」不等於「任意 ambient 共軛不變」。任意 G 共軛可能把某個 subgroup class 搬到另一個 subgroup class，第二分量正是為了保留這個 splitting，不能要求它被抹去。

### 4.2 Cyclic reduction 與 prefix witness 方向

唯一 normal form 與 (10) 使不同合法 cyclic reductions 產生同一 rotation 集，故 c 不變。若

\[
r_0=CwC^{-1},\qquad w=AB,\qquad c=BA=A^{-1}wA,
\]

則

\[
\boxed{r_0=(CA)c(CA)^{-1}.}
\tag{19}
\]

將 canonical c 搬回 \(r_0\) 的見證是 **CA**，不是 \(CA^{-1}\)。不同合法 choices 最後仍由 (17)–(18) 消除。即使有多個達到最小值的 rotation index，也只需最小詞值唯一，不需把 index 加入 K。

### 4.3 Cycle 起點與人口

(13) 對完整 orbit 取最小值，因此改變 cycle 起點不改鍵。對任何两個有限人口 \(F,F'\) 及 \(A\in F\cap F'\)，其計算定義只用 A、固定群／生成元／兩全序及完整射影作用，所以

\[
K_F(A)=K_{F'}(A)=K(A).
\tag{20}
\]

此處沒有「人口中最早出現的 representative」「本批最小 owner ID」或「已觀測到的 states」等依賴人口的選擇。兩全序若日後變更，鍵值可能變；本定理的 canonical 性是**相對於已固定數學慣例**，不是免除實作版本綁定的宣稱。

## 5. 完備性定理與 exact subgroup 共軛子

**定理。** 對所有 (4) 的 admissible exact inputs A、B，

\[
\boxed{K(A)=K(B)\iff [P_A]\sim_\Gamma[P_B].}
\tag{21}
\]

**同一 owner 給同鍵。** 若 \([P_B]=\gamma[P_A]\gamma^{-1}\)、\(\gamma\in\Gamma\)，由正向 ambient root 唯一性，它們的 ambient roots 也由 \(\gamma\) 共軛，故第一分量 c 相同。若 H 是 (11) 的見證，可以為 \(P_B\) 選 \(\gamma H\)。因 \(\gamma\) 固定 \(\infty\)，

\[
(\overline{\gamma H})^{-1}\infty
=\overline H^{-1}\overline\gamma^{-1}\infty
=\overline H^{-1}\infty.
\tag{22}
\]

再由 §4.1 的見證無關性，對任意有效見證都得到同一鍵。

**同鍵給同一 owner。** 假設 \(K(A)=K(B)\)，寫

\[
[P_A]=Hr_c^dH^{-1},\qquad
[P_B]=Jr_c^eJ^{-1}.
\tag{23}
\]

第二分量相等，使兩個完整 cycles 含有相同的最小 state；permutation 的 cycles 互不相交，故這兩個 cycles 相同。由 (16)，\(d=e\)。存在 \(n\in\mathbb Z\) 使

\[
\overline J^{-1}\infty
=\overline r_c^{\,n}\overline H^{-1}\infty.
\tag{24}
\]

令

\[
\boxed{\gamma=Jr_c^nH^{-1}.}
\tag{25}
\]

(24) 正好說 \(\overline\gamma\infty=\infty\)，因此 \(\gamma\in\Gamma\)。並且

\[
\gamma[P_A]\gamma^{-1}
=Jr_c^dJ^{-1}=[P_B].
\tag{26}
\]

取 determinant-one lifts 後，projective 等式至多差負號；兩邊皆正跡，故為 exact matrix equality。這給出同鍵時明確的 subgroup 共軛子公式，而非僅有存在性敘述。定理證畢。

不同正遍歷 \(A=P^a\)、\(B=P^b\)，即使 \(a\ne b\)，也有相同鍵。這是 (8) 的 primitive-owner 語義，不是聲稱原矩陣互相共軛。反之，僅有相同 trace、cycle 長度、測地長度或 mod-11 reduction，均不足以代替 (21)。

結合 §3 的首次返回論證，每一個 ambient primitive hyperbolic canonical c 的每條完整 cycle 都給出一個 subgroup primitive class，而 (21) 證明不同鍵不重複 owner。因此這是一個全 admissible domain 的抽象分類，不只是一個給定人口內的 pairwise 決策規則。

## 6. 取逆、ambient reversible 例外與 normalizer 禁區

\(P_A^{-1}\) 是 \(A^{-1}\) 的正向 subgroup primitive root，其正向 ambient root 是原根的逆。若

\[
r_c^{-1}\not\sim_G r_c,
\]

則由 (10)，inverse owner 的第一分量已不同。

若存在 ambient reverser

\[
nr_cn^{-1}=r_c^{-1},
\tag{27}
\]

則兩個 ambient roots 的 canonical c **確實可以相同**。不能假稱第一分量本身在所有情形都區分方向。此時

\[
[P_A^{-1}]=(Hn)r_c^d(Hn)^{-1},
\qquad
x_A^-=(\overline{Hn})^{-1}\infty
=\overline n^{-1}x_A.
\tag{28}
\]

### 6.1 Reverser 必為非平凡二階元

由 (27)，\(n^2\in C_G(r_c)=\langle r_c\rangle\)，可寫 \(n^2=r_c^a\)。n 一方面交換自己的平方，另一方面把 \(r_c^a\) 共軛為 \(r_c^{-a}\)，所以 \(a=0\)，即

\[
n^2=1,\qquad n\ne1.
\tag{29}
\]

對每個 \(k\in\mathbb Z\)，亦有 \((nr_c^k)^2=1\)，且 \(nr_c^k\ne1\)，否則 n 是 r 的冪而不可能反轉無限階 r。

### 6.2 Level 11 排除 subgroup 二階元

本段只需 \(\Gamma\) 沒有非平凡二階元，不另調用完整 torsion-free 定理。若有此元素，其 determinant-one lift M 必滿足 \(M^2=-I\)、\(\operatorname{tr}M=0\)：若 \(M^2=I\)，則 determinant 1 與特徵 0 迫使 \(M=\pm I\)，不給非平凡 projective 二階元。寫

\[
M=\begin{pmatrix}a&b\\c&-a\end{pmatrix},
\qquad c\equiv0\pmod{11}.
\]

由 \(\det M=1\)，有

\[
a^2\equiv-1\pmod{11}.
\tag{30}
\]

但這使非零 \(a\in\mathbb F_{11}\) 滿足
\(a^{10}=(a^2)^5=-1\)，與 \(\mathbb F_{11}^{\times}\) 的 \(a^{10}=1\) 矛盾。所以不存在這樣的 subgroup 元素。此證明沒有枚舉平方剩餘或實際 cosets。

### 6.3 逆向必落在另一條 cycle

假如 (28) 的 inverse cycle 與原 cycle 相同，則某個整數 k 滿足

\[
\overline n^{-1}x_A=\overline r_c^{\,k}x_A.
\tag{31}
\]

所以 \(\overline{nr_c^k}\) 固定 \(x_A\)，從而

\[
Hnr_c^kH^{-1}\in\Gamma.
\tag{32}
\]

但 (32) 是非平凡二階元，與 §6.2 矛盾。因此這兩條 cycles 不相交，固定全序下的最小 state 必不同。綜合兩種 ambient 情形，得到

\[
\boxed{K(A^{-1})\ne K(A).}
\tag{33}
\]

不同 reverser choices 不改 inverse cycle：若 \(n'\) 亦滿足 (27)，則 \(n'=nr_c^j\)，於是 \((n')^{-1}x_A=r_c^{-j}n^{-1}x_A\) 仍在同一 cycle。reverser 對 cycles 的作用是保持長度、反向且無 fixed cycle 的 involution。

### 6.4 為何不能改成 normalizer quotient

同一正向元素的見證比較只推出 (17) 的 centralizer 條件，相應參數為

\[
\Gamma\backslash G/\langle r_c\rangle
\simeq\langle r_c\rangle\backslash G/\Gamma.
\tag{34}
\]

可逆情形中，\(N_G(\langle r_c\rangle)\) 還包含 n；若把右商群擴為此 normalizer，就會把 H 與 Hn 識別，也就是把 (28) 的 \(P_A\) 與 \(P_A^{-1}\) 識別。§6.3 已證它們是兩個不同的有向 owners。

因此不能對 inverse words 自動取較小者，不能對 normalizer orbit 取最小值，也不能因 ambient class 自逆就對同一 cycle 就地建立 self-inverse owner。那些操作轉向無向循環子群／無向閉測地線的商，不是 (8) 的有向元素共軛類。

## 7. 已閉合的理論與未完成的實際接口

已閉合：在 (1)–(4) 及兩個抽象固定全序下，(13) 是人口無關、見證無關且保留方向的 primitive-owner 完備鍵；d 由完整 cycle 恢復；同鍵的 subgroup 共軛子由 (25) 給出；ambient reversible 的 inverse owners 由第二分量分離。

以下仍然沒有完成或獲本筆記替代：

- frozen IDs／words 的版本化 exact decoding、matrix binding、subgroup-root 與 traversal certificates；
- ambient normal-form／root／H 的實際 replay，以及完整 orbit closure 證書；
- 138 rows 的 population coverage、Attach／Separate、inverse-owner links 或任何 pair audit；
- 兩全序與 serialization 的正式 implementation choice、版本綁定及 injective bytes encoding；
- 對既有 `owner_bytes` 的指定、替換、相容性或遷移；
- total `delta`、resolved-domain `kappa`、G/I/C 或 frozen 科學輸出的實際計算。

定理要求全部 admissible inputs，而非僅已遇見的人口；但「在全域上有數學定義及證明」不等於「已對全部 frozen inputs 執行」。沒有藉此改動 newform、\(k=2y+z\)、Hecke、clock、原 owner 契約或任何既有停止線。

## 8. 實際動作與保全

已完整讀取兩份指定上游筆記、`docs/workflow.md`、適用的 ARS router／academic-paper workflow／argument-builder 指令；normal-form 與 coset 內容按其實際等式方向核讀。本文的中心化子、最小返回、見證變換、(25) 與 inverse 二階排除均為紙面推導，沒有用另一個 agent 的同意充當獨立科學證據。

本次唯一新增檔案是本筆記，另只作一次局部文字靜態檢查並在交接報告其結果。沒有新外部來源、程式實作、遞推回放、矩陣／coset 枚舉、資料生成、正式 build、實驗或 Route／Stage 變更。靜態檢查不證明數學正確性、資料 binding 或 owner coverage。

[normal]: internal_ambient_normal_forms_and_conjugacy_certificates_20260908.md
[cycles]: internal_coset_cycle_lifts_and_oriented_class_splitting_20260909.md
