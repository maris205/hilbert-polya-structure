"""Build the immutable manifest after a successful registered audit."""

from pathlib import Path

from capacity_audit.manifest import write_result_manifest


def main() -> None:
    project_root = Path(__file__).resolve().parents[2]
    output = write_result_manifest(project_root)
    print(output)


if __name__ == "__main__":
    main()
