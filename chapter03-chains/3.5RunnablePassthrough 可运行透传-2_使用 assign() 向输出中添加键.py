from langchain_core.runnables import RunnablePassthrough

chain = {
  "text1": lambda x: x + " world",
  "text2": lambda x: x + ", how are you",
} | RunnablePassthrough.assign(word_count=lambda x: len(x["text1"] + x["text2"]))

result = chain.invoke("hello")
print(result)

# {'text1': 'hello world', 'text2': 'hello, how are you', 'word_count': 29}