# Test report — HCS-C354

All executable lanes pass under ordinary Python and explicitly refuse -O and
-OO:

- producer: PASS, canonical payload c056f6741a06aee5b2f2892e93886cdad3c9caa52ec7efef8bf895225723f15a;
- producer-independent checker: PASS, 2,334 checks;
- independent SymPy cross-check: PASS, 223 identities;
- two-isolated-directory replay: PASS, 34,819 identical bytes;
- repaired-hash hostile mutation: PASS, 48/48 rejected;
- canonical JSON, duplicate/nonfinite rejection, strict YAML raw/semantic lock:
  PASS;
- deterministic fresh LuaLaTeX, embedded/subset fonts, text and raster gates:
  PASS.

Release closure is 27 payload files plus one self-excluded manifest.
