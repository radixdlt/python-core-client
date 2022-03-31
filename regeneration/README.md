# Regeneration README

We regenerate the client against a new spec

## Updating the client for a new Open API version

* Download https://search.maven.org/artifact/org.openapitools/openapi-generator-cli/5.2.1/jar as a jar, and put it in `regeneration/openapi-generator-cli-5.2.1.jar`
* Copy in the new core-api specification to `regeneration/core-api-openapi.yaml`
* Change openapi: 3.1.0 to openapi: 3.0.0 in its first line.
* Run `regeneration/regen-core-client.sh`

## Why we need custom generation

We use `allOf` throughout our specs, but the generated `ModelComposed` files by the default templates contain a few bugs,
notably this: https://github.com/OpenAPITools/openapi-generator/issues/11299

So we make use of custom templating to workaround these bugs:
* https://openapi-generator.tech/docs/templating/
* https://openapi-generator.tech/docs/customization

Any changes that have been made live in the `5.2.1-template-file-overrides` folder, and have been flagged up with a comment like the following:

```
{{! RADIX-MODIFICATION - Explanation }}
```

The source templates come from this folder: https://github.com/OpenAPITools/openapi-generator/tree/v5.2.1/modules/openapi-generator/src/main/resources/python
