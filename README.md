# Alt Text Generator OpenAI

A Docker image that automatically generates and applies alternative image descriptions to PDF files using PDFix SDK and OpenAI.

## Table of Contents

- [Alt Text Generator OpenAI](#alt-text-generator-openai)
  - [Table of Contents](#table-of-contents)
  - [Getting Started](#getting-started)
  - [Run using Command Line Interface](#run-using-command-line-interface)
  - [Run Description Generation using REST API](#run-description-generation-using-rest-api)
    - [Exporting Configuration for Integration](#exporting-configuration-for-integration)
  - [License \& libraries used](#license--libraries-used)
  - [Help \& Support](#help--support)
  

## Getting Started

To use this Docker application, you'll need to have Docker installed on your system. If Docker is not installed, please follow the instructions on the [official Docker website](https://docs.docker.com/get-docker/) to install it.


## Run using Command Line Interface

To run the docker container as CLI, you should share the folder containing the PDF for processing using the `-i` parameter. In this example, the current folder is used.

```bash 
docker run -v $(pwd):/data/ -w /data/ pdfix/alt-text-openai:latest detect -i document.pdf -o out.pdf --openai <api_key> 
```

With PDFix License add these arguments. 
```bash
--name ${LICENSE_NAME} --key ${LICENSE_KEY}
```

First run will pull the docker image, which may take some time. Make your own image for more advanced use.

For more detailed information about the available command-line arguments, you can run the following command:

```bash
docker run --rm pdfix/alt-text-openai:latest --help
```

## Run Description Generation using REST API
Comming soon. Please contact us.

### Exporting Configuration for Integration
To export the configuration JSON file, use the following command:
```bash
docker run -v $(pwd):/data -w /data --rm pdfix/alt-text-openai:latest config -o config.json
```

## License & libraries used
- PDFix SDK - https://pdfix.net/terms
- OpenAI API - https://openai.com/policies/

Trial version of the PDFix SDK may apply a watermark on the page and redact random parts of the PDF including the scanned image in background. Contact us to get an evaluation or production license.

## Help & Support
To obtain a PDFix SDK license or report an issue please contact us at support@pdfix.net.
For more information visit https://pdfix.net


