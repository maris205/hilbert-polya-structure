# CS01 执行锁定与细节澄清 v1

**Scope ID:** `ASFS-DISCOVERY-20260919-CS01`。  
**State/date:** `FROZEN BEFORE EXECUTION` / 2026-09-19。

执行主合同是不可变的 [组合卡](candidate-card.md)与[五形式定义](forms.md)。
用户已授权自动构造、拟合和比较，本次命令无需再次等待逐项批准。

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 timeout -k 10s 600s python -u papers/251-constructive-fit-portfolio/run_search.py
```

cwd为项目根目录，只写本包evidence/run-1，已有输出则拒绝覆盖。
CPU/BLAS线程环境1，不是OS线程/CPU亲和性承诺；无GPU、依赖安装或外部上传。
硬限600秒后TERM，10秒仍未退出则KILL；正常完成后不重复运行。

明确两种“冻结尺度”语义：101–150外推使用同一冻结训练网格的数值尺度，
不重新定标；而末尾分辨率诊断沿用**首点定标规则**，各网格各自计算
gamma_1/E_1并报告数值尺度变化。这与247一致，不称作固定数值尺度检验。
网格诊断不反馈到本轮参数或形式选择。

90个预选训练调用 + 每形式至多40个细化调用，总≤290调用；重复点
缓存只减少真实前向，不减少调用账本。默认A回归是第一个预选调用，
不另加隐藏优化预算；两个分辨率前向在训练冻结及外推计算之后。
原N250外推基线只读复用旧全谱，不新增前向。

脚本及三张定义卡/旧谱/原源码的运行前hash在manifest保存。
全部参数点在每个forward前记入evaluation_start。失败不缩短100点，
不重试崩溃；正常训练budget耗尽是记录状态，不是全局优化收敛。
