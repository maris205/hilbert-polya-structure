# Test report

Commands and expected release status:

```text
python3 code/c127_uniform_horseshoe_producer.py  PASS
python3 code/c127_uniform_horseshoe_checker.py   PASS
python3 code/c127_sympy_crosscheck.py            PASS
python3 code/c127_replay.py                      PASS
python3 code/c127_mutation.py                    PASS (16/16 rejected)
```

The producer uses exact `Fraction` arithmetic.  The independent checker does
not import the producer and now reconstructs every displayed sample coordinate,
closure, and strip itinerary.  SymPy separately reconstructs 121 identities.
