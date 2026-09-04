#!/usr/bin/env ruby
# frozen_string_literal: true

require "digest"
require "json"
require "pathname"
require "time"

ROOT = Pathname.new(__dir__).parent.expand_path.freeze
WORKFLOW_DATE = "2026-09-04"

AUTHORITY_PREFIX = "BATCH_ROUND10_STAGE4_PRIME_CORRECTION_SCOPE_REISSUE_EXACT_CONFIRMATION"
EVENT = ROOT / "#{AUTHORITY_PREFIX}_AUTHOR_EVENT_20260904.txt"
RECORD = ROOT / "#{AUTHORITY_PREFIX}_AUTHORIZATION_RECORD.md"
FREEZE = ROOT / "#{AUTHORITY_PREFIX}_INPUT_FREEZE.json"
RECEIPT = ROOT / "#{AUTHORITY_PREFIX}_AUTHORIZATION_RECEIPT.json"

LINEAGE = {
  "controlling_checkpoint" => [
    "BATCH_ROUND10_STAGE4_PRIME_CORRECTION_SCOPE_REISSUE_MANDATORY_CHECKPOINT.md",
    "0fb41c724ee484335190b823d904d199b11b69528ea890d15119530eb26507d2"
  ],
  "scope_reissue_completion_report" => [
    "BATCH_ROUND10_STAGE4_PRIME_CORRECTION_SCOPE_REISSUE_COMPLETION_REPORT.md",
    "ff40f0226aa9660e27b44e7ecb9b62380016baba422c41ce8fdb1948cd2efb73"
  ],
  "scope_reissue_final_audit" => [
    "BATCH_ROUND10_STAGE4_PRIME_CORRECTION_SCOPE_REISSUE_FINAL_AUDIT.json",
    "21de23b4e3481e7eadcd7c42ed674187654954fea54bee3459a6676749efc97d"
  ],
  "scope_reissue_completion_receipt" => [
    "BATCH_ROUND10_STAGE4_PRIME_CORRECTION_SCOPE_REISSUE_COMPLETION_RECEIPT.json",
    "4b9a49a7fbdd7c7c0e9553c538321d95e8797f93dced5e804350b04a0273a9b4"
  ],
  "scope_reissue_sync_manifest" => [
    "BATCH_ROUND10_STAGE4_PRIME_CORRECTION_SCOPE_REISSUE_SYNC_MANIFEST.json",
    "206904d1d7375a877bd0ea9e57ae865efe7fa172ee0ec79de1f233a085e03cec"
  ],
  "superseded_execution_input_freeze" => [
    "BATCH_ROUND10_STAGE4_PRIME_CORRECTION_EXECUTION_INPUT_FREEZE.json",
    "87ce645eeccbd3a179d05ee48d7abe8c468e1a8f04e9e84cd1ca4037bf95ccff"
  ],
  "noncontrolling_nonexact_author_event" => [
    "BATCH_ROUND10_STAGE4_PRIME_CORRECTION_SCOPE_REISSUE_EXECUTION_AUTHOR_EVENT_20260904.txt",
    "111505020ac13b92ac253361e21777de8343455edd9ed3a4436fe924600cb812"
  ],
  "noncontrolling_nonexact_authorization_record" => [
    "BATCH_ROUND10_STAGE4_PRIME_CORRECTION_SCOPE_REISSUE_EXECUTION_AUTHORIZATION_RECORD.md",
    "8df7a63d2fe998cd27556e10c66f2333e26a9cd0e2b78b64b22da31dbea6a283"
  ],
  "noncontrolling_nonexact_input_freeze" => [
    "BATCH_ROUND10_STAGE4_PRIME_CORRECTION_SCOPE_REISSUE_EXECUTION_INPUT_FREEZE.json",
    "e835f073d785fbad2de809fcf44dd24bc4abf98300ed21857d3b5e9f67751ce4"
  ],
  "noncontrolling_nonexact_authorization_receipt" => [
    "BATCH_ROUND10_STAGE4_PRIME_CORRECTION_SCOPE_REISSUE_EXECUTION_AUTHORIZATION_RECEIPT.json",
    "b154d92f84487b381b50e2e9addb5aecd924c6d9d2fb2277d6604a5cb42a17d1"
  ],
  "noncontrolling_nonexact_authority_audit" => [
    "BATCH_ROUND10_STAGE4_PRIME_CORRECTION_SCOPE_REISSUE_EXECUTION_AUTHORITY_AUDIT.json",
    "ef6d2961029bce839f46d9d5d9a17f325e4d4f06133b62a244f93a87d5851b2d"
  ]
}.freeze

