# Route A — Round-2 hostile review report for P187–P191

round2_status=PASS
papers=5
review_replays=5
review_b_assertions=3372593
open_findings=critical:0,major:0,minor:0
external_status=OWNER_AMBER/HOLD_EXTERNAL
P187_review_b_assertions=219556
P188_review_b_assertions=57622
P189_review_b_assertions=1493195
P190_review_b_assertions=1438171
P191_review_b_assertions=164049

All five Round-2 packages replay byte-identically from reviewer-owned
verifiers against frozen Round-1 inputs. No manuscript or source change was
requested; all five no-change delta records were accepted, and every
`main_round2.pdf` is the immutable accepted manuscript receipt.

| paper | reviewer representation | review-B assertions | verdict | live PDF SHA-256 | bytes |
|---|---|---:|---|---|---:|
| P187 | cyclic difference-constraint DP | 219,556 | PASS | `399ee1fd64a569ef3076e1049a5151e5b4b07d03d2c1592f84c5b2a811fbb8a1` | 332,246 |
| P188 | profile difference-sequence DP | 57,622 | PASS | `10b881a6200e075ed66514e8f4f8873c433383c8118c6037ad1ecd1d5bcb8bc3` | 304,360 |
| P189 | column-bit tuples + orbit repeat detection | 1,493,195 | PASS | `6ba00f6b542fdbefd4789e8f23f2d683c642132e989ff7af828436da063d6a81` | 363,099 |
| P190 | anchor-gap zero-transition DP | 1,438,171 | PASS | `81c785768621a2c3450fc67eeabc9b91d8cfda67d1061aad851844b5dd68905d` | 383,748 |
| P191 | interval deleted-cut subset grammar | 164,049 | PASS | `d8675928ecfe528b950af5402097b5f69657efc9cba7c8eb0bb5c27ec96df78b` | 380,787 |

Round-2 keeps the same lifecycle boundary as Round 1: internal acceptance
only, `OWNER_AMBER / HOLD_EXTERNAL`.
