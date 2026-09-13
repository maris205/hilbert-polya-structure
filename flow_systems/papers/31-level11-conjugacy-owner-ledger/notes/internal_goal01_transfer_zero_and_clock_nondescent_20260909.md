# P31 Goal 01：零 transfer 與原時鐘不下降

日期：2026-09-09。內部有界理論筆記；將上一輪已核驗的紙面論證首次落盤。
本次授權僅新增本文件；不修改既有聲明、原稿、鎖、receipt、Route 或 Stage 5/6 狀態，
不執行科學程式、實驗、producer、矩陣／coset 枚舉或 frozen 138 inputs。
ARS 的來源核對與論證邊界在此作有限使用；不啟動完整研究到論文 pipeline。

## 1. 結論、對象與失敗假設 H31

沿用 P26 的固定形式與時鐘，令
\[
G=\mathrm{PSL}_2(\mathbb Z),\quad
\Gamma=\Gamma_0(11)/\{\pm I\},\quad
\omega=2\pi i f(z)\,dz,\quad \alpha=\operatorname{Re}\omega,
\qquad f=q-2q^2-q^3+\cdots\in S_2(\Gamma_0(11)).
\]
在 \(M_\Gamma=\Gamma\backslash\mathrm{PSL}_2(\mathbb R)\) 上，
\(a(v)=\alpha(v)\)、\(\rho_\varepsilon=1+\varepsilon a\)，而實際向量場為
\(X_\varepsilon=X_{\rm geo}/\rho_\varepsilon\)。本文件只取固定的正密度區間
\(|\varepsilon|<\|a\|_\infty^{-1}\)，不改換速度／slowness 慣例。
記 \(\pi:M_\Gamma\to M_G\) 為十二層覆蓋；下文所有時間積分皆用單位速
geodesic 參數 \(t\)。來源與其支持範圍見 §7。

**定理。** 存在同一個 ambient primitive oriented geodesic family，令其基軌道
長度為 \(L\)，各 primitive lifts 為 \(P_O\)，首次返回度數為 \(d_O\)，則
對每個上述區間內的 \(\varepsilon\ne0\)，均有
\[
\boxed{\min_O\frac{T_\varepsilon(P_O)}{d_O}
<L<\max_O\frac{T_\varepsilon(P_O)}{d_O}.}
\tag{1}
\]
同一個 family 對所有這些非零 \(\varepsilon\) 適用；不是每個 family 都必須有差異。

保留並否定的失敗假設為
\[
\mathrm{H31}:\qquad
\rho_\varepsilon=\pi^*\bar\rho+X_{\rm geo}u
\quad\hbox{在整個 }M_\Gamma\hbox{ 上成立},
\tag{2}
\]
其中 \(\bar\rho\) 可為任意 ambient 相空間密度，\(u\) 單值且沿每條閉 geodesic
軌道為 \(C^1\)。定理否定非零 \(\varepsilon\) 的 (2)，不要求 \(u\) 全局有界。
\(\varepsilon=0\) 時 \(\bar\rho=1,u=0\) 當然成立。
這是存在性結論，**沒有定位 frozen 138 rows 中的任何具體反例**。

## 2. 群乘法、左右陪集及 primitive lifts

群元素以矩陣／Möbius 變換左作用於 \(\mathbb H\)；\(gh\) 表示先 h 後 g。
使用右陪集集合
\[
\Gamma\backslash G=\{\Gamma a_i:1\le i\le12\},\qquad
\Gamma a_i\longmapsto\Gamma a_i g.
\tag{3}
\]
指標 12 可直接看出：左陪集 \(G/\Gamma\) 經 \(h\Gamma\mapsto h\infty\)
識別為 \(\mathbb P^1(\mathbb F_{11})\)，因 \(\Gamma\) 正是 infinity 的 stabilizer，
且 \(T^zS\infty=z\) 給出所有十一個有限點。
取逆 \(h\Gamma\mapsto\Gamma h^{-1}\) 將左乘 r 變為右乘 \(r^{-1}\)。
所以本文件右乘 r 的正向 monodromy，對應左陪集上左乘 \(r^{-1}\)，**不是 r**。
兩個 inverse permutations 的 cycle 集合與度數相同，但箭頭不可混用。

