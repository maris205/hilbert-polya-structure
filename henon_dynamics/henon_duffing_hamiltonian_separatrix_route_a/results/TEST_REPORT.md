# C232 test report

Final counts are filled after the release manifest run. Required gates are:

- producer and independent checker PASS;
- SymPy identities PASS;
- canonical replay PASS;
- hostile mutation PASS;
- manifest closure `28 physical = 27 payload + manifest`;
- two fresh fixed-epoch builds per revision with embedded subset fonts and
  settled warning-free logs.
