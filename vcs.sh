#!/bin/sh


set -e # Exit early if any commands fail

# - Edit this to change how your program runs locally
PYTHONPATH=$(dirname $0)/app exec python3 -m app.main "$@"
