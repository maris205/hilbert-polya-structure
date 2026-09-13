#!/usr/bin/env ruby
# Read-only, concrete-chain checker. Writes stdout JSON only.
# No ARS runtime imports, subprocesses, network, or filesystem writes.
#
# The input inventory contains TeX paragraph fragments only: 345 anchored
# replacements and nine anchored insertions. Eleven replacements split into
# two paragraphs. This is deliberately not a general Markdown patch engine.
# Fresh IDs are allocated in base-document order, then edits are applied in
# reverse byte-offset order. Expected successor bytes never drive rendering.
require "json"
require "digest"
require "pathname"
require "time"

ROOT = Pathname.new("/root/autodl-tmp/flow_systems").freeze
LOCK_PATH = "BATCH_ROUND10_STAGE4_5_ROUND3_INPUT_LOCK.json".freeze
LOCK_SHA = "0c7755b343990af1d37049838f81e0483323584c96eab58cddf6e14bc572e229".freeze
EXPECTED_COUNTS = {"P29" => 100, "P30" => 80, "P31" => 52, "P32" => 52, "P33" => 70}.freeze

class ReplayStop < StandardError
  attr_reader :details
  def initialize(kind, details)
    @details = {"kind" => kind}.merge(details)
    super(kind)
  end
end

def demand(condition, kind, details = {})
  raise ReplayStop.new(kind, details) unless condition
end

def digest(bytes)
  Digest::SHA256.hexdigest(bytes)
end

def bound_read(descriptor, relative_root = ROOT)
  path = relative_root.join(descriptor.fetch("path")).cleanpath
  demand(path.to_s.start_with?(ROOT.to_s + "/"), "outside_authorized_root", {"path" => path.to_s})
  bytes = File.binread(path)
  observed = digest(bytes)
  demand(observed == descriptor.fetch("sha256"), "bound_artifact_hash_mismatch",
         {"path" => path.relative_path_from(ROOT).to_s, "expected" => descriptor["sha256"], "actual" => observed})
  if descriptor.key?("bytes")
    demand(bytes.bytesize == descriptor["bytes"], "bound_artifact_size_mismatch",
           {"path" => path.to_s, "expected" => descriptor["bytes"], "actual" => bytes.bytesize})
  end
  bytes
end

def blank_line?(line)
  line.sub(/\r?\n\z/, "").strip.empty?
end

def normalized_hash(content)
  lines = content.gsub("\r\n", "\n").split("\n", -1)
  lines.shift while !lines.empty? && lines.first.strip.empty?
  lines.pop while !lines.empty? && lines.last.strip.empty?
  digest(lines.join("\n"))[0, 12]
end

