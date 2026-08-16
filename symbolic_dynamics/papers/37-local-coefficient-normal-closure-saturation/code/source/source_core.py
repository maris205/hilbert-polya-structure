"""Frozen source constructor for the Paper 37 exact audit.

This module constructs presentations, words, and coefficient matrices only.
It contains no acceptance predicate, target ledger, primality routine,
factorization routine, or numerical root data.  All scientific decisions are
made in ``independent_evaluator.py``, which does not import this module.
"""

from __future__ import annotations

from itertools import product
import random


ALPHABET = ("u", "U", "v", "V")
INVERSE = {"u": "U", "U": "u", "v": "V", "V": "v"}
RANDOM_SEED = 370037


def inverse_word(word: str) -> str:
    return "".join(INVERSE[letter] for letter in reversed(word))


def is_freely_reduced(word: str) -> bool:
    return all(word[index + 1] != INVERSE[word[index]]
               for index in range(len(word) - 1))


def is_cyclically_reduced(word: str) -> bool:
    return bool(word) and is_freely_reduced(word) and word[0] != INVERSE[word[-1]]


def is_literal_power(word: str) -> bool:
    for period in range(1, len(word)):
        if len(word) % period == 0 and word == word[:period] * (len(word) // period):
            return True
    return False


def affine_relator(exponent: int) -> str:
    """Return ``v u v^-1 u^-r`` for ``vuv^-1=u^r``."""
    if exponent < 1:
        raise ValueError("the exponent must be positive")
    return "vuV" + "U" * exponent


def sl2_connection(shear: int) -> dict[str, dict[str, tuple[int, int, int, int]]]:
    """A syntax-derived even/odd non-flat connection.

    The even and odd sectors use the same upper shear for ``u`` and opposite
    lower shears for ``v``.  Formal reverse letters receive exact inverses.
    The rule uses only the frozen source integer ``shear``.
    """
    if shear < 1:
        raise ValueError("the shear must be positive")
    upper = (1, 1, 0, 1)
    upper_inverse = (1, -1, 0, 1)
    lower_even = (1, 0, shear, 1)
    lower_even_inverse = (1, 0, -shear, 1)
    lower_odd = (1, 0, -shear, 1)
    lower_odd_inverse = (1, 0, shear, 1)
    return {
        "even": {
            "u": upper,
            "U": upper_inverse,
            "v": lower_even,
            "V": lower_even_inverse,
        },
        "odd": {
            "u": upper,
            "U": upper_inverse,
            "v": lower_odd,
            "V": lower_odd_inverse,
        },
    }


def reduced_conjugators(max_length: int) -> list[str]:
    words = [""]
    for length in range(1, max_length + 1):
        for letters in product(ALPHABET, repeat=length):
            word = "".join(letters)
            if is_freely_reduced(word):
                words.append(word)
    return words


def two_cell_products(relator: str, max_conjugator_length: int) -> list[dict[str, object]]:
    """Construct products of two conjugates of a relator or its inverse.

    No reduction or holonomy test occurs here.  The raw normal-closure words
    are handed to the independent evaluator.
    """
    relators = {1: relator, -1: inverse_word(relator)}
    rows: list[dict[str, object]] = []
    for left in reduced_conjugators(max_conjugator_length):
        left_inverse = inverse_word(left)
        for right in reduced_conjugators(max_conjugator_length):
            right_inverse = inverse_word(right)
            for left_sign in (1, -1):
                for right_sign in (1, -1):
                    raw = (left + relators[left_sign] + left_inverse
                           + right + relators[right_sign] + right_inverse)
                    rows.append({
                        "left_conjugator": left,
                        "right_conjugator": right,
                        "left_sign": left_sign,
                        "right_sign": right_sign,
                        "raw_word": raw,
                    })
    return rows


def deterministic_random_relators(count: int = 48) -> list[str]:
    """Generate a frozen family of generic cyclically reduced relators."""
    rng = random.Random(RANDOM_SEED)
    rows: list[str] = []
    while len(rows) < count:
        length = rng.randint(5, 10)
        letters: list[str] = []
        for index in range(length):
            choices = [letter for letter in ALPHABET
                       if not letters or letter != INVERSE[letters[-1]]]
            if index == length - 1 and letters:
                choices = [letter for letter in choices
                           if letter != INVERSE[letters[0]]]
            letters.append(rng.choice(choices))
        word = "".join(letters)
        if (word not in rows and is_cyclically_reduced(word)
                and not is_literal_power(word)):
            rows.append(word)
    return rows


def build_source_fixtures() -> dict[str, object]:
    affine_rows = []
    for exponent in range(1, 9):
        affine_rows.append({
            "exponent": exponent,
            "relator": affine_relator(exponent),
            "connection": sl2_connection(exponent),
            "mixed_candidates": two_cell_products(
                affine_relator(exponent), max_conjugator_length=3
            ),
        })

    random_relators = deterministic_random_relators(48)
    random_rows = []
    baseline_connection = sl2_connection(4)
    for index, relator in enumerate(random_relators):
        random_rows.append({
            "control_id": f"R{index:02d}",
            "relator": relator,
            "connection": baseline_connection,
            "mixed_candidates": two_cell_products(
                relator, max_conjugator_length=2
            ),
        })

    fixed_one_relator_rows = [
        {"control_id": "balanced_commutation", "relator": "vuVU"},
        {"control_id": "mutation_2_to_5", "relator": "vuuVUUUUU"},
        {"control_id": "mutation_3_to_7", "relator": "vuuuVUUUUUUU"},
        {"control_id": "mutation_2_to_8", "relator": "vuuVUUUUUUUU"},
        {"control_id": "commutator_squared_left", "relator": "vuuVUU"},
        {"control_id": "asymmetric_short", "relator": "uvvUVV"},
    ]
    for row in fixed_one_relator_rows:
        row["connection"] = baseline_connection
        row["mixed_candidates"] = two_cell_products(
            str(row["relator"]), max_conjugator_length=2
        )

    random_presentations = []
    for index in range(0, len(random_relators), 2):
        random_presentations.append({
            "control_id": f"P{index // 2:02d}",
            "relators": [random_relators[index], random_relators[index + 1]],
            "connection": baseline_connection,
        })

    return {
        "schema": "paper37-source-fixtures-v1",
        "alphabet": list(ALPHABET),
        "inverse": dict(INVERSE),
        "baseline_exponent": 4,
        "affine_rows": affine_rows,
        "fixed_one_relator_rows": fixed_one_relator_rows,
        "random_seed": RANDOM_SEED,
        "random_one_relator_rows": random_rows,
        "random_presentations": random_presentations,
        "source_prohibitions": {
            "accepted_support_table": False,
            "factorization_routine": False,
            "primality_routine": False,
            "target_coefficients": False,
            "target_zeros": False,
            "network_oracle": False,
        },
    }
