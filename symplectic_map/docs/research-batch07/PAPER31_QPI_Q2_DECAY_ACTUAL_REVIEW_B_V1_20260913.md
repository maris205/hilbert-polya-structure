# Paper31 Q2：全衰减实际数学独立审查 B V1

日期标签：2026-09-13。审查者：`/root/p31_q2_decay_actual_review_b`。
角色：fresh 非作者、实际数学独查 B；未读取审查 A，未编辑 K/E/G 或旧接受输入。
方法：research-review secondary skill，按本轮委派使用当前 secondary xhigh fallback；
没有调用或冒称调用 GPT-5.4 端点，不声称跨模型验证。本件未再委派协作者。
状态：`PROVABLE_AS_STATED / REQUIRED_FIXES_EMPTY / ACTUAL_MATH_REVIEW_ONLY`。
route_applicability: NOT_APPLICABLE。不是正式新意／价值／容量四门，也不先授 Paper31 准入。

## 1. 结论与审查量词

完整纸核结果：K 的混合导数与倒相位导数符号、E 的原光滑椭圆 jets 与全 Fourier 端点式、
G 的原离散相关全局渐近及最优性，均可按现有声明成立；没有发现必须修改的数学错误或缺失科学假设。
这里的数学票仅来自本审查者；是否合取接受及之后的正式四门由主控另行处置。

核查对象始终是任意固定 $T>0$ 的原完整 $U$、原 $F$、$d\mu=|\Omega|$，
以及任意原 $f,g\in C_c^\infty(U)$；$\Pi$ 是逐连通圆均值。
为自包含，原 torus 上的表达是
$F(x,y)=(T/(x-y),x/y)$、$h=-x+y+x/y-T/x$、$\Omega=dx\wedge dy/(xy)$；
这些对象均按 M 延至含四条 terminal 的原完整曲面，而非只使用该坐标表达的定义域。
相关与 Fourier 约定为

$$C_n(f,g)=\int_U[(I-\Pi)f](F^nz)\overline{[(I-\Pi)g](z)}\,d\mu,
\qquad \widehat f_{c,k}=\int_0^1f(z_c(h,\theta))e^{-2\pi ik\theta}d\theta.$$

这里 $\theta$ 为正 Hamilton 时间角，$L$ 为完整正时间周期；内积第一槽线性。
没有缩限为有限 Fourier 模、离节点正距离的观测或删去 terminal 的仿射片。
固定有限能窗和固定参数的常数允许变化；不要求 $T$ 接近阈值或无穷端时一致。
全文只是纯纸核：无 CAS、数值、扫描、枚举、试排或新外部文献判断。

## 2. 终态身份及 FULL 读取范围

已通过实际本地 `wc`、`sha256sum` 与全文读取确认三件终态。以下短名仅在本报告内使用。

| 件 | FULL 行数／字节 | SHA-256 |
|---|---:|---|
| [K] 混合节点符号 | 292／15637 | `f01797fdfaf8bcff40881cac199ff9e06fc1484bc578a2fad2f3c599b129cb79` |
| [E] 椭圆 jets | 377／17873 | `adaa676ad6fd049d65f2137eb52ee158a98604a652bcd7505c62f4ddf9aebfe6` |
| [G] 全局衰减证明 | 358／18193 | `48fff63450138a788e4442c7b94c90e454eeebee2c1960afd895d15577c0cf6f` |

以下五件也 FULL 读取；M/N 只按 D 的既有接受范围消费，不重发旧阶段数学票。
TW/B 消费其既定完整 twist 分类与 acnode 导数；核查的是本轮如何使用这些结论，不重新打开其祖先证明。

| 依赖 | FULL 行数／字节 | SHA-256 |
|---|---:|---|
| [M] 原测度／terminal／投影 | 128／7241 | `cdf173e47f86f4558ad125c5894f825441449bf4ea6c4c8801d31507e8c53700` |
| [N] 节点周期／原离散时间／范数／尾 | 238／12871 | `f50d3291694a6156cac21edfd47af7288ab4fef2b8615c82afe1778471b3d686` |
| [D] 旧数学与预核处置 | 118／9712 | `647f9ff04a023ce6dd889558cfd8834b7a1f7adf451e7fa356543e20bfe4d4ec` |
| [TW] 全实 twist 合成 | 133／6753 | `63f5fb82d37ecb629482d97ccd629ccc0964bcece65edbfb630caf9cd39a0c24` |
| [B] acnode twist 锚定 | 144／7701 | `9c948e5a649754192e781aac8fdec3c2d313645290dd36686f4b8a8e004eb96d` |

