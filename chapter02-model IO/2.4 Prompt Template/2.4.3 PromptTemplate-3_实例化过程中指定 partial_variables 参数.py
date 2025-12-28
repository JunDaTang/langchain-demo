from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
  template="{foo} {bar}",
  input_variables=["foo", "bar"],
  partial_variables={"foo": "hello"}, # 预先定义部分变量
)

prompt = template.format(bar="world")

print(prompt) # hello world