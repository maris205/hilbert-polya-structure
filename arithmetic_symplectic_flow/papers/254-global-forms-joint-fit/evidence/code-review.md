# CS04 执行前静态代码复核

## Material Passport

- Origin Skill: `ars-codex:academic-research-suite` / experiment-agent
- Origin Mode: bounded static reproducibility review
- Scope: `ASFS-DISCOVERY-20260919-CS04`
- Verification Status: `ANALYZED`; numerical rerun `NOT PERFORMED`
- Version Label: `cs04_code_review_v1`
- Review ownership: `/root/logistic_fit_readback`；Hermite/DVR及公式另由
  `/root/logistic_fit_readback/review_current_tests`独立核对。共享项目上下文，
  不是盲评、跨模型复核或外部同行评审。

结论：**当前脚本未发现执行前阻断项**。此结论只针对代码与冻结契约的
静态一致性，不保证运行完成、浮点稳定性、拟合改善或任何无限维结论。
审查没有运行forward、eig/eigh、zetazero，也没有导入实验脚本。
仅执行AST解析、输入哈希核对及只读源码检查；本文件是唯一审查写入。

## 审查对象与锁

完整读取了[candidate card](../candidate-card.md)、
[execution card](../execution-card.md)和[run_search.py](../run_search.py)。
审查快照：

```text
run_search.py SHA-256:
24eab23bade643dfc5888f458243066beeecc625e48627ae7461e23e89a9d6b5

input-locks.json SHA-256:
ac1c5c022f42f706a95a1d64ecde5baacbc49469082e3bd255316dd9de4589e5
```

AST解析通过；[input-locks.json](../input-locks.json)列出的11/11输入
SHA-256与当前文件完全一致。脚本在创建输出目录前复核这些锁，manifest
另记录脚本和锁文件哈希；既有输出目录会被拒绝。旧251 helper的main
不因别名导入而运行，本脚本只调用其polynomial和metrics。

## 1. 公共默认缓存与角色身份

源码L255–277只在F/L/W/A各自参数精确等于本形式默认点时跨形式共享。
F默认nu=2与L/W/A默认z=0对应同一个有限周期对象；H不进入该共享分支。
其他成员按形式和浮点参数hex值缓存，未把其他z=0或nu=2参数点跨族复用。

初版公共缓存的参数元数据问题已在首次运行前由主代理修正：当前L272
使用`{**shared_arrays, "theta": theta.copy()}`。因而L/W/A缓存角色的theta
正确保留第三参数0，不会把F的nu=2误存为它们的rho/kappa=2。矩阵、
能级与预测共享的是公共成员，记录仍携带源evaluation ID及本形式身份。

同形式缓存命中若不提供完整数组也不会遗漏新赢家：该精确成员首次实际
计算时已参与所有排序，best/champions之后只会改善，重复相同rank不能
再次成为严格更优成员。公共缓存提供完整数组并照常参与角色比较。

## 2. 同一对象、Hermite动能与DVR

F/L/W/A动能、位置势和交替路径的实现与卡一致（源码L116–154）：

- F的`expm1((nu/2)*log1p(p*p))/nu`为冻结软幂色散；nu=2明确取p²/2。
- L使用`log1p(rho*p*p)/(2*rho)`，rho=0取二次动能。
- W对完整P*_a应用Q_rho位置变形，保留原动能与平直测度。
- A的`(-1.)**arange(S)`对应第s步的(-1)^(s−1)。首末点不变；
  A不被错误要求单调或在原参数区间内。

Hermite构造（源码L86–113）正确区分了压缩p²/2与截断p后平方。由

\[
\frac{p^2}{2}=\frac{\hbar}{4}
\left(2a^\dagger a+1-a^2-(a^\dagger)^2\right)
\]

得到卡中对角元hbar(2n+1)/4和隔二阶元
−hbar sqrt[(n+1)(n+2)]/4；代码先构造hbar=1矩阵，再乘hbar。
Q_N=sqrt(hbar)Q_0，所以O可按N复用、节点按sqrt(hbar)缩放。

