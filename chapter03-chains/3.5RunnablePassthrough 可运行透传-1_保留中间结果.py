from langchain_core.runnables import RunnablePassthrough, RunnableParallel

chain = RunnableParallel(
  original=RunnablePassthrough(), # 保留中间结果
  word_count=lambda x: len(x),
)

result = chain.invoke("hello world")
print(result) # {'original': 'hello world', 'word_count': 11}