# P213 exact finite-permission capture; operational authority is external.
# The preparation copy has an unconditional gate before cwd/allocation.

# Chosen paths are permissions, not observations of tool identity or presence.
# Ordinary trusted bootstrap/filesystem limits are specified in PREPARATION.md.
P213_CAPTURE_ENV='/usr/bin/env'
P213_CAPTURE_MKDIR='/usr/bin/mkdir'
P213_CAPTURE_PYTHON='/usr/bin/python3.10'
P213_CAPTURE_OBSERVER='/root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/qa/p213_minimal_observer_enabled01/observe.py'
P213_CAPTURE_CWD='/root/autodl-tmp/symbolic_dynamics'
P213_CAPTURE_DIRECTORY='/root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/qa/p213_minimal_observer_probe01'
for P213_CAPTURE_VALUE in "$P213_CAPTURE_ENV" "$P213_CAPTURE_MKDIR" \
    "$P213_CAPTURE_PYTHON" "$P213_CAPTURE_OBSERVER" \
    "$P213_CAPTURE_CWD" "$P213_CAPTURE_DIRECTORY"; do
    case "$P213_CAPTURE_VALUE" in
        /*) ;;
        *) printf '%s\n' 'P213_CAPTURE_PATH_UNRESOLVED' >&2; exit 78 ;;
    esac
done
umask 077
set -o noclobber
cd -- "$P213_CAPTURE_CWD" || exit 78
# Nonrecursive, exclusive directory allocation; an existing directory is a failure.
# Trusted mkdir/filesystem/0700 ownership, not hostile-parent protection, is assumed.
"$P213_CAPTURE_MKDIR" -m 700 -- "$P213_CAPTURE_DIRECTORY" || exit 78
P213_CAPTURE_STDOUT="$P213_CAPTURE_DIRECTORY/stdout.bin"
P213_CAPTURE_STDERR="$P213_CAPTURE_DIRECTORY/stderr.bin"
# Fresh private directory plus noclobber, not noclobber alone on arbitrary devices.
# If the second allocation fails, the first empty artifact is retained.
exec 3>"$P213_CAPTURE_STDOUT" || exit 78
exec 4>"$P213_CAPTURE_STDERR" || exit 78
"$P213_CAPTURE_ENV" -i LANG=C LC_ALL=C "$P213_CAPTURE_PYTHON" \
    -I -S -B "$P213_CAPTURE_OBSERVER" 1>&3 2>&4 3>&- 4>&-
P213_CAPTURE_STATUS=$?
exec 3>&-
exec 4>&-
printf 'P213_OBSERVER_NATIVE_EXIT=%s\n' "$P213_CAPTURE_STATUS"
exit "$P213_CAPTURE_STATUS"