TRACKS = {
  "P29_P32" => {
    "request" => [
      "BATCH_ROUND10_STAGE4_5_CORRECTION_AUTHORIZATION_REQUEST_P29_P32_EXPANDED.json",
      "51735eed804f9bd933e2f5a1f69ad0068b74921b4ab6fc4cdddaade0b6bc2e5b"
    ],
    "human_request" => [
      "BATCH_ROUND10_STAGE4_5_CORRECTION_AUTHORIZATION_REQUEST_P29_P32_EXPANDED.md",
      "74045f2b6758333d6dc1792e5e5a40052a559ed9f983a88b6154e37aa3e6f63d"
    ],
    "validation" => [
      "BATCH_ROUND10_STAGE4_5_CORRECTION_AUTHORIZATION_REQUEST_P29_P32_EXPANDED_VALIDATION.json",
      "947e7203cc22109969831aa0bee066dbc2b0fa5415090c6781aa3b33d8f7dd80"
    ],
    "preparation_receipt" => [
      "BATCH_ROUND10_P29_P32_STAGE4_PRIME_SOURCE_FINALIZATION_SCOPE_CHECKPOINT_RECEIPT.json",
      "160e13e777f7545e9fa08c73adc51e5de5c001b0284155482bcbed72ac86a4bb"
    ]
  },
  "P30_P31" => {
    "request" => [
      "BATCH_ROUND10_STAGE4_PRIME_EXPANDED_CORRECTION_AUTHORIZATION_REQUEST_P30_P31.json",
      "9fecba23da5ea90f3c8f252d0a7fbd019d042f600dbeaa320167865273692135"
    ],
    "human_request" => [
      "BATCH_ROUND10_STAGE4_PRIME_EXPANDED_CORRECTION_AUTHORIZATION_REQUEST_P30_P31.md",
      "858256909b6d30423e22977bfd8bebb7d4b5f46c8406890e17ca65cc5f9a9960"
    ],
    "validation" => [
      "BATCH_ROUND10_STAGE4_PRIME_EXPANDED_CORRECTION_AUTHORIZATION_REQUEST_P30_P31_VALIDATION.json",
      "b2ae5c8e5c6fa542bd004cca6b9dd97451d16ccb7847b05ce25daa4006d33a97"
    ],
    "preparation_receipt" => [
      "BATCH_ROUND10_STAGE4_PRIME_EXPANDED_CORRECTION_AUTHORIZATION_REQUEST_P30_P31_PREPARATION_RECEIPT.json",
      "460dfda1ed4e443181565fcaab40d87834d2a624117e801a2fd31bdd8cb5235f"
    ]
  },
  "P33" => {
    "request" => [
      "BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P33_SCOPE_EXPANSION.json",
      "100c97df01c356a52e3dea39ab327873f544d3ac6b32107f1576ae4dcb02db65"
    ],
    "human_request" => [
      "BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P33_SCOPE_EXPANSION.md",
      "b36b65521481d6a8f568b78ac2ba7b2f09c638b5f26fd9fa9b5255ba9af9d6e0"
    ],
    "validation" => [
      "BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P33_SCOPE_EXPANSION_VALIDATION.json",
      "cfec67180ec0f6e8e24909af47f4a62de7402fb3eedd060cb6abcd318bb697b8"
    ],
    "preparation_receipt" => [
      "BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P33_SCOPE_EXPANSION_RECEIPT.json",
      "70e24304b48e9d1981273e064e58b41a60de9126169e8971298390d89f783a26"
    ]
  }
}.freeze

