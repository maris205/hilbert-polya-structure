"""P211 B: histogram paths, whole-map powers and a kernel-first inverse.

SOURCE ONLY until root accepts this exact source/parameter/schema capsule
and supplies a role-specific initial binding. No author/A/pilot imports.
The only file read is the explicitly supplied parameter document. No file
is written; an actual authorized main invocation emits one complete JSON.
"""

import itertools
import json
import math
import sys


EXPECTED_PARAMETERS = {
    "schema": "p211-b-parameters-v1",
    "n_values": [1, 2, 3, 4, 5, 6, 7],
    "carrier_sizes": [1, 3, 10, 35, 126, 462, 1716],
    "expected_total_states": 2353,
    "carrier": "all_nondecreasing_maps_[n]_to_[n]_without_initial_restrictions",
    "representation": "weak_composition_histograms_and_stars_bars_paths",
    "graph_method": "whole_carrier_successive_composition_tables_full_carrier_guard",
    "inverse_method": "kernel_first_last_kernel_cut_then_global_fixed_size_image_subsets",
    "output_schema": "p211-b-complete-path-certificate-v1",
    "ordering": "n_ascending_histogram_lexicographic_ids_kernel_masks_ascending_sources_by_id",
    "serialization": "JSON_sort_keys_ensure_ascii_compact_allow_nan_false_plus_single_LF",
    "predicate_categories": [
        "B01_carrier_and_encoding",
        "B02_literal_histogram_update",
        "B03_support_identity_and_normalization",
        "B04_composition_certificate",
        "B05_fixed_recurrent_terminal",
        "B06_pointwise_clock",
        "B07_boundary_lifetimes",
        "B08_image_iff_and_witness",
        "B09_kernel_first_decoder",
        "B10_rank_branch_binomial_counts",
        "B11_laurent_identity_and_total_mass",
        "B12_sharp_parity_and_boundaries",
    ],
    "excluded_claims": [
        "global_fibre_maximum_or_maximizers",
        "basin_cardinality_formulas",
        "all_time_inverse_formulas",
        "global_priority_or_no_factor_no_lift_theorems",
    ],
}


def insist(condition, detail):
    if not condition:
        raise AssertionError(detail)


def exact_document(actual, expected):
    if type(actual) is not type(expected):
        return False
    if type(expected) is dict:
        return (actual.keys() == expected.keys()
                and all(exact_document(actual[key], expected[key]) for key in expected))
    if type(expected) is list:
        return (len(actual) == len(expected)
                and all(exact_document(a, b) for a, b in zip(actual, expected)))
    return actual == expected


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        insist(key not in result, ("duplicate_parameter_key", key))
        result[key] = value
    return result


def reject_nonfinite(token):
    raise ValueError("non-finite JSON token: " + token)


def read_parameters():
    insist(len(sys.argv) == 3 and sys.argv[1] == "--parameters",
           "verify.py --parameters ABSOLUTE_PARAMETERS")
    insist(sys.argv[0].startswith("/") and sys.argv[2].startswith("/"),
           "absolute scientific argv is required")
    insist(sys.flags.isolated == 1 and sys.flags.no_site == 1
           and sys.flags.dont_write_bytecode == 1 and sys.flags.optimize == 0,
           "source-only isolated unoptimized interpreter required")
    with open(sys.argv[2], "r", encoding="utf-8") as stream:
        parameters = json.load(stream, object_pairs_hook=unique_object,
                               parse_constant=reject_nonfinite)
    insist(exact_document(parameters, EXPECTED_PARAMETERS),
           "parameters differ in key, type, order or value from approved specification")
    return parameters


def mask_sites(mask, n):
    return [site for site in range(1, n + 1) if mask & (1 << (site - 1))]


def sites_mask(sites):
    result = 0
    for site in sites:
        result |= 1 << (site - 1)
    return result


def all_histograms(n):
    """Choose n-1 bars among 2n-1 positions; the remaining n are stars."""
    result = []
    for bars in itertools.combinations(range(2 * n - 1), n - 1):
        boundaries = (-1,) + bars + (2 * n - 1,)
        histogram = tuple(boundaries[j + 1] - boundaries[j] - 1 for j in range(n))
        result.append(histogram)
    return result


