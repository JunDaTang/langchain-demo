import asyncio
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client


async def streamablehttp_run():
    url = "http://127.0.0.1:8000/mcp" # /mcp路径是一个固定的路径
    # headers = {"Authorization": "Bearer sk-atguigu"}


    async with streamablehttp_client(url,) as (read, write, _):
        async with ClientSession(read, write) as session:
            # 初始化连接

            # 得到session之后，和stdio的方式是一样的
            await session.initialize()

            tools = await session.list_tools()
            print(tools)
            print()

            # 调用工具
            call_res = await session.call_tool("add", {"a": 1, "b": 2})
            print(call_res)
            print()


asyncio.run(streamablehttp_run())

