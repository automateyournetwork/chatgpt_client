import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_KEY")

client = OpenAI(api_key=api_key)

question = input('What is your question: ')

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": "You are a chatbot"},
            {"role": "user", "content": f"{ question }"},
        ]
    )

result = ''
for choice in response.choices:
    result += choice.message.content

print(f"We asked chatGPT { question } - Here Is there Answer:")
print("-----------------------------------------------------------------")
print(result)