def path_word(histogram):
    return "|".join("*" * count for count in histogram)


def histogram_from_word(word):
    return tuple(len(segment) for segment in word.split("|"))


def whole_values(histogram):
    return [label for label, count in enumerate(histogram, 1) for _ in range(count)]


def support_masks(histogram):
    cuts = occupied = cumulative = 0
    for label, count in enumerate(histogram, 1):
        cumulative += count
        if count:
            cuts |= 1 << (cumulative - 1)
            occupied |= 1 << (label - 1)
    return cuts, occupied


def histogram_from_masks(kernel, image, n):
    insist(kernel & (1 << (n - 1)), "kernel mask is missing the top cut")
    ends, values = mask_sites(kernel, n), mask_sites(image, n)
    insist(len(ends) == len(values) > 0, "unequal or empty support ranks")
    histogram = [0] * n
    previous = 0
    for rank in range(len(ends)):
        histogram[values[rank] - 1] = ends[rank] - previous
        previous = ends[rank]
    return tuple(histogram)


def retraction_product_histogram(outer_mask, inner_mask, n):
    """Push lengths of inner-ceiling blocks into the first outer cut above them."""
    top = 1 << (n - 1)
    insist(outer_mask & top and inner_mask & top, "both retractions need the top")
    histogram = [0] * n
    cells = []
    previous = 0
    for block_end in mask_sites(inner_mask, n):
        suffix = outer_mask >> (block_end - 1)
        insist(suffix > 0, "uncovered retraction block")
        output = block_end + (suffix & -suffix).bit_length() - 1
        width = block_end - previous
        histogram[output - 1] += width
        cells.append({"inner_block_end": block_end, "block_width": width,
                      "outer_suffix_mask": suffix, "assigned_output": output})
        previous = block_end
    return tuple(histogram), cells


def literal_histogram_step(histogram):
    n = len(histogram)
    kernel, image = support_masks(histogram)
    return retraction_product_histogram(kernel, image | (1 << (n - 1)), n)


def boundary_language(histogram):
    """Ignore empty sites and recognize successive (K V)* B boundary words."""
    n = len(histogram)
    kernel, image = support_masks(histogram)
    if not image & (1 << (n - 1)):
        return None
    phase = 0
    strict_sites = []
    intervals = []
    for site in range(1, n + 1):
        bit = 1 << (site - 1)
        letter = (1 if kernel & bit else 0) + (2 if image & bit else 0)
        if letter == 0:
            continue
        if letter == 3:
            if phase != 0:
                return None
            size = len(strict_sites)
            tokens = [{"site": point, "initial_role": "K" if rank % 2 == 0 else "V",
                       "death_epoch": min(rank + 1, size - rank)}
                      for rank, point in enumerate(strict_sites)]
            intervals.append({"anchor": site, "tokens": tokens})
            strict_sites = []
        elif letter == 1 and phase == 0:
            strict_sites.append(site)
            phase = 1
        elif letter == 2 and phase == 1:
            strict_sites.append(site)
            phase = 0
        else:
            return None
    if phase != 0 or strict_sites or not intervals or intervals[-1]["anchor"] != n:
        return None
    radius = max((token["death_epoch"] for interval in intervals
                  for token in interval["tokens"]), default=0)
    return {"anchor_mask": kernel & image, "intervals": intervals, "radius": radius}


def surviving_masks(boundary, epoch):
    kernel = image = boundary["anchor_mask"]
    for interval in boundary["intervals"]:
        for token in interval["tokens"]:
            if epoch < token["death_epoch"]:
                is_kernel = (token["initial_role"] == "K") != bool(epoch % 2)
                if is_kernel:
                    kernel |= 1 << (token["site"] - 1)
                else:
                    image |= 1 << (token["site"] - 1)
    return kernel, image


