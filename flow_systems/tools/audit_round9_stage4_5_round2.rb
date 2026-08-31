#!/usr/bin/env ruby
# frozen_string_literal: true

# Independent batch replay for Round 9 Papers 24--28, fresh Stage 4.5 round 2.
#
# The script is deliberately read-only.  It validates exact input/canonical
# bindings, current ARS machine contracts, bounded coverage replay, evidence
# rows, the seven-mode gate summary, and the separation between Stage 4.5 and
# Stage 5.  It does not make semantic findings or promote any manuscript.

require "digest"
require "find"
require "json"
require "open3"
require "pathname"

ROOT = Pathname.new(__dir__).parent.expand_path
LOCK_PATH = ROOT / "BATCH_ROUND9_STAGE4_5_ROUND2_INPUT_LOCK.json"
ARS_ROOT = Pathname.new(
  "/root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/0.1.26/" \
  "skills/academic-research-suite/ars"
)

PAPER_DIRS = {
  24 => "24-bianchi-holonomy-flow",
  25 => "25-three-disk-scattering-flow",
  26 => "26-level11-newform-time-change",
  27 => "27-congruence-inverse-limit-no-go",
  28 => "28-bolza-magnetic-flow"
}.freeze

EXPECTED_REFERENCE_COUNTS = {24 => 7, 25 => 8, 26 => 7, 27 => 5, 28 => 6}.freeze
EXPECTED_CITATION_CONTEXTS = {24 => 9, 25 => 13, 26 => 8, 27 => 5, 28 => 9}.freeze

REQUIRED_BASENAMES = %w[
  stage4_5_round2_input_manifest.json
  stage4_5_round2_reference_source_snapshot.json
  stage4_5_round2_reference_citation_audit.md
  stage4_5_round2_phase_c_internal_consistency_audit.md
  stage4_5_round2_originality_failure_mode_audit.md
  stage4_5_round2_originality_failure_mode_audit.json
  stage4_5_round2_claim_registry.json
  stage4_5_round2_claim_registry_coverage.json
  stage4_5_round2_evidence_source_map.json
  stage4_5_round2_evidence_rows.json
  stage4_5_round2_claim_strength_drift_findings.json
  stage4_5_round2_e6_semantic_audit.md
  stage4_5_round2_compliance_report.json
  stage4_5_round2_integrity_report.json
  stage4_5_round2_final_integrity_report.md
  stage4_5_round2_material_passport.json
  stage4_5_round2_preview_build_receipt.json
].freeze

C4_BOUNDARY = (
  "This check verifies disclosure and claim-to-provenance fidelity. " \
  "It does not judge whether the experiment was correctly designed, run, " \
  "statistically adequate, or reproducible by ARS."
).freeze

FAILURE_MODE_NAMES = [
  "Implementation bug passing AI self-review",
  "Hallucinated citation",
  "Hallucinated experimental result",
  "Shortcut reliance",
  "Implementation bug reframed as novel insight",
  "Methodology fabrication",
  "Frame-lock at early pipeline stage"
].freeze

