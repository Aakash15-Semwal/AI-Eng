import os
import requests
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

client = Groq(
    api_key=api_key
)
model = "openai/gpt-oss-20b"

def call_without_role(prompt):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    
    return response.choices[0].message.content

def call_with_role(role, prompt):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": role
            },
            {""
                "role": "user",
                "content": prompt
            }
        ]
    )
    
    return response.choices[0].message.content

def call_with_temperature(prompt, temperature):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=temperature
    )
    
    return response.choices[0].message.content

# print(call_without_role("Write a poem of 5 lines about the beauty of nature."))
# print(call_with_role(
#     "You are an Indian shopkeeper", 
#     "Write a poem of 5 lines about the beauty of nature."
# ))
print(call_with_temperature(
    "Write a poem of 5 lines about the beauty of nature.", 
    temperature=2
))