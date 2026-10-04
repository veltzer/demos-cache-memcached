# TOFIX

Findings from a code scan on 2026-10-04.

## Medium

- `methods_of_intallation.txt:35` - the line "My containers are not managed by the OS but rather by docker." is spliced into the middle of the "usually runs as root" sentence (lines 34 and 36), breaking both points; move it after line 36.
- `rsconstruct.toml:21` - only the shell scripts are checked; `memcached_and_python/insert_and_retrieve.py` is not covered by any processor (no ruff/mypy section), so it is never linted in CI; add a `[processor.ruff]` section for `memcached_and_python`.

## Low

- `methods_of_intallation.txt` - file name typo ("intallation"); rename to `methods_of_installation.txt`.
- `memcached_and_python/exercise.txt:1` - "memchached" typo; also line 8 "Write does all the tools" should be "Write down all the tools".
- `methods_of_intallation.txt:10` - "rate" should be "rare"; line 44 "under my feed" should be "under my feet".
- `README.md:1` - the README is just the repo title and says nothing about the exercise, the docker `start.sh`/`stop.sh` helpers or the Python requirements; add a short description.
