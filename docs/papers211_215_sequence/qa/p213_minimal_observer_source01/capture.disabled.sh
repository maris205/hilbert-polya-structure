# P213 SOURCE ONLY. A new exact literal binding/source review is mandatory.
# The unconditional gate runs before cwd changes or artifact allocation.
printf '%s\n' 'P213_CAPTURE_DISABLED_UNRESOLVED_BINDING' >&2
exit 78

# Below this gate is the proposed small capture body, never executed here.
# Fill these literal absolute values only in a new independently reviewed copy.
P213_CAPTURE_ENV=''
P213_CAPTURE_MKDIR=''
P213_CAPTURE_PYTHON=''
P213_CAPTURE_OBSERVER=''
P213_CAPTURE_CWD=''
P213_CAPTURE_DIRECTORY=''
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
