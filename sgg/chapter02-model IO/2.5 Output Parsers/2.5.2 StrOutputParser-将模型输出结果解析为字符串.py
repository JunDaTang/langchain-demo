import os
from langchain.chat_models import init_chat_model
from langchain_core.output_parsers import StrOutputParser
import dotenv
dotenv.load_dotenv()  # 默认加载 .env

llm = init_chat_model(
  model="openai/gpt-oss-20b:free",
  model_provider="openai",
  base_url="https://openrouter.ai/api/v1",
  api_key=os.getenv("OPENROUTER_API_KEY"),
)

messages = [
  {"role": "system", "content": "你是一个机器人"},
  {"role": "user", "content": "你好"},
]

resp = llm.invoke(messages)
print(resp) # content='你好！有什么我可以帮忙的吗？' additional_kwargs=......

str_resp = StrOutputParser().invoke(resp)
print(str_resp) # 你好！有什么我可以帮忙的吗？