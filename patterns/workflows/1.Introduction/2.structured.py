"""Module to get response in structured format from a gpt model"""
import os
from openai import OpenAI
from pydantic import BaseModel

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class CalendarEvent(BaseModel):
    """Event Response schema"""
    name: str
    date: str
    participants: list[str]

completion = client.beta.chat.completions.parse(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "Extract the event information."},
        {
            "role": "user",
            "content": "Alice and Bob are going to a science fair on Friday.",
        },
    ],
    response_format=CalendarEvent,
)

event = completion.choices[0].message.parsed
print(event.name)
print(event.date)
print(event.participants)
