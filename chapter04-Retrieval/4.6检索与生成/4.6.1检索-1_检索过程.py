import os
from pymilvus import MilvusClient, DataType
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import UnstructuredWordDocumentLoader

# 实例化向量数据库客户端
client = MilvusClient(
  uri="./milvus_demo.db", # 数据存储在本地当前目录下
)

# ========== 构建索引 ==========
# 创建 schema
def build_schema():
  return (
    MilvusClient.create_schema(auto_id=True, enable_dynamic_field=True)
    .add_field(field_name="id", datatype=DataType.INT64, is_primary=True)
    .add_field(field_name="vector", datatype=DataType.FLOAT_VECTOR, dim=768)
    .add_field(field_name="text", datatype=DataType.VARCHAR, max_length=1024)
    .add_field(field_name="metadata", datatype=DataType.JSON)
  )

# 创建 index
def build_index():
  index_params = MilvusClient.prepare_index_params()
  index_params.add_index(
    field_name="vector", # 建立索引的字段
    index_type="AUTOINDEX", # 索引类型
    metric_type="L2", # 向量相似度度量方式
  )
  return index_params

# 创建 collection
if client.has_collection(collection_name="demo_collection"):
  client.drop_collection(collection_name="demo_collection")
client.create_collection(
  collection_name="demo_collection", # collection 名称
  schema=build_schema(), # collection 的 schema
  index_params=build_index(), # collection 的 index
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

# ========== 检索 ==========
def retrieval(query, embed_model, client):
  """检索并返回上下文"""
  query_embedding = embed_model.embed_query(query) # 查询嵌入
  context = client.search(
    collection_name="demo_collection", # collection 名称
    data=[query_embedding], # 搜索的向量
    anns_field="vector", # 进行向量搜索的字段
    # 度量方式：L2 欧氏距离/IP 内积/COSINE 余弦相似度
    search_params={"metric_type": "L2"},
    output_fields=["text", "metadata"], # 输出字段
    limit=3, # 搜索结果数量
  )
  return context

context = retrieval("不动产被占有了怎么办?", embed_model, client)
print(context)