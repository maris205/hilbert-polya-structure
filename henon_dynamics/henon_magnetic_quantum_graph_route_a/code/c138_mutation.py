#!/usr/bin/env python3
"""Repaired-hash semantic plus stale-hash mutation suite for C138."""
import copy,hashlib,importlib.util,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("c138_checker",ROOT/"code/c138_magnetic_graph_checker.py"); checker=importlib.util.module_from_spec(spec); assert spec.loader; spec.loader.exec_module(checker)
base=json.loads((ROOT/"results/c138_magnetic_graph_evidence.json").read_text())


def trial(path,value,repair=True):
    data=copy.deepcopy(base); node=data
    for key in path[:-1]: node=node[key]
    node[path[-1]]=value
    if repair:
        data.pop("payload_sha256",None); data["payload_sha256"]=hashlib.sha256(json.dumps(data,sort_keys=True,separators=(",",":")).encode()).hexdigest()
    return data


mutations=[
(["unexpected_top_level"],True,True),(["schema"],"bad",True),(["candidate_id"],"HCS-X",True),(["scope"],"open",True),
(["graph","edge_lengths",2],4,True),(["graph","directed_bond_order",0],"-1",True),(["graph","vertex_condition"],"Dirichlet",True),
(["scattering","C_orthogonal"],False,True),(["scattering","kirchhoff_C",0,0],"0",True),(["magnetic_family","operator"],"P*S",True),
(["magnetic_family","unitary_for_real_k_alpha"],False,True),(["magnetic_family","common_phase_gauge"],"covariant only",True),
(["magnetic_family","gauge_invariant_flux_coordinates",0],"alpha_1",True),(["magnetic_family","antiunitary_identity"],"fixed alpha",True),
(["magnetic_family","orientation_statement"],"each phase is even",True),(["laurent_determinant","rho_degree"],4,True),
(["laurent_determinant","rho_coefficients","2"],"0",True),(["laurent_determinant","rho_coefficients","4"],"0",True),
(["laurent_determinant","closed_form"],"1",True),(["laurent_determinant","common_q_scaling_invariant"],False,True),
(["laurent_determinant","q_inversion_invariant"],False,True),(["laurent_determinant","zero_flux_c133_factor"],"0",True),
(["oriented_orbit_ledger","periods_through_8",1,"rooted_closed_walks"],17,True),
(["oriented_orbit_ledger","periods_through_8",3,"primitive_cycles"],35,True),
(["oriented_orbit_ledger","periods_through_8",7,"rooted_ledger_sha256"],"0"*64,True),
(["oriented_orbit_ledger","rooted_closed_walks_through_8"],14759,True),(["oriented_orbit_ledger","primitive_cycles_through_8"],1904,True),
(["oriented_orbit_ledger","phase_rule"],"cosine",True),(["oriented_orbit_ledger","shortest_orientation_witnesses",0,"phase"],"cos(alpha)",True),
(["controls","zero_flux_recovery","passes"],False,True),(["controls","common_phase_gauge","passes"],False,True),
(["controls","pi_flux","changes_determinant"],False,True),(["controls","pi_over_2_fixed_alpha_reversal","wrong_fixed_alpha_defect_nonzero_entries"],0,True),
(["controls","pi_over_2_fixed_alpha_reversal","wrong_fixed_alpha_frobenius_norm_squared"],"0",True),
(["controls","wrong_vertex_normalization","unitary"],True,True),(["controls","direction_asymmetric_reverse_length","preserves_reversal"],True,True),
(["progress","orientation_sensitive_orbit_ledger"],"FAIL",True),(["route_a","tuple"],["A1_WEAK","A2_FAIL","A3_FAIL","A4_FAIL"],True),
(["route_a","route_b_invocation_allowed"],True,True),(["scope_flags","claims_target_divisor"],True,True),
(["scope_flags","claims_euler_factors"],True,True),(["scope_flags","claims_hilbert_polya"],True,True),(["scope_flags","renamed_false_flag"],False,True),
(["nonclaims",0],"prime match",True),(["payload_sha256"],"0"*64,False)]
caught=0
for path,value,repair in mutations:
    try: checker.validate(trial(path,value,repair))
    except (AssertionError,KeyError,ValueError,TypeError): caught+=1
assert caught==len(mutations)
print(f"C138 mutation suite: PASS ({caught}/{len(mutations)} rejected; {len(mutations)-1} repaired-hash + 1 stale-hash)")
