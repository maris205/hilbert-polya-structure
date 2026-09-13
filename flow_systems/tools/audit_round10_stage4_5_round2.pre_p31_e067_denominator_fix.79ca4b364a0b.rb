#!/usr/bin/env ruby
# frozen_string_literal: true

# Independent, read-only replay for Round 10 Papers 29--33, Stage 4.5
# Round 2.  The replay deliberately derives the batch decision from the
# current evidence and blocking findings.  A package/coherence PASS is never
# treated as an academic-integrity PASS.

require "digest"
require "find"
require "json"
require "open3"
require "pathname"

ROOT = Pathname.new(__dir__).parent.expand_path
LOCK_PATH = ROOT / "BATCH_ROUND10_STAGE4_5_ROUND2_INPUT_LOCK.json"
AUTH_RECORD_PATH = ROOT / "BATCH_ROUND10_STAGE4_5_ROUND2_AUTHORIZATION_RECORD.md"
AUTH_RECEIPT_PATH = ROOT / "BATCH_ROUND10_STAGE4_5_ROUND2_AUTHORIZATION_RECEIPT.json"
ARS_ROOT = Pathname.new(
  "/root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/0.1.28/" \
  "skills/academic-research-suite/ars"
)

EXPECTED_LOCK_SHA = "11875bf33e0318997c385d0d89bde3a7987bb9166b18967994ccb3ca5ac44bb0"
EXPECTED_AUTH_RECORD_SHA = "e9505895fe78e2910ff32c4c97d4e7c42abf2fc1f63b25ca7170cb17477dd06d"
EXPECTED_AUTH_RECEIPT_SHA = "139631992e610beb9ffc2e5b72c1ee5022bed87460d95b3c5da7812dd3b2db60"

CURRENT_AUDIT_EXECUTION_ENTRYPOINT =
  "tools/audit_round10_stage4_5_round2.rb#FULL_BATCH_REPLAY"
CURRENT_AUDIT_EXECUTION_ASSERTION =
  "VALIDATOR_IS_EXECUTING_THE_FULL_EXACT_AUTHORITY_ROUND10_STAGE4_5_ROUND2_REPLAY"
CURRENT_AUDIT_EXECUTION_SCOPE = {
  "paper_id" => "P30",
  "claim_id" => "P30-S45R2-E1-107",
  "component_id" => "P30-S45R2-E1-107:current_round2_audit_execution"
}.freeze
CURRENT_AUDIT_DRAFT = {
  "repo_path" => "papers/30-three-disk-nonconstant-roof-determinant/notes/stage4_prime_revision_round3.tex",
  "sha256" => "509e9f45b798ad2257acf2f62db81f95a43e3c574da8f1ba7e654c9fa9d21ead",
  "bytes" => 71_520
}.freeze
CURRENT_AUTH_RECORD = {
  "repo_path" => "BATCH_ROUND10_STAGE4_5_ROUND2_AUTHORIZATION_RECORD.md",
  "sha256" => EXPECTED_AUTH_RECORD_SHA,
  "bytes" => 1_674
}.freeze
CURRENT_AUTH_RECEIPT = {
  "repo_path" => "BATCH_ROUND10_STAGE4_5_ROUND2_AUTHORIZATION_RECEIPT.json",
  "sha256" => EXPECTED_AUTH_RECEIPT_SHA,
  "bytes" => 1_203
}.freeze
CURRENT_INPUT_LOCK = {
  "repo_path" => "BATCH_ROUND10_STAGE4_5_ROUND2_INPUT_LOCK.json",
  "sha256" => EXPECTED_LOCK_SHA,
  "bytes" => 45_264
}.freeze

PAPERS = {
  "P29" => "29-bianchi-ideal-owner-refinement",
  "P30" => "30-three-disk-nonconstant-roof-determinant",
  "P31" => "31-level11-conjugacy-owner-ledger",
  "P32" => "32-homology-cover-renormalization-uniformity",
  "P33" => "33-bolza-control-matched-census"
}.freeze

# The Stage-2 lineage predates path-bearing artifact descriptors for exactly
# these four P31 links.  Each legacy witness records an unambiguous SHA field;
# the child path is therefore derived from a frozen, rule-specific canonical
# path.  No other SHA-only path derivation is accepted.
P31_CANONICAL_SHA_FIELD_DERIVATIONS = {
  "FIELD_NAME_TO_ROOT_STAGE2_OUTPUT_MANIFEST" => {
    "sha_field" => "stage2_output_manifest_sha256",
    "parent_artifact" => {
      "repo_path" => "BATCH_ROUND10_STAGE2_5_INPUT_FREEZE.json",
      "sha256" => "8da3f9b70f09d0f7555ce3e233eeddb81c7250b726a8871d0f76fa2aa053907e",
      "bytes" => 6_682
    },
    "child_artifact" => {
      "repo_path" => "BATCH_ROUND10_STAGE2_OUTPUT_MANIFEST.json",
      "sha256" => "b023d9b91e18580bc9921be56c1ab0fb0c6723575305baae1a7f330eb1907bfa",
      "bytes" => 9_289
    },
    "span" => [615, 714],
    "paper_id" => nil,
    "slug" => nil,
    "basename" => "BATCH_ROUND10_STAGE2_OUTPUT_MANIFEST.json",
    "scope_after" => nil,
    "scope_before" => nil
  },
  "FIELD_NAME_TO_ROOT_STAGE2_INPUT_FREEZE" => {
    "sha_field" => "input_freeze_sha256",
    "parent_artifact" => {
      "repo_path" => "BATCH_ROUND10_STAGE2_OUTPUT_MANIFEST.json",
      "sha256" => "b023d9b91e18580bc9921be56c1ab0fb0c6723575305baae1a7f330eb1907bfa",
      "bytes" => 9_289
    },
    "child_artifact" => {
      "repo_path" => "BATCH_ROUND10_STAGE2_INPUT_FREEZE.json",
      "sha256" => "923339d65d4fd073483d01d54cdf8eb4e1e0e540d944dae7aaf1198db9f2212c",
      "bytes" => 5_702
    },
    "span" => [251, 340],
    "paper_id" => nil,
    "slug" => nil,
    "basename" => "BATCH_ROUND10_STAGE2_INPUT_FREEZE.json",
    "scope_after" => nil,
    "scope_before" => nil
  },
  "PAPER_SLUG_PHASE6_MANIFEST" => {
    "sha_field" => "phase6_manifest_sha256",
    "parent_artifact" => {
      "repo_path" => "BATCH_ROUND10_STAGE2_INPUT_FREEZE.json",
      "sha256" => "923339d65d4fd073483d01d54cdf8eb4e1e0e540d944dae7aaf1198db9f2212c",
      "bytes" => 5_702
    },
    "child_artifact" => {
      "repo_path" => "papers/31-level11-conjugacy-owner-ledger/notes/stage1_phase6_claim_intent_manifest.json",
      "sha256" => "b9a61badd7e6d05c31ae0ce4f81adfa6ea1c40269afe37de9a620c763597aa38",
      "bytes" => 6_905
    },
    "span" => [3_121, 3_213],
    "paper_id" => "P31",
    "slug" => "31-level11-conjugacy-owner-ledger",
    "basename" => "stage1_phase6_claim_intent_manifest.json",
    "scope_after" => "\"paper\": \"P31\"",
    "scope_before" => "\"paper\": \"P32\""
  },
  "PAPER_SLUG_PHASE6_REPORT" => {
    "sha_field" => "phase6_report_sha256",
    "parent_artifact" => {
      "repo_path" => "BATCH_ROUND10_STAGE2_INPUT_FREEZE.json",
      "sha256" => "923339d65d4fd073483d01d54cdf8eb4e1e0e540d944dae7aaf1198db9f2212c",
      "bytes" => 5_702
    },
    "child_artifact" => {
      "repo_path" => "papers/31-level11-conjugacy-owner-ledger/notes/stage1_phase6_final_report.md",
      "sha256" => "bb674098ead518a44ab1e8e57cd63599549cc8035d54fddda924926c20560f61",
      "bytes" => 34_198
    },
    "span" => [3_023, 3_113],
    "paper_id" => "P31",
    "slug" => "31-level11-conjugacy-owner-ledger",
    "basename" => "stage1_phase6_final_report.md",
    "scope_after" => "\"paper\": \"P31\"",
    "scope_before" => "\"paper\": \"P32\""
  }
}.freeze

EXPECTED_DRAFT_SHA = {
  "P29" => "009ae2e9b30cb087902c7fbb9d01226bc544ce536da8ebf40f244e7b07d817ae",
  "P30" => "509e9f45b798ad2257acf2f62db81f95a43e3c574da8f1ba7e654c9fa9d21ead",
  "P31" => "733e37dfe4e7377a711ade04f7bc6d902b311e2ded48211331d70506735d2729",
  "P32" => "b43c5cb6c7770dd80600e1ee64a8e23d17ffc2ceb39e9fcb625ff2b6c5f692fd",
  "P33" => "40ff6a91c311e7bdd01d6a37bfdd3bd351073311d7781bd4074f0975362e60ce"
}.freeze

