import os
from dotenv import load_dotenv
from openai import OpenAI

# Load OpenAI API Key from .env file
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Define your followup question
prompt = "Who is the first president of USA?."

# Initilize model and it will automatically pass API key via environment variable OPENAI_API_KEY
# Initialize OpenAI Chat Model
chat = ChatOpenAI()

# Send prompt question and get response from Model
chat_completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    stream=True,
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
    #temperature=0,                              # Optional
    #max_tokens=1,                               # Optional
    #response_format={ "type": "json_object" },  # Optional
)

#Display Response
stream = chat_completion.choices[0].message.content
for chunk in stream:
    print(chunk.choices[0].delta.content or "", end="")

