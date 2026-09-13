# P31：天然 holonomy、真時鐘與有限覆蓋誘導傳輸

日期：2026-09-09。Goal 01 授權範圍內的單一有界理論筆記；不是正式稿、Route 評估或 Stage 推進。

## 0. 結論、固定輸入與證據層級

**紙面結論。** 不要求時間密度下降，也能把十二層覆蓋上同一流的真時間與天然酉 holonomy 編入 ambient rank-\(12m\) bundle cocycle。每個 ambient primitive 幾何閉軌的有限 monodromy determinant，逐 cycle 精確等於其全部 cover primitive lifts 的真週期因子。更特殊地，凍結的閉一形式時鐘允許將此 cocycle 寫成測地衰減乘上一族 **依賴 spectral parameter 的誘導平坦傳輸**。

這不是 ambient scalar physical roof，不是固定酉表示的替換，也不是無限維 transfer/Fredholm determinant 或 cusp 正則化的證明。

本筆記只使用 [P31 coset-cycle 筆記][cycles] 的十二層覆蓋、cycle/primitive-lift 與方向接口，以及 [P26 README 的 Frozen dynamical system][clock]。參數 \(\epsilon\)、rank \(m\)、表示或閉一形式相位均先固定；不讀取 prime/zero 目標表選權，不改 newform、\(k=2y+z\)、Hecke、owner 或任何既有契約。以下等式由文內有限維線性代數、路徑提升及閉形式積分直接證明，沒有科學程式或實驗證據。

## 1. 同一覆蓋、兩種時間

令

\[
G=\mathrm{PSL}_2(\mathbb Z),\quad
\Gamma=\Gamma_0(11)/\{\pm I\},\quad
M=\Gamma\backslash\mathrm{PSL}_2(\mathbb R),\quad
N=G\backslash\mathrm{PSL}_2(\mathbb R).
\tag{1}
\]

自然映射 \(p:M\to N\) 是十二層覆蓋。這是在 unit-tangent quotient 上的覆蓋；離散群在 Lie group 上左乘自由，無須把有 elliptic points 的 ambient 二維 orbifold 當作無挠曲面。

用 \(\phi_0^u\)、\(g^u\) 分別記 cover 與 ambient 的 unit-speed geodesic flow；\(p\phi_0^u=g^u p\)。凍結

\[
\alpha_f=\operatorname{Re}(2\pi i f(z)\,dz),\quad
a(v)=\alpha_f(v),\quad
\rho_\epsilon=1+\epsilon a>0,\quad
X_\epsilon=X_{\rm geo}/\rho_\epsilon.
\tag{2}
\]

其中仍是凍結的 \(f(z)=\eta(z)^2\eta(11z)^2\)，且 \(|\epsilon|<\|a\|_\infty^{-1}\)。這個條件給正的 \(\rho_\epsilon\)；不另換 roof 或 speed convention。

此處 \(\rho_\epsilon\) 是 slowness，不是速度。\(u\) 是測地參數；lift 起點 \(y\in M\) 的物理時間為

\[
t_\epsilon(u,y)=\int_0^u\rho_\epsilon(\phi_0^v y)\,dv
=u+\epsilon\int_{\pi\phi_0^{[0,u]}y}\alpha_f.
\tag{3}
\]

對 \(u>0\) 它嚴格為正，並滿足

\[
t_\epsilon(u+v,y)=t_\epsilon(u,y)+t_\epsilon(v,\phi_0^u y).
\tag{4}
\]

其中 \(\pi:M\to Y_0(11)\) 是 footpoint projection。不同 sheets 在相同 \(u\) 下可以累積不同的 \(t_\epsilon\)；本筆記不另證或假定 \(\rho_\epsilon\) 下降。

## 2. 相位必須先來自同一流的幾何

取 \(Y_0(11)\) 上固定 rank-\(m\) 酉平坦局部系，再拉回為 \(M\) 上的 \(E\)。等價地，可先指定一個固定的 subgroup 酉表示，並一次固定其與正向 loop monodromy 的慣例。沿幾何流段的酉平行傳輸記為

\[
U_y(u):E_y\longrightarrow E_{\phi_0^u y}.
\tag{5}
\]

rank-one 例子是固定實閉一形式 \(\beta\) 的 connection \(d-i\beta\)，其傳輸為 \(\exp(i\int\beta)\)。因此相位遵守路徑拼接、同倫與遍歷律，不能逐閉軌獨立調節。以 \(\beta+d\psi\) 代替 \(\beta\) 只作 endpoint gauge，不改 closed-loop holonomy。

