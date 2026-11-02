import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

API_KEY=os.getenv("GROQ_API_KEY")

client = Groq(
    api_key=API_KEY
)

MODEL="openai/gpt-oss-20b"

# Creating a list of prompts
prompt_list = [
    "Good Morning",
    "Explain gravity in detail",
    "Write an essay of 1000 on musk deer"
]

# Executing multiple prompts using a for loop
for prompt in prompt_list:
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_completion_tokens=500
    )
    usage = response.usage
    print(f"Prompt: {prompt} ---> Input tokens: {usage.prompt_tokens}, Completion tokens: {usage.completion_tokens}, Total tokens: {usage.total_tokens}, Reason: {response.choices[0].finish_reason}")
    
    