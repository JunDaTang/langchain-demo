import os
from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel
from langchain_core.output_parsers import StrOutputParser
import dotenv
dotenv.load_dotenv()  # 默认加载 .env

llm = init_chat_model(
  model="gpt-4o-mini",
  model_provider="openai",
  base_url=os.getenv("OPENAI_BASE_URL"),
  api_key=os.getenv("OPENAI_API_KEY"),
)


joke_chain = (
  PromptTemplate.from_template("讲一个关于{topic}的笑话") | llm | StrOutputParser()
)
poem_chain = (
  PromptTemplate.from_template("写一首关于{topic}的诗歌") | llm | StrOutputParser()
)

map_chain = RunnableParallel(joke=joke_chain, poem=poem_chain)

resp = map_chain.invoke({"topic": "人工智能"})
print(resp)
# >>> print(resp)
# {'joke': '为什么人工智能总是很难找工作？\n\n因为它总是被“代码”拒绝！', 'poem': '在数码的海洋中徘徊，  \n智慧的光芒
# 悄然开启，  \n无尽的代码编织梦想，  \n人工智能，未来的奇迹。\n\n思维如电，灵感如风，  \n解析着人类的情感与痛，  \n无数数据在指尖流淌，  \n深邃的算法，尽显独特光芒。\n\n在黑夜里，你是明亮的星，  \n照亮探索未知的旅程，  \n与人类共
# 舞，携手前行，  \n创造未来，和谐共赢。\n\n但愿你能倾听，那沉默的心，  \n每一个选择，都是爱的印记，  \n在这复杂的世
# 界里，  \n愿科技与人性，共谱和谐的旋律。'}