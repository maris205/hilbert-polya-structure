# Hostile audit

The mutation harness applies 13 repaired-hash semantic edits and one stale-hash
edit. The independent checker rejects all 14:

    repaired_hash=13
    stale_hash=1
    caught=iterate,time,roof,fixed,zeno,r_zero_zeno,zeta_domain,closed_series,multiplier,route,route_b,scope,unknown,stale

The r_zero_zeno attack is intentional: under the guard excluding zero incoming
velocity and the separate rest state, r=0,J=0 is one positive flight followed
by sticking, not an infinite Zeno execution.
