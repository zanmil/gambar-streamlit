from openai import OpenAI
# Setel API key Anda 
openai.api_key = "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"

# Buat klien 
cresponse = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello!"}]
)
print(response.choices[0].message.content)
