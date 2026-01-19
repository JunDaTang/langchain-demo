from langchain_core.prompts import ChatPromptTemplate

template = ChatPromptTemplate.from_messages(
  [
    ("system", "你是一个助手。"),
    ("placeholder", "{conversation}"),
    # 等同于 MessagesPlaceholder(variable_name="conversation", optional=True)
  ]
)

prompt = template.format_messages(
  conversation=[
    ("human", "你好！"),
    ("ai", "想让我帮你做些什么？"),
    ("human", "能帮我做一个冰淇凌吗？"),
    ("ai", "不能"),
  ]
)
print(prompt)
# [
#   SystemMessage(content="你是一个助手。", ...),
#   HumanMessage(content="你好！", ...),
#   AIMessage(content="想让我帮你做些什么？", ...),
#   HumanMessage(content="能帮我做一个冰淇凌吗？", ...),
#   AIMessage(content="不能", ...),
# ]