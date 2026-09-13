#!/usr/bin/env ruby
# frozen_string_literal: true

require "digest"
require "json"
require "pathname"

ROOT = Pathname.new(__dir__).parent.expand_path
REQUEST = ROOT / "BATCH_ROUND9_STAGE4_AUTHORIZATION_REQUEST.md"
EVENT = ROOT / "BATCH_ROUND9_STAGE4_AUTHOR_EVENT_20260830.txt"
EXPECTED_REQUEST_SHA256 = "174cf1b035c55f72cdc06f1df6eb5e39138cbc9982ed1fb97457189a964ecd63"
EVENT_ID = "AUTHOR-EVENT-20260830-ROUND9-STAGE4-ALL33"

PAPERS = {
  24 => "24-bianchi-holonomy-flow",
  25 => "25-three-disk-scattering-flow",
  26 => "26-level11-newform-time-change",
  27 => "27-congruence-inverse-limit-no-go",
  28 => "28-bolza-magnetic-flow"
}.freeze

def sha256(path)
  Digest::SHA256.file(path).hexdigest
end

abort "authorization request digest mismatch" unless sha256(REQUEST) == EXPECTED_REQUEST_SHA256
abort "author event is empty" if EVENT.read.empty?

event_sha256 = sha256(EVENT)
total_items = 0

PAPERS.each do |paper_number, slug|
  paper_root = ROOT / "papers" / slug
  roadmap_path = paper_root / "notes" / "stage3_revision_roadmap.json"
  output_path = paper_root / "notes" / "stage4_author_choices.json"
  abort "missing roadmap: #{roadmap_path}" unless roadmap_path.file?
  abort "refusing to overwrite: #{output_path}" if output_path.exist?

  roadmap = JSON.parse(roadmap_path.read)
  items = roadmap.fetch("items")
  total_items += items.length

  item_ids = items.map { |item| item.fetch("id") }
  abort "duplicate item id in Paper #{paper_number}" unless item_ids.uniq.length == item_ids.length

  adjudications = items.map do |item|
    proposed_targets = item.fetch("proposed_targets")
    abort "empty proposed target set for #{item.fetch('id')}" if proposed_targets.empty?

    {
      "item_id" => item.fetch("id"),
      "author_event_id" => EVENT_ID,
      "author_triage" => "will_address",
      "authorized_targets" => proposed_targets,
      "claim_strength_authorizations" => []
    }
  end

  choices = {
    "schema_version" => "author-adjudication-input/1.0",
    "author_events" => [
      {
        "event_id" => EVENT_ID,
        "source" => "explicit_session_user_message",
        "actor_role" => "author",
        "input_sha256" => event_sha256
      }
    ],
    "display_order" => {
      "mode" => "source_traceability",
      "item_ids" => item_ids,
      "author_event_id" => EVENT_ID
    },
    "author_adjudications" => adjudications,
    "collateral_authorizations" => []
  }

  output_path.write(JSON.pretty_generate(choices) + "\n")
  puts "P#{paper_number}: #{items.length} choices -> #{output_path.relative_path_from(ROOT)}"
end

abort "expected 33 roadmap items, found #{total_items}" unless total_items == 33
puts "author_event_sha256=#{event_sha256}"
puts "authorization_request_sha256=#{EXPECTED_REQUEST_SHA256}"
puts "total_items=#{total_items}"
