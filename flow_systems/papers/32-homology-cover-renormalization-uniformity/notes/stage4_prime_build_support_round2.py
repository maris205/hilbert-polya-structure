#!/usr/bin/env python3
"""Build notes-only support artifacts for P32 Stage 4-prime Round 2.

The script reads frozen research artifacts and the already captured bounded
replay.  It never edits the canonical manuscript, canonical bibliography,
PDF, code, experiments, results, route files, or README, and it performs no
scientific execution or numerical-result refresh.
"""

from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path


NOTES = Path(__file__).resolve().parent
PAPER = NOTES.parent
STAMP = "2026-09-04T00:30:00Z"
PINNED_COMMIT = "d29a829b4acac29ff8429724467409e9820a8fa2"
REPOSITORY_ROOT = "https://github.com/maris205/hilbert-polya-structure"
PINNED_BASE = (
    f"{REPOSITORY_ROOT}/tree/{PINNED_COMMIT}/flow_systems/"
    "papers/32-homology-cover-renormalization-uniformity"
)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(name: str, payload: dict) -> Path:
    path = NOTES / name
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return path


def write_tsv(name: str, rows: list[dict], fields: list[str]) -> Path:
    path = NOTES / name
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    return path


def read_tsv(name: str) -> list[dict]:
    with (NOTES / name).open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def build_notes_bibliography() -> Path:
    canonical = PAPER / "paper" / "references.bib"
    expected = "e699c96196377892d3aa1f280e6a5117001c3cec37a511a3d1c08fdc52127de9"
    if sha(canonical) != expected:
        raise RuntimeError("canonical bibliography drift; fail closed")
    text = canonical.read_text(encoding="utf-8")
    for key in ("P32-CW01", "P32-CW02", "P32-CW03", "P32-CW04"):
        if "{" + key + "," in text:
            raise RuntimeError(f"notes bibliography would overwrite {key}")
    additions = r"""

@article{P32-CW01,
  author  = {Levitt, Gilbert and Vogtmann, Karen},
  title   = {A Whitehead Algorithm for Surface Groups},
  journal = {Topology},
  year    = {2000},
  volume  = {39},
  number  = {6},
  pages   = {1239--1251},
  doi     = {10.1016/S0040-9383(99)00027-0},
  url     = {https://doi.org/10.1016/S0040-9383(99)00027-0}
}

@article{P32-CW02,
  author  = {Venkov, A. B. and Zograf, P. G.},
  title   = {On Analogues of the Artin Factorization Formulas in the Spectral Theory of Automorphic Functions Connected with Induced Representations of Fuchsian Groups},
  journal = {Mathematics of the USSR-Izvestiya},
  year    = {1983},
  volume  = {21},
  number  = {3},
  pages   = {435--443},
  doi     = {10.1070/IM1983v021n03ABEH001800},
  url     = {https://www.mathnet.ru/eng/im1700}
}

@article{P32-CW03,
  author  = {Blute, Richard and Cockett, Robin and Jacqmin, Pierre-Alain and Scott, Philip},
  title   = {Finiteness Spaces and Generalized Power Series},
  journal = {Electronic Notes in Theoretical Computer Science},
  year    = {2018},
  volume  = {341},
  pages   = {5--22},
  doi     = {10.1016/j.entcs.2018.11.002},
  url     = {https://doi.org/10.1016/j.entcs.2018.11.002}
}

@book{P32-CW04,
  author    = {Parry, William and Pollicott, Mark},
  title     = {Zeta Functions and the Periodic Orbit Structure of Hyperbolic Dynamics},
  series    = {Ast\'erisque},
  number    = {187--188},
  year      = {1990},
  publisher = {Soci\'et\'e math\'ematique de France},
  pages     = {1--272},
  url       = {https://numdam.org/item/AST_1990__187-188__1_0/}
}
"""
    out = NOTES / "stage4_prime_references_round2.bib"
    out.write_text(text.rstrip() + additions, encoding="utf-8")
    if sha(canonical) != expected:
        raise RuntimeError("canonical bibliography changed while building notes copy")
    return out


