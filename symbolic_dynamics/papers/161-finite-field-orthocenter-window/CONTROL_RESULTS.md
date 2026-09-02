# Exact control results — P161 Round 0

**Status:** `PASS / HOLD_EXTERNAL`.

## Frozen command

~~~bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_p161.py
~~~

The deterministic output is frozen in `verification_output.txt`.

~~~text
P161_ORT_EXACT_V1
ORT p=3:states=433,T=432,R=144,Q=0,cycles4=0,image1=145,stable_image=1,sink_fibre=289,depths=0:1,1:288,2:144
ORT p=7:states=98785,T=98784,R=14112,Q=56448,cycles4=14112,image1=70561,stable_image=56449,sink_fibre=28225,depths=0:56449,1:28224,2:14112
BOUNDARY p=3_empty_periodic_triangle_core_height_two
INVERSE unique_reverse_window_and_sink_fibre
ASSERTIONS=1317843
STATUS=PASS
~~~

Transcript SHA-256:
`26846bfd5cb94d397605f7f4dbf19b22bb29081fe43156e8e45c5ea2839f045c`.

## Audited boxes

- Every vector in `F_p^2` for `p=3,7`: anisotropy.
- Every ordered noncollinear triangle: unique solved orthocenter, two altitude
  equations, oriented right-angle class, literal successor, and fixed-point
  status.
- Every nonright target: four distinct windows and exact fourth return.
- Every right target: direct depth and orientation transition.
- Every triangle target: literal indegree, forced reverse candidate, and
  validity iff it is nonright or right at coordinate three.
- Full carrier: sink fibre, fibre mass, depth histogram, one-step image,
  second image, and third-image stability.
- Boundary `p=3`: empty periodic triangle core, singleton stable image, and
  nonempty depth-two shell.

The script uses only Python integer arithmetic, no random seed, network call,
floating point, or third-party package.  Enumeration is finite falsification
pressure, not an all-prime proof or a source, novelty, priority, or release
certificate.