固定的 Jacobian character 亦可作相位來源；若使用整個角色族，族本身須由同一同調格預定，不能事後用目標表挑選參數。本文不為任何具體角色宣稱額外算術表現。

## 3. Pushforward local system 與一般真時鐘 cocycle

**引理 1。**

\[
F=p_*E,\qquad F_q=\bigoplus_{y\in p^{-1}(q)}E_y
\tag{6}
\]

是 rank-\(12m\) 酉平坦局部系。

**證明。** 在 evenly covered 小鄰域，每張 sheet 上的平坦框架直和給出框架。換鄰域時只出現 sheet permutation 與各 summand 的酉平坦 transition。任意 ambient 路徑從每個 sheet 唯一提升，將各 \(E_y\) 傳到 endpoint sheet；拼接與同倫相容，因而定義 \(F\) 的平坦傳輸。□

這也直接給誘導表示的含義：選定 sheets 的路徑代表後，一個 ambient loop 的提升置換 sheets，並在每個非零 block 放入對應 subgroup loop 的 holonomy。這正是 induced monodromy 的 block-permutation 模型。

嚴格在 \(M,N\) 上，表示記為

\[
\operatorname{Ind}_{p_*\pi_1(M)}^{\pi_1(N)}\nu.
\tag{7}
\]

本筆記的局部系從二維底面拉回，中心纖維 monodromy 平凡；在一致的 loop/deck convention 下，可用 \(\operatorname{Ind}_{\Gamma}^{G}\nu\) 記同一結構，這裡也以 \(\nu\) 記對基本群的拉回表示。不能把非單連通的 \(\mathrm{PSL}_2(\mathbb R)\) 誤當 universal cover。

**定理 2（不需屋頂下降的誘導加權傳輸）。** 對任意 \(s\in\mathbb C\)，在 (6) 上定義

\[
\mathcal A_{\epsilon,s}(u,q)|_{E_y}
=e^{-s t_\epsilon(u,y)}U_y(u):E_y\to E_{\phi_0^u y}.
\tag{8}
\]

它是覆蓋同一 ambient 幾何流 \(g^u\) 的 rank-\(12m\) cocycle：

\[
\mathcal A_{\epsilon,s}(u+v,q)
=\mathcal A_{\epsilon,s}(v,g^u q)\mathcal A_{\epsilon,s}(u,q).
\tag{9}
\]

**證明。** \(\phi_0^u\) 將 \(p^{-1}(q)\) 雙射到 \(p^{-1}(g^u q)\)；各 block 的 scalar weight 由 (4) 相乘，\(U\) 由平行傳輸拼接相乘。逐 summand 即得 (9)。□

這裡的「矩陣 cocycle」指選局部框架後的矩陣；全局自然對象是 bundle morphism，未要求 \(F\) 有特選全局平凡化。若 \(\operatorname{Re}s=0\)，(8) 為酉傳輸；一般 \(s\) 則只是加權可逆傳輸。

等價的 clock endomorphism 是

\[
\mathcal R_\epsilon(q)|_{E_y}=\rho_\epsilon(y)I_m.
\tag{10}
\]

它與 induced connection 共同決定 (8)。它是 scalar 當且僅當該 fiber 的所有 \(\rho_\epsilon(y)\) 相等；\(s\)-independent gauge 只共軛此 coefficient，不能把非 scalar coefficient 變成 scalar。這個點態陳述不是對任意非酉、參數依賴 gauge 或 cohomological roof reduction 的總體 no-go。

## 4. 凍結閉一形式時鐘的額外平坦化

一般正時間密度只給 (8)。本案 (2) 還有更強、可直接證明的結構。

**引理 3。** 對固定 \(\epsilon,s\)，閉形式的 loop periods 給角色

\[
\kappa_{\epsilon,s}([\gamma])
=\exp\!\left(-s\epsilon\int_\gamma\alpha_f\right).
\tag{11}
\]

**證明。** 閉性使積分對 based-loop 同倫不變，拼接使其相加，因此 (11) 對 loop multiplication 相乘。倒向使 period 變號；共軛路徑的來回段互相抵消。□

在 \(E\) 上把 connection 改寫為

\[
\nabla^{E_{\epsilon,s}}=\nabla^E+s\epsilon\pi^*\alpha_f\,I_m.
\tag{12}
\]

因原 connection 平坦、\(d\alpha_f=0\)，且新增項為 scalar closed form，(12) 仍平坦。其流段傳輸為