# The input lock predates the final Git-clean packaging pass.  Consequently,
# its canonical-tree commitments include thirteen LaTeX intermediates that are
# deliberately excluded by the repository's .gitignore.  Keep their exact
# hashes here so a clean clone can reconstruct the original tree commitment
# without force-adding generated logs.  If an intermediate is present, its
# bytes must still match this binding; only absence is projected.
LOCKED_IGNORED_BUILD_ARTIFACTS = {
  24 => {
    "papers/24-bianchi-holonomy-flow/paper/paper.log" =>
      "c66740aa4bea9820a1739723428782632d49d2ed476296e4d1b7de6714827b40"
  }.freeze,
  25 => {
    "papers/25-three-disk-scattering-flow/paper/paper.aux" =>
      "d642cff44f3740a84a4d1ae9194d3aebd8425d07caae814e9583950fd2a0f927",
    "papers/25-three-disk-scattering-flow/paper/paper.bbl" =>
      "9b2f74518f67a0226e606ae99525f72b3076f581f455910fa068b869fb8d21a4",
    "papers/25-three-disk-scattering-flow/paper/paper.blg" =>
      "94e73fc83c94d2d55182b896229a639d7aa3c7154aa1f4c6d9a288b2fdd06db9",
    "papers/25-three-disk-scattering-flow/paper/paper.log" =>
      "a8e0836258e7dbc50c2a702692f278523b17f74eb8525f638af7e09ae21cb767",
    "papers/25-three-disk-scattering-flow/paper/paper.out" =>
      "7e16542304f7fc97237cc7add8a3d1698017f05997772fefa205e93b9b68ca0b"
  }.freeze,
  26 => {
    "papers/26-level11-newform-time-change/paper/paper.log" =>
      "9412dc28c6af63c3707ad51598dd7830600e9a1f9968de2c0d1ff2449f48770f"
  }.freeze,
  27 => {
    "papers/27-congruence-inverse-limit-no-go/paper/paper.log" =>
      "f0124c9f26bdd08fae8a1edc777b11c0ff10140ecee5206f3b71da3d565bdfb6"
  }.freeze,
  28 => {
    "papers/28-bolza-magnetic-flow/paper/paper.aux" =>
      "0a0a2a8ddea0213a5c0d6317f5cfae2b9ab0db1cc4c498bfee254611974b8dca",
    "papers/28-bolza-magnetic-flow/paper/paper.bbl" =>
      "49ca5b0ab4a5292608c9def541982ba13e804f6b6f89eef0f921db4956b01c1e",
    "papers/28-bolza-magnetic-flow/paper/paper.blg" =>
      "c636a1f0bf09160111f49ccab4eeeeac66011c91f779c30679312d394d1d9511",
    "papers/28-bolza-magnetic-flow/paper/paper.log" =>
      "629e8ca8ccb79aadcbab8b6112e6107660ecf3b9b87e72610b86a401e231570c",
    "papers/28-bolza-magnetic-flow/paper/paper.out" =>
      "e67d797f612b8ce8202aa63cc3397733c9fa17e7f23b450725dda2a5e9ac9a31"
  }.freeze
}.freeze

@pass_count = 0
@failures = []
@gate_rows = []

def rel(path)
  Pathname.new(path).expand_path.relative_path_from(ROOT).to_s
rescue ArgumentError
  path.to_s
end

def sha256(path)
  Digest::SHA256.file(path).hexdigest
end

def load_json(path)
  JSON.parse(File.binread(path).force_encoding("UTF-8"))
rescue JSON::ParserError => e
  raise "invalid JSON at #{rel(path)}: #{e.message}"
end

def check(label)
  result = yield
  raise "returned false" unless result

  @pass_count += 1
  puts "PASS #{label}"
rescue StandardError => e
  @failures << "#{label}: #{e.message}"
  warn "FAIL #{label}: #{e.message}"
end

def require_equal(actual, expected, context)
  return true if actual == expected

  raise "#{context}: #{actual.inspect} != #{expected.inspect}"
end

def tree_hash(path, bound_absent_files: {})
  file_hashes = {}
  Find.find(path.to_s) do |entry|
    stat = File.lstat(entry)
    next unless stat.file?

    file = Pathname.new(entry)
    file_hashes[rel(file)] = sha256(file)
  end

  bound_absent_files.each do |relative_path, expected_sha|
    candidate = (ROOT / relative_path).expand_path
    tree_prefix = "#{path.expand_path}#{File::SEPARATOR}"
    raise "bound omission escapes tree: #{relative_path}" unless candidate.to_s.start_with?(tree_prefix)

    if file_hashes.key?(relative_path)
      require_equal(file_hashes.fetch(relative_path), expected_sha, relative_path)
    else
      file_hashes[relative_path] = expected_sha
    end
  end

  rows = file_hashes.sort_by { |relative_path, _sha| relative_path }.map do |relative_path, sha|
    "#{sha}  #{relative_path}\n"
  end
  Digest::SHA256.hexdigest(rows.join)
end

