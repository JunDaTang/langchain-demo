import os
from pymilvus import MilvusClient
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import UnstructuredWordDocumentLoader

# 实例化向量数据库客户端
client = MilvusClient(
  uri="./milvus_demo.db", # 数据存储在本地当前目录下
)

# 加载文档
docs = UnstructuredWordDocumentLoader(
  file_path="assets/sample.docx",
  mode="single",
).load()

# 文档切分
chunks = RecursiveCharacterTextSplitter(
  separators=["\n\n", "\n", "。", "！", "？", "……", "，", ""],
  chunk_size=400,
  chunk_overlap=50,
).split_documents(docs)

# 加载嵌入模型
embed_model = HuggingFaceEmbeddings(
  model_name=os.path.expanduser("~/models/bge-base-zh-v1.5")
)

# 计算嵌入向量
embeddings = embed_model.embed_documents([chunk.page_content for chunk in chunks])

# 转换数据格式
data = [
  {
    "vector": embedding,
    "text": chunk.page_content,
    "metadata": chunk.metadata,
  }
  for chunk, embedding in zip(chunks, embeddings)
]

# 插入实体
res = client.insert(collection_name="demo_collection", data=data)
print(res)