import os
from openai import OpenAI

prompt = "Hi there! Thanks for using OpenAI GPT Model."

# Setup a environment variable on Linux Server with name OPENAI_API_KEY and save the key in there. Make sure to run source command to enable the variable.
client = OpenAI(
    os.environ.get("OPENAI_API_KEY")
)

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
