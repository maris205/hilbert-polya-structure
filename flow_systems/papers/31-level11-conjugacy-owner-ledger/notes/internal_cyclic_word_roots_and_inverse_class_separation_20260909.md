# P31：循環詞取根、子群本原性與逆向類分離

日期：2026-09-09。狀態：**第四次五篇整輪的內部有界數學增量；非正式稿、非執行回執、非 Route 變更。**

## 0. 本輪結果與精確範圍

承接 [ambient normal-form 與共軛證書][normal]、[十二狀態子群下降][coset]。本輪把已證的 cyclic conjugacy 判準進一步轉為 **ambient primitive-root 的有限詞證書**：

> 若 exact 正跡 hyperbolic P 的 projective cyclic core w 長度為 n，則其最短完整重複前綴 v 必為偶長；寫 \(w=v^m\)，將 v 共軛回原矩陣座標並取正跡 lift，就得到 P 沿原方向的唯一 ambient primitive root R，且有 exact \(P=R^m\)。

這裡「最短」只需對有限個偶數因子長度比較，不需要無界搜尋根。證明特別排除一個潛在缺口：根本身可處於不同 cyclic 起點，但任意重複詞的 rotation 仍是同次數的重複詞，所以固定起點的前綴判準已窮盡。

再令 d 為 R 模 11 對 infinity 的最小返回週期，則

\[
P\in\widetilde\Gamma_0(11)\iff d\mid m,
\qquad R_\Gamma=R^d,\qquad
\nu_\Gamma(P)=m/d
\quad\text{（在 }P\in\widetilde\Gamma_0(11)\text{ 時）}.
\tag{1}
\]

因此 P 在 subgroup 中本原當且僅當 \(m=d\)。此外，重證已有的 level-11 不自逆引理，接上
\(R_\Gamma(P^{-1})=R_\Gamma(P)^{-1}\) 與相同 traversal exponent。
這個不自逆引理已出現在 [certified-partition 筆記 §5][partition]；本輪不把它重命名為新的發現。

本筆記只作紙面命題、證明與 certificate 需求說明，使用 ARS academic-paper 的 argument-builder 角色組織證據與反例邊界。沒有實作 normal-form/root verifier、執行 frozen 138 inputs／pairs、發放 owner 或 inverse canonical bytes，亦不改 total `delta`／resolved-domain `kappa`、時鐘、方向或 G/I/C 的原契約。

## 1. 固定輸入與沿用的已證語義橋

沿用

\[
\widetilde G=\mathrm{SL}_2(\mathbb Z),\qquad
G=\mathrm{PSL}_2(\mathbb Z),\qquad
\widetilde\Gamma=\left\{\begin{pmatrix}a&b\\c&d\end{pmatrix}\in\widetilde G:
c\equiv0\pmod {11}\right\},\quad
\Gamma=\widetilde\Gamma/\{\pm I\}.
\tag{2}
\]

S、T、U 及其 projective syllables 固定為

\[
S=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\quad
T=\begin{pmatrix}1&1\\0&1\end{pmatrix},\quad
U=ST=\begin{pmatrix}0&-1\\1&1\end{pmatrix},
\qquad \sigma=[S],\quad u=[U].
\tag{3}
\]

[前筆記][normal]自含證明了以下接口，本文按其相同約定使用：

1. \(G=C_2*C_3\)，字母表 \(\{\sigma,u,u^2\}\) 的 reduced words 在兩個因子間交替，且每個元素的 reduced word 唯一。
2. 任意 exact determinant-one 整數矩陣均可由 Euclidean row operations 有限解碼，保留 central sign 與 exact matrix replay。
3. 可有限循環約化，記錄
   \[
   [P]=CwC^{-1},
   \tag{4}
   \]
   其中 w cyclically reduced。對 hyperbolic P，其 syllable 長度 n 為偶數且至少 2。
4. 長度至少 2 的 cyclically reduced words 共軛，當且僅當它們互為 cyclic syllable rotation。若 \(w=AB\)，則 \(A^{-1}wA=BA\)。

所有 word equality 都指有限 syllable 序列的精確相等，不是數值、hash 或未指定 encoding 的相等。syllable 長度也不是 flow period 或幾何長度；本輪不改時鐘。

