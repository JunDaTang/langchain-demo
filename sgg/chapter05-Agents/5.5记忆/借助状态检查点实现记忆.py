import os
import datetime
from langchain_tavily import TavilySearch
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langgraph.checkpoint.memory import InMemorySaver
import dotenv
dotenv.load_dotenv()

# 定义模型
llm = init_chat_model(
  model="deepseek-chat",
  model_provider="deepseek",
  base_url=os.getenv("DEEPSEEK_BASE_URL"),
  api_key=os.getenv("DEEPSEEK_API_KEY"),
)
os.environ["LANGSMITH_PROJECT"] = "agent-with-memory"

# 定义 Tavily 搜索工具
search = TavilySearch(max_results=5)
tools = [search]


# 创建 Agent
agent = create_agent(
  model=llm,
  tools=tools,
  checkpointer=InMemorySaver(),
)

# 调用
for chunk in agent.stream(
  input={
    "messages": [
      {
        "role": "system",
        "content": f"当前时间：{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
      },
      {"role": "user", "content": "今天北京天气怎么样？"},
    ]
  },
  config={"configurable": {"thread_id": "1"}},
):
  print(chunk, end="\n\n")

for chunk in agent.stream(
  input={
    "messages": [
      {
        "role": "system",
        "content": f"当前时间：{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
      },
      {"role": "user", "content": "上海呢？"},
    ]
  },
  config={"configurable": {"thread_id": "1"}},
):
  print(chunk, end="\n\n")