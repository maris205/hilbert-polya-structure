# P31：把子群共軛化為 ambient 共軛與有限射影軌道

日期：2026-09-08。狀態：**內部有界理論增量；未執行 frozen population，非正式稿、非複審回執、非 Route 變更。**

## 0. 本輪結果與適用邊界

承接 [有限分割與 G/I/C 筆記](internal_certified_partition_and_gic_descent_20260908.md) 的 hyperbolic 中心化子和 exact root recurrence。本輪補上一個具體的子群非共軛證書來源：

> 若正跡 hyperbolic 矩陣 \(P,Q\in\Gamma_0(11)\) 已有 exact ambient 共軛子 \(H_0PH_0^{-1}=Q\)，且 \(R\) 是 P 在 \(\mathrm{PSL}_2(\mathbb Z)\) 中的正向本原根，則 P、Q 在 \(\Gamma_0(11)\) 中共軛，當且僅當 \(H_0^{-1}\infty\) 落在 \(R\) 對 \(\mathbb P^1(\mathbb F_{11})\) 的 \(\infty\)-軌道。

這個軌道至多有 12 個不同狀態。命中給出精確正 witness；一個經驗證的完整閉合週期且不含目標，給出真正的負 witness，不是「搜尋共軛子失敗」。關鍵是使用 **ambient primitive root**，而不是已知的 subgroup primitive owner。

本筆記也給出兩個手算構造：一個 ambient 共軛但 subgroup 不共軛的例；一個說明錯用 subgroup root 會產生假陰性的例。它們不是 138 個 frozen inputs 的執行结果，也不是註冊 fixture suite。流、時鐘、方向、Hecke/period/zeta 正規化與 [round6 原文](stage4_prime_revision_round6.tex) 的 total `delta`／resolved-domain `kappa` 契約均不改變。

工作方式沿用 ARS academic-paper 的 argument-builder 角色，僅作自含命題、證明、反例與界限說明。沒有啟動正式論文流程、producer、科學程式、實驗或 canonicalization 執行。

## 1. 固定 lift、作用方向與十二個狀態

記

\[
\widetilde G=\mathrm{SL}_2(\mathbb Z),\qquad
G=\mathrm{PSL}_2(\mathbb Z),\qquad
\widetilde\Gamma=\{M\in\widetilde G:M_{21}\equiv0\pmod {11}\},
\qquad\Gamma=\widetilde\Gamma/\{\pm I\}.
\tag{1}
\]

以下 P、Q 是 \(\widetilde\Gamma\) 中跡大於 2 的 hyperbolic 矩陣。它們是相關 projective 元素的唯一正跡 lifts。若要處理 P31 primitive-owner 相等，先對實際輸入作 **subgroup** 取根，再把所得 P、Q 放入本定理；不同 traversal powers 的原始矩陣不應直接拿來替代 owner。

令

\[
\mathcal S=\mathbb P^1(\mathbb F_{11})
=\{\infty\}\sqcup\mathbb F_{11},
\qquad \infty=[1:0],\quad z=[z:1].
\tag{2}
\]

矩陣使用左作用

\[
\begin{pmatrix}a&b\\c&d\end{pmatrix}[x:y]
=[ax+by:cx+dy].
\tag{3}
\]

所有運算在模 11 下進行。determinant 為 1，所以這是 12 個狀態的 permutation；\(M\) 與 \(-M\) 的作用完全相同。尤其

\[
[M]\in\Gamma\iff \overline M\,\infty=\infty
\iff M_{21}\equiv0\pmod {11}.
\tag{4}
\]

在 finite chart 上，(3) 是 \(z\mapsto(az+b)/(cz+d)\)；分母為零時值為 \(\infty\)，不能把它當成未定義或丟棄。對 infinity 則用第一欄 \([a:c]\)，不作浮點除法。

這個 action 是 transitive：取

\[
S=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
T=\begin{pmatrix}1&1\\0&1\end{pmatrix},
\]

