from pymilvus import MilvusClient

# 实例化向量数据库客户端
client = MilvusClient(
  uri="./milvus_demo.db", # 数据存储在本地当前目录下
)

# 通过主键查询实体
res = client.get(
  collection_name="demo_collection",
  ids=[461484610130804912, 461484610130804913],
  output_fields=["text", "metadata"],
)
print(res)

# 通过过滤条件(https://milvus.io/docs/zh/boolean.md)查询实体
res = client.query(
  collection_name="demo_collection",
  filter='metadata["source"] == "assets/sample.docx"', # 使用 metadata["source"] 进行过滤
  output_fields=["text", "metadata"],
  limit=1,
)
print(res)