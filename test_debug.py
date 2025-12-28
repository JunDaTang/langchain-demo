# 调试脚本
from openai import OpenAI
import dotenv
import os
import json

dotenv.load_dotenv()

print("环境变量检查:")
print(f"OPENAI_API_KEY 存在: {'OPENAI_API_KEY' in os.environ}")
print(f"OPENAI_BASE_URL 存在: {'OPENAI_BASE_URL' in os.environ}")
print(f"OPENAI_BASE_URL 值: {os.getenv('OPENAI_BASE_URL')}")

client = OpenAI(
  base_url=os.getenv("OPENAI_BASE_URL"), # 平台提供的 URL
  api_key=os.getenv("OPENAI_API_KEY"), # 平台提供的 API-Key
)

print("\n正在调用 API...")
try:
    completion = client.chat.completions.create(
      model="gpt-4o-mini", # 模型名称
      messages=[{"role": "user", "content": "将'你好'翻译成意大利语"}], # 用户输入
    )
    
    print(f"completion 类型: {type(completion)}")
    print(f"completion 内容: {completion}")
    
    # 尝试访问属性
    if hasattr(completion, 'choices'):
        print(f"choices 属性存在: {completion.choices}")
        if len(completion.choices) > 0:
            print(f"第一个 choice 的内容: {completion.choices[0].message.content}")
    else:
        print("completion 没有 choices 属性")
        # 尝试将其作为字符串处理
        if isinstance(completion, str):
            print(f"completion 是字符串，内容为: {completion}")
            # 尝试解析为 JSON
            try:
                parsed = json.loads(completion)
                print(f"可以解析为 JSON: {parsed}")
            except json.JSONDecodeError:
                print("无法解析为 JSON")
                
except Exception as e:
    print(f"发生异常: {type(e).__name__}: {e}")
    import traceback
    traceback.print_exc()