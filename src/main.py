import base64
import requests
import argparse
import os
import sys
from openai import OpenAI


# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def alt_description(api_key: str):
    # Getting the base64 string
    base64_image = encode_image("img_10.jpg")
    print("Using api key: {}".format(api_key))
    client = OpenAI(api_key=api_key)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Generate alternate description for the image",
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}",
                        },
                    },
                ],
            }
        ],
        max_tokens=300,
    )

    print(response.choices[0])


def main():
    parser = argparse.ArgumentParser(
        description="Process a PDF or image file with Tesseract OCR"
    )
    parser.add_argument("-i", "--input", type=str, help="The input PDF file")
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        help="The output PDF file",
    )

    parser.add_argument("--name", type=str, default="", help="Pdfix license name")
    parser.add_argument("--key", type=str, default="", help="Pdfix license key")
    parser.add_argument("--openai", type=str, default="", help="OpenAI API key")
    args = parser.parse_args()

    if not args.input or not args.output or not args.openai:
        parser.error(
            "The following arguments are required: -i/--input, -o/--output, --openai"
        )

    input_file = args.input
    output_file = args.output

    if not os.path.isfile(input_file):
        sys.exit(f"Error: The input file '{input_file}' does not exist.")
        return

    if input_file.lower().endswith(".pdf") and output_file.lower().endswith(".pdf"):
        try:
            desc = alt_description(args.openai)
            # print(desc)
        except Exception as e:
            sys.exit("Failed to run OCR: {}".format(e))

    else:
        print("Input and output file must be PDF")


if __name__ == "__main__":
    main()
