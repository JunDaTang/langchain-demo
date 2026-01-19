from langchain.tools import tool
from pydantic import BaseModel, Field

class FieldInfo(BaseModel):
  a: int = Field(description="第1个参数")
  b: int = Field(description="第2个参数")

@tool(
  name_or_callable="add_2_number",
  description="计算两整数之和",
  args_schema=FieldInfo, # 定义参数模式
)
def add_number(a: int, b: int) -> int:
  """两个整数相加"""
  return a + b

print(f"{add_number.name=}\n{add_number.description=}\n{add_number.args=}")

# add_number.name='add_2_number'
# add_number.description='计算两整数之和'
# add_number.args={'a': {'description': '第1个参数', 'title': 'A', 'type': 'integer'}, 'b': {'description': '第2个参数', 'title': 'B', 'type': 'integer'}}