#!/usr/bin/env python3
"""Exact Bessel-series and action-normalization evidence, not numerical eigenproof."""
if not __debug__:
    raise RuntimeError("c398 producer refuses optimized Python")
import argparse,hashlib,json
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
FLAGS=['claims_target_arithmetic_local_data','claims_target_euler_factors','claims_root_number','claims_automorphy','claims_target_divisor_or_counting_law','claims_target_functional_equation','claims_target_zero_match','claims_hilbert_polya_operator','invokes_route_b']
def canonical(x):return json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()
def q(x):x=F(x);return [x.numerator,x.denominator]
def metadata():return {'schema':'hcs-exact-evidence-v1','candidate_id':'HCS-C398','source_commit':'697518b6db90458f86f7916fbf397b8ad5ef2372','fixed_epoch':1788566400,'scope_literal':'NO_BAD_EULER_OR_ROOT_NUMBER','scope_flags':{k:False for k in FLAGS},'route_a':{'tuple':['A0_FAIL','A1_FAIL','A2_FAIL','A3_FAIL','A4_NATURAL_QUANTIZATION'],'overall_verdict':'ROUTE_A_REJECTED','route_b_invocation_allowed':False},'evidence_role':'finite exact regression; not an infinite theorem or target match'}
def build():
    d=metadata();d['series']=[];d['actions']=[];d['tails']=[]
    for a in (F(1,2),F(1),F(2),F(3)):
        for k in (8,16,32):
            re,im=F(1),F(0);terms=[[q(re),q(im)]]
            for j in range(1,9):
                factor=a*a/(4*j*(j*j+k*k));re,im=factor*(re*j-im*k),factor*(re*k+im*j);terms.append([q(re),q(im)])
            d['series'].append({'a':q(a),'k':k,'terms':terms})
            h=a*a/(4*k)
            d['tails'].append({'a':q(a),'k':k,'h':q(h),'series_minus_one_bound':q(h/(1-h)),'series_derivative_bound':q(h/(k*(1-h)**2))})
        for r in (F(3,2),F(2),F(3),F(5)):
            k=a*(r+1/r)/2;root=a*(r-1/r)/2
            d['actions'].append({'a':q(a),'r':q(r),'k':q(k),'sqrt_energy_minus_a2':q(root),'action_log_coefficient':q(2*k),'action_constant':q(-2*root),'period_log_coefficient':q(1/k)})
    d['controls']={'energy_order':[1,2],'schatten_threshold_strict':[1,2],'spectral_zeta_double_pole':[1,2],'double_pole_coefficient_times_pi':[1,4],'heat_log_coefficient_times_sqrt_pi':[1,4],'forced_frequency_scale':[1,2],'forced_a_over_pi':[2,1],'a_zero':'free Dirichlet half-line; no compact resolvent','normalizations':'all fixed a,c>0,b real in E=c^2 T^2+b; not arbitrary nonlinear changes','external_input':'Dobner arXiv:2101.01747v2 equation(1),Theorem1; unconditional unbounded S(T)'}
    return d
def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,default=ROOT/'results/c398_wall_evidence.json');a=p.parse_args();d=build();d['payload_sha256']=hashlib.sha256(canonical(d)).hexdigest();a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(d,sort_keys=True,indent=2)+'\n');print('C398 producer PASS: '+d['payload_sha256'])
if __name__=='__main__':main()