另已完整读取 `/root/autodl-tmp/.codex/skills/skills-codex/research-review/SKILL.md` 与 `docs/WORKFLOW.md`。
没有读取 A 的审查稿，没有把 D 中旧审查摘要冒称为本次亲读旧审查全文；未读的历史引用不列入 FULL。

## 3. 逐主张状态

| 主张 | 状态 | 核查依据 |
|---|---|---|
| K C1：完整圆混合导数及原有限阶范数 | PROVABLE_AS_STATED | Euler 导数、隐函数归纳、箱外与接缝检查，见第4节 |
| K C2：全部非零模混合符号 | PROVABLE_AS_STATED | 周期分部积分与共同 gauge，见第4节 |
| K C3：同一个 $1/(\tau/L)'$ 的全阶符号 | PROVABLE_AS_STATED | $R\to\tau(0)A(0)>0$，见第4节 |
| E：定向且半径反号对称的真实时间角 | PROVABLE_AS_STATED | 零均值周期原函数与逆提升，见第5节 |
| E：所有乘积在 $\varepsilon$ 光滑、有限原范数 | PROVABLE_AS_STATED | 偶函数除法与 Fourier 权重，见第6节 |
| E：非驻端点 $-m^{-2}$ 系数及全模 $O(m^{-3})$ | PROVABLE_AS_STATED | 三次分部积分，见第7节 |
| E：退化端点 $m^{-1}$ 系数及全模 $O(m^{-3/2})$ | PROVABLE_AS_STATED | 二次换元与紧支振幅分部积分，见第7节 |
| G：完整 saddle 邻域任意有限幂衰减 | PROVABLE_AS_STATED | 符号闭合、逐层边界与绝对求和，见第8节 |
| G：二次驻相系数、完整余项及全 Fourier 求和 | PROVABLE_AS_STATED | Fourier–Gaussian 恒等式，见第9节 |
| G：原完整曲面的全参数拼合 | PROVABLE_AS_STATED | 持续圆／消失圆分离、固定不变分割，见第10节 |
| G：原单步奇偶、上区间换圆和负时间 | PROVABLE_AS_STATED | Koopman 对易与相位矩阵，见第11节 |
| G：$T\ne1$ 与 $T=1$ 的真实原光滑最优性 | PROVABLE_AS_STATED | 正则圆管模式与中心一阶 jet，见第12节 |
| 本轮新意／价值／22–30页容量／正式准入 | NOT_REVIEWED | 不属于本次实际数学票 |

## 4. K：核清 G 的实际节点输入

K 不是从长时间流的粗估计猜导数。在 $e=pq$ 的固定箱内取
$p=\sigma e^u,q=\sigma e e^{-u}$，则固定 $u$ 时 $D_0=e\partial_e=q\partial_q$，
$\partial_u=p\partial_p-q\partial_q$，两算子对易且在固定物理箱内系数有界。
入口 $u_0=\log|e|-\log r$ 有 $Du_0=1$，因此沿入口的总导数是
$D_0+\partial_u=p\partial_p$，不会出现遗漏的 $q^{-1}$。

对 $I(e,u)=\int_{u_0(e)}^uH(e,v)\,dv$，一次导数为
$D_0I=\int D_0H-H(e,u_0)$。重复此规则给 K 所列端点有限和；
其每一项有界，积分部分至多 $O(\ell)$。至少一次 $u$ 导数后，积分直接变成 $H$ 的有界导数。
所以 $S_u\ge c>0$，$D_0^iS=O(\ell)$，$D_0^i\partial_u^jS=O(1)$ 对 $j\ge1$ 成立。