EXPECTED_REFERENCE_COUNTS = {"P29" => 22, "P30" => 28, "P31" => 24, "P32" => 30, "P33" => 22}.freeze
EXPECTED_CONTEXT_COUNTS = {"P29" => 22, "P30" => 30, "P31" => 26, "P32" => 30, "P33" => 48}.freeze

EXPECTED_ROUTE = {
  "formal_route_a_tuples" => "0/5",
  "positive_arithmetic_A2" => "0/5",
  "A3" => "0/5",
  "A4" => "0/5",
  "route_b_invocations" => "0/5"
}.freeze

# Measured at the root independent replay boundary before any final package
# promotion.  P29/P32 are also independently bound by their per-paper input
# manifests; these rows make the no-README/no-status write boundary explicit
# for the whole batch.
READONLY_TEXT_BOUNDARIES = {
  "README.md" => "607d1beea7a92d3dd86b1d5dae66a3d783c1a903ad5e7b81dd85d9a9181f2986",
  "papers/29-bianchi-ideal-owner-refinement/README.md" => "6305e67a774760e68cb040abd77d5ea9924bb0763ce5c2c1a5b74bb444054144",
  "papers/29-bianchi-ideal-owner-refinement/notes/pipeline_state.md" => "02fe22c353cda2d963d2e44cbe5ff03ef1ad1188f810a58f0685c006a9f03366",
  "papers/29-bianchi-ideal-owner-refinement/paper/README.md" => "ccd6ecb0a62565eea069423e18de611ae14cca1f811c9feb3bd7832abcc87bfe",
  "papers/30-three-disk-nonconstant-roof-determinant/README.md" => "bdfa23343c3c0a977c394076535dc397a378a181091f580d30d6ed10d873a7ed",
  "papers/30-three-disk-nonconstant-roof-determinant/notes/pipeline_state.md" => "aae88c2dd67d592871e8dcca44e2f8366dc7505cb9f3838dd1e9681e7708bc4c",
  "papers/30-three-disk-nonconstant-roof-determinant/paper/README.md" => "fca74db30aee0ec5388f2a0190e5a8f66b54df62b261023d53fb6cf9ad75abdc",
  "papers/31-level11-conjugacy-owner-ledger/README.md" => "a6d52c892cc5b64ed58ded16bcf9895f2659635be03a2ef058d7107c4df35507",
  "papers/31-level11-conjugacy-owner-ledger/notes/pipeline_state.md" => "e4424e51f38dac494877dc29e07acd28fab6bb835ba4206c3d53ec71a6a6a10d",
  "papers/31-level11-conjugacy-owner-ledger/paper/README.md" => "8d700ad690a0f6bd0c1d1689380332489ddcf6f0017f864a5b0c76a55ffe6674",
  "papers/32-homology-cover-renormalization-uniformity/README.md" => "0cc9ee2cb5ca093497f0d4faf0ff2b62ce5cc609a8a540555aa59236e63254f0",
  "papers/32-homology-cover-renormalization-uniformity/notes/pipeline_state.md" => "6a207e222f96972332721f6a754fdd159a267248878c7cb75c33e2601b7eaee8",
  "papers/32-homology-cover-renormalization-uniformity/paper/README.md" => "fbf6c79912292ad5b0b335a6839d78c5446a855c1d0150548119b19429ba2ce5",
  "papers/33-bolza-control-matched-census/README.md" => "87efa649902b6801132706a3144f6e7311069c3d5c2bb768c0bd86945efd4499",
  "papers/33-bolza-control-matched-census/notes/pipeline_state.md" => "eaa673b6ab52e9fd3ff01058bd4240aae709e2a14e063aaf18efce01b6d34d55",
  "papers/33-bolza-control-matched-census/paper/README.md" => "4e7f85dafc09ee82d85d8c640cd1e21b8bef10c18ddd330f33b2f383e6b5f321"
}.freeze

EXPECTED_COMPLIANCE = {
  "P29" => ["primary_research", nil, "principles_only"],
  "P30" => ["other_evidence_synthesis", :present, "full"],
  "P31" => ["other_evidence_synthesis", :present, "full"],
  "P32" => ["primary_research", nil, "principles_only"],
  "P33" => ["other_evidence_synthesis", :present, "full"]
}.freeze

@checks = 0
@failures = []
@paper_rows = {}
@full_batch_replay_active = false
@current_paper_id = nil

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

def expect(condition, message = "expectation was false")
  raise message unless condition

  true
end

def diagnostic_value(value)
  if value.is_a?(String) && value.bytesize > 240
    return "<String bytes=#{value.bytesize} sha256=#{Digest::SHA256.hexdigest(value.b)}>"
  end
  value.inspect
end

def equal(actual, expected, context)
  return true if actual == expected

  raise "#{context}: #{diagnostic_value(actual)} != #{diagnostic_value(expected)}"
end

def check(label)
  yield
  @checks += 1
  puts "PASS #{label}"
rescue StandardError => e
  @failures << "#{label}: #{e.message}"
  warn "FAIL #{label}: #{e.message}"
end

def run_command(label, *argv)
  stdout, stderr, status = Open3.capture3(*argv, chdir: ROOT.to_s)
  return stdout if status.success?

  raise "#{label} exit #{status.exitstatus}: #{[stdout, stderr].join("\n").strip}"
end

def verify_binding(row, label = nil)
  path_value = row["path"]
  expect(path_value.is_a?(String) && !path_value.empty?, "binding path absent")
  path = (ROOT / path_value).cleanpath
  expect(path.to_s.start_with?("#{ROOT}#{File::SEPARATOR}"), "path escapes root: #{path_value}")
  expect(path.file?, "missing regular file: #{path_value}")
  expect(!path.symlink?, "symlink forbidden: #{path_value}")
  equal(path.size, row.fetch("bytes"), "#{label || path_value} bytes")
  equal(sha256(path), row.fetch("sha256"), "#{label || path_value} SHA-256")
  path
end

def descriptor_path(descriptor)
  descriptor["path"] || descriptor["repo_path"]
end

def normalized_descriptor(descriptor)
  {
    "path" => descriptor_path(descriptor),
    "sha256" => descriptor.fetch("sha256"),
    "bytes" => descriptor.fetch("bytes")
  }
end

def verify_descriptor(descriptor, label = nil)
  verify_binding(normalized_descriptor(descriptor), label)
end

def verify_package_binding(row, paper_root, label = nil)
  path_value = row["path"]
  expect(path_value.is_a?(String) && !path_value.empty?, "binding path absent")
  base = path_value.start_with?("notes/", "paper/") ? paper_root : ROOT
  path = (base / path_value).cleanpath
  expect(path.to_s.start_with?("#{base}#{File::SEPARATOR}"), "path escapes package base: #{path_value}")
  expect(path.file?, "missing regular file: #{rel(path)}")
  expect(!path.symlink?, "symlink forbidden: #{rel(path)}")
  equal(path.size, row.fetch("bytes"), "#{label || rel(path)} bytes")
  equal(sha256(path), row.fetch("sha256"), "#{label || rel(path)} SHA-256")
  path
end

def span_bounds(span)
  return [nil, nil] unless span.is_a?(Hash)

  [span["start"] || span["start_byte"], span["end"] || span["end_byte"]]
end

def canonical_json(value)
  case value
  when Hash
    "{" + value.keys.sort.map { |key| "#{JSON.generate(key)}:#{canonical_json(value.fetch(key))}" }.join(",") + "}"
  when Array
    "[" + value.map { |child| canonical_json(child) }.join(",") + "]"
  else
    JSON.generate(value)
  end
end

def same_descriptor?(left, right)
  normalized_descriptor(left) == normalized_descriptor(right)
end

