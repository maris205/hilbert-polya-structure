#!/usr/bin/env ruby
# frozen_string_literal: true

require "digest"
require "json"
require "pathname"

ROOT = Pathname.new(__dir__).parent.freeze
NOW = Time.now.utc.strftime("%Y-%m-%dT%H:%M:%SZ")

INCIDENT = "BATCH_ROUND10_STAGE4_PRIME_CORRECTION_SCOPE_EXPANSION_FAIL_CLOSED_INCIDENT_P30_P31.json"
REQUEST = "BATCH_ROUND10_STAGE4_PRIME_EXPANDED_CORRECTION_AUTHORIZATION_REQUEST_P30_P31.json"
REQUEST_MD = "BATCH_ROUND10_STAGE4_PRIME_EXPANDED_CORRECTION_AUTHORIZATION_REQUEST_P30_P31.md"
VALIDATION = "BATCH_ROUND10_STAGE4_PRIME_EXPANDED_CORRECTION_AUTHORIZATION_REQUEST_P30_P31_VALIDATION.json"
RECEIPT = "BATCH_ROUND10_STAGE4_PRIME_EXPANDED_CORRECTION_AUTHORIZATION_REQUEST_P30_P31_PREPARATION_RECEIPT.json"
PROVENANCE = "BATCH_ROUND10_STAGE4_PRIME_SCOPE_REISSUE_PROVENANCE_TIMESTAMP_CORRECTION.json"

EXPECTED = {
  INCIDENT => "7833c8e8796ba1fa691dfaad95460406fd8026e8d12a6d6d9665011d41685b6e",
  REQUEST => "9fecba23da5ea90f3c8f252d0a7fbd019d042f600dbeaa320167865273692135",
  REQUEST_MD => "858256909b6d30423e22977bfd8bebb7d4b5f46c8406890e17ca65cc5f9a9960",
  VALIDATION => "ec9561f7b533e4afe581e899f3dc19bde1b25066d308366857d1f6c4e35e3ca3",
  RECEIPT => "340482f297aa504f1bf67e67a717404878f3df83e58ec81c44c5a6635d357ec5",
  PROVENANCE => "b804d04da55c1f0a6b04098641c3b6166a6ecdb2c1c755b8514dee40b63dafbe"
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

EXPECTED.each do |relative, expected|
  actual = sha(relative)
  abort("pre-fix hash mismatch for #{relative}: #{actual}") unless actual == expected
end

human = full(REQUEST_MD).read
request_sha = EXPECTED.fetch(REQUEST)
incident_sha = EXPECTED.fetch(INCIDENT)
abort("human request does not bind current machine request exactly once") unless human.scan(request_sha).length == 1
abort("human request does not bind current incident exactly once") unless human.scan(incident_sha).length == 1
abort("human request still contains superseded request SHA") if human.include?("bae806e48a240b9a139b84c16aefb32c1199406b43d1cfe9c142c47768d94705")

validation = load_json(VALIDATION)
validation["generated_at_utc"] = NOW
validation["human_request"] = artifact(REQUEST_MD)
validation.fetch("fixed_checks") << {
  "check_id" => "C21",
  "description" => "human-facing request mentions the current machine-request and incident SHA-256 exactly once and no superseded request SHA",
  "status" => "PASS"
}
validation.fetch("counts")["fixed_checks"] = 21
validation.fetch("counts")["passed"] = 84
validation.fetch("counts")["total_checks"] = 84
validation["human_request_binding_remediation"] = {
  "status" => "PASS_REBOUND_BEFORE_AUTHOR_CONFIRMATION",
  "recorded_at_utc" => NOW,
  "machine_request_sha256" => request_sha,
  "incident_sha256" => incident_sha,
  "superseded_machine_request_sha256_absent" => true,
  "scientific_or_scope_change" => false
}
write_json(VALIDATION, validation)

receipt = load_json(RECEIPT)
receipt["recorded_at_utc"] = NOW
receipt["human_request"] = artifact(REQUEST_MD)
receipt["validation"] = artifact(VALIDATION)
receipt.fetch("counts")["validation_checks_passed"] = 84
receipt["human_request_binding_remediation"] = {
  "status" => "PASS_REBOUND_BEFORE_AUTHOR_CONFIRMATION",
  "recorded_at_utc" => NOW
}
write_json(RECEIPT, receipt)

provenance = load_json(PROVENANCE)
provenance["recorded_at_utc"] = NOW
provenance.fetch("p30_p31").fetch("new_bindings")[REQUEST_MD] = artifact(REQUEST_MD)
provenance.fetch("p30_p31").fetch("new_bindings")[VALIDATION] = artifact(VALIDATION)
provenance.fetch("p30_p31").fetch("new_bindings")[RECEIPT] = artifact(RECEIPT)
provenance["human_request_binding_followup"] = {
  "status" => "PASS_FIXED_BEFORE_AUTHOR_CONFIRMATION",
  "recorded_at_utc" => NOW,
  "finding" => "The human-facing P30/P31 request retained the superseded pre-timestamp-correction request and incident hashes.",
  "machine_request_sha256" => request_sha,
  "human_request" => artifact(REQUEST_MD),
  "validation" => artifact(VALIDATION),
  "receipt" => artifact(RECEIPT),
  "scientific_or_target_scope_change" => false
}
write_json(PROVENANCE, provenance)

puts JSON.pretty_generate(
  "status" => "PASS_HUMAN_REQUEST_REBOUND_BEFORE_AUTHOR_CONFIRMATION",
  "human_request" => artifact(REQUEST_MD),
  "validation" => artifact(VALIDATION),
  "receipt" => artifact(RECEIPT),
  "provenance_record" => artifact(PROVENANCE)
)
