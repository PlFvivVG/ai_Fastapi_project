from google import  genai




client = genai.Client(api_key='AIzaSyCF_wKBM5kTmZfPTH7C9g8ZU8xoW67Tg7E')

def get_answer_from_gemeni(prompt: str):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text

