# pip install langchain-tavily
import os
from langchain_tavily import TavilySearch
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model

# 定义模型
llm = init_chat_model(
  model="z-ai/glm-4.5-air:free",
  model_provider="openai",
  base_url="https://openrouter.ai/api/v1",
  api_key=os.getenv("OPENROUTER_API_KEY"),
)

# 定义 Tavily 搜索工具
search = TavilySearch(max_results=5)
tools = [search]

# 创建 Agent
agent = create_agent(
  model=llm, # 模型
  tools=tools, # 工具
  system_prompt="你是位助手，需要调用工具来帮助用户。", # 系统提示词
)

# 调用 Agent
res = agent.invoke(
  {"messages": [{"role": "user", "content": "今天北京的天气怎么样？"}]}
)
print(res)