from pymilvus import MilvusClient

# 实例化向量数据库客户端
client = MilvusClient(
  uri="./milvus_demo.db", # 数据存储在本地当前目录下
)

# 通过主键删除实体
res = client.delete(
  collection_name="demo_collection",
  ids=[461484610130804912, 461484610130804913],
)
print(res)

# 通过过滤条件(https://milvus.io/docs/zh/boolean.md)删除实体
res = client.delete(
  collection_name="demo_collection",
  filter='text LIKE "第%"', # 使用 text 前缀过滤
)
print(res)