def replay_p31_canonical_sha_field_derivation_hop(hop, chain_type, dependency_context)
  expected_hop_keys = %w[
    binding_kind child_artifact parent_artifact path_derivation raw_excerpt
    raw_excerpt_sha256 raw_utf8_span scope_after scope_before sha_field
  ]
  equal(hop.keys.sort, expected_hop_keys.sort, "canonical SHA-field hop keys")
  equal(chain_type, "TRANSITIVE_SHA_BINDING", "canonical SHA-field chain type")
  expect(dependency_context.is_a?(Hash), "canonical SHA-field dependency context absent")
  claim_id = dependency_context.fetch("claim_id")
  component_id = dependency_context.fetch("component_id")
  expect(claim_id.match?(/\AP31-S45R2-E1-\d{3}\z/), "canonical SHA-field rule used outside P31")
  expect(component_id.start_with?("#{claim_id}:"), "canonical SHA-field component/claim mismatch")

  derivation = hop.fetch("path_derivation")
  equal(derivation.keys.sort, %w[paper_id resolved_repo_path rule slug].sort,
        "canonical path-derivation keys")
  rule = derivation.fetch("rule")
  spec = P31_CANONICAL_SHA_FIELD_DERIVATIONS[rule]
  expect(!spec.nil?, "unsupported canonical SHA-field derivation rule #{rule.inspect}")

  equal(hop.fetch("binding_kind"), "SHA_FIELD_WITH_CANONICAL_PATH_DERIVATION",
        "canonical SHA-field binding kind")
  equal(hop.fetch("sha_field"), spec.fetch("sha_field"), "canonical SHA-field name")
  equal(normalized_descriptor(hop.fetch("parent_artifact")),
        normalized_descriptor(spec.fetch("parent_artifact")), "canonical SHA-field parent")
  equal(normalized_descriptor(hop.fetch("child_artifact")),
        normalized_descriptor(spec.fetch("child_artifact")), "canonical SHA-field child")
  equal(span_bounds(hop.fetch("raw_utf8_span")), spec.fetch("span"),
        "canonical SHA-field witness span")
  equal(hop.fetch("scope_after"), spec.fetch("scope_after"), "canonical SHA-field scope-after")
  equal(hop.fetch("scope_before"), spec.fetch("scope_before"), "canonical SHA-field scope-before")

  derived_path = if spec.fetch("paper_id")
                   "papers/#{PAPERS.fetch('P31')}/notes/#{spec.fetch('basename')}"
                 else
                   spec.fetch("basename")
                 end
  equal(derivation.fetch("paper_id"), spec.fetch("paper_id"), "canonical derivation paper")
  equal(derivation.fetch("slug"), spec.fetch("slug"), "canonical derivation slug")
  equal(derivation.fetch("resolved_repo_path"), derived_path, "canonical derived path")
  equal(descriptor_path(hop.fetch("child_artifact")), derived_path, "canonical child path")
  equal(File.basename(derived_path), spec.fetch("basename"), "canonical child basename")

  expected_excerpt =
    "\"#{spec.fetch('sha_field')}\": \"#{spec.dig('child_artifact', 'sha256')}\""
  equal(hop.fetch("raw_excerpt"), expected_excerpt, "canonical SHA-field witness")
  expect(hop.fetch("raw_excerpt").include?(spec.fetch("sha_field")),
         "canonical witness omits exact SHA field")
  expect(hop.fetch("raw_excerpt").include?(spec.dig("child_artifact", "sha256")),
         "canonical witness omits child digest")
  true
end

def validator_self_descriptor
  path = Pathname.new(__FILE__).expand_path
  {
    "repo_path" => rel(path),
    "sha256" => sha256(path),
    "bytes" => path.size
  }
end

def replay_current_authorized_audit_execution(chain, target_descriptor, dependency_context)
  expected_keys = %w[
    audit_draft authorization_record authorization_receipt claim_id component_id
    entrypoint input_lock paper_id runtime_assertion type validator
  ]
  equal(chain.keys.sort, expected_keys.sort, "current-audit execution chain keys")
  expect(@full_batch_replay_active == true, "current-audit execution used outside full replay")
  equal(@current_paper_id, "P30", "current-audit runtime paper")
  expect(dependency_context.is_a?(Hash), "current-audit dependency context absent")
  CURRENT_AUDIT_EXECUTION_SCOPE.each do |key, value|
    equal(chain.fetch(key), value, "current-audit chain #{key}")
  end
  %w[claim_id component_id].each do |key|
    equal(dependency_context.fetch(key), CURRENT_AUDIT_EXECUTION_SCOPE.fetch(key),
          "current-audit dependency #{key}")
  end
  equal(chain.fetch("entrypoint"), CURRENT_AUDIT_EXECUTION_ENTRYPOINT,
        "current-audit entrypoint")
  equal(chain.fetch("runtime_assertion"), CURRENT_AUDIT_EXECUTION_ASSERTION,
        "current-audit runtime assertion")

  equal(normalized_descriptor(chain.fetch("audit_draft")), normalized_descriptor(CURRENT_AUDIT_DRAFT),
        "current-audit frozen draft")
  equal(normalized_descriptor(chain.fetch("authorization_record")),
        normalized_descriptor(CURRENT_AUTH_RECORD), "current-audit authorization record")
  equal(normalized_descriptor(chain.fetch("authorization_receipt")),
        normalized_descriptor(CURRENT_AUTH_RECEIPT), "current-audit authorization receipt")
  equal(normalized_descriptor(chain.fetch("input_lock")), normalized_descriptor(CURRENT_INPUT_LOCK),
        "current-audit input lock")
  equal(normalized_descriptor(chain.fetch("validator")), normalized_descriptor(validator_self_descriptor),
        "current-audit validator")
  expect(same_descriptor?(target_descriptor, chain.fetch("authorization_record")),
         "current-audit dependency target must be the exact authorization record")

  %w[audit_draft authorization_record authorization_receipt input_lock validator].each do |name|
    verify_descriptor(chain.fetch(name), "current-audit #{name}")
  end

  receipt = load_json(AUTH_RECEIPT_PATH)
  equal(receipt.fetch("status"), "AUTHORIZED_AUDIT_ONLY", "current-audit authority status")
  equal(receipt.fetch("authorized_action"), "fresh Stage 4.5 Mode-2 integrity audit from scratch",
        "current-audit authorized action")
  equal(receipt.fetch("authorized_papers"), PAPERS.keys, "current-audit authorized papers")
  equal(receipt.fetch("repairs_authorized"), false, "current-audit repair authority")
  equal(receipt.fetch("stage5_authorized"), false, "current-audit Stage 5 authority")
  expect(same_descriptor?(receipt.fetch("authorization_record"), chain.fetch("authorization_record")),
         "current-audit receipt/record mismatch")
  expect(same_descriptor?(receipt.fetch("input_lock"), chain.fetch("input_lock")),
         "current-audit receipt/lock mismatch")

  current_lock = load_json(LOCK_PATH)
  locked_descriptors = binding_rows(current_lock)
  expect(locked_descriptors.any? do |row|
    same_descriptor?(row, chain.fetch("authorization_record"))
  end, "current-audit authorization record absent from input lock")
  p30_lock = current_lock.fetch("papers").find { |row| row["paper_id"] == "P30" }
  expect(p30_lock && same_descriptor?(p30_lock.fetch("audit_draft"), chain.fetch("audit_draft")),
         "current-audit P30 draft absent from input lock")
  true
end

