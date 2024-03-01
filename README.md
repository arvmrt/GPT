# gtp

# Install openai package 
pip install openai

# Write your first code

from openai import OpenAI
client = OpenAI(
    os.environ.get("OPENAI_API_KEY")
)

chat_completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    #response_format={ "type": "json_object" },  #Optional if you need output in JSON format
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ]
)

#Extracted Response
generated_text = chat_completion.choices[0].message.content
print(generated_text)

#Full Response
generated_text = chat_completion
print(generated_text)

