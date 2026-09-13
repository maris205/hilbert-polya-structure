# P33 內部理論：實際八邊形與 Poincaré 幾何證書

日期：2026-09-09 UTC。Goal01 的有界內部論證；本文件是新寫的紙面幾何證書，不是舊 canonical 回執的更新。固定 S01 控制參數、八字母、曲率負一、基點 0、`Lambda=21/10`、`abs(alpha)^2<=20000`、磁場與 owner 約定。沒有運行符號程序、科學計算、BFS、producer、fixture 或實驗；不改舊輸入、協議、鎖、Stage／Route 或認證狀態。

本文把[精確狀態筆記][exact]尚未供給的基本域識別接到一個明確引用的多邊形定理。本地證明包括凸性、端點等式、半平面換側、全部有向邊循環、角度及 SU relator；Poincaré 定理本身是外部前提，不聲稱在此重證。有限 owner 商由另一單元處理。

## 1. 凍結定義、作用方向與實際端點

[凍結 JSON 的 `definition` 第 100–113 行][control-definition]固定 `a=exp(-1/10)`、`x=exp(-1/5)`、`N=-1/sqrt((1-x)(2x-1))`、角度 `pi/4` 及四個生成元。以

\[
u=e^{-1/10},\quad x=u^2,\quad t=1-x,\quad k=2x-1,\quad y=\sqrt{tk}>0
\tag{1}
\]

書寫它們。此處 t 是代數簡寫，不是流的時間；k 不是頂點下標。由 \(e^{-1/5}>1-1/5\)，有 \(4/5<x<1\)，故 u、t、k、y 皆正。令

\[
B_0=x+it,\quad B_1=t+ix=i\overline{B_0},\quad
B_2=iB_0,\quad B_3=iB_1,
\qquad
g_j=-\frac1y\begin{pmatrix}u&B_j\\\overline{B_j}&u\end{pmatrix}.
\tag{2}
\]

凍結 `rotation_R` 記為 \(\mathsf R=\operatorname{diag}(e^{i\pi/4},e^{-i\pi/4})\)，以免與下文 relator \(\mathcal R\) 混淆。其圓盤作用是 z↦iz，(2) 正是 \(g_2=\mathsf Rg_0\mathsf R^{-1}\)、\(g_3=\mathsf Rg_1\mathsf R^{-1}\)。

\[
|B_j|^2=x^2+t^2,\qquad x-|B_j|^2=tk=y^2.
\tag{3}
\]

所以 (2) 的 determinant 精確為 1，具有 SU(1,1) 形式；逆矩陣由 \(B_j\mapsto-B_j\) 得到。採用

\[
\begin{pmatrix}\alpha&\beta\\\bar\beta&\bar\alpha\end{pmatrix}[z]
=\frac{\alpha z+\beta}{\bar\beta z+\bar\alpha}.
\tag{4}
\]

矩陣乘積右端先作用；整體 ± 號不影響圓盤作用。由 \(|\alpha|>|\beta|\)，分母在單位圓盤內不為零；這些是定向保持雙曲等距映射。

設 \(b=1/(\sqrt2u)\)，並取八個不同端點

\[
v_{2m}=i^mu,\qquad v_{2m+1}=i^m\frac{1+i}{2u},\qquad m=0,1,2,3.
\tag{5}
\]

以下頂點／邊下標皆模 8。它們是 [Nazarenko §2、(10)–(11)][S01] 的頂點在實際凍結參數下的寫法；本文不用來源中的 Fuchsian 宣告代替以下檢查。由 \(1/\sqrt2<u,b<1\)，所有頂點都在圓盤內。又 \(u^4=e^{-2/5}>3/5>1/2\)，故 b<u；兩半徑不相等，沒有以 regular Bolza 八邊形替代控制組。

## 2. 緊致、嚴格凸性及中心內外半徑

令 D 是按 (5) 順序連接雙曲測地邊 \(s_j=[v_j,v_{j+1}]\) 的閉區域。Klein 變換及徑向函數為

\[
K(z)=\frac{2z}{1+|z|^2},\qquad f(r)=\frac{2r}{1+r^2},\qquad
f'(r)=\frac{2(1-r^2)}{(1+r^2)^2}>0.
\tag{6}
\]

這是保極角的徑向同胚。與單位圓正交、圓心 c 的邊圓滿足 \(2c\cdot z=1+|z|^2\)，故變成直線 \(c\cdot K(z)=1\)；直徑仍為直徑。因此測地邊和半平面對應到直線邊和半平面。