def composition_certificate(arrows):
    """No clock formula or per-orbit cycle traversal determines these tables."""
    size = len(arrows)
    tables = [list(range(size))]
    times = [None] * size
    terminals = [None] * size
    for epoch in range(size):
        previous = tables[-1]
        following = [arrows[vertex] for vertex in previous]
        for source in range(size):
            if times[source] is None and following[source] == previous[source]:
                times[source] = epoch
                terminals[source] = previous[source]
        tables.append(following)
        if all(time is not None for time in times):
            break
    insist(all(time is not None for time in times),
           "full-carrier composition guard found a source with no fixed entrance")
    return tables, times, terminals


def subsets_of_mask(mask):
    choices = [0]
    submask = mask
    while submask:
        choices.append(submask)
        submask = (submask - 1) & mask
    return sorted(choices)


def binomial_or_zero(total, chosen):
    return math.comb(total, chosen) if 0 <= chosen <= total else 0


def kernel_first_atlas(target):
    """Target only: no successor table, actual fibre or source scan is consulted."""
    boundary = boundary_language(target)
    if boundary is None:
        return None
    n = len(target)
    target_kernel, target_image = support_masks(target)
    ends, outputs = mask_sites(target_kernel, n), mask_sites(target_image, n)
    gaps = []
    previous_output = 0
    free_mask = 0
    for rank in range(len(ends)):
        sites = list(range(previous_output + 1, ends[rank]))
        gap_mask = sites_mask(sites)
        gaps.append({"previous_output": previous_output, "target_end": ends[rank],
                     "target_output": outputs[rank], "sites": sites, "mask": gap_mask})
        free_mask |= gap_mask
        previous_output = outputs[rank]
    options = []
    descriptions = []
    branch_counts = [0, 0]
    for extra_kernel in subsets_of_mask(free_mask):
        rightmost = []
        eligible_mask = 0
        for gap in gaps:
            selected = extra_kernel & gap["mask"]
            last_cut = selected.bit_length() if selected else gap["previous_output"]
            rightmost.append(last_cut)
            eligible_mask |= gap["mask"] & ~((1 << last_cut) - 1)
        kernel_count = extra_kernel.bit_count()
        eligible = mask_sites(eligible_mask, n)
        option_counts = [binomial_or_zero(len(eligible), kernel_count + branch)
                         for branch in (0, 1)]
        branch_counts = [branch_counts[j] + option_counts[j] for j in (0, 1)]
        options.append({"extra_kernel_mask": extra_kernel,
                        "rightmost_kernel_by_gap": rightmost,
                        "eligible_image_mask": eligible_mask,
                        "kernel_extra_count": kernel_count,
                        "eligible_image_count": len(eligible),
                        "branch_binomial_counts": option_counts})
        source_kernel = target_image | extra_kernel
        for branch in (0, 1):
            chosen_size = kernel_count + branch
            if chosen_size > len(eligible):
                continue
            for selected_image in itertools.combinations(eligible, chosen_size):
                extra_image = sites_mask(selected_image)
                completed_image = target_kernel | extra_image
                source_image = (completed_image if branch == 0
                                else completed_image & ~(1 << (n - 1)))
                source = histogram_from_masks(source_kernel, source_image, n)
                descriptions.append({"source_histogram": list(source),
                                     "source_kernel_mask": source_kernel,
                                     "source_image_mask": source_image,
                                     "completed_image_mask": completed_image,
                                     "extra_kernel_mask": extra_kernel,
                                     "extra_image_mask": extra_image,
                                     "balance": branch})
    return {"gaps": gaps, "free_mask": free_mask, "kernel_options": options,
            "branch_counts": branch_counts, "count": sum(branch_counts),
            "descriptions": descriptions}


def independent_laurent(gaps):
    """Coefficient parity sums, not selected-site splits or ternary-word counts."""
    factors = []
    product = {0: 1}
    for gap in gaps:
        length = len(gap["sites"])
        factor = {exponent: sum(math.comb(length, selected)
                               for selected in range(abs(exponent), length + 1, 2))
                  for exponent in range(-length, length + 1)}
        factors.append([[exponent, count] for exponent, count in sorted(factor.items())])
        updated = {}
        for exponent, count in product.items():
            for shift, multiplicity in factor.items():
                updated[exponent + shift] = updated.get(exponent + shift, 0) + count * multiplicity
        product = updated
    return {"gap_factors": factors,
            "product": [[exponent, count] for exponent, count in sorted(product.items())],
            "branch_counts": [product.get(0, 0), product.get(1, 0)],
            "count": product.get(0, 0) + product.get(1, 0)}


