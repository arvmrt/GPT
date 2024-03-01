import os
from openai import OpenAI

prompt = "Who is the first president of USA?."

'''
Setup a environment variable on Linux Server with name OPENAI_API_KEY and save the key in there. Make sure to run source command to enable the variable.
# vi .bashrc
export OPENAI_API_KEY="<Input your API Key Here>"  #Add this line at end of file and save file.
# source .bashrc
'''
# Initilize model and it will automatically pass API key via environment variable OPENAI_API_KEY
client = OpenAI()

# Create the Model
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
