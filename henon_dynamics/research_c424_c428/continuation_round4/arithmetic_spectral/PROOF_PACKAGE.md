# AS4-S 證明嘗試與精確缺口

2026-09-08 UTC（工具時鐘）。凍結物件見 [FROZEN_QUESTIONS.md](FROZEN_QUESTIONS.md)。
本文件沒有改變全 Salem／全 $\mathbb Q(\beta)$ 輸入的量詞。

## Claim 與 Status

**原完整主張：** 對每個 Salem 數 $\beta$ 及每個
$x\in\mathbb Q(\beta)\cap[0,1)$，給出對實際 greedy 映射
$T_\beta(x)=\beta x-\lfloor\beta x\rfloor$ 的終止週期判定，並在
週期情形給出精確最小 preperiod／period；或者證明相同全域的完整分類。

**原題狀態：`NOT CURRENTLY JUSTIFIED`。** 以下給出實際嘗試：
完整格點和全部共軛遞推、分母剩餘類的精確週期必要條件、以及
凍結時指定的 uniform quadratic 截留機制的失敗。這些都不等於
原題閉合，不把局部方法失敗變成原動力全類 no-go。

## Assumptions 與 Notation

$f(X)=X^d+c_{d-1}X^{d-1}+\cdots+c_0\in\mathbb Z[X]$
是 $\beta$ 的最小多項式。Salem 情形 $d\geq4$ 為偶數，
$c_0=1$。$C\in\mathrm{SL}_d(\mathbb Z)$ 為在有序基
$1,\beta,\ldots,\beta^{d-1}$ 中表示乘 $\beta$ 的 companion matrix。
令 $e=(1,0,\ldots,0)^t$，$r=(1,\beta,\ldots,\beta^{d-1})$
為列明的 row vector，故 $rC=\beta r$。

寫 $x=ry_0$，$y_0\in\mathbb Q^d$ 唯一；$q\geq1$ 為使
$z_0=qy_0\in\mathbb Z^d$ 的最小正整數。令
$x_n=T_\beta^n(x)$，$a_{n+1}=\lfloor\beta x_n\rfloor$，
$B=\lfloor\beta\rfloor$。$\beta$ 非整數，故
$a_{n+1}\in\{0,\ldots,B\}$。

共軛依序記為 $\beta_1=\beta$、$\beta_2=\beta^{-1}$ 和
$\beta_3,\ldots,\beta_d$；後者為成對共軛的模一根。
$\sigma_i$ 是 $\sigma_i(\beta)=\beta_i$ 的 embedding。
所有範數界以下均為 Archimedean，不用 $p$-adic 界替代。

## Strategy 與 Dependency Map

1. 由 companion 格點動力保留實際 floor 和全部分母。
2. 有限軌道等價於全部共軛有界；這是 Schmidt／Maia 已有機制，
   以下直接重建以暴露當前仍缺的 uniform 步驟。
3. 檢查分母有限商是否足夠：它只給必要週期整除條件。
4. 檢查單位圓中心方向的 global quadratic drift；此特定機制被
   一個完整線性代數反證淘汰。
5. 列出原題仍需的全軌道控制，不以有限商或有限前綴填補。

來源適用及實際讀取範圍見 [SOURCE_AUDIT.md](SOURCE_AUDIT.md)。
本文件不是獨立新候選的數學審查；沒有執行數學程序。

## Proof／實際嘗試

### Step 1. 精確格點迴圈，含零點和分支邊界

由 $rC=\beta r$ 和 $re=1$，實際 coefficient state 滿足

$$
y_{n+1}=Cy_n-a_{n+1}e,\qquad
a_{n+1}=\lfloor rCy_n\rfloor,\qquad
z_{n+1}=Cz_n-q a_{n+1}e. \tag{1}
$$

因此 $y_n\in q^{-1}\mathbb Z^d$ 且 $ry_n=x_n\in[0,1)$
對所有 $n\geq0$ 成立。精確等號 $rCy_n\in\mathbb Z$ 時
下一主實坐標為 $0$，之後留在 $0$；這不需要近似的 digit 判斷。
給定精確代數數，其與有理數的次序及等號可判定，因此每一步
(1) 都是有效運算。此處不宣稱這個逐步迭代在非週期情況也會停止。

### Step 2. 全共軛有界性的真正內容

因為 $f$ 在特徵零不可約，其根互異。故 Vandermonde matrix
$V=(\beta_i^{j-1})_{1\leq i,j\leq d}$ 可逆，且