def analyse_histogram_carrier(n, declared_size, categories):
    counts = {category: 0 for category in categories}

    def check(category_number, condition, detail):
        name = categories[category_number - 1]
        insist(condition, {"predicate": name, "n": n, "detail": detail})
        counts[name] += 1

    histograms = all_histograms(n)
    ids = {histogram: number for number, histogram in enumerate(histograms)}
    check(1, histograms == sorted(set(histograms))
          and len(histograms) == declared_size == math.comb(2 * n - 1, n - 1),
          "complete weak-composition census and ordering")
    arrows, literal_cells = [], []
    incoming = [[] for _ in histograms]
    boundaries = [boundary_language(histogram) for histogram in histograms]
    for number, histogram in enumerate(histograms):
        word = path_word(histogram)
        check(1, len(histogram) == n and all(type(x) is int and x >= 0 for x in histogram)
              and sum(histogram) == n and word.count("*") == n
              and word.count("|") == n - 1 and histogram_from_word(word) == histogram,
              number)
        successor, cells = literal_histogram_step(histogram)
        check(2, successor in ids and sum(cell["block_width"] for cell in cells) == n,
              number)
        arrows.append(ids[successor])
        literal_cells.append(cells)
        incoming[ids[successor]].append(number)
    tables, times, terminals = composition_certificate(arrows)
    check(4, tables[0] == list(range(len(histograms))) and tables[1] == arrows
          and tables[-1] == tables[-2], "identity, literal edge table and stable full power")
    for epoch in range(1, len(tables)):
        check(4, tables[epoch] == [arrows[vertex] for vertex in tables[epoch - 1]], epoch)
    fixed_ids = [number for number, target in enumerate(arrows) if target == number]
    expected_fixed = sorted(ids[histogram_from_masks(mask | (1 << (n - 1)),
                                                   mask | (1 << (n - 1)), n)]
                            for mask in range(1 << (n - 1)))
    check(5, fixed_ids == expected_fixed and len(fixed_ids) == 2 ** (n - 1),
          "complete fixed set; stable full power excludes every nonfixed cycle")
    records = []
    for number, histogram in enumerate(histograms):
        kernel, image = support_masks(histogram)
        completed = image | (1 << (n - 1))
        successor = histograms[arrows[number]]
        next_kernel, next_image = support_masks(successor)
        check(1, histogram_from_masks(kernel, image, n) == histogram, number)
        check(3, (next_kernel & ~completed) == 0 and (next_image & ~kernel) == 0
              and (next_kernel & next_image) == (kernel & completed), number)
        check(3, boundaries[arrows[number]] is not None and successor[-1] > 0
              and all(value >= place for place, value in enumerate(whole_values(successor), 1)),
              number)
        first_equalities = [epoch for epoch in range(len(tables) - 1)
                            if tables[epoch][number] == tables[epoch + 1][number]]
        check(4, first_equalities and times[number] == first_equalities[0]
              and all(tables[epoch][number] == terminals[number]
                      for epoch in range(times[number], len(tables))), number)
        terminal_mask = kernel & completed
        predicted_terminal = ids[histogram_from_masks(terminal_mask, terminal_mask, n)]
        check(5, terminals[number] == predicted_terminal
              and terminals[number] in fixed_ids
              and ((arrows[number] == number) == (kernel == image)), number)
        predicted_time = 0 if kernel == image else 1 + boundaries[arrows[number]]["radius"]
        check(6, times[number] == predicted_time, number)
        boundary = boundaries[number]
        check(8, bool(incoming[number]) == (boundary is not None), number)
        survival = None
        atlas = None
        laurent = None
        if boundary is not None:
            check(6, times[number] == boundary["radius"], number)
            survival = []
            for epoch in range(boundary["radius"] + 2):
                predicted_kernel, predicted_image = surviving_masks(boundary, epoch)
                predicted_histogram = histogram_from_masks(predicted_kernel, predicted_image, n)
                predicted_id = ids[predicted_histogram]
                check(7, epoch < len(tables) and predicted_id == tables[epoch][number],
                      {"source_id": number, "epoch": epoch})
                survival.append({"epoch": epoch, "kernel_mask": predicted_kernel,
                                 "image_mask": predicted_image, "state_id": predicted_id})
            transpose_histogram = histogram_from_masks(image, kernel, n)
            check(8, arrows[ids[transpose_histogram]] == number, number)
            atlas = kernel_first_atlas(histogram)
            for description in atlas["descriptions"]:
                decoded = tuple(description["source_histogram"])
                check(9, decoded in ids, {"target_id": number, "description": description})
                description["source_id"] = ids[decoded]
                decoded_kernel, decoded_image = support_masks(decoded)
                check(9, decoded_kernel == description["source_kernel_mask"]
                      and decoded_image == description["source_image_mask"]
                      and (decoded_image | (1 << (n - 1))) == description["completed_image_mask"]
                      and description["completed_image_mask"].bit_count()
                      - decoded_kernel.bit_count() == description["balance"],
                      {"target_id": number, "source_id": ids[decoded]})
            atlas["descriptions"].sort(key=lambda item: item["source_id"])
            decoded_ids = [item["source_id"] for item in atlas["descriptions"]]
            check(9, len(decoded_ids) == len(set(decoded_ids))
                  and decoded_ids == incoming[number], number)
            decoded_branches = [sum(item["balance"] == branch for item in atlas["descriptions"])
                                for branch in (0, 1)]
            check(10, decoded_branches == atlas["branch_counts"]
                  and sum(decoded_branches) == atlas["count"], number)
            for option in atlas["kernel_options"]:
                actual_branches = [sum(item["balance"] == branch
                                       and item["extra_kernel_mask"] == option["extra_kernel_mask"]
                                       for item in atlas["descriptions"])
                                   for branch in (0, 1)]
                check(10, actual_branches == option["branch_binomial_counts"],
                      {"target_id": number, "extra_kernel_mask": option["extra_kernel_mask"]})
            laurent = independent_laurent(atlas["gaps"])
            check(11, laurent["branch_counts"] == atlas["branch_counts"]
                  and laurent["count"] == len(incoming[number]), number)
        else:
            check(9, incoming[number] == [] and kernel_first_atlas(histogram) is None, number)
        records.append({"id": number, "histogram": list(histogram), "path_word": path_word(histogram),
                        "whole_values": whole_values(histogram), "kernel_mask": kernel,
                        "image_mask": image, "completed_image_mask": completed,
                        "literal_block_cells": literal_cells[number], "successor_id": arrows[number],
                        "predecessor_ids": incoming[number], "fixed": arrows[number] == number,
                        "recurrent": arrows[number] == number,
                        "first_fixed_epoch": times[number], "terminal_id": terminals[number],
                        "predicted_terminal_id": predicted_terminal, "predicted_time": predicted_time,
                        "image_criterion": boundary is not None, "boundary_lifetimes": boundary,
                        "survival_certificate": survival, "kernel_first_atlas": atlas,
                        "laurent_certificate": laurent, "fibre_count": len(incoming[number])})
    height = max(times)
    expected_height = 0 if n == 1 else (n + 1) // 2
    witness = tuple(1 if label == n and n % 2 else 2 if label % 2 and label < n else 0
                    for label in range(1, n + 1))
    witness_id = ids[witness]
    check(12, height == expected_height and times[witness_id] == height
          and len(tables) == height + 2, "sharp histogram parity witness")
    if n > 1:
        check(12, whole_values(witness)[0] == 1
              and whole_values(histograms[arrows[witness_id]])[0] == 2,
              "witness has a genuine first normalization step")
    inverse_mass = sum(record["fibre_count"] for record in records)
    formula_mass = sum(0 if record["kernel_first_atlas"] is None
                       else record["kernel_first_atlas"]["count"] for record in records)
    check(11, inverse_mass == formula_mass == len(histograms), "all targets including zero fibres")
    return {"n": n, "state_count": len(histograms), "records": records,
            "successor_table": arrows, "composition_tables": tables,
            "first_fixed_epochs": times, "terminal_table": terminals,
            "fixed_ids": fixed_ids, "recurrent_ids": list(fixed_ids),
            "image_ids": [number for number, predecessors in enumerate(incoming) if predecessors],
            "zero_fibre_ids": [number for number, predecessors in enumerate(incoming) if not predecessors],
            "height": height, "height_formula": expected_height, "sharp_witness_id": witness_id,
            "inverse_mass": inverse_mass, "kernel_first_mass": formula_mass,
            "check_counts": counts, "check_total": sum(counts.values())}


