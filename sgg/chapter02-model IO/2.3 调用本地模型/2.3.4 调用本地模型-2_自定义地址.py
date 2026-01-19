# pip install langchain-ollama
from langchain_ollama import ChatOllama


ollama_llm = ChatOllama(
  model="deepseek-r1:7b",
  base_url="http://your-ip:port", # 自定义地址
)
messages = {"role": "user", "content": "你好，请介绍一下你自己"}
resp = ollama_llm.invoke(messages)
print(resp.content)