import json
from pathlib import Path

from ai import alt_description


def alt_text_json(
    input_path: str,
    output_path: str,
    api_key: str,
    lang: str,
) -> None:
    """Run OpenAI for alternate text description.

    Parameters
    ----------
    input_path : str
        Input path to the JSON file.
    output_path : str
        Output path for saving the JSON file.
    api_key : str
        OpenAI API key.
    lang : str
        Alternate description language.

    Raises
    ------
    FileNotFoundError
        Path to the input file does not exist.
    KeyError
        image attribute is not present in the JSON file.

    """
    json_file_path = Path(input_path)

    if not json_file_path.is_file():
        raise FileNotFoundError(f"The file {json_file_path} does not exist.")

    with open(json_file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    if "image" not in data:
        raise KeyError("The 'image' attribute is not present in the JSON file.")

    base64_image = data["image"]

    response = alt_description(base64_image, api_key, lang)

    alt = response.message.content
    output_data: dict[str, str] = {"text": alt}

    output_file_path = Path(output_path)
    with open(output_file_path, "w", encoding="utf-8") as output_file:
        json.dump(output_data, output_file, indent=2, ensure_ascii=False)
