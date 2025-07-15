from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

prompt_user = input("EU: ")
prompt_system = "Você é um especialista em qualquer assunto."

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"), base_url="https://api.deepseek.com"
)

stream = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": prompt_system},
        {"role": "user", "content": prompt_user},
    ],
    max_tokens=300,
    temperature=0.7,
    stream=True,
)

if stream:
    print("Resposta: ")
    for chunk in stream:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="", flush=True)