\[
U_y^{\epsilon,s}(u)=
e^{-s\epsilon\int_{\pi\phi_0^{[0,u]}y}\alpha_f}U_y(u).
\tag{13}
\]

**定理 4（參數依賴的 flat induction）。** 把 \(E_{\epsilon,s}\) push forward 為 \(F_{\epsilon,s}\)，則在相同底層向量叢識別下

\[
\boxed{\mathcal A_{\epsilon,s}(u,q)
=e^{-su}\operatorname{PT}_{F_{\epsilon,s}}(g^{[0,u]}q).}
\tag{14}
\]

其 monodromy 是 \(\operatorname{Ind}(\nu\otimes\kappa_{\epsilon,s})\)，而非忽略時鐘的 \(\operatorname{Ind}\nu\)。

**證明。** 將 (3) 代入 (8)，再逐 summand 使用 (13) 與引理 1。□

此平坦化沒有使 \(\alpha_f\) 或 \(\rho_\epsilon\) 下降：它把 cover 的閉形式資訊保存在 ambient vector coefficients 裡。\(\epsilon\)、原形式與原酉相位沒有改動；\(s\) 依賴由凍結時鐘強制決定，不是擬合。一般 \(\kappa_{\epsilon,s}\) 非酉；當 \(\epsilon\operatorname{Re}s=0\) 時才保證酉性。

所以 (14) 雖有 scalar 測地衰減 \(e^{-su}\)，剩餘表示仍攜帶依賴 \(s\) 的真時間修正；不能把它敘述成「已找到共同 ambient physical roof 加固定酉表示」。

## 5. 每個 primitive ambient 閉軌的精確 factorization

固定一條**有向 primitive** ambient geodesic \(c\)，其最小幾何周期為 \(L>0\)，取 \(q\in c\)。令

\[
X=p^{-1}(q),\quad \sigma(y)=\phi_0^L y,\quad
\tau_y=t_\epsilon(L,y)>0,\quad A_y=U_y(L),\quad
W_c(s)=\mathcal A_{\epsilon,s}(L,q).
\tag{15}
\]

於是 \(W_c(s)v_y=e^{-s\tau_y}A_yv_y\)，結果放在 \(E_{\sigma y}\)。這一定義以正向 path lifting 為準；若轉回 [P31 左 cosets][cycles]，需遵守其 §1.1 的 inverse-arrow 對照，不能只抄 permutation 而忽略方向。

對 cycle \(\mathcal O=(y_0,\ldots,y_{d-1})\)，定義

\[
H_{\mathcal O}=A_{y_{d-1}}\cdots A_{y_0},\qquad
T_{\mathcal O}=\sum_{j=0}^{d-1}\tau_{y_j}.
\tag{16}
\]

矩陣在向量上由右向左作用；非交換的 \(A_y\) 不能任意換序。

**引理 5。** cycle 首次閉合的 lift \(P_{\mathcal O}\) 是 cover primitive orbit，且

\[
T_{\mathcal O}=T_\epsilon(P_{\mathcal O})
=dL+\epsilon\int_{P_{\mathcal O}}\alpha_f.
\tag{17}
\]

**證明。** 任意 cover 幾何返回必投影為 \(q\) 的返回，故其幾何時間為 \(nL\)。sheet cycle 的最小性使首次返回為 \(dL\)。正時間變換不增刪閉軌或使首次遍歷變成本原冪；其首次物理周期是 (3) 沿完整 lift 的積分。相鄰的 \(d\) 段正好分割該 lift，給 (17)。□

同一 lifted orbit 在 \(p^{-1}(q)\) 中的全部交點恰構成一條 \(\sigma\)-cycle；不同 cycles 因此不重複 owner。這是 orbit 的分類，不是以 trace、同調或 period 數值合併 owners。

**定理 6（有限 block-cycle determinant）。** 對所有 \(s,z\in\mathbb C\)，

\[
\boxed{\det(I-zW_c(s))=
\prod_{\mathcal O\in X/\langle\sigma\rangle}
\det\!\left(I-z^{d_{\mathcal O}}
e^{-sT_\epsilon(P_{\mathcal O})}H_{\mathcal O}\right).}
\tag{18}
\]

**證明。** \(W_c\) 保持各 cycle 直和。對單一 \(d\)-cycle，若 \(d\nmid n\)，\(W_c^n\) 沒有對角 block，故 trace 為零；若 \(n=dr\)，每個對角 block 的 holonomy 與 \(H_{\mathcal O}^r\) 共軛，scalar weight 為 \(e^{-srT_{\mathcal O}}\)，所以