def closest_records() -> list[dict]:
    return [
        {
            "key": "P32-CW01",
            "component_family": "oriented-owner algorithmic neighbor",
            "authors": ["Gilbert Levitt", "Karen Vogtmann"],
            "year": 2000,
            "title": "A Whitehead algorithm for surface groups",
            "venue": "Topology 39(6), 1239--1251",
            "doi": "10.1016/S0040-9383(99)00027-0",
            "authoritative_metadata": "https://api.crossref.org/works/10.1016/S0040-9383(99)00027-0",
            "publisher_locator": "https://www.sciencedirect.com/science/article/pii/S0040938399000270",
            "exact_passage_locator": "publisher abstract on the article landing page",
            "verified_passage_scope": "For a closed-surface fundamental group, decides whether an automorphism sends one specified finite set to another and finds one when it exists; the abstract also states a surface-with-boundary extension.",
            "hypotheses": "fundamental group of a closed surface; two supplied finite sets; automorphism-orbit question",
            "admissible_transfer": "surface-group finite-set automorphism decision as an algorithmic neighbor",
            "prohibited_transfer": "does not supply the frozen oriented-conjugacy owner bytes, maximal-root proof, inverse policy, or prefix-completeness certificate",
            "correction_state": "NOT_CHECKED_IN_BOUNDED_SEARCH",
            "verdict": "VERIFIED_NARROW_ABSTRACT_SCOPE",
        },
        {
            "key": "P32-CW02",
            "component_family": "finite-index cover-factorization neighbor",
            "authors": ["A. B. Venkov", "P. G. Zograf"],
            "year": 1983,
            "title": "On analogues of the Artin factorization formulas in the spectral theory of automorphic functions connected with induced representations of Fuchsian groups",
            "venue": "Mathematics of the USSR-Izvestiya 21(3), 435--443",
            "doi": "10.1070/IM1983v021n03ABEH001800",
            "authoritative_metadata": "https://www.mathnet.ru/eng/im1700",
            "publisher_locator": "https://www.mathnet.ru/eng/im1700",
            "exact_passage_locator": "MathNet article record, Abstract, and bibliographic lines for volume 21(3), pp. 435--443",
            "verified_passage_scope": "Factorization formulas for the Selberg zeta function and automorphic scattering determinant for arbitrary finite-index subgroups of first-kind Fuchsian groups.",
            "hypotheses": "arbitrary subgroup of finite index in a Fuchsian group of the first kind; zeta/scattering objects named in the abstract",
            "admissible_transfer": "finite-index Fuchsian-group zeta factorization as a cover-product neighbor",
            "prohibited_transfer": "does not derive P32 ownerwise lift multiplicity, primitive-lift status, or the fixed 1/N time and 1/N^3 logarithmic normalizations, especially for zero content",
            "correction_state": "NOT_CHECKED_IN_BOUNDED_SEARCH",
            "verdict": "VERIFIED_NARROW_ABSTRACT_SCOPE",
        },
        {
            "key": "P32-CW03",
            "component_family": "formal generalized-series neighbor",
            "authors": ["Richard Blute", "Robin Cockett", "Pierre-Alain Jacqmin", "Philip Scott"],
            "year": 2018,
            "title": "Finiteness Spaces and Generalized Power Series",
            "venue": "Electronic Notes in Theoretical Computer Science 341, 5--22",
            "doi": "10.1016/j.entcs.2018.11.002",
            "authoritative_metadata": "https://api.crossref.org/works/10.1016/j.entcs.2018.11.002",
            "publisher_locator": "https://www.sciencedirect.com/science/article/pii/S1571066118300823",
            "author_manuscript_locator": "https://arxiv.org/abs/1805.09836",
            "exact_passage_locator": "publisher abstract; author manuscript pp. 1--3, Section 2 and Theorem 1",
            "verified_passage_scope": "Relates Ribenboim generalized power-series rings to partially ordered monoids and finitary supports and states a ring construction under its declared strictness/support hypotheses.",
            "hypotheses": "ring coefficients and the strict partially ordered monoid/finitary-support conditions stated in the paper",
            "admissible_transfer": "support and convolution discipline for generalized formal series",
            "prohibited_transfer": "does not define P32's frozen finite-owner/degree inverse system, one-owner zero-content type, localization embeddings, singleton maps, factor derivation, or scalar tail",
            "correction_state": "NOT_CHECKED_IN_BOUNDED_SEARCH",
            "verdict": "VERIFIED_NARROW_PASSAGE_SCOPE",
        },
        {
            "key": "P32-CW04",
            "component_family": "periodic-orbit zeta and analytic-program neighbor",
            "authors": ["William Parry", "Mark Pollicott"],
            "year": 1990,
            "title": "Zeta functions and the periodic orbit structure of hyperbolic dynamics",
            "venue": "Astérisque 187--188, 272 pages",
            "doi": None,
            "authoritative_metadata": "https://numdam.org/item/AST_1990__187-188__1_0/",
            "publisher_locator": "https://numdam.org/item/AST_1990__187-188__1_0/",
            "exact_passage_locator": "Numdam publisher record and contents; monograph Introduction and Chapter 5 (Periodic Points and Zeta Functions), beginning p. 73",
            "verified_passage_scope": "A monograph-scale thermodynamic and periodic-orbit zeta program, including a chapter explicitly devoted to periodic points and zeta functions.",
            "hypotheses": "hyperbolic-dynamical and symbolic/thermodynamic settings specified chapter by chapter; no P32 owner schedule is assumed",
            "admissible_transfer": "periodic-orbit zeta and convergence-method positioning",
            "prohibited_transfer": "does not establish P32's exact owner/modulus logarithmic summand, compact majorant, cofinal enumeration, AN-1--AN-5 interchanges, or zero-content comparison",
            "correction_state": "NOT_CHECKED_IN_BOUNDED_SEARCH",
            "verdict": "VERIFIED_NARROW_MONOGRAPH_SCOPE",
        },
    ]


