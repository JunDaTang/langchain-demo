# pip install python-dotenv
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv() # 默认加载 .env

client = OpenAI()

completion = client.chat.completions.create(
  model="openai/gpt-oss-20b:free", 
  messages=[{"role": "user", "content": "将'你好'翻译成意大利语"}],
)

print(completion.choices[0].message.content)