def replay_dependency_binding_chain(chain, target_descriptor, dependency_context = nil)
  expect(chain.is_a?(Hash), "dependency binding chain absent")
  chain_type = chain.fetch("type")
  verify_descriptor(target_descriptor, "dependency target")

  # P30/P31 encode top-level and transitive closure as a contiguous hop list.
  if chain["hops"].is_a?(Array)
    expect(%w[TOP_LEVEL_INPUT_LOCK TRANSITIVE_SHA_BINDING].include?(chain_type),
           "unsupported hop-list chain type #{chain_type}")
    hops = chain.fetch("hops")
    expect(!hops.empty?, "empty dependency binding hop list")
    equal(normalized_descriptor(hops.first.fetch("parent_artifact")),
          normalized_descriptor(CURRENT_INPUT_LOCK),
          "dependency hop list is not rooted at the exact current input lock")
    previous_child = nil
    hops.each do |hop|
      parent = hop.fetch("parent_artifact")
      child = hop.fetch("child_artifact")
      parent_path = verify_descriptor(parent, "binding parent")
      verify_descriptor(child, "binding child")
      start_byte, end_byte = span_bounds(hop.fetch("raw_utf8_span"))
      raw = File.binread(parent_path)
      expect(start_byte.is_a?(Integer) && end_byte.is_a?(Integer) &&
             start_byte >= 0 && end_byte > start_byte && end_byte <= raw.bytesize,
             "invalid binding witness span")
      excerpt_raw = raw.byteslice(start_byte...end_byte)
      equal(excerpt_raw.force_encoding("UTF-8"), hop.fetch("raw_excerpt"), "binding witness text")
      equal(Digest::SHA256.hexdigest(excerpt_raw), hop.fetch("raw_excerpt_sha256"), "binding witness digest")
      if hop["binding_kind"] == "SHA_FIELD_WITH_CANONICAL_PATH_DERIVATION"
        replay_p31_canonical_sha_field_derivation_hop(hop, chain_type, dependency_context)
      else
        expect(!hop.key?("path_derivation") && !hop.key?("sha_field"),
               "canonical path-derivation metadata used without its exact binding kind")
        expect(hop.fetch("raw_excerpt").include?(descriptor_path(child)) ||
               hop.fetch("raw_excerpt").include?(File.basename(descriptor_path(child))),
               "binding witness omits child path")
        expect(hop.fetch("raw_excerpt").include?(child.fetch("sha256")), "binding witness omits child digest")
      end
      expect(previous_child.nil? || same_descriptor?(parent, previous_child), "non-contiguous binding chain")
      previous_child = child
    end
    expect(previous_child && same_descriptor?(previous_child, target_descriptor),
           "binding chain does not terminate at dependency")
    return true
  end

  case chain_type
  when "TOP_LEVEL_INPUT_LOCK"
    lock_descriptor = chain.fetch("input_lock")
    locked = chain.fetch("locked_artifact")
    expect(same_descriptor?(locked, target_descriptor), "top-level target mismatch")
    lock_path = verify_descriptor(lock_descriptor, "dependency input lock")
    equal(lock_descriptor.fetch("sha256"), EXPECTED_LOCK_SHA, "dependency lock digest")
    start_byte, end_byte = span_bounds(chain.fetch("lock_raw_utf8_span"))
    raw = File.binread(lock_path)
    expect(start_byte.is_a?(Integer) && end_byte.is_a?(Integer) &&
           start_byte >= 0 && end_byte > start_byte && end_byte <= raw.bytesize,
           "invalid input-lock witness span")
    excerpt_raw = raw.byteslice(start_byte...end_byte)
    equal(excerpt_raw.force_encoding("UTF-8"), chain.fetch("lock_raw_excerpt"), "input-lock witness text")
    equal(Digest::SHA256.hexdigest(excerpt_raw), chain.fetch("lock_raw_excerpt_sha256"),
          "input-lock witness digest")
    unless same_descriptor?(locked, lock_descriptor)
      expect(chain.fetch("lock_raw_excerpt").include?(descriptor_path(locked)), "input-lock witness omits path")
      expect(chain.fetch("lock_raw_excerpt").include?(locked.fetch("sha256")), "input-lock witness omits digest")
    end
  when "TRANSITIVE_SHA_BINDING"
    parent = chain.fetch("parent_artifact")
    child = chain.fetch("child_artifact")
    expect(same_descriptor?(child, target_descriptor), "transitive child mismatch")
    parent_path = verify_descriptor(parent, "transitive parent")
    start_byte, end_byte = span_bounds(chain.fetch("parent_raw_utf8_span"))
    raw = File.binread(parent_path)
    expect(start_byte.is_a?(Integer) && end_byte.is_a?(Integer) &&
           start_byte >= 0 && end_byte > start_byte && end_byte <= raw.bytesize,
           "invalid transitive witness span")
    excerpt_raw = raw.byteslice(start_byte...end_byte)
    equal(excerpt_raw.force_encoding("UTF-8"), chain.fetch("parent_raw_excerpt"),
          "transitive witness text")
    equal(Digest::SHA256.hexdigest(excerpt_raw), chain.fetch("parent_raw_excerpt_sha256"),
          "transitive witness digest")
    normalized = chain["normalization"] == "REMOVE_LITERAL_TEX_ALLOWBREAK_COMMANDS" ?
      chain.fetch("parent_raw_excerpt").gsub("\\allowbreak{}", "") : chain.fetch("parent_raw_excerpt")
    expect(normalized.include?(descriptor_path(child)) || normalized.include?(File.basename(descriptor_path(child))),
           "transitive witness omits normalized child path")
    expect(normalized.include?(child.fetch("sha256")), "transitive witness omits normalized child digest")
    replay_dependency_binding_chain(chain.fetch("parent_binding_chain"), parent, dependency_context)
  when "FRESH_AUTHORIZED_RETRIEVAL_PROVENANCE"
    %w[authorization_receipt input_lock collector_script retrieval_artifact].each do |name|
      verify_descriptor(chain.fetch(name), "fresh retrieval #{name}")
    end
    equal(chain.dig("authorization_receipt", "sha256"), EXPECTED_AUTH_RECEIPT_SHA,
          "fresh retrieval authority")
    equal(chain.dig("input_lock", "sha256"), EXPECTED_LOCK_SHA, "fresh retrieval input lock")
    expect(same_descriptor?(chain.fetch("retrieval_artifact"), target_descriptor),
           "fresh retrieval target mismatch")
    collector_path = verify_descriptor(chain.fetch("collector_script"), "fresh retrieval collector")
    witness = chain.fetch("collector_authority_witness")
    start_byte, end_byte = span_bounds(witness.fetch("raw_utf8_span"))
    collector_raw = File.binread(collector_path)
    excerpt_raw = collector_raw.byteslice(start_byte...end_byte)
    equal(excerpt_raw.force_encoding("UTF-8"), witness.fetch("raw_excerpt"),
          "collector authority witness")
    equal(Digest::SHA256.hexdigest(excerpt_raw), witness.fetch("raw_excerpt_sha256"),
          "collector authority witness digest")
    expect(witness.fetch("raw_excerpt").include?(EXPECTED_AUTH_RECEIPT_SHA),
           "collector witness omits authority digest")
    events = chain.fetch("retrieval_events")
    expect(events.is_a?(Array) && !events.empty?, "fresh retrieval events absent")
    events.each do |event|
      equal(event.fetch("request_method"), "GET", "fresh request method")
      equal(event.fetch("http_status"), 200, "fresh HTTP status")
      expect(event.fetch("request_url").start_with?("https://"), "fresh request URL is not HTTPS")
      expect(event.fetch("response_bytes").positive?, "fresh response byte count")
      expect(event.fetch("response_sha256").match?(/\A[0-9a-f]{64}\z/), "fresh response digest")
      message_raw = canonical_json(event.fetch("embedded_crossref_message")).encode("UTF-8")
      equal(Digest::SHA256.hexdigest(message_raw), event.fetch("embedded_crossref_message_sha256"),
            "embedded Crossref message digest")
    end
  when "CURRENT_AUTHORIZED_AUDIT_EXECUTION"
    replay_current_authorized_audit_execution(chain, target_descriptor, dependency_context)
  else
    raise "unsupported dependency binding-chain type #{chain_type}"
  end
  true
end

def component_verdict(value)
  return "MAJOR_DISTORTION" if value == "MAJOR_DISTORTION" || value.start_with?("CONTRADICT") ||
                                value.start_with?("MAJOR_DISTORTION")
  return "UNVERIFIABLE" if value.start_with?("UNVERIFIABLE")
  return "MINOR_DISTORTION" if value.start_with?("MINOR_DISTORTION")
  return "VERIFIED" if value == "VERIFIED" || value.start_with?("VERIFIED") ||
                       value.start_with?("EXACT_SURFACE_PRESENT")

  raise "unknown component verdict #{value.inspect}"
end

def weakest_verdict(values)
  rank = {"VERIFIED" => 0, "MINOR_DISTORTION" => 1, "UNVERIFIABLE" => 2,
          "UNVERIFIABLE_ACCESS" => 2, "MAJOR_DISTORTION" => 3}
  values.max_by { |value| rank.fetch(value) }
end

def count_values(values)
  values.each_with_object(Hash.new(0)) { |value, out| out[value] += 1 }.sort.to_h
end

