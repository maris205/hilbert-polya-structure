#!/usr/bin/env python3
"""Post-pilot AMC theorem audit consuming fixed complete output; not a new map pilot."""
from collections import Counter
from hashlib import sha256
from math import comb, factorial
from pathlib import Path
import json
import sys

CHECKS = Counter()


def need(condition, section):
    CHECKS[section] += 1
    if not condition:
        raise AssertionError(section)


def matching_family(rows, columns):
    result = []

    def visit(row, used, mask, pairs):
        if row == rows:
            result.append((mask, tuple(pairs)))
            return
        visit(row+1, used, mask, pairs)
        for column in range(columns):
            if column not in used:
                visit(row+1, used | {column}, mask | (1 << (row*columns+column)), pairs+[(row, column)])

    visit(0, set(), 0, [])
    return sorted(result, key=lambda entry: (-len(entry[1]), entry[0]))


def acyclic(adjacency):
    remaining = set(range(len(adjacency)))
    while remaining:
        sources = {target for target in remaining
                   if not any(target in adjacency[source] for source in remaining)}
        if not sources:
            return False
        remaining -= sources
    return True


def main():
    need(sys.flags.isolated == 1 and sys.flags.optimize == 0 and sys.flags.dont_write_bytecode == 1,
         'isolated_unoptimized_no_bytecode')
    source = Path(__file__).resolve().parent/'CANONICAL.json'
    raw = source.read_bytes()
    need(sha256(raw).hexdigest() == 'b0e7a2aee8a6afa8f9e3488647364d08638612eb06d2d86a8048ed1ea0e2dd75',
         'exact_fixed_pilot_output')
    data = json.loads(raw)
    need(data['status'] == 'PASS_FIXED_THIRTEENTH_AUTHOR_PILOT', 'actual_pilot_status')
    boxes = [box for box in data['boxes'] if box['rule'] == 'AMC']
    need(len(boxes) == 15 and sum(box['state_count'] for box in boxes) == 70515, 'same_original_AMC_boxes')
    dags = [1]
    for size in range(1, 5):
        dags.append(sum((-1)**(chosen+1)*comb(size, chosen)*2**(chosen*(size-chosen))*dags[size-chosen]
                        for chosen in range(1, size+1)))
    need(dags == [1, 1, 3, 25, 543], 'DAG_source_inclusion_exclusion_values')
    summaries = []
    source_total = 0
    for box in boxes:
        rows, columns = box['parameters']['rows'], box['parameters']['columns']
        whole = (1 << (rows*columns))-1
        arrows = box['all_forward_target_indices']
        supports = box['all_allowed_support_masks']
        ranks = box['all_maximum_matching_ranks']
        fibres = box['all_target_fibre_sizes']
        need(len(arrows) == len(supports) == len(ranks) == len(fibres) == whole+1,
             'all_original_array_lengths')
        indegrees = Counter(arrows)
        need(fibres == [indegrees[target] for target in range(whole+1)], 'complete_fibre_reconstruction_from_arrows')
        need(max(fibres) == box['maximum_fibre'] == dags[rows], 'all_target_sharp_DAG_maximum')
        family = matching_family(rows, columns)
        maximum_matches = {}
        encoded_by_support = {}
        for old, target in enumerate(arrows):
            source_total += 1
            core = whole ^ target
            need(core == supports[old] and old & core == core, 'fixed_target_complement_and_core_containment')
            need(ranks[old] == ranks[core], 'core_rank_equals_source_rank')
            if core not in maximum_matches:
                chosen, pairs = next((mask, pairs) for mask, pairs in family if core & mask == mask)
                maximum_matches[core] = chosen, pairs
                need(len(pairs) == ranks[core], 'separate_canonical_maximum_matching')
            chosen, pairs = maximum_matches[core]
            row_index = {row: i for i, (row, column) in enumerate(pairs)}
            column_index = {column: i for i, (row, column) in enumerate(pairs)}
            extra = old ^ core
            adjacency = [set() for _ in pairs]
            encoded = 0
            for bit in range(rows*columns):
                if extra >> bit & 1:
                    row, column = divmod(bit, columns)
                    need(row in row_index and column in column_index, 'every_extra_endpoint_matched')
                    left, right = row_index[row], column_index[column]
                    need(left != right, 'no_extra_matching_loop')
                    adjacency[left].add(right)
                    encoded |= 1 << (left*len(pairs)+right)
            need(acyclic(adjacency), 'all_fibre_extra_graphs_are_DAGs')
            previous = encoded_by_support.setdefault(core, set())
            need(encoded not in previous, 'complete_fibre_injection_is_injective')
            previous.add(encoded)
        maximum_targets = [target for target, size in enumerate(fibres) if size == dags[rows]]
        need(maximum_targets == box['all_maximum_fibre_target_indices'], 'every_maximizer_matches_raw_list')
        for target, size in enumerate(fibres):
            core = whole ^ target
            need(size <= dags[ranks[core]], 'all_target_rank_refined_DAG_bound')
            if rows >= 2:
                saturating_matching = ranks[core] == rows and core.bit_count() == rows
                need((size == dags[rows]) == saturating_matching, 'necessity_and_sufficiency_of_every_equality_target')
            else:
                need(size == 1 and arrows[target] == whole ^ target, 'empty_or_one_row_complement_bijection')
        if rows >= 2:
            need(len(maximum_targets) == factorial(columns)//factorial(columns-rows),
                 'all_equality_target_count')
        summaries.append({'rows': rows, 'columns': columns, 'states_audited': whole+1,
                          'maximum_fibre': dags[rows], 'maximum_target_count': len(maximum_targets),
                          'all_nonempty_fibres_injected_into_DAGs': len(encoded_by_support),
                          'observed_height_not_all_parameter_proof': box['height']})
    need(source_total == 70515, 'every_original_AMC_source_consumed_once')
    print(json.dumps({'status': 'PASS_POST_PILOT_AMC_EXTREMA_ARTIFACT_AUDIT',
                      'role': 'Author artifact-consuming theorem check, NOT new map execution or independent review.',
                      'input_bytes': len(raw), 'input_sha256': sha256(raw).hexdigest(),
                      'dag_counts_at_original_row_bounds': dags, 'boxes': summaries,
                      'box_count': len(summaries), 'original_sources_audited': source_total,
                      'assertions': sum(CHECKS.values()), 'assertions_by_section': dict(sorted(CHECKS.items())),
                      'imports_of_pilot_or_historical_code': False,
                      'map_evaluations': 0, 'new_state_boxes': 0, 'sharp_temporal_theorem_claimed': False,
                      'independent_review': False, 'external_status': 'HOLD_EXTERNAL'}, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