寫 \(U=f(u),V=f(b),W=V/\sqrt2\)，則

\[
2\sqrt2/3<U,V<1,\qquad U>V/\sqrt2,\quad V>U/\sqrt2.
\tag{7}
\]

Klein 頂點依次是 \((U,0),(W,W),(0,U),(-W,W),(-U,0),(-W,-W),(0,-U),(W,-W)\)。相鄰線段各在自己的角扇區，故閉折線簡單。第一條定向邊的邊向量是 \((W-U,W)\)；其與其餘六個頂點相對第一頂點的向量之叉積依次為

\[
U(2W-U),\quad2W^2,\quad2UW,\quad2UW,\quad U^2,\quad2W(U-W),
\tag{8}
\]

全部嚴格正。其他偶數邊由旋轉得到，奇數邊旋轉後交換 U、V 得同一檢查。故每一邊都是凸包的嚴格支撐邊；原點的叉積為 UW>0。這證明八頂點凸包就是 K(D)，D 嚴格凸且原點在內部。凸包含於半徑小於 1 的閉圓盤，逆變換給 D 緊致。

每邊的兩 Klein 半徑 p、q 都大於 \(2\sqrt2/3\)，夾角 \(\pi/4\)。令 p≥q；邊長 L 和整條支撐直線距原點的距離 h 滿足

\[
L^2=p^2+q^2-\sqrt2pq<p^2,\qquad
h=\frac{pq}{\sqrt2L}>\frac q{\sqrt2}>\frac23.
\tag{9}
\]

凸半平面交遂含閉 Euclidean 圓盤半徑 2/3。因 \(f(1/4)=8/17<2/3\)，(6) 拉回並積分雙曲線元，得

\[
\overline B_{\mathbb H^2}(0,\rho_0)\subset\operatorname{int}D,
\qquad \rho_0=2\operatorname{atanh}(1/4)=\log(5/3)>1/2.
\tag{10}
\]

最後一個嚴格界可由 \(n!\ge2\cdot3^{n-2}\)（n≥2）給 \(e<11/4<25/9\)，從而 \(e^{1/2}<5/3\)。

外半徑也可直接固定為 3：\(u<181/200\)，且

\[
e^3>\sum_{n=0}^{9}\frac{3^n}{n!}=\frac{22471}{1120}>\frac{381}{19},
\qquad22471\cdot19-381\cdot1120=229>0.
\tag{11}
\]

所以 \(\tanh(3/2)>181/200>u>b\)。中心雙曲球在 Klein 模型仍是 Euclidean 圓盤，因而測地凸；它包含全部頂點即包含 D。故 \(D\subset B_{\mathbb H^2}(0,3)\)。

## 3. 全部端點配對及半平面換側

(4) 中消去共同標量 −1/y 後，\(g_0(z)=(uz+x+it)/((x-it)z+u)\)，g1 將上右分子換為 t+ix。四個基本代入完整化為

\[
\begin{aligned}
g_0(v_4)&=\frac{it}{ut(1+i)}=v_1,&
g_0(v_5)&=\frac{(k/2)(1-i)}{(k/(2u))(1-i)}=v_0,\\
g_1(v_5)&=\frac{(k/2)(-1+i)}{(k/(2u))(1+i)}=v_2,&
g_1(v_6)&=\frac{t}{ut(1-i)}=v_1.
\end{aligned}
\tag{12}
\]

分母均非零，由 (1) 可見。旋轉給 g2、g3；所有八個側變換的端點表是

| 變換 | 有序源端點 | 有序像端點 |
| --- | --- | --- |
| g0 | (v4,v5) | (v1,v0) |
| g1 | (v5,v6) | (v2,v1) |
| g2 | (v6,v7) | (v3,v2) |
| g3 | (v7,v0) | (v4,v3) |
| g0^-1 | (v0,v1) | (v5,v4) |
| g1^-1 | (v1,v2) | (v6,v5) |
| g2^-1 | (v2,v3) | (v7,v6) |
| g3^-1 | (v3,v4) | (v0,v7) |

映射為等距同胚，故整條源邊段映到指定邊段，長度也相等。D 在各逆時針邊左側；g_j 將源邊 \((v_{j+4},v_{j+5})\) 映成目標逆時針邊的反向 \((v_{j+1},v_j)\)。定向保持故將源內部半平面映到目標外部半平面。兩閉多邊形的相交只能在目標直線上，且雙方均包含整個目標邊，得到

