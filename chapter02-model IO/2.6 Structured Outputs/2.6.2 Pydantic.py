import os
from pydantic import BaseModel, Field
from langchain.chat_models import init_chat_model

llm = init_chat_model(
  model="openai/gpt-oss-20b:free",
  model_provider="openai",
  base_url="https://openrouter.ai/api/v1",
  api_key=os.getenv("OPENROUTER_API_KEY"),
)

class Animal(BaseModel):
  animal: str = Field(description="动物")
  emoji: str = Field(description="表情")

class AnimalList(BaseModel):
  animals: list[Animal] = Field(description="动物与表情列表")

messages = [{"role": "user", "content": "任意生成三种动物，以及他们的 emoji 表情"}]

llm_with_structured_output = llm.with_structured_output(AnimalList)
resp = llm_with_structured_output.invoke(messages)
print(resp)
# animals=[Animal(animal='猫', emoji='🐱'), Animal(animal='乌龟', emoji='🐢'), Animal(animal='企鹅', emoji='🐧')]