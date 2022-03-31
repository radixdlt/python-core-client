java -jar ./openapi-generator-cli-5.2.1.jar \
    generate \
    -i "./api.yaml" \
    -g python \
    -o "../" \
    -c "./config-custom.yaml"