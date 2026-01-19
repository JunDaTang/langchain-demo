from langchain_core.runnables import RunnableLambda

chain = {
  "text1": lambda x: x + " world",
  "text2": lambda x: x + ", how are you",
} | RunnableLambda(lambda x: len(x["text1"]) + len(x["text2"]))

result = chain.invoke("hello")
print(result) # 29