from pathlib import Path

from centralizer_q.candidate import proof_only_contract, validate_proof_only_contract
from centralizer_q.protocol import stable_file_bytes


def test_registered_candidate_contract_has_zero_forbidden_counters() -> None:
    contract = proof_only_contract()
    assert validate_proof_only_contract(contract)["pass"]
    assert contract["intrinsic_prime_selector"] is False
    assert contract["route_b_open"] is False
    source = stable_file_bytes(Path(__file__).parents[1] / "centralizer_q" / "candidate.py").decode("utf-8")
    for field in (
        '"network_accesses": 0',
        '"external_data_loads": 0',
        '"numeric_s_evaluations": 0',
        '"numeric_log_evaluations": 0',
        '"random_draws": 0',
        '"equivariant_stacky_or_twisted_constructions": 0',
    ):
        assert field in source
