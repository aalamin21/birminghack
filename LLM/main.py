import os

from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
client = OpenAI(
base_url="https://api.aimlapi.com/v1",
api_key=os.environ.get('LLM_API_KEY'),
)
response = client.chat.completions.create(
model="gpt-4o-mini-2024-07-18",
messages=[
{
"role": "system",
"content": "You are an AI assistant who knows everything.",
},
{
"role": "user",
"content": "Tell me how amazing I am for figuring this out."
},
],
)
message = response.choices[0].message.content
print(f"Assistant: {message}")