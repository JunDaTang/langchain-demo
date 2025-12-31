# pip install mcp
import asyncio
from mcp.client.stdio import stdio_client
from mcp import ClientSession, StdioServerParameters
import dotenv
dotenv.load_dotenv()

async def stdio_run():
  server_params = StdioServerParameters(
    command="python",
    args=[r"chapter05-Agents\5.6MCP\5.6.5MCP SDK-1_Stdio 服务端.py"],
  )

  async with stdio_client(server_params) as (read, write):
    async with ClientSession(read, write) as session:
      # 初始化连接
      await session.initialize()

      # 获取可用工具
      tools = await session.list_tools()
      print(tools)
      print()

      # 调用工具
      call_res = await session.call_tool("add", {"a": 1, "b": 2})
      print(call_res)
      print()

      # 获取可用资源
      resources = await session.list_resources()
      print(resources)
      print()

      # 调用资源
      read_res = await session.read_resource("greeting://default")
      print(read_res)
      print()

      # 获取可用提示
      prompts = await session.list_prompts()
      print(prompts)
      print()

      # 调用提示
      get_res = await session.get_prompt("greet_user", {"name": "Jack"})
      print(get_res)
      print()

asyncio.run(stdio_run())