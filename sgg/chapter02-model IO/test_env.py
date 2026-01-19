import dotenv
import os
dotenv.load_dotenv()

# 调试：检查环境变量是否正确加载
print(f"API Key: {os.getenv('OPENAI_API_KEY1')[:10] if os.getenv('OPENAI_API_KEY1') else 'Not set'}...")
print(f"Base URL: {os.getenv('OPENAI_BASE_URL')}")
print(f"Model Name: {os.getenv('OPENAI_MODEL_NAME')}")
