# DS03 精确只读后处理命令

**Scope ID:** `ASFS-DISCOVERY-20260919-DS03`。

下列命令在项目根目录执行，退出码 0，终端计时约 0.232 秒。
仅 stdout；未写原数据、未导入源码、未运行 solve、未重分解 U_tot。
stdout 原样存为 [readout-analysis.json](readout-analysis.json)。
Numpy eigh 默认读取 H_base 下三角并按 Hermitian 矩阵求解；
没有预先平均 H 和 H*。分解相对残差 1.5771e-15，有限 H 的
Hermitian 偏差见 245；理想 Hermitian 代数与浮点实现分开解释。

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 timeout 60s python - <<'PY'
import hashlib,json
from pathlib import Path
import numpy as np
base=Path('papers/245-dynamic-start-ablation/evidence/run-1')
paths={k:base/('DS02-'+k)/'spectrum.npz' for k in ('D','S')}
expected={'D':'e5817dc78833b35f1f4f4b234c2ed41d6f0b2c213f56bebe128b7f0136ef0833','S':'f7d89909a4f48381b8af9f6e39f029bad4a719fc2d9bafd2b936070de8f6b2aa'}
z={}
for k,p in paths.items():
 assert hashlib.sha256(p.read_bytes()).hexdigest()==expected[k]
 z[k]=np.load(p,allow_pickle=False)
assert np.array_equal(z['D']['H_base'],z['S']['H_base'])
H=z['D']['H_base']; eps,Q=np.linalg.eigh(H)
h=.06138739295586476; S=300; bound=np.pi*h/S
out={'scope_id':'ASFS-DISCOVERY-20260919-DS03','input_sha256':expected,'hbase_identical':True,'hbase_eigh_residual':float(np.linalg.norm(H@Q-Q*eps)/np.linalg.norm(H)),'hbase_first10':eps[:10].tolist(),'hbase_range':[float(eps[0]),float(eps[-1])],'rounding_bound':bound,'cases':{}}
def metrics(p,t):
 return {'mse':float(np.mean((p-t)**2)),'mape_percent':float(np.mean(np.abs((p-t)/t))*100),'max_percent':float(np.max(np.abs((p-t)/t))*100)}
for k,a in z.items():
 v=a['evecs']; norms=np.sum(abs(v)**2,axis=0); assert np.max(abs(norms-1))<1e-8
 vn=v/np.sqrt(norms); hv=H@vn; ee=np.real(np.sum(vn.conj()*hv,axis=0)); weights=abs(Q.conj().T@vn)**2
 sigma=np.linalg.norm(hv-vn*ee,axis=0); neff=1/np.sum(weights**2,axis=0); peak=np.max(weights,axis=0)
 q=a['q']; potential=-q+q*q+(1.02/3)*q**3+.05*q**4
 pot=np.sum(abs(vn)**2*potential[:,None],axis=0)
 momentum=np.fft.fft(vn,axis=0)/np.sqrt(len(vn)); kin=np.sum(abs(momentum)**2*a['T_kin'][:,None],axis=0)
 order=a['sort_order']; raw=a['ee']; target=a['target']; orig=a['pred']
 fixed=raw[order]-raw[order[0]]; pure=np.sort(raw)-np.min(raw)
 pfixed=fixed[1:101]*target[0]/fixed[1]; ppure=pure[1:101]*target[0]/pure[1]
 gram=vn.conj().T@vn; uv=a['U_tot']; comm=H@uv-uv@H
 low=[]
 for r,j in enumerate(order[:10]):
  top=np.argsort(-weights[:,j])[:3]
  low.append({'rank':r,'original_eigen_index':int(j),'ee':float(raw[j]),'energy_unshifted':float(a['energy_unshifted'][j]),'kinetic':float(kin[j]),'potential':float(pot[j]),'energy_std':float(sigma[j]),'h_relative_residual':float(sigma[j]/max(np.linalg.norm(hv[:,j]),1e-300)),'effective_levels':float(neff[j]),'max_weight':float(peak[j]),'top_h_levels':[{'index0':int(t),'epsilon':float(eps[t]),'weight':float(weights[t,j])} for t in top]})
 out['cases'][k]={'norm_error':float(np.max(abs(norms-1))),'orthogonality_max_abs':float(np.max(abs(gram-np.eye(len(gram))))),'ee_recompute_max_error':float(np.max(abs(raw-ee))),'weighted_energy_max_error':float(np.max(abs(weights.T@eps-ee))),'kinetic_potential_max_error':float(np.max(abs(kin+pot-ee))),'weight_rowsum_max_error':float(np.max(abs(weights.sum(axis=1)-1))),'weight_colsum_max_error':float(np.max(abs(weights.sum(axis=0)-1))),'commutator_relative_fro':float(np.linalg.norm(comm)/np.linalg.norm(H)),'ee_range':[float(raw.min()),float(raw.max())],'energy_std_min_median_max':[float(x) for x in [sigma.min(),np.median(sigma),sigma.max()]],'effective_levels_min_median_max':[float(x) for x in [neff.min(),np.median(neff),neff.max()]],'max_weight_min_median_max':[float(x) for x in [peak.min(),np.median(peak),peak.max()]],'lowest10':low,'pure_expectation_fixed_order':metrics(pfixed,target),'pure_expectation_resorted':metrics(ppure,target),'pure_expectation_first_gap':float(pure[1]),'pure_expectation_scale':float(target[0]/pure[1]),'sort_positions_different':int(np.sum(np.argsort(raw)!=order)),'pure_vs_original_max_prediction_difference':float(np.max(abs(ppure-orig))),'pure_vs_original_max_difference_index':int(np.argmax(abs(ppure-orig))+1),'rounding_max':float(np.max(abs(a['energy_unshifted']-raw))),'target2_pure':float(ppure[1]),'target2_original':float(orig[1])}
print(json.dumps(out,indent=2,allow_nan=False))
PY
```