本文的 P 固定取 \(\operatorname{tr}P>2\) 的 hyperbolic lift。「正跡」消去同一 projective 元素的 \(\pm\) 歧義，但 **不** 在 R、\(R^{-1}\) 之間選方向；方向由 \(P=R^m\)、\(m\ge1\) 決定。

## 2. 三個有限詞引理

### 2.1 Hyperbolic 元素的根仍為 hyperbolic

**引理 1。** 若 \([A]^k=[P]\)、\(k\ge1\)，且 P 為正跡 hyperbolic，則 \([A]\) 也是 hyperbolic。選 A 的正跡 lift 後，有 exact \(A^k=P\)。

**證明。** 任取 determinant-one lift \(A_0\)，有 \(A_0^k=\pm P\)，所以 \(A_0P=PA_0\)。在 P 的實特徵基中，

\[
P=\operatorname{diag}(\lambda,\lambda^{-1}),\quad\lambda>1,
\qquad A_0=\operatorname{diag}(t,t^{-1}),\quad t\in\mathbb R\setminus\{0\}.
\]

這裡矩陣等式表示在該基底下的表示；P 的兩個 eigenvalues 不同，故交換矩陣必為對角。由 \(A_0^k=\pm P\)，有 \(|t|^k=\lambda>1\)，因而 \(|\operatorname{tr}A_0|>2\)。取正跡 lift A 後，兩個 eigenvalues 均為正，故 \(A^k\) 正跡，projective 等式中的負號不可能留下。□

這覆蓋負跡 lift 的偶次冪情形；不以浮點 eigenvalue 計算實作該選擇。

### 2.2 Cyclically reduced 詞的冪無消去

**引理 2。** 若 b cyclically reduced 且長度 \(\ell\ge2\)，則 \(\ell\) 為偶數，對每個 \(k\ge1\)，字面串接 \(b^k\) 已是 cyclically reduced normal form，長度為 \(k\ell\)。

**證明。** 首尾來自不同因子，所以每個 block 邊界仍交替，不發生因子內合併。串接後首尾依然屬不同因子。由唯一 normal form 即得。□

### 2.3 Rotation 不會隱藏重複 block

用 \(\operatorname{rot}_s\) 表示左移 s 個 syllables 的 cyclic rotation，s 以詞長取餘數。

**引理 3。** 對任意非空有限詞 b、長度 \(\ell\)，

\[
\operatorname{rot}_s(b^k)
=\bigl(\operatorname{rot}_r(b)\bigr)^k,
\qquad r\equiv s\pmod\ell,\quad0\le r<\ell.
\tag{5}
\]

**證明。** 寫 \(b=AB\)、\(|A|=r\)。先移去完整的 b blocks 不改循環序列，再移首段 A，結果恰為 \((BA)^k\)。這是字面序列等式，不需先假定群中的 root uniqueness。□

## 3. 固定循環核心的完整 root 判準

**定理 4（指定 exponent）。** 在 (4) 的 hyperbolic 前提下，對每個整數 \(k\ge2\)，以下等價：

\[
\begin{aligned}
&[P]\text{ 在 }G\text{ 中有 k 次根};\\
&k\mid n,\quad \ell=n/k\text{ 為偶數},\quad
w=(w_1\cdots w_\ell)^k
\text{ 作為字面 syllable 序列成立}.
\end{aligned}
\tag{6}
\]

**必要性。** 若 \([P]=[A]^k\)，引理 1 使 A hyperbolic。將其有限循環約化為 \([A]=DbD^{-1}\)，b 的偶數長度至少為 2。由引理 2，\(b^k\) 已 cyclically reduced，且與 w 共軛。沿用 §1 的 cyclic conjugacy 定理，w 是 \(b^k\) 的 rotation。引理 3 再給 \(w=v^k\)，其中 v 為 b 的某個 rotation，故 \(n=k|v|\)，且 v 就是 w 在當前起點的長度 \(n/k\) 前綴。

**充分性。** 若 (6) 成立，v 為該偶長前綴。因 w reduced，v 亦 reduced；偶長與因子交替使其首尾不同，所以 v cyclically reduced。令 \(r=CvC^{-1}\)，則 \(r^k=[P]\)。其 lift 與正跡處理由引理 1 給出。□

