# CS02 执行前输入绑定

**Scope ID:** `ASFS-DISCOVERY-20260919-CS02`。  
**State/date:** `FROZEN BEFORE EXECUTION` / 2026-09-19。

执行 [原卡](candidate-card.md) 的既定读出扫描。五个251源胜者按训练
指标绑定于 [input-locks.json](input-locks.json)，不用外推成绩选择源。
原卡冻结的观测时间为18:12:58 UTC；251训练胜者冻结时间为
2026-09-18T18:14:58.938962 UTC。两者先于本包外推评分，原卡亦先于
251的外推参考生成。研究日期采用环境给出的2026-09-19，与实际UTC分列。

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 timeout -k 10s 120s python -u papers/252-path-energy-readout/scan_readout.py
```

cwd项目根目录；仅写本包evidence/run-1，不覆盖已有输出。
预定每形式2006个训练alpha调用，加1个不参与选型的时间均值诊断，
总10035个调用；重复值可以缓存，全部调用仍写CSV。
不做新的forward或eig。输入hash检查读文件字节不解析外推数值；
只有本包胜者冻结文件保存后才读取/解析外推参考并计算对应误差。
若同源允许复用网格，仍以各网格自身首间隙应用相同定标规则，
不是沿用训练网格数值尺度；同一alpha不再拟合。

每个v列沿用251的未显式再归一化约定，仿射斜率与ee_end一致。
相位固定时分支固定区间内损失分段常数；格点扫描不证明连续全局最优。
新增alpha明确计入监督拟合容量，不当作动力学方程本身的改善。