PREPARED_EXECUTION_EVIDENCE = {
  "P29" => {
    "patch" => ["papers/29-bianchi-ideal-owner-refinement/notes/stage4_prime_revision_patch_round3.json", "2e2db6ad458c5acb0ed96481a0c01f83af2f5c6f18009b9e0e77ac4fcf455309"],
    "writer_handoff" => ["papers/29-bianchi-ideal-owner-refinement/notes/stage4_prime_correction_round3_writer_handoff.json", "274e41b45ee497be89065a59d68447f91a4c99d93c602d65d66dc46b51392e6e"],
    "writer_validation" => ["papers/29-bianchi-ideal-owner-refinement/notes/stage4_prime_writer_validation_receipt_round3.json", "542af7a0e81a61047f0f19d5df3cc39062b8ad398285a6e7f817f9c4010db553"],
    "revision_roadmap" => ["papers/29-bianchi-ideal-owner-refinement/notes/stage4_prime_correction_round3_revision_roadmap.json", "e067432ae7368bd720afb7d65325613d3e98ff30ed53db7166f848dba3ca1186"],
    "author_choices" => ["papers/29-bianchi-ideal-owner-refinement/notes/stage4_prime_correction_round3_author_choices.json", "67120054ac8c72275ebc62e672f8a823761297a4543729c34cb757d9cebd429e"],
    "author_adjudication" => ["papers/29-bianchi-ideal-owner-refinement/notes/stage4_prime_correction_round3_author_adjudication.json", "67a12441354fa69c76aaba99a7b477da9e102ca18d05781a5a8b116f624037bb"],
    "claim_surface_manifest" => ["papers/29-bianchi-ideal-owner-refinement/notes/stage4_prime_correction_round3_claim_surface_manifest.json", "1fcb1c1f3a8d24c314f01c6e2cb834766a1b30c788871bd2c040ac4ab512ea52"]
  },
  "P30" => {
    "patch" => ["papers/30-three-disk-nonconstant-roof-determinant/notes/stage4_prime_revision_patch_round3.json", "8d8c209bec0c639878b63b7faffcbafafcb1dfe46967cf69b790217e6b1a365b"],
    "writer_handoff" => ["papers/30-three-disk-nonconstant-roof-determinant/notes/stage4_prime_correction_round3_writer_handoff.json", "08f8856ac8b524992fa89e0af2d598d932c3dcbc32ede4b086536445f4f2e8e6"],
    "writer_validation" => ["papers/30-three-disk-nonconstant-roof-determinant/notes/stage4_prime_correction_round3_writer_validation_receipt.json", "f3d76ab7bb504da6085d1f2363e7fb8b6140fd3658c44f3f23cdecca27459478"],
    "revision_roadmap" => ["papers/30-three-disk-nonconstant-roof-determinant/notes/stage4_prime_correction_round3_revision_roadmap.json", "856465e2fe5fe018e55eb84f00d49b3be2e2498f57c7e2e984b7441fa875e167"],
    "author_choices" => ["papers/30-three-disk-nonconstant-roof-determinant/notes/stage4_prime_correction_round3_author_choices.json", "3037afaa22174c1b4d772415d4d8432a7aebc77b438b170410d7630cfa58f113"],
    "author_adjudication" => ["papers/30-three-disk-nonconstant-roof-determinant/notes/stage4_prime_correction_round3_author_adjudication.json", "0f39cc2bef92622ad0e80b202f9370330b941418e50a52feaacdac72557ebc48"],
    "claim_surface_manifest" => ["papers/30-three-disk-nonconstant-roof-determinant/notes/stage4_prime_correction_round3_claim_surface_manifest.json", "d1c7f64212ed8ee7c1b8ea1039e4d49210cf16089571324da74656844ab1e438"],
    "matrix_regeneration_plan" => ["papers/30-three-disk-nonconstant-roof-determinant/notes/stage4_prime_correction_round3_matrix_regeneration_plan.json", "949c3ac3bd629c67c4d3605a4b4b173603b1c000d0ef8bae5c47a5b4c7e9b553"]
  },
  "P31" => {
    "patch" => ["papers/31-level11-conjugacy-owner-ledger/notes/stage4_prime_revision_patch_round3.json", "778b35df262cc28fc7aec2bb2d8a1f1c51f62fd6556ece02a5fd88c0266056b5"],
    "writer_handoff" => ["papers/31-level11-conjugacy-owner-ledger/notes/stage4_prime_correction_round3_writer_handoff.json", "57d35678744c248f4de5f07612abb58e37442874e09b3e6f81241108fccd1ae5"],
    "writer_validation" => ["papers/31-level11-conjugacy-owner-ledger/notes/stage4_prime_correction_round3_writer_validation_receipt.json", "fc6611a7051d92abcf79ebdcffeda7f9dcda9b268f7befb530cb73ca3e6c5260"],
    "revision_roadmap" => ["papers/31-level11-conjugacy-owner-ledger/notes/stage4_prime_correction_round3_revision_roadmap.json", "2d78c87fb52dc542f9abc681f7795d1a4a72b659fce2d88b87d7944f64c627d7"],
    "author_choices" => ["papers/31-level11-conjugacy-owner-ledger/notes/stage4_prime_correction_round3_author_choices.json", "3f152d005593621fe9398a10bcaf1655202641fba96e0536c377b46879e52456"],
    "author_adjudication" => ["papers/31-level11-conjugacy-owner-ledger/notes/stage4_prime_correction_round3_author_adjudication.json", "26df423226d1fa0474789a489223988567f6a50bf1a9615a2df25b0345833fe2"],
    "claim_surface_manifest" => ["papers/31-level11-conjugacy-owner-ledger/notes/stage4_prime_correction_round3_claim_surface_manifest.json", "c1fbc6552c7ab328d680957efe504d1b5f93add9f68f1a0c9b5f6138e7c4a635"],
    "matrix_regeneration_plan" => ["papers/31-level11-conjugacy-owner-ledger/notes/stage4_prime_correction_round3_matrix_regeneration_plan.json", "ce7063c0fe7f24bced010076062acf60ce63716b42eac082ff9b6ed995f0ebe8"]
  },
  "P32" => {
    "patch" => ["papers/32-homology-cover-renormalization-uniformity/notes/stage4_prime_revision_patch_round3.json", "c19b10178928a7873a612d48b7e330c3bc513bdbe18f7cd55720da5990784ae6"],
    "writer_handoff" => ["papers/32-homology-cover-renormalization-uniformity/notes/stage4_prime_correction_round3_writer_handoff.json", "d33f4b4c819bf49ab8ebe2c5fb8870515e5ebcf3f4f42997d8c81fa53994d44b"],
    "writer_validation" => ["papers/32-homology-cover-renormalization-uniformity/notes/stage4_prime_writer_validation_receipt_round3.json", "677fa817e035b84948757c9e80fe575d4598b04ad058e9bb63e6fa517f11ea61"],
    "revision_roadmap" => ["papers/32-homology-cover-renormalization-uniformity/notes/stage4_prime_correction_round3_revision_roadmap.json", "581eae6a367b1485a8487962a626675f2b840b4fe0094a827cbc13cd8cd5bf3d"],
    "author_choices" => ["papers/32-homology-cover-renormalization-uniformity/notes/stage4_prime_correction_round3_author_choices.json", "b47caafa57e21c334347008324da96683602160db1bdaace6c11dc4e05f25201"],
    "author_adjudication" => ["papers/32-homology-cover-renormalization-uniformity/notes/stage4_prime_correction_round3_author_adjudication.json", "49a35f55d55c855741cf543d55737800b907f88f522bf86afbc40340a1eaa0d0"],
    "claim_surface_manifest" => ["papers/32-homology-cover-renormalization-uniformity/notes/stage4_prime_correction_round3_claim_surface_manifest.json", "bd11b756aa61797451da5d261f50edf612fc5d701bc7533f38a25c941a636363"]
  },
  "P33" => {
    "patch" => ["papers/33-bolza-control-matched-census/notes/stage4_prime_revision_patch_round6.json", "6de8c7d910d22cf2436f11863689de1bc7d2c35e80027fca42815b95d82e6326"],
    "writer_handoff" => ["papers/33-bolza-control-matched-census/notes/stage4_prime_round6_writer_handoff.json", "990b5a4ffa98d20d37e23ee0cfb989eb7762d8022f5b674514723a0e0366806f"],
    "writer_validation" => ["papers/33-bolza-control-matched-census/notes/stage4_prime_round6_writer_validation_receipt.json", "7eec4aff2fb492520c2000a94d2765545b68a7497de19a6493a8d6f381ea4cee"],
    "revision_roadmap" => ["papers/33-bolza-control-matched-census/notes/stage4_prime_round6_revision_roadmap.json", "504a72d2d623299d935aec4e8864577a8a89d93671474498db1143605d5d4f27"],
    "author_choices" => ["papers/33-bolza-control-matched-census/notes/stage4_prime_round6_author_choices.json", "8cdf84a52c8f0ddce11f605d50fecc3f87c62648004172cd847532ff7677cf94"],
    "author_adjudication" => ["papers/33-bolza-control-matched-census/notes/stage4_prime_round6_author_adjudication.json", "0f70b311c06d5f4b503a857aa6952c41af971ce90f5bff5764b97fdc10263ce1"],
    "claim_surface_manifest" => ["papers/33-bolza-control-matched-census/notes/stage4_prime_round6_claim_surface_manifest.json", "4b0cc91921470410ac84d169c2f5c187e8e824d4fda9495f82153e85cf4a7730"],
    "bibliography_append_plan" => ["papers/33-bolza-control-matched-census/notes/stage4_prime_round6_bibliography_append_plan.json", "44ac528b952b74f80ba7a223446d672e636831afbd827b5aadbb976c7de7d249"]
  }
}.freeze

