# pip install langchain_mcp_adapters
import os
import asyncio
from urllib.parse import urlencode
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain_mcp_adapters.client import MultiServerMCPClient

# 配置 MCP 客户端
mcp_client = MultiServerMCPClient(
  {
    "WebSearch": {
      "transport": "sse",
      "url": "https://dashscope.aliyuncs.com/api/v1/mcps/WebSearch/sse",
      "headers": {"Authorization": f"Bearer {os.getenv('DASHSCOPE_API_KEY')}"},
    }, # https://bailian.console.aliyun.com/?tab=mcp#/mcp-market/detail/WebSearch
    "RailService": {
      "transport": "streamable_http",
      "url": f"{'https://server.smithery.ai/@DeniseLewis200081/rail/mcp'}?{urlencode({'api_key': os.getenv('SMITHERY_API_KEY')})}",
    }, # https://smithery.ai/server/@DeniseLewis200081/rail
  }
)
# 获取工具
tools = asyncio.run(mcp_client.get_tools())

# 定义模型
llm = init_chat_model(
  model="z-ai/glm-4.5-air:free",
  model_provider="openai",
  base_url="https://openrouter.ai/api/v1",
  api_key=os.getenv("OPENROUTER_API_KEY"),
)

# 创建 Agent
agent = create_agent(model=llm, tools=tools)

# 调用 Agent
async def main():
  async for chunk in agent.astream(
    {
      "messages": [
        {"role": "system", "content": "你是位助手，需要调用工具来帮助用户。"},
        {
          "role": "user",
          "content": "北京今天天气怎么样，要是还不错的话，帮我看看今天上海到北京的车票",
        },
      ]
    }
  ):
    print(chunk, end="\n\n")

asyncio.run(main())