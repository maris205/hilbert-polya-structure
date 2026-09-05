#!/usr/bin/env python3
"""Audit explicitly selected retained papers without claiming five-paper PASS.

--evidence-only checks replays/builds/reviews before final paper manifests.
Without it, every ordinary paper_gate requirement is enforced as well.
No remote actions or output-file writes. Canonicals remain immutable.
"""
import argparse
import audit_batch as audit


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("papers", nargs="+", type=int, choices=tuple(audit.PAPERS))
    parser.add_argument("--evidence-only", action="store_true")
    args = parser.parse_args()
    assert len(args.papers) == len(set(args.papers)), "duplicate paper"
    print("scope=RETAINED_SUBSET_NOT_FIVE_PAPER_BATCH", flush=True)
    print("mode="+("evidence_only" if args.evidence_only else "full_paper_packages"), flush=True)
    totals = [0, 0, 0]
    pages = 0
    for n in args.papers:
        directory = audit.PAPERS[n]
        if args.evidence_only:
            p = audit.cold_gate(n, directory)
            c = audit.citation_gate(n, directory)
            author = audit.replay(*audit.AUTHOR[n], f"P{n} author")
        else:
            p, c, author = audit.paper_gate(n, directory)
        a = audit.review_gate(n, "a")
        b = audit.review_gate(n, "b")
        pages += p
        totals = [x+y for x,y in zip(totals,(author,a,b))]
        print(f"P{n} pages={p} citations={c} author={author} A={a} B={b} each_replayed_twice=YES", flush=True)
    print(f"papers={len(args.papers)} pages={pages} cold_builds={2*len(args.papers)}", flush=True)
    print("canonical_counts_author_A_B="+repr(totals), flush=True)
    print(f"audit_assertions={audit.ASSERTIONS}", flush=True)
    print("status="+("EVIDENCE_PASS_NOT_FINAL" if args.evidence_only else "SUBSET_PASS_NOT_BATCH_COMPLETE"), flush=True)
    print("external_status=OWNER_AMBER/HOLD_EXTERNAL", flush=True)


if __name__ == "__main__":
    main()
