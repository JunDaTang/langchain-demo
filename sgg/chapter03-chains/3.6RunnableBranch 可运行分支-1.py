from langchain_core.runnables import RunnableBranch

branch = RunnableBranch(
  (lambda x: isinstance(x, str), lambda x: x.upper()),
  (lambda x: isinstance(x, int), lambda x: x + 1),
  (lambda x: isinstance(x, float), lambda x: x * 2),
  lambda x: "goodbye",
)

result = branch.invoke("hello")
print(result) # HELLO

result = branch.invoke(None)
print(result) # goodbye