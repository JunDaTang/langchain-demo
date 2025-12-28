import os
import time
import asyncio
from langchain.chat_models import init_chat_model
import dotenv
dotenv.load_dotenv()  # 默认加载 .env

llm = init_chat_model(
  model="openai/gpt-oss-20b:free",
  model_provider="openai",
  base_url="https://openrouter.ai/api/v1",
  api_key=os.getenv("OPENROUTER_API_KEY"),
)

messagess = [
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

async def async_invoke():
  tasks = [llm.ainvoke(messages) for messages in messagess]
  return await asyncio.gather(*tasks)

start_time = time.time()

resps = asyncio.run(async_invoke())
print(resps)

end_time = time.time()
print(f"Total time: {end_time - start_time}")
# Total time: 8.280137062072754