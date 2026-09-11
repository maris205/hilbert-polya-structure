"""SOURCE_PREPARATION_NO_RUN: proposed cold_build_2 diagnostic census.

This function has not been imported, compiled, called or tested. It is not a
standalone executable. The future full auditor must supply the documented
helpers/globals and separately bind this complete source, runtime, all exact
inputs and exclusive output authority. No prepared census is imported.
"""


def diagnostic_census():
    """Reread exact cold2 log roles; preserve every diagnostic literal/context.

    Required helpers: read(path)->bytes, raw_pin(bytes), obj(path),
    put(name, value), demand(test, group, detail).
    Required globals: INNER, COLD (Path-like), DETAILS (dict), FINDINGS (list).
    read/obj must already enforce the future auditor's immutable input scope
    and record complete read provenance. put must be exclusive/no-overwrite.
    Parent handles all-file tree closure, native/capture/runtime/options,
    FLS/BibTeX graph semantics, actual page views and final adjudication.
    """
    import re

    expected_inner = (
        "/root/autodl-tmp/symbolic_dynamics/papers/"
        "211-kernel-image-projection-feedback/qa_final/cold_build_2/inner"
    )
    demand(str(INNER) == expected_inner and COLD == INNER / "source_only",
           "diagnostic_scope", "literal cold_build_2 inner/source_only roles")
    demand(isinstance(DETAILS, dict) and isinstance(FINDINGS, list),
           "diagnostic_scope", "explicit DETAILS/FINDINGS interfaces")
    role_names = (
        "commands/bibtex/stdout.raw",
        "commands/pass1/stdout.raw",
        "commands/pass2/stdout.raw",
        "commands/pass3/stdout.raw",
        "pass_artifacts_bibtex/after/main.blg",
        "pass_artifacts_bibtex/after/main.log",
        "pass_artifacts_bibtex/before/main.log",
        "pass_artifacts_pass1/after/main.log",
        "pass_artifacts_pass2/after/main.blg",
        "pass_artifacts_pass2/after/main.log",
        "pass_artifacts_pass2/before/main.blg",
        "pass_artifacts_pass2/before/main.log",
        "pass_artifacts_pass3/after/main.blg",
        "pass_artifacts_pass3/after/main.log",
        "pass_artifacts_pass3/before/main.blg",
        "pass_artifacts_pass3/before/main.log",
        "source_only/main.blg",
        "source_only/main.log",
    )
    demand(len(role_names) == 18 and len(set(role_names)) == 18,
           "diagnostic_scope", "exact eighteen unique text roles")
    patterns = (
        ("warning", r"\bwarning\b"),
        ("undefined", r"undefined"),
        ("missing_character", r"missing\s+character|character.*missing"),
        ("overfull", r"overfull"),
        ("underfull", r"underfull"),
        ("rerun", r"rerun"),
        ("error_or_fatal", r"\berror\b|\bfatal\b|emergency stop|^!"),
    )
    compiled = [(name, re.compile(pattern, re.I))
                for name, pattern in patterns]
    emission_categories = {
        "ACTUAL_ENGINE_WARNING",
        "ACTUAL_LATEX_PACKAGE_OR_CLASS_WARNING",
        "ACTUAL_BIBTEX_WARNING",
    }
    census = []
    before_pins = {}
    for relative in role_names:
        demand(relative and not relative.startswith("/") and
               ".." not in relative.split("/"),
               "diagnostic_scope", "normalized role " + relative)
        path = INNER / relative
        raw = read(path)
        demand(isinstance(raw, bytes), "diagnostic_bytes", str(path))
        value = raw_pin(raw)
        before_pins[str(path)] = value
        # Strict UTF-8 is intentional: malformed bytes must fail rather than
        # disappear into replacement characters. Raw pins retain all bytes.
        text = raw.decode("utf-8")
        lines = text.split("\n")
        if lines and lines[-1] == "":
            lines.pop()
        matching = []
        for index, line in enumerate(lines):
            categories = [name for name, pattern in compiled
                          if pattern.search(line)]
            if not categories:
                continue
            classification = "OTHER_LITERAL_MATCH_REQUIRES_CONTEXT"
            if re.match(r"^(?:pdftex|xetex|luatex|luahbtex)\s+warning\b",
                        line, re.I):
                classification = "ACTUAL_ENGINE_WARNING"
            elif re.match(
                r"^(?:latex(?:\s+font)?|package\s+\S+|class\s+\S+)"
                r"\s+warning\b", line, re.I
            ):
                classification = "ACTUAL_LATEX_PACKAGE_OR_CLASS_WARNING"
            elif re.match(r"^warning--", line, re.I):
                classification = "ACTUAL_BIBTEX_WARNING"
            elif re.match(r"^underfull\b", line, re.I):
                classification = "ACTUAL_UNDERFULL_DIAGNOSTIC"
            elif re.match(r"^overfull\b", line, re.I):
                classification = "ACTUAL_OVERFULL_DIAGNOSTIC"
            elif re.match(r"^missing\s+character\b", line, re.I):
                classification = "ACTUAL_TEX_MISSING_CHARACTER_DIAGNOSTIC"
            elif re.match(r"^(?:!|emergency stop|fatal error)", line, re.I):
                classification = "ACTUAL_ERROR_OR_FATAL_DIAGNOSTIC"
            elif re.match(r"^\(rerunfilecheck\)\s+rerun\b", line, re.I):
                classification = "ACTUAL_RERUN_REQUEST_CONTINUATION"
            elif re.match(
                r"^package microtype info: character .* is missing$",
                line, re.I
            ):
                classification = (
                    "MICROTYPE_INFO_PROTRUSION_CONTEXT_NOT_TEX_MISSING_CHARACTER"
                )
            elif (re.match(
                r"^(?:Package:|File:|[(/]| file:line:error|"
                r"Package rerunfilecheck Info:|Package uniquecounter Info:)",
                line
            ) or "Providing info/warning/error" in line):
                classification = (
                    "LOADER_METADATA_OR_INFORMATIONAL_LITERAL_NOT_WARNING_EMISSION"
                )
            first = max(0, index - 2)
            end = min(len(lines), index + 3)
            matching.append({
                "line": index + 1,
                "text": line,
                "categories": categories,
                "classification": classification,
                "context_first_line": first + 1,
                "context_last_line": end,
                "context": lines[first:end],
            })
        row = {
            "relative_role": relative,
            "path": str(path),
            "pin": value,
            "line_count": len(lines),
            "trailing_lf": text.endswith("\n"),
            "matching_lines": matching,
            "literal_match_counts": {
                name: sum(name in item["categories"] for item in matching)
                for name, _ in patterns
            },
            "actual_engine_warnings": [
                item for item in matching
                if item["classification"] == "ACTUAL_ENGINE_WARNING"
            ],
            "actual_warning_emission_count": sum(
                item["classification"] in emission_categories
                for item in matching
            ),
            "actual_tex_missing_character_diagnostic_count": sum(
                item["classification"] ==
                "ACTUAL_TEX_MISSING_CHARACTER_DIAGNOSTIC"
                for item in matching
            ),
            "unclassified_matches": [
                item for item in matching if item["classification"] ==
                "OTHER_LITERAL_MATCH_REQUIRES_CONTEXT"
            ],
            "interpretation_limit": (
                "Literal census/categories are not harmlessness, glyph loss, "
                "whole-build validity, diagnostic disposition or acceptance."
            ),
        }
        census.append(row)

    by_role = {row["relative_role"]: row for row in census}
    final_row = by_role["source_only/main.log"]
    final_archive_row = by_role["pass_artifacts_pass3/after/main.log"]
    demand(final_row["pin"] == final_archive_row["pin"],
           "diagnostic_final_log", "final and pass3 archive have same bytes")
    emitted = [
        item for item in final_row["matching_lines"]
        if item["classification"] in emission_categories
    ]

    # This additional input must be pinned by the future parent binding.
    # obj/read are required to reject inconsistent multiple reads.
    measurement_path = INNER / "MEASURED_NOT_VIEWED.json"
    measurement = obj(measurement_path)
    measurement_pin = raw_pin(read(measurement_path))
    demand(isinstance(measurement, dict) and
           isinstance(measurement.get("diagnostics"), dict),
           "diagnostic_recorded", "actual saved diagnostics object")
    recorded_warnings = measurement["diagnostics"].get("warnings")
    demand(isinstance(recorded_warnings, list) and
           all(isinstance(line, str) for line in recorded_warnings),
           "diagnostic_recorded", "actual saved warning array")

    # Multiset matching preserves repeated warning occurrences. There is no
    # expected count or cold1-specific warning string in this logic.
    recorded_remaining = list(recorded_warnings)
    emitted_only = []
    for item in emitted:
        if item["text"] in recorded_remaining:
            recorded_remaining.remove(item["text"])
        else:
            emitted_only.append(item)
    comparison = {
        "measurement_path": str(measurement_path),
        "measurement_pin": measurement_pin,
        "recorded_warning_lines": list(recorded_warnings),
        "actual_final_warning_emissions": emitted,
        "emitted_not_recorded": emitted_only,
        "recorded_not_emitted": recorded_remaining,
        "matching_method": "exact text multiset, preserving duplicates",
        "diagnostic_disposition": "PENDING_ROOT",
    }
    finding = None
    if emitted_only or recorded_remaining:
        finding = {
            "id": "P211-COLD2-DIAGNOSTIC-CENSUS",
            "severity": "Minor",
            "status": "OPEN_PENDING_ROOT_DIAGNOSTIC_DISPOSITION",
            "scope": "actual emitted-versus-recorded warning census",
            "final_log": {"path": final_row["path"], "pin": final_row["pin"]},
            "measurement": {
                "path": str(measurement_path), "pin": measurement_pin
            },
            "emitted_not_recorded": emitted_only,
            "recorded_not_emitted": recorded_remaining,
            "inference_limits": [
                "Not a claim of harmlessness or glyph loss.",
                "Does not close other artifact findings or grant acceptance.",
                "No source/log/measurement repair or rebuild is authorized.",
            ],
            "required_next_gate": (
                "Preserve originals and obtain an immutable supplemental "
                "root diagnostic disposition under the full artifact gate."
            ),
        }
        demand(not any(isinstance(item, dict) and item.get("id") == finding["id"]
                       for item in FINDINGS),
               "diagnostic_finding", "do not overwrite or duplicate a finding")
        FINDINGS.append(finding)

    after_pins = {}
    for relative in role_names:
        path = INNER / relative
        after_pins[str(path)] = raw_pin(read(path))
        demand(after_pins[str(path)] == before_pins[str(path)],
               "diagnostic_input_closure", str(path))
    demand(raw_pin(read(measurement_path)) == measurement_pin,
           "diagnostic_input_closure", str(measurement_path))
    product = {
        "schema": "p211-cold2-full-log-diagnostic-census-v1",
        "status": "CENSUS_RECORDED_PENDING_ROOT_DIAGNOSTIC_DISPOSITION",
        "case_insensitive_patterns": [
            {"category": name, "pattern": pattern, "flags": "I"}
            for name, pattern in patterns
        ],
        "context_radius": 2,
        "role_names": list(role_names),
        "raw_log_pins_before": before_pins,
        "raw_log_pins_after": after_pins,
        "census": census,
        "recorded_warning_comparison": comparison,
        "finding": finding,
        "uses_prepared_census_as_evidence": False,
        "terminal_acceptance": False,
        "diagnostic_disposition": "PENDING_ROOT",
        "visual_review_by_this_function": False,
    }
    put("FULL_LOG_DIAGNOSTIC_CENSUS.json", product)
    DETAILS["diagnostic_census"] = {
        "role_count": len(role_names),
        "raw_log_bytes": sum(value["bytes"] for value in before_pins.values()),
        "measurement_pin": measurement_pin,
        "recorded_warning_comparison": comparison,
        "finding_id": finding["id"] if finding else None,
        "product": "FULL_LOG_DIAGNOSTIC_CENSUS.json",
        "terminal_acceptance": False,
        "diagnostic_disposition": "PENDING_ROOT",
    }
    return product
