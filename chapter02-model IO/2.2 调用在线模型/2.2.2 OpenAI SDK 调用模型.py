from openai import OpenAI
import dotenv
import os
dotenv.load_dotenv()

# 调试：检查环境变量是否正确加载
print(f"API Key: {os.getenv('OPENAI_API_KEY1')[:10] if os.getenv('OPENAI_API_KEY1') else 'Not set'}...")
print(f"Base URL: {os.getenv('OPENAI_BASE_URL')}")
print(f"Model Name: {os.getenv('OPENAI_MODEL_NAME')}")

client = OpenAI(
  base_url=os.getenv("OPENAI_BASE_URL"),
  api_key=os.getenv("OPENAI_API_KEY1"),
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[{"role": "user", "content": "将'你好'翻译成意大利语"}],
)

# 正确的访问方式
print(completion.choices[0].message.content)