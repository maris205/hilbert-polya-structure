# P30 goal01：保原週期的一側正 roof 與固定 Hölder 空間轉移算子界

日期：2026-09-09 UTC。範圍：使用者授權持續主控研究後的單檔內部理論整理；唯一新寫本檔，不改舊稿、鎖定輸入、程式、資料或正式狀態。

固定原等邊三圓盤，半徑 `a>0`、中心間距 `d=6a`、單位歐氏速率、逐碰撞截面及原盤標記。下文服務[路線圖][roadmap] §4 的真實流—週期資料鏈與 §8「Flow Zeta and Resonance Structure」，不是 Hilbert–Pólya 算子構造，也不簽發 Route 或 Stage 結論。

## 0. 證據層級與本次增量

- **既有落盤輸入**：[雙向編碼筆記][coding] 的式 (8)、(21)、(27)–(29)，給全部真實雙向被困碰撞的編碼及原 roof 的定量 Hölder 界。該舊檔沒有證明一側化或算子結論。
- **繼承此前只讀理論輪的推導**：§2–3 的穩定纖維求和、降指數、有限平均與保週期共邊界；§5–6 的 n 步 distortion、Lasota–Yorke 及實／複參數譜界；附錄 A 的複權反例已經另席提出並逐式交叉核對。這些在本檔完整重述，不以同伴同意充當獨立科學證據。
- **本次補出的步驟**：§3 末的雙向懸掛時間保持映射，以及 §4 固定 Banach 空間上的算子範數整族證明。「本次新增」僅描述研究鏈進度，不是文獻新穎性宣稱。

這是一份可逐式檢查的內部數學筆記，不是數值、形式化證明器或外部獨立再現的證書。ARS academic-paper / argument-builder 的有限 Phase 3 原則用於分開前提、證明與升級失敗點；未啟動完整寫作或審查流水線。

## 1. 固定物件、度量與全部需要的上游輸入

圓盤中心為 `C1=(0,0)`、`C2=(6a,0)`、`C3=(3a,3sqrt(3)a)`。令

\[
\Sigma=\{x\in\{1,2,3\}^{\mathbb Z}:x_i\ne x_{i+1}\},\qquad
\Sigma^+=\{x\in\{1,2,3\}^{\mathbb N_0}:x_i\ne x_{i+1}\}.
\tag{1}
\]

`sigma`、`sigma+` 均為左移，`pi:Sigma→Sigma+` 保留非負座標。上游物理編碼在本頁記為 `H_phys`，以免和共邊界函數混淆；它把雙向盘字送到唯一真實被困碰撞狀態，與原碰撞映射共軛。若 `Q_i(x)` 是實際碰撞點，原單位速率飛行時間是

\[
\tau(x)=|Q_1(x)-Q_0(x)|\in[4a,8a],\qquad
\rho=\frac3{2\sqrt6-1}<1,\qquad C=\frac{4a}{\rho^2}.
\tag{2}
\]

對不同的雙向盤字令 `N(x,y)=min{|j|:x_j!=y_j}`，並固定一次 `0<theta<1`。兩種度量、指數及上游界為

\[
d_\theta(x,y)=\theta^{N(x,y)},\quad
d_\theta^+(x,y)=\theta^{\min\{j\ge0:x_j\ne y_j\}},\quad
\alpha=\frac{\log\rho}{\log\theta},\quad
|\tau(x)-\tau(y)|\le C\rho^{N(x,y)}=Cd_\theta(x,y)^\alpha.
\tag{3}
\]

相同盤字的距離定為零。下文固定

\[
\beta=\alpha/2>0,\qquad q=\theta^\beta=\sqrt\rho<1.
\tag{4}
\]

此處是符號超距離；不把它誤認為歐氏度量，也不要求這個符號 Hölder 指數小於等於 1。§2 以後只使用 (1)–(3) 及上游已證的物理編碼，不重複宣稱已完成幾何證明的獨立認證。

## 2. 穩定纖維求和：明確一側化與指數控制

