#!/usr/bin/env python3
"""Repaired-hash and stale-hash hostile tests for HCS-C158."""
from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import subprocess,sys,tempfile
ROOT=Path(__file__).resolve().parents[1];EVIDENCE=ROOT/"results/c158_full_cycle_evidence.json";CHECKER=ROOT/"code/c158_full_cycle_checker.py"
def digest(data):
    work=dict(data);work.pop("payload_sha256",None)
    return sha256(json.dumps(work,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def put(data,path,value):
    target=data
    for key in path[:-1]:target=target[key]
    target[path[-1]]=value
def main():
    source=json.loads(EVIDENCE.read_text())
    concentration=source["surviving_log_modulus_theorem"]["concentration_sentinels"]
    boundary_without_root_numbers={key:value for key,value in source["claim_boundary"].items() if key!="root_numbers"}
    mutations=[
      ("schema",("schema",),"x"),
      ("candidate",("candidate_id",),"x"),
      ("date",("evaluation_date",),"x"),
      ("scope",("scope_literal",),"x"),
      ("commit",("source_commit",),"x"),
      ("source_object",("source_lock","object"),"forged source object"),
      ("source_gate",("source_lock","gate"),"forged gate"),
      ("clock",("source_lock","clock"),"one full cycle"),
      ("secular",("source_lock","secular_convention"),"wrong"),
      ("scaling",("source_lock","scaling_convention"),"unnormalized"),
      ("cutoff",("source_lock","cutoffs","binomial_k_max"),23),
      ("precision",("source_lock","precision"),"float"),
      ("forbidden_data",("source_lock","forbidden_data"),"none"),
      ("source_lock_extra",("source_lock","forged"),True),
      ("tau",("one_site_spectrum","tau_q_sqrt3_i_sqrt3i",1),"1/3"),
      ("q",("one_site_spectrum","q0_q_sqrt3_i_sqrt3i",0),"0"),
      ("disc",("one_site_spectrum","discriminant_q_sqrt3_i_sqrt3i",0),"1"),
      ("simple",("one_site_spectrum","zero_simple"),False),
      ("distinct",("one_site_spectrum","nonzero_roots_distinct"),False),
      ("label",("one_site_spectrum","lambda_label"),"equal"),
      ("charpoly_text",("one_site_spectrum","characteristic_polynomial"),"lambda^3"),
      ("psum",("one_site_spectrum","squared_modulus_sum"),"0"),
      ("pprod",("one_site_spectrum","squared_modulus_product"),"1"),
      ("pdisc",("one_site_spectrum","squared_modulus_discriminant"),"0"),
      ("squared_moduli_text",("one_site_spectrum","squared_moduli"),"p_+=p_-"),
      ("decimal",("one_site_spectrum","decimal_sentinels","mu"),"0"),
      ("one_site_extra",("one_site_spectrum","forged"),True),
      ("cycle",("full_cycle_secular_theorem","identity"),"false"),
      ("factor",("full_cycle_secular_theorem","factorization"),"false"),
      ("degree",("full_cycle_secular_theorem","degree"),"3^k"),
      ("zerospace",("full_cycle_secular_theorem","zero_generalized_eigenspace_dimension"),"0"),
      ("trace_identity",("full_cycle_secular_theorem","trace_identity"),"Tr=0"),
      ("proof_basis",("full_cycle_secular_theorem","proof_basis"),"finite table"),
      ("theorem_extra",("full_cycle_secular_theorem","forged"),True),
      ("poly",("field_trace_and_polynomial_ledgers","3","coefficients_ascending",2,0),"999"),
      ("trace",("field_trace_and_polynomial_ledgers","4","trace_Ck_power_n",2,"value",0),"999"),
      ("field_basis",("field_trace_and_polynomial_ledgers","5","coefficient_basis"),"R"),
      ("field_row_extra",("field_trace_and_polynomial_ledgers","5","forged"),True),
      ("trace_row_extra",("field_trace_and_polynomial_ledgers","5","trace_Ck_power_n",0,"forged"),True),
      ("direct",("direct_kronecker_determinant_checks","2","direct_matrix_power_traces",1,0),"999"),
      ("directflag",("direct_kronecker_determinant_checks","3","matches_factor_theorem"),False),
      ("direct_row_extra",("direct_kronecker_determinant_checks","3","forged"),True),
      ("measure_text",("surviving_log_modulus_theorem","measure"),"delta_0"),
      ("binomial_model_text",("surviving_log_modulus_theorem","binomial_model"),"J_k=0"),
      ("mean",("surviving_log_modulus_theorem","mean"),"0"),
      ("variance",("surviving_log_modulus_theorem","variance"),"0"),
      ("hoeffding",("surviving_log_modulus_theorem","hoeffding"),"false"),
      ("weak",("surviving_log_modulus_theorem","weak_limit"),"false"),
      ("clt",("surviving_log_modulus_theorem","central_limit"),"false"),
      ("phase",("surviving_log_modulus_theorem","phase_limit_claimed"),True),
      ("scaling_extra",("surviving_log_modulus_theorem","forged"),True),
      ("binom",("surviving_log_modulus_theorem","binomial_ledgers",10,"rows",3,"multiplicity"),999),
      ("mass",("surviving_log_modulus_theorem","binomial_ledgers",12,"multiplicity_sum"),1),
      ("moment",("surviving_log_modulus_theorem","binomial_ledgers",15,"centered_2j_minus_k_square_sum"),1),
      ("bin_mean_identity",("surviving_log_modulus_theorem","binomial_ledgers",23,"mean_identity"),"mu=0"),
      ("bin_variance_identity",("surviving_log_modulus_theorem","binomial_ledgers",23,"variance_identity"),"Var=0"),
      ("bin_ledger_extra",("surviving_log_modulus_theorem","binomial_ledgers",23,"forged"),True),
      ("bin_row_extra",("surviving_log_modulus_theorem","binomial_ledgers",23,"rows",0,"forged"),True),
      ("tail",("surviving_log_modulus_theorem","concentration_sentinels",2,"exact_tail_numerator"),1),
      ("bound",("surviving_log_modulus_theorem","concentration_sentinels",3,"hoeffding_bound_decimal"),"9"),
      ("concentration_event",("surviving_log_modulus_theorem","concentration_sentinels",0,"event"),"wrong event"),
      ("concentration_bound_text",("surviving_log_modulus_theorem","concentration_sentinels",0,"hoeffding_bound"),"1"),
      ("concentration_delete_k64",("surviving_log_modulus_theorem","concentration_sentinels"),deepcopy(concentration[:-1])),
      ("concentration_append_extra",("surviving_log_modulus_theorem","concentration_sentinels"),deepcopy(concentration)+[deepcopy(concentration[-1])]),
      ("concentration_row_extra",("surviving_log_modulus_theorem","concentration_sentinels",0,"forged"),True),
      ("controls_extra",("controls","forged"),True),
      ("closed_projector",("controls","closed_parent","projector"),"0"),
      ("closed",("controls","closed_parent","result"),"nonunitary"),
      ("closed_extra",("controls","closed_parent","forged"),True),
      ("order_gate",("controls","projector_order","gate"),"forged gate"),
      ("order",("controls","projector_order","result"),"changes"),
      ("order_extra",("controls","projector_order","forged"),True),
      ("moved_projector",("controls","moved_hole","projector"),"diag(1,1,0)"),
      ("movedspec",("controls","moved_hole","nonzero_eigenvalues"),"equal"),
      ("moved_rank_degree",("controls","moved_hole","rank_and_degree"),"rank 1"),
      ("movedmean",("controls","moved_hole","mean_changes"),True),
      ("movedvar",("controls","moved_hole","variance_changes"),False),
      ("moved_variance_text",("controls","moved_hole","variance"),"sigma_0^2=0"),
      ("moved_extra",("controls","moved_hole","forged"),True),
      ("tuple",("route_a","tuple",0),"A1_PASS"),
      ("routeb",("route_a","route_b_invocation_allowed"),True),
      ("flag",("claim_boundary","phase_limit"),True),
      ("claim_false_extra",("claim_boundary","forged"),False),
      ("claim_delete_root_numbers",("claim_boundary",),boundary_without_root_numbers),
      ("extra",("route_a","forged"),True)]
    rejected=[]
    with tempfile.TemporaryDirectory(prefix="c158-mutations-") as temporary:
      for name,path,value in mutations:
        candidate=deepcopy(source);put(candidate,path,value);candidate["payload_sha256"]=digest(candidate);output=Path(temporary)/f"{name}.json";output.write_text(json.dumps(candidate,sort_keys=True,indent=2)+"\n")
        result=subprocess.run([sys.executable,str(CHECKER),str(output),"--mutation-fast"],capture_output=True,text=True)
        if result.returncode==0:raise AssertionError(f"checker accepted repaired mutation {name}")
        rejected.append(name)
      stale=deepcopy(source);stale["payload_sha256"]="0"*64;output=Path(temporary)/"stale.json";output.write_text(json.dumps(stale,sort_keys=True,indent=2)+"\n")
      if subprocess.run([sys.executable,str(CHECKER),str(output),"--mutation-fast"],capture_output=True,text=True).returncode==0:raise AssertionError("checker accepted stale hash")
    print(json.dumps({"status":"C158_MUTATION_PASS","repaired_hash_rejected":len(rejected),"stale_hash_rejected":1,"total":len(rejected)+1,"names":rejected},sort_keys=True))
if __name__=="__main__":main()
