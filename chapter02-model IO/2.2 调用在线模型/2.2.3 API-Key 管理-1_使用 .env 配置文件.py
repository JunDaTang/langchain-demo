# pip install python-dotenv
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv() # 默认加载 .env
os.getenv("OPENAI_API_KEY1")
os.getenv("OPENAI_BASE_URL")
client = OpenAI(
  base_url=os.getenv("OPENAI_BASE_URL"), # 平台提供的 URL
  api_key=os.getenv("OPENAI_API_KEY"), # 平台提供的 API Key
)

completion = client.chat.completions.create(
  model="openai/gpt-oss-20b:free", 
  messages=[{"role": "user", "content": "将'你好'翻译成意大利语"}],
)
print(completion.choices[0].message.content)