則 \(T^zS\infty=z\)。其 stabilizer 正是 \(\Gamma\)，因此 cosets \(g\Gamma\mapsto g\infty\) 給出 \([G:\Gamma]=12\)。這是直接的作用證明；Sage 官方文件的 \(\Gamma_0(N)\) index 公式亦給出 \(11(1+1/11)=12\)，僅作外部背景核對，不代替後面的共軛證明。[Sage 官方 Gamma0 文件：index](https://doc.sagemath.org/html/en/reference/arithgroup/sage/modular/arithgroup/congroup_gamma0.html#sage.modular.arithgroup.congroup_gamma0.Gamma0_class.index)

## 2. Ambient 中心化子：為什麼一個整數參數已包含所有共軛子

**引理 1。** 對正跡 hyperbolic \(P\in\widetilde G\)，有唯一沿 P 正方向的 ambient primitive \([R]\in G\) 及唯一 \(e\ge1\)，使 \([P]=[R]^e\)，且

\[
C_G([P])=\langle[R]\rangle.
\tag{5}
\]

取 R 的正跡 lift 後，\(P=R^e\) 是精確矩陣等式。矩陣中心化子為

\[
C_{\widetilde G}(P)=\{\pm R^n:n\in\mathbb Z\}.
\tag{6}
\]

**證明。** 前筆記的中心化子論證只用 discrete subgroup 性質，故對 G 同樣成立：在 P 的兩條實特徵線基底中，\(C_{\mathrm{PSL}_2(\mathbb R)}([P])\) 是正對角一參數群，與 \((\mathbb R,+)\) 同構。與 G 的交集為含 P 的非零離散子群，因而無限循環；與 P 同方向的生成元給出 R。任何正根都在此中心化子內，所以本原根與 e 唯一。

若矩陣 lift 原本為負跡，改取其負號；正跡 hyperbolic lift 的兩個特徵值均為正，正冪仍為正跡。於是 projective 等式不能提升成 \(P=-R^e\)，必為正號。這也涵蓋偶次冪原本可寫成負跡根之冪的情形。反過來，projective 中心化關係提升後若有 \(MPM^{-1}=-P\)，取跡立即矛盾；故 (5) 提升為 (6)。□

**引理 2（全部共軛子）。** 若 \(H_0\in\widetilde G\) 滿足

\[
H_0PH_0^{-1}=Q,
\tag{7}
\]

則所有 \(\widetilde G\) 中將 P 共軛至 Q 的矩陣恰為

\[
\{\pm H_0R^n:n\in\mathbb Z\}.
\tag{8}
\]

**證明。** H 也满足 (7)，當且僅當 \(H_0^{-1}H\) 與 P 交換；代入 (6) 即得。若輸入的是 projective 共軛 witness，正跡 P、Q 排除 \(H_0PH_0^{-1}=-Q\)，故仍得到精確 (7)。不要求 H 或 \(H_0\) 自身為正跡或 hyperbolic，例如 S 是合法的零跡 ambient 共軛子。□

注意 (8) 是 **右乘** \(R^n\)。一般不能在公式中把它改成 \(R^nH_0\) 而仍使用 P 的中心化子；這會改錯後續 orbit target。

## 3. 核心定理：子群共軛的有限軌道判準

令 \(\overline R\) 表示 R 的模 11 projective action，並設

\[
v_0=\infty,\qquad v_{j+1}=\overline R v_j,
\qquad y=\overline{H_0}^{-1}\infty.
\tag{9}
\]

令 h 是 \(v_h=v_0\) 的最小正整數。

**定理 3（十二狀態共軛下降）。** 在 (1)、(5)、(7) 的已驗證前提下，\(1\le h\le12\)，且

\[
\boxed{P\sim_\Gamma Q
\iff y\in\{v_0,\ldots,v_{h-1}\}.}
\tag{10}
\]

若 \(y=v_j\)，\(0\le j<h\)，則

\[
H=H_0R^j\in\widetilde\Gamma,
\qquad HPH^{-1}=Q.
\tag{11}
\]

若 y 不在這個完整週期中，則不存在 subgroup 共軛子。

**證明。** \(\overline R\) 是 finite permutation，故 infinity 的前向軌道從起點便是週期，沒有暫態尾巴。若首次重複為 \(v_i=v_j\)、\(0\le i<j\)，可乘 \(\overline R^{-i}\) 得 \(v_0=v_{j-i}\)，所以最遲 12 次轉移必回到 \(v_0\)。負整數冪亦落在同一 h-cycle，不需另作無限負向搜尋。

由 (4)、(8)，subgroup 共軛子存在，當且僅當某個 n 满足

\[
\overline{H_0}\,\overline R^n\infty=\infty
\iff \overline R^n\infty=\overline{H_0}^{-1}\infty=y.
\tag{12}
\]

把 n 對 h 取餘數即得 (10)，命中時由相同等式得 (11)。無命中排除的是 (8) 的**全部**共軛子，而不是只排除已嘗試的有限矩陣。\(\pm\) 在 action、membership 與共軛作用中均不改變結果。□

12 是不同狀態數的上界，不表示 h 必須整除 12；§7 給出 \(h=5\) 的例。選別的 ambient witness 也不影響 verdict：若 \(H_1=\pm H_0R^a\)，則新 target 為 \(\overline R^{-a}y\)，它落在 infinity 軌道與否與 y 相同。

### 3.1 正、負證書的必要內容

一個 prospective finite-coset certificate 應至少綁定 exact P、Q、\(H_0\)、R、e、群與 lift 版本，以及：

1. determinant、integrality、P/Q subgroup membership、hyperbolicity、正跡與 exact (7)；
2. exact \(P=R^e\) 和 R 在 **ambient G** 中的 primitiveness；
3. 模 11 target y 的計算與 action 規則；
4. 對 positive branch，命中的 j 以及 (11) 的 exact matrix replay；
5. 對 negative branch，\(v_0,\ldots,v_{h-1}\) 的互異性、每個 successor、\(v_h=v_0\)，以及 y 缺席。

第 5 項給定一個 cycle closure 就已窮盡全部整數冪，不需要 producer 宣稱「已搜尋足夠久」。但缺少第 2 項時，這個 cycle 可能只覆蓋真實中心化子的真子群，從而不能作 negative certificate。數值近似、重複狀態比較或 hash 一致性均不能替代 exact field/matrix predicates。

## 4. Ambient root 可以用有限整數遞迴確證

保留前筆記的遞迴

\[
\begin{aligned}
s_0(t)&=2,&s_1(t)&=t,&s_{m+1}(t)&=t s_m(t)-s_{m-1}(t),\\
q_0(t)&=0,&q_1(t)&=1,&q_{m+1}(t)&=t q_m(t)-q_{m-1}(t).
\end{aligned}
\tag{13}
\]

對 trace t、determinant-one 矩陣 A，

\[
\operatorname{tr}(A^m)=s_m(t),\qquad
A^m=q_m(t)A-q_{m-1}(t)I.
\tag{14}
\]

給定正跡 hyperbolic B、\(T_B=\operatorname{tr}B\)，任何 proper positive root \(B=A^m\) 都在有限候選範圍

\[
2\le m\le M(T_B):=\max\{r\ge1:s_r(3)\le T_B\},
\quad 3\le t\le T_B,
\quad s_m(t)=T_B,
\tag{15}
\]

且被迫等於

\[
A_{m,t}=\frac{B+q_{m-1}(t)I}{q_m(t)}.
\tag{16}
\]

ambient primitiveness 的 finite verifier 逐候選重建 (15)，檢查 (16) 的 integrality、determinant 1、trace \(t>2\) 與 exact powering。相較前筆記的 subgroup primitive check，**唯一刪除的 membership 条件是左下 entry 可被 11 整除**；不能把它保留後就聲稱已證 ambient primitive。

(15) 的窮盡性直接來自正跡 root 的整數 trace 至少為 3、\(s_m(t)\) 在 \(t\ge3\) 上單調，以及 (14)。負跡 lift 與偶次冪由引理 1 的正規化覆蓋。所有截止均以整數遞迴決定，不依浮點 log。

因此一份 R,e 證書只要驗證 \(P=R^e\) 並用上述有限方法排除 R 的 ambient proper roots，就足以供定理 3 使用。若談數學上的 extraction，可對 P 的有限候選加上 \((m,A)=(1,P)\)，選最大通過 exponent；若其根仍有 proper root，組合後會給更大通過 exponent，矛盾。這證明有限 extraction 的存在，不宣稱其效率、程式實作或 frozen input 執行。

## 5. Ambient exponent 與 subgroup exponent 的精確關係

仍令 \(P=R^e\in\widetilde\Gamma\)，h 為 (9) 的 infinity orbit length。由 (4)，

\[
\langle[R]\rangle\cap\Gamma=\langle[R]^h\rangle,
\qquad h\mid e.
\tag{17}
\]

**推論 4。** P 的 subgroup 正向本原根是 \(R^h\)，其 subgroup traversal exponent 是 \(e/h\)。尤其

\[
P\text{ 在 }\Gamma\text{ 中本原}\iff e=h.
\tag{18}
\]

**證明。** \(R^n\in\widetilde\Gamma\iff v_n=\infty\iff h\mid n\)，故得 (17)。若 \(R^h\) 在 subgroup 中有 proper root，該根交換 P，必為 ambient 中心化子的 \(R^a\)；其屬 subgroup 又要求 \(h\mid a\)，不可能正冪等於 \(R^h\)。因此 \(R^h\) 本原，而 \(P=(R^h)^{e/h}\)。□

這提供了另一種 exact subgroup-root 介面，也揭示為什麼「owner 已經本原」不容許在 (8) 中把 R 改成 P：owner 的本原性所屬群是 \(\Gamma\)，不是 G。

## 6. 手算負證書：ambient 共軛不代表 level-11 共軛

取

\[
P=\begin{pmatrix}1&11\\11&122\end{pmatrix},
\qquad H_0=S=\begin{pmatrix}0&-1\\1&0\end{pmatrix},
\qquad Q=\begin{pmatrix}122&-11\\-11&1\end{pmatrix}.
\tag{19}
\]

直接算得 \(\det P=122-121=1\)、\(\det Q=1\)、两者 trace 123，且

\[
SPS^{-1}=Q=P^{-1}.
\tag{20}
\]

P、Q 在 \(\widetilde\Gamma\)，但 S 不在；只知道 S 不在 subgroup 尚不足以推出非共軛，必須排除其他 ambient 共軛子。

### 6.1 先證 P ambient primitive

若 \(P=A^m\)，取 A 的正跡 lift 並令 \(t=\operatorname{tr}A\ge3\)。由 (14) 的非對角 entries，\(q_m(t)\) 必整除 11。

- \(m\ge4\)：\(q_m(t)\ge q_m(3)\ge q_4(3)=21>11\)，不可能。
- \(m=2\)：\(q_2(t)=t\)，故只能 \(t=11\)，但 \(s_2(11)=11^2-2=119\ne123\)。
- \(m=3\)：\(q_3(t)=t^2-1\ge8\)，要整除 11 只能等於 11，導致 \(t^2=12\)，沒有整數解。

所用下界可由 \(q_1=1,q_2=t\) 與遞迴直接歸納：對 \(t\ge3\)，\(q_m(t)\) 隨 m 嚴格增加，並且隨 t 不減。例如後者亦由
\(q_m(t)=\lambda^{m-1}+\lambda^{m-3}+\cdots+\lambda^{-(m-1)}\)、\(\lambda=(t+\sqrt{t^2-4})/2>1\) 的成對項得到。因此所有 \(m\ge2\) 已排除，P 在 ambient G 中本原，R=P、e=1。

### 6.2 一個狀態就完成負證書

P 模 11 為 I，所以

\[
\mathcal O_R(\infty)=\{\infty\},\qquad h=1,
\qquad y=S^{-1}\infty=0.
\tag{21}
\]

target 不在完整閉合軌道內。定理 3 因而證明 \(P\not\sim_\Gamma Q\)，但 (20) 已證 \(P\sim_GQ\)。這與前筆記的 level-11 不自逆引理一致；本輪給出的是可重播的 finite-coset obstruction，不以該舊引理代替 (21) 的證明。

## 7. 手算防錯例：使用 subgroup primitive 元素仍可能漏掉共軛子

取

\[
R_0=\begin{pmatrix}2&1\\1&1\end{pmatrix},\qquad
P_0=R_0^5=\begin{pmatrix}89&55\\55&34\end{pmatrix}.
\tag{22}
\]

\(R_0\) 的 trace 是 3，任何 proper positive root 的二次或更高次冪 trace 至少 \(s_2(3)=7\)，故 \(R_0\) ambient primitive。模 11 使用 \(z\mapsto(2z+1)/(z+1)\) 得

\[
\infty\longmapsto2\longmapsto9\longmapsto3
\longmapsto10\longmapsto\infty.
\tag{23}
\]

例如 \(5/3=9\)、\(19/10=3\)、\(7/4=10\pmod {11}\)；最後一步分母為零。五個狀態互異，故 h=5。由 (22)、(18)，P₀ 是 **subgroup primitive**，但其 ambient exponent 是 5。

令 \(Q_0=P_0\)、\(H_0=R_0^{-1}\)。這是合法 ambient 共軛 witness，但 \(H_0\notin\widetilde\Gamma\)。正確 target 為 \(R_0\infty=2\)，在 (23) 的 j=1 命中，得到

\[
H_0R_0=I\in\widetilde\Gamma.
\tag{24}
\]

若誤用 P₀ 取代 R₀，則 \(P_0\) 的 infinity 軌道只有 \(\infty\)，反而會將這個與自身共軛的例判成負例。這精確說明 ambient primitive certificate 是負分支的必要邏輯前提，而非僅改善效率的選項。

## 8. 同一 ambient class 在子群中的分裂：有限狀態解釋

這一節給出與定理 3 相同機制的全 class 版本，限於一個固定 ambient hyperbolic class。對 \(A\in\widetilde G\)，設其正向 ambient primitive root 為 R。定義

\[
\operatorname{Fix}(\overline A)
=\{x\in\mathcal S:\overline A x=x\}.
\tag{25}
\]

R 交換 A，故 \(\overline R\) 保持這個 fixed-point set。

**命題 5。** A 的 ambient conjugacy class 中，落在 \(\Gamma\) 的元素之 subgroup conjugacy classes，與

\[
\operatorname{Fix}(\overline A)/\langle\overline R\rangle
\tag{26}
\]

自然一一對應。特別地，此 ambient class 在 \(\Gamma\) 中至多分成 12 個 classes。

**證明。** 寫 \(Q_g=gAg^{-1}\)。由 (4)，\(Q_g\in\Gamma\iff x_g=g^{-1}\infty\in\operatorname{Fix}(\overline A)\)。G 在 \(\mathcal S\) 上 transitive，所以每個 fixed point 都有如此代表。若 \(Q_g,Q_h\) subgroup 共軛，则某個 \(\gamma\in\Gamma\) 滿足 \(h^{-1}\gamma g\in C_G(A)=\langle R\rangle\)，即 \(\gamma=hR^n g^{-1}\)。由 (4)，這等價於 \(\overline R^n x_g=x_h\)。反方向同式構造 \(\gamma\)，所以恰為 (26) 的 orbit equivalence。□

對 (19) 的手算 A=P，\(\overline A=\overline R=I\)，故 (26) 恰有 12 個 singleton orbits。這個**手造 ambient class** 因而恰分成 12 個 subgroup classes，而且 P ambient primitive 使其所有共軛代表也 subgroup primitive。可選 \(g_\infty=I\)、\(g_z=ST^{-z}\) 作代表，因 \(g_z^{-1}\infty=z\)。這是該例的代數推論，不是 frozen population 的 owner count、全局 geodesic census 或 138-input 結果。

## 9. 與 finite partition 契約的接合及尚未完成項

前筆記的 `Attach + Separate` 定理中，一對代表的 separation 現在可來自下列分支：

| 已有證據 | 本輪允許的處置 | 不允許的推論 |
| --- | --- | --- |
| 正確 ambient nonconjugacy 證書 | subgroup nonconjugacy | ambient solver timeout 不等於此證書 |
| exact ambient H₀，加 ambient root 與完整 orbit 命中 | subgroup conjugacy，輸出 (11) | H₀ 本身不在 subgroup 不能直接否決 |
| exact ambient H₀，加 ambient root 與完整 orbit 缺席 | subgroup nonconjugacy，輸出 closed-cycle obstruction | 只掃到若干不重複狀態、尚未閉合，不能作負例 |
| 缺少 root、版本、input binding 或 ambient 判定 | typed unresolved | 不可依期待 owner count 選 branch |

這使 subgroup refinement 不再需要無界枚舉 \(\Gamma\) 共軛子：**在 ambient 決策與 exact witness 已閉合後**，追加的 membership 搜尋由最多 12 個狀態完全控制。但這不是從無到有的完整 owner canonicalizer：

- 本文沒有指定、實作或驗證 ambient \(\mathrm{PSL}_2(\mathbb Z)\) 共軛演算法及其 negative certificate 語言。一般不同 trace 可直接排除；trace 相同仍不能推断 ambient 共軛。
- frozen words 到 exact matrices、subgroup root/traversal、theorem/schema binding、independent verifier 與 inverse-owner links 仍需各自閉合。
- 一個 pair 的 exact negative certificate 不建立所有 input IDs 的 coverage，也不自動建立 deterministic canonical bytes；前筆記對 finite-local labels 與跨人口 canonical forms 的區別繼續有效。
- 沒有執行 `delta`、138-input replay、9453-pair audit 或 G/I/C；任何 unresolved 仍禁止完整 estimands。派生 pair audit 不因本定理而取消。

## 10. 實際檢查與保全記錄

本輪實際只讀當前 `AGENTS.md`、`docs/workflow.md`、ARS router/argument-builder 指令及前筆記 §§4–5；沿用同一已完整讀取的 academic-paper workflow。普通公開瀏覽僅核對 Sage 官方 `Gamma0(N).index()` 段落，沒有 API、資料上傳、受限通道繞行或外部模型。

局部數學核對包括：\(\pm\) lifts、右乘中心化子與 target 方向、infinity 的 projective encoding、完整 permutation cycle 覆蓋負冪、ambient/root 群別、例 (19) 的 determinant/trace/共軛與三類 proper-root 排除、例 (22) 的五步 cycle 與正 witness，以及 (26) 的兩個方向。所有例均為文字內手算證明；未運行矩陣、owner、數值或實驗程式。

唯一 filesystem 寫入是以 `apply_patch` 新增本筆記。讀取時，前筆記 SHA-256 為 `4462f9f6bf88bf5de0aa4cc27da3ba7210911e812f3387adaf9a5abb324dd946`，round6 原文為 `4bc1a960b5527a5d389b5c70e29fa0dc7b3199b93a808dd3f347616dd686d1a3`；它們只用於本輪來源身分與未修改檢查，不替代既有 input lock 或科學回執。

本筆記沒有宣稱發表新穎性、formal proof checker 接受、可執行 certificate pipeline、實際 owner classification 或 Route 晉級。舊文件、科學 code、experiments/results、正式稿與所有歷史回執均保持只讀。
