# Results

Selected exact census rows:

| n | all primitive | reversible | edge--edge | vertex--vertex |
|---:|---:|---:|---:|---:|
| 7 | 4 | 4 | -- | -- |
| 8 | 5 | 3 | 2 | 1 |
| 12 | 25 | 11 | 6 | 5 |
| 16 | 135 | 37 | 20 | 17 |
| 20 | 750 | 102 | 55 | 47 |

The exact formulas are emitted through period 32.  Direct primitive-necklace
enumeration agrees through period 16; an implementation-independent Cartesian
enumerator agrees through period 12.

The asymptotic theorem is

```text
full primitive entropy       = log(phi)
reflection primitive entropy = (1/2) log(phi)
reflection density           = O(n phi^(-n/2))
```