PREPARED_CROSS_AUDITS = {
  "P29_P32" => ["BATCH_ROUND10_STAGE4_PRIME_SCOPE_REISSUE_CROSS_AUDIT_P29_P32.json", "65063533efe471a5598c2d08b494fa55ad0906ceda34a99ac2f59eace372e80b"],
  "P30_P31" => ["BATCH_ROUND10_STAGE4_PRIME_SCOPE_REISSUE_CROSS_AUDIT_P30_P31.json", "fccb5fc7267684041da8b10554a5aa40174c7fe71af945bc7a8ba90f78d004e9"],
  "P33" => ["BATCH_ROUND10_STAGE4_PRIME_SCOPE_REISSUE_CROSS_AUDIT_P33.json", "4d7cdcf7684b82e8bdacb919331dd5603ae6c2185f3a179b0e81c78824c21914"]
}.freeze

PAPERS = {
  "P29" => {
    "slug" => "29-bianchi-ideal-owner-refinement",
    "draft" => "notes/stage4_prime_revision_round2.tex",
    "bibliography" => "notes/stage4_prime_references_round2.bib",
    "manifest" => "notes/stage4_prime_correction_round3_base.block-manifest.json"
  },
  "P30" => {
    "slug" => "30-three-disk-nonconstant-roof-determinant",
    "draft" => "notes/stage4_prime_revision_round2.tex",
    "bibliography" => "notes/stage4_prime_references_round2.bib",
    "manifest" => "notes/stage4_prime_correction_round3_base.block-manifest.json",
    "matrix" => "notes/stage4_prime_claim_passage_matrix_round2.json"
  },
  "P31" => {
    "slug" => "31-level11-conjugacy-owner-ledger",
    "draft" => "notes/stage4_prime_revision_round2.tex",
    "bibliography" => "notes/stage4_prime_references_round2.bib",
    "manifest" => "notes/stage4_prime_correction_round3_base.block-manifest.json",
    "matrix" => "notes/stage4_prime_method_passage_matrix_round2.json"
  },
  "P32" => {
    "slug" => "32-homology-cover-renormalization-uniformity",
    "draft" => "notes/stage4_prime_revision_round2.tex",
    "bibliography" => "notes/stage4_prime_references_round2.bib",
    "manifest" => "notes/stage4_prime_correction_round3_base.block-manifest.json"
  },
  "P33" => {
    "slug" => "33-bolza-control-matched-census",
    "draft" => "notes/stage4_revision_round1.tex",
    "bibliography" => "paper/references.bib",
    "manifest" => "notes/stage4_prime_round5_base.block-manifest.json"
  }
}.freeze