這個必要性不能縮成「看起來像重複詞」：關鍵依次為任意根可循環約化、冪無消去、共軛 iff rotation、rotation of power 仍是 power。四步都閉合後，才可只查 fixed-start 前綴。

非平凡重複 block 不可能為奇長：奇長交替詞的首尾在同一因子，重複時其邊界便不 reduced，與 w 的 normal form 矛盾。若 \(\ell=n\)，其偶數性則直接來自 w。

## 4. 最短 block 給出唯一 ambient primitive root

定義非空有限候選集

\[
\mathcal L(w)=\{\ell:2\le\ell\le n,\quad
\ell\mid n,\quad \ell\text{ 偶數},\quad
w=(w_1\cdots w_\ell)^{n/\ell}\}.
\tag{7}
\]

n 本身屬於其中。令

\[
\ell_0=\min\mathcal L(w),\qquad
v=w_1\cdots w_{\ell_0},\qquad
m=n/\ell_0,\qquad r=CvC^{-1}\in G.
\tag{8}
\]

**定理 5。** r 為 P 沿原方向的 ambient primitive root；其正跡 lift R 滿足 exact \(P=R^m\)。m 是可能的正 root exponent 的最大值。

**證明。** 字面 \(w=v^m\) 給 \(r^m=[P]\)，由引理 1 可取正跡 hyperbolic lift。若 \(r=s^j\)、\(j\ge2\)，則 \([P]=s^{jm}\)。定理 4 強迫 w 有偶長重複前綴
\(n/(jm)=\ell_0/j<\ell_0\)，違反 (7) 的最小性。因此 r 不可再開 proper root。任何 \([P]=a^k\) 同樣使 \(n/k\in\mathcal L(w)\)，所以 \(k\le m\)。□

唯一性沿用 [ambient 中心化子引理][coset]：

\[
C_G([P])=\langle r\rangle,
\qquad C_{\widetilde G}(P)=\{\pm R^j:j\in\mathbb Z\}.
\tag{9}
\]

該引理的依據是在實特徵基中 projective 中心化子為一個實一參數對角群；與離散的 G 相交是含 P 的非零離散循環子群。其沿 P 方向的生成元唯一。本輪構造的 r 已證 primitive 且有正冪等於 P，因而正是該生成元，而非真子群的生成元。

### 4.1 必須保留的 exact lift replay

令 \(\widetilde C\) 是 C 的任一固定 determinant-one lift，\(V_w=\operatorname{Eval}(v)\) 使用 (3) 的 S、U、\(U^2\) 相乘。先重建

\[
R_0=\widetilde C V_w\widetilde C^{-1},
\qquad R=\operatorname{sgn}(\operatorname{tr}R_0)R_0.
\tag{10}
\]

引理 1 保證 \(|\operatorname{tr}R_0|>2\)，所以 sign 不會是零。因為 \(S^2=U^3=-I\)，word equality 暫時只給 \(R_0^m=\pm P\)；不能直接把 raw evaluation 當正跡根。正規化後兩邊都是正跡，同一 projective 元素強迫

\[
\boxed{P=R^m,\qquad \det R=1,\qquad\operatorname{tr}R>2.}
\tag{11}
\]

prospective certificate 仍應 exact replay (10)–(11)。正跡理論不代替 input binding、integrality 檢查或矩陣乘法驗證；任何輸入 transcript 未驗證時不能簽發 resolved root。

### 4.2 有限的「不可再開根」證書

對提議的 v，只需驗證其 cyclically reduced 性質、\(w=v^m\)，並對每一個

\[
\ell\mid |v|,\qquad 2\le\ell<|v|,\qquad \ell\text{ 偶數}
\tag{12}
\]

提供一個 exact mismatch，證明 \(v\ne(v_1\cdots v_\ell)^{|v|/\ell}\)。例如記錄某個 index i，驗證
\(v_i\ne v_{1+((i-1)\bmod\ell)}\)。全部有限候選被排除，定理 4 就排除 **所有** proper roots，不是只排除已試過的矩陣。

不需再枚舉所有 rotations：引理 3 已證若任一 rotation 有此完整重複長度，當前起點也有。沒有必要查非因子長度或奇數 block，因為定理 4 已排除它們。

