# Test report

Command:

    bash code/run_c51.sh

Result:

    producer: PASS
    independent checker: PASS
    unit/adversarial tests: 10/10 PASS

The independent checker does not import the producer.  It recomputes the
adjacency traces, pressure threshold, fixed-algebra rank, period-four packet
sentinels, boundary growth, and claim-ceiling controls.
