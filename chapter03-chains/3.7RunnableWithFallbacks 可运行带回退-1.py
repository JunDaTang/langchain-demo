import os
from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda

llm = init_chat_model(
  model="openai/gpt-oss-20b:free",
  model_provider="openai",
  base_url="https://openrouter.ai/api/v1",
  api_key=os.getenv("OPENROUTER_API_KEY"),
)

chain = PromptTemplate.from_template("hello") | llm
chain_with_fallback = chain.with_fallbacks([RunnableLambda(lambda x: "sorry")])

result = chain_with_fallback.invoke("1") # 提示词模板中没有需要填充的变量，会报错
print(result) # sorry