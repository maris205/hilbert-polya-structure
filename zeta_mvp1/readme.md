# 从“无路可走”到 RH-398：新线索之后的研究进展与后续路线

## 摘要

这份文档总结本轮研究从“所有候选均被来源或量词边界挡住，暂无下一篇可分配”，到连续完成 RH-386—RH-398 的全过程。核心变化不是多做了若干有限计算，而是两条新的承重解析线索先后补齐了统一误差控制和奇总指数消去通道，使原本无法合法推进的候选，逐步形成了：

1. 增长阶数的定量 prime-tail 理论；
2. 完整的固定三移位 terminal-log table law；
3. 精确的 centered graph-coupled 容量公式；
4. 任意固定滞后的 Euler-run endpoint；
5. 有限时钟取到与不取到的几何分类；
6. 跨滞后的精确最大值、最大化者和联合端点。

当前 RH-398 已完成论文、可执行证书、来源闭包、独立证明审计、PDF 审计和发布归档，并已推送到 `origin/main`。这条 fixed-data / terminal-log / centered-noncausal 支线已经自然封口；下一步应先做 post-RH-398 breadth audit，而不是机械分配 RH-399。

---

## 1. 最初为什么会“无路可走”

当时并不是没有问题可研究，而是所有看起来有价值的候选都至少缺一项承重条件：

- 缺少对增长阶数或增长参数统一有效的定量解析来源；
- active `c_11`、三重奇通道以及未平方偶四点通道尚未被已有来源支付；
- centered 规则读取未来值，不能改名包装成 causal/online 规则；
- 有限枚举和数值证书可以发现结构，却不能替代 terminal-limit 解析定理；
- 物理 Gates A–E 所需的 typed objects、identification theorem 或 uniform bridge 仍未给出。

因此，当时的 `STOP_SCOPED` 并不是“想不到计算方法”，而是：现有来源、数据类型和量词不足以支持一个诚实的新定理。post-RH-385 的交接记录曾明确写明，在缺少新来源时没有 RH-386 可分配。

这一区别很重要：

- **计算暂时困难**，意味着同一定理合同内仍可继续攻坚；
- **来源或数据类型不匹配**，意味着继续计算也不能合法升级为论文结论。

本轮突破发生在第二种障碍被真正补上之后。

---

## 2. 两条真正改变局面的新线索

### 2.1 Johnston–Yang：补上增长阶数所需的统一素数误差

第一条线索来自 Johnston–Yang 的显式素数定理误差估计。它提供了可冻结、可定位并带统一常数控制的 `vartheta` 误差，从而允许严格处理增长单阶和增长有限分拆族。

在此之前，仓库只有固定阶或定性 PNT 输入，无法把“每个固定参数成立”提升为“在某个增长窗口上一致成立”。新来源使下列推进成为可能：

- 严格 Abel/Stieltjes 边界；
- exact-kernel 到 power-kernel，再到 leading-kernel 的统一比较；
- 随阶数与分拆增长的误差聚合；
- 对允许增长窗口的清晰量词和 sharpness obstruction。

这条线索直接打开了 RH-386—RH-391 的定量 prime-tail 路线。

### 2.2 Tao–Teräväinen：补上固定三移位唯一缺失的奇通道

第二条线索是 Tao–Teräväinen 对固定互异仿射形式、正整数指数且总指数为奇数的 logarithmic Möbius 消去结果。

RH-393 当时只能处理“单项式中奇指数坐标至多两个”的范围：

- 三移位插值覆盖 `26/27` 个单项式；
- 唯一缺失的是三重奇通道 `c_111`；
- distinguished-current 三元表只能覆盖 `192/512`；
- 四移位的未平方偶四点通道 `c_1111` 仍然缺失。

新线索配合固定相位仿射化和 terminal-clock 变换，恰好补上所有正奇总指数通道。于是：

- 固定三移位从 `26/27` 变成完整 `27/27`；
- 任意固定三元表的 terminal-log 极限都有了合法解析来源；
- 四移位达到 `80/81`，同时明确保留 `c_1111` 边界。

它的价值不只是补了一个单项式。它把“无法合法优化任意三窗口表”转化成了一个稳定的解析接口，后续所有 graph-coupled 容量定理才有可能成立。

---

## 3. 第一阶段：定量 prime-tail 与增长阶数（RH-386—RH-391）

### RH-386：增长单阶与增长有限分拆族

利用 Johnston–Yang 的显式误差，RH-386 建立了统一 prime-tail 比较，并得到：