固定正向 ambient primitive hyperbolic \(R\in G\)。若 \(O\) 是右乘 R 的 cycle，
從 \(\Gamma a_i\in O\) 出發的最小返回度數為 \(d=d_O\)，則
\[
\Gamma a_iR^d=\Gamma a_i,\qquad
P_i=a_iR^da_i^{-1}\in\Gamma,\qquad \ell(P_i)=dL,
\quad L=\ell(R)>0.
\tag{4}
\]
若沿用左陪集代表 \(h=a_i^{-1}\)，同一個提升元素即 \(h^{-1}R^dh\)。
R、\(a_i\)、\(P_i\) 在此皆為 projective 元素；取正跡 hyperbolic lifts 時，
同一公式可在 \(\mathrm{SL}_2(\mathbb Z)\) 中成立，代表的中心符號不改共軛結果。
相空間方向亦可直接核對：令 \(b_t=[\operatorname{diag}(e^{t/2},e^{-t/2})]\)，
選 g 使 \(Rg=gb_L\)。fiber points \(q_i=\Gamma a_i g\) 在流
\(\Phi^t(\Gamma g)=\Gamma gb_t\) 下滿足
\(\Phi^Lq_i=\Gamma a_iRg=q_{\sigma_R(i)}\)。左乘離散群在此相空間自由，
所以 ambient 曲面的 elliptic 點不妨礙這個十二層 flow cover。

以下給出所需 root／cycle 事實，以免把有限返回誤當本原性的證明。
hyperbolic 元素在 \(\mathrm{PSL}_2(\mathbb R)\) 的中心化子是保持其軸方向的
一參數對角群，與 \(\mathbb R\) 同構。與離散 G 相交為非零離散循環群。
因此每個 hyperbolic 元素都有沿其正方向的唯一 ambient primitive root；
對本原 R 及 \(d\ge1\)，有 \(C_G(R^d)=\langle R\rangle\)。
若 (4) 中 \(P_i=b^k\)、\(b\in\Gamma,k\ge2\)，則 \(a_i^{-1}ba_i=R^j\)，
其中 \(jk=d\)，所以 \(0<j<d\)，違反首次返回的最小性。故 \(P_i\) 本原。

更換代表 \(a_i\mapsto\eta a_i\)、\(\eta\in\Gamma\)，只使 \(P_i\) 作
\(\Gamma\)-共軛；沿 cycle 換起點也只作這種共軛。
若兩個 cycles 的提升共軛，先由長度得其 d 相同，再由
\(a_j^{-1}\eta a_i\in C_G(R^d)=\langle R\rangle\) 得兩陪集位於同一 cycle。
反之，每個形如 \(aR^ma^{-1}\) 的 subgroup primitive 元素，因其最小返回
度數 d 整除 m，而必有 \(m=d\)。故 cycles 恰給全部不同的 primitive oriented
lifts；保留方向，不以 normalizer 或取逆商替代此分類。尤其
\[
\sum_Od_O=12.
\tag{5}
\]

## 3. 實週期同態非零，而且 hyperbolic 類能檢測

權二變換律使 \(\omega\) 為 \(\Gamma\)-不變的全純微分，故 \(\alpha\) 閉。
先把 cusp 用 scaling map 移到 infinity；在其寬度 w 座標
\(q_c=e^{2\pi iz/w}\) 中，cuspidality 給出
正次冪 Fourier 展開，而 \(dz=w\,dq_c/(2\pi i q_c)\)。因此 \(\omega\)
延拓為緊化 \(X_0(11)\) 上的全純微分，沒有 cusp residue。
實際 level 11 子群沒有 elliptic 點：有限階非平凡 projective 元素的整數跡
只能為 \(0,\pm1\)；其模 11 上三角條件要求判別式 \(-4\) 或 \(-3\) 為平方，
但二者模 11 為 7、8，不在平方集 \(\{0,1,3,4,5,9\}\) 中。

