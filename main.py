import os
from dotenv import load_dotenv

from agent import Agent
from tools import schema_tools
from prompts import PROMPT_SYSTEM

from huggingface_hub import InferenceClient

load_dotenv()

# Setup
HF_TOKEN = os.getenv('HF_TOKEN')
HF_MODEL=os.getenv('HF_MODEL')

client = InferenceClient(
    token=HF_TOKEN,
    model=HF_MODEL
)

agent = Agent(
    client=client,
    system=PROMPT_SYSTEM,
    tools=[schema_tools]
)

response = agent(message='Qual a temperatura em tokyo?')
print(response)