def hand_boundary_attacks(carriers):
    by_n = {carrier["n"]: carrier for carrier in carriers}
    records = {n: {tuple(row["histogram"]): row for row in carrier["records"]}
               for n, carrier in by_n.items()}
    source = (2, 0, 1)
    kernel, image = support_masks(source)
    forward, _ = retraction_product_histogram(kernel, image | 4, 3)
    reversed_product, _ = retraction_product_histogram(image | 4, kernel, 3)
    insist(forward == (0, 1, 2) and reversed_product == (0, 0, 3)
           and records[3][source]["first_fixed_epoch"] == 2,
           "orientation and initial-time hand attack failed")
    nonimage = records[4][(0, 1, 1, 2)]
    insist(nonimage["whole_values"] == [2, 3, 4, 4]
           and all(value >= place for place, value in enumerate(nonimage["whole_values"], 1))
           and not nonimage["image_criterion"] and nonimage["fibre_count"] == 0,
           "extensive top-fixing nonimage hand attack failed")
    constant = records[3][(0, 0, 3)]
    decoded = [item["source_histogram"] for item in constant["kernel_first_atlas"]["descriptions"]]
    insist(decoded == [[0, 0, 3], [0, 1, 2], [0, 3, 0], [3, 0, 0]]
           and constant["kernel_first_atlas"]["branch_counts"] == [2, 2],
           "constant-three target hand inverse attack failed")
    return [
        {"name": "right_factor_first_and_initial_time", "n": 3,
         "source_histogram": list(source), "forward_histogram": list(forward),
         "reversed_product_histogram": list(reversed_product), "full_time": 2},
        {"name": "extensive_top_fixing_is_not_image_iff", "n": 4,
         "target_histogram": [0, 1, 1, 2], "fibre_count": 0},
        {"name": "constant_three_rank_branches", "n": 3,
         "target_histogram": [0, 0, 3], "predecessor_histograms": decoded,
         "branch_counts": [2, 2]},
    ]


