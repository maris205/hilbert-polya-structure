from pathlib import Path

from equivariant_clock.candidate import proof_only_contract, validate_proof_only_contract
from equivariant_clock.protocol import stable_file_bytes


def test_registered_candidate_contract_has_zero_forbidden_counters() -> None:
    contract = proof_only_contract()
    assert validate_proof_only_contract(contract)["pass"]
    assert contract["common_modulus_clock"] is False
    assert contract["intrinsic_prime_selector"] is False
    assert contract["route_b_open"] is False
    source = stable_file_bytes(
        Path(__file__).parents[1] / "equivariant_clock" / "candidate.py"
    ).decode("utf-8")
    for field in (
        '"network_access_count": 0',
        '"external_prime_data_access_count": 0',
        '"riemann_zero_data_access_count": 0',
        '"numeric_s_evaluation_count": 0',
        '"numeric_log_q_evaluation_count": 0',
        '"numeric_q_power_minus_s_evaluation_count": 0',
        '"random_seed_count": 0',
        '"new_zeta_definition_count": 0',
        '"cross_q_coefficient_ring_identification_count": 0',
        '"route_b_open_count": 0',
    ):
        assert field in source
    assert '"ambient_ring_varies_with_q": True' in source
    assert '"intrinsic_prime_selector": False' in source
    assert '"external_modulus_specialization_required": True' in source
