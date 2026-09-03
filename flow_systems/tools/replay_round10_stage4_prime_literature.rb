#!/usr/bin/env ruby
# frozen_string_literal: true

# Dated Crossref replay for the exact query strings frozen in the P30/P31
# Stage-1 annotated bibliographies.  This is deliberately a one-result-per-
# query metadata replay: it does not pretend to reconstruct unrecorded rows
# from the original multi-interface search session.

require "digest"
require "json"
require "net/http"
require "thread"
require "time"
require "uri"

ROOT = File.expand_path("..", __dir__)
STAMP = "2026-09-03T15:50:00Z"
USER_AGENT = "flow-systems-stage4-prime-replay/1.0 (mailto:wangliang.f@gmail.com)"

PAPERS = {
  30 => {
    slug: "30-three-disk-nonconstant-roof-determinant",
    section: /### Query families and strings executed verbatim(.*?)### A priori inclusion/m,
    extraction: :fences
  },
  31 => {
    slug: "31-level11-conjugacy-owner-ledger",
    section: /### Verbatim queries(.*?)### Prior inclusion/m,
    extraction: :bullets
  }
}.freeze

def sha256(path)
  Digest::SHA256.file(path).hexdigest
end

def frozen_queries(path, spec)
  match = File.read(path, encoding: "UTF-8").match(spec.fetch(:section))
  raise "query section not found in #{path}" unless match

  body = match[1]
  case spec.fetch(:extraction)
  when :fences
    body.scan(/```text\n(.*?)```/m).flat_map do |capture|
      capture.fetch(0).lines.map(&:strip).reject(&:empty?)
    end
  when :bullets
    body.lines.map(&:strip).filter_map do |line|
      next unless line.start_with?("- \"")

      line.delete_prefix("- ")
    end
  else
    raise "unknown extraction mode"
  end
end

def compact_message(message)
  return nil unless message

  {
    "doi" => message["DOI"],
    "title" => Array(message["title"]).first,
    "authors" => Array(message["author"]).map { |a| [a["given"], a["family"]].compact.join(" ") },
    "year" => (message.dig("published-print", "date-parts", 0, 0) ||
               message.dig("published-online", "date-parts", 0, 0) ||
               message.dig("published", "date-parts", 0, 0)),
    "container_title" => Array(message["container-title"]).first,
    "publisher" => message["publisher"],
    "type" => message["type"],
    "url" => message["URL"]
  }
end

def crossref_query(query)
  uri = URI("https://api.crossref.org/works")
  uri.query = URI.encode_www_form(
    "query.bibliographic" => query,
    "rows" => 1,
    "select" => "DOI,title,author,published-print,published-online,published,container-title,publisher,type,URL"
  )
  request = Net::HTTP::Get.new(uri)
  request["User-Agent"] = USER_AGENT
  request["Accept"] = "application/json"
  response = nil
  error = nil
  4.times do |attempt|
    begin
      response = Net::HTTP.start(uri.host, uri.port, use_ssl: true, open_timeout: 20, read_timeout: 40) do |http|
        http.request(request)
      end
      break unless response.code.to_i == 429
    rescue StandardError => e
      error = e
    end
    sleep(1 + attempt)
  end
  raise error if response.nil? && error
  raise "no Crossref response" unless response
  parsed = response.is_a?(Net::HTTPSuccess) ? JSON.parse(response.body) : nil
  {
    "endpoint" => uri.to_s,
    "http_status" => response.code.to_i,
    "message_type" => parsed&.fetch("message-type", nil),
    "total_results" => parsed&.dig("message", "total-results"),
    "top_record" => compact_message(parsed&.dig("message", "items")&.first),
    "error" => nil
  }
rescue StandardError => e
  {
    "endpoint" => uri&.to_s,
    "http_status" => nil,
    "message_type" => nil,
    "total_results" => nil,
    "top_record" => nil,
    "error" => "#{e.class}: #{e.message}"
  }
end

def run_rows(queries, workers: 3)
  queue = Queue.new
  queries.each_with_index { |query, index| queue << [index, query] }
  rows = Array.new(queries.length)
  [workers, queries.length].min.times.map do
    Thread.new do
      loop do
        index, query = queue.pop(true)
        rows[index] = {
          "query_id" => format("Q%02d", index + 1),
          "query" => query,
          "retrieved_at_utc" => STAMP,
          "crossref" => crossref_query(query)
        }
      rescue ThreadError
        break
      end
    end
  end.each(&:join)
  rows
end

PAPERS.each do |number, spec|
  notes = File.join(ROOT, "papers", spec.fetch(:slug), "notes")
  source = File.join(notes, "stage1_phase2_annotated_bibliography.md")
  queries = frozen_queries(source, spec)
  rows = run_rows(queries)
  output = {
    "schema_version" => "round10-stage4-prime-literature-replay-raw/1.0",
    "paper_id" => "P#{number}",
    "generated_at_utc" => STAMP,
    "retrieval_interface" => "Crossref REST /works query.bibliographic",
    "retrieval_bound" => "one Crossref-ranked metadata record per exact frozen query",
    "source_query_document" => {
      "path" => "notes/stage1_phase2_annotated_bibliography.md",
      "sha256" => sha256(source),
      "query_count" => queries.length
    },
    "historical_reconstruction_boundary" => "Original-session result rows not present in the frozen record remain UNAVAILABLE; these dated replay rows are not backfilled as historical observations.",
    "rows" => rows
  }
  out = File.join(notes, "stage4_prime_literature_replay_round2.raw.json")
  File.write(out, JSON.pretty_generate(output) + "\n", mode: "wb")
  puts "P#{number}: #{rows.length} queries, #{rows.count { |r| r.dig('crossref', 'http_status') == 200 }} HTTP 200, #{out}"
end
