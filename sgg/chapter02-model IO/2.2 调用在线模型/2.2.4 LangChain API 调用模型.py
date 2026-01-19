import os
from langchain.chat_models import init_chat_model
from langchain.messages import SystemMessage, HumanMessage, AIMessage
import dotenv
dotenv.load_dotenv()  # 默认加载 .env

llm = init_chat_model(
  model="openai/gpt-oss-20b:free",
  model_provider="openai",
  base_url="https://openrouter.ai/api/v1",
  api_key=os.getenv("OPENROUTER_API_KEY"),
)


messages = [
  SystemMessage(content="你是一个诗人"),
  HumanMessage(content="写一首关于春天的诗"),
]
resp = llm.invoke(messages)
print(type(resp)) # <class 'langchain_core.messages.ai.AIMessage'>
print(resp.content)