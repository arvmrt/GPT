import os
from openai import OpenAI

prompt = "Who is the first president of USA?."

'''
Setup a environment variable on Linux Server with name OPENAI_API_KEY and save the API key. Make sure to run source command to enable the variable.
# vi .bashrc
export OPENAI_API_KEY="<Input your API Key Here>"  #Add this line at end of file and save file.
# source .bashrc
'''
client = OpenAI()

chat_completion = client.chat.completions.create(
    model="gpt-3.5-turbo",    
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

#Extract only Answer from the Response
generated_text = chat_completion.choices[0].message.content
print(generated_text)

#Display Full Response
generated_text = chat_completion
print(generated_text)
