from mcp.server.fastmcp import FastMCP

#
# 创建 MCP 实例
mcp = FastMCP("Demo")

# 为 MCP 实例添加工具
@mcp.tool()
def add(a: int, b: int) -> int:
    return a + b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    return a * b

if __name__ == '__main__':
    # transport参数，传值为streamable-http
    mcp.settings.host = "0.0.0.0"
    mcp.run(transport="streamable-http")