取 `b(1)=2`、`b(2)=b(3)=1`。令 `Rx` 保留全部非負座標；負座標在 `x_0,b(x_0)` 間交替，即 `(Rx)_{-2k}=x_0`（`k>=1`）及 `(Rx)_{-(2k+1)}=b(x_0)`（`k>=0`）。它是合法盤字，只依賴 `pi x`，但一般不與移位交換。

定義

\[
h(x)=\sum_{n=0}^{\infty}
 [\tau(\sigma^n x)-\tau(\sigma^n Rx)],\qquad
B_0=\frac{C\rho}{1-\rho}.
\tag{5}
\]

兩個被比較盤字在所有座標 `j>=-n` 一致，故第 n 項絕對值至多 `C rho^{n+1}`。級數一致絕對收斂，`||h||_infty<=B_0`。

若 `pi x=pi y`，則 `Rx=Ry`，所以

\[
h(x)-h(y)=\sum_{n\ge0}[\tau(\sigma^n x)-\tau(\sigma^n y)].
\tag{6}
\]

對 `sigma x,sigma y` 的同式恰刪去右側首項。因此

\[
f=\tau-h+h\circ\sigma=f^+\circ\pi
\tag{7}
\]

確實有一個只依賴非負座標的實值代表 `f+`。這是由 (6) 證明的一側依賴，不是直接刪去物理狀態的過去。

**正則性另證。** 若 `N=N(x,y)>=1`，令 `k=floor(N/2)`。在 (5) 的前 k 項，分別比較移位後的 x、y 及 Rx、Ry，每項差至多 `2C rho^{N-n}`；尾項則用穩定纖維界。因而

\[
|h(x)-h(y)|\le\frac{2C}{1-\rho}
 (\rho^{N-k+1}+\rho^{k+1})
 \le K_h\rho^{N/2},\qquad
K_h=\frac{4C\sqrt\rho}{1-\rho}.
\tag{8}
\]

`N=0` 由 `2B_0<=K_h` 補足。故 h 是 beta-Hölder。移位的 beta-Hölder 常數至多放大 `q^{-1}`，且 (3) 亦給 `[tau]_beta<=C`，所以

\[
[f]_\beta\le K_f:=C+(1+q^{-1})K_h.
\tag{9}
\]

從一側盤字補入上述標準過去的提升不擴張距離；對該提升使用 (9)，得到 `[f+]_beta<=K_f`。本證明只保證至少一半原指數，不聲稱保留 alpha，也不聲稱損失一半是最優。

## 3. 正性修正、全部週期和及原物理時間

共邊界不自動保持點值正性，(7) 尚不能直接稱為正 roof。固定與複參數 s 無關的整數

\[
m_*:=\left\lceil B_0/a\right\rceil
 =\left\lceil\frac4{\rho(1-\rho)}\right\rceil,\qquad
g:=\frac1{m_*}\sum_{j=0}^{m_*-1} f^+\circ(\sigma^+)^j.
\tag{10}
\]

令 `S_m tau=sum_{j=0}^{m-1}tau o sigma^j`，則 (7) 望遠鏡相消給

\[
g(\pi x)=\frac{S_{m_*}\tau(x)+h(\sigma^{m_*}x)-h(x)}{m_*},
\qquad 2a\le g\le10a.
\tag{11}
\]

有限平均仍是一側 beta-Hölder 函數，具有明確有限界

\[
G:=[g]_\beta\le\frac{K_f}{m_*}\sum_{j=0}^{m_*-1}q^{-j}.
\tag{12}
\]

再令

\[
v=\frac1{m_*}\sum_{j=0}^{m_*-2}(m_*-1-j)f^+\circ(\sigma^+)^j,
\qquad U=h+v\circ\pi.
\tag{13}
\]

v 同樣是有限個移位的線性組合，故為一側 beta-Hölder；pi 不擴張所選距離，因此 U 為雙向 beta-Hölder。逐項比較有限和，`g=f+-v+v o sigma+`，所以

\[
\boxed{g\circ\pi=\tau-U+U\circ\sigma.}\qquad
S_ng(\pi x)=S_n\tau(x)+U(\sigma^n x)-U(x).
\tag{14}
\]