def verify_dependency_catalog(catalog, evidence, source_map)
  raw_dependencies = catalog.fetch("dependencies")
  missing_dependencies = catalog["missing_dependencies"] || raw_dependencies.select { |row| row["artifact"].nil? }
  raw_dependencies = raw_dependencies.reject { |row| row["artifact"].nil? }
  all_dependencies = raw_dependencies + missing_dependencies
  ids = all_dependencies.map { |row| row.fetch("evidence_row_id") }
  equal(ids.uniq.length, ids.length, "unique catalog evidence-row IDs")
  evidence_by_id = evidence.to_h { |row| [row.fetch("row_id"), row] }
  equal(evidence_by_id.length, evidence.length, "unique evidence-row IDs for catalog replay")

  raw_dependencies.each do |dependency|
    artifact = dependency.fetch("artifact")
    path = verify_descriptor(artifact, "raw dependency")
    raw = File.binread(path)
    start_byte, end_byte = span_bounds(dependency.fetch("raw_utf8_span"))
    expect(start_byte.is_a?(Integer) && end_byte.is_a?(Integer) &&
           start_byte >= 0 && end_byte > start_byte && end_byte <= raw.bytesize,
           "invalid raw dependency span #{dependency['component_id']}")
    excerpt_raw = raw.byteslice(start_byte...end_byte)
    equal(excerpt_raw.force_encoding("UTF-8"), dependency.fetch("raw_excerpt"),
          "raw dependency text #{dependency['component_id']}")
    equal(Digest::SHA256.hexdigest(excerpt_raw), dependency.fetch("raw_excerpt_sha256"),
          "raw dependency digest #{dependency['component_id']}")
    row = evidence_by_id.fetch(dependency.fetch("evidence_row_id"))
    equal(row.dig("claim", "claim_id"), dependency.fetch("claim_id"), "catalog claim join")
    equal(row["verdict"], dependency.fetch("claim_overall_verdict"), "catalog verdict join")
    equal(row.dig("source", "source_artifact_sha256"), artifact.fetch("sha256"), "catalog source join")
    equal(row.dig("excerpt", "text"), dependency.fetch("raw_excerpt"), "catalog excerpt join")
    equal(row.dig("excerpt", "excerpt_sha256"), dependency.fetch("raw_excerpt_sha256"),
          "catalog excerpt digest join")
    equal(span_bounds(row.dig("excerpt", "source_span_utf8")), [start_byte, end_byte],
          "catalog span join")
    source_slug = dependency["source_ref_slug"] || row.dig("source", "ref_slug")
    equal(row.dig("source", "ref_slug"), source_slug, "catalog source-slug join") if dependency["source_ref_slug"]
    equal(source_map.fetch(source_slug).b, raw, "source-map/raw dependency join")
    if dependency["raw_dependency_scope"].is_a?(Hash)
      scope = dependency.fetch("raw_dependency_scope")
      scope_start, scope_end = span_bounds(scope.fetch("utf8_span"))
      expect(scope_start.is_a?(Integer) && scope_end.is_a?(Integer) &&
             scope_start >= 0 && scope_end > scope_start && scope_end <= raw.bytesize,
             "invalid full dependency scope #{dependency['component_id']}")
      scope_raw = raw.byteslice(scope_start...scope_end)
      equal(scope_raw.bytesize, scope.fetch("bytes"), "dependency-scope bytes")
      equal(Digest::SHA256.hexdigest(scope_raw), scope.fetch("sha256"), "dependency-scope digest")
    end
    parsed_value = dependency["parsed_value"]
    if parsed_value.is_a?(Hash) && parsed_value["recomputed_sha256"]
      equal(parsed_value.fetch("recomputed_sha256"), artifact.fetch("sha256"),
            "complete-artifact recomputed digest")
      equal(parsed_value.fetch("bytes"), artifact.fetch("bytes"),
            "complete-artifact recomputed bytes") if parsed_value["bytes"]
    end
    replay_dependency_binding_chain(dependency.fetch("binding_chain"), artifact, dependency)
  end

  missing_dependencies.each do |dependency|
    row = evidence_by_id.fetch(dependency.fetch("evidence_row_id"))
    equal(row.dig("claim", "claim_id"), dependency.fetch("claim_id"), "missing dependency claim join")
    equal(row["verdict"], dependency.fetch("claim_overall_verdict"), "missing dependency verdict join")
    equal(row.dig("anchor", "kind"), "none", "missing dependency anchor")
    equal(row.dig("source", "source_artifact_sha256"), nil, "missing dependency source digest")
    equal(row.dig("excerpt", "state"), "anchorless", "missing dependency state")
    equal(row.dig("excerpt", "text"), nil, "missing dependency text")
    equal(row.dig("excerpt", "excerpt_sha256"), nil, "missing dependency excerpt digest")
    equal(row.dig("excerpt", "source_span_utf8"), nil, "missing dependency span")
    if dependency["binding_chain"]
      equal(dependency.dig("binding_chain", "type"), "MISSING_LOCKED_CARRIER", "missing chain type")
    end
    equal(component_verdict(dependency.fetch("component_semantic_verdict")), "UNVERIFIABLE",
          "missing component verdict")
  end

  joined_claim_ids = all_dependencies.map { |row| row.fetch("claim_id") }.uniq
  joined_evidence_ids = evidence.select { |row| joined_claim_ids.include?(row.dig("claim", "claim_id")) }
                                .map { |row| row.fetch("row_id") }
  equal(joined_evidence_ids.sort, ids.sort, "catalog/evidence reverse join")

  component_counts = count_values(all_dependencies.map { |row| row.fetch("component_semantic_verdict") })
  equal(component_counts, catalog.fetch("component_semantic_verdict_counts"), "component denominator counts")
  if catalog["dependency_count"]
    equal(all_dependencies.length, catalog.fetch("dependency_count"), "component denominator")
    equal(raw_dependencies.length, catalog.fetch("raw_dependency_count"), "raw dependency denominator")
    equal(missing_dependencies.length, catalog.fetch("anchorless_missing_dependency_count"),
          "missing dependency denominator")
  else
    equal(all_dependencies.length, catalog.fetch("dependency_component_count"), "component denominator")
  end

  by_claim = all_dependencies.group_by { |row| row.fetch("claim_id") }
  by_claim.each do |claim_id, dependencies|
    expected = weakest_verdict(dependencies.map { |row| component_verdict(row.fetch("component_semantic_verdict")) })
    observed = dependencies.map { |row| row.fetch("claim_overall_verdict") }.uniq
    equal(observed, [expected], "weakest-component result #{claim_id}")
  end

  if catalog["claims"].is_a?(Array)
    claims = catalog.fetch("claims")
    equal(claims.map { |row| row.fetch("claim_id") }.sort, joined_claim_ids.sort, "catalog claim denominator")
    claims.each do |claim|
      dependencies = by_claim.fetch(claim.fetch("claim_id"))
      equal(claim.fetch("component_ids").sort, dependencies.map { |row| row.fetch("component_id") }.sort,
            "catalog claim component join")
      equal(claim.fetch("evidence_row_ids").sort, dependencies.map { |row| row.fetch("evidence_row_id") }.sort,
            "catalog claim EVR join")
      equal(claim.fetch("claim_overall_verdict"), dependencies.first.fetch("claim_overall_verdict"),
            "catalog claim verdict")
    end
    claim_counts = count_values(claims.map { |row| row.fetch("claim_overall_verdict") })
    shared_counts = count_values(evidence.select { |row| joined_claim_ids.include?(row.dig("claim", "claim_id")) }
                                          .map { |row| row.fetch("verdict") })
  else
    overall = catalog.fetch("claim_overall_verdicts")
    evidence_overall = evidence.group_by { |row| row.dig("claim", "claim_id") }.transform_values do |rows|
      verdicts = rows.map { |row| row.fetch("verdict") }.uniq
      equal(verdicts.length, 1, "uniform shared-EVR verdict")
      verdicts.first
    end
    equal(overall, evidence_overall.sort.to_h, "all-claim overall map")
    claim_counts = count_values(overall.values)
    shared_counts = count_values(evidence.map { |row| row.fetch("verdict") })
  end
  equal(claim_counts, catalog.fetch("claim_overall_verdict_counts"), "claim-overall denominator counts")
  equal(shared_counts, catalog.fetch("shared_evr_verdict_counts"), "shared-EVR denominator counts")
  true
end

def binding_rows(value, rows = [])
  case value
  when Hash
    if value["path"].is_a?(String) && value["sha256"].is_a?(String) && value["bytes"].is_a?(Integer)
      rows << value
    end
    value.each_value { |child| binding_rows(child, rows) }
  when Array
    value.each { |child| binding_rows(child, rows) }
  end
  rows
end

def tree_digest(path)
  rows = []
  Find.find(path.to_s) do |entry|
    stat = File.lstat(entry)
    raise "symlink in protected tree: #{rel(entry)}" if stat.symlink?
    next unless stat.file?

    rows << [rel(entry), sha256(entry)]
  end
  Digest::SHA256.hexdigest(rows.sort_by(&:first).map { |name, digest| "#{digest}  #{name}\n" }.join)
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

def manifest_path(notes)
  candidates = [
    notes / "stage4_5_round2_output_manifest.json",
    notes / "stage4_5_round2_package_manifest.json"
  ].select(&:file?)
  expect(candidates.length == 1, "expected exactly one controlling manifest, found #{candidates.map(&:basename)}")
  candidates.first
end

def report_evidence_rows(report)
  candidates = []
  walk = lambda do |value|
    case value
    when Hash
      value.each do |key, child|
        candidates << child if key == "evidence_rows" && child.is_a?(Array)
        walk.call(child)
      end
    when Array
      value.each { |child| walk.call(child) }
    end
  end
  walk.call(report)
  candidates.max_by(&:length)
end

def evidence_by_claim(rows)
  rows.group_by { |row| row.dig("claim", "claim_id") }
end

def verdicts_for(rows, claim_id)
  rows.select { |row| row.dig("claim", "claim_id") == claim_id }.map { |row| row["verdict"] }.uniq
end

def verify_claim_spans(registry, draft_raw)
  registry.fetch("claims").each do |claim|
    span = claim.fetch("draft_span")
    start_byte = span.fetch("start_byte")
    end_byte = span.fetch("end_byte")
    expect(start_byte.is_a?(Integer) && end_byte.is_a?(Integer), "noninteger span #{claim['claim_id']}")
    expect(start_byte >= 0 && end_byte > start_byte && end_byte <= draft_raw.bytesize,
           "out-of-bounds span #{claim['claim_id']}")
    equal(draft_raw.byteslice(start_byte...end_byte).force_encoding("UTF-8"), claim.fetch("claim_text"),
          "claim span #{claim['claim_id']}")
  end
  ids = registry.fetch("claims").map { |claim| claim.fetch("claim_id") }
  equal(ids.uniq.length, ids.length, "unique claim IDs")
