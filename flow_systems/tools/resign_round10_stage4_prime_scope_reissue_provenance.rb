#!/usr/bin/env ruby
# frozen_string_literal: true

require "digest"
require "json"
require "pathname"

ROOT = Pathname.new(__dir__).parent.freeze
NOW = Time.now.utc.strftime("%Y-%m-%dT%H:%M:%SZ")

P30_P31_INCIDENT = "BATCH_ROUND10_STAGE4_PRIME_CORRECTION_SCOPE_EXPANSION_FAIL_CLOSED_INCIDENT_P30_P31.json"
P30_P31_REQUEST = "BATCH_ROUND10_STAGE4_PRIME_EXPANDED_CORRECTION_AUTHORIZATION_REQUEST_P30_P31.json"
P30_P31_VALIDATION = "BATCH_ROUND10_STAGE4_PRIME_EXPANDED_CORRECTION_AUTHORIZATION_REQUEST_P30_P31_VALIDATION.json"
P30_P31_RECEIPT = "BATCH_ROUND10_STAGE4_PRIME_EXPANDED_CORRECTION_AUTHORIZATION_REQUEST_P30_P31_PREPARATION_RECEIPT.json"
P29_P32_RECEIPT = "BATCH_ROUND10_P29_P32_STAGE4_PRIME_SOURCE_FINALIZATION_SCOPE_CHECKPOINT_RECEIPT.json"
CORRECTION_RECORD = "BATCH_ROUND10_STAGE4_PRIME_SCOPE_REISSUE_PROVENANCE_TIMESTAMP_CORRECTION.json"

EXPECTED_BEFORE = {
  P30_P31_INCIDENT => "dc748f5b24b242f17090f3e039ae2b6b0c485d38a6804a7fced1acf496d8012e",
  P30_P31_REQUEST => "bae806e48a240b9a139b84c16aefb32c1199406b43d1cfe9c142c47768d94705",
  P30_P31_VALIDATION => "dd78f87c6cf26b62ccec904a02537464d25c735ab09cd4310faab193f83d4f65",
  P30_P31_RECEIPT => "63fbacd6759155b635260e0411f9a6c934f5ff92cbb8474564c6cf7a474c3f33",
  P29_P32_RECEIPT => "9fd436eea6bc97edb1d0f1798554ee1c5709b9bf5e1e54e3ab34ecd0c5ffc210"
}.freeze

P33_CORRECTED = {
  "BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P33_SCOPE_EXPANSION.json" => "100c97df01c356a52e3dea39ab327873f544d3ac6b32107f1576ae4dcb02db65",
  "BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P33_SCOPE_EXPANSION.md" => "b36b65521481d6a8f568b78ac2ba7b2f09c638b5f26fd9fa9b5255ba9af9d6e0",
  "BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P33_SCOPE_EXPANSION_VALIDATION.json" => "cfec67180ec0f6e8e24909af47f4a62de7402fb3eedd060cb6abcd318bb697b8",
  "BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P33_SCOPE_EXPANSION_RECEIPT.json" => "70e24304b48e9d1981273e064e58b41a60de9126169e8971298390d89f783a26"
}.freeze

def full(relative)
  ROOT / relative
end

def sha(relative)
  Digest::SHA256.file(full(relative)).hexdigest
end

def artifact(relative)
  p = full(relative)
  { "path" => relative, "sha256" => Digest::SHA256.file(p).hexdigest, "bytes" => p.size }
end

def load_json(relative)
  JSON.parse(full(relative).read)
end

def write_json(relative, value)
  full(relative).write(JSON.pretty_generate(value) + "\n")
end

EXPECTED_BEFORE.each do |relative, expected|
  actual = sha(relative)
  abort("pre-correction hash mismatch for #{relative}: #{actual}") unless actual == expected
end
P33_CORRECTED.each do |relative, expected|
  actual = sha(relative)
  abort("P33 corrected binding mismatch for #{relative}: #{actual}") unless actual == expected
end

before = EXPECTED_BEFORE.transform_values.with_index { |digest, _| digest }

incident = load_json(P30_P31_INCIDENT)
old_incident_time = incident.fetch("recorded_at_utc")
incident["recorded_at_utc"] = NOW
incident["provenance_timestamp_correction"] = {
  "status" => "CORRECTED_BEFORE_AUTHOR_CONFIRMATION",
  "original_value" => old_incident_time,
  "correction_reason" => "A local +08:00 wall-clock value was mislabeled with the UTC designator Z.",
  "corrected_at_utc" => NOW,
  "scientific_or_scope_change" => false
}
write_json(P30_P31_INCIDENT, incident)

request = load_json(P30_P31_REQUEST)
old_request_time = request.fetch("generated_at_utc")
request["generated_at_utc"] = NOW
request.fetch("fail_closed_incident")["sha256"] = sha(P30_P31_INCIDENT)
request["provenance_timestamp_correction"] = {
  "status" => "REISSUED_BEFORE_AUTHOR_CONFIRMATION",
  "original_value" => old_request_time,
  "corrected_at_utc" => NOW,
  "scope_and_target_bytes_unchanged" => true
}
write_json(P30_P31_REQUEST, request)

