import os
import json
from pydantic import BaseModel
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")
MODEL = "openai/gpt-oss-20b"

client = Groq(
    api_key=API_KEY
)

class Ticket(BaseModel):
    name: str
    email: str
    phone: int | None
    problem: str

schema = Ticket.model_json_schema()
    
system_prompt = f"""
You are a customer support agent. Use the following JSON schema to understand the structure of the ticket {schema} and give a JSON output.
"""
user_message = "Hello my name is John Doe, I am a software developer and I am having issues with my laptop which i just bought. I like ice cream and my favorite color is blue. My email is john.doe@example.com and contact is 12345"

messages = [
    {
        "role": "system",
        "content": system_prompt
    },
    {
        "role": "user",
        "content": user_message
    }
]

response = client.chat.completions.create(
    model=MODEL,
    messages=messages,
    response_format={
        "type": "json_object"
    }
)

raw_json = response.choices[0].message.content
print(raw_json)


data_file = json.loads(raw_json)
ticket = Ticket(**data_file)

print(ticket.name)
print(ticket.email)
print(ticket.problem)