- 增长单阶的统一渐近；
- 增长有限分拆族的统一误差；
- exact/kernel/leading 三层公式；
- leading-equivalent 的精确判据 `H/L -> 0`；
- all-ones 长分拆产生 `exp(-c)` 的 sharpness obstruction。

这一步第一次把“固定阶结论”推进为有合法窗口的增长阶数定理。

### RH-387：all-order 重求和

RH-387 不再逐个有限阶拼接，而是先用绝对收敛和 Tonelli 把所有阶数重求和成闭合的 logarithmic integrals，再通过冻结的端点映射。

它关闭了：

- all-order source/power-kernel 坐标；
- 严格的坐标误差常数；
- 端点 Lipschitz 传递；
- 精确的 gap constants。

### RH-388：推进到 `P_2` 精度

RH-388 证明：

- 保留 exact rank one、平滑所有更高 rank，足以达到统一 `P_2` 精度；
- 完全平滑 rank one 在该尺度并不充分；
- Maynard 的有界连续素数间隔提供了严格反向 obstruction。

因此，这里不仅有正定理，还有同一冻结层级内的 sharp negative theorem。

### RH-389：active `c_11` 的固定时钟 terminal-log 容量

RH-389 关闭了此前长期停滞的 active `c_11` fixed-clock 路线：

- 把 `512` 个三元表投影为 `8` 个有限动作；
- 得到精确兼容关系；
- 用 predecessor charge 支付 active-memory 增益；
- 对每个固定安全周期族给出精确 terminal-log 容量。

边界仍然明确：这不是 ordinary Cesàro，也不是 growing-clock 结论。

### RH-390：同步增长 rank filtration

RH-390 保留移动阈值以下的所有 exact prime tails，把阈值以上 rank 统一替换为 factorial order，并证明：

- 在同时增长的 `(s,K)` 窗口内有统一 next-scale accuracy；
- 每个 fixed rank 的 endpoint direction 都严格为正；
- 在冻结的 `P/J/I` 层级内，逐个 fixed rank 都是必要的。

### RH-391：线性尺度 moving-rank 必要性

RH-391 把必要性推进到线性 moving-rank 范围：

- 在连续素数边上使用相同 rank；
- 得到自然 pair profile；
- 得到粗线性和 sharp sublinear lower bounds；
- 证明 next-rank separation。

至此，第一条新线索所打开的增长阶数链完成了从统一单阶到 all-order、`P_2`、active memory 和 moving-rank necessity 的连续闭环。

---

## 4. 第二阶段：固定滞后编译器（RH-392—RH-394）

### RH-392：每个固定非零滞后的 terminal-log 容量

RH-392 建立了：

- 固定有限移位的 total-quadratic diagonalization；
- 单一固定滞后的 coordinatewise-biquadratic compiler；
- 精确的 pair-squarefree phase densities；
- 每个固定 `(q,h)` 的安全表容量；
- square-divisor landscape 的最大值与不取到下端点。

这一步把研究对象从 rank/tail 重新接到固定滞后 Möbius 容量。

### RH-393：多移位、至多两个奇指数

RH-393 推广到任意固定有限移位集，只要每个单项式至多含两个奇指数坐标。它给出：

- 精确多移位 phase densities；
- admitted dimension；
- `26/27` signed-cube boundary；
- `192/512` distinguished-current table class；
- 完整 squarefree-density landscape。

这篇最重要的作用之一，是精确暴露了下一道墙：三重奇通道不是有限算法遗漏，而是解析来源缺口。

### RH-394：完整固定三移位 table law

Tao–Teräväinen 的新线索在 RH-394 中被完整编译。结果包括：

- 所有正奇总指数通道的 fixed-data cancellation；
- 完整三移位 `27/27` table law；
- 任意固定三元表的 terminal-log 极限；
- 四移位 `80/81` boundary；
- 非负 exact-support 权重 `Pi_(q,r)(U)`；
- intrinsic support-stratum / Fourier-degree census。

RH-394 是后续 RH-395—RH-398 的解析地基。这里仍明确没有解决 unsquared even four-point `c_1111`。

---

## 5. 第三阶段：图耦合容量、滞后端点与全局极值（RH-395—RH-398）

### 5.1 RH-395：`h=1` centered 三窗口容量

研究窗口为

```text
(mu(n-1), mu(n), mu(n+1)).
```

RH-395 完成：

- positive projection，把三元表降为外侧 ternary relation；
- 精确 safety/composition criterion；
- relation saturation；
- 每个固定时钟的八状态 tropical trace；
- `q>=3` 时的四状态压缩，以及 `q=1,2` 的自环例外；
- reflection 对称和双符号取到；
- 固定时钟真实 memory gain；
- square-support marginal charge 和严格 all-clock endpoint。