end

def exact_failure_verdict(report)
  report["verdict"] || report["integrity_verdict"]
end

def failure_verdict?(value)
  value.is_a?(String) && value.start_with?("FAIL")
end

def stage5_false?(value)
  values = deep_values(value)
  values.include?(false) && !values.include?("AUTHORIZED")
end

def failure_mode_status(audit, mode)
  if audit["modes"].is_a?(Hash)
    key = audit["modes"].keys.find { |candidate| candidate.start_with?("#{mode}_") }
    return audit.dig("modes", key, "status") if key
  end
  if audit["rows"].is_a?(Array)
    row = audit["rows"].find { |candidate| candidate["mode"] == mode }
    return row["status"] if row
  end
  nil
end

# Authority and lock.  The performative CURRENT_AUTHORIZED_AUDIT_EXECUTION
# carrier is valid only while this exact full-batch entrypoint is executing.
@full_batch_replay_active = true
check("authorization receipt exact SHA") { equal(sha256(AUTH_RECEIPT_PATH), EXPECTED_AUTH_RECEIPT_SHA, "receipt") }
check("input lock exact SHA") { equal(sha256(LOCK_PATH), EXPECTED_LOCK_SHA, "lock") }

auth = load_json(AUTH_RECEIPT_PATH)
lock = load_json(LOCK_PATH)

check("audit-only authority is exact") do
  equal(auth["status"], "AUTHORIZED_AUDIT_ONLY", "authority status")
  equal(auth["authorized_papers"], PAPERS.keys, "authorized papers")
  equal(auth["repairs_authorized"], false, "repairs authority")
  equal(auth["stage5_authorized"], false, "Stage 5 authority")
  verify_binding(auth.fetch("author_event"))
  verify_binding(auth.fetch("authorization_record"))
  equal(auth.dig("input_lock", "sha256"), EXPECTED_LOCK_SHA, "authority lock binding")
end

check("lock scope forbids every mutation/promotion") do
  scope = lock.fetch("scope")
  equal(scope["operation"], "fresh_mode2_final_integrity_audit", "operation")
  equal(scope["papers"], [29, 30, 31, 32, 33], "paper scope")
  %w[
    canonical_promotion git_synchronization manuscript_or_bibliography_mutation
    readme_or_status_mutation route_or_initial_system_mutation
    scientific_execution_or_result_refresh silent_repair stage5_or_stage6_entry
  ].each { |key| equal(scope[key], false, "scope.#{key}") }
end

lock_rows = binding_rows(lock).uniq { |row| [row["path"], row["sha256"], row["bytes"]] }
check("all 119 unique lock bindings replay") do
  equal(lock_rows.length, 119, "unique lock bindings")
  lock_rows.each { |row| verify_binding(row) }
end

check("all 15 protected science-tree digests replay") do
  trees = lock.fetch("papers").flat_map { |paper| paper.fetch("science_trees") }
  equal(trees.length, 15, "science-tree denominator")
  trees.each do |tree|
    root = ROOT / tree.fetch("path")
    equal(tree_digest(root), tree.fetch("sha256"), "science tree #{tree['path']}")
  end
end

check("Route-A/Route-B batch boundary remains frozen") do
  equal(lock.fetch("aggregate_route_boundary"), EXPECTED_ROUTE, "route boundary")
end

check("README and pipeline-status files remain read-only") do
  READONLY_TEXT_BOUNDARIES.each do |name, digest|
    path = ROOT / name
    expect(path.file? && !path.symlink?, "missing/unsafe read-only boundary #{name}")
    equal(sha256(path), digest, name)
  end
end

paper_locks = lock.fetch("papers").to_h { |row| [row.fetch("paper_id"), row] }