令 \(\beta=\operatorname{Im}\omega\)。局部寫 \(\omega=(u+iv)(dx+i\,dy)\)，則
\[
\alpha\wedge\beta=(u^2+v^2)\,dx\wedge dy,
\qquad\int_{X_0(11)}\alpha\wedge\beta>0
\tag{6}
\]
因 \(\omega\ne0\)。若 \(\alpha=dU\) 在緊化上 exact，閉性 \(d\beta=0\)
與 Stokes 定理卻給此積分為零。因此 \([\alpha]\ne0\)；必有非零閉環週期。
該環可避開有限個 cusps，故可在 \(Y_0(11)\) 上表示。

在單連通 \(\mathbb H\) 上取 \(dA=\alpha\)，定義
\[
I(\gamma)=A(\gamma z)-A(z),\qquad \gamma\in\Gamma.
\tag{7}
\]
微分不變性使右邊與 z 無關，並給出 \(I(\gamma\delta)=I(\gamma)+I(\delta)\)。
它正是閉環週期，所以 (6) 證明 \(I\ne0\)。有限階元素的 I 值為零；
parabolic 元素對應 cusp 環的遍歷，其週期因微分延拓而為零。
離散 \(\mathrm{PSL}_2(\mathbb R)\) 群中的其他非平凡元素為 hyperbolic。
故某個 hyperbolic \(h\in\Gamma\) 滿足 \(I(h)\ne0\)；沿其軸正向從 z 至 hz
的積分正是其閉 geodesic 週期。取 primitive \(\Gamma\)-root P，仍有
\(I(P)\ne0\)，因 \(I(P^k)=kI(P)\)。

## 4. Transfer 同態為零：純群論證明

對 (3) 的固定代表，唯一地寫
\[
a_i g=\gamma_i(g)a_{\sigma_g(i)},\qquad \gamma_i(g)\in\Gamma,
\qquad F(g)=\sum_{i=1}^{12}I(\gamma_i(g)).
\tag{8}
\]
右作用慣例給 \(\sigma_{gh}=\sigma_h\circ\sigma_g\)，且
\[
\gamma_i(gh)=\gamma_i(g)\gamma_{\sigma_g(i)}(h).
\tag{9}
\]
對 i 求和，置換不改總和，故 \(F(gh)=F(g)+F(h)\)。
代表更換 \(a_i'=\eta_i a_i\) 時，summand 改變
\(I(\eta_i)-I(\eta_{\sigma_g(i)})\)，總和不變；重排代表亦無影響。
所以 F 是良定的 additive transfer，同時是 \(G\to\mathbb R\) 的同態。

令 \(S=[\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}]\)、
\(T=[\begin{smallmatrix}1&1\\0&1\end{smallmatrix}]\)。二者生成 G：
對 determinant-one 整數矩陣的第一個欄向量反覆左乘 T 的冪與 S，即 Euclidean
algorithm，將其化為 \((\pm1,0)^t\)，餘下矩陣為 T 的冪（到中心符號）。
又 \(S^2=1\)、\((ST)^3=1\) 在 G 中成立，所以任何 \(G\to\mathbb R\)
同態都消去 S、ST，也消去 T。因此
\[
F(g)=0\qquad(g\in G).
\tag{10}
\]

現在取 (8) 的 \(g=R\)。若 \(i_j=\sigma_R^j(i_0)\) 是一個 d-cycle，
按 \(j=0,1,\ldots,d-1\) 的次序乘法得
\[
\gamma_{i_0}(R)\gamma_{i_1}(R)\cdots\gamma_{i_{d-1}}(R)
=a_{i_0}R^da_{i_0}^{-1}=P_O.
\]
故 (10) 恰給出
\[
\boxed{\sum_O I(P_O)=0.}
\tag{11}
\]
這是對各完整 lift 的週期各算一次，不是 \(\sum_O d_OI(P_O)\)。
全程只用有限陪集與群同態；不需假定非緊 orbifold 上的某個解析 trace
算子有良好域，也不需 \(L^2\) 或 compact-support 條件。
若用微分形式表達，相容的 convention 是
\(\operatorname{Tr}\alpha=\sum_{\Gamma a_i}a_i^*\alpha\)，不是對左陪集代表
不加取逆便作同一求和；上面的 F 是其閉環週期。

