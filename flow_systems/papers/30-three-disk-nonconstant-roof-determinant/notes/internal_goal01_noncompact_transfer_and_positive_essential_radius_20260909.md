# P30 goal01：全 Hölder 空間上的非緊轉移算子與正本質譜半徑

日期：2026-09-09 UTC。主線已核對前一只讀輪的分區差商與常數，並明確授權僅新增本獨立筆記。只保存紙面證明，不改舊筆記、現稿、程式、資料、歷史、鎖定輸入或正式狀態。

## 1. 固定物件、結論及證據範圍

沿用[正一側 roof 筆記][roof]的原固定全空間、范數與算子：

\[
\begin{gathered}
\Sigma^+=\{x\in\{1,2,3\}^{\mathbb N_0}:x_j\ne x_{j+1}\},\qquad
d_\theta^+(x,y)=\theta^{N(x,y)},\\
\mathcal B_\beta=C^\beta(\Sigma^+,d_\theta^+;\mathbb C),\qquad
\|u\|_\beta=\|u\|_\infty+[u]_\beta,\qquad q=\theta^\beta\in(0,1),\\
g\in C^\beta(\Sigma^+;\mathbb R),\quad 2a\le g\le10a,\quad
G=[g]_\beta,\qquad
(\mathcal L_su)(x)=\sum_{j\ne x_0}e^{-sg(jx)}u(jx).
\end{gathered}
\tag{1}
\]

N 是第一個分歧位置，相同點的距離定為零。a 是原三盤半徑，單位飛行速率和正代表 g 均不改變。上游已證所有複參數 s 的 \(\mathcal L_s\) 在同一 \(\mathcal B_\beta\) 上有界。

對每個固定 \(s\in\mathbb C\)，令

\[
t=\operatorname{Re}s,\qquad
M_t=\max_{x\in\Sigma^+}(t g(x)),\qquad
D=\frac{Gq}{1-q},\qquad C_s=\max\{1,|s|D\}.
\tag{2}
\]

本頁證明，對所有 n≥1，

\[
\boxed{
\|\mathcal L_s^n\|_{\rm ess}
\ge\frac{(q e^{-M_t})^n}{2C_s}>0,\qquad
r_{\rm ess}(\mathcal L_s)\ge q e^{-M_t}>0.
}
\tag{3}
\]

因此每個 \(\mathcal L_s^n\) 都非緊。此處本質范數及本質譜半徑只取傳統緊算子理想／Calkin 定義，與上游 §6 的口徑一致。

ARS 有限 argument-builder 指引在此用於分開局部右逆、柱內／跨邊界差商、緊理想論證及 determinant 限定。本頁是內部紙面推導，不是形式化驗證、外部獨立再現或新穎性認證。

## 2. 閉无限維子空間與有界投影

令

\[
E=\{u\in\mathcal B_\beta:u=0\text{ 於 }[1]^c\},\qquad
P f=\mathbf1_{[1]}f.
\tag{4}
\]

同在 \([1]\) 的兩點以 \([f]_\beta\) 控制；一點在 \([1]\)、另一點不在時首個分歧位置為零，距離為 1；同在外部時差為零。因此

\[
\|Pf\|_\infty\le\|f\|_\infty,\qquad
[Pf]_\beta\le\max\{[f]_\beta,\|f\|_\infty\},\qquad
\|P\|_{\mathcal B_\beta\to E}\le2.
\tag{5}
\]

P 是投影，E 為其閉像，使用繼承自 \(\mathcal B_\beta\) 的范數。E 无限維：合法柱集 \([1(21)^k3]\)、k≥0，彼此不交；每個柱集示性函數均為 Hölder 函數，且這些示性函數線性無關。

對 u∈E，將 \([1]\) 內任一點與一個首字母不為 1 的點比較，還有

\[
\boxed{\|u\|_\infty\le[u]_\beta\qquad(u\in E).}
\tag{6}
\]

這項支集性質將用於統一柱內及跨邊界的差商。

## 3. 單分支局部右逆的精確等式

對每個 n≥1，固定一個內部合法、長度 n、末字母不為 1 的詞 \(w_n\)。例如取字母 2、3 交替的長度 n 前綴即可；所有選擇與 s 無關。令

\[
C_n=[w_n1],\qquad
(R_{n,s}u)(y)=\mathbf1_{C_n}(y)e^{sS_ng(y)}u(\sigma_+^ny),
\qquad u\in E.
\tag{7}
\]