def main():
    parameters = read_parameters()
    categories = parameters["predicate_categories"]
    carriers = [analyse_histogram_carrier(n, size, categories)
                for n, size in zip(parameters["n_values"], parameters["carrier_sizes"])]
    total = sum(carrier["state_count"] for carrier in carriers)
    insist(total == parameters["expected_total_states"], "wrong complete state/target census")
    attacks = hand_boundary_attacks(carriers)
    check_counts = {name: sum(carrier["check_counts"][name] for carrier in carriers)
                    for name in categories}
    transcript = {
        "schema": parameters["output_schema"], "role": "P211_REVIEW_B",
        "parameters": parameters, "carrier_count": len(carriers), "carriers": carriers,
        "total_states": total, "total_targets": total, "total_edges": total,
        "check_counts": check_counts, "carrier_check_total": sum(check_counts.values()),
        "hand_attack_checks": len(attacks), "hand_boundary_attacks": attacks,
        "check_total": sum(check_counts.values()) + len(attacks),
        "status": "FINITE_COMPLETE_PATH_CHECKS_PASS",
        "scope": "original n=1..7 counterexample pressure; not all-n proof or manuscript acceptance",
    }
    sys.stdout.write(json.dumps(transcript, sort_keys=True, ensure_ascii=True,
                               separators=(",", ":"), allow_nan=False) + "\n")


if __name__ == "__main__":
    main()
