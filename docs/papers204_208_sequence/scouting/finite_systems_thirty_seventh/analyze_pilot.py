#!/usr/bin/env python3
"""Analyze only the already retained finite-box output; no successor evaluation."""
import json
import pathlib
import sys

OWN = pathlib.Path(__file__).absolute().parent
SOURCE = OWN / 'pilot_run/stdout.raw'


def analyze():
    source = json.loads(SOURCE.read_text())
    rows = []
    for box in source['boxes']:
        p = box['prime']
        cycles = box['cycles']
        witnesses = []
        recurrent_all_distinct_squares = 0
        for cycle in cycles:
            for point in cycle['nodes']:
                if len({x * x % p for x in point}) == 3:
                    recurrent_all_distinct_squares += 1
                    if len(witnesses) < 3:
                        witnesses.append(dict(point=point, period=cycle['length']))
        rows.append(dict(prime=p, states=box['state_count'], image=box['image_size'],
                         max_depth=box['maximum_depth'], observed_max_depth_equals_p_minus_one=box['maximum_depth'] == p - 1,
                         cycle_lengths=sorted(int(k) for k in box['cycle_length_histogram']),
                         cycle_counts=box['cycle_length_histogram'], max_fibre=box['max_fibre'],
                         number_maximizing_targets=len(box['max_fibre_target_indices']),
                         recurrent_all_distinct_squares=recurrent_all_distinct_squares,
                         first_distinct_square_witnesses=witnesses))
    print(json.dumps(dict(role='analysis_of_archived_canonical_only_not_new_pilot', rows=rows,
                          total_states=source['total_states'], checks_in_original_pilot=source['checks'],
                          new_successor_evaluations=0, extra_fields=0, extrapolated_theorems=0,
                          interpretation='Four complete prime boxes do not prove an all-odd-field temporal theorem.'), sort_keys=True))


if __name__ == '__main__':
    if sys.argv[1:] == ['record']:
        sys.path.insert(0, str(OWN))
        import record
        result = record.capture('07_archived_pilot_analysis', ['python3', '-I', '-B', str(pathlib.Path(__file__).absolute())],
                                [pathlib.Path(__file__).absolute(), SOURCE])
        assert result.returncode == 0
    else:
        assert sys.argv[1:] == []
        analyze()
