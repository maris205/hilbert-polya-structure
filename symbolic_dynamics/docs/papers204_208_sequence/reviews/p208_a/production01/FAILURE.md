# Actual first recorder failure

The mathematical producer and its canonical comparison exited zero. The
subsequent runtime-coverage assertion failed because Python isolated mode
still imports the site-startup module `_distutils_hack/__init__.py` and the
first inventory excluded site-packages. This is an evidence failure, not
a mathematical failure and not a successful cold replay receipt. The
raw producer, full commands/streams, before inventories, actual consumed
runtime and exact recorder version are preserved. The recorder was archived
after this observed failure but before modification; it matches its recorded
pre-run hash. Revised runs explicitly pin already-loaded startup modules
before their child executes. No old failed receipt is relabelled PASS.
