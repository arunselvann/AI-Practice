"""Module to explain how to call a gpt model"""
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

completion = client.chat.completions.create(
    model="gpt-4.1",
    messages=[
        {
            "role": "system", 
            "content": "You're a helpful assistant."},
        {
            "role": "user",
            "content": "Write a limerick about the Python programming language.",
        },
    ]
)

response = completion.choices[0].message.content
print(response)