若 `sigma^n x=x`，兩個週期和完全相等，無須 n 是 `m_*` 的倍數。一側週期盤字有唯一的雙向週期延拓；結合上游物理編碼，(14) 保留原碰撞週期的實際總飛行時間。平均不會把週期時間除以 `m_*`。

正性確實需要論證：僅從同樣的值域及 (3)，可取抽象 `tau_toy(x)=F(x_{-4})`，其中 `F(1)=F(2)=4a`、`F(3)=4a+4a rho^2`。差異發生時 `N<=4`，所以它符合 (3)；但依相同 R 構造的 `f+` 在首塊 13 上等於 `4a-8a rho^2<0`。這不是實際幾何 tau 的負性判定，只排除不經證明便省略 (10) 的做法。

**本次明列的時間保持核對。** 在雙向懸掛中，把 `(x,r+tau(x))` 與 `(sigma x,r)` 識別。由 (14)，

\[
\Phi:[x,r]_\tau\longmapsto[x,r-U(x)]_{g\circ\pi}
\tag{15}
\]

與邊界識別相容；其逆加回 U，且與任意時間平移 `r→r+t` 交換。tau 與 `g o pi` 皆為正連續函數，故這給雙向符號懸掛間的時間保持同胚，沒有重新縮放物理時鐘。g 一般不逐點等於單次物理飛行長度；單側非可逆基底也不能直接稱為全部雙向碰撞狀態的共軛。

## 4. 固定 Banach 空間上的有界算子與整族（本次補證）

固定

\[
\mathcal B_\beta=C^\beta(\Sigma^+,d_\theta^+;\mathbb C),\qquad
\|u\|_\beta=\|u\|_\infty+[u]_\beta,
\quad [u]_\beta=\sup_{x\ne y}\frac{|u(x)-u(y)|}{d_\theta^+(x,y)^\beta}.
\tag{16}
\]

它是 Banach 空間：范數 Cauchy 列先一致收斂；將每個差商取極限，再對兩點取上確界，即得在 (16) 中收斂。由乘積差商有 `||uv||_beta<=||u||_beta||v||_beta`，故亦是含單位元的 Banach 代數。

對每個 `s in C` 定義同一空間上的有限兩分支算子

\[
(\mathcal L_su)(x)=\sum_{b\ne x_0}e^{-sg(bx)}u(bx).
\tag{17}
\]

`b x` 表示在 x 前加字母 b；每個 x 恰有兩個前像。取弱范數 `||u||_infty`。對 `s=0`，同首字母的兩點可配對分支，前綴將 beta 次方距離縮成 q 倍；不同首字母則距離為 1，以兩個上確界控制。因此

\[
\|\mathcal L_0u\|_\infty\le2\|u\|_\infty,\qquad
[\mathcal L_0u]_\beta\le2q[u]_\beta+4\|u\|_\infty,
\quad\|\mathcal L_0\|_{\beta\to\beta}\le6.
\tag{18}
\]

令 `M_g u=g u`，則 `||M_g||<=||g||_beta`。Banach 代數中的指数級數給

\[
\mathcal L_s=\mathcal L_0M_{e^{-sg}}
 =\mathcal L_0\sum_{k=0}^{\infty}\frac{(-s)^k}{k!}M_g^k,
\qquad \|\mathcal L_s\|\le6e^{|s|\|g\|_\beta}.
\tag{19}
\]

級數及各階逐項導數在 s 的每個緊集上以算子范數一致收斂；其逐點值正是 (17)。故 `s→L_s` 是 `C→B(B_beta)` 的整函數，並有

\[
\partial_s^k\mathcal L_su=\mathcal L_s((-g)^ku),\qquad
\|\partial_s^k\mathcal L_s\|\le6\|g\|_\beta^k e^{|s|\|g\|_\beta}.
\tag{20}
\]

theta、beta、標準過去、`m_*`、g 與函數空間全都預先固定，沒有隨 s 更换空間或 roof。整算子族不等於整行列式，也不保證各參數都有簡單主特徵值。