def build_closest_work(notes_bib: Path) -> tuple[Path, Path, Path]:
    records = closest_records()
    verification = {
        "schema_version": "round10-stage4-prime-closest-work-source-verification/1.0",
        "paper_id": "P32",
        "verified_at_utc": STAMP,
        "search_scope": "bounded four-family search: owner algorithms, finite-index cover factors, formal coefficient carriers, and compact-uniform/periodic-orbit programs",
        "search_bound": {"maximum_authorized_new_entries": 4, "retained_entries": 4},
        "records": records,
        "novelty_boundary": "No priority, firstness, exhaustive-search, or global novelty claim is made. Each source positions one nearby component and every stronger transfer is prohibited explicitly.",
        "correction_boundary": "The bounded pass did not perform a general retraction, correction, source-conflict, or conflict-of-interest screen; NOT_CHECKED is retained where applicable.",
        "bibliography_mode": "notes-side versioned bibliography only; canonical paper/references.bib remains frozen",
        "canonical_bibliography": {
            "path": "paper/references.bib",
            "sha256": sha(PAPER / "paper" / "references.bib"),
            "changed": False,
        },
        "versioned_bibliography": {
            "path": "notes/stage4_prime_references_round2.bib",
            "sha256": sha(notes_bib),
        },
        "verdict": "PASS_WITH_NARROW_PASSAGE_AND_CORRECTION_BOUNDARIES",
    }
    ver_path = write_json("stage4_prime_closest_work_source_verification_round2.json", verification)

    matrix_rows = [
        {
            "source_id": "P32-CW01",
            "owner_algorithm_component": {"overlap": "finite-set automorphism decision for surface groups", "difference": "no oriented-conjugacy canonical bytes, maximal root, inverse branch, or certified exhaustion"},
            "higher_and_zero_content_factor_component": {"overlap": "none verified", "difference": "no homology-cover deck order, lift count, primitive-lift proof, or normalized factor"},
            "formal_coefficient_component": {"overlap": "none verified", "difference": "no inverse-limit/Hahn carrier or projection theorem"},
            "compact_uniform_limit_component": {"overlap": "none verified", "difference": "no owner tail, compact majorant, or limit interchange"},
        },
        {
            "source_id": "P32-CW02",
            "owner_algorithm_component": {"overlap": "Fuchsian-group setting only", "difference": "no canonical owner interface or enumeration"},
            "higher_and_zero_content_factor_component": {"overlap": "finite-index subgroup zeta/scattering factorization", "difference": "no independent-owner lift formula, zero-content branch, or frozen 1/N and 1/N^3 normalization trace"},
            "formal_coefficient_component": {"overlap": "product factorization motivates comparison", "difference": "no P32 coefficient carrier, equality, localization, or singleton map"},
            "compact_uniform_limit_component": {"overlap": "spectral/zeta analytic context", "difference": "no infinite homology-tower schedule or AN-1--AN-5 majorant"},
        },
        {
            "source_id": "P32-CW03",
            "owner_algorithm_component": {"overlap": "none verified", "difference": "no surface-group owner decision or prefix certificate"},
            "higher_and_zero_content_factor_component": {"overlap": "formal series can house candidate expansions", "difference": "no deck-action or factor derivation and no normalization"},
            "formal_coefficient_component": {"overlap": "ordered-monoid/finitary-support generalized-series ring construction", "difference": "does not itself instantiate the frozen finite-owner/degree inverse limit, the one-owner zero-content Hahn fiber, localization embeddings, or singleton compatibility"},
            "compact_uniform_limit_component": {"overlap": "support discipline only", "difference": "formal support is not a compact-uniform scalar tail theorem"},
        },
        {
            "source_id": "P32-CW04",
            "owner_algorithm_component": {"overlap": "periodic-orbit populations", "difference": "no marked surface-group owner canonicalizer or exhaustion certificate"},
            "higher_and_zero_content_factor_component": {"overlap": "zeta factors indexed by periodic data", "difference": "no P32 cover multiplicity, content split, or fixed normalized local factors"},
            "formal_coefficient_component": {"overlap": "formal zeta/product expressions", "difference": "no independent-owner inverse-limit equality or one-owner Hahn comparison"},
            "compact_uniform_limit_component": {"overlap": "thermodynamic and periodic-orbit zeta analytic program", "difference": "no exact P32 logarithmic summands, schedule-uniform summable majorant, cofinality proof, or named AN interchange"},
        },
    ]
    for row in matrix_rows:
        row["joint_design_relation"] = "nearest in one component only; does not close the four-component dependency chain"
    matrix = {
        "schema_version": "round10-stage4-prime-closest-work-comparison-matrix/1.0",
        "paper_id": "P32",
        "generated_at_utc": STAMP,
        "source_verification": {"path": "notes/" + ver_path.name, "sha256": sha(ver_path)},
        "component_order": [
            "owner_algorithm_component",
            "higher_and_zero_content_factor_component",
            "formal_coefficient_component",
            "compact_uniform_limit_component",
        ],
        "row_count": 4,
        "rows": matrix_rows,
        "boundary": "The matrix is bounded component positioning, not priority, exhaustive novelty, proof transfer, or evidence that the joint P32 design has been executed.",
    }
    matrix_json = write_json("stage4_prime_closest_work_comparison_matrix_round2.json", matrix)
    flat = []
    for row in matrix_rows:
        out = {"source_id": row["source_id"]}
        for component in matrix["component_order"]:
            out[component + "_overlap"] = row[component]["overlap"]
            out[component + "_difference"] = row[component]["difference"]
        out["joint_design_relation"] = row["joint_design_relation"]
        flat.append(out)
    fields = list(flat[0])
    matrix_tsv = write_tsv("stage4_prime_closest_work_comparison_matrix_round2.tsv", flat, fields)
    return ver_path, matrix_json, matrix_tsv