def require!(condition, message)
  raise "ROUND10_SCOPE_REISSUE_EXECUTION_AUTHORITY_FAIL: #{message}" unless condition
end

def sha(path)
  Digest::SHA256.file(path).hexdigest
end

def binding(path)
  require!(path.file?, "missing bound input #{path.relative_path_from(ROOT)}")
  {
    "path" => path.relative_path_from(ROOT).to_s,
    "sha256" => sha(path),
    "bytes" => path.size
  }
end

def expected_binding(relative, expected)
  path = ROOT / relative
  require!(path.file?, "missing authority input #{relative}")
  actual = sha(path)
  require!(actual == expected, "authority hash mismatch #{relative}: #{actual} != #{expected}")
  binding(path)
end

def collect_bindings(node, rows = [])
  case node
  when Hash
    if node["path"].is_a?(String) && node["sha256"].is_a?(String) && node["sha256"].match?(/\A[0-9a-f]{64}\z/)
      rows << { "path" => node.fetch("path"), "sha256" => node.fetch("sha256") }
    end
    node.each_value { |value| collect_bindings(value, rows) }
  when Array
    node.each { |value| collect_bindings(value, rows) }
  end
  rows
end

def replay_binding_rows!(rows, label)
  unique = rows.each_with_object({}) do |row, out|
    prior = out[row.fetch("path")]
    require!(prior.nil? || prior == row.fetch("sha256"), "conflicting #{label} hash for #{row.fetch('path')}")
    out[row.fetch("path")] = row.fetch("sha256")
  end
  unique.each do |relative, expected|
    path = ROOT / relative
    require!(path.file?, "#{label} path missing: #{relative}")
    require!(sha(path) == expected, "#{label} replay mismatch: #{relative}")
  end
  unique.map { |relative, _| binding(ROOT / relative) }.sort_by { |row| row.fetch("path") }
end

def write_json(path, value)
  File.binwrite(path, JSON.pretty_generate(value) + "\n")
end

def full_normalized_block_hashes(path)
  text = path.binread.force_encoding("UTF-8")
  text.scan(/<!--block:(B\d{4,})-->\r?\n(.*?)(?=\r?\n<!--block:B\d{4,}-->|\z)/m).to_h.transform_values do |block|
    lines = block.gsub("\r\n", "\n").split("\n", -1)
    lines.shift while lines.first&.strip == ""
    lines.pop while lines.last&.strip == ""
    Digest::SHA256.hexdigest(lines.join("\n"))
  end
end

require!(EVENT.file?, "author event missing")
require!(EVENT.binread == "确认\n".b, "author event bytes differ")
[RECORD, FREEZE, RECEIPT].each { |path| require!(!path.exist?, "refusing to overwrite #{path.basename}") }

lineage = LINEAGE.transform_values { |relative, expected| expected_binding(relative, expected) }
track_bindings = TRACKS.transform_values do |artifacts|
  artifacts.transform_values { |relative, expected| expected_binding(relative, expected) }
end
requests = TRACKS.transform_values { |artifacts| JSON.parse((ROOT / artifacts.fetch("request").first).read) }
prepared_execution_evidence = PREPARED_EXECUTION_EVIDENCE.transform_values do |artifacts|
  artifacts.transform_values { |relative, expected| expected_binding(relative, expected) }
