# DS03 全态方差恒等式的只读后处理

**Scope ID:** `ASFS-DISCOVERY-20260919-DS03`。

此补充只读取同样两个 NPZ，不重分解 H 或 U，不传播任何态。
退出码 0，终端计时约 0.128 秒。输出见
[variance-analysis.json](variance-analysis.json)。
使用原本征向量逐列归一化但不作正交化；数值 V 非完全酉时，
由 V diag(.) V* 得到的是理想公式的有限诊断，不宣称精确矩阵恒等式。

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 timeout 60s python - <<'PY'
import json
import numpy as np
base='papers/245-dynamic-start-ablation/evidence/run-1/'
out={}
for lane in ('D','S'):
 a=np.load(base+'DS02-'+lane+'/spectrum.npz',allow_pickle=False)
 H=a['H_base']; v=a['evecs']; v=v/np.linalg.norm(v,axis=0); mu=np.real(np.sum(v.conj()*(H@v),axis=0))
 mean=float(np.trace(H).real/len(H)); intrinsic=float(np.linalg.norm(H-mean*np.eye(len(H)))**2/len(H))
 diag=(v*mu)@v.conj().T; rec=(v*a['energy_unshifted'])@v.conj().T
 out[lane]={'mean_h_energy':mean,'mean_expectation':float(mu.mean()),'h_spectral_variance':intrinsic,'between_expectation_variance':float(np.mean((mu-mean)**2)),'within_state_mean_variance':float(np.mean(np.sum(abs(H@v-v*mu)**2,axis=0))),'between_over_spectral_variance':float(np.mean((mu-mean)**2)/intrinsic),'h_minus_diagonal_relative_fro':float(np.linalg.norm(H-diag)/np.linalg.norm(H)),'rec_minus_diagonal_relative_fro':float(np.linalg.norm(rec-diag)/np.linalg.norm(H)),'h_minus_rec_relative_fro':float(np.linalg.norm(H-rec)/np.linalg.norm(H))}
print(json.dumps(out,indent=2,allow_nan=False))
PY
```