§4 將直接證明 \(R_{n,s}:E\to\mathcal B_\beta\) 有界。迭代 (1) 的有限分支公式給

\[
(\mathcal L_s^n R_{n,s}u)(x)
=\sum_{\sigma_+^ny=x}e^{-sS_ng(y)}
 \mathbf1_{C_n}(y)e^{sS_ng(y)}u(x).
\tag{8}
\]

若 \(x_0=1\)，其中恰有 y=\(w_nx\) 一個分支保留；由末字母條件，此分支合法，兩個指数權重相消。若 \(x_0\ne1\)，所有示性函數為零，而 u(x) 也為零。因此

\[
\mathcal L_s^nR_{n,s}u=u
\quad\text{作為 }E\hookrightarrow\mathcal B_\beta\text{ 的嵌入等式},
\qquad
\boxed{P\mathcal L_s^nR_{n,s}=I_E.}
\tag{9}
\]

這只是在 E 上建立局部右逆；沒有聲稱 \(\mathcal L_s^n\) 在整個空間可逆，也沒有聲稱 \(R_{n,s}\mathcal L_s^n=I\)。

## 4. 分區范數估計：只出現一個 \(q^{-n}\)

固定 \(s,n,u\)，寫 \(a_u=\|u\|_\infty\)、\(b_u=[u]_\beta\)，由 (6) 有 \(a_u\le b_u\)。無論 t 正負，都有

\[
tS_ng(y)\le nM_t,\qquad
\|R_{n,s}u\|_\infty\le e^{nM_t}a_u.
\tag{10}
\]

尤其當 t<0 時，\(M_t=t\min g\)，不是 \(t\max g\)，也不需要改成 \(|M_t|\)。

### 4.1 兩點都在支集柱內

若 \(y,z\in C_n\)，則 N(y,z)≥n+1。移位後的距離恰縮放為
\(d_\theta^+(\sigma_+^ny,\sigma_+^nz)^\beta
=q^{-n}d_\theta^+(y,z)^\beta\)。
且

\[
|S_ng(y)-S_ng(z)|
\le G\sum_{j=0}^{n-1}q^{-j}d_\theta^+(y,z)^\beta
=D(q^{-n}-1)d_\theta^+(y,z)^\beta.
\tag{11}
\]

對任意實數 A、B，沿實線段積分指数的導數，得

\[
|e^{sA}-e^{sB}|
\le |s|\,|A-B|\max\{e^{tA},e^{tB}\}.
\tag{12}
\]

這一式不要求 t≥0。對 \(A=S_ng(y), B=S_ng(z)\) 使用 (10)–(12)，再將乘積差分成 u 的差和指数權的差，柱內差商至多

\[
e^{nM_t}q^{-n}
\bigl(b_u+|s|D(1-q^n)a_u\bigr).
\tag{13}
\]

### 4.2 跨 cutoff 邊界與柱外

若 \(y\in C_n,z\notin C_n\)，則首個分歧位置 k≤n，因此
\(d_\theta^+(y,z)^\beta=q^k\ge q^n\)。
不比較柱外的指数權，而直接使用 \(R_{n,s}u(z)=0\)，得到

\[
\frac{|R_{n,s}u(y)-R_{n,s}u(z)|}{d_\theta^+(y,z)^\beta}
\le e^{nM_t}q^{-n}a_u
\le e^{nM_t}q^{-n}b_u.
\tag{14}
\]

這已被 (13) 控制。兩點都在柱外時，差為零。

### 4.3 合併及 \(n\)-無關常數

由 (10)、(13)–(14)，

\[
\|R_{n,s}u\|_\beta
\le e^{nM_t}q^{-n}
\left(b_u+
\bigl[q^n+|s|D(1-q^n)\bigr]a_u\right).
\tag{15}
\]

中括號係數是 1 與 \(|s|D\) 的凸組合。因此

\[
\boxed{\|R_{n,s}\|_{E\to\mathcal B_\beta}
\le C_s e^{nM_t}q^{-n},
\qquad C_s=\max\{1,|s|D\}.}
\tag{16}
\]

C_s 允許依賴 s、固定 g 和空間，但不依賴 n、所選合法詞或 u。粗常數 \(1+|s|D\) 亦可使用。證明不能用 cutoff、指数和移位函數的三個全局范數機械相乘；那會帶入不必要的額外 \(q^{-n}\)，而 (13)–(14) 只損失一次。