若T_0=V diag(t_j)V^T，则保存漂移为

\[
D=O^T V\operatorname{diag}(e^{-it_j})V^T O
  =\exp(-iT_{\mathrm{DVR}}/\hbar),
\qquad T_{\mathrm{DVR}}=\hbar O^TT_0O.
\]

因此按N缓存漂移没有遗漏hbar，`v * exp(...)`也确实按列乘相位。
Q/T对称、O正交、Q对角化及漂移酉性残差有执行时失败检查。H的势为
P_a(q)+delta*q⁴+lambda*q⁴，是卡中定义的有限DVR势，不能改称完整势的
精确Galerkin压缩。

每形式用自己的T、势和路径构造U_S…U_1；源码L155–161的H_ref使用
同一tmat与potential(a_ref)，读出使用该U自己的本征态。没有借入其他
形式的态、能级或动能。两个旧控制只供固定评分基准与后续比较。

## 3. 联合目标、预算与选择

源码L73–83实现冻结目标J=max(M/M_ref,W/W_ref)，并分别按
(J,M,W,evaluation ID)、(M,W,evaluation ID)、(W,M,evaluation ID)
选择联合、平均误差及最差误差角色。固定基准另与旧保存预测核对。
J下降并不自动表示M和W都下降，后续报告仍须保留原始指标。

种子严格为每族17点：默认、8结构、4宽域、4局部；共同RNG先生成宽域，
再生成局部扰动，85点按F→L→W→A→H轮转。随后每族两个事前固定阶段，
maxfev各20、单纯形边长.005和2e−7，每阶段从该族当前联合最好点启动。
故调用上限为85+5×2×20=285；源码L263另作显式参数和预算检查。
缓存仍计调用，失败或未收敛状态按优化器实际返回保存；没有追加预算或重试。

完整谱N250减去基态后有249个可用点，`energy[1:241]`恰取编号1–240，
没有访问第250个非基态。长度、有限性和正首间隔检查先于定标。
优化目标只使用`pred[:100]`与原100点表；alpha固定，不在本轮优化。

## 4. 七角色冻结、评价窗口及网格

源码L346–370的顺序为：确定主联合赢家及五族联合角色、两个全局次要
角色；形成训练Pareto清单；写winners-frozen；写完七角色的完整数组；
写calls和Pareto；记录training_frozen；然后才开始201–240参考生成。
角色允许重复，distinct_role_members按源evaluation ID明确计数。

旧101–200参考在冻结及新参考生成之后才读入作开发集评价。生成201–240
后没有训练、角色替换或未来成绩排序。旧Q0103与S控制的240点预测直接
从既有完整能量和既有尺度取得，不运行旧对象前向。

源码L398–405只对已冻结的主联合赢家做N260和N280两个新前向，保持同一
theta；若为H则按新N建立对应Hermite基底。没有给次要角色追加网格，
也没有网格调参。各网格按冻结首点规则定标，随后窗口沿用该网格尺度。

## 5. 运行与报告边界

输出限本包evidence/run-1，使用排他创建；冻结执行命令提供600秒硬限及
10秒终止宽限。预计算、训练、参考生成和两个网格都在同一进程预算内。
运行中的线程环境、PID、30秒资源采样、文件尺寸及事件会保存；审查没有
验证实际启动环境或预计耗时。Hermite稠密漂移比FFT分支成本更高，硬限
触发时应如实保留部分完成，不因静态通过而声称必然完成。

两个非阻断的日志解释注意事项：

1. 缓存记录继承来源的seconds；不能把全部调用行的seconds求和当总耗时。
2. event先生成UTC再取得写锁，资源线程可与主线程交错；不应预先要求所有
   事件时间戳严格单调。冻结/参考的主线程调用顺序与文件哈希才是该门控
   的代码依据，运行后仍需核对实际保存事件。

本审查不提供数值结果、独立复现、历史盲测、实直线极限、谱收敛或
prime-symbolic机制证明。监督构造允许继续，但任何有限拟合改善都不能
由此直接升级为可信A−1或正式Route结论；卡中的未评价状态保持不变。