在 $S(e,u(e,\theta))=\vartheta L(e)$ 中求总阶 $n$ 导数，最高阶未知项唯一为
$S_uD^a\partial_\theta^bu$。其余含 $u$ 导数的项均有至少一个 $S$ 的 $u$ 微分，
故系数有界；低阶 $u$ jets 的总阶不超过 $n$，归纳得 $O(\ell^n)$。
纯能量导数项只有 $O(\ell)$，不破坏该界。恢复 $p,q$ 后每项仍带一个有界 $p$ 或 $q$，
于是 $D^a\partial_\theta^b(f\circ z)=O(\ell^{a+b}\|f\|_{C^{a+b}})$。

箱外 $z=Z_j(e,\vartheta L-c_j)$ 使用统一有界短时流图；接缝是同一光滑 $z$ 的重叠表达，
没有对移动分段指标求导。固定物理延拓足以提供点态导数控制，角宽缩为 $O(L^{-1})$ 不另加损失。
基点的圆周接缝用周期恒等式切换局部 lift，不改变真实能量导数。
最后 $e^a\partial_e^a=\prod_{j=0}^{a-1}(D-j)$ 给 C1；角向分部积分给 C2，边界确实周期消失。

对相位，重新计算 $L=A\log(1/|e|)+B$ 得

$$R=(D\tau)L-\tau DL
=\tau A+e(\tau'A-\tau A')\log(1/|e|)+e(\tau'B-\tau B'),$$

$$\alpha'=\frac{R}{eL^2},\qquad q=\frac1{\alpha'}=\frac{eL^2}{R}.$$

$R\to\tau(0)A(0)>0$；所有有限 Euler 导数保持有界，故 $R^{-1}$ 亦然。
$D^j(L^2/R)=O(\ell^2)$，再用 Euler–普通导数恒等式即得
$\partial_e^a q=O(|e|^{1-a}\ell^2)$，包括 $a=0$。$\alpha'$ 的符号等于 $e$ 的符号。
这些符号使用 N 的同一 $L,\tau$，足够支持 G 的全部节点积分，未更换时间提升。

## 5. E：面积方向与对称 Hamilton 时间角

在 Morse 图中 $h=h_--(p^2+q^2)/2$，选择反射使
$\Omega=-b\,dp\wedge dq=-br\,dr\wedge d\varphi$，$b>0$。
直接收缩 $X=v\partial_\varphi$ 得 $\iota_X\Omega=brv\,dr$；
它必须等于 $-dh=r\,dr$，所以 $v=b^{-1}>0$。E 的正方向正确，不能用正面积密度替代有符号 $\Omega$。
因此 $dt=b\,d\varphi$、$L=2\pi\bar b$，线性化给 $L_0=2\pi/\omega_-$。

对 $b_r-\bar b(r)$ 取唯一零均值周期原函数 $B_r$，定义
$\Psi_r=\varphi+B_r/\bar b$。因为 $\partial_\varphi\Psi_r=b_r/\bar b>0$，
它是解析的圆微分同胚提升，参数逆函数在固定紧圆柱可一致选取。
在 $r=0$，$B_0=0$，所以一阶角度严格为通常的 $(\cos2\pi\theta,\sin2\pi\theta)$。

独立计算反号关系：$b_{-r}(\varphi)=b_r(\varphi+\pi)$、$\bar b(-r)=\bar b(r)$。
原函数零均值的唯一性推出 $B_{-r}(\varphi)=B_r(\varphi+\pi)$，从而

$$\Psi_{-r}(\varphi)=\Psi_r(\varphi+\pi)-\pi,
\quad\varphi_{-r}(\psi)=\varphi_r(\psi+\pi)-\pi,
\quad z(-r,\theta)=z(r,\theta+1/2).$$

这里的半径反号没有新增物理圆；它正是保证原光滑乘积可下推到 $\varepsilon=r^2/2$ 的额外对称规范。
面积在该角下为 $d\mu=L\,d\varepsilon\,d\theta$，没有漏掉 $2\pi$ 或额外 $r$。

## 6. E：真实 $\varepsilon$ 光滑、jets 与全模范数

