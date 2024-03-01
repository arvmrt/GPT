import os
from openai import OpenAI

prompt = "Enter your question here"

client = OpenAI(
    os.environ.get("OPENAI_API_KEY", "<your OpenAI API key if not set as env var>")
)

chat_completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    temperature=0,
    max_tokens=1,
    #response_format={ "type": "json_object" },
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
