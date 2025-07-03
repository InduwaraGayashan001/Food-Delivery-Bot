from openai import OpenAI
import os
from dotenv import load_dotenv
from src.prompt import *

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1-mini"

messages = [
    {
        "role": "system",
        "content":system_instruction,
    }
]

client = OpenAI(
    base_url=endpoint,
)

def ask_llm(prompt):
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message.content