def run_command(label, *argv)
  stdout, stderr, status = Open3.capture3(*argv, chdir: ROOT.to_s)
  return true if status.success?

  raise "#{label} exit #{status.exitstatus}: #{[stdout, stderr].join("\n").strip}"
end

def validate_json_schema(schema, instance)
  code = <<~PY
    import json, sys
    from jsonschema import Draft202012Validator
    with open(sys.argv[1], "r", encoding="utf-8") as f:
        schema = json.load(f)
    with open(sys.argv[2], "r", encoding="utf-8") as f:
        instance = json.load(f)
    errors = sorted(Draft202012Validator(schema).iter_errors(instance), key=lambda e: list(e.path))
    if errors:
        for error in errors[:20]:
            print(f"{list(error.path)}: {error.message}", file=sys.stderr)
        sys.exit(1)
  PY
  run_command("jsonschema", "python3", "-c", code, schema.to_s, instance.to_s)
end

def bib_keys(raw)
  raw.scan(/@\w+\s*\{\s*([^,\s]+)/).flatten
end

def citation_commands(raw)
  raw.scan(/\\cite\w*\s*(?:\[[^\]]*\]\s*)*\{([^}]*)\}/m).map(&:first)
end

def citation_keys(raw)
  citation_commands(raw).flat_map { |group| group.split(",") }.map(&:strip).reject(&:empty?)
end

def deep_values(value, out = [])
  case value
  when Hash
    value.each_value { |child| deep_values(child, out) }
  when Array
    value.each { |child| deep_values(child, out) }
  else
    out << value
  end
  out
end

def canonical_failure_mode_name(value)
  value.to_s.downcase.gsub(/\A\s*(?:mode\s*)?\d+[\s_.:-]*/, "")
    .gsub(/[^a-z0-9]+/, " ").strip
end

check("input lock exists and parses") do
  LOCK_PATH.file? && load_json(LOCK_PATH)["schema_version"] == "round9-stage4.5-input-lock/1.0"
end

lock = load_json(LOCK_PATH)
lock_sha = sha256(LOCK_PATH)

check("input lock carries five unique papers") do
  ids = lock.fetch("papers").map { |row| row.fetch("paper_id") }
  ids == PAPER_DIRS.keys && ids.uniq.length == 5
end

lock.fetch("route_evaluators").each do |route, binding|
  path = ROOT / binding.fetch("path")
  check("#{route} evaluator hash binding") do
    require_equal(sha256(path), binding.fetch("sha256"), rel(path))
  end
end