## 5. n 步共同分支 distortion 與強弱范數界

令 `D=Gq/(1-q)`。若 w 是長度 n 的盤字，且 `w x,w y` 均合法，則對 `0<=j<n`，其 j 次移位後的距離為 `theta^{n-j}d_theta^+(x,y)`。求幾何和得

\[
\boxed{|S_ng(wx)-S_ng(wy)|\le
 D(1-q^n)d_\theta^+(x,y)^\beta.}
\tag{21}
\]

同一長度 n 柱集中的 distortion 因此至多 D，對 n 一致。直接迭代 (17) 給出對全部長度 n 合法前綴的求和，權重為 `exp(-s S_n g(w x))`。

對 `t=Re s` 定義

\[
A_n(t)=\|\mathcal L_t^n1\|_\infty,\qquad K_s=3+2|s|D.
\tag{22}
\]

權重的模等於實權重，故 `||L_s^n u||_infty<=A_n(t)||u||_infty`。同首字母的兩點具有相同前綴集合，函数值之差貢獻 `A_n q^n[u]_beta`。對實數 X、Y，沿兩者之間的實線段積分可得

\[
|e^{-sX}-e^{-sY}|\le|s||X-Y|\max(e^{-tX},e^{-tY}).
\tag{23}
\]

用 (21) 後，分支的最大權重之和至多兩端權重和，即 `2A_n`；權重之差的貢獻至多 `2A_n|s|D||u||_infty`。不同首字母時距離為 1，直接用 `2A_n||u||_infty`。合併得到

\[
\boxed{\begin{aligned}
\|\mathcal L_s^nu\|_\infty&\le A_n(t)\|u\|_\infty,\\
\|\mathcal L_s^nu\|_\beta&\le A_n(t)
 (q^n[u]_\beta+K_s\|u\|_\infty).
\end{aligned}}
\tag{24}
\]

K_s 對 n 一致，但不是對任意高頻 `|Im s|` 一致的相消常數。(24) 保留實際 `A_n`；沒有未經證明便把它換成常數倍的 `lambda_t^n`。

## 6. 譜半徑、本質譜半徑及精確停止線

正性給 `A_{n+m}(t)<=A_n(t)A_m(t)`，故次乘性（或將 n 分成固定長度塊）給

\[
\lambda_t:=\lim_{n\to\infty}A_n(t)^{1/n}
 =\inf_{n\ge1}A_n(t)^{1/n},\qquad
2\min(e^{-2at},e^{-10at})\le\lambda_t\le2\max(e^{-2at},e^{-10at}).
\tag{25}
\]

上下界使用每點恰有 `2^n` 個前綴及 `2an<=S_n g<=10an`；特別地 `lambda_t>0`。由 (24) 及譜半徑公式，`r(L_s)<=lambda_t`。對實 s=t，常數函數 1 在 (16) 中范數為 1，故 `||L_t^n||>=A_n(t)`，得到 `r(L_t)=lambda_t`。此處不將 lambda 命名為尚未在本檔建立的壓力或流熵。

**本質譜界的直接有限秩證明。** 每個長度 m 柱集選一個合法無限延拓作代表點，令 `P_m u` 在該柱集上等於代表點的函數值。它有限秩；不同柱集代表點保留兩柱集的首個分歧位置，因此

\[
\|u-P_mu\|_\infty\le q^m[u]_\beta,\qquad
[P_mu]_\beta\le[u]_\beta,\qquad
[(I-P_m)u]_\beta\le2[u]_\beta.
\tag{26}
\]

把 `(I-P_m)u` 代入 (24)，得

\[
\|\mathcal L_s^n-\mathcal L_s^nP_m\|_{\beta\to\beta}
 \le A_n(t)(2q^n+K_sq^m).
\tag{27}
\]

右側近似算子有限秩，故先令 m 趨向無窮，算子到緊算子集合的距離至多 `2A_n(t)q^n`。依[Hennion，Corollaire 5.3(ii)][hennion] 的緊算子距離公式（本質譜半徑取緊算子商中的譜半徑），再取 n 次根即得

