# pip install langchain_community jq
from langchain_community.document_loaders import JSONLoader

# 提取所有字段
docs = JSONLoader(
  file_path="sgg/chapter04-Retrieval/assets/sample.json", # 文件路径
  jq_schema=".", # 提取所有字段
  text_content=False, # 提取内容是否为字符串格式
).load()

print(docs)