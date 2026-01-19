import os
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
import dotenv
dotenv.load_dotenv()  # 默认加载 .env

llm = init_chat_model(
  model="google/gemini-2.0-flash-exp:free",
  model_provider="openai",
  base_url="https://openrouter.ai/api/v1",
  api_key=os.getenv("OPENROUTER_API_KEY"),
)

template = ChatPromptTemplate(
  [
    {"role": "system", "content": "用中文简短描述图片内容"},
    {"role": "user", "content": [{"image_url": "{image_url}"}]},
  ]
)

prompt = template.format_messages(
  image_url="https://img2.baidu.com/it/u=2976763563,2523722948&fm=253&app=138&f=JPEG?w=800&h=1200"
)

resp = llm.invoke(prompt)
print(resp.content) # 图片中是...