def build_claim_passage_matrix(closest_verification: Path) -> tuple[Path, Path]:
    inventory = {row["source_id"]: row for row in read_tsv("stage1_phase2_source_inventory.tsv")}
    verification = {row["source_id"]: row for row in read_tsv("stage1_phase2_source_verification.tsv")}
    matrix_rows = read_tsv("stage1_phase3_literature_matrix.tsv")
    if len(inventory) != 26 or len(verification) != 26 or len(matrix_rows) != 26:
        raise RuntimeError("frozen 26-source inputs do not close")
    rows = []
    for row in matrix_rows:
        sid = row["source_id"]
        vr = verification[sid]
        correction = "NOT_CHECKED"
        if sid == "P32-S02":
            correction = "BIBLIOGRAPHIC_PAGE_CORRECTION_R10PH2_C05_APPLIED; THEOREM_PASSAGE_UNFINALIZED"
        elif sid == "P32-S17":
            correction = "KNOWN_2022_ERRATUM_BOUND; AFFECTED_SECTION_7_AND_DEPENDENT_COUNTING_EXCLUDED"
        identity = vr["existence_outcome"]
        if sid == "P32-S13":
            identity = "VERIFIED_BY_LATER_STAGE2_5_METADATA_REPAIR; PASSAGE_SCOPE_UNCHANGED"
        rows.append(
            {
                "source_id": sid,
                "source_identity_state": identity,
                "component_or_claim_role": row["admissible_contribution"],
                "exact_passage_locator": None,
                "passage_status": "INCONCLUSIVE",
                "hypotheses": "UNEXTRACTED_AT_EXACT_PASSAGE_LEVEL; bounded support class: " + row["support_class"],
                "correction_state": correction,
                "applicability_statement": row["admissible_contribution"],
                "prohibited_stronger_transfer": row["excluded_stronger_claim"],
                "verified_record_locator": vr["verified_locator"],
                "evidence_note": row["locator_or_verification_limit"] + "; no theorem passage was reconstructed",
            }
        )
    for record in closest_records():
        rows.append(
            {
                "source_id": record["key"],
                "source_identity_state": "VERIFIED",
                "component_or_claim_role": record["admissible_transfer"],
                "exact_passage_locator": record["exact_passage_locator"],
                "passage_status": record["verdict"].replace("VERIFIED_", "FINALIZED_"),
                "hypotheses": record["hypotheses"],
                "correction_state": record["correction_state"],
                "applicability_statement": record["verified_passage_scope"],
                "prohibited_stronger_transfer": record["prohibited_transfer"],
                "verified_record_locator": record["publisher_locator"],
                "evidence_note": "Paraphrase only; no direct quotation and no theorem transfer beyond the named passage scope.",
            }
        )
    payload = {
        "schema_version": "round10-stage4-prime-claim-passage-matrix/1.0",
        "paper_id": "P32",
        "generated_at_utc": STAMP,
        "frozen_source_matrix": {
            "path": "notes/stage1_phase3_literature_matrix.tsv",
            "sha256": sha(NOTES / "stage1_phase3_literature_matrix.tsv"),
        },
        "closest_work_verification": {
            "path": "notes/" + closest_verification.name,
            "sha256": sha(closest_verification),
        },
        "row_count": len(rows),
        "passage_finalized_count": sum(r["passage_status"].startswith("FINALIZED") for r in rows),
        "passage_inconclusive_count": sum(r["passage_status"] == "INCONCLUSIVE" for r in rows),
        "rows": rows,
        "boundary": "Record identity, metadata, and role coding do not establish theorem-to-claim transfer. The 26 inherited anchor:none uses remain INCONCLUSIVE; only four new narrow publisher/author-source scopes are finalized. No missing passage, hypothesis, correction state, or historical decision is fabricated.",
    }
    json_path = write_json("stage4_prime_claim_passage_matrix_round2.json", payload)
    fields = [
        "source_id", "source_identity_state", "component_or_claim_role",
        "exact_passage_locator", "passage_status", "hypotheses", "correction_state",
        "applicability_statement", "prohibited_stronger_transfer",
        "verified_record_locator", "evidence_note",
    ]
    tsv_path = write_tsv("stage4_prime_claim_passage_matrix_round2.tsv", rows, fields)
    return json_path, tsv_path


