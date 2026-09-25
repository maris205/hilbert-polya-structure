# CS09 — 单次有界执行卡 v1

Scope ID: `ASFS-DISCOVERY-20260919-CS09`。  
State: `FROZEN BEFORE COMPUTATION`。

对象、种子、123成对调用上限、所有前置控制、255传播/full SVD及14静态
上限由[candidate-card.md](candidate-card.md)唯一规定。用户已授权继续本地
构造发现，不另扩大成本或权限。主控独占启动权，作者和审查者不得启动。

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 timeout -k 10s 600s python -u papers/259-hyperbolic-tail-heat-search/run_search.py
```

工作目录`arithmetic_symplectic_flow`。输出唯一为本包`evidence/run-1`，存在即拒绝。
新输出1GiB硬限、RSS1GiB提示，真实600秒+10秒宽限；不安装、GPU或外部调用。
执行前必须完成全参数箱势/根所有权审查和实现审查，核对实际日志测试、
全SVD/缓存态、训练数组冻结先于开发读取、预算和同参数静态角色。
输入锁和脚本SHA在启动前记录；未冻结实现不能启动。
若控制/实现/超时失败，不自动重试；普通INVALID成员完整保存按卡处理。
执行后以保存数据复核拟合/比较/计数/哈希，不另传播、分解、求根或优化。
结果按ANALYZED报告，除非真正另获授权完成独立复现，不标VERIFIED。
所有原负结果与241/242暂停保留；无Route评估、发布、PDF、提交或推送。
