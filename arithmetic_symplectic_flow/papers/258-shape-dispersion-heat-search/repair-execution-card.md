# CS08 — 用户批准的固定赢家恢复执行卡 v2

Scope ID: `ASFS-DISCOVERY-20260919-CS08`。
Execution ID: `CS08-REPAIR-FIXED-01`。
State: `FROZEN BEFORE REPAIR COMPUTATION`，2026-09-19研究标签。

## 授权和不变对象

用户在获知run-1的日志参数冲突及后检缺失后明确回复：
“可以修复，没问题的”。本卡据此批准一次修复后固定赢家补齐；
不是自动重试，也不授权重新搜索、改参数或更换赢家。

沿用原[候选卡](candidate-card.md)的全部势、动能、连续最低值、
冷却路径、beta=.02、尺度/读出、分辨率规则和后检窗口。
同一Scope/Form/成员ID保持；没有新数学候选或算术/Route信用。
原run_search.py、candidate-card、execution-card、input-locks和run-1
逐字节保留，原失败报告及审查不改写。新代码仅为resume_fixed.py，
新数值输出仅为evidence/run-2-fixed，排他创建，不覆盖原结果。

唯一成员来源是run-1/winners-frozen.json：B0068、O0089、Q0107、
U0135、D0158；完整ID和theta直接读取其锁定值。全局主赢家固定Q0107。
原排序、J、sigma/E/mask/预测/尺度属于run-1，不能被修复的SVD或
开发指标替换。所有目标1–320均为历史已知数据，没有新目标生成。

## 修复与执行前回归

旧失败为局部event(name, **fields)与name=对象元数据冲突。
新日志函数使用独立的event_type参数（可设为位置专用），保留
name元数据；不得通过关闭日志绕过。执行前必须用StringIO等内存流
实际测试原失败调用形状及重建完成/后检开始/后检完成的name=调用，
核对事件名和对象名各自保留。该单元测试不做任何研究数值运算。

允许AST、纯导入和上述非数值日志测试；纯导入时禁止forward、
propagate、SVD/eigh、求根、优化或旧main。独立代码审查应重点核对
所有事件调用、无优化路径、计数与保存/开发冻结顺序。

新脚本可只读导入锁定258的propagate/readout/add_states/
static_readout/metrics/compare等纯helper及其锁定256数学源函数，
不修改任何旧模块全局量，不调用旧main或优化器。数学kernel不改。
旧16项输入锁、新修复锁与run-1的815文件清单须在开始及结束核验。

## 十个训练矩阵的重建与保留原选择谱

按B/O/Q/U/D顺序，各自N511、N639；L8、64中点、theta固定。
每个角色只传播一次，直接做一次full SVD取得左右态，共10传播/
10次full SVD；不重新运行160成员搜索，也不额外做sigma-only SVD。

重建必须逐项核对原训练NPZ的theta、N/L/B/beta、q/p/k、midpoint/
schedule、W/meanW、minimum_values/minimizers，要求数组精确相等。
最低值索引属于新的根账本，不能要求与旧编号相同或无标记混用。
原mask/有效性从原sigma按同一规则核对；所有原选择数组原样保留。

新full-SVD全sigma与原sigma最大绝对差须≤1e−12；超限整次停止，
不改排名或用新sigma替换旧sigma。新sigma及由它计算的E/预测/尺度
另存reconstruction字段，并报告差值。原有效性必须仍有效；重建
读出无效属于恢复一致性失败。无需把未经规定的全谱能量绝对误差
容差补作选择门，尤其不得因尾sigma的日志放大而偷偷裁尾或改谱。

用重建C和左右态、原选择sigma记录原卡的左右方程/正交/全谱
Frobenius矩及前100/320边缘和最高ceil(N/5)动量占据；完整C、
全原sigma/E/mask和前320左右态全部落盘。每角色同参数静态H_avg
也按原规则计算并保存完整H/全lambda/前320态，共10次静态分解。

先在新目录保存原赢家身份的逐字节副本及原SHA，再执行上述恢复。
十份完整热数组和十份静态数组全部保存并写training-arrays-frozen
及其SHA后，才读取101–320参考内容并计算开发拟合。原身份始终不变。

## 十二个原定后检与判定

每族N1023、N1279各一次，共10传播/10静态分解；参数固定，L8/B64。
Q0107另做N1279/L8/B128和N1599/L10/B64，共2传播/2静态分解。
每次热传播仅一次full SVD，保存完整C/全sigma/E及前320左右态。
后检普通INVALID按原卡保留并使相关比较不可判定；不递补赢家或加N。
实现/根/非有限异常整次停止；不再自动重试。

所有族报告N639→N1023及N1023→N1279的原四窗口G；Q额外报告
时间和箱宽G，均沿用严格2%工程线及各网格自身E0尺度。
同参数热/静态差另报，不另训静态；所有五族已知开发窗口均报告，
禁止因后检有利而改全局主赢家。旧S0047/N1535仅为固定对照。

## 预算、命令与结果边界

一次修复最多22传播、22次full SVD、22次静态分解，零优化调用；
其中10传播是显式新增的恢复成本，12传播为原定未执行后检。
不将其伪称原run-1已经完成，也不拿缓存节省额度进行新探索。
原run-1已完成323传播；若此次全部完成，两次合计345传播。
旧三解析控制及母体双回归作为锁定既有证据，不额外重复运行。

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 timeout -k 10s 600s python -u papers/258-shape-dispersion-heat-search/resume_fixed.py
```

工作目录arithmetic_symplectic_flow。真实600秒硬限+10秒宽限；单BLAS
线程和约30秒资源监控；RSS1GiB为提示，新输出预算1GiB为硬上限。
调用尝试与已完成传播/分解分开记账，失败不得靠预增计数冒充完成。
保留PID、UTC、退出码、环境、脚本/输入SHA、输出文件清单及失败日志。
新输出目录存在即拒绝；不安装、GPU、上传、发布、PDF、提交或推送。

运行标签UNVERIFIED；保存分析ANALYZED。十个训练角色的一致性恢复
不等于完整搜索的独立复现，高N/时间/箱宽的有限G也不认证无限收敛。
241/242保持暂停；same-object账本不拼接；A0/A1/A2/T0–T3未评，
formal UNASSIGNED，B NOT INVOKED。结果决定有限advance/stop/fork。