end
prepared_cross_audits = PREPARED_CROSS_AUDITS.transform_values do |relative, expected|
  row = expected_binding(relative, expected)
  audit = JSON.parse((ROOT / relative).read)
  require!(audit.fetch("status") == "PASS", "prepared cross-audit is not PASS: #{relative}")
  require!(audit.fetch("papers").all? { |paper| paper.fetch("findings") == [] }, "prepared cross-audit has findings: #{relative}")
  row
end

require!(requests.fetch("P29_P32").dig("totals", "block_operation_pairs") == 46, "P29/P32 count is not 46")
require!(requests.fetch("P30_P31").dig("totals", "expanded_block_operation_pairs") == 47, "P30/P31 count is not 47")
require!(requests.fetch("P30_P31").dig("totals", "derived_matrix_regenerations") == 2, "matrix count is not 2")
require!(requests.fetch("P33").dig("counts", "total_unique_block_operation_pairs") == 37, "P33 count is not 37")
require!(requests.fetch("P33").dig("counts", "supporting_operations") == 7, "P33 support count is not 7")
require!(requests.values.map { |request| request.fetch("status") }.all? { |status| status.include?("AWAITING") },
         "one expanded request is not awaiting confirmation")

p29_p32_targets = requests.fetch("P29_P32").fetch("papers").flat_map do |paper|
  paper.fetch("issues").flat_map do |issue|
    issue.fetch("proposed_targets").map { |target| [paper.fetch("paper_id"), issue.fetch("issue_id"), target] }
  end
end
p30_p31_targets = requests.fetch("P30_P31").fetch("papers").flat_map do |paper|
  paper.fetch("all_requested_targets").map { |target| [paper.fetch("paper_id"), target.fetch("issue_id"), target] }
end
p33_targets = requests.fetch("P33").dig("carried_forward_exact_request", "items").flat_map do |item|
  item.fetch("proposed_targets").map { |target| ["P33", item.fetch("item_id"), target] }
end + requests.fetch("P33").fetch("new_issue_actions").flat_map do |action|
  action.fetch("proposed_targets").map { |target| ["P33", action.fetch("action_id"), target] }
end

unique_pairs = (p29_p32_targets + p30_p31_targets + p33_targets).map do |paper_id, _, target|
  require!(target.fetch("allowed_operations") == ["replace_block"], "non-replace operation requested for #{paper_id}/#{target.fetch('block_id')}")
  [paper_id, target.fetch("block_id"), "replace_block"]
end.uniq
require!(unique_pairs.length == 130, "expanded unique pair count is #{unique_pairs.length}, expected 130")
require!(p29_p32_targets.map { |paper_id, _, target| [paper_id, target.fetch("block_id")] }.uniq.length == 46,
         "P29/P32 unique target count mismatch")
require!(p30_p31_targets.map { |paper_id, _, target| [paper_id, target.fetch("block_id")] }.uniq.length == 47,
         "P30/P31 unique target count mismatch")
require!(p33_targets.map { |paper_id, _, target| [paper_id, target.fetch("block_id")] }.uniq.length == 37,
         "P33 unique target count mismatch")

paper_rows = PAPERS.map do |paper_id, config|
  paper_root = ROOT / "papers" / config.fetch("slug")
  draft = paper_root / config.fetch("draft")
  bibliography = paper_root / config.fetch("bibliography")
  manifest_path = paper_root / config.fetch("manifest")
  manifest = JSON.parse(manifest_path.read)
  block_hashes = manifest.fetch("blocks").to_h { |row| [row.fetch("block_id"), row.fetch("old_hash")] }
  full_block_hashes = full_normalized_block_hashes(draft)
  paper_targets = (p29_p32_targets + p30_p31_targets + p33_targets).select { |row| row.first == paper_id }
  paper_targets.each do |_, _, target|
    block_id = target.fetch("block_id")
    expected = target.fetch("expected_old_hash")
    manifest_hash = block_hashes[block_id]
    actual = full_block_hashes[block_id]
    require!(!manifest_hash.nil? && !actual.nil?, "#{paper_id} target #{block_id} absent from base or block manifest")
    require!(actual.start_with?(manifest_hash), "#{paper_id} target #{block_id} manifest prefix mismatch #{manifest_hash} vs #{actual}")
    require!(expected.match?(/\A(?:[0-9a-f]{12}|[0-9a-f]{64})\z/),
             "#{paper_id} target #{block_id} old-hash has an invalid width: #{expected}")
    hash_matches = expected.length == 64 ? expected == actual : actual.start_with?(expected)
    require!(hash_matches, "#{paper_id} target #{block_id} request old-hash mismatch #{expected} vs #{actual}")
  end
  row = {
    "paper_id" => paper_id,
    "paper_slug" => config.fetch("slug"),
    "current_working_draft" => binding(draft),
    "current_working_bibliography" => binding(bibliography),
    "block_manifest" => binding(manifest_path),
    "authorized_unique_replace_block_pairs" => paper_targets.map { |_, _, target| target.fetch("block_id") }.uniq.length,
    "canonical_files" => %w[paper/manuscript.tex paper/references.bib paper/paper.pdf].map { |relative| binding(paper_root / relative) },
    "science_files" => %w[code experiments results].flat_map do |directory|
      (paper_root / directory).glob("**/*").select(&:file?).reject(&:symlink?)
    end.sort_by(&:to_s).map { |path| binding(path) },
    "initial_system_source" => binding(paper_root / "notes/stage1_prestart_brief.md"),
    "route_crosswalk" => binding(paper_root / "notes/stage4_route_crosswalk.md")
  }
  row["authorized_in_place_matrix_regeneration"] = binding(paper_root / config.fetch("matrix")) if config.key?("matrix")
  row
