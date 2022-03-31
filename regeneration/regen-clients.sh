#!/bin/sh

set -e

# NB - as currently written, this script has only been tested on Mac OSX
# In particular, Mac makes use of a variant of sed which might not work on other UNIX variants

SCRIPT_DIR="$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
cd "$SCRIPT_DIR"

java -jar ./openapi-generator-cli-5.2.1.jar \
    generate \
    -i "./system-api-openapi.yaml" \
    -g python \
    -o "../" \
    --additional-properties=packageName=system_client \
    -t "./5.2.1-template-file-overrides"

java -jar ./openapi-generator-cli-5.2.1.jar \
    generate \
    -i "./core-api-openapi.yaml" \
    -g python \
    -o "../" \
    --additional-properties=packageName=core_client \
    -t "./5.2.1-template-file-overrides"