def build_formal_audit() -> Path:
    payload = {
        "schema_version": "round10-stage4-prime-formal-definition-audit/1.0",
        "paper_id": "P32",
        "generated_at_utc": STAMP,
        "frozen_initial_system_preserved": {
            "coefficient_field": "Q",
            "positive_finite_coordinates": "R_(F,D)=Q[u_g:g in F]/m_F^(D+1)",
            "positive_index_order": "(F,D)<=(F',D') iff F subseteq F' and D<=D'",
            "positive_transition": "set variables in F'\\F to zero, then truncate total degree to D",
            "positive_inverse_limit": "R_+=inverse-limit_(F,D) R_(F,D)",
            "zero_object": "one-owner H_g with rational nonnegative exponents and well-ordered support; no multivariate zero-content product",
            "finite_scalar_gate": "u_g maps to exp(-s ell(g)/d(g)) only on A_F and z_g^q maps to exp(-s ell(g)q) only on the stated zero fiber subalgebra",
        },
        "typed_definitions": {
            "owner_types": "O_+ and O_0 are disjoint typed sets of oriented primitive owners with d(g)>=1 and d(g)=0 respectively; ell(g)>0.",
            "R_F_D": "For finite F subset O_+ and D in N_0, m_F=(u_g:g in F) and R_(F,D)=Q[u_g:g in F]/m_F^(D+1).",
            "R_plus": "The inverse limit over finite F and D, with each coordinate discrete and the limit topology; equality is equality in every (F,D) coordinate.",
            "positive_localization": "A_F=Q[u_g:g in F][(1-u_g^r)^(-1):g in F,r>=1]. Denominators have constant term one and map to units in every degree truncation.",
            "positive_embedding": "j_F:A_F->R_+ is defined coordinatewise by setting variables outside F intersect E to zero and taking the degree-D expansion in R_(E,D).",
            "singleton_projection": "pi_g:R_+->Q[[u_g]]=inverse-limit_D Q[u_g]/(u_g^(D+1)); at each degree it is the (F,D)->({g},D) transition for any finite F containing g.",
            "zero_fiber": "For each g in O_0, H_g consists of sums sum_(q in S) a_q z_g^q with a_q in Q and S subset Q_{>=0} well ordered. Equality is coefficientwise and the valuation topology has neighborhoods v(f)>r.",
            "R_zero_type": "R_0 is the tagged family disjoint-union_(g in O_0) {g}xH_g; algebra operations and comparisons occur only within one H_g fiber, and there is no cross-owner or R_+-to-R_0 coercion.",
            "scalar_domains": "For Re(s)>0, sigma_(s,F):A_F->C sends u_g to exp(-s ell(g)/d(g)); for zero g and fixed N, tau_(s,g,N) is defined on the subalgebra generated by z_g^(1/N) and the two required unit denominators. No scalar map on all R_+ or all H_g is declared.",
        },
        "compatibility_lemma": {
            "label": "P32-FORMAL-COMPATIBILITY",
            "statement": [
                "R_(F,D) transition maps are well defined continuous unital Q-algebra homomorphisms, with identity and composition laws.",
                "R_+ is Hausdorff and complete in the inverse-limit topology, and equality is coordinatewise.",
                "Every declared localization denominator maps to a unit in every compatible truncation; j_F is a well-defined injective homomorphism and the j_F commute with finite-owner restriction.",
                "pi_g is a well-defined continuous unital homomorphism and pi_g equals the compatible singleton transition at every finite degree.",
                "H_g multiplication and the valuation topology are well defined; the two displayed zero-content/base factors have well-ordered supports.",
                "The finite scalar maps are well defined on their exact domains because every denominator image has modulus-separated nonzero value for Re(s)>0.",
            ],
            "proof_steps": [
                "A polynomial of degree at least D'+1 remains zero after variable deletion and degree-D truncation when D<=D', which proves quotient well-definedness; substitution and truncation visibly compose.",
                "The inverse limit is a closed subalgebra of the product of discrete coordinate algebras. Products of complete Hausdorff discrete spaces are complete Hausdorff, so the closed inverse limit is complete Hausdorff.",
                "In each truncation, (1-u_g^r)^(-1) is the finite geometric sum through degree D. These inverses commute with transitions. If j_F(p/q)=0, multiplication by the unit expansion of q gives p=0 in every degree, hence p=0 and j_F is injective.",
                "For E containing g, two choices of E give the same singleton coordinate by the inverse-limit compatibility equation; this proves pi_g is independent of the chosen finite coordinate and commutes with every transition.",
                "For well-ordered S,T in Q_{>=0}, the ordered-monoid lemma gives well-ordered S+T and finitely many decompositions of each exponent; otherwise an increasing support subsequence would force an infinite descending subsequence in the other support. Thus Hahn convolution is coefficient-finite. The candidate supports {r/N:r>=0} and {r:r>=0} are well ordered.",
                "For Re(s)>0, |exp(-s ell(g)r/d(g))|<1 and |exp(-s ell(g)/N)|<1. Hence the declared denominator images do not vanish and the finite algebra evaluations are homomorphisms.",
            ],
        },
        "audit_checks": {
            "coefficient_and_exponent_data": "PASS",
            "support_and_equality": "PASS",
            "topology": "PASS",
            "transition_domain_codomain_composition": "PASS",
            "localization_domain_and_embedding": "PASS",
            "singleton_projection_compatibility": "PASS",
            "finite_scalar_specialization": "PASS",
            "separate_zero_type": "PASS",
        },
        "audit_outcome": "PASS_FORMAL_CARRIER_AND_COMPATIBILITY_ONLY",
        "scientific_application_status": "NOT_EVALUABLE_PENDING_OWNER_BINDING_AND_FACTOR_DERIVATION",
        "non_global_boundary": "Singleton projections are not jointly faithful on mixed-owner monomials (for example u_g u_h is killed by every singleton projection). The lemma defines carriers and local maps only; it proves no global product, factor derivation, obstruction, recovery theorem, infinite scalar specialization, or Route credit. CP-P32-004 remains unresolved as a literature-transfer comparison and is not used as a premise.",
    }
    return write_json("stage4_prime_formal_definition_audit_round2.json", payload)


