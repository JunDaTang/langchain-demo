import os
from pymilvus import MilvusClient
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableLambda

# 实例化向量数据库客户端
client = MilvusClient(
  uri="./milvus_demo.db", # 数据存储在本地当前目录下
)

# 加载嵌入模型
embed_model = HuggingFaceEmbeddings(
  model_name=os.path.expanduser("~/models/bge-base-zh-v1.5")
)

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

# ========== 生成 ==========
llm = init_chat_model(
  model="openai/gpt-oss-20b:free",
  model_provider="openai",
  base_url="https://openrouter.ai/api/v1",
  api_key=os.getenv("OPENROUTER_API_KEY"),
)

template = ChatPromptTemplate.from_messages(
  [
    (
      "system",
      "# 任务\n\n根据上下文参考，回答用户的问题。\n\n# 上下文参考\n\n{context}",
    ),
    ("human", "{query}"),
  ]
)

rag_chain = (
  {
    "query": RunnablePassthrough(),
    "context": lambda x: retrieval(query=x, embed_model=embed_model, client=client),
  }
  | RunnableLambda(lambda x: print(x) or x) # 打印中间结果
  | template
  | llm
  | StrOutputParser()
)
res_chunks = rag_chain.stream(input="不动产被占有了怎么办?")
for chunk in res_chunks:
  print(chunk, end="", flush=True)