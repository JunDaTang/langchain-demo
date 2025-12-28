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
  {"role": "system", "content": "你是一名数学家"},
  {"role": "user", "content": "请证明以下黎曼猜想"},
]
resp = llm.invoke(messages)
print(resp.content)