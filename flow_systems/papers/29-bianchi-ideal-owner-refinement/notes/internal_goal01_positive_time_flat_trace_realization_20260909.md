# P29 內部論證：正時間 distributional flat trace 的實現

日期：2026-09-09 UTC。Goal 01 的有界紙面推進；只新增本筆記。

**摘要。** 對實際 Gaussian level-(3) 雙曲三流形的完整單位速
測地流，正時間联合傳播子核可拉回至時空對角；有界時間返回類
有限性又使拉回分佈的支撐對時間投影 proper。下文因而定義真正的
\(\mathcal D'((0,\infty))\) flat trace，證明它等於既有自然橫向
權重的閉軌道測度，並給出方向明確的 rank-one unitary 擴張。

本篇閉合的是[自然振幅筆記，§7][amplitude]當時尚未核查的
**正時間聯合核之對角拉回與非緊推送接口**。先前 formal 筆記保持
原樣；本篇不把這一進展改寫成當時已證，也不宣告普通 \(L^2\) 迹、
resolvent flat trace、零時間項、scattering 或全局譜恆等式。

ARS 的有界來源核對與 argument-builder 用於辨認局部文獻證明中
真正使用的假設，並把本案的 proper-support 補充與譜側邊界分開。

## 1. 對象、已證輸入與正時間定理

固定
\[
\Gamma(3)=\{B\in SL_2(\mathbb Z[i]):B\equiv I\pmod3\},\quad
M=\bar\Gamma(3)\backslash\mathbb H^3,\quad Y=SM.
\tag{1}
\]
曲率為 -1；\(\phi_t\) 是完整、無零點的單位速測地流，X 是其
生成元。以下兩項已分別在[實際有限週期包筆記][packets]與
[自然振幅筆記][amplitude]證明：

- 每個有限 \(L>0\) 只有有限個有向正返回類
  \((\gamma,r)\)，其中 \(\gamma\) 是按時間平移取商的本原流軌道，
  \(r\ge1\)，且 \(T_{\gamma,r}=r\ell_\gamma\le L\)。
- 周期橫向空間 \(E^s\oplus E^u\) 維數為 4，其返回譜是
  \(e^{\pm T_{\gamma,r}\pm ir\vartheta_\gamma}\)，没有特徵值 1。
  對正時間返回 \(P_\gamma=d\phi_{\ell_\gamma}|_{E^s\oplus E^u}\)，
  \[
  D_{\gamma,r}:=|\det(I-P_\gamma^r)|
  =4\bigl(\cosh(r\ell_\gamma)-\cos(r\vartheta_\gamma)\bigr)^2>0.
  \tag{2}
  \]

取 scalar 傳播子
\[
U(t)f(x):=f(\phi_{-t}x),\qquad t\in\mathbb R.
\tag{3}
\]
每個固定 t 的流映射為全局微分同胚，故 (3) 作用於
\(C_c^\infty(Y)\) 合法；本篇不以任何 trace-class 性定義其跡。

**定理（真正的正時間 distributional flat trace）。**
式 (3) 的聯合核在 \(t>0\) 有合法對角拉回，其對時間的
support-proper 推送定義與密度、合格空间 cutoff 無關的分佈
\(\mathcal T=\operatorname{tr}^{\flat}_{+}U\)。且
\[
\boxed{\displaystyle
\mathcal T=
\sum_{\gamma\ {\rm primitive, oriented}}\sum_{r\ge1}
\frac{\ell_\gamma}{D_{\gamma,r}}\delta_{r\ell_\gamma}
=\mu^{\rm orb}_0
\quad\text{於 }\mathcal D'((0,\infty)).}
\tag{4}
\]
因此這個分佈實際上是局部有限正 Radon 測度。求和按本原有向
相空間圓周及正整數重複索引，不額外計起點或矩陣共軛代表。

## 2. 聯合圖形核與 wavefront 橫截

固定光滑正密度 dm，例如 Liouville 密度。令 \(K_m(t,x,y)\)
為相對 dm(y) 的聯合 Schwartz 核：
\[
f(\phi_{-t}x)=\int_Y K_m(t,x,y)f(y)\,dm(y).
\tag{5}
\]
這是在 \((0,\infty)\times Y\times Y\) 上的合法分佈核，
支撐於光滑圖形 \(\mathcal G=\{y=\phi_{-t}x\}\)。若局部
\(dm(y)=m(y)\,dy\)，則可寫作
\(m(y)^{-1}\delta(y-\phi_{-t}x)\)。

令 \(y=\phi_{-t}x\)。圖形上的非零 conormal covector 具有形式
\[
\bigl(\eta(X_y),-(D\phi_{-t})_x^*\eta,\eta\bigr),
\qquad0\ne\eta\in T_y^*Y.
\tag{6}
\]
因為 \(\partial_t\phi_{-t}x=-X_y\)，第一項符號如上；乘上光滑
密度因子不增添 wavefront。對聯合對角嵌入
\[
i(t,x)=(t,x,x)
\]
而言，其非零法協向量是 \((0,\xi,-\xi)\)。故拉回可能受阻的
相交必須同時滿足
\[
\phi_{-t}x=x,\qquad \eta(X_x)=0,\qquad
(D\phi_{-t})_x^*\eta=\eta.
\tag{7}
\]
週期點處 \(T_xY=\mathbb RX_x\oplus E^s_x\oplus E^u_x\)，且此
分解對返回映射不變。\(\eta(X_x)=0\) 使 \(\eta\) 由橫向限制
完全決定；(7) 的最後一式要求該限制是橫向返回的固定協向量。
由 (2) 的譜沒有特徵值 1，只能 \(\eta=0\)，與 (6) 矛盾。
所以 \(W_m:=i^*K_m\) 在 \((0,\infty)\times Y\) 上存在。

此處必須先保留聯合時間變量。若先固定週期時間 \(t=T\)，
流方向的特徵值 1 通常使 fixed-time kernel 的對角限制失敗；
\(\mathcal T\) 不是把每一個 t 的數值跡拼起來。

## 3. 緊時間窗的 proper 支撐與 cutoff 定義

令
\[
F:=\{(t,x)\in(0,\infty)\times Y:\phi_t x=x\}.
\tag{8}
\]
F 是閉集，且 \(\operatorname{supp}W_m\subset F\)。對任意
\(J=[a,b]\subset(0,\infty)\)，已有返回類有限性給
\[
F\cap(J\times Y)=
\bigcup_{r\ell_\gamma\in J}\{r\ell_\gamma\}\times\gamma,
\tag{9}
\]
右邊為有限個緊圓周之並。這裡 \(\gamma\) 是**全部相狀態**的
本原周期圓周；即使底空間的閉測地線自交，其速度流圓周仍由流的
唯一性辨識。重複返回使用同一相狀態圓周，不增加起點重數。

因此 \(\pi(t,x)=t\) 在 \(\operatorname{supp}W_m\) 上 proper。
不需要全部時間的週期軌道都留在同一個緊集，也不需要整個非緊
Y 有緊支撐。不存在尚需補進 (9) 的「無窮遠閉包點」：F 在本
流形內已閉，且窗內支撐已是有限緊並；本篇未作空間緊化。

具體地，給定 \(h\in C_c^\infty(0,\infty)\)，選略大緊時間窗
J，使 \(\operatorname{supp}h\subset\operatorname{int}J\)。令
\(Q_J\subset Y\) 是 (9) 中全部圓周之聯集，選
\(\chi_J\in C_c^\infty(Y)\)，使它在 \(Q_J\) 的開鄰域恆為 1。
定義
\[
\langle\mathcal T,h\rangle
:=\langle W_m,h(t)\chi_J(x)\rangle_{dt\,dm(x)}.
\tag{10}
\]
這就是把 \(W_m\) 乘上纖維密度後作 support-proper 推送。

若 \(\chi_1,\chi_2\) 都合格，兩者之差在有關分佈支撐的鄰域
消失，故 (10) 不變。若改變 J，可改用包含兩個窗的更大窗來比較。
對支撐於同一緊時間集的全部 h，可固定同一個 \(\chi_J\)；映射
\(h\mapsto h\chi_J\) 連續進入聯合測試函數空間，因而 (10)
確實定義 \(\mathcal D'((0,\infty))\) 元素。用更大共同窗口亦
直接給出不同 h 之間的線性相容性。

帶有緊集 plateau 的 cutoff exhaustion 對每個固定時間測試函數
最終**精確穩定**，不是僅在某個估計下收斂。必須要求 cutoff 在
圓周的鄰域恆等 1；在尚未求出分佈階數前，只說它在圓周點上
取值 1 不足以保證獨立性。也不能以[packets]中僅與每條閉軌道
相交一次的截尖點緊核代替本處全部 \(Q_J\)。

## 4. 密度抵消與局部係數的實際計算

若 \(dm'=q\,dm\)，其中 \(q>0\) 光滑，則由 (5)
\[
K_{m'}(t,x,y)=q(y)^{-1}K_m(t,x,y),\qquad
W_{m'}(t,x)=q(x)^{-1}W_m(t,x).
\tag{11}
\]
(10) 配對的積分密度同時乘 q(x)，兩者抵消。因此 trace 與選擇
哪一個光滑正密度無關，並不需要先證某個普通算子跡。

以下局部計算對應 [Dyatlov–Zworski，Appendix B，Lemma B.1][dz]。
在 \(\phi_T(x_0)=x_0\)、\(T>0\) 附近取 flow-box 座標
\((u,w)\)，使 \(X=\partial_u\)，且 \(w=0\) 是軌道。
將截面取成在 \(x_0\) 與 \(E^s\oplus E^u\) 相切，寫
\[
\phi_{-T}(0,w)=(F_0(w),A_0(w)),\qquad F_0(0)=0,
\quad A_0(0)=0.
\]
對鄰近 t，流的群性給
\[
\phi_{-t}(u,w)=(u-t+T+F_0(w),A_0(w)).
\tag{12}
\]
由密度獨立性可在此計算中取座標 Lebesgue 密度。聯合對角核於是是
\[
\delta(w-A_0(w))\,\delta(t-T-F_0(w)).
\tag{13}
\]
\(dA_0(0)\) 與反時間橫向返回共軛；故 \(I-dA_0(0)\) 可逆，
在足夠小鄰域中 \(w=A_0(w)\) 的唯一解為 0。對 w 作 delta 換元，
再用 \(F_0(0)=0\)，得到對局部測試函數 \(\Psi\)
\[
\langle W_m,\Psi\rangle_{dt\,dm}
=\frac1{|\det(I-P_\gamma^{-r})|}
\int\Psi(T,\phi_u x_0)\,du.
\tag{14}
\]
積分只跨此 flow box 的軌道弧。由横向維數 4 及
\(\det P_\gamma=1\)，
\[
|\det(I-P_\gamma^{-r})|=|\det(I-P_\gamma^r)|=D_{\gamma,r}.
\tag{15}
\]
這也直接顯示拉回是沿周期圓周的零階 delta density，沒有額外
的 delta 導數項。

对 (9) 的有限緊並使用有限 flow-box 覆蓋與 partition of unity；
其外的部分因沒有固定點而不貢獻。局部 (14) 合成
\[
\langle W_m,\Psi\rangle_{dt\,dm}
=\sum_{\gamma,r}\frac1{D_{\gamma,r}}
\int_0^{\ell_\gamma}
\Psi(r\ell_\gamma,\phi_u x_\gamma)\,du
\tag{16}
\]
對緊支撐 \(\Psi\) 成立。代入 (10) 的 \(h\chi_J\) 即得 (4)。
分子為 \(\ell_\gamma\)，不是 \(r\ell_\gamma\)，因為积分走遍
的是相空間中本原圓周一次。兩個空間方向已是兩個有向流軌道，
不再額外乘 2。分母也仍是完整四維横向行列式，不是平方根。

來源使用的範圍很具體：作者稿正文 pp.24–26 的 (B.2)–(B.5)
與 Lemma B.1 提供上述局部圖形、橫截及 delta 計算；其整篇定理
以緊流形為背景。局部 (12)–(14) 只需光滑 flow box、有限時間流
與 \(I-P\) 可逆，不需 Y 全局緊性。本案取掉空間測試 cutoff 的
理由是 §3 的 proper-support 論證，不是直接引用一個原文未陳述
的本案非緊定理。

## 5. Rank-one unitary 擴張與正向 holonomy 約定

令 \(\Theta\) 為[正返回筆記，§4][positive]的完整自由同調角色
torus；此符號只指角色參數空間，不指 trace 分佈。
取平坦 Hermitian 線叢 \(L_\theta\to Y\)，以**沿正向流圈的
平行移動**定義角色：
\[
\operatorname{Hol}^{+}(\gamma)=\chi_\theta([\gamma]).
\tag{17}
\]
定義傳播子
\[
(U_\theta(t)f)(x)
:=\mathcal P^{+}_{\phi_{-t}x\to x}\,f(\phi_{-t}x),
\tag{18}
\]
其中平行移動路径明確為
\(u\mapsto\phi_{u-t}x\)，\(0\le u\le t\)。它從過去點沿正向流
走至當前點；在 \(t=r\ell_\gamma\) 時正好走正向閉路 \(\gamma^r\)。
因此周期點處纖維返回係數是 \(\chi_\theta(r[\gamma])\)。

聯合核現在取值於 \(\operatorname{Hom}((L_\theta)_y,(L_\theta)_x)\)，
其局部表達只是 scalar 圖形核乘上光滑平行移動因子，wavefront
與支撐論證均不增添新障礙。對角拉回後取纖維迹、再按 §3 推送，
由 (16) 得
\[
\boxed{\displaystyle
\operatorname{tr}^{\flat}_{+}U_\theta
=\sum_{\gamma,r}\frac{\ell_\gamma}{D_{\gamma,r}}
\chi_\theta(r[\gamma])\delta_{r\ell_\gamma}
=\mu^{\rm orb}_\theta.}
\tag{19}
\]
沿同一周期圆周改變起點只把 holonomy 共軛；rank one 時為同一
個純量，因此 (19) 沒有額外起點依賴。

逆角色約定不可忽略。例如若用 universal-cover 配叢 action
\(g\cdot(\widetilde x,z)=(g\widetilde x,\chi(g)z)\)，並以提升終點
\(g\widetilde x\) 標記正向圈，則其正向平行移動是
\(\chi(g)^{-1}\)，不是 \(\chi(g)\)。若採此 convention，須把
配叢角色換成 \(\chi^{-1}\) 以符合 (17)，或把右側寫成
\(\mu^{\rm orb}_{-\theta}\)。本篇不用模糊的「twisted pullback」
省略這個方向選擇。

## 6. 接上自然振幅的 Laplace 界與一般角色障礙

[自然振幅筆記，§2–§5][amplitude]已另證：本群可取
\(\delta=2\operatorname{arcosh}(7/2)>0\)，且存在 \(A>0\) 使所有
unitary 角色 \(\theta\) 及 \(\sigma>0\) 皆滿足
\[
|\mu^{\rm orb}_\theta|([0,L])
\le\frac A2(L+1)(L+2),\qquad
\int e^{-\sigma t}\,d|\mu^{\rm orb}_\theta|(t)
\le\frac A{(1-e^{-\sigma})^2}.
\tag{20}
\]
由 (19)，這現在也是本篇真正正時間 flat-trace 分佈的測度與
Laplace 界，給 \(\operatorname{Re}s>0\) 上的全純變換。
這一步是先有 (19)，再援用已證測度估計；不是從局部 flat trace
的存在性本身推導無窮時間的收斂。

為保持常數時鐘歸一化清楚，令 \(c>0\)，並明定
\(U_{c,\theta}(s):=U_\theta(s/c)\)。新本原周期為
\(c\ell_\gamma\)，橫向返回不變。同一正時間證明或時間變量換元給
\[
\mathcal T_{c,\theta}:=\operatorname{tr}^{\flat}_{+}U_{c,\theta}
=c\,(t\mapsto ct)_*\mu^{\rm orb}_\theta.
\tag{21}
\]
其中整體 c 也可直接由
\(\delta(s/c-T)=c\delta(s-cT)\) 看出。它不同於舊筆記定義的
「固定舊振幅再推送」測度；本篇不省略這個因子。每個固定 c 仍有
\[
\int e^{-\sigma s}\,d|\mathcal T_{c,\theta}|(s)
\le\frac{cA}{(1-e^{-c\sigma})^2},\qquad \sigma>0.
\tag{22}
\]
不聲稱這個估計在所有 c 的範圍內一致有界。

把本次自然正權重代入[實際有限週期包，§6][packets]，三個完整
碰撞包的零 Fourier 係數為正，得到同一開稠密、滿 Haar 測度集合
\(G\subset\Theta\)。[三交換子時鐘筆記][clock]的算術輸入保證
任意 \(c>0\) 至少有一個見證時間不屬於素數對數的有理線性包。
整體正因子 c 不改包的零集，故
\[
\forall\theta\in G\quad\forall c>0:\quad
\mathcal T_{c,\theta}\text{ 不集中於 }
\{k\log p:k\in\mathbb Z_{\ge1},\ p\text{ 為有理素數}\}.
\tag{23}
\]
這是對 (18)、(21) 所明定傳播子族的正時間分佈結論。若比較目標
有指數總變差界，(20)–(22) 也供給共同 Laplace 右域，從而可使用
[正返回筆記，§2–§3][positive]中已明定的唯一性與非原子修正界線。
一般 \(\rho\) 換時或重新指定的束、振幅與算子不由 (21) 包含。

## 7. 仍未建立的接口及本次工作的證據範圍

本篇的 cutoff 獨立性發生在**準確的聯合對角拉回之後**。
不由此推出「先平滑完整非緊核、再無截斷積分」的任意正則化
必得同值，也不交換無窮時間或空間極限。

本篇不建立：

- \(t=0\) 的聯合核拉回、identity／零軌道項，或該處正則化；
- 每個固定時間算子的普通迹、\(L^2\) trace-class 性；
- 時間 Laplace 積分與算子 flat trace 的交換、resolvent flat trace；
- 共振展开、譜跡公式、連續譜／尖點 scattering 項；
- 全局 determinant 恆等式或所有例外角色、非阿貝爾模型的否定。

正時間測度可有其自身的 Laplace 變換，不代表它已等於某個
resolvent 的 flat trace。其在一段零附近正時間上消失，也不能
據此宣告聯合核在 \(t=0\) 的對角拉回存在。

本輪實際核讀 [Dyatlov–Zworski 作者稿 arXiv:1306.4203v4][dz]
正文 pp.24–26 的 Appendix B，尤其 (B.2)–(B.5) 與 Lemma B.1；
它提供局部步驟，不直接提供本案非緊全局命題。§3 的 proper 支撐、
plateau cutoff、連續性與 §5 的方向明定擴張，是本篇逐項展開的
補充。另一次同模型代理覆核只作邏輯校對，不當作獨立科學證據。

這是 AI 輔助內部論證，需主線整合核驗，不是正式證明認證。
實際只讀取工作流、相關筆記與公開作者稿，以 apply_patch 新增
本檔並作一次最小靜態回讀／格式檢查。未執行科學、符號、census、
枚舉、實驗、producer 或 build；先前 formal 筆記、所有舊鎖與
失敗證據保持原樣，任何 Route／Stage 或正式狀態均不改。

[packets]: internal_goal01_actual_finite_period_packets_20260909.md
[amplitude]: internal_goal01_geometric_return_amplitude_and_laplace_bound_20260909.md
[positive]: internal_goal01_positive_trace_and_generic_abelian_twists_20260909.md
[clock]: internal_goal01_null_homology_clock_obstruction_20260909.md
[dz]: https://arxiv.org/pdf/1306.4203v4
