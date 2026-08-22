# Test report

The release gate runs the following commands from the package directory:

```text
producer                 PASS
independent checker      PASS
SymPy cross-check        PASS
canonical replay         PASS
hostile mutation         PASS (12/12)
```

The final manifest records the exact evidence and PDF hashes. The PDF is
compiled twice under a fixed timestamp and checked for embedded fonts and
layout/reference warnings.