這是一個替代舊 trace recurrence 的數學 root-certificate 來源，不刪除舊方法、不切換既有 implementation。若兩種方法都對相同 exact input 通過，唯一性強迫得到同一正向根；本輪沒有執行任何兩方法比較測試。

### 4.3 改變循環起點不改原矩陣座標中的根

完整重複長度集合對 rotation 不變，故 \(\ell_0,m\) 不變。更具體地，取 \(0\le s<n\)，寫 \(s=t\ell_0+r_s\)、\(0\le r_s<\ell_0\)，再寫 \(v=AB\)、\(|A|=r_s\)。把 w 左移 s 個 syllables 時，被移去的前綴為 \(v^tA\)，新詞為 \((BA)^m\)，(4) 的共軛詞應改成
\(C'=Cv^tA\)。於是

\[
C'(BA)(C')^{-1}
=Cv^t A(A^{-1}vA)A^{-1}v^{-t}C^{-1}
=CvC^{-1}=r.
\tag{13}
\]

這個方向檢查說明不能在旋轉詞後保留舊 C 不變，再聲稱仍在原矩陣座標中得到同一 root。對其他合法 cyclic reduction choices，也可直接由定理 5 的唯一性得到相同 R。

## 5. 十二狀態週期給 subgroup root 與 traversal exponent

R 在 \(\mathbb P^1(\mathbb F_{11})\) 上按矩陣左作用。令

\[
v_0=\infty=[1:0],\qquad
v_{j+1}=\overline Rv_j,\qquad
d=\min\{j\ge1:v_j=v_0\}.
\tag{14}
\]

determinant 1 保證這是 12 個狀態的 permutation。故從起點即為完整 cycle，沒有 transient tail；\(1\le d\le12\)。對所有整數 j，

\[
R^j\in\widetilde\Gamma
\iff\overline R^j\infty=\infty
\iff d\mid j.
\tag{15}
\]

此處 12 是狀態数上界，不表示 d 必須整除 12，也不界定 word decoding 的成本。

**定理 6。** 令 \(P=R^m\) 如定理 5。P 在 \(\widetilde\Gamma\) 當且僅當 \(d\mid m\)。在此條件下，

\[
\boxed{R_\Gamma=R^d,\qquad
P=R_\Gamma^{\nu},\quad\nu=m/d,\qquad
P\text{ 在 }\Gamma\text{ 中本原}\iff\nu=1\iff m=d.}
\tag{16}
\]

**證明。** membership 等價由 (15) 得到。任何 P 的 subgroup root 均交換 P，故由 (9) 其 projective 元素為 r 的整數冪；正冪等於 P 又要求沿同方向。屬於 subgroup 時，(15) 迫使這個冪數被 d 整除。所以 \(r^d\) 是該中心化子與 subgroup 交集的正向生成元，必為 subgroup primitive。正跡 lifts 給出 (16) 的 exact 矩陣等式。□

亦可直接描述全部正跡 subgroup roots：對 \(k\ge1\)，存在正跡 A 滿足
\(A\in\widetilde\Gamma\)、\(A^k=P\)，當且僅當
\(k\mid\nu\)，此時唯一的 A 是 \(R_\Gamma^{\nu/k}\)。這是數學分類，不是實際 row 的 extraction 結果。

如果只拿已知 subgroup primitive \(R_\Gamma\) 代替 R 去做 ambient 中心化子或前筆記的 coset conjugacy 搜尋，仍可能漏掉合法共軛子。詞的最短 block 解答的是 **ambient** primitive，orbit 最小週期 d 才把它轉為 subgroup primitive。

## 6. Level-11 的 hyperbolic 類不與自身逆向共軛

以下重證 [既有不自逆引理][partition]，用於本輪 inverse/root 接口。

**定理 7。** 若 \(P\in\widetilde\Gamma\)、\(\operatorname{tr}P>2\)，則不存在 \([H]\in\Gamma\) 使

\[
[H][P][H]^{-1}=[P]^{-1}.
\tag{17}
\]

**證明。** 任取 \(H\in\widetilde\Gamma\) lift，(17) 提升成
\(HPH^{-1}=\pm P^{-1}\)。因 determinant 1 有
\(\operatorname{tr}P^{-1}=\operatorname{tr}P>2\)，共軛保跡排除負號。

在 P 的實特徵基中，HPH⁻¹=P⁻¹ 強迫 H 交換兩條不同的特徵線。因此 H 的矩陣形如

