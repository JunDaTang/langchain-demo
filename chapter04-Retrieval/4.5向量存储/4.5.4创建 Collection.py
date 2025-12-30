# pip install pymilvus[milvus_lite]
from pprint import pprint
from pymilvus import MilvusClient, DataType

# 实例化向量数据库客户端
client = MilvusClient(
  uri="./milvus_demo.db", # 数据存储在本地当前目录下
)

# 创建 schema
def build_schema():
  return (
    MilvusClient.create_schema(
      # 自动分配主键
      auto_id=True,
      # 启用动态字段，未在 Schema 中声明的字段会以键值对的形式存储在这个动态字段
      enable_dynamic_field=True,
    )
    # 添加 id 字段，类型为整数，设置为主键
    .add_field(field_name="id", datatype=DataType.INT64, is_primary=True)
    # 添加 vector 字段，类型为浮点数向量，维度为 768
    .add_field(field_name="vector", datatype=DataType.FLOAT_VECTOR, dim=768)
    # 添加 text 字段，类型为字符串，最大长度为 1024
    .add_field(field_name="text", datatype=DataType.VARCHAR, max_length=1024)
    # 添加 metadata 字段，类型为 JSON
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
  # 删除 collection
  # 在 Milvus 中删除数据后，存储空间不会立即释放。虽然删除数据会将实体标记为 "逻辑删除"，但实际空间可能不会立即释放。
  # Milvus 会在后台自动压缩数据。这个过程会将较小的数据段合并为较大的数据段，并删除"逻辑删除"的数据或已超过有效时间的数据。
  # 一个名为 Garbage Collection (GC) 的独立进程会定期删除这些 "已删除 "的数据段，从而释放它们占用的存储空间。
  client.drop_collection(collection_name="demo_collection")
client.create_collection(
  collection_name="demo_collection", # collection 名称
  schema=build_schema(), # collection 的 schema
  index_params=build_index(), # collection 的 index
)

# 查看 collection
print(client.list_collections())

# 查看 collection 描述
pprint(client.describe_collection(collection_name="demo_collection"))