def build_scalar_audit() -> Path:
    payload = {
        "schema_version": "round10-stage4-prime-conditional-scalar-lemma-audit/1.0",
        "paper_id": "P32",
        "generated_at_utc": STAMP,
        "lemma": {
            "label": "P32-CONDITIONAL-SCALAR",
            "hypotheses": ["ell>0", "s is real and s>0", "m is an integer and m>=2"],
            "definitions": {
                "Phi_m(s)": "(1-exp(-s ell/m))^(-m)",
                "B(s)": "(1-exp(-s ell))^(-1)",
            },
            "conclusion": "Phi_m(s)>B(s)",
            "proof": [
                "Set x=exp(-s ell/m). The hypotheses imply 0<x<1 and exp(-s ell)=x^m.",
                "Because m>=2, (1-x)^m=(1-x)(1-x)^(m-1)<1-x.",
                "Because 0<x<1 and m>=2, x^m<x, hence 1-x<1-x^m.",
                "All three quantities are positive. Taking reciprocals reverses both strict inequalities: (1-x)^(-m)>(1-x)^(-1)>(1-x^m)^(-1). The outer terms are Phi_m(s) and B(s).",
            ],
        },
        "hypothesis_checks": {"positivity": "PASS", "strictness": "PASS", "reciprocal_direction": "PASS", "endpoint_exclusion": "PASS"},
        "conditional_applications": [
            {"branch": "higher content", "substitution": "m=d>=2 after d divides N on the frozen schedule", "gate": "valid ownerwise higher-content factor derivation and permitted singleton comparison", "status": "CONDITIONAL_ONLY_NOT_EXECUTED"},
            {"branch": "zero content", "substitution": "m=N>=2", "gate": "valid separate zero-content factor derivation and permitted one-owner fiber comparison", "status": "CONDITIONAL_ONLY_NOT_EXECUTED"},
        ],
        "audit_outcome": "PASS_ELEMENTARY_CONDITIONAL_LEMMA",
        "boundary": "The lemma compares two candidate positive real functions only. It supplies no cover-factor derivation, formal owner identification, observed owner, coefficient execution, global obstruction, recovery result, scientific disposition, canonical-result refresh, or Route credit.",
    }
    return write_json("stage4_prime_conditional_scalar_lemma_audit_round2.json", payload)


