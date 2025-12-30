# pip install sentence-transformers langchain_huggingface
import os
from langchain_huggingface import HuggingFaceEmbeddings

# 加载嵌入模型
embed_model = HuggingFaceEmbeddings(
  model_name=os.path.expanduser("~/models/bge-base-zh-v1.5")
)

# 单文本嵌入
query = "你好，世界"
print(embed_model.embed_query(query))

# 多文本嵌入
docs = ["你好，世界", "你好，世界"]
print(embed_model.embed_documents(docs))