end

old_freeze = JSON.parse((ROOT / LINEAGE.fetch("superseded_execution_input_freeze").first).read)
old_rows = replay_binding_rows!(collect_bindings(old_freeze), "superseded 94-binding freeze")
require!(old_rows.length == 94, "superseded freeze row count is #{old_rows.length}, expected 94")
request_rows = replay_binding_rows!(requests.values.flat_map { |request| collect_bindings(request) }, "expanded request")
require!(request_rows.length == 85, "expanded request referenced row count is #{request_rows.length}, expected 85")

generated_at = Time.now.utc.iso8601
freeze = {
  "schema_version" => "round10-stage4-prime-correction-scope-reissue-exact-confirmation-input-freeze/1.0",
  "generated_at_utc" => generated_at,
  "workflow_date" => WORKFLOW_DATE,
  "status" => "FROZEN_FOR_EXACT_CONFIRMATION_130_BLOCK_EXECUTION",
  "author_event" => binding(EVENT).merge("exact_text" => "确认\n"),
  "scope_reissue_lineage" => lineage,
  "expanded_request_artifacts" => track_bindings,
  "superseded_freeze_replay" => {
    "status" => "PASS_94_OF_94_EXACT",
    "bindings" => old_rows
  },
  "expanded_request_referenced_artifact_replay" => {
    "status" => "PASS_85_OF_85_EXACT",
    "bindings" => request_rows
  },
  "prepared_execution_evidence" => prepared_execution_evidence,
  "prepared_cross_audits" => prepared_cross_audits,
  "prepared_evidence_authority_role" => "NON_AUTHORIZING_PREPARATION_EVIDENCE_FOR_EXACT_CONFIRMATION_REEMISSION_ONLY",
  "papers" => paper_rows,
  "route_evaluators" => %w[skills/route-a-evaluator.md skills/route-b-evaluator.md].map { |relative| binding(ROOT / relative) },
  "authorized_scope" => {
    "paper_ids" => PAPERS.keys,
    "unique_replace_block_pairs" => 130,
    "per_paper" => paper_rows.to_h { |row| [row.fetch("paper_id"), row.fetch("authorized_unique_replace_block_pairs")] },
    "p30_p31_in_place_matrix_regenerations" => 2,
    "p33_bibliography_append_keys" => ["P33-S03-CORR", "P33-S16-CORR"],
    "p33_use_bindings" => ["P33-U08", "P33-U22", "P33-U27", "P33-U28", "P33-U37"],
    "p33_supporting_operations" => 7,
    "p33_fresh_successor_authority_chain" => true,
    "new_versioned_drafts_and_isolated_builds" => true
  },
  "boundaries" => {
    "fresh_stage4_5_authorized" => false,
    "p33_re_review_authorized" => false,
    "stage5_or_stage6_authorized" => false,
    "canonical_promotion_authorized" => false,
    "scientific_producer_enumeration_census_or_result_refresh_authorized" => false,
    "route_a_or_route_b_credit_authorized" => false,
    "route_or_initial_system_mutation_authorized" => false,
    "registered_claim_strength_change_authorized_only_if_explicitly_listed" => true,
    "structural_edit_authorized" => false,
    "citation_style" => "natbib numbers sort&compress with plainnat"
  },
  "stop_conditions" => [
    "any target old-hash mismatch",
    "any operation outside the three expanded requests",
    "any scientific numerical or canonical-result change",
    "any registered claim-strength change beyond an explicit request contract",
    "any structural edit or structural apply refusal",
    "any bibliography mutation other than the two exact P33 appends",
    "any build or deterministic validation failure"
  ]
}
write_json(FREEZE, freeze)