\[
\operatorname{Tr}W_c^{dr}|_{\mathcal O}
=d\,e^{-srT_{\mathcal O}}\operatorname{tr}H_{\mathcal O}^r.
\tag{19}
\]

在 \(z=0\) 的形式級數環使用

\[
\log\det(I-zW_c)=-\sum_{n\ge1}\frac{z^n}{n}\operatorname{Tr}W_c^n
\tag{20}
\]

即得各 cycle 因子的 log 展開。兩邊都是常數項為 1 的有限多項式，故形式等式給所有 \(z\) 的多項式恆等式。□

由 (14)，左邊也可寫為

\[
\det\!\left(I-ze^{-sL}\operatorname{Hol}_{F_{\epsilon,s}}(c)\right).
\tag{21}
\]

因此不需 \(\rho_\epsilon\) 下降，rank-\(12m\) induced monodromy 已逐 lift 重現**真**周期，而不是把每個周期冒充為 \(dL\)。這裡的「重現」保留 cycle 標籤及 (16)；不宣稱僅由未標記 determinant 就能唯一反演所有 owners 或 periods。

每個 cover primitive orbit 投影為某個 ambient primitive 幾何軌道的正整數次遍歷，故相同論證覆蓋其所屬 family。對任意**有限** ambient primitive 集合 \(\mathcal C\)，(18) 相乘給全部相應 lift 因子的精確有限乘積。沒有從此有限等式推導無窮乘積收斂或解析延拓。

## 6. Gauge、起點及細分

若逐纖維換酉框架 \(g_y\)，

\[
A_y'=g_{\sigma y}A_yg_y^{-1},\qquad
W_c'=GW_cG^{-1},\qquad
H_{\mathcal O}'=g_{y_0}H_{\mathcal O}g_{y_0}^{-1}.
\tag{22}
\]

故 (18) gauge invariant。cycle 改起點給 cyclic-conjugate holonomy，亦不改因子。沿 ambient orbit 改基點，由 (9) 給 monodromy 的相似變換；該 conjugator 對一般 \(s\) 未必酉，但 determinant 不變。

把某段再分割時，時間相加、平坦傳輸按路徑次序相乘，故閉軌的 \(e^{-sT}H\) 不變。輔助變數 \(z\) 計數的是**所選離散步數**；若改變整個 section 或步數定義，不能要求含 \(z\) 的式子逐字不變。其 \(z=1\) 閉軌因子才不依賴這種段落細分。

## 7. 真正反向：\(\epsilon\) 反號與酉伴隨

令 \(\mathsf R(v)=-v\)。因 \(E\) 從 footpoint 底面拉回，\(E_{\mathsf Ry}=E_y\) 有自然酉識別；這是以下反向公式使用的條件。若改用任意 \(M\) 上局部系，須另給 \(\mathsf R^*E\simeq E\) 的相容資料，不能省略。

由 \(a(\mathsf Rv)=-a(v)\)，

\[
T_\epsilon(P^{-1})=\ell(P)-\epsilon I(P)
=T_{-\epsilon}(P),\qquad
H(P^{-1})=H(P)^{-1}=H(P)^*.
\tag{23}
\]

其中 \(I(P)=\int_P\alpha_f\)。這是凍結參數族的數學比較，不是更改當前 \(\epsilon\) 或授權新實驗。

更精確地，正向邊 \(y\to\sigma y\) 的反向邊是 \(\mathsf R\sigma y\to\mathsf Ry\)，其 \(\epsilon\)-時間為原邊的 \(-\epsilon\)-時間，酉 transport 為 \(A_y^*\)。在 (6) 的自然反向識別 \(\mathsf J:F_q\to F_{\mathsf Rq}\) 下，

\[
\boxed{\mathsf J^{-1}W_{\bar c,\epsilon}(s)\mathsf J
=W_{c,-\epsilon}(\bar s)^*
=W_{c,-\epsilon}(-s)^{-1}.}
\tag{24}
\]

證明只需比較 \(E_{\sigma y}\to E_y\) 的 block，兩側均為 \(e^{-s\tau_{-\epsilon,y}}A_y^*\)。一般的 \(W_{c,\epsilon}(s)^{-1}\) 卻帶 \(e^{+s\tau_{\epsilon,y}}\)，不是 (24)。特例中可能重合，不構成省略兩個參數變換的理由。

反向 family 與正向 family 的識別遵守 [P31 §7][cycles]：除非另有 exact ambient reverser，不能在固定 family 裡自行 inverse pairing，更不能將每條 cycle 當作自逆 owner。