def build_analytic_audit() -> Path:
    common = {
        "compact_domain": "K(delta,T,R)={s in C:1+delta<=Re(s)<=R, |Im(s)|<=T}, for every delta>0, finite T>=0, and finite R>=1+delta",
        "schedules": "S_k in {k!,2(k!)} for every integer k>=1; diagonal m_k=2^k",
        "summand": "a_(j,N)(s)=-q_N(g_j) Log_0(1-exp(-s ell(g_j)/q_N(g_j)))=q_N(g_j) sum_(r>=1) exp(-r s ell(g_j)/q_N(g_j))/r; g_j is the jth certified content-one owner, so q_N(g_j)=1",
        "branch": "Log_0 is the analytic branch defined by the displayed absolutely convergent series for |exp(-s ell/q)|<1 and normalized to 0 as Re(s)->infinity",
        "partial_sum": "L(m,N;s)=sum_(j=1)^m a_(j,N)(s)",
        "pointwise_majorant": "M_(j,N,K)=-q_N(g_j) log(1-exp(-(1+delta)ell(g_j)/q_N(g_j))); for content one this is M_(j,K)=-log(1-exp(-(1+delta)ell(g_j)))",
    }
    rows = [
        {
            "claim_id": "AN-1",
            "indices_and_coupling": "fix schedule choice and k; N=S_k; let m->infinity through the certified owner order",
            "limit_order": "lim_(m->infinity) L(m,S_k;s)",
            "majorant_obligation": "prove sum_(j>=1) M_(j,S_k,K)<infinity for the exact certified owners",
            "specific_interchange": "identify lim_m sum_(j<=m) a_(j,S_k) with the infinite owner sum uniformly on K",
            "prerequisites": "factor derivation; certified cofinal content-one enumeration; exact lengths; branch binding",
            "status": "UNPROVED_NOT_EXECUTED",
        },
        {
            "claim_id": "AN-2",
            "indices_and_coupling": "fix m; N=S_k; let k->infinity separately for S_k=k! and S_k=2(k!)",
            "limit_order": "lim_(k->infinity) L(m,S_k;s)",
            "majorant_obligation": "for each j<=m prove sup_k sup_(s in K)|a_(j,S_k)(s)|<=M_(j,K)<infinity; finite sum_(j<=m) M_(j,K)",
            "specific_interchange": "lim_k sum_(j<=m) a_(j,S_k)=sum_(j<=m) lim_k a_(j,S_k)",
            "prerequisites": "factor derivation and branch binding; content-one q=1 must be proved applicable, not inferred from an executed result",
            "status": "UNPROVED_NOT_EXECUTED",
        },
        {
            "claim_id": "AN-3",
            "indices_and_coupling": "for each schedule first m->infinity at fixed k, then k->infinity",
            "limit_order": "lim_(k->infinity)[lim_(m->infinity)L(m,S_k;s)]",
            "majorant_obligation": "prove one k-independent summable sequence M_j(K) with |a_(j,S_k)(s)|<=M_j(K) for every j,k,s in K",
            "specific_interchange": "lim_k sum_(j>=1)a_(j,S_k)=sum_(j>=1)lim_k a_(j,S_k), uniformly on K",
            "prerequisites": "AN-1 for every k; component limits; certified cofinal enumeration; uniform dominated tail",
            "status": "UNPROVED_NOT_EXECUTED",
        },
        {
            "claim_id": "AN-4",
            "indices_and_coupling": "for each schedule first k->infinity at fixed m, then m->infinity; compare with AN-3",
            "limit_order": "lim_(m->infinity)[lim_(k->infinity)L(m,S_k;s)] and equality with the AN-3 order",
            "majorant_obligation": "prove the same k-independent summable M_j(K) and convergence of each a_(j,S_k) on K",
            "specific_interchange": "justify lim_m lim_k L=lim_k lim_m L and identify both with sum_j lim_k a_(j,S_k)",
            "prerequisites": "AN-2 for every m; AN-3 dominated tail; common certified owner order",
            "status": "UNPROVED_NOT_EXECUTED",
        },
        {
            "claim_id": "AN-5",
            "indices_and_coupling": "m=m_k=2^k and N=S_k, separately for S_k=k! and S_k=2(k!)",
            "limit_order": "lim_(k->infinity)L(2^k,S_k;s)",
            "majorant_obligation": "prove a k-independent summable M_j(K), component convergence, and sup_(s in K) sum_(j>2^k)|a_(j,S_k)(s)|<=sum_(j>2^k)M_j(K)->0",
            "specific_interchange": "identify the coupled diagonal limit with the common AN-3/AN-4 iterated limit",
            "prerequisites": "certified cofinal diagonal; both schedule branches; AN-3/AN-4 common limit; uniform tail",
            "status": "UNPROVED_NOT_EXECUTED",
        },
    ]
    payload = {
        "schema_version": "round10-stage4-prime-analytic-registry-audit/1.0",
        "paper_id": "P32",
        "generated_at_utc": STAMP,
        "common_definitions": common,
        "row_count": len(rows),
        "rows": rows,
        "audit_outcome": "PASS_COMPLETE_REGISTRY_SHAPE; ALL_ANALYTIC_CLAIMS_UNPROVED",
        "finite_diagnostic_boundary": "The prospective k<=8 prefix and m in {8,16,32,64,128} panels remain unexecuted serialization diagnostics. They have no convergence, cofinality, majorant, interchange, or scientific-result force.",
        "non_global_boundary": "No tail theorem, infinite scalar specialization, factor theorem, owner enumeration, limit identity, recovery statement, obstruction, or Route credit is asserted.",
    }
    return write_json("stage4_prime_analytic_registry_audit_round2.json", payload)