\[
\boxed{r(\mathcal L_s)\le\lambda_{\operatorname{Re}s},\qquad
r_{\rm ess}(\mathcal L_s)\le q\lambda_{\operatorname{Re}s}.}
\tag{28}
\]

特別地，對每個實 t，

\[
\boxed{r(\mathcal L_t)=\lambda_t,\qquad
r_{\rm ess}(\mathcal L_t)\le q\lambda_t<\lambda_t.}
\tag{29}
\]

故實權歸一化算子 `lambda_t^{-1}L_t` 已有準緊性。但本檔沒有證明模 `lambda_t` 的譜點唯一、正主特徵函數嚴格為正或該特徵值代數單重；不把 (29) 寫成已完成的 Perron–Frobenius 簡單主譜隙。

對一般複 s，(28) 只比較實權增長率，沒有給出 `r(L_s)>r_ess(L_s)`，所以不宣稱任意複參數準緊，也不宣稱實際物理 g 具有扭曲譜隙、全高頻無譜線或統一混合率。附錄 A 顯示，若只保留目前抽象前提，「任意複參數準緊」甚至可以為假。

## 7. 未完成義務與路線圖位置

論證鏈為「真實雙向 roof 的上游定量界 → 保週期一側正代表 → 固定空間整算子族 → n 步界 → 實權準緊／複權上界」。這些結論服務自然 flow-zeta／共振物件的算子入口，不是已經建成該物件。

最近可單獨核對的下一工作單元，是實權的 Perron–Frobenius 外圍譜論證：正主特徵函數、代數單重、其餘外圍譜排除。複扭曲的週期相位條件、非格性或高頻抵消必須另立精確假設與證明，不能由 (29) 外推。

本檔未建立核性、trace-class、算子跡、dynamical／Fredholm／quantum determinant 身份、完整解析延拓或共振計數；更未建立自伴量子算子、域、素數 trace、Weil 公式或 Hilbert–Pólya 結論。原 `A0_FAIL / A2_NOT_ELIGIBLE / NO_ROUTE_PROMOTION`、Gate 6 `NOT_ACTIVATED` 及原 Stage 5／6 停止條件不因此改動。

## 附錄 A. 抽象複權反例：不是實際三圓盤 roof

此附錄只否定不加條件的算子升級，沒有替換主文 g、凍結新候選或改變 P30 物理模型。繼承前一輪已交叉核對的反例，令 `omega=exp(2pi i/3)`，

\[
W=\begin{pmatrix}0&1&1\\1&0&i\omega^2\\\omega&-i&0\end{pmatrix},\qquad
s_0=i\pi/a.
\tag{A1}
\]

取局部常數邊 roof `g_toy(i,j)`：`g12=g13=g21=2a`、`g23=13a/6`、`g31=10a/3`、`g32=5a/2`。它在 `[2a,4a]`，且 `exp(-s_0 g_toy(i,j))=W_ij`。它属于相同符號 Hölder 類，並非由真實飛行 tau 經 (5)–(14) 得到的 g。

三個反向邊乘積為 `1,omega,omega^2`，兩個三循環乘積為 `i,-i`，所以 W 的特徵多項式為 `z^3`，Cayley–Hamilton 給 `W^3=0`。此 toy 算子 T 在首字母函數空間上是 `W^T`。若 F_m 是只依賴前 m 字母的函數，則 `T F_m subset F_(m-1)`（`m>=2`），再三步消滅 F_1。因此對 (26) 的投影

\[
T^{m+2}P_m=0\quad(m\ge1),\qquad T^nP_{n-2}=0\quad(n\ge3).
\tag{A2}
\]

把 (24) 用於 toy roof，`A_n(0)=2^n`，得到 `||T^n||<= (2q)^n(2+K_{s_0}q^{-2})`，此處 K 以 toy roof 的 Hölder 常數計算；故 `r(T)<=2q`。

記 `w(y)=exp(-s_0 g_toy(y))`，定義右逆 `Ru(y)=u(sigma+ y)/(2w(y))`，則 `TR=I`。有