由上式换角，$f_k(-r)=(-1)^kf_k(r)$，且 $f_k(0)=0$ 对所有 $k\ne0$ 成立。
$L$ 为偶函数，故 $\widetilde a_k=L f_k\overline{g_k}$ 为偶函数并至少二阶消失。
对任意 $u,S$，先对原复合函数作链式法则再角向分部积分，得到
$\|f_k\|_{C^u_r}\le C(1+|k|)^{-S}\|f\|_{C^{u+S}}$，常数确实独立于 $k$。

偶函数下推的有限阶损失为每一阶 $\varepsilon$ 导数至多两阶 $r$ 导数：
$\partial_\varepsilon=r^{-1}\partial_r$，而对偶 $v$ 有
$v'(r)/r=\int_0^1v''(tr)dt$。迭代时每个看似除以 $r$ 的奇导数都用该恒等式消除，
故闭半轴 $C^J$ 范数由 $C^{2J}_r$ 控制，不只是形式 Taylor 系数。

四阶 Taylor 积分余项给
$\widetilde a_k=r^2L_0d_{f,k}\overline{d_{g,k}}+r^4q_k(r)$，
其中 $q_k$ 偶且 $\|q_k\|_{C^{2J}}$ 受 $\|\widetilde a_k\|_{C^{2J+4}}$ 控制。
以 $r^2=2\varepsilon$ 代回，准确得到

$$a_k=\varepsilon A_k+\varepsilon^2R_k,
\quad A_k=2L_0d_{f,k}\overline{d_{g,k}},
\quad R_k=4q_k(\sqrt{2\varepsilon}).$$

取 Fourier 权重 $S$ 于一个因子已经足够，两个因子各用原 $C^{2J+4+S}$ 范数是安全上界。
因此 E(1.2) 的全 $k$ 加权估计成立，不隐含无限光滑范数，也未删掉高模。

若原一阶 jet 为 $a_fp+b_fq$，则
$d_{f,1}=(a_f-ib_f)/2$、$d_{f,-1}=(a_f+ib_f)/2$，其他 $d_{f,k}=0$。
代入即得 E(6.2) 的共轭符号，$A_k$ 仅在 $k=\pm1$ 非零。
中心化只移除 $k=0$；以上从未对可能非 Hölder 的 $(I-\Pi)f$ 求原高阶导数。

## 7. E：两种端点的独立系数及余项核算

原偶步相位为 $\sigma_E(\varepsilon)=2\rho_-(h_--\varepsilon)$，故
$\beta=-2\rho_-'(h_-)$、$\gamma=2\rho_-''(h_-)$。
反向能量坐标只改变一阶导数符号，二阶导数仍有正的因子2。

当 $\beta\ne0$，用递增坐标 $x=\operatorname{sgn}(\beta)(\sigma_E-\sigma_c)$。
换元振幅 $b_k=\chi(E)a_k(E)E'$ 满足 $b_k(0)=0$、$b_k'(0)=A_k/\beta^2$。
三次分部积分直接给

$$\int_0^\infty b_k(x)e^{i\omega x}dx
=-\frac{b_k'(0)}{\omega^2}+O\left(\frac{|b_k''(0)|+\|b_k'''\|_1}{|\omega|^3}\right).$$

令 $\omega=2\pi km\operatorname{sgn}\beta$，主项确为
$-A_ke^{2\pi ikm\sigma_c}/[(2\pi k\beta)^2m^2]$，与 $\beta$ 的正负无关。
余项以 $|A_k|+\|R_k\|_{C^3}$ 控制；E(1.2) 中 $J=3,S=2$ 只需原 $C^{12}$。

当 $T=3/16$，用 $x=\sqrt{2(\sigma_E-\sigma_c)/\gamma}$，有 $x=\varepsilon+O(\varepsilon^2)$。
换元振幅是 $x c_k(x)$，$c_k(0)=A_k$，令 $\omega=2\pi km\gamma$。
利用相位导数 $i\omega x$，紧支积分严格给

$$\int_0^\infty xc_k(x)e^{i\omega x^2/2}dx
=\frac{iA_k}{\omega}-\frac1{i\omega}\int_0^\infty c_k'(x)e^{i\omega x^2/2}dx.$$