\[
D\cap g_jD=s_j,\qquad D\cap g_j^{-1}D=s_{j+4},\qquad j=0,1,2,3.
\tag{13}
\]

這是未使用離散性或全局鋪砌的局部結論。

## 4. 兩类實際角度與全部有向邊循環

第一條邊圓的圓心為 \(c=((1+x)/(2u),u/2)\)：它滿足兩端點的 \(2c\cdot z=1+|z|^2\)。在 v0=u，朝 v1 的切線可取 \((-u/2,t/(2u))\)；另一側由實軸反射得到。圓盤保角，因此半徑 u 的頂點內角為 \(2\arctan(t/x)\)。將角色交換為半徑 b 的頂點，\(b^2=1/(2x)\)，同一計算給

\[
\beta_a=2\arctan\frac{1-x}{x},\qquad
\beta_b=2\arctan(2x-1),\qquad \beta_a+\beta_b=\frac\pi2.
\tag{14}
\]

為核對最後等式，令 r=(1-x)/x、s=2x-1；0<r,s<1，且 r+s=1-rs。故兩個主值 arctan 之和在 (0,π/2) 且 tangent=1，即 π/4。沒有把每個內角設成 π/4。

依 [Ormsby §30][Ormsby]，對有向邊 \(e_j=(v_j,v_{j+1})\) 定義配對及「取同一起點的另一條邊」算子 ↓，則

\[
*e_j=e_{j+4}^{-1},\quad *(e_j^{-1})=e_{j+4},\qquad
\Psi=\downarrow*,\quad\Psi(e_j)=e_{j+5},\quad\Psi(e_j^{-1})=e_{j+3}^{-1}.
\tag{15}
\]

全部 16 條有向邊恰分成以下兩個長度 8 的 orbit；從別處起步只是循環位移：

| 方向 | 邊下標順序 | 對應初始頂點下標 |
| --- | --- | --- |
| e0 起的正向 | 0,5,2,7,4,1,6,3 | 0,5,2,7,4,1,6,3 |
| e0^-1 起的反向 | 0,3,6,1,4,7,2,5 | 1,4,7,2,5,0,3,6 |

因 gcd(5,8)=gcd(3,8)=1，這兩個列表沒有遺漏或提前返回。每一列表各含四個 a 類角及四個 b 類角，由 (14) 各有總角 2π，cycle order 都是 1。

## 5. 座標逐次作用、邊 cycle map 與精確 SU relator

定義 \(\tau_j=g_j\)（0≤j≤3）、\(\tau_j=g_{j-4}^{-1}\)（4≤j≤7）。由端點表，\(\tau_j(*e_j)=e_j\)，因此 Ormsby 的側變換 \(\sigma_{e_j}=\sigma_{e_j^{-1}}=\tau_j\)。正向邊 cycle map 為

\[
\mathcal R=\tau_0\tau_5\tau_2\tau_7\tau_4\tau_1\tau_6\tau_3
=g_0g_1^{-1}g_2g_3^{-1}g_0^{-1}g_1g_2^{-1}g_3.
\tag{16}
\]

這正是凍結 `relator` 的乘積，不是凍結 `rotation_R`。但座標頂點序列 0→5→2→7→4→1→6→3→0 **依次施加**的是

\[
g_0^{-1},g_1,g_2^{-1},g_3,g_0,g_1^{-1},g_2,g_3^{-1}.
\tag{17}
\]

其右端先作用的總合成為 \(g_3^{-1}g_2g_1^{-1}g_0g_3g_2^{-1}g_1g_0^{-1}=\mathcal R^{-1}\)。不能把 (16) 從左至右當作 (17) 的逐次作用。若 j_r 是正向列表，向外展开前綴 \(w_0=I,w_r=\tau_{j_0}\cdots\tau_{j_{r-1}}\) 滿足 \(w_r^{-1}v_0=v_{j_r}\)，故 w_rD 的相應角仍在同一 v0。

以下另作純粹 SU 代數檢查，避免依賴近似 relator 或只證到 ±I。設

\[
A=\begin{pmatrix}x+i&u(1-i)\\u(1+i)&x-i\end{pmatrix},\qquad
B=\begin{pmatrix}x+i&u(1+i)\\u(1-i)&x-i\end{pmatrix},\qquad J=\operatorname{diag}(1,-1).
\tag{18}
\]