\[
\begin{pmatrix}0&b_*\\c_*&0\end{pmatrix},
\qquad-b_*c_*=1.
\tag{18}
\]

從而 \(\operatorname{tr}H=0\)、\(H^2=-I\)，這兩個等式與基底無關。在原整數座標寫

\[
H=\begin{pmatrix}a&b\\c&-a\end{pmatrix},\qquad
-a^2-bc=1,\qquad c\equiv0\pmod {11}.
\tag{19}
\]

模 11 因而要求 \(a^2\equiv-1\equiv10\)。但逐一平方 0、1、2、3、4、5，再利用 \((-a)^2=a^2\)，得到所有模 11 平方剩餘恰在
\(\{0,1,3,4,5,9\}\)，不含 10。矛盾。□

這是 exact membership 與 determinant 的代數 obstruction，不依赖搜索失敗，也不要求 P 本原。它不排除 ambient G 中存在 reverser：H 的左下 entry 不滿足 level-11 條件時，(19) 的模 11 矛盾便不成立。本文不把 ambient cyclic-word inverse rotation 默認合併為 subgroup owner 相等。

## 7. 逆向與取根相容，但不自動完成 observed inverse ledger

**推論 8。** 若 \(P=R^m\in\widetilde\Gamma\) 為上述正向 ambient 分解，則

\[
P^{-1}=(R^{-1})^m,\qquad
R_\Gamma(P^{-1})=R^{-d}=R_\Gamma(P)^{-1},\qquad
\nu_\Gamma(P^{-1})=\nu_\Gamma(P).
\tag{20}
\]

**證明。** \(R^{-1}\) 仍是正跡 hyperbolic；若有 proper root，取逆便給 R 的 proper root，矛盾。其正冪等於 \(P^{-1}\)，因此由唯一性就是 inverse input 的正向 ambient 根。\(\overline R^{-1}\) 的 infinity cycle 是 (14) 的反向 cycle，最小返回週期仍為 d。代入定理 6 得 (20)。□

詞層面上，inverse 是將 syllable 順序反轉並逐項取逆：
\(\sigma^{-1}=\sigma\)、\(u^{-1}=u^2\)、\((u^2)^{-1}=u\)。因此
\(w^{-1}=(v^{-1})^m\)，其最短完整重複長度也不變。
**單純 reverse 而不取 syllable inverses 並不等於這個操作。**

對實際的 hyperbolic \(\Gamma\)-conjugacy classes，

\[
\iota(\operatorname{cl}_\Gamma(P))
=\operatorname{cl}_\Gamma(P^{-1})
\tag{21}
\]

是良定 involution，因為共軛與取逆交換；定理 7 說明它沒有 fixed point。primitiveness 也被取逆保持，所以此結論對實際 subgroup primitive classes 同樣成立。

但以下界限不能略過：

- 全 class 空間的無 fixed-point involution，不證明 frozen observed image 在 inversion 下封閉。
- 只有對**已證 inverse-closed 的有限 class 集合**，才可推出它分成兩兩不同的 inverse pairs、cardinality 為偶數。本輪沒有證明觀測集合具此條件，也不改任何 owner count。
- 知道 P 不與 \(P^{-1}\) 共軛，不決定 \(P^{-1}\) 等於哪個另一個 observed owner。宣稱指向 Q 的 inverse link 仍需 \(P^{-1}\sim_\Gamma Q\) 的 exact witness 或完整分類證明。
- (20) 是語義上的 root/inverse 相容，不是 canonical serialization。既有 inverse branches、typed unresolved 與任何需註冊的 theorem/schema binding 均不在本輪修改。

## 8. 一個手算 central-sign 檢查

令 \(V=\begin{pmatrix}1&0\\1&1\end{pmatrix}\)，取 cyclic word

\[
v=(\sigma u)(\sigma u)(\sigma u^2).
\tag{22}
\]

其長度為 6，唯一可能的 proper 偶數因子長度為 2；三個 u 因子 exponent 為 1、1、2，不全相同，故 v 不由長度 2 的前綴重複而成。結合下式的 hyperbolic 檢查，定理 4–5 判定它 ambient primitive。

但 raw matrix evaluation 不是正跡根：