def reject_nonparagraph_syntax(lines, label)
  # These forms have special Markdown segmentation rules. None was present in
  # the inspected chain; fail closed if the concrete input scope changes.
  lines.each do |line|
    text = line.sub(/\r?\n\z/, "")
    special = text.match?(/\A[ \t]{0,3}(?:\#{1,6}[ \t]|```|~~~|>|[-+*][ \t]|[0-9]+[.)][ \t]|\|)/)
    special ||= text.match?(/\A[ \t]*(?:<[^!]|<\/|\[\^[^\]]+\]:|={3,}[ \t]*\z|-{3,}[ \t]*\z)/)
    demand(!special, "unsupported_nonparagraph_shape", {"surface" => label, "line" => text[0, 120]})
  end
end

def parse_base(bytes, label)
  marks = []
  bytes.to_enum(:scan, /^<!--block:(B[0-9]{4,})-->\r?\n/).each do
    match = Regexp.last_match
    marks << {"id" => match[1], "marker_start" => match.begin(0), "content_start" => match.end(0)}
  end
  demand(!marks.empty?, "no_block_markers", {"surface" => label})
  demand(marks.map { |x| x["id"] }.uniq.length == marks.length, "duplicate_block_id", {"surface" => label})
  marks.each_with_index do |block, i|
    ending = i + 1 < marks.length ? marks[i + 1]["marker_start"] : bytes.bytesize
    segment = bytes.byteslice(block["content_start"], ending - block["content_start"])
    lines = segment.lines
    demand(!lines.empty? && !blank_line?(lines.first), "orphan_marker", {"surface" => label, "block_id" => block["id"]})
    lines.pop while !lines.empty? && blank_line?(lines.last)
    demand(lines.none? { |line| blank_line?(line) }, "unsupported_internal_blank_in_base_block",
           {"surface" => label, "block_id" => block["id"]})
    reject_nonparagraph_syntax(lines, "#{label}:#{block['id']}")
    content = lines.join
    block["content"] = content
    block["content_end"] = block["content_start"] + content.bytesize
    block["unit_end"] = ending
    block["old_hash"] = normalized_hash(content)
  end
  marks
end

def fragment_paragraphs(text, label)
  bytes = text.b
  demand(!bytes.include?("<!--block:"), "embedded_writer_marker", {"surface" => label})
  lines = bytes.lines
  reject_nonparagraph_syntax(lines, label)
  paragraphs = []
  current = +"".b
  lines.each do |line|
    if blank_line?(line)
      unless current.empty?
        paragraphs << current
        current = +"".b
      end
    else
      current << line
    end
  end
  paragraphs << current unless current.empty?
  demand(!paragraphs.empty?, "empty_fragment", {"surface" => label})
  paragraphs.map { |part| part.end_with?("\n") ? part : part + "\n" }
end

def reproduce(base, patch, manifest, label)
  blocks = parse_base(base, label)
  by_id = blocks.to_h { |b| [b["id"], b] }
  declared = manifest.fetch("blocks").to_h { |b| [b.fetch("block_id"), b.fetch("old_hash")] }
  demand(declared.keys.sort == by_id.keys.sort, "manifest_target_set_mismatch", {"surface" => label})
  demand(patch["base_draft_hash"] == digest(base)[0, 12] &&
         manifest["base_draft_hash"] == digest(base)[0, 12], "base_prefix_mismatch", {"surface" => label})
  demand(patch["patch_format_version"] == "1.1", "unsupported_patch_version", {"surface" => label})
  planned = {}
  patch.fetch("ops").each_with_index do |op, index|
    id = op.fetch("block_id")
    demand(%w[replace_block insert_after].include?(op["op"]), "unsupported_operation", {"surface" => label, "op_index" => index})
    demand(by_id.key?(id), "unknown_target", {"surface" => label, "op_index" => index, "block_id" => id})
    demand(!planned.key?(id), "duplicate_target", {"surface" => label, "block_id" => id})
    observed = by_id[id]["old_hash"]
    demand(op.fetch("old_hash") == observed && declared[id] == observed, "old_hash_mismatch",
           {"surface" => label, "op_index" => index, "block_id" => id, "patch" => op["old_hash"], "manifest" => declared[id], "actual" => observed})
    demand(op.fetch("roadmap_item_ids").is_a?(Array) && !op["roadmap_item_ids"].empty?,
           "missing_roadmap_trace", {"surface" => label, "op_index" => index})
    planned[id] = {"index" => index, "op" => op, "parts" => fragment_paragraphs(op.fetch("new_text"), "#{label}:op#{index}")}
  end
  next_id = blocks.map { |b| b["id"][1..].to_i }.max + 1
  edits = []
  operation_rows = []
  fresh_ids = []
  blocks.each_with_index do |block, block_index|
    action = planned[block["id"]]
    next unless action
    op = action["op"]
    replacement = op["op"] == "replace_block"
    ids = []
    rendered_parts = action["parts"].each_with_index.map do |part, segment_index|
      if replacement && segment_index.zero?
        part
      else
        id = format("B%04d", next_id)
        next_id += 1
        ids << id
        fresh_ids << id
        "<!--block:#{id}-->\n".b + part
      end
    end
    rendered = rendered_parts.join("\n").b
    if replacement
      rendered = rendered.byteslice(0, rendered.bytesize - 1) unless block["content"].end_with?("\n")
      edits << [block["content_start"], block["content_end"], rendered]
    else
      prefix = block["content"].end_with?("\n") ? "\n" : "\n\n"
      gap_empty = block["content_end"] == block["unit_end"]
      suffix = gap_empty && block_index + 1 < blocks.length ? "\n" : ""
      edits << [block["content_end"], block["content_end"], prefix.b + rendered + suffix.b]
    end
    operation_rows << {"op_index" => action["index"], "op" => op["op"], "block_id" => block["id"],
                       "old_hash" => block["old_hash"], "segment_count" => action["parts"].length, "generated_new_block_ids" => ids}
  end
  output = base.dup
  edits.sort_by { |start, _, _| -start }.each do |start, ending, replacement|
    output = output.byteslice(0, start) + replacement + output.byteslice(ending, output.bytesize - ending)
  end
  [output, operation_rows.sort_by { |row| row["op_index"] }, fresh_ids]
end

report = {
  "schema_version" => "round10-stage4.5-round3-independent-replay/1.0",
  "started_at_utc" => Time.now.utc.iso8601,
  "status" => "RUNNING",
  "implementation" => "Standalone Ruby; independent paragraph/marker parsing and reverse byte-offset splicing; no ARS imports or calls.",
  "specification_boundary" => "Written patch1.1 protocol and rendering conventions inspected. Concrete TeX paragraph subset only; not a general Markdown engine or independent scientific verifier.",
  "side_effects" => "Read-only files and in-memory strings; stdout JSON only. No manuscript, receipt, lock, bibliography, science, Git, or network writes.",
  "input_lock" => {"path" => LOCK_PATH, "sha256" => LOCK_SHA},
  "checker" => {"path" => Pathname.new(__FILE__).realpath.relative_path_from(ROOT).to_s, "sha256" => digest(File.binread(__FILE__))},
  "papers" => []
}
begin
  lock = JSON.parse(bound_read({"path" => LOCK_PATH, "sha256" => LOCK_SHA}))
  demand(lock.fetch("paper_ids").sort == EXPECTED_COUNTS.keys.sort, "paper_set_mismatch")
  lock.fetch("papers").each do |paper|
    id = paper.fetch("paper_id")
    descriptor = paper.fetch("continuous_revision_evidence").fetch("bundle")
    bundle = JSON.parse(bound_read(descriptor))
    paper_root = ROOT.join(descriptor.fetch("path")).dirname.dirname
    start = bound_read(bundle.fetch("chain_start").fetch("draft"), paper_root)
    state = start
    result = {"paper_id" => id, "bundle" => descriptor, "rounds" => [], "operation_count" => 0}
    report["papers"] << result
    bundle.fetch("rounds").each do |round|
      label = "#{id}:R#{round.fetch('revision_round')}"
      pre = bound_read(round.fetch("pre_round_draft"), paper_root)
      demand(state == pre, "continuous_predecessor_mismatch", {"surface" => label})
      patch = JSON.parse(bound_read(round.fetch("revision_patch"), paper_root))
      manifest = JSON.parse(bound_read(round.fetch("pre_round_block_manifest"), paper_root))
      apply_report = JSON.parse(bound_read(round.fetch("apply_report"), paper_root))
      expected = bound_read(round.fetch("post_round_draft"), paper_root)
      demand(patch["revision_round"] == round["revision_round"], "round_number_mismatch", {"surface" => label})
      reproduced, operations, fresh_ids = reproduce(state, patch, manifest, label)
      unless reproduced == expected
        common = [reproduced.bytesize, expected.bytesize].min
        offset = (0...common).find { |i| reproduced.getbyte(i) != expected.getbyte(i) } || common
        raise ReplayStop.new("successor_byte_mismatch",
                             {"surface" => label, "first_mismatch_byte" => offset, "expected_sha256" => digest(expected),
                              "reproduced_sha256" => digest(reproduced), "expected_bytes" => expected.bytesize, "reproduced_bytes" => reproduced.bytesize})
      end
      demand(apply_report["base_draft_hash"] == digest(state)[0, 12] &&
             apply_report["output_draft_hash"] == digest(reproduced)[0, 12] &&
             apply_report["patch_digest"] == round["revision_patch"]["sha256"],
             "apply_report_chain_mismatch", {"surface" => label})
      demand(apply_report.fetch("fresh_block_ids") == fresh_ids, "fresh_id_report_mismatch", {"surface" => label})
      applied = apply_report.fetch("ops_applied").to_h { |row| [row.fetch("op_index"), row] }
      operations.each do |operation|
        recorded = applied.fetch(operation["op_index"])
        demand(recorded["new_block_ids"] == operation["generated_new_block_ids"] &&
               recorded["block_id"] == operation["block_id"] && recorded["op"] == operation["op"],
               "operation_report_mismatch", {"surface" => label, "op_index" => operation["op_index"]})
      end
      result["rounds"] << {"revision_round" => round["revision_round"], "status" => "BYTE_IDENTICAL",
                           "pre_sha256" => digest(state), "patch_sha256" => round["revision_patch"]["sha256"],
                           "reproduced_post_sha256" => digest(reproduced), "post_bytes" => reproduced.bytesize,
                           "operation_count" => operations.length, "fresh_block_ids" => fresh_ids, "operations" => operations}
      result["operation_count"] += operations.length
      state = reproduced
    end
    final = bound_read(bundle.fetch("final_draft"), paper_root)
    current = bound_read(paper.fetch("current_preview").fetch("draft"))
    demand(state == final && state == current, "final_target_mismatch", {"paper_id" => id})
    demand(result["operation_count"] == EXPECTED_COUNTS.fetch(id), "operation_count_mismatch", {"paper_id" => id})
    result["final_draft"] = {"sha256" => digest(state), "bytes" => state.bytesize, "status" => "BYTE_IDENTICAL_TO_CURRENT_LOCK"}
    result["status"] = "PASS_EXACT_CONTINUOUS_REPLAY"
  end
  report["operation_count"] = report["papers"].sum { |paper| paper["operation_count"] }
  demand(report["operation_count"] == 354, "batch_operation_count_mismatch")
  report["round_count"] = report["papers"].sum { |paper| paper["rounds"].length }
  report["status"] = "PASS_EXACT_CONTINUOUS_REPLAY"
rescue ReplayStop => e
  report["status"] = "STOP_FIRST_MISMATCH"
  report["failure"] = e.details
rescue StandardError => e
  report["status"] = "STOP_FIRST_CHECKER_OR_INPUT_ERROR"
  report["failure"] = {"class" => e.class.name, "message" => e.message}
ensure
  report["completed_at_utc"] = Time.now.utc.iso8601
  report["claim_truth_or_authorization_semantics_verified"] = false
  puts JSON.pretty_generate(report)
end
exit(report["status"] == "PASS_EXACT_CONTINUOUS_REPLAY" ? 0 : 1)