使用 \(B_0^2=k+2ixt\)、\(B_1=i\overline{B_0}\)、\(y^2=tk\)，逐 entry 相乘得

\[
g_0g_1^{-1}=A/t,\quad g_2g_3^{-1}=B/t,\quad
g_0^{-1}g_1=JAJ/t,\quad g_2^{-1}g_3=JBJ/t.
\tag{19}
\]

例如第一乘積的上左分子為 \(x+iB_0^2=k(x+i)\)，上右分子為 \(u(B_0-B_1)=uk(1-i)\)；另一乘積只交換 (1−i)、(1+i)。再直接相乘，AB 的兩個對角 entries 為 \(x^2-1=-t(1+x)\)，兩個非對角 entries 為 \(2u(x-1)=-2ut\)，所以

\[
P:=g_0g_1^{-1}g_2g_3^{-1}=-\frac1t\begin{pmatrix}1+x&2u\\2u&1+x\end{pmatrix},
\quad Q:=g_0^{-1}g_1g_2^{-1}g_3=JPJ=-\frac1t\begin{pmatrix}1+x&-2u\\-2u&1+x\end{pmatrix}.
\tag{20}
\]

\[
\boxed{\mathcal R=PQ=\frac{(1+x)^2-4u^2}{t^2}I=I},\qquad
(1+x)^2-4u^2=(1-x)^2=t^2.
\tag{21}
\]

這是正的 SU identity。反向邊 cycle map 為 \(g_0g_3g_2^{-1}g_1g_0^{-1}g_3^{-1}g_2g_1^{-1}\)。若 \(c=g_3^{-1}g_2g_1^{-1}\)，它等於 \(c^{-1}\mathcal R^{-1}c=I\)。因此兩種方向及所有循環起點都一致閉合。

## 6. 引用 Poincaré 定理；不把其結論倒放成前提

**引用的外部定理。** [Ormsby, *Hyperbolic Geometry*, §30、Lemma 30.2、Definition 31.1、Theorem 31.2][Ormsby]：緊凸雙曲多邊形，配有等長、相容於反向的側配對及內部到外部的側變換；若每個有向邊 cycle 的內角和為 2π/n_c（正整數 n_c），則側變換生成離散群，多邊形為其基本域，側關係與 cycle 關係給出完整 presentation。本文使用這個定理，不重證它。

適用條件在本地逐項為：§2 的緊凸性及有限內部頂點；§3 的完整等距配對、無邊自配對及半平面換側；(15) 的反向相容性；§4 的兩個完整 cycle、n_c=1。§5 又獨立核對了精確矩陣 relator。此處沒有理想頂點，故不需要額外 cusp 條件。

**結論。** 令 \(\Gamma=\langle[g_0],[g_1],[g_2],[g_3]\rangle\subset PSU(1,1)\)。由該定理，D 的 translates 覆蓋雙曲平面，不同群元素的 tile 內部互不相交，且

\[
\Gamma\simeq\langle a_0,a_1,a_2,a_3\mid
a_0a_1^{-1}a_2a_3^{-1}a_0^{-1}a_1a_2^{-1}a_3=1\rangle,
\qquad a_j\longmapsto[g_j].
\tag{22}
\]

側逆元關係已消去，反向 cycle 關係由 (21) 的逆及共軛得到。故 (22) 是 faithful 的標記，而非僅有滿射或某一 relator 成立。這項 faithfulness 來自引用定理的完整 presentation 結論；不能由有限字可判零或 (21) 單獨推出。

邊內部的兩個半圓鄰域及頂點的完整 2π 扇區給商的普通圓盤鄰域，沒有鏡邊或錐點。頂點全在一個 cycle，故商有一個面、四条邊、一個頂點，Euler 數 1−4+1=−2；配對反轉邊界方向而保持平面定向，故商是閉定向 genus-two 雙曲曲面。其覆蓋作用無挠；緊 D 又给余緊性。這是由實際配對推出的曲面，不是先假定為標準 Bolza。

## 7. 真實鄰接、頂點 star 與 guard 的幾何接口

由 (13)，每條邊已有指定的外側鄰居。若另一 tile 在同一邊的相對內部相鄰，兩個外側 tile 都含那裏的一個開半圓，將造成內部重疊，違反基本域結論。因此完整側鄰居恰為

