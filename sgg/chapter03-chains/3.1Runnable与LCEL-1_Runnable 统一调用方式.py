from langchain_core.prompts import PromptTemplate
import os
from langchain.chat_models import init_chat_model
from langchain_core.messages.base import BaseMessage
from langchain_core.messages import HumanMessage
from langchain_core.output_parsers import StrOutputParser
import dotenv
dotenv.load_dotenv()  # 默认加载 .env

prompt = PromptTemplate.from_template("说一下关于{topic}的一句话小笑话。")

model = init_chat_model(
  model="gpt-4o-mini",
  model_provider="openai",
  base_url=os.getenv("OPENAI_BASE_URL"),
  api_key=os.getenv("OPENAI_API_KEY"),
)

parser = StrOutputParser()

# 方法1：传统分步调用（使用format/generate/parse）
prompt_text = prompt.format(topic="猫")  # 生成提示词文本
# 注意：generate方法通常用于批量处理，这里使用invoke更合适
# 如果要使用generate，需要传递正确的消息格式
messages: list[list[BaseMessage]] = [[HumanMessage(content=prompt_text)]]  # 添加类型注解
model_out = model.generate(messages)  # 现在类型正确了
result = parser.parse(model_out.generations[0][0].text)  # 正确解析结果
print(f"传统方法结果: {result}")

# 传统方法结果: 为什么猫总是坐在电脑键盘上？因为它们想要“猫”博个好位置！


# 方法2：使用invoke的统一调用方式
prompt_result = prompt.invoke({"topic": "猫"})  # 方法1
model_result = model.invoke(prompt_result)  # 方法2
final_result = parser.invoke(model_result)  # 方法3
print(f"统一调用结果: {final_result}")

# 统一调用结果: 为什么猫喜欢在电脑上走来走去？
# 因为它们想掌握“鼠标”的使用技巧！



# 方法3：LCEL管道式调用
chain = prompt | model | parser  # 用管道符组合
chain_result = chain.invoke({"topic": "猫"})  # 所有组件统一用invoke
print(f"LCEL管道结果: {chain_result}")

# LCEL管道结果: 为什么猫总是喜欢坐在计算机键盘上？因为它们想要“控制”一切！