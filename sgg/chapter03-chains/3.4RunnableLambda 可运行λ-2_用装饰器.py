from langchain_core.runnables import RunnableLambda

@RunnableLambda
def total_len(x):
  return len(x["text1"]) + len(x["text2"])

chain = {
  "text1": lambda x: x + " world",
  "text2": lambda x: x + ", how are you",
} | total_len

result = chain.invoke("hello")
print(result) # 29