from langchain_core.prompts import ChatPromptTemplate

template = ChatPromptTemplate(
  [
    ("system", "你是一个AI开发工程师，你的名字是{name}。"),
    ("human", "你能帮我做什么?"),
    ("ai", "我能开发很多{thing}。"),
    ("human", "{user_input}"),
  ]
)
# prompt = template.format(name="小谷AI", thing="AI", user_input="行")
prompt = template.invoke({"name": "小谷AI", "thing": "AI", "user_input": "行"})
print(prompt)
# messages=[
# SystemMessage(content="你是一个AI开发工程师，你的名字是小谷AI。",...),
# HumanMessage(content="你能帮我做什么?", ...),
# AIMessage(content="我能开发很多AI。", ...),
# HumanMessage(content="行", ...),
# ]