\[
\mathcal A=\{[g_0],[g_1],[g_2],[g_3],[g_0^{-1}],[g_1^{-1}],[g_2^{-1}],[g_3^{-1}]\}.
\tag{23}
\]

八者不同：若兩者相同，(13) 會把 D 與同一 tile 的相交同時等於兩條不同側。對任意 hD，鄰接正是 \(hD\to haD\)、a∈𝒜，與右乘相容。

在 v0，§5 的八個前綴 tile 各帶來 §4 所列的一個正角；半平面換側使相鄰扇區沿公共邊續接。嚴格正的部分角和小於 2π，完整角和等於 2π，故它們填滿一個小圓鄰域且無內部重疊。基本域內部不交排除額外扇區。由另一方向或平移可得每個頂點的完整八 tile star；其邊鄰接圖是連通的循環。這也排除把只在頂點接觸誤算成一條側鄰接。

由 (10)，不同 g、h 的 \(B(go,\rho_0)\)、\(B(ho,\rho_0)\) 內部分離，否則中心測地線中點屬於兩球。因此 \(d(go,ho)\ge2\rho_0>1\)。以半徑 1/2 的球比較面積，對任何有限中心子集均得

\[
\#\{g:d(o,go)\le T\}\le\frac{\cosh(T+1/2)-1}{\cosh(1/2)-1}.
\tag{24}
\]

因界與有限子集無關，這同時證明中心球有限，不預設其有限性。若緊 K⊂B(o,L) 與 hD 相交，§2 的外半徑給 d(o,ho)≤L+3，故只有有限個此種 tile；鋪砌局部有限。

SU 圓盤公式給 \(\cosh^2(d(o,go)/2)=|\alpha_g|^2\)。固定 guard 因而取 \(\cosh T=39999\)。由 \(e^{1/2}<5/3\)、\(\cosh(1/2)-1>1/8\)，(24) 给

\[
\boxed{\#C_T<8(39999\cdot5/3-1)=533312.}
\tag{25}
\]

這為[前輪內切球／容量筆記][inradius]與[軸到中心筆記][coverage]提供同一實際群的基本域、外半徑 3、完整鄰接及 star 前提。它不是 systole 下界，也不表示整个 C_T 都是 identity-connected；本文不重寫 owner 商或 producer 合同。

## 8. 證據層次、方法與未完成事項

1. 本地公式證明：§§1–5 的有限代數、幾何、兩方向循環；未執行符號或數值矩陣檢查。
2. 外部前提：普通一手瀏覽核讀 Ormsby 作者公開講義 §§30–31；引用其定理到 §6。Nazarenko 只負責模型來源對應。遠端章節／公式定位不冒稱重播舊本地來源 SHA 或完成本地 PDF preflight。
3. 理論接口：§7 的有限性與容量；[精確狀態筆記][exact]另給有限字判定的終止方法。兩者不等於實用固定精度、已實作 codec 或已完成遍歷。
4. 實例仍未完成：版本與 canonical bytes 綁定、完整發現樹／全邊分類、FIFO、root／conjugacy／inverse owner 商、排序流、observed digest、zero unresolved 及獨立 replay。舊 18533 狀態／深度 11 未重播，舊 `PROVED`／`PASS` 不因本文件而更新。

本輪使用 ARS academic-paper 的有界 argument-builder，將本地推導、引用定理及實例證據分開；已讀適用 router、workflow、role 與 repo 指南，不啟動 full pipeline、正式 reviewer 或 Route review。文件唯一寫入為本文件的 `apply_patch`。只讀的行數、引用／文本結構與 SHA 檢查不構成數學或生產認證。

[control-definition]: /root/autodl-tmp/flow_systems/papers/28-bolza-magnetic-flow/results/round7_nonarithmetic_control_matrices.json:100
[exact]: /root/autodl-tmp/flow_systems/papers/33-bolza-control-matched-census/notes/internal_exact_state_identity_and_guard_decidability_20260909.md
[inradius]: /root/autodl-tmp/flow_systems/papers/33-bolza-control-matched-census/notes/internal_inradius_separation_and_explicit_guard_capacity_20260909.md
[coverage]: /root/autodl-tmp/flow_systems/papers/33-bolza-control-matched-census/notes/internal_axis_to_center_coverage_and_finite_guards_20260908.md
[S01]: https://arxiv.org/pdf/1301.5446v1
[Ormsby]: https://people.reed.edu/~ormsbyk/341/hyperbolic_notes.pdf