$$
Vy_n=(\sigma_1(x_n),\ldots,\sigma_d(x_n))^t. \tag{2}
$$

$(y_n)$ 有界當且僅當 (2) 的全部坐標一致有界。由 (1)，
一個有界軌道包含在固定離散格點 $q^{-1}\mathbb Z^d$ 的有限集；
兩個相同狀態及確定性使之最終週期。反向由有限初段加有限週期
即得有界。因此

$$
x\text{ 最終週期}
\iff (y_n)\text{ 有界}
\iff \sup_n|\sigma_i(x_n)|<\infty\quad(1\leq i\leq d). \tag{3}
$$

這不是本輪新定理：Maia Theorem 4.1 完整擁有該等價並歸屬
Schmidt Lemma 2.3。只從 (3) 不能得有效截留半徑。

逐步取 embedding 給出精確式

$$
\sigma_i(x_n)=\beta_i^n\sigma_i(x)
-\sum_{k=1}^n a_k\beta_i^{n-k}. \tag{4}
$$

主實坐標由定義有界；穩定實共軛則有

$$
|\sigma_2(x_n)|\leq |\sigma_2(x)|+
\frac{B}{1-\beta^{-1}}. \tag{5}
$$

對每個 $i\geq3$，目前只能直接推出

$$
|\sigma_i(x_n)|\leq|\sigma_i(x)|+nB,\qquad
|\sigma_i(x_n)|=
\left|\sigma_i(x)-\sum_{k=1}^n a_k\beta_i^{-k}\right|. \tag{6}
$$

所以完整原題在這個方法下要求控制**同一條實際 greedy digit
序列**在全部模一共軛上的 oscillatory partial sums，而不是任選
可消去的 digits。Pisot 的 $|\beta_i|<1$ 幾何級數界不能套在 (6)。
上界隨 $n$ 線性增長並不證明實际增長，更不證明非週期。

### Step 3. 原生分母算術有限商：必要而不充分

由 (1)，$z_n\equiv C^n z_0\pmod q$。因 $C$ 是整數
unimodular matrix，$\gcd(q,z_{n,1},\ldots,z_{n,d})=1$：若某個質數
$\ell\mid q$ 除盡 $z_n$，則以 $C^{-n}$ 在 $\mathbb F_\ell$
上逆推也除盡 $z_0$，與 $q$ 最小矛盾。故 coefficient denominator
$q$ 沿軌道保持，不是被穩定坐標的實數收縮消掉。

在有限集 $(\mathbb Z/q\mathbb Z)^d$ 上，$C$ 為置換。
令

$$
r_q(z_0)=\min\{r\geq1:C^rz_0\equiv z_0\pmod q\};
\qquad r_1(0)=1. \tag{7}
$$

如果 $x$ 的 eventual least period 是 $p$，取週期段內任意
$n$，由 $z_{n+p}=z_n$ 和 $C$ 在模 $q$ 上可逆，得
$C^pz_0\equiv z_0\pmod q$，因此 $r_q(z_0)\mid p$。
也可用 CRT 分解 $q$，但那只是相同有限商的經典局部拆分。

反向尚未成立：$C^rz_0\equiv z_0\pmod q$ 只使
$y_{n+r}-y_n\in\mathbb Z^d$，不使差為零。實際 digit carry 的
整數 lift 在中心方向仍可能沒有已證界。有限剩餘類會返回，
不能把這件事改寫成原實數狀態已返回；本輪不另列更多模數表。
這是 (1) 的標準 corollary，不提出新的 prime-owner 宣稱。

### Step 4. 淘汰凍結的 uniform quadratic drift 嘗試

考察一個具體、比原題更強的證明裝置：存在實正定二次型
$Q(y)=y^tHy$、常數 $0\leq\rho<1$ 和 $K<\infty$，只依賴
$\beta$，使每個合法代數狀態 $y\in\mathbb Q^d$、$0\leq ry<1$
均滿足

$$
Q(Cy-\lfloor rCy\rfloor e)\leq\rho Q(y)+K. \tag{8}
$$

若上述係數與常數可有效給定和驗證，這會以幾何級數給出有效
逐軌道界；只有任意實數常數的存在尚不保證有效性。故在凍結時
先檢查更基本的存在性。
但對每一個 Salem $\beta$，(8) 不存在。

