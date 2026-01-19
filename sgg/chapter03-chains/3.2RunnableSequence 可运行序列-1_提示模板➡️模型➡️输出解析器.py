import os
from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import dotenv
dotenv.load_dotenv()  # 默认加载 .env

prompt_template = PromptTemplate(
  template="讲一个关于{topic}的笑话",
  input_variables=["topic"],
)

llm = init_chat_model(
  model="gpt-4o-mini",
  model_provider="openai",
  base_url=os.getenv("OPENAI_BASE_URL"),
  api_key=os.getenv("OPENAI_API_KEY"),
)


parser = StrOutputParser()

# chain = runnable1 | runnable2 等同于 chain = RunnableSequence([runnable1, runnable2])
chain = prompt_template | llm | parser


resp = chain.invoke({"topic": "人工智能"})
print(resp)
# >>> print(resp)
# 为什么人工智能从不感到孤独？

# 因为它总是有"数据"陪伴！