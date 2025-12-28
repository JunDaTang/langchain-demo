import os
from typing import TypedDict, Annotated
from langchain.chat_models import init_chat_model

llm = init_chat_model(
  model="openai/gpt-oss-20b:free",
  model_provider="openai",
  base_url="https://openrouter.ai/api/v1",
  api_key=os.getenv("OPENROUTER_API_KEY"),
)

class Animal(TypedDict):
  animal: Annotated[str, "动物"]
  emoji: Annotated[str, "表情"]

class AnimalList(TypedDict):
  animals: Annotated[list[Animal], "动物与表情列表"]

messages = [{"role": "user", "content": "任意生成三种动物，以及他们的 emoji 表情"}]

llm_with_structured_output = llm.with_structured_output(AnimalList)
resp = llm_with_structured_output.invoke(messages)
print(resp)
# {'animals': [{'animal': '猫', 'emoji': '🐱'}, {'animal': '老虎', 'emoji': '🐯'}, {'animal': '企鹅', 'emoji': '🐧'}]}