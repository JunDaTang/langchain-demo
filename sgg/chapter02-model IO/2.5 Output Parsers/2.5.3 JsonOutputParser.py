import os
from pydantic import BaseModel, Field
from langchain.chat_models import init_chat_model
from langchain_core.output_parsers import JsonOutputParser
import dotenv
dotenv.load_dotenv()  # 默认加载 .env

llm = init_chat_model(
  model="openai/gpt-oss-20b:free",
  model_provider="openai",
  base_url="https://openrouter.ai/api/v1",
  api_key=os.getenv("OPENROUTER_API_KEY"),
)

class Prime(BaseModel):
  prime: list[int] = Field(description="素数")
  count: list[int] = Field(description="小于该素数的素数个数")

json_parser = JsonOutputParser(pydantic_object=Prime)
messages = [
  {"role": "system", "content": json_parser.get_format_instructions()},
  {
    "role": "user",
    "content": "任意生成5个1000-100000之间素数，并标出小于该素数的素数个数",
  },
]

resp = llm.invoke(messages)
json_resp = json_parser.invoke(resp)
print(json_resp)
# {'prime': [1009, 2003, 3001, 4001, 5003], 'count': [168, 303, 430, 584, 669]}