## 5. 嚴格雙側差異與 H31 的反證

取 §3 的 primitive P，使 \(I(P)\ne0\)，再取其正向 ambient primitive root R。
若 \(P=R^m\)，令 d 為 \(\Gamma\in\Gamma\backslash G\) 的最小返回度數，
則 \(R^d\in\Gamma,d\mid m\)。P 的 subgroup primitiveness 迫使 \(d=m\)。
所以 §2 的 R-family 含有非零週期的 primitive lift。
由 (11)，該 family 必同時含 \(I(P_O)>0\) 與 \(I(P_O)<0\)。
原時鐘的定義直接給
\[
T_\varepsilon(P_O)=\int_{P_O}\rho_\varepsilon\,dt
=d_OL+\varepsilon I(P_O),\qquad
\sum_OT_\varepsilon(P_O)=12L.
\tag{12}
\]
正、負週期各除以正整數 \(d_O\)，乘任意非零 \(\varepsilon\) 後仍有兩種符號，
即得 (1)。這補充的是本次 newform-specific transfer 論證；不把舊筆記
僅憑 coset 度數不得推斷實際週期的警告，改寫成當時已證 (12)。

若 (2) 成立，沿一條 primitive lift 積分，單值性給
\[
\int_0^{d_OL}X_{\rm geo}u(\Phi^t q)\,dt
=u(\Phi^{d_OL}q)-u(q)=0.
\]
\(\pi^*\bar\rho\) 則沿同一 ambient 閉軌道遍歷 \(d_O\) 次，故
\[
\frac{T_\varepsilon(P_O)}{d_O}
=\int_0^L\bar\rho(\Phi^t\pi q)\,dt
\]
對該 family 全部 O 相同，與 (1) 矛盾。證畢。
此處 X 必須是 \(X_{\rm geo}\)：不能把 \(X_\varepsilon u\) 未經換測度就當作
geodesic 時間中的全微分。也未使用任何 Livšic 逆命題。

## 6. 有界推論：閉軌條件與有限 determinant 的共同標量化

對任意有限 flow cover，若正密度 \(\rho=\pi^*\bar\rho+Xu\)，且 X 為共用的
原流生成元、u 在閉軌上單值可微，則每個 primitive base family 必滿足
\(T_\rho(P_O)/d_O=A\)，其中 A 是該 base orbit 的 \(\bar\rho\) 積分。
這是必要條件，不在此聲稱跨所有 families 的此條件充分推出光滑／可測下降。

只固定一條長度 L 的 base orbit，在其十二個 fiber points \(q_i\) 定義
\(\tau_i=\int_0^L\rho(\Phi^tq_i)\,dt\)，使 \(\Phi^Lq_i=q_{\sigma(i)}\)。
令 \(P_\sigma e_i=e_{\sigma(i)}\)，並採用 source-column weight convention
\[
W_s e_i=e^{-s\tau_i}e_{\sigma(i)},\qquad
D_R(z,s)=\det(I-zW_s)
=\prod_O(1-z^{d_O}e^{-sT_\rho(P_O)}).
\tag{13}
\]
每個 cycle 上 \(W_s^{d_O}=e^{-sT_\rho(P_O)}I\)，且任一 basis vector 為 cyclic
vector，故其 characteristic polynomial 為 \(\lambda^{d_O}-e^{-sT_\rho(P_O)}\)，
直接證明此有限代數等式。
z 計數的是完整 base period 的次數，不是跨全部 base orbits 的統一 symbolic 時間。