record = <<~MD
  # Round 10 Papers 29--33 — expanded Stage 4′ correction-execution authorization

  - Workflow date: `#{WORKFLOW_DATE} UTC`
  - Confirmation recorded at: `#{generated_at}`
  - Exact author event: `确认`
  - Author-event artifact: `#{EVENT.basename}`, SHA-256 `#{sha(EVENT)}`
  - Controlling checkpoint: `#{LINEAGE.fetch('controlling_checkpoint').first}`, SHA-256 `#{LINEAGE.fetch('controlling_checkpoint').last}`

  ## Authorized execution

  The author confirmation binds the following immutable machine requests and authorizes every listed `will_address` target in `source_traceability` order:

  1. P29/P32 request SHA-256 `#{TRACKS.dig('P29_P32', 'request', 1)}`: 46 exact `replace_block` pairs (P29 31; P32 15).
  2. P30/P31 request SHA-256 `#{TRACKS.dig('P30_P31', 'request', 1)}`: 47 exact `replace_block` pairs (P30 34; P31 13) and exactly two named notes-side in-place matrix regenerations.
  3. P33 request SHA-256 `#{TRACKS.dig('P33', 'request', 1)}`: 37 unique exact `replace_block` pairs, exactly two bibliography appends (`P33-S03-CORR`, `P33-S16-CORR`), five named use bindings, seven evidence-bound support operations, and a fresh successor roadmap/choices/claim-manifest/adjudication chain.

  Aggregate manuscript authority is exactly **130** unique block replacements. New versioned working drafts, exact patch/apply/provenance artifacts, direct isolated LaTeX/BibTeX builds, validation receipts, response material, and README status updates are authorized only insofar as they implement and document this scope.

  ## Retained boundaries

  This authorization does not include fresh Stage 4.5, P33 re-review, Stage 5/6, canonical promotion, scientific producer/enumeration/census execution, canonical-result refresh, Route A/B credit, or changes to a frozen initial dynamical system. Citation style remains `natbib[numbers,sort&compress]` with `plainnat`.

  The previously generated writer artifacts and cross-audits are frozen only as non-authorizing preparation evidence. Their manuscript replacement text may be reused, but their old author-event, adjudication, patch, handoff, and validation bindings are not executable; fresh exact-confirmation sidecars and fresh cross-audits are required before deterministic apply.

  Stop fail-closed on any hash mismatch, unlisted operation, scientific numerical change, registered-claim movement beyond an explicit contract, structural edit/refusal, unlisted bibliography mutation, or build/validation failure. The older 105-block chain and the earlier non-exact `确认，下一轮` execution chain remain provenance only and are noncontrolling for this execution.
MD
File.binwrite(RECORD, record)

receipt = {
  "schema_version" => "round10-stage4-prime-correction-scope-reissue-exact-confirmation-authorization-receipt/1.0",
  "recorded_at_utc" => generated_at,
  "workflow_date" => WORKFLOW_DATE,
  "status" => "AUTHORIZED_BY_EXACT_CONFIRMATION_FOR_130_BLOCK_STAGE4_PRIME_EXECUTION",
  "author_event" => binding(EVENT).merge("exact_text" => "确认\n"),
  "authorization_record" => binding(RECORD),
  "input_freeze" => binding(FREEZE),
  "controlling_checkpoint" => lineage.fetch("controlling_checkpoint"),
  "tracks" => {
    "P29_P32" => track_bindings.fetch("P29_P32").fetch("request").merge("replace_block_pairs" => 46),
    "P30_P31" => track_bindings.fetch("P30_P31").fetch("request").merge("replace_block_pairs" => 47, "matrix_regenerations" => 2),
    "P33" => track_bindings.fetch("P33").fetch("request").merge(
      "replace_block_pairs" => 37,
      "bibliography_appends" => ["P33-S03-CORR", "P33-S16-CORR"],
      "use_bindings" => ["P33-U08", "P33-U22", "P33-U27", "P33-U28", "P33-U37"],
      "supporting_operations" => 7,
      "fresh_successor_authority_chain_required" => true
    )
  },
  "aggregate" => {
    "papers" => 5,
    "unique_replace_block_pairs" => 130,
    "matrix_regenerations" => 2,
    "p33_bibliography_appends" => 2
  },
  "prepared_execution_evidence" => prepared_execution_evidence,
  "prepared_cross_audits" => prepared_cross_audits,
  "prepared_evidence_authority_role" => "NON_AUTHORIZING_PREPARATION_EVIDENCE_FOR_EXACT_CONFIRMATION_REEMISSION_ONLY",
  "boundaries" => freeze.fetch("boundaries"),
  "next_legal_action" => "Dispatch disjoint writer tracks, apply only exact listed operations to new versioned drafts, validate, build in isolation, and stop before fresh Stage 4.5."
}
write_json(RECEIPT, receipt)

puts "authorization record: #{sha(RECORD)}"
puts "input freeze: #{sha(FREEZE)}"
puts "authorization receipt: #{sha(RECEIPT)}"
puts "author event: #{sha(EVENT)}"
puts "expanded pairs: #{unique_pairs.length}"
puts "prior freeze replay: #{old_rows.length}/#{old_rows.length}"
puts "request artifact replay: #{request_rows.length}/#{request_rows.length}"
