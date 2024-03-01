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

#Extract and Output only Answer
generated_text = chat_completion.choices[0].message.content
print(generated_text)

#Output Full Response
generated_text = chat_completion
print(generated_text)
