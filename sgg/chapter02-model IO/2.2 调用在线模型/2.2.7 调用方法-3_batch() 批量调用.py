import os
from langchain.chat_models import init_chat_model
import dotenv
dotenv.load_dotenv()  # 默认加载 .env

llm = init_chat_model(
  model="openai/gpt-oss-20b:free",
  model_provider="openai",
  base_url="https://openrouter.ai/api/v1",
  api_key=os.getenv("OPENROUTER_API_KEY"),
)

messages = [
  [
    {"role": "system", "content": "你是一位诗人"},
    {"role": "user", "content": "写一首关于春天的诗"},
  ],
  [
    {"role": "system", "content": "你是一位诗人"},
    {"role": "user", "content": "写一首关于夏天的诗"},
  ],
  [
    {"role": "system", "content": "你是一位诗人"},
    {"role": "user", "content": "写一首关于秋天的诗"},
  ],
]
resp = llm.batch(messages) # 批量调用,返回一个消息列表
print(resp)