## 8. 能改變什麼，不能推出什麼

由 (19)–(20)，單 cycle 的 log 因子為

\[
-\sum_{r\ge1}\frac{z^{dr}}r e^{-srT}\operatorname{tr}H^r.
\tag{25}
\]

改變合法的酉 holonomy 可改振幅、相位及零點，也可能讓 \(\operatorname{tr}H^r\) 消失，或讓同頻項相消。這裡指固定、\(s\)-independent 局部系 \(E\) 的 \(H\)，不是把 (11) 的時鐘角色當作可自由選取的相位。對 \(s=\sigma+it\)，其實頻率支撐仍包含於固定的 \(\{rT_\epsilon(P)\}\)；不會新增原先欠缺的 \(\log p\)。這是 log/trace 展開的支撐陳述，不是說 determinant 的零點位置固定。

當 \(\rho_\epsilon\) 不下降時，cover 的 \(X_\epsilon\) 一般不投影成 \(N\) 上單一向量場，因為

\[
Dp_y(X_\epsilon(y))=X_{\rm geo}(p(y))/\rho_\epsilon(y).
\tag{26}
\]

在同一 fiber 上要相同，必須 \(\rho_\epsilon\) 相同。故 (8) 的共同參數是 \(u\)，不是讓所有 cover sheets 同步的物理時間 \(t\)；(14) 也不消除此區分。

有限 rank 只描述 coefficient bundle，不是空間變數上的 transfer operator 有限維。本筆記尚未構造全局 coding、共同 Banach/Hilbert domain、核性、trace formula、Fredholm determinant、meromorphic continuation 或 cusp/scattering 正則化。也未證固定 self-adjoint operator 的全局 determinant 等式。任何此類結論均不能由 (18) 或 \(s\in i\mathbb R\) 時的有限纖維酉性直接取得。

**後續提議，未證且未執行。** 可以詢問 (14) 的 \(s\)-依賴誘導局部系是否有同一函數空間上的解析 transfer-operator 實現，並在明示 cusp 條件下得到與 (18) 相容的正則化 determinant。需要先處理 parameter-dependent coefficient 與 cusp tails；不能直接套固定表示的結論，也不能以 prime/zero 擬合來補缺。

## 9. 文獻位置與實際檢查

有限覆蓋與 induced representations 的 Artin 思想不是本筆記的優先權主張。Brenner–Spinu 在有限體積雙曲三維商及有限維酉表示的設定證明 Selberg zeta 的誘導等式，並在相應規範下證明 scattering function 的等式；這是已存在的相鄰機制，不是本文時間變換與 \(s\)-依賴表示的解析證明。來源：E. Brenner and F. Spinu, *Artin formalism for Selberg zeta functions of co-finite Kleinian groups*, Journal de théorie des nombres de Bordeaux **21** (2009), 59–75，DOI [10.5802/jtnb.657](https://www.numdam.org/articles/10.5802/jtnb.657/)。本輪只以該官方頁的摘要與書目確認這段有限範圍定位；未冒充全文 theorem audit。

已讀 ARS 0.1.28 router、academic-paper workflow、argument-builder 指令及 `docs/workflow.md`；使用有界的 claim/proof/counterclaim 寫作方式，未啟動 full pipeline 或生成評分、審稿通過及 venue readiness。本文是 AI 輔助的內部紙面推導。

實際操作限於檔案定位與讀取、上述普通一手來源查核、檔案存在性/行數/字元檢查、SHA-256，以及 `apply_patch` 新增本文件。一次 `git status --short -- <本新文件>` 回報工作目錄不是 Git repository；沒有嘗試修復、初始化或同步。沒有執行科學程式、矩陣/coset 枚舉、frozen-input replay、實驗或 manuscript build。

寫入前讀取的兩個来源 SHA-256 為：

- [P31 cycle 筆記][cycles]：`cd4132329a3903f148b3529941dd92170f86df67a04f691e6525f3fbde19d895`。
- [P26 README][clock]：`89f62e461e3c6c367940c941d51f1758738e662ae58aec4ad59638a7e4c29f32`。

雜湊只確認這兩份讀取來源的身分與後續未改動，不證明數學結論或全 workspace 無變更。唯一授權寫入目標是本文件；其他 writer 的工作、舊輸入、歷史失敗、receipts、正式稿與 Route/Stage 狀態均不由本筆記修改。

[cycles]: internal_coset_cycle_lifts_and_oriented_class_splitting_20260909.md
[clock]: ../../26-level11-newform-time-change/README.md#frozen-dynamical-system
