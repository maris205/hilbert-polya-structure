require 'json'
require 'digest'
require 'time'

# Read-only final binding check. Historical nested manifest expectations are
# not relabelled as the current lock. No artifact is modified by this script.
root = File.expand_path('..', __dir__)
lock_path = File.join(root, 'BATCH_ROUND10_STAGE4_5_ROUND3_INPUT_LOCK.json')
raw = File.binread(lock_path)
lock = JSON.parse(raw)
rows = []
failure = nil
lock.fetch('observed_workspace_bindings').each do |entry|
  begin
    actual = File.binread(File.join(root, entry.fetch('path')))
    sha = Digest::SHA256.hexdigest(actual)
    match = sha == entry.fetch('sha256') && actual.bytesize == entry.fetch('bytes')
    row = { path: entry['path'], expected_sha256: entry['sha256'], actual_sha256: sha, bytes: actual.bytesize, match: match }
    rows << row
    unless match
      failure = row
      break
    end
  rescue StandardError => e
    failure = { path: entry['path'], error: e.message }
    break
  end
end
trees = []
unless failure
  lock.fetch('protected_boundary').fetch('science_trees').each do |tree|
    prefix = tree.fetch('path') + '/'
    actual_paths = Dir.glob(File.join(root, tree.fetch('path'), '**', '*'), File::FNM_DOTMATCH).select { |path| File.file?(path) || File.symlink?(path) }.map { |path| path.delete_prefix(root + '/') }.sort
    expected_paths = lock.fetch('observed_workspace_bindings').map { |entry| entry.fetch('path') }.select { |path| path.start_with?(prefix) }.sort
    match = actual_paths == expected_paths && actual_paths.length == tree.fetch('file_count')
    row = {path: tree['path'], file_count: actual_paths.length, expected_paths: expected_paths, actual_paths: actual_paths, match: match}
    trees << row
    unless match
      failure = row
      break
    end
  end
end
puts JSON.generate({status: failure ? 'STOP_FIRST_NEW_MISMATCH' : 'PASS', checked_bindings: rows.length, expected_bindings: lock['observed_workspace_bindings'].length, input_lock_sha256: Digest::SHA256.hexdigest(raw), checked_at_utc: Time.now.utc.iso8601, failure: failure, rows: rows, science_trees: trees, known_p30_nested_reader_exception_retained: true, scientific_execution_performed: false})
exit(failure ? 1 : 0)