## 5. 緊理想、所有冪非緊及正本質譜半徑

對任意 Banach 空間 X，記 \(\mathcal K(X)\) 為緊算子理想，並定義

\[
\|T\|_{\rm ess}
=\inf_{K\in\mathcal K(X)}\|T-K\|.
\tag{17}
\]

无限維 E 上有 \(\|I_E\|_{\rm ess}=1\)：零緊算子給上界 1；若緊算子 K 滿足 \(\|I_E-K\|<1\)，則 K 由 Neumann 級數可逆，於是 \(I_E=K^{-1}K\) 緊，與无限維 Banach 空間單位球非緊矛盾。

任取 \(K\in\mathcal K(\mathcal B_\beta)\)。有界算子與緊算子的複合仍緊，所以 \(PKR_{n,s}:E\to E\) 緊。由 (9)，

\[
\begin{aligned}
1
&\le\|I_E-PKR_{n,s}\|\\
&=\|P(\mathcal L_s^n-K)R_{n,s}\|\\
&\le2C_s e^{nM_t}q^{-n}\|\mathcal L_s^n-K\|.
\end{aligned}
\tag{18}
\]

對 K 取下確界便得

\[
\boxed{\|\mathcal L_s^n\|_{\rm ess}
\ge\frac{(q e^{-M_t})^n}{2C_s}>0.}
\tag{19}
\]

所以每個正整數冪都非緊。僅需定性結論時，也可直接從 (9) 看出：若 \(\mathcal L_s^n\) 緊，則 \(I_E=P\mathcal L_s^nR_{n,s}\) 緊，矛盾。

本頁採 \(\mathcal B(\mathcal B_\beta)/\mathcal K(\mathcal B_\beta)\) 的 Calkin Banach 代數；\(r_{\rm ess}\) 是其中等價類的譜半徑。商映射保持乘法，因此 quotient 中的 Gelfand 譜半徑公式給

\[
r_{\rm ess}(\mathcal L_s)
=\lim_{n\to\infty}\|\mathcal L_s^n\|_{\rm ess}^{1/n}
\ge q e^{-M_t}>0.
\tag{20}
\]

這是與上游相同的緊算子商定義；沒有改換成另一種 essential spectrum 或一個新選的弱空間。

## 6. 與已有上界及準緊性相容

[一側 roof 筆記][roof] §6 在同一空間已證
\(r_{\rm ess}(\mathcal L_s)\le q\lambda_t\)，其中
\(\lambda_t=\lim_n\|\mathcal L_t^n1\|_\infty^{1/n}\)。
因此合併為

\[
\boxed{0<q e^{-M_t}\le r_{\rm ess}(\mathcal L_s)\le q\lambda_t.}
\tag{21}
\]

其相容性也可直接核對：每個實權分支至少為 \(e^{-M_t}\)，每點恰有 \(2^n\) 個 n 步前像，故 \(\lambda_t\ge2e^{-M_t}\)。

非緊及正本質譜半徑均不排除準緊性。特別是實 t 的既有結論
\(r_{\rm ess}(\mathcal L_t)\le q\lambda_t<\lambda_t=r(\mathcal L_t)\)
仍成立。本文沒有證明一般複 s 都準緊，也沒有把 (20) 升級為精確本質譜半徑公式。

## 7. Nuclear 限定與 finite-memory determinant 極限

### 7.1 所用核性定義及 nuclear 蘊含 compact 的直接證明

此處普通 1-nuclear 指 Banach 算子有表示

\[
Tu=\sum_{j\ge1}\ell_j(u)v_j,\qquad
\ell_j\in\mathcal B_\beta^*,\quad v_j\in\mathcal B_\beta,\qquad
\sum_{j\ge1}\|\ell_j\|\,\|v_j\|<\infty.
\tag{22}
\]

令 \(T_Nu=\sum_{j=1}^N\ell_j(u)v_j\)，則它有限秩，且

\[
\|T-T_N\|\le\sum_{j>N}\|\ell_j\|\,\|v_j\|\longrightarrow0.
\tag{23}
\]

緊算子在算子范數下閉，故 T 緊。這一步不需要 approximation property、核跡的表示獨立性或 determinant 存在定理。

若採通常 \(0<p<1\) 的 p-nuclear 表示，即相應的正數 \(a_j=\|\ell_j\|\|v_j\|\) 滿足 \(\sum a_j^p<\infty\)，則 \(a_j\to0\)，充分大 j 有 \(a_j\le a_j^p\)，所以仍有 (22)。通常意義的 nuclear of order zero 要求所有正階的相應核性，尤其滿足上述更強於 1-nuclear 的條件。因此也必緊；本頁明確使用這個通常的階數慣例。

