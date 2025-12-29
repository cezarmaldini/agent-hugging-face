import os
from dotenv import load_dotenv

from huggingface_hub import InferenceClient

load_dotenv()

HF_TOKEN = os.getenv('HF_TOKEN')
HF_MODEL=os.getenv('HF_MODEL')

client = InferenceClient(
    api_key=HF_TOKEN,
    model=HF_MODEL 
)

message = input('Faça sua pergunta:')

response = client.chat.completions.create(
    messages=[
        {'role': 'user', 'content': message}
    ]
)

print(response.choices[0].message.content)