按 $|\omega|^{-1/2}$ 分割最后一个积分，并在远端分部积分，其模至多
$|\omega|^{-1/2}(3\|c_k'\|_\infty+\|c_k''\|_1)$。
所以主项是 $iA_ke^{2\pi ikm\sigma_c}/(2\pi k\gamma m)$，余项是
$O(|km|^{-3/2}(|A_k|+\|R_k\|_{C^2}))$；$J=2,S=2$ 只需原 $C^{10}$。
两种余项均可对全部 $k$ 绝对求和，$C^{20}$ 足够。

作为因子检查，B 在 $T=3/16$ 给 $w_-=-1/2,h_-=-2$，
$q_*=-25,\delta'_*=-125/4$，因此
$\rho_-''=-6/(3125L_0)$、$\gamma=-12/(3125L_0)<0$，与 E/G 一致。
该 $m^{-1}$ 项来自消失圆，不是持续圆驻相项的重复表达。

## 8. G：完整 saddle 积分不是薄层估计的替代物

K C2 作用于两个因子给
$\partial_e^ja_k=O(|e|^{-j}\ell^{M_{j,s}}|k|^{-2s})$，原范数阶至多 $j+s$。
对 $\mathcal Ta=-\partial_e(qa)$，展开 $\partial_e^j\mathcal Ta$ 的各项，能量幂准确为
$|e|^{1-v}|e|^{-(j+1-v)}=|e|^{-j}$。
因此每次转置保持此符号类；迭代后 $\mathcal T^Na_k$ 仅有有限对数增长，可积。
真正的边界量是 $q\mathcal T^ja_k=O(|k|^{-2s}|e|\ell^{M_j})\to0$；
不需要错误地要求 $\mathcal T^ja_k\to0$。

先在避开0的闭区间积分，再用上述边界与可积主控传到节点，得到 G(4.5) 的准确恒等式。
另一端的平滑截断及其导数恒零。下侧递增 $e$ 的取向没有新增符号，因为两端边界各自为零。
取 $s=1$ 后余项和为 $m^{-N}\sum_{k\ne0}|k|^{-N-2}\int_0^\delta\ell^{M_N}de<\infty$。
$N$ 次转置最多用 $N$ 阶振幅导数；原 $C^{N+2}$ 比实际需要的 $C^{N+1}$ 更保守，声明成立。

下侧 $\sigma=1+\tau/L$、上侧 $\sigma=\tau/L$，整数 $k,m$ 使多出的1不影响指数。
故这里分析的是原 $F^2$，不是连续时间替代物；没有选择随 $m$ 缩小的能带。

## 9. G：二次驻相的完整余项与有限原范数

Morse 坐标取 $y=\operatorname{sgn}(h-h_*)\sqrt{2|\sigma(h)-\sigma(h_*)|}$，
则 $\sigma=\sigma_*+s_*y^2/2$，正 Jacobian 为 $|\sigma''_*|^{-1/2}$。
在 $e^{-2\pi i\xi y}$ 的 Fourier 约定下，高斯公式是

$$\int b(y)e^{i\pi vy^2}dy
=|v|^{-1/2}e^{i\pi\operatorname{sgn}v/4}
\int\widehat b(\xi)e^{-i\pi\xi^2/v}d\xi.$$

先加高斯阻尼时，两次积分绝对收敛；取极限时 Fourier 侧核由常数乘 $|v|^{-1/2}$ 控制，
且 $\widehat b\in L^1$，所以恒等式的传极限合法。
$b\in C_c^4$ 给 $|\widehat b(\xi)|\le C\|b\|_{C^4}(1+|\xi|)^{-4}$，
故 $\int\xi^2|\widehat b|<\infty$。
使用 $|e^{-i\pi\xi^2/v}-1|\le\pi\xi^2/|v|$ 并取 $v=mks_*$，恰得

$$\frac{a(h_*)e^{2\pi ikm\sigma_*+i\pi\operatorname{sgn}(k\sigma''_*)/4}}
{\sqrt{m|k\sigma''_*|}}+O(\|a\|_{C^4}|mk|^{-3/2}).$$

没有遗漏 $2\pi$：它已由 $2\pi km\cdot s_*y^2/2=\pi mks_*y^2$ 抵消。
原振幅的四阶能量导数加两次角向积分可由原 $C^6$ 范数及 $|k|^{-4}$ 控制，
主项和余项因此绝对可求和。剩余紧正则圆管中 $|\sigma'|$ 的下界和有限导数均受控，
任意有限次非驻相积分同样合法；证明没有停在固定模态结论。

## 10. G：持续圆、消失圆与全参数合成

M 的 proper 紧性允许先把支撑能量饱和，再用有限圆管覆盖，不增加无穷远端点。
在 $h_-$ 的奇异纤维中，椭圆点与持续紧圆互不相交，可取有正距离的分离邻域。
足够窄能带里的中心小圆盘和持续圆管分别使用圆上常值能量截断；前者近中心为1，
后者跨 $h_-$ 光滑。这样每个局部积分仍是完整圆的 Fourier 积分，分割权重只乘一次。

在 $T=3/16$，持续圆的相位满足 $\sigma''=2\rho_-''<0$，应使用一次完整双侧驻相。
另一消失圆的振幅在端点为 $\varepsilon A_k+O(\varepsilon^2)$，故贡献 $m^{-1}\mathcal D$。
G 已同时保留二者，没有把持续圆拆成两条人为半管，也没有用小圆尾删除它。
其他参数的持续圆在 $h_-$ 非驻相；内部驻点完全由 TW 已接受分类列出。
具体而言，$F^2$ 相位依下／中／上区间为 $2\rho_-,2\rho_0,\rho_+$。
$0<T<3/16$ 有中区间一驻点圆；$T=3/16$ 有 $h_-$ 持续一圆；
$3/16<T<1$ 有下区间同能量两圆；$T=1$ 无驻点圆；$T>1$ 有上区间同能量两圆。
每一驻点均为 $\sigma''<0$ 的非退化极大，故第9节主项应逐圆、逐全部非零 $k$ 相加。

由此得到的准确全局层次为：

- $T\notin\{3/16,1\}$：$m^{-1/2}\mathcal A_{r_0}+O(m^{-3/2})$；中心 $m^{-2}$ 合法吸收在余项内。
- $T=3/16$：$m^{-1/2}\mathcal A_{r_0}+m^{-1}\mathcal D_{r_0}+O(m^{-3/2})$。
- $T=1$：没有任何有限驻点圆，中心成为 $m^{-2}\mathcal B_{r_0}+O(m^{-3})$ 的主项。

Saddle 和普通非驻相部分取 $N=3$ 即够；连同第7、9节的阶数，统一原 $R=20$ 确实充足。
terminal 在原紧图中正则，任意一个分割圆管可跨越它，不产生额外角度端点或范数奇性。

## 11. 原单步的奇偶与上侧换圆

由 M 的 $\Pi\mathsf U=\mathsf U\Pi$，准确有
$C_{2m+r_0}(f,g)=C_{2m}(f\circ F^{r_0},g)$。
$r_0=0,1$ 只用固定紧能窗中 $F$ 的有限链式法则，不引入随 $m$ 增长的观测范数。
下／中／持续圆上平移给
$\widehat{f\circ F^{r_0}}_k=e^{2\pi ikr_0\rho}\widehat f_k$，
端点取一阶 jet 即给 $A_k^{(r_0)}=e^{2\pi ikr_0\theta(T)}A_k^{(0)}$。

上侧令 $z_1=Fz_0$，因为 $F_*X=X$，两参数均为相同正时间方向。
直接代入 $Fz_0=z_1$、$Fz_1=z_0(\theta+\sigma)$，奇数幅恰为

$$L\left(\widehat f_{1,k}\overline{\widehat g_{0,k}}
+e^{2\pi ik\sigma}\widehat f_{0,k}\overline{\widehat g_{1,k}}\right).$$

所以 G(7.3) 的相位放置正确；只有一条上圆支撑时，奇数相关可以恒零。
负时间由测度不变直接换元给 $C_{-n}(f,g)=\overline{C_n(g,f)}$，两方向的率一致。

## 12. 最优性、真实原光滑 jet 与泛型边界

对 $T\ne1$，任取分类中的驻点圆，在与临界点分離的紧圆管上取
$f=g=\chi(h)e^{2\pi i\theta}$。能量 bump 在圆管边界附近为零，故延零后是真正原 $C_c^\infty(U)$，
包括 $T=3/16$ 的持续圆与 terminal 穿越。它的偶步相关有唯一 $k=1$ 主项，
因而 $m^{1/2}|C_{2m}|\to L(h_c)/\sqrt{|\sigma''(h_c)|}>0$。

对 $T=1$，Morse 图内取 $f=g=\zeta((p^2+q^2)/2)(p+iq)$，在图外延零。
由原一阶 jet 而不是任意指定时间角模式，有 $d_{f,1}=1,d_{f,-1}=0$，
故 $A_1=2L_0>0,A_{-1}=0$。实际时间角中允许高模存在，但其贡献全在已控余项里。
因此 $m^2|C_{2m}|\to2L_0/(2\pi\beta)^2>0$，换成 $n=2m$ 即得到 E(9.2)。

实观测取实部。$T\ne1$ 出现 $\cos(2\pi m\sigma_* -\pi/4)$，
若它趋零则 $e^{4\pi im\sigma_*}\to-i$；相邻项商迫使 $e^{4\pi i\sigma_*}=1$，
反而原序列恒1，矛盾。$T=1$ 的 $\cos(2\pi m\sigma_c)$ 同理不能趋零。
所以实观测也有正 limsup；结论不是对每个 $n$ 的一致正下界。

一般复观测在 $T=1$ 时，$\sigma_c\in(1,4/3)$ 保证两单位频率
$e^{2\pi i\sigma_c}$、$e^{-2\pi i\sigma_c}$ 不同。
若 $A_1,A_{-1}$ 不同时零，其两频主项平方模的 Cesàro 平均为两系数模平方之和，严格正。
同时为零是有限一阶 jet 对中的真闭实代数条件，因此所述开稠密“泛型”含义准确。
一阶 jet 消失时只声明 $O(m^{-3})$，未越权推断全部高阶最优分类。

## 13. Required fixes、可接受主张与停止边界

**Required fixes：空。** 没有建议把原观测类缩为有限模或正则窗口，也无需删掉任何节点或 terminal。
E 的方向与因子2、G 的 $T=3/16$ 次层和持续圆分离、所有有限原范数与无穷 $k$ 余项均已在当前稿中落实。

允许的实际数学主张是 G(1.6)、完整局部 saddle 的任意指定有限幂率、原奇偶系数及存在观测的最优性。
不允许从此推为单圆混合、未投影系统混合、CLT、全参数一致常数或每对观测的非零下界；作者稿没有作这些声明。
标准迁移技术与新意压力不是本次数学缺口，本审查没有改变旧新意评价，也不重开任何未变旧接受阶段。

本报告不提供新意／价值分、内生22–30页容量票、Route A/B 票或稿件/PDF验收。
Paper31 正式准入、旧 FAIL/STOP、批次4/5和后续独立四门要求均不因本报告自行改变。
交付后仅向主控报告本文件行数、字节与 SHA；冻结停止编辑，不修改作者稿、索引或其他代理文件。

[K]: PAPER31_QPI_Q2_MIXED_NODE_SYMBOLS_V1_20260913.md
[E]: PAPER31_QPI_Q2_ELLIPTIC_JETS_V1_20260913.md
[G]: PAPER31_QPI_Q2_GLOBAL_DECAY_PROOF_V1_20260913.md
[M]: PAPER31_QPI_Q2_MEASURE_TERMINAL_PROJECTION_V1_20260913.md
[N]: PAPER31_QPI_Q2_NODE_NORM_AND_TAIL_V1_20260913.md
[D]: PAPER31_QPI_Q2_MATHEMATICS_AND_PREFLIGHT_DISPOSITION_V1_20260913.md
[TW]: PAPER31_QPI_REAL_GLOBAL_TWIST_SYNTHESIS_V1_20260912.md
[B]: PAPER31_QPI_REAL_ACNODE_TWIST_BOUND_V1_20260912.md
