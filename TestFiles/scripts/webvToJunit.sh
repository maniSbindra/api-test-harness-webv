#!/bin/bash

set -x

COMPOSE_LOG_FILE=$1
OUT_XML_FILE=$2
SCRIPT_DIR=$3

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# Filter webv json results from docker-compose logs and convert into single JSON array
cat $COMPOSE_LOG_FILE | grep '{"date":' | sed 's/\(^[^{]*{\)\(.*\)/{\2/g' | sed 's/$/,/g' | sed '1 s/^/[/g' | sed '$s/\,$/]/g' > $DIR/input.json

# convert web validate results into JUnit format so that results can be publised to Azure DevOps Dashboard
python3 $SCRIPT_DIR/webvtoJunit.py $DIR/input.json $OUT_XML_FILE