结论是：固定有限时钟的记忆增益是真实的，但不会提高最终 endpoint；每个有限时钟都严格低于同一个 all-clock supremum。

### 5.2 RH-396：任意固定滞后与 Euler-run endpoint

窗口推广为

```text
(mu(n-h), mu(n), mu(n+h)),   d=2h.
```

模 `p^2` 的移位碰撞使问题显著复杂。RH-396 引入 collision-aware 的 `Theta/Pi/lambda` 权重，并完成：

- 每个固定 `(h,q)` 的八状态 `r -> r+2h` tropical trace；
- `q | 2h` self-loop 边界，禁止无条件四状态压缩；
- 含 reset prime `p_0(h)` 的 square-support marginal equality；
- finite Euler-run endpoint；
- fresh-prime recurrence 和 CRT even-run strictness；
- 对任意固定有限时钟的严格不取到：

  ```text
  sup_(q<infinity) C_h(q) = B_infinity(h),
  C_h(q) < B_infinity(h) for every finite q;
  ```

- 跨固定滞后的不取到下端点：

  ```text
  inf_(h>=1) B_infinity(h) = 3/pi^2.
  ```

RH-396 当时明确没有解决跨 `h` 的最大值、最大化者或单调性。

### 5.3 RH-397：half-span 两符号重叠几何

RH-397 不是 RH-396 的简单强化，而是换了安全几何：安全间距从 `2h` 变为 `h`，相邻窗口共享两个符号。第四个符号只出现在有限安全谓词中，不是第四个解析移位。

RH-397 完成：

- relation 精确塌缩为 source/target 两个 Boolean flags；
- 四个饱和矩形；
- collision-aware `M,U,V,W` 权重；
- translation `V_r=U_(r+h)`；
- weighted step-`h` rising-set / independent-set optimizer；
- 每个固定 `(h,q)` 的精确容量公式；
- 对每个固定奇数 `h`：

  ```text
  max_q C_h^hs(q)
    = K_1 - kappa_2(h)/2 + kappa_3(h)/4,
  ```

  且等号恰在声明时钟 `q` 为偶数时成立。

这揭示了一个关键结构差异：

- RH-396 的 distance-`2h` 类在任何有限时钟都不取到 endpoint；
- RH-397 的 half-span 类在所有偶数声明时钟都取到最大值。

### 5.4 RH-398：跨滞后的最大值和精确最大化者

RH-398 回到 RH-396 的 endpoint。定义

```text
t_p(d) = p^2 / gcd(d,p^2),
A_m(d) = product_p (1 - min(m,t_p(d))/p^2),
```

并把 Euler-run 端点望远镜化为

```text
B_infinity(h)
  = sum_(m=1)^(p_0(h)^2-1) (-1)^(m+1) A_m(2h).
```

证明方法依次为：

1. 有限 prime-support CRT phase space；
2. path-residue deletion total loss `Lambda_T(L)` 的四个奇偶分支；
3. one-prime collision-level transfer；
4. common finite support；
5. common cofinal passage；
6. positive-density exact-run cylinders 支付严格性。

最终得到

```text
max_(h>=1) B_infinity(h) = B_infinity(1),
```

以及精确等号条件

```text
B_infinity(h) = B_infinity(1)
iff mu^2(h)=1 and gcd(h,210)=1.
```

同时关闭：

- 非最大化集合的 supremum 仍为 `B_infinity(1)`，但不取到；
- 对素数 `p>=11`，`h=p^2` 从补集逼近最大值，并满足

  ```text
  0 < B_infinity(1)-B_infinity(p^2) <= 1/p^2;
  ```

- `p_0(h)>=5` 区域存在统一正间隙；
- 联合端点

  ```text
  sup_(h>=1, q finite) C_h(q) = B_infinity(1)
  ```

  没有任何有限 `(h,q)` 取到；
- RH-396 的下端点 `3/pi^2` 及其不取到性继续保留。

---

## 6. 完整逻辑依赖图