共同實 roof A 的對角 gauge 標量化作為 s 的恆等式成立，當且僅當全部
\(T_\rho(P_O)=d_OA\)：
必要性由循環權重相乘；充分性在各 cycle 遞推
\(b_{\sigma(i)}=b_i+\tau_i-A\)，總和為零恰保證閉合。此時
\[
W_s=D_s(e^{-sA}P_\sigma)D_s^{-1},\qquad
D_se_i=e^{-sb_i}e_i.
\tag{14}
\]
對 (1) 的 family，任意非零允許的 \(\varepsilon\) 都使 (14) 不可能。
更強地，固定任意實 \(s\ne0\)，(13) 的各 cycle 因子之 z-roots 模長為
\(e^{sT_\varepsilon(P_O)/d_O}\)，至少有兩種；共同標量 permutation 的所有
z-roots 則只有模長 \(e^{sA}\)。因此連其完整 z-determinant 也不可能相等。
此論證只論實 s 與實 A；\(s=0\) 的退化相等不受否定。

零 transfer 卻仍固定最高次係數：由 (12)，\(\det W_s
=\det(P_\sigma)e^{-12sL}\)。因此總週期／最高次係數相同，並不消除 cycle
間差異，也不證明整個 determinant 為共同標量形式。
這只是單一 family 的有限矩陣推論；沒有構造全局 section、transfer operator、
Fredholm determinant、解析延拓、Euler 乘積或任何 automorphic determinant 等式。

## 7. 來源支持、核對記錄與未解義務

- [P26 README，Frozen dynamical system](../../26-level11-newform-time-change/README.md#frozen-dynamical-system)
  固定 normalized level-11 form、\(\omega,\alpha,\rho\)、正區間與週期公式。
  [P31 Phase-1 scope](stage1_phase1_rq_brief.md#scope-boundaries) 明確承接這些定義。
  二者是本地對象／範圍證據，不是本定理的外部獨立證明。
- [William Stein，Modular Forms: A Computational Approach，Example 3.27](https://wstein.org/books/modform/stein-modform.pdf)
  明確給 \(q-2q^2-q^3+\cdots\) 為 \(S_2(\Gamma_0(11))\) 的非零基。
  已於 2026-09-09 用作者站點的可讀正文核對此 passage；只用來支持既定
  normalized cusp form 非零及其空間，不把本文件的 no-go 歸給 Stein，亦不以
  少數 q-coefficients 另行證明完整 eta-product 身分。
- [先前 coset-cycle 筆記](internal_coset_cycle_lifts_and_oriented_class_splitting_20260909.md)
  提供既有左右陪集、orientation 與時鐘限制的對照；本文件 §2 重述並證明所需部分。
  先前 ordinary lookup 的 LMFDB 頁面回傳 reCAPTCHA，沒有繞過或計為成功核驗；
  Stein 的瀏覽器 PDF screenshot 也失敗，故本來源依據是 Example 3.27 的可讀正文，
  不宣稱本地 PDF 結構檢查、圖像核驗或完整書籍閱讀。

本文件的新增證據種類是明示假設下的自含數學推導；AI 協助整理，未經外部獨立
審查。不是文獻綜述；只有一個外部數學來源，不主張跨文獻衝突掃描或 novelty。
本次只做來源／本地定義閱讀及新文件的行數、文本與範圍檢查，未執行科學程式。
工作目錄未被 git 識別為 repository；不據此聲稱有 git diff 或 tracked-clean 證書。

仍未解且不得由本筆記代替的義務：

1. 找到具體 ambient R 與非零 real period 的精確證書，及其是否落在 frozen 138
   rows；存在性證明沒有給出 matrix、owner ID、誤差界或非零數值下界。
2. 全局有限／可數 symbolic coding、roof 的正則性與可和性、operator 空間及真正
   dynamical determinant 的定義／收斂；(13) 不是這些對象的完成證明。
3. 對其他候選 cover／密度若閉軌必要條件成立，其 cohomological descent 的充分
   條件與所需非緊 Livšic 理論；本次只是必要條件失敗的直接反證。
4. 任意修改原稿、既有 H31 記錄、鎖、正式 verdict、Route 或 stage 狀態，皆需
   各自適用的後續授權；本文件未做任何這類升格。
