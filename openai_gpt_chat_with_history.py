import os
from openai import OpenAI

# Initilize model and it will automatically pass API key via environment variable OPENAI_API_KEY
client = OpenAI()

# Create a list with some sample history messages. Note following format is must for it to work.
example_messages = [
    {
        "role": "user",
        "content": "Who is the first president of USA?",
    },
    {
        "role": "system",
        "content": "George Washington",
    },
    {
        "role": "user",
        "content": "and who was 16th",
    },
    {
        "role": "system",
        "content": "Abraham Lincoln",
    },
    {
        "role": "user",
        "content": "and who was after him ?",
    },    
]

# Create the Model
chat_completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    #temperature=0,                              # Optional
    #max_tokens=1,                               # Optional
    #response_format={ "type": "json_object" },  # Optional
    messages=example_messages
)

#Extract only Answer from the Response
generated_text = chat_completion.choices[0].message.content
print(generated_text)

print("-----------------------------------------------------------")

#Display Full Response
generated_text = chat_completion
print(generated_text)
