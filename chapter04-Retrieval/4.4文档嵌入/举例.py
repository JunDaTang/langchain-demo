# pip install sentence-transformers langchain_huggingface
import os
from langchain_huggingface import HuggingFaceEmbeddings

# 加载嵌入模型
# 注意：如果模型文件不存在本地，将从HuggingFace Hub自动下载
embed_model = HuggingFaceEmbeddings(
    # model_name=os.path.expanduser("~/models/bge-base-zh-v1.5")
  model_name="BAAI/bge-base-zh-v1.5"  # 使用在线模型ID，HuggingFace会自动下载
)

# 单文本嵌入
query = "你好，世界"
print(embed_model.embed_query(query))

# 多文本嵌入
docs = ["你好，世界", "你好，世界"]
print(embed_model.embed_documents(docs))