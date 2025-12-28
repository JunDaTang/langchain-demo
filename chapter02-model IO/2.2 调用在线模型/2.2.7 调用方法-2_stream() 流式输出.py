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
# 使用 stream() 方法流式输出
for chunk in llm.stream(messages):
  # 逐个打印内容块，并刷新缓冲区以即时显示内容
  
  print(chunk.content, end="", flush=True)