\[
R^nu=2^{-n}V_n\,u\circ(\sigma^+)^n,\quad
V_n=\prod_{j=0}^{n-1}(w\circ(\sigma^+)^j)^{-1},\quad
|V_n|=1,\quad [V_n]_\beta\le2q^{-n},\quad
\|R^n\|\le3(2q)^{-n}.
\tag{A3}
\]

`V_n` 只依賴前 `n+1` 字母，故其值若不同，首分歧索引至多 n；這證明 (A3) 的常數對 n 一致，沒有遺漏的 n 因子。對首字母 j，將兩個允許的前置字母固定按數字大小排序為 `b_1(j),b_2(j)`；對每個 x 在兩個前像 `b_1(x_0)x,b_2(x_0)x` 上分別置 `w(b_1(x_0)x)^{-1}phi(x)`、`-w(b_2(x_0)x)^{-1}phi(x)`。分支選擇只看首字母，這把任意 Hölder phi 單射送入 `ker T`，所以該核無限維。

對 `|z|<2q` 及 `v in ker T`，(A3) 使 `F_zv=sum_{n>=0}z^nR^nv` 在固定 Hölder 范數中收斂。`T F_zv=z F_zv`，且 `(I-RT)F_zv=v`，故 `ker(T-zI)` 無限維。若 `T-zI` 在緊算子商中可逆，便有有界算子 S 使 `S(T-zI)=I-K`，K 緊；限制到此無限維閉核會令 K 成為恒等算子，與緊性矛盾。因此這些 z 都在本質譜中，結合上界得

\[
\boxed{r_{\rm ess}(T)=r(T)=2q.}
\tag{A4}
\]

這個反例不否定實際物理 g 可能另有可證的複扭曲譜性質，只證明「正 Hölder roof、兩分支與 LY」本身不保證任意複参数準緊。

## 8. 來源、實際操作及可再核對範圍

本次完整重讀實際 `AGENTS.md`、`docs/workflow.md`、ARS 0.1.28 router、academic-paper workflow 與 argument-builder role，以及[雙向編碼筆記][coding]；讀取[路線圖][roadmap] §4、§8 以核定科學位置。沒有開啟 Route 評估 skill、正式 reviewer 或實驗流水線。

上游雙向筆記在本次寫前的 SHA-256 是 `55d4f7a0cdbfc654a7707850787c76903faa04f02fb74f20e9d617197b3549e5`。它只承擔 §1 的幾何／雙向 roof 輸入；本頁一側化和算子界由上述公式承擔，不能倒寫為舊檔已證。

公開來源沿用此前只讀輪已實際核讀的兩個定位：[Dougall–Sharp 作者稿，Lemma 3.3][dougall-sharp] 支持通用保週期一側化時容許降低指數；[Hennion，Corollaire 5.3(ii)][hennion] 支持 §6 的緊算子距離公式。前者不是本頁顯式常數或正性修正的證據；後者不是替 P30 自動核發譜隙。核讀範圍為相應文字層敘述及所需上下文，不宣稱全文審查；先前 Hennion 頁面截圖曾逾時，未冒稱視覺核對，也未因此上傳私人稿件。

寫前 `test ! -e` 確認新目標不存在，以 `apply_patch` 建立唯一授權新檔。沒有運行科學／符號程式、字詞枚舉、數值迭代、實驗、producer、artifact writer、稿件 build 或正式驗證器；沒有寫舊檔、鎖或正式狀態。主線的原檔快照不由本分支重建。交接另報檔案行數、摘要和最小只讀文字檢查；格式／hash 檢查不等於數學成立性。

[coding]: /root/autodl-tmp/flow_systems/papers/30-three-disk-nonconstant-roof-determinant/notes/internal_biinfinite_coding_and_roof_locality_20260909.md
[roadmap]: /root/autodl-tmp/flow_systems/propose-flow-systems.md
[dougall-sharp]: https://warwick.ac.uk/fac/sci/maths/people/staff/richard_sharp/p2/anosov_amenable_revised_15may2020.pdf
[hennion]: https://www.numdam.org/item/PSMIR_1995___2_A6_0.pdf
