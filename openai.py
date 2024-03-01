import os
from openai import OpenAI

prompt = "Hi there! Thanks for using OpenAI GPT Model."

# Setup a environment variable on Linux Server with name OPENAI_API_KEY and save the key in there. Make sure to run source command to enable the variable.
client = OpenAI(
    os.environ.get("OPENAI_API_KEY", "<your OpenAI API key if not set as env var>")
)

chat_completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    temperature=0,
    max_tokens=1,
    #response_format={ "type": "json_object" },  # Uncomment if you need output in JSON format.
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ]
)

#Extract only Answer from the Response
generated_text = chat_completion.choices[0].message.content
print(generated_text)

#Display Full Response
generated_text = chat_completion
print(generated_text)