```text
缺少统一素数误差
        |
        | Johnston–Yang 显式定量 PNT 输入
        v
RH-386—RH-391：增长阶数、all-order、P_2、active c_11、moving-rank

RH-392：固定非零滞后 terminal-log 容量
        |
        v
RH-393：多移位、至多两个奇指数，三移位 26/27
        |
        | Tao–Teräväinen 正奇总指数消去
        v
RH-394：完整固定三移位 table law，27/27
        |
        v
RH-395：h=1 centered graph capacity 与 all-clock rigidity
        |
        v
RH-396：任意固定 h 的 Euler-run endpoint 与有限时钟不取到
       / \
      /   \
     v     v
RH-397   RH-398
新 half-  跨 h 最大值、最大化者、补集与联合端点
span 几何
```

RH-398 的唯一承重解析 endpoint 来源是 RH-396。RH-397 是另一条 overlap-geometry 分支和直接发布前驱，不参与 RH-398 的解析证明。

---

## 7. 当前完成状态

RH-398 已完成完整的研究到发布闭环：

- 论文、LaTeX、PDF 与语义 PDF 已冻结；
- core certificate 为 `72` 条语义记录；
- core/result/schema 分别拒绝 `66/44/32` 个命名语义变异；
- normal 与 `python -OO` 完整测试均为 `75/75`；
- 官方 Draft 2020-12 JSON Schema 检验为零错误；
- 来源闭包为 `184` 个 Git 对象加 `4` 个 remote logical locks，共 `188`；
- 发布归档为 `41` 个 publication members、`43` 个 release-stage files；
- 证明、来源、引用、PDF 和发布独立审计均为 `0 blocker / 0 minor`；
- 包提交为 `f026f7b5dd3aca499b656d03b1a3edc27b02eb8e`；
- 总交接提交为 `c80d26e327ef2a979536c0f7dd3f69fe022befac`；
- 本地 `main`、`origin/main` 与远端已一致。

主要材料：

- [总交接](prime_dynamics_theory/RH_HANDOFF.md)
- [RH-394 路线图](prime_dynamics_theory/papers/RH-394-odd-parity-terminal-log-mobius-compiler/UPDATED_ROADMAP.md)
- [RH-395 路线图](prime_dynamics_theory/papers/RH-395-all-clock-rigidity-centered-three-window-mobius-capacity/UPDATED_ROADMAP.md)
- [RH-396 路线图](prime_dynamics_theory/papers/RH-396-euler-run-spectrum-fixed-lag-centered-mobius-capacity/UPDATED_ROADMAP.md)
- [RH-397 路线图](prime_dynamics_theory/papers/RH-397-odd-lag-half-span-overlap-mobius-capacity/UPDATED_ROADMAP.md)
- [RH-398 路线图](prime_dynamics_theory/papers/RH-398-exact-lag-endpoint-maximum-and-maximizers/UPDATED_ROADMAP.md)
- [RH-398 论文 PDF](prime_dynamics_theory/papers/RH-398-exact-lag-endpoint-maximum-and-maximizers/main.pdf)

---

## 8. 这条路线仍然没有解决什么

当前成果属于一个完整但明确受限的 fixed-data / terminal-log / centered-noncausal 子程序。它没有给出：

- ordinary Cesàro Möbius cancellation；
- `h=h(X)`、`q=q(X)`、增长表族或统一有效率；
- prelimit maximum 或 adaptive capacity；
- causal/online 控制器；
- unsquared even four-point correlation；
- unrestricted four-coordinate 或 larger-window table law；
- generic graph capacity；
- operator、trace 或 zeta-zero identification；
- Riemann Hypothesis；
- Gates A–E 的任何关闭。

因此，正确的总体判断是：

> 一条此前被高阶解析通道卡死的独立数学支线已经被打通并完整关闭，但它没有自动跨越到物理 Gate、零点模型或 RH。

---

## 9. 后续研究思路与优先级

### P0：先完成 post-RH-398 breadth audit

当前尚未分配 RH-399。下一步必须先对候选做独立的 Route A / Route B 审计：

- Route A：是否具有独立、非重包装的数学发现价值；
- Route B：是否与现有来源、数据类型和量词严格兼容。

只有二者都通过，才应建立新编号、source lock 和论文合同。

### P1：RH-397 的 even-lag clock landscape

这是当前最接近、最值得优先审计的候选。

RH-397 已经对每个固定 `(h,q)` 给出精确 weighted independent-set 公式，缺口主要是偶数 `h` 的全时钟分类：

- step-`h` 循环怎样按 `gcd(h,q)` 分解；
- self-loop 和碰撞怎样改变权重；
- 哪些声明时钟取得最大值；
- 是否存在多个 arithmetic attainment types；
- 奇数 `h` 的 iff-even 结论为什么、以及在何处失效。

这个方向的优点是解析三移位接口已经付清，主要工作可能是 exact weighted graph、CRT 和时钟算术。主要风险是：