由 §5，每個 \(\mathcal L_s^n\)、n≥1，都不可能是上述 1-nuclear 或 order-zero nuclear 算子。特別是原全空間上的 \(\mathcal L_s\) 並非這些核算子。

### 7.2 有限矩陣極限仍成立，但不是原算子的傳統核 Fredholm 行列式

[finite-memory 筆記][finite-memory] §4–6 使用 \(g_m=P_mg\) 及有限維不變子空間上的矩陣
\(A_m(s)=\mathcal L_s^{[m]}|_{\mathcal F_{m-1}}\)，不是原全空間算子本身。它已證明

\[
\det(I-zA_m(s))\longrightarrow
\mathfrak d(s,z)=
\exp\!\left(-\sum_{n\ge1}\frac{z^n}{n}
\sum_{\sigma_+^np=p}e^{-sS_ng(p)}\right)
\tag{24}
\]

在
\(\mathcal D=\{(s,z):\operatorname{Re}s>0,\quad
2|z|e^{-4a\operatorname{Re}s}<1\}\)
的緊子集上局部一致；取 z=1 則在
\(\operatorname{Re}s>\log2/(4a)\)
得到同一物理週期 zeta 的倒數。

非緊性不破壞這個有限維恒等式和受控標量極限。該筆記也明確未證 \(P_m\to I\) 在全大 Hölder 范數中的強／算子范數收斂，未證原算子在核范數下被逼近，並區分柱集壓縮跡與有限記憶矩陣的冪。

但 (22)–(23) 與 §5 現在給出更明確的障礙：原 \(\mathcal L_s\) 不屬於上述核算子類，所以不能把 (24) 識別為它在這個原全空間上的傳統 nuclear Fredholm determinant。有限矩陣 determinant 有極限，不會將一個已證非核的原算子變成核算子；本頁也不賦予 \(\mathcal L_s^n\) ordinary nuclear trace。

這不否定其他函數空間、另行構造的核算子、正规化 determinant 或 dynamical determinant。任何這樣的另類身份都須有自己的定義、空間及證明，不能由本頁排除或由 (24) 自動取得。

## 8. 授權、來源與實際操作

本頁完整展開前一只讀輪已核對的證明；主線另已核對分區差商及精確 C_s。同模型唯讀席補查局部右逆、緊理想及 nuclear 限定；其同意不算外部獨立科學證據。

使用已完整讀取的[一側 roof 筆記][roof]，本次又完整讀取[finite-memory 筆記][finite-memory]以核定它的有限維矩陣、收斂域及既有停止線。沒有新增未實際核讀的一手文獻引用；§5 明列所用 Calkin 定義與 quotient Gelfand 公式，§7 的核性障礙由級數尾界直接證明。

寫前確認目標不存在，只以 apply_patch 建立本新檔；寫後做最小靜態檢查，涵蓋控制字元、尾空白、衝突標記、公式分隔／編號、本地引用目標及 SHA-256。首次檢查發現一處行末 TeX 空格；引用檢查式亦因只辨識 inline 連結而漏掉本頁的 reference-style 定義，報告引用數零，並非引用目標缺失。僅修本頁該空格、使檢查式辨識實際引用格式，再對變更後的新檔做必要複查；不覆寫失敗紀錄。未運行科學程式、符號／數值計算、字詞／矩陣枚舉、實驗、producer、稿件 build 或正式驗證器。靜態檢查不認證數學成立性。

本頁不構成 Route 評估或正式 Stage 升級。原 A0_FAIL / A2_NOT_ELIGIBLE / NO_ROUTE_PROMOTION、Gate 6 NOT_ACTIVATED、Stage 5／6 停止條件及歷史失敗記錄保持不變。原物理時鐘、正 roof、符號度量及全 Banach 空間均未替換。

[roof]: /root/autodl-tmp/flow_systems/papers/30-three-disk-nonconstant-roof-determinant/notes/internal_goal01_one_sided_roof_and_transfer_bounds_20260909.md
[finite-memory]: /root/autodl-tmp/flow_systems/papers/30-three-disk-nonconstant-roof-determinant/notes/internal_goal01_cylinder_trace_and_finite_memory_determinants_20260909.md