**反證。** 設 $E_c\subset\mathbb R^d$ 為全部模一 eigenvalues
的實 invariant subspace，$\dim E_c=d-2>0$。因 $rC=\beta r$，
且 $C-\beta I$ 在 $E_c$ 上可逆，得 $r|_{E_c}=0$。
對任意 $v\in E_c$ 和 $t>0$，選擇有理向量 $y_j\to tv$ 且
$0<ry_j<1/\beta$：先用 $tv+\varepsilon e$ 從 slab 內逼近
$tv$，再利用 $\mathbb Q^d$ 稠密及 slab 開性選取有理逼近。
這些向量對應**合法**全分母輸入，
並且其 digit 為零。對 (8) 取 $j\to\infty$，二次型的連續性給出

$$
t^2 Q(Cv)\leq\rho t^2Q(v)+K.
$$

再令 $t\to\infty$ 得 $Q(Cv)\leq\rho Q(v)$，對所有
$v\in E_c$ 成立。令 $R=C|_{E_c}$，$H_c$ 是 $Q$ 在 $E_c$
上的正定矩陣，則

$$
R^tH_cR\leq\rho H_c.
$$

如 $\rho=0$，左側正定即矛盾。如 $0<\rho<1$，以
$H_c^{-1/2}$ 合同化後，正定矩陣的全部 eigenvalues 不超過
$\rho$；取 determinant 得

$$
|\det R|^2\leq\rho^{d-2}<1.
$$

然而 $R$ 的 eigenvalues 為成對的模一共軛，故
$|\det R|=1$，矛盾。證畢。

這是離散 Lyapunov strict-contraction 的基本譜限制在此實際
greedy branch 上的適用檢查；不是一篇獨立完整 obstruction。
它不排除 input-dependent 非均勻界、多步非線性截留、帶有
確切 entry proof 的格點有限盒，或不同有效負證書。
尤其沒有推出任何 $x$ 的實際 orbit 無界。

### Step 5. 為何來源不能代替剩餘一步

- Maia 的 companion／有界等價和 Pisot 收縮是 Step 1–2 的已有
  理論，不提供 Salem 所需的 (6) 全界。
- Akiyama–Hichri 的 Theorem 1 對正密度的 $m$ 研究
  $d_{\beta^m}(1)$。$T_{\beta^m}$ 不是本題 $T_\beta$ 的
  $m$-iterate：二者的中間 floor 不能任意合併。且單一邊界輸入
  的展開，不等於所有 $x\in\mathbb Q(\beta)$ 的返回。
- Vávra Theorem 2.1 選取 alphabet 與數字選擇器 $D(x)$，使
  多-place 區域不变；沒有證明該 $D(x)=\lfloor\beta x\rfloor$。
  其 Theorem 2.5 又明確排除單位圓共軛，不能用來填 Salem 缺口。
- Hare–Orovec Theorem 2.3 有指定 Pisot 極限、reversibly greedy
  及 cofactor／初始展開假設，只描述特定參數族的 $1$。

所以以下完整義務仍無證明：對**每個**合法 $(\beta,x)$，要麼
得到實際中心和 (6) 的有效有界／entry certificate，要麼得到
真正非週期且可有限識別的 exhaustive alternative。沒有任一個
來源適用結果或本輪推導滿足這個義務。

## Corrections／尚缺假設與最終核查

原題沒有被悄悄弱化。若额外給出經證明且可計算的共軛半徑
$H(\beta,x)$，(2) 可把軌道限定到可列的有限格點盒，再以精確
迭代取得第一重複；該 first-repeat pair 恢復最小 preperiod 和
period。這只是一個**條件式程序**，而 $H$ 的存在與計算正是缺口。
若只逐步找重複，得到的是對正例的 semidecision，並非完整判定。

逐項核查已保持：$x=0$、零 digits、floor 邊界、所有 $q$、所有
偶數 $d\geq4$ 和全部模一共軛。Step 4 的 uniform $(H,\rho,K)$
限制已顯式寫出，不能擴張成所有 Lyapunov 函數或所有證明法失敗。
本輪無全題證明、無已證非週期例、無停止時間上界、無新數學程序，
亦無完整候選可交付非作者准入審查。

## Disposition 與 Open Risks

`AS4_S_FULL_GREEDY_RETURN_UNCLOSED`；
`COMPANION_AND_BOUNDEDNESS_SOURCE_OWNED`；
`QUADRATIC_DRIFT_METHOD_REJECTED_ONLY`；`NO_NEW_CONTRACT`。

這是有界搜尋／證明嘗試的結束，不是全世界不存在更強定理的宣言。
不把有限商週期、代數數域、Salem 譜或任何 source count 提升為
目標 Euler factors、root numbers、automorphy、zero/divisor 對應。
`NO_BAD_EULER_OR_ROOT_NUMBER`。