- 把 weighted optimizer 偷换成 cardinality；
- 忽略 self-loop；
- 忽略 collision-aware phase weights；
- 把 odd-lag parity 直接外推到 even lag。

因此它适合立即进入 source-lock 与 adversarial proof audit，但在审计通过前仍只是候选，不是下一篇既定论文。

### P2：其他固定 overlap relations

在 RH-394 已支付的三移位接口内，可以系统搜索其他固定重叠关系，检查：

1. positive projection 是否仍然合法；
2. relation 是否能塌缩成少量 flags；
3. 每个 flag class 是否有精确 saturation；
4. phase weights 是否能 telescope 成 weighted graph；
5. 新模型是否真的不是 RH-397 的重参数化。

只有出现新的精确优化结构和不同的 attainment phenomenon，才构成独立 theorem edge。

### P3：新的 scalar endpoint landscapes

若 P1 或 P2 产生新的精确 endpoint，可以再沿 RH-398 的方法研究：

- common finite support；
- one-prime local transfer；
- common cofinal passage；
- positive-density strict cylinders；
- exact equality class；
- complement supremum 与取到性。

不能在没有新 endpoint 公式时先猜跨参数最大值，也不能假定参数单调。

### P4：causal/end-window graph-coupled capacity

该方向数学价值高，但目前仍为 `STOP_SCOPED`。重新启动至少需要：

- 明确的 causal information set；
- 与其匹配的 table/safety 数据类型；
- 合法的 compatibility/charge theorem；
- source-lock 证明现有三移位解析定理足够，或补充新的解析通道。

centered 模型读取 `mu(n+h)`，不能通过重命名变成 online transducer。

### P5：偶四点或完整四坐标表

这是最清楚的解析硬墙之一。当前来源支付正奇总指数，不支付 unsquared even four-point correlation。因此：

- RH-394 的 `80/81` 边界必须保留；
- finite signed-cube census 不能替代新四点定理；
- 只有真正的新解析来源才能重开 unrestricted four-coordinate route。

### P6：growing parameters 与 uniform rates

增长 `m,h,q`、移位、mask、系数或表族，要求一个对所有移动参数共同有效的 uniform theorem。禁止：

- 交换 `X -> infinity` 与 clock extremum；
- 把每个 fixed-`q` saving 对角化成 prescribed polynomial clock；
- 把非有效 diagonal 当成新 theorem edge；
- 把有限证书解释为 uniform analytic rate。

### P7：bouquet、continuum projector 与 original physical triggers

- RH-365 bouquet exact radius 仍缺 exponential multiplicity lower bound 或 composite-order primitive divisors；
- continuum `-1` Riesz projector 仍为 `NOT_TESTABLE`，缺 mesh-independent Banach pair、consistent projection/lift maps 和 common resolvent contour；
- 原始 physical triggers 1–4 仍需其各自缺失的 typed theorem；
- 在没有新 typed input 前，重复有限 diagnostics 不会形成新的 Gate 进展。

---

## 10. 推荐的实际执行顺序

1. 对 post-RH-398 全部候选做 breadth audit，不预先编号；
2. 优先审计 even-lag fixed-data clock landscape；
3. 并行进行其他 overlap relation 的有限结构分类；
4. 只有出现新 endpoint 后，才研究新的 scalar extremum landscape；
5. 持续监测 causal、偶四点和 uniform-rate 是否出现真正的新来源；
6. 缺少承重定理时宁可停在 RH-398，也不机械制造 RH-399；
7. Gates A–E 保持 false/open，直到对应 typed objects 与 identification theorem 被严格建立。

---

## 11. 总结

本轮推进可以概括为：

> 新线索先补上了两个具体的解析接口，一个负责增长阶数的统一误差，一个负责固定三移位唯一缺失的奇通道。真正的连锁效应，是把原来无法合法推进的候选，逐步转化为可精确求解、可比较端点、可分类取到性、可独立审计并可发布的完整研究链。

从“无路可走”到 RH-398，已经完成的不是若干小修补，而是两条承重线索触发的连续大步：

- 定量 prime-tail 与 moving-rank 链；
- 固定滞后 Möbius table/compiler 链；
- centered graph capacity；
- Euler-run endpoint；
- overlap geometry 的取到性分类；
- 跨滞后的精确最大值和最大化者。

这条路线目前在 RH-398 处自然闭合。下一步最有希望的是 even-lag overlap landscape；因果、偶四点、增长参数和物理 Gate 则必须等待各自真正的新承重输入。
