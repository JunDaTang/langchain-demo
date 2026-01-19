# pip install langchain_community
from langchain_community.document_loaders import TextLoader

docs = TextLoader(
  file_path="sgg/chapter04-Retrieval/assets/sample.txt", # 文件路径
  encoding="utf-8", # 文件编码方式
).load() # 返回List[Document]

print(docs)
# [Document(metadata={'source': 'sgg/chapter04-Retrieval/assets/sample.txt'}, page_content='Hello,jed')]