PAPERS.each do |paper_id, slug|
  @current_paper_id = paper_id
  paper_lock = paper_locks.fetch(paper_id)
  paper_root = ROOT / "papers" / slug
  notes = paper_root / "notes"
  draft_path = ROOT / paper_lock.dig("audit_draft", "path")
  registry_path = notes / "stage4_5_round2_claim_registry.json"
  coverage_path = notes / "stage4_5_round2_claim_registry_coverage.json"
  evidence_path = notes / "stage4_5_round2_evidence_rows.json"
  source_map_path = notes / "stage4_5_round2_evidence_source_map.json"
  compliance_path = notes / "stage4_5_round2_compliance_report.json"
  integrity_path = notes / "stage4_5_round2_integrity_report.json"
  passport_path = notes / "stage4_5_round2_material_passport.json"
  manifest = manifest_path(notes)

  registry = load_json(registry_path)
  coverage = load_json(coverage_path)
  evidence = load_json(evidence_path)
  source_map = source_map_path.file? ? load_json(source_map_path) : nil
  compliance = load_json(compliance_path)
  report = load_json(integrity_path)
  passport = load_json(passport_path)
  manifest_data = load_json(manifest)
  draft_raw = File.binread(draft_path)

  check("#{paper_id} exact successor remains locked") do
    equal(sha256(draft_path), EXPECTED_DRAFT_SHA.fetch(paper_id), "#{paper_id} draft")
    equal(registry["draft_raw_sha256"], EXPECTED_DRAFT_SHA.fetch(paper_id), "#{paper_id} registry draft")
    equal(coverage["draft_raw_sha256"], EXPECTED_DRAFT_SHA.fetch(paper_id), "#{paper_id} coverage draft")
  end

  check("#{paper_id} registered claim spans replay exactly") do
    verify_claim_spans(registry, draft_raw)
    equal(coverage["registry_claim_count"], registry.fetch("claims").length, "#{paper_id} coverage count")
    equal(coverage["candidate_unregistered_count"], 0, "#{paper_id} mechanical candidate gaps")
  end

  check("#{paper_id} official claim-coverage replay") do
    output = run_command(
      "claim coverage",
      "python3", (ARS_ROOT / "scripts/claim_registry_coverage.py").to_s,
      "--draft", draft_path.to_s,
      "--registry", registry_path.to_s,
      "--validate-report", coverage_path.to_s
    )
    expect(output.include?("PASS"), "coverage tool emitted no PASS marker")
  end

  check("#{paper_id} official evidence-row replay") do
    command = [
      "python3", (ARS_ROOT / "scripts/evidence_rows.py").to_s,
      "validate", evidence_path.to_s
    ]
    command.concat(["--source-map", source_map_path.to_s]) if source_map_path.file?
    output = run_command("evidence rows", *command)
    expect(output.include?("PASS"), "evidence tool emitted no PASS marker")
  end

  check("#{paper_id} evidence tuple population is exact") do
    expect(evidence.is_a?(Array) && !evidence.empty?, "empty/non-array evidence rows")
    row_ids = evidence.map { |row| row.fetch("row_id") }
    equal(row_ids.uniq.length, row_ids.length, "#{paper_id} unique evidence row IDs")
    registry_by_id = registry.fetch("claims").to_h { |claim| [claim.fetch("claim_id"), claim] }
    known_claims = registry_by_id.keys
    evidence.each do |row|
      claim_id = row.dig("claim", "claim_id")
      expect(known_claims.include?(claim_id), "unknown claim in #{row['row_id']}")
      registered = registry_by_id.fetch(claim_id)
      equal(row.dig("claim", "text"), registered.fetch("claim_text"),
            "#{paper_id} evidence/registry claim text #{row['row_id']}")
      equal(row.dig("claim", "selection_tier"), registered.fetch("selection_tier"),
            "#{paper_id} evidence/registry selection tier #{row['row_id']}")
      if paper_id == "P33"
        expect(registered.fetch("writer_anchors").include?(row.dig("claim", "paper_locator")),
               "#{paper_id} evidence/registry block-line locator #{row['row_id']}")
      else
        expected_locator = "notes/#{draft_path.basename}:UTF8[#{registered.dig('draft_span', 'start_byte')}:" \
                           "#{registered.dig('draft_span', 'end_byte')}]"
        equal(row.dig("claim", "paper_locator"), expected_locator,
              "#{paper_id} evidence/registry paper locator #{row['row_id']}")
      end
    end
    equal(evidence.map { |row| row.dig("claim", "claim_id") }.uniq.sort, known_claims.sort,
          "#{paper_id} all registered claims represented")
    allowed = %w[VERIFIED MINOR_DISTORTION MAJOR_DISTORTION UNVERIFIABLE UNVERIFIABLE_ACCESS]
    unknown = evidence.map { |row| row["verdict"] }.uniq - allowed
    equal(unknown, [], "#{paper_id} evidence verdict vocabulary")
  end

  check("#{paper_id} report embeds the controlling evidence population") do
    embedded = report_evidence_rows(report)
    expect(embedded.is_a?(Array), "no embedded evidence rows")
    equal(embedded, evidence, "#{paper_id} embedded evidence rows")
  end

  if %w[P29 P30 P31 P32].include?(paper_id)
    check("#{paper_id} raw dependency catalog replays bidirectionally") do
      expect(source_map.is_a?(Hash), "dependency source map absent")
      catalog = load_json(notes / "stage4_5_round2_local_claim_dependency_catalog.json")
      verify_dependency_catalog(catalog, evidence, source_map)
      if %w[P30 P31].include?(paper_id)
        equal(catalog.fetch("dependencies").map { |row| row.fetch("evidence_row_id") }.sort,
              evidence.map { |row| row.fetch("row_id") }.sort,
              "#{paper_id} full EVR/catalog one-to-one reverse join")
        equal(catalog.fetch("claim_overall_verdicts").keys.sort,
              registry.fetch("claims").map { |row| row.fetch("claim_id") }.sort,
              "#{paper_id} catalog/registry complete claim population")
      end
    end
  end

  check("#{paper_id} Schema-12 dispatch and official replay") do
    mode, prisma, raise_mode = EXPECTED_COMPLIANCE.fetch(paper_id)
    equal(compliance["mode"], mode, "#{paper_id} compliance mode")
    if prisma == :present
      expect(compliance["prisma_trAIce"].is_a?(Hash), "PRISMA-trAIce adaptation absent")
    else
      equal(compliance["prisma_trAIce"], nil, "PRISMA-trAIce null dispatch")
    end
    equal(compliance.dig("raise", "mode"), raise_mode, "#{paper_id} RAISE mode")
    equal(compliance["overall_decision"], "warn", "#{paper_id} compliance contribution")
    output = run_command(
      "Schema-12",
      "python3", (ARS_ROOT / "scripts/check_compliance_report.py").to_s,
      compliance_path.to_s
    )
    expect(output.start_with?("OK:"), "compliance checker emitted no OK marker")
  end

  check("#{paper_id} controlling integrity verdict is FAIL") do
    blockers = evidence.count { |row| %w[MAJOR_DISTORTION UNVERIFIABLE].include?(row["verdict"]) }
    expect(blockers.positive?, "no Phase-E blocking evidence verdict exists")
    expect(failure_verdict?(exact_failure_verdict(report)),
           "#{paper_id} integrity verdict is #{exact_failure_verdict(report).inspect}")
    equal(report["audit_mode"] || report["mode"], 2, "#{paper_id} Mode")
    equal(report["stage5_started"], false, "#{paper_id} Stage 5")
    values = deep_values(report)
    expect(values.any? { |value| value.to_s.include?("FAIL_CORRECTIONS_PROPOSED_NOT_APPLIED") } ||
           values.any? { |value| value.to_s.include?("PROPOSED_NOT_APPLIED") } ||
           values.any? { |value| value.to_s.include?("PROPOSED_NOT_AUTHORIZED_NOT_APPLIED") },
           "no fail-closed correction state")
  end

  check("#{paper_id} reference and context denominators are preserved") do
    phases = report.fetch("phases")
    phase_a = phases.fetch("A_references")
    phase_b = phases.fetch("B_citation_contexts")
    equal(phase_a["registered"], EXPECTED_REFERENCE_COUNTS.fetch(paper_id), "#{paper_id} references")
    equal(phase_b["registered"], EXPECTED_CONTEXT_COUNTS.fetch(paper_id), "#{paper_id} contexts")
  end

  check("#{paper_id} manifest is a FAIL checkpoint and hashes all listed artifacts") do
    manifest_verdict = manifest_data["verdict"] || manifest_data["integrity_verdict"]
    expect(failure_verdict?(manifest_verdict), "#{paper_id} manifest verdict is #{manifest_verdict.inspect}")
    rows = binding_rows(manifest_data).uniq { |row| [row["path"], row["sha256"], row["bytes"]] }
    expect(rows.length >= 8, "manifest binds too few files: #{rows.length}")
    rows.each { |row| verify_package_binding(row, paper_root, "#{paper_id} manifest #{row['path']}") }
  end

  check("#{paper_id} passport records this FAIL audit and no Stage 5 promotion") do
    audit_row = passport.fetch("stage4_5_round2_audit")
    expect(failure_verdict?(audit_row["verdict"]),
           "passport current verdict is #{audit_row['verdict'].inspect}")
    equal(audit_row["stage5_started"], false, "#{paper_id} passport Stage 5")
  end

  check("#{paper_id} no protected or scientific boundary changed") do
    paper_lock.fetch("protected_canonical_files").each { |row| verify_binding(row) }
    paper_lock.fetch("science_trees").each do |tree|
      equal(tree_digest(ROOT / tree.fetch("path")), tree.fetch("sha256"), tree.fetch("path"))
    end
    input_manifest_path = notes / "stage4_5_round2_input_manifest.json"
    if input_manifest_path.file?
      input_manifest = load_json(input_manifest_path)
      input_manifest.fetch("protected_snapshot_before").each do |name, binding|
        verify_binding(binding.merge("path" => name), "#{paper_id} protected snapshot #{name}")
      end
    end
  end


  check("#{paper_id} seven-mode audit reflects the discovered evidence defect") do
    seven_path = notes / if (notes / "stage4_5_round2_seven_failure_modes.json").file?
                           "stage4_5_round2_seven_failure_modes.json"
                         else
                           "stage4_5_round2_seven_failure_mode_audit.json"
                         end
    seven = load_json(seven_path)
    expect(["SUSPECTED", "INSUFFICIENT_EVIDENCE", "INSUFFICIENT EVIDENCE"].include?(failure_mode_status(seven, 2)),
           "Mode 2 remained #{failure_mode_status(seven, 2).inspect}")
    expected_mode4 = paper_id == "P33" ? "SUSPECTED" : "CLEAR"
    equal(failure_mode_status(seven, 4), expected_mode4, "#{paper_id} Mode 4")
  end

  @paper_rows[paper_id] = {
    "claims" => registry.fetch("claims").length,
    "evidence_rows" => evidence.length,
    "verdict_counts" => evidence.each_with_object(Hash.new(0)) { |row, out| out[row["verdict"]] += 1 },
    "manifest_path" => rel(manifest),
    "manifest_sha256" => sha256(manifest),
    "integrity_report_sha256" => sha256(integrity_path),
    "compliance_report_sha256" => sha256(compliance_path)
  }

  # Paper-specific semantic blockers.  These checks are intentionally
  # explicit so an old structurally valid PASS package cannot pass replay.
  case paper_id
  when "P29"
    check("P29 translated-abstract contradiction is blocking") do
      equal(verdicts_for(evidence, "P29-S45R2-E1-089"), ["MAJOR_DISTORTION"], "P29 E1-089")
      values = deep_values(report).map(&:to_s)
      expect(values.any? { |value| value.include?("TRANSLATED-ABSTRACT-STATUS") }, "P29 issue absent")
    end
    check("P29 component-level raw review preserves every unresolved local claim") do
      %w[001 031 037 038 040 043 057 058 061 062 066 069 070 071 072 079 082 084 087 088].each do |suffix|
        expect(verdicts_for(evidence, "P29-S45R2-E1-#{suffix}").include?("UNVERIFIABLE"),
               "P29 claim #{suffix} was promoted")
      end
    end
    check("P29 local successor uses occurrence-specific raw dependencies") do
      catalog = load_json(notes / "stage4_5_round2_local_claim_dependency_catalog.json")
      local = catalog.fetch("dependencies").select { |row| row["source_ref_slug"] == "P29LocalSuccessor" }
      expect(!local.empty?, "no P29 local successor dependencies")
      leading = local.select { |row| span_bounds(row["raw_utf8_span"]).first.zero? }
      expect(leading.all? do |row|
        scope = row["raw_dependency_scope"]
        scope.is_a?(Hash) && span_bounds(scope["utf8_span"]) == [0, row.dig("artifact", "bytes")] &&
          %w[SCAN_COMPLETE_DRAFT REPLAY_COMPLETE_TREE].include?(row["derivation_rule"])
      end, "P29 leading excerpt lacks a complete-artifact derivation boundary")
      expect(local.all? { |row| row["mapper_tuple_id"] || row["derivation_rule"] },
             "P29 occurrence provenance absent")
    end
    check("P29 search lane contributes no identity or correction clearance") do
      phase_a = load_json(notes / "stage4_5_round2_browser_reference_verification.json")
      equal(phase_a["irrelevant_bing_result_sets_contributing_to_resolution"], 0, "P29 Bing contribution")
      equal(phase_a["correction_retraction_eoc_clearances"], 0, "P29 clearance count")
      equal(phase_a["resolved"], 22, "P29 identity carriers")
    end
  when "P30"
    check("P30 correction-lineage mismatch is blocking") do
      by_claim = evidence.group_by { |row| row.dig("claim", "claim_id") }
      unverified = by_claim.select do |_claim_id, rows|
        rows.map { |row| row["verdict"] }.uniq == ["UNVERIFIABLE"]
      end.keys.sort
      distorted = by_claim.select do |_claim_id, rows|
        rows.map { |row| row["verdict"] }.uniq == ["MAJOR_DISTORTION"]
      end.keys.sort
      equal(unverified, %w[
        P30-S45R2-E1-001 P30-S45R2-E1-047 P30-S45R2-E1-083 P30-S45R2-E1-106
      ], "P30 exact UNVERIFIABLE claim set")
      equal(distorted, %w[
        P30-S45R2-E1-049 P30-S45R2-E1-050 P30-S45R2-E1-051 P30-S45R2-E1-053
        P30-S45R2-E1-092 P30-S45R2-E1-094 P30-S45R2-E1-107
      ], "P30 exact MAJOR_DISTORTION claim set")
      catalog = load_json(notes / "stage4_5_round2_local_claim_dependency_catalog.json")
      livsic_missing = catalog.fetch("dependencies").select do |row|
        row["artifact"].nil? && row.fetch("component_id").end_with?("missing_livsic_passage")
      end
      equal(livsic_missing.map { |row| row["claim_id"] }.sort, %w[
        P30-S45R2-E1-001 P30-S45R2-E1-047 P30-S45R2-E1-083
      ], "P30 exact missing Livsic-passage claim set")
      network = load_json(notes / "stage4_5_round2_reference_network_audit.json")
      network_rows = network.fetch("references").to_h { |row| [row.fetch("ref_slug"), row] }
      s02_updates = network_rows.dig("P30-S02", "query_attempts", "crossref_doi", "crossref_message", "updated-by")
      c01_updates = network_rows.dig("P30-C01", "query_attempts", "crossref_doi", "crossref_message", "update-to")
      equal(s02_updates.map { |row| row["DOI"] }, ["10.1063/1.457672"], "P30-S02 correction relation")
      equal(c01_updates.map { |row| row["DOI"] }, ["10.1063/1.456017"], "P30-C01 corrected work")
      bib = File.read(ROOT / paper_lock.dig("audit_bibliography", "path"))
      expect(bib.include?("P30-S02") && bib.include?("10.1063/1.457669"), "locked mismatch surface absent")
    end
  when "P31"
    check("P31 S23/S24 passage support remains UNVERIFIABLE") do
      catalog = load_json(notes / "stage4_5_round2_local_claim_dependency_catalog.json")
      missing = catalog.fetch("dependencies").select do |row|
        row["artifact"].nil? && row.fetch("component_id").match?(/missing_s2[34]_passage\z/)
      end
      equal(missing.length, 8, "P31 S23/S24 missing component denominator")
      rows = missing.map { |dependency| evidence.find { |row| row["row_id"] == dependency["evidence_row_id"] } }
      expect(rows.none?(&:nil?), "P31 S23/S24 EVR join absent")
      equal(rows.map { |row| row["verdict"] }.uniq, ["UNVERIFIABLE"], "P31 S23/S24 verdicts")
      equal(missing.map { |row| row["claim_id"] }.uniq.sort, %w[
        P31-S45R2-E1-008 P31-S45R2-E1-077 P31-S45R2-E1-079 P31-S45R2-E1-080
      ], "P31 exact S23/S24 passage-gap claim set")
      by_claim = evidence.group_by { |row| row.dig("claim", "claim_id") }
      unverified = by_claim.select do |_claim_id, claim_rows|
        claim_rows.map { |row| row["verdict"] }.uniq == ["UNVERIFIABLE"]
      end.keys.sort
      distorted = by_claim.select do |_claim_id, claim_rows|
        claim_rows.map { |row| row["verdict"] }.uniq == ["MAJOR_DISTORTION"]
      end.keys.sort
      equal(unverified, %w[
        P31-S45R2-E1-008 P31-S45R2-E1-067 P31-S45R2-E1-077
        P31-S45R2-E1-079 P31-S45R2-E1-080 P31-S45R2-E1-126
      ], "P31 exact UNVERIFIABLE claim set")
      equal(distorted, %w[P31-S45R2-E1-108 P31-S45R2-E1-125],
            "P31 exact MAJOR_DISTORTION claim set")
      %w[081 117].each do |suffix|
        equal(verdicts_for(evidence, "P31-S45R2-E1-#{suffix}"), ["VERIFIED"],
              "P31 claim #{suffix} irrelevant passage gap removed")
      end
      reader_manifest_path = notes / "stage4_prime_reader_artifact_manifest_round2.json"
      reader_manifest = load_json(reader_manifest_path)
      manifest_rows = reader_manifest["artifacts"] || reader_manifest["entries"] || reader_manifest["files"]
      method_row = manifest_rows.find do |row|
        row["path"] == "notes/stage4_prime_method_passage_matrix_round2.json"
      end
      expect(!method_row.nil?, "P31 reader manifest method-matrix row absent")
      current_method_path = ROOT / "papers" / PAPERS.fetch("P31") / method_row.fetch("path")
      expect(method_row["sha256"] != sha256(current_method_path) || method_row["bytes"] != current_method_path.size,
             "P31 stale reader-manifest mismatch unexpectedly disappeared")
    end
  when "P32"
    check("P32 translated abstract and closest-work gaps are blocking") do
      equal(verdicts_for(evidence, "P32-S45R2-E1-098"), ["MAJOR_DISTORTION"], "P32 E1-098")
      rows = evidence.select { |row| %w[P32-CW01 P32-CW02 P32-CW03 P32-CW04].include?(row.dig("source", "ref_slug")) }
      equal(rows.length, 4, "P32 closest-work tuple count")
      equal(rows.map { |row| row["verdict"] }.uniq, ["UNVERIFIABLE"], "P32 closest-work verdicts")
    end
    check("P32 local successor uses occurrence-specific raw dependencies") do
      catalog = load_json(notes / "stage4_5_round2_local_claim_dependency_catalog.json")
      local = catalog.fetch("dependencies").select { |row| row["source_ref_slug"] == "P32LocalSuccessor" }
      expect(!local.empty?, "no P32 local successor dependencies")
      leading = local.select { |row| span_bounds(row["raw_utf8_span"]).first.zero? }
      expect(leading.all? do |row|
        row.dig("parsed_value", "recomputed_sha256") == row.dig("artifact", "sha256") &&
          row["derivation_rule"].to_s.include?("COMPLETE_ARTIFACT")
      end, "P32 leading excerpt lacks a complete-artifact digest derivation")
    end
    check("P32 search lane contributes no identity or correction clearance") do
      phase_a = load_json(notes / "stage4_5_round2_browser_reference_verification.json")
      equal(phase_a["irrelevant_bing_result_sets_contributing_to_resolution"], 0, "P32 Bing contribution")
      equal(phase_a["correction_retraction_eoc_clearances"], 0, "P32 clearance count")
      equal(phase_a["resolved"], 30, "P32 identity carriers")
    end
  when "P33"
    check("P33 passage and independent-oracle blockers remain controlling") do
      values = deep_values(report).map(&:to_s)
      expect(values.include?("IL-SERIOUS-1"), "P33 passage issue absent")
      expect(values.include?("IL-MEDIUM-1"), "P33 Mode-4 issue absent")
      unverified = evidence.select { |row| row["verdict"] == "UNVERIFIABLE" }
      equal(unverified.length, 85, "P33 unverifiable evidence rows")
      equal(unverified.map { |row| row.dig("claim", "claim_id") }.uniq.length, 62,
            "P33 claims with at least one unverifiable tuple")
    end
  end
end

check("batch decision derives to zero passes and five failures") do
  equal(@paper_rows.length, 5, "paper result denominator")
  PAPERS.each_key do |paper_id|
    report = load_json(ROOT / "papers" / PAPERS.fetch(paper_id) / "notes/stage4_5_round2_integrity_report.json")
    expect(failure_verdict?(exact_failure_verdict(report)),
           "#{paper_id} aggregate verdict is #{exact_failure_verdict(report).inspect}")
  end
end

check("batch Stage 5 gate remains closed") do
  PAPERS.each do |paper_id, slug|
    notes = ROOT / "papers" / slug / "notes"
    report = load_json(notes / "stage4_5_round2_integrity_report.json")
    equal(report["stage5_started"], false, "#{paper_id} Stage 5 started")
  end
  equal(auth["stage5_authorized"], false, "batch Stage 5 authority")
end

@current_paper_id = nil
@full_batch_replay_active = false

puts
puts "Checks passed: #{@checks}"
puts "Paper summary: #{JSON.generate(@paper_rows)}"
if @failures.empty?
  puts "ROUND10_STAGE4_5_ROUND2_AUDIT_PASS"
  exit 0
end

warn "Failures: #{@failures.length}"
@failures.each { |failure| warn "- #{failure}" }
warn "ROUND10_STAGE4_5_ROUND2_AUDIT_FAIL"
exit 1
