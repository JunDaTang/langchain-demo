import os
from langchain.tools import tool
from langchain.chat_models import init_chat_model

@tool
def query_user_info(user_id: int) -> str:
  """查询用户信息"""
  return {1001: "Jack", 1002: "Tom", 1003: "Alice"}[user_id]

llm = init_chat_model(
  model="z-ai/glm-4.5-air:free",
  model_provider="openai",
  base_url="https://openrouter.ai/api/v1",
  api_key=os.getenv("OPENROUTER_API_KEY"),
)

# 为模型提供工具
tools = [query_user_info]
llm_with_tools = llm.bind_tools(tools)
resp = llm_with_tools.invoke("帮我查下1001用户的信息")
print(resp)
# content='\n\n我来帮您查询1001用户的信息。\n'
# additional_kwargs={'tool_calls': [{'id': '...', 'function': {'arguments': '{"user_id": 1001}', 'name': 'query_user_info'}

# 返回的响应中 additional_kwargs 参数中包括了工具调用的信息，此时还没有调用工具，只是返回了要调用的工具及参数

# 手动执行工具
for tool_call in resp.tool_calls:
  tool_name = tool_call["name"] # 获取工具名称
  tool_args = tool_call["args"] # 获取工具参数
  tool_result = globals()[tool_name].invoke(tool_args) # 执行工具
  print(tool_name, tool_args, tool_result)