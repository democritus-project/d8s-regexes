#!/usr/bin/env bash

set -euxo pipefail

echo "Running linters and formatters..."

isort democritus_regexes/ tests/

black democritus_regexes/ tests/

mypy democritus_regexes/ tests/

pylint --fail-under 9 democritus_regexes/*.py

flake8 democritus_regexes/ tests/

bandit -r democritus_regexes/

# we run black again at the end to undo any odd changes made by any of the linters above
black democritus_regexes/ tests/