validation = load_json(P30_P31_VALIDATION)
old_validation_time = validation.fetch("generated_at_utc")
validation["generated_at_utc"] = NOW
validation["incident"] = artifact(P30_P31_INCIDENT)
validation["request"] = artifact(P30_P31_REQUEST)
validation["provenance_timestamp_correction"] = {
  "status" => "CORRECTED_AND_REBOUND",
  "original_value" => old_validation_time,
  "corrected_at_utc" => NOW
}
write_json(P30_P31_VALIDATION, validation)

receipt = load_json(P30_P31_RECEIPT)
old_receipt_time = receipt.fetch("recorded_at_utc")
receipt["recorded_at_utc"] = NOW
receipt["incident"] = artifact(P30_P31_INCIDENT)
receipt["expanded_request"] = artifact(P30_P31_REQUEST)
receipt["validation"] = artifact(P30_P31_VALIDATION)
receipt["per_paper_readme_status_updates"] = [
  artifact("papers/30-three-disk-nonconstant-roof-determinant/README.md"),
  artifact("papers/31-level11-conjugacy-owner-ledger/README.md")
]
receipt["provenance_timestamp_correction"] = {
  "status" => "CORRECTED_AND_REBOUND",
  "original_value" => old_receipt_time,
  "corrected_at_utc" => NOW
}
write_json(P30_P31_RECEIPT, receipt)

# The P29/P32 source checkpoint was temporally valid; only refresh its
# intentionally mutable status-document bindings after the README conclusion
# was moved to the top.
p29_p32_receipt = load_json(P29_P32_RECEIPT)
p29_p32_receipt["per_paper_readmes"] = [
  artifact("papers/29-bianchi-ideal-owner-refinement/README.md"),
  artifact("papers/32-homology-cover-renormalization-uniformity/README.md")
]
p29_p32_receipt["readme_status_sync"] = {
  "status" => "CURRENT_CONCLUSION_MOVED_TO_PRIMARY_STATUS_BLOCK",
  "recorded_at_utc" => NOW,
  "scientific_or_request_scope_change" => false
}
write_json(P29_P32_RECEIPT, p29_p32_receipt)

record = {
  "schema_version" => "round10-stage4-prime-scope-reissue-provenance-timestamp-correction/1.0",
  "recorded_at_utc" => NOW,
  "workflow_date" => "2026-09-04",
  "status" => "PASS_CORRECTED_BEFORE_AUTHOR_CONFIRMATION",
  "finding" => "P30/P31 used a +08:00 wall-clock value with a Z suffix; P33 used precommitted future minutes. Both request chains were corrected before the next author confirmation.",
  "scientific_or_scope_change" => false,
  "p30_p31" => {
    "old_bindings" => EXPECTED_BEFORE.slice(P30_P31_INCIDENT, P30_P31_REQUEST, P30_P31_VALIDATION, P30_P31_RECEIPT),
    "new_bindings" => [P30_P31_INCIDENT, P30_P31_REQUEST, P30_P31_VALIDATION, P30_P31_RECEIPT].to_h { |relative| [relative, artifact(relative)] },
    "original_timestamp_values" => {
      "incident" => old_incident_time,
      "request" => old_request_time,
      "validation" => old_validation_time,
      "receipt" => old_receipt_time
    },
    "corrected_timestamp_utc" => NOW
  },
  "p33" => {
    "old_request_sha256" => "0eaee7b0272fc4f1df78117ee6147be5858ae6b9fda5d1b4aafdf3b7fbbc5a20",
    "old_validation_sha256" => "136512aca6480928f4b073f910a107494433c6eb9f2e229754c441f9debd8bb6",
    "old_receipt_sha256" => "b5668ba12048af46919581e55974a31c229c9b033a7e541e4ed5b3dcec3fdd4a",
    "corrected_bindings" => P33_CORRECTED.keys.to_h { |relative| [relative, artifact(relative)] },
    "validation_checks" => 701,
    "validation_failures" => 0
  },
  "p29_p32_readme_receipt_rebind" => artifact(P29_P32_RECEIPT),
  "boundaries" => {
    "target_sets_changed" => false,
    "manuscript_or_bibliography_changed" => false,
    "canonical_science_results_route_or_initial_system_changed" => false,
    "new_author_confirmation_required_for_corrected_request_hashes" => true
  }
}
write_json(CORRECTION_RECORD, record)

puts JSON.pretty_generate(
  "status" => record.fetch("status"),
  "record" => artifact(CORRECTION_RECORD),
  "p29_p32_receipt" => artifact(P29_P32_RECEIPT),
  "p30_p31_incident" => artifact(P30_P31_INCIDENT),
  "p30_p31_request" => artifact(P30_P31_REQUEST),
  "p30_p31_validation" => artifact(P30_P31_VALIDATION),
  "p30_p31_receipt" => artifact(P30_P31_RECEIPT),
  "p33" => P33_CORRECTED.keys.to_h { |relative| [relative, artifact(relative)] }
)