lock.fetch("papers").each do |binding|
  id = binding.fetch("paper_id")
  paper_root = ROOT / "papers" / PAPER_DIRS.fetch(id)
  notes = paper_root / "notes"
  draft = ROOT / binding.dig("audit_draft", "path")
  bib = ROOT / binding.dig("audit_bibliography", "path")
  bundle = ROOT / binding.dig("revision_evidence_bundle", "path")

  {
    "audit draft" => [draft, binding.dig("audit_draft", "sha256")],
    "audit bibliography" => [bib, binding.dig("audit_bibliography", "sha256")],
    "revision evidence bundle" => [bundle, binding.dig("revision_evidence_bundle", "sha256")]
  }.each do |label, (path, expected)|
    check("P#{id} #{label} hash binding") do
      path.file? && require_equal(sha256(path), expected, rel(path))
    end
  end

  check("P#{id} canonical tree unchanged") do
    path = ROOT / binding.fetch("canonical_tree_path")
    bound_absent_files = LOCKED_IGNORED_BUILD_ARTIFACTS.fetch(id, {})
    actual = tree_hash(path, bound_absent_files: bound_absent_files)
    require_equal(actual, binding.fetch("canonical_tree_sha256"), rel(path))
  end

  check("P#{id} results tree unchanged") do
    path = ROOT / binding.fetch("results_tree_path")
    require_equal(tree_hash(path), binding.fetch("results_tree_sha256"), rel(path))
  end

  REQUIRED_BASENAMES.each do |basename|
    check("P#{id} required artifact #{basename}") { (notes / basename).file? }
  end

  # Continue after the existence inventory so a partial run reports every gap.
  next unless REQUIRED_BASENAMES.all? { |basename| (notes / basename).file? }

  paths = REQUIRED_BASENAMES.to_h { |basename| [basename, notes / basename] }
  manifest = load_json(paths.fetch("stage4_5_round2_input_manifest.json"))
  manifest_text = JSON.generate(manifest)
  check("P#{id} manifest binds batch input lock") do
    manifest_text.include?(LOCK_PATH.basename.to_s) && manifest_text.include?(lock_sha)
  end
  [[draft, binding.dig("audit_draft", "sha256")],
   [bib, binding.dig("audit_bibliography", "sha256")],
   [bundle, binding.dig("revision_evidence_bundle", "sha256")]].each do |path, digest|
    check("P#{id} manifest binds #{path.basename}") do
      manifest_text.include?(path.basename.to_s) && manifest_text.include?(digest)
    end
  end

  draft_raw = File.binread(draft).force_encoding("UTF-8")
  bib_raw = File.binread(bib).force_encoding("UTF-8")
  refs = bib_keys(bib_raw)
  cites = citation_commands(draft_raw)
  cited_keys = citation_keys(draft_raw)

  check("P#{id} bibliography denominator") do
    refs.uniq.length == EXPECTED_REFERENCE_COUNTS.fetch(id) && refs.length == refs.uniq.length
  end
  check("P#{id} citation-context denominator") do
    cites.length == EXPECTED_CITATION_CONTEXTS.fetch(id)
  end
  check("P#{id} all citation keys resolve") do
    (cited_keys.uniq - refs).empty?
  end

  snapshot_path = paths.fetch("stage4_5_round2_reference_source_snapshot.json")
  snapshot = load_json(snapshot_path)
  snapshot_text = JSON.generate(snapshot)
  check("P#{id} fresh reference snapshot date and query trail") do
    snapshot_text.include?("2026-08-31") &&
      snapshot_text.match?(/query/i) && snapshot_text.match?(%r{https?://})
  end
  refs.each do |ref_slug|
    check("P#{id} snapshot includes #{ref_slug}") { snapshot_text.include?(ref_slug) }
  end
  snapshot_records = snapshot["records"] || snapshot["references"] || []
  check("P#{id} snapshot has exactly one record per reference") do
    snapshot_records.map { |row| row["ref_slug"] || row["citation_key"] }.sort == refs.sort &&
      snapshot_records.length == refs.length
  end
  check("P#{id} every reference has a fresh WebSearch/authority trail") do
    snapshot_records.all? do |row|
      row.fetch("fresh_query").to_s.strip != "" &&
        row.fetch("query_url").to_s.match?(%r{\Ahttps?://}) &&
        (row["queried_at"] || row.dig("semantic_scholar", "queried_at") ||
          snapshot["captured_at"] || snapshot["generated_at"]).to_s.start_with?("2026-08-31") &&
        (row["audit_status"] || row["metadata_verdict"] || row["status"]).to_s.match?(/VERIFIED|PASS/) &&
        !row.fetch("result", row["result_summary"]).to_s.empty? &&
        !JSON.generate(row).match?(/SEARCH_ACCESS_LIMITATION|DOI_MISMATCH/)
    end
  end
  check("P#{id} Semantic Scholar Tier-0 trail covers every reference") do
    snapshot_records.all? do |row|
      s2 = row.fetch("semantic_scholar")
      %w[S2_VERIFIED S2_NOT_FOUND S2_API_UNAVAILABLE].include?(s2.fetch("status")) &&
        s2.fetch("queried_at").to_s.start_with?("2026-08-31") &&
        !JSON.generate(s2).match?(/DOI_MISMATCH/)
    end
  end
  check("P#{id} successful S2 matches meet title-similarity protocol") do
    snapshot_records.all? do |row|
      s2 = row.fetch("semantic_scholar")
      next true unless s2.fetch("status") == "S2_VERIFIED"

      s2.fetch("match_score").to_f >= 0.70 &&
        !s2.fetch("semantic_scholar_id").to_s.empty? &&
        !s2.fetch("s2_title").to_s.empty? &&
        %w[s2_title_search s2_doi_lookup].include?(s2.fetch("verification_method"))
    end
  end

  reference_audit = File.read(paths.fetch("stage4_5_round2_reference_citation_audit.md"), encoding: "UTF-8")
  check("P#{id} reference audit is fresh and complete") do
    reference_audit.include?("#{refs.length}/#{refs.length}") &&
      reference_audit.include?("#{cites.length}/#{cites.length}")
  end

  registry_path = paths.fetch("stage4_5_round2_claim_registry.json")
  coverage_path = paths.fetch("stage4_5_round2_claim_registry_coverage.json")
  evidence_path = paths.fetch("stage4_5_round2_evidence_rows.json")
  source_map_path = paths.fetch("stage4_5_round2_evidence_source_map.json")
  drift_path = paths.fetch("stage4_5_round2_claim_strength_drift_findings.json")

  check("P#{id} claim registry schema") do
    validate_json_schema(
      ARS_ROOT / "shared/contracts/evidence/claim_registry.schema.json",
      registry_path
    )
  end
  registry = load_json(registry_path)
  claims = registry.fetch("claims")
  check("P#{id} claim registry binds exact draft and ALL tier") do
    registry.fetch("draft_raw_sha256") == sha256(draft) &&
      !claims.empty? && claims.all? { |claim| claim["selection_tier"] == "ALL" }
  end
  check("P#{id} claim spans are exact UTF-8 slices") do
    claims.all? do |claim|
      span = claim.fetch("draft_span")
      draft_raw.byteslice(span.fetch("start_byte")...span.fetch("end_byte")) == claim.fetch("claim_text")
    end
  end

  check("P#{id} bounded claim coverage replay") do
    run_command(
      "claim coverage replay",
      "python3", (ARS_ROOT / "scripts/claim_registry_coverage.py").to_s,
      "--draft", draft.to_s,
      "--registry", registry_path.to_s,
      "--validate-report", coverage_path.to_s
    )
  end
  coverage = load_json(coverage_path)
  check("P#{id} bounded coverage has zero candidate gaps") do
    coverage.fetch("candidate_unregistered_count") == 0 &&
      coverage.fetch("semantic_extraction_coverage") == "not_machine_detectable" &&
      coverage.fetch("registry_claim_count") == claims.length
  end

  check("P#{id} evidence rows official replay") do
    run_command(
      "evidence rows replay",
      "python3", (ARS_ROOT / "scripts/evidence_rows.py").to_s,
      "validate", "--source-map", source_map_path.to_s, evidence_path.to_s
    )
  end
  evidence_rows = load_json(evidence_path)
  evidence_claim_ids = evidence_rows.map { |row| row.dig("claim", "claim_id") }.uniq
  check("P#{id} evidence rows cover every registered claim") do
    evidence_claim_ids.sort == claims.map { |claim| claim.fetch("claim_id") }.sort
  end
  actual_evidence_tuples = evidence_rows.map do |row|
    [row.dig("claim", "claim_id"), row.dig("source", "ref_slug")]
  end
  expected_evidence_tuples = claims.flat_map do |claim|
    claim.fetch("ref_slugs").map { |ref_slug| [claim.fetch("claim_id"), ref_slug] }
  end
  check("P#{id} evidence rows exactly cover every claim/ref tuple") do
    expected_evidence_tuples.sort == actual_evidence_tuples.sort &&
      actual_evidence_tuples.length == actual_evidence_tuples.uniq.length &&
      claims.all? { |claim| !claim.fetch("ref_slugs").empty? }
  end
  check("P#{id} evidence rows are source-bound, not anchorless upgrades") do
    evidence_rows.all? do |row|
      !row.dig("source", "ref_slug").to_s.empty? &&
        row.dig("excerpt", "state") == "agent_extracted" &&
        !row.dig("excerpt", "text").to_s.empty?
    end
  end
  source_map = load_json(source_map_path)
  check("P#{id} explicit source map covers every ref slug") do
    actual_evidence_tuples.map(&:last).uniq.all? do |ref_slug|
      source_map[ref_slug].is_a?(String) && !source_map[ref_slug].empty?
    end
  end

  check("P#{id} E6 finding schema") do
    validate_json_schema(
      ARS_ROOT / "shared/contracts/revision/claim_strength_drift_findings.schema.json",
      drift_path
    )
  end
  drift = load_json(drift_path)
  check("P#{id} E6 exact draft/bundle binding") do
    drift.fetch("status") == "completed" &&
      drift.fetch("final_draft_sha256") == sha256(draft) &&
      drift.fetch("revision_evidence_bundle_sha256") == sha256(bundle)
  end
  e6_text = File.read(paths.fetch("stage4_5_round2_e6_semantic_audit.md"), encoding: "UTF-8")
  check("P#{id} E6 semantic limitation is explicit") do
    e6_text.match?(/model[- ]mediated/i) &&
      e6_text.match?(/none detected by (?:the )?recorded/i) &&
      !e6_text.match?(/deterministically proves no drift/i)
  end

  phase_c_text = File.read(paths.fetch("stage4_5_round2_phase_c_internal_consistency_audit.md"), encoding: "UTF-8")
  check("P#{id} C4 boundary is verbatim") { phase_c_text.include?(C4_BOUNDARY) }

  originality_text = File.read(paths.fetch("stage4_5_round2_originality_failure_mode_audit.md"), encoding: "UTF-8")
  check("P#{id} originality audit is fresh Mode 2 with professional-screen boundary") do
    originality_text.include?("2026-08-31") &&
      originality_text.match?(/Mode 2/i) &&
      originality_text.match?(/(?:Turnitin|iThenticate|professional (?:plagiarism|similarity))/i)
  end
  FAILURE_MODE_NAMES.each_with_index do |mode_name, index|
    check("P#{id} failure mode #{index + 1} recorded") do
      canonical_failure_mode_name(originality_text).include?(canonical_failure_mode_name(mode_name))
    end
  end
  originality = load_json(paths.fetch("stage4_5_round2_originality_failure_mode_audit.json"))
  phrase_searches = originality["phrase_searches"] || originality["queries"] ||
    originality["samples"] || []
  denominator = originality["body_paragraph_denominator"] || originality.fetch("denominator")
  successful_phrase_searches = phrase_searches.select do |row|
    tracks = row["tracks"] || row["searches"] || [
      row.fetch("quoted_exact_search", {}).merge("track" => "quoted_exact"),
      row.fetch("unquoted_supplementary_search", {}).merge("track" => "unquoted_supplementary_paraphrase")
    ]
    track_names = tracks.map do |track|
      name = track["track"] || track["lane"]
      name == "unquoted_supplementary" ? "unquoted_supplementary_paraphrase" : name
    end
    row_success = row["successful"] == true || row["successful_two_route_search"] == true ||
      row["dual_lane_success"] == true
    row_success &&
      %w[quoted_exact unquoted_supplementary_paraphrase].all? { |name| track_names.include?(name) } &&
      tracks.all? do |track|
        track_success = track["successful"] == true || track["status"].to_s.match?(/SUCCESS|REVIEWED/) ||
          track["transport_status"] == "success"
        top_results = track["top_results"] || track["results"] || track["top_result_summary"] || []
        transport_ok = track["http_status"] == 200 ||
          track["transport"].to_s.match?(/web.?search.?connector/i) ||
          track["transport_status"] == "success"
        track_success && transport_ok &&
          top_results.any? do |result|
            result["url"].to_s.match?(%r{\Ahttps?://}) &&
              !result["title"].to_s.empty? && !result["snippet"].to_s.empty?
          end &&
          !JSON.generate(track).match?(/SEARCH_ACCESS_LIMITATION/)
      end
  end
  check("P#{id} originality sample has genuine dual-search success at >=50%") do
    denominator.positive? &&
      originality.fetch("denominator") == denominator &&
      successful_phrase_searches.length >= (denominator / 2.0).ceil &&
      originality.fetch("successful_search_count") == successful_phrase_searches.length
  end
  check("P#{id} every changed paragraph has a successful dual search") do
    changed_rows = phrase_searches.select do |row|
      row["stage4_or_stage4_prime_changed"] == true ||
        row["stage4_or_stage4_prime_changed_surface"] == true
    end
    declared_changed_rate = originality["changed_success_rate"] ||
      (originality.fetch("changed_total").positive? ?
        originality.fetch("changed_successful").to_f / originality.fetch("changed_total") : 1.0)
    changed_rows.length == originality.fetch("changed_total") &&
      changed_rows.all? { |row| successful_phrase_searches.include?(row) } &&
      originality.fetch("changed_successful") == changed_rows.length &&
      declared_changed_rate == 1.0
  end
  check("P#{id} phrase queries use 8--12-word quoted excerpts") do
    successful_phrase_searches.all? do |row|
      quoted_track = (row["tracks"] || row["searches"] || []).find do |track|
        (track["track"] || track["lane"]) == "quoted_exact"
      end
      query = row["query"] || row.dig("quoted_exact_search", "query") || quoted_track&.dig("query")
      words = row["quoted_word_count"] || row["word_count"] ||
        (query.to_s.start_with?(%q{"}) && query.to_s.end_with?(%q{"}) ?
          query[1...-1].scan(/[[:alnum:]][[:alnum:]'\xE2\x80\x99-]*/).length : 0)
      query.to_s.start_with?(%q{"}) && query.to_s.end_with?(%q{"}) && words.between?(8, 12)
    end
  end
  seven_failure_modes = originality.fetch("seven_failure_modes")
  check("P#{id} exact ARS seven-mode taxonomy and closed statuses") do
    seven_failure_modes.keys.map { |key| canonical_failure_mode_name(key) }.sort ==
      FAILURE_MODE_NAMES.map { |name| canonical_failure_mode_name(name) }.sort &&
      seven_failure_modes.values.all? do |row|
        evidence = row["evidence"] || row["basis"]
        row.fetch("status") == "CLEAR" &&
          !(evidence.respond_to?(:empty?) ? evidence.empty? : evidence.to_s.empty?)
      end
  end

  compliance_path = paths.fetch("stage4_5_round2_compliance_report.json")
  check("P#{id} compliance schema") do
    run_command(
      "compliance schema",
      "python3", (ARS_ROOT / "scripts/check_compliance_report.py").to_s,
      compliance_path.to_s
    )
  end

  report_path = paths.fetch("stage4_5_round2_integrity_report.json")
  report = load_json(report_path)
  phases = report.fetch("phases")
  check("P#{id} Schema-5 required top-level fields") do
    (report.keys & %w[verdict mode phases overall_issues citation_integrity_score fabrication_risk_score timestamp]).length == 7 &&
      report.fetch("mode") == "final-check" && report.fetch("timestamp").start_with?("2026-08-31")
  end
  check("P#{id} Phase A denominator and zero failed refs") do
    a = phases.fetch("A_references")
    a.fetch("checked") == refs.length && a.fetch("passed") == refs.length && a.fetch("failed") == 0
  end
  check("P#{id} Phase B denominator and support") do
    b = phases.fetch("B_citation_context")
    b.fetch("sampled") == cites.length && b.fetch("verified") == cites.length && b.fetch("issues").empty?
  end
  check("P#{id} Phase C registered surfaces all verified") do
    c = phases.fetch("C_data")
    c.fetch("claims_checked").positive? && c.fetch("verified") == c.fetch("claims_checked") && c.fetch("issues").empty?
  end
  check("P#{id} Phase D completed without blocking issue") do
    d = phases.fetch("D_originality")
    d.fetch("checked") == true && d.fetch("issues").none? { |row| %w[CRITICAL SERIOUS MODERATE].include?(row["severity"]) }
  end
  check("P#{id} Phase E complete population and pointers") do
    e = phases.fetch("E_claims")
    pointer = e.fetch("claim_registry_coverage")
    drift_pointer = e.fetch("claim_strength_drift_findings")
    e.fetch("checked") == claims.length &&
      e.fetch("verified") == claims.length &&
      e.fetch("distortions").empty? &&
      e.fetch("evidence_rows") == evidence_rows &&
      pointer.fetch("status") == "completed" &&
      pointer.fetch("registry_schema_version") == "claim-registry/1.0" &&
      pointer.fetch("candidate_unregistered_count") == 0 &&
      pointer.fetch("draft_raw_sha256") == sha256(draft) &&
      pointer.fetch("registry_raw_sha256") == sha256(registry_path) &&
      pointer.fetch("report_sha256") == sha256(coverage_path) &&
      drift_pointer.fetch("artifact_path").end_with?(drift_path.basename.to_s) &&
      drift_pointer.fetch("artifact_sha256") == sha256(drift_path)
  end

  issues = report.fetch("overall_issues")
  verdict = report.fetch("verdict")
  check("P#{id} verdict/issue-count consistency") do
    case verdict
    when "PASS"
      issues.values.all?(&:zero?) && drift.fetch("findings").empty?
    when "PASS_WITH_CONDITIONS"
      issues.fetch("SERIOUS").zero? && issues.fetch("MEDIUM").zero? && issues.fetch("MINOR").positive?
    when "FAIL"
      issues.fetch("SERIOUS").positive? || issues.fetch("MEDIUM").positive? || !drift.fetch("findings").empty?
    else
      false
    end
  end

  passport = load_json(paths.fetch("stage4_5_round2_material_passport.json"))
  passport_text = JSON.generate(passport)
  check("P#{id} passport required lineage and experiment declaration") do
    %w[origin_skill origin_mode origin_date verification_status version_label repro_lock].all? { |key| passport.key?(key) } &&
      passport.dig("experiment_intake_declaration", "status") == "experiments_declared" &&
      passport_text.include?(sha256(draft)) && passport_text.include?(sha256(report_path))
  end

  receipt = load_json(paths.fetch("stage4_5_round2_preview_build_receipt.json"))
  receipt_text = JSON.generate(receipt)
  check("P#{id} isolated preview receipt binds inputs and successful build") do
    receipt_text.include?(sha256(draft)) && receipt_text.include?(sha256(bib)) &&
      (receipt_text.match?(/(?:exit_code|return_code)\D*0/) ||
        (receipt["status"] == "PASS" && receipt["isolated_build"] == true)) &&
      !receipt_text.match?(/canonical[^\n]{0,80}(?:promoted|refreshed)[^\n]{0,20}true/i)
  end

  final_text = File.read(paths.fetch("stage4_5_round2_final_integrity_report.md"), encoding: "UTF-8")
  final_plain = final_text.delete("*")
  check("P#{id} final report preserves Stage-5 checkpoint and Route state") do
    final_text.include?(verdict) && final_plain.match?(/Stage 5[^\n]*(?:closed|not|未)/i) &&
      final_plain.match?(/(?:A2[^\n]*0\/5|0\/5[^\n]*A2)/i) &&
      final_plain.match?(/Route[- ]B[^\n]*0\/5/i)
  end

  gate_open = verdict == "PASS" && drift.fetch("findings").empty?
  @gate_rows << {paper_id: id, verdict: verdict, stage4_5_pass: gate_open, claims: claims.length, evidence_rows: evidence_rows.length}
end

puts
puts "Batch gate rows:"
@gate_rows.each do |row|
  puts "P#{row[:paper_id]} #{row[:verdict]} claims=#{row[:claims]} evidence_rows=#{row[:evidence_rows]} stage4_5_pass=#{row[:stage4_5_pass]}"
end

puts
puts "Checks passed: #{@pass_count}"
if @failures.empty?
  puts "ROUND9_STAGE4_5_ROUND2_AUDIT_PASS"
  exit 0
end

warn "Checks failed: #{@failures.length}"
@failures.each { |failure| warn "- #{failure}" }
exit 1
