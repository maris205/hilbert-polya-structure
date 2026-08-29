# Narrative report

The apparent ambiguity of dry friction at zero velocity is removed by freezing
the maximal-monotone Sign graph together with a viability rule: the interval
\([-a_f,a_f]\), \(a_f=c/\omega^2\), is a static set, while an exterior rest
point releases inward.  Each slip branch is a harmonic oscillator shifted by
\(\pm a_f\), so energy decreases exactly by the friction work.

From a positive rest \(A>a_f\), the first turning point is
\(2a_f-A\); each subsequent complete half-cycle lowers the turning magnitude
by \(2a_f\).  The ceiling formula gives finite capture and retains the exact
stopping turn.  For a nonzero initial velocity, the first segment is generally
only a partial arc.  The center/radius/`atan2` ledger then adds an integer number
of complete half-cycles and records the first finite stop.

The `c=0` face is not silently folded into the ceiling formula: it is an exact
conservative harmonic oscillator with no capture.  The package therefore
separates physical event dynamics from any zeta or target-operator language.