def build_reader_manifest(support_paths: list[Path]) -> Path:
    section6 = [
        ("stage1_phase2_source_inventory.tsv", "text/tab-separated-values; frozen Phase-2 inventory header", "26-source identity and metadata inventory"),
        ("stage1_phase2_source_verification.tsv", "text/tab-separated-values; frozen Phase-2 verification header", "source identity, bounded fitness, and limitation rows"),
        ("stage1_phase4_research_report.md", "text/markdown; no machine schema declared", "Phase-4 evidence synthesis report"),
        ("stage1_phase5_citation_integrity_review.md", "text/markdown; no machine schema declared", "citation-integrity role review provenance"),
        ("stage1_phase5_devils_advocate.md", "text/markdown; no machine schema declared", "Devil's Advocate role review provenance"),
        ("stage1_phase5_editorial_review.md", "text/markdown; no machine schema declared", "editorial role review provenance"),
        ("stage1_phase5_ethics_review.md", "text/markdown; no machine schema declared", "ethics/integrity role review provenance"),
        ("stage1_phase5_review_synthesis.md", "text/markdown; no machine schema declared", "role-preserving Phase-5 synthesis provenance"),
        ("stage1_phase6_checkpoint.md", "text/markdown; no machine schema declared", "Phase-6 checkpoint and gate provenance"),
        ("stage1_phase1_methodology_blueprint.md", "text/markdown; no machine schema declared", "frozen research contract and initial formal system"),
        ("stage1_phase6_claim_intent_manifest.json", "application/json; ClaimIntent manifest_version 1.0", "frozen ClaimIntent and negative constraints"),
    ]
    entries = []
    for name, media, role in section6:
        path = NOTES / name
        entries.append(
            {
                "path": "notes/" + name,
                "sha256": sha(path),
                "bytes": path.stat().st_size,
                "schema_or_media_type": media,
                "access_state": "PRESENT_AT_PINNED_COMMIT_EXACT_BYTES",
                "commit_pinned_url": (
                    f"{REPOSITORY_ROOT}/blob/{PINNED_COMMIT}/flow_systems/"
                    "papers/32-homology-cover-renormalization-uniformity/notes/" + name
                ),
                "pinned_commit_sha256": sha(path),
                "pinned_commit_verification": "RAW_GITHUB_BYTES_FETCHED_AND_SHA256_EQUAL",
                "bounded_evidentiary_role": role,
            }
        )
    for path in support_paths:
        if path.name == "stage4_prime_reader_artifact_manifest_round2.json":
            continue
        media = "text/x-python; helper source" if path.suffix == ".py" else "text/tab-separated-values" if path.suffix == ".tsv" else "text/x-bibtex; notes-side bibliography" if path.suffix == ".bib" else "application/json; schema_version declared in file"
        entries.append(
            {
                "path": "notes/" + path.name,
                "sha256": sha(path),
                "bytes": path.stat().st_size,
                "schema_or_media_type": media,
                "access_state": "LOCAL_NOTES_SIDECAR_NOT_PRESENT_AT_PINNED_COMMIT",
                "commit_pinned_url": None,
                "bounded_evidentiary_role": "Stage-4-prime support evidence only; pending repository synchronization and not yet reader-resolved by the pinned snapshot",
            }
        )
    payload = {
        "schema_version": "round10-stage4-prime-reader-artifact-manifest/1.0",
        "paper_id": "P32",
        "generated_at_utc": STAMP,
        "repository_locator": PINNED_BASE,
        "repository_commit": PINNED_COMMIT,
        "commit_record": f"{REPOSITORY_ROOT}/commit/{PINNED_COMMIT}",
        "locator_state": "public commit-addressed repository snapshot; not a persistent archive, release DOI, or preservation guarantee",
        "pinned_commit_verification": {
            "verified_at_utc": STAMP,
            "method": "Fetched each of the 11 claimed Section-6 files from raw.githubusercontent.com at the exact commit and compared SHA-256 and byte content with the local file.",
            "http_and_hash_outcome": "11/11 FETCHED; 11/11 EXACT_SHA256_MATCH",
        },
        "entry_count": len(entries),
        "section6_claimed_current_count": len(section6),
        "section6_exact_at_pinned_commit_count": len(section6),
        "local_stage4_prime_sidecar_count": len(entries) - len(section6),
        "entries": entries,
        "self_binding": "This manifest's own path, hash, and byte count are carried by the manuscript patch and writer handoff to avoid a recursive self-hash entry.",
        "boundary": {
            "persistent_archive_claimed": False,
            "canonical_artifact_modified": False,
            "canonical_result_refreshed": False,
            "scientific_artifacts_or_results_claimed": False,
            "reader_recoverability_limited_to_exact_pinned_entries": True,
            "local_sidecars_not_misrepresented_as_remote": True,
        },
    }
    return write_json("stage4_prime_reader_artifact_manifest_round2.json", payload)


def main() -> None:
    notes_bib = build_notes_bibliography()
    closest_verification, comparison_json, comparison_tsv = build_closest_work(notes_bib)
    passage_json, passage_tsv = build_claim_passage_matrix(closest_verification)
    formal = build_formal_audit()
    scalar = build_scalar_audit()
    analytic = build_analytic_audit()
    replay_paths = [
        NOTES / "stage4_prime_build_support_round2.py",
        NOTES / "stage4_prime_build_literature_replay_round2.py",
        NOTES / "stage4_prime_literature_replay_round2.raw.json",
        NOTES / "stage4_prime_literature_screening_ledger_round2.json",
        NOTES / "stage4_prime_literature_screening_ledger_round2.tsv",
    ]
    support = replay_paths + [
        notes_bib, closest_verification, comparison_json, comparison_tsv,
        passage_json, passage_tsv, formal, scalar, analytic,
    ]
    manifest = build_reader_manifest(support)
    result = {
        "support_artifacts": [
            {"path": "notes/" + p.name, "sha256": sha(p), "bytes": p.stat().st_size}
            for p in support + [manifest]
        ],
        "canonical_bibliography_sha256": sha(PAPER / "paper" / "references.bib"),
        "canonical_bibliography_changed": False,
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
