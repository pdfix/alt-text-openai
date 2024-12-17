import httpx
from openai import OpenAI


def alt_description(img: str, api_key: str, lang: str):
    client = OpenAI(
        api_key=api_key, timeout=httpx.Timeout(None, connect=10, read=60, write=30)
    )

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": f"Generate alternate description for the image in {lang} language",
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{img}",
                        },
                    },
                ],
            },
        ],
        max_tokens=100,
    )

    return response.choices[0]
