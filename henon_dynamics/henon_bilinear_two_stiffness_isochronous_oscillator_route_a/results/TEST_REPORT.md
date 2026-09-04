# Test report — HCS-C357

All executable lanes pass under ordinary Python and explicitly refuse -O and
-OO:

- producer: PASS, canonical payload 1e0139204f638da12936b7198912a8bbf528494d78e9383df735d06ced78481c;
- producer-independent checker: PASS, 8,125 checks;
- independent SymPy cross-check: PASS, 490 identities;
- two-isolated-directory replay: PASS, 90,025 identical bytes;
- repaired-hash hostile mutation: PASS, 54/54 rejected;
- canonical JSON, duplicate/nonfinite rejection, strict YAML raw/semantic lock:
  PASS;
- deterministic fresh LuaLaTeX, embedded/subset fonts, text and raster gates:
  PASS.

Release closure is 27 payload files plus one self-excluded manifest.