\[
\operatorname{Eval}(v)=(-T)(-T)(-V)
=-\begin{pmatrix}3&2\\1&1\end{pmatrix}=-R_*.
\tag{23}
\]

正跡 lift 為 \(R_*\)，trace 4，且紙面乘法給

\[
P_*=R_*^2=\begin{pmatrix}11&8\\4&3\end{pmatrix},
\qquad\operatorname{tr}P_*=14.
\tag{24}
\]

所以 \(v^2\) 的 raw evaluation 是 \(P_*\)，但取 block 時仍須將 \(-R_*\) 正跡化。這正是偶次冪不能使 sign bookkeeping 消失的例子。P_* 的左下 entry 為 4，不在 level-11 subgroup；此例只檢查 ambient 詞與 lift，未充作 subgroup fixture、frozen row 或任何實驗輸出。

## 9. Prospective 證書鏈與仍待實際完成的工作

若將來要讓本輪定理成為 executable pipeline，至少須綁定並驗證：

1. frozen word／ID 到 exact P、subgroup 與 hyperbolicity predicates，以及群、lift、normal-form 版本。
2. 上輪 Euclidean 與 cyclic reduction transcript，精確 (4) 及 central signs。
3. \(w=v^m\)、v 的 cyclic reduction、(12) 全部 proper block 長度的 mismatch witnesses，以及 (10)–(11) 的 exact powering。
4. 模 11 的狀態規則；\(v_0,\ldots,v_{d-1}\) 互異、每條 successor、\(v_d=v_0\)；\(d\mid m\) 與 (16) 的 exact replay。
5. 實際代表之間的 attachment／separation、inverse targets、population coverage 與 canonical encoding；定理 7 的前提和版本也需獨立 binding。

每個列表都是有限的數學需求。缺少實際 binding、verifier 或執行記錄，不能因本筆記證明「存在終止判準」而將未處理 rows 改為 resolved。本輪沒有輸出實際 primitive-owner partition、canonical bytes、138-row replay、9453-pair audit 或 G/I/C。

## 10. 實際讀取、核對與保全

本輪完整讀取當前 `AGENTS.md`、`docs/workflow.md`、ARS 0.1.28 router、academic-paper workflow 與 argument-builder role。只讀前 normal-form 筆記全文、finite-coset 的中心化子／root／週期段落，以及 certified-partition 的既有 inverse 引理定位。新增推導自含，不需要本輪新外部來源；未重新取得或截圖此前有提取限定的 Conrad PDF，也未重試任何舊失敗來源通道。

紙面核對包括：根與 P 的 exact commutation；偶長 concatenation 無消去；(5) 對所有 rotation 起點的窮盡性；最短 block 排除 proper roots；正跡不等於方向；(13) 的 conjugating-word 更新；d 的最小完整 cycle；逆向 reverser 的 trace 0／square \(-I\)；模 11 平方排除；root/inverse 相容；以及 (23)–(24) 的手算 signs、determinant、trace。

Filesystem 檢查僅用讀取、搜尋、存在性與 SHA-256；唯一寫入是 `apply_patch` 新增本筆記。讀取時相關舊文件 SHA-256 為：

- normal-form 筆記：`28f6e75b62598c3ff2638dca3458550c06bcb6774b8249e269cdec7499ef692e`；
- finite-coset 筆記：`a5b6344017fb6d04ea999ff1ba311eed87e20ba13a2f455c2930e9d696c3ffd1`；
- certified-partition 筆記：`4462f9f6bf88bf5de0aa4cc27da3ba7210911e812f3387adaf9a5abb324dd946`；
- round6 原文：`4bc1a960b5527a5d389b5c70e29fa0dc7b3199b93a808dd3f347616dd686d1a3`。

這些只作來源身分與未修改檢查，不代替既有鎖定回執或科學驗證。本輪未運行科學／符號程式、矩陣實驗、producer、fixture、歷史 artifact writer、Git 修復或正式稿 build；舊筆記、正式稿、code、inputs、experiments/results、receipts、失敗記錄及正式 Stage／Route 邊界保持不變。

[normal]: internal_ambient_normal_forms_and_conjugacy_certificates_20260908.md
[coset]: internal_finite_coset_conjugacy_reduction_20260908.md
[partition]: internal_certified_partition_and_gic_descent_20260908.md
