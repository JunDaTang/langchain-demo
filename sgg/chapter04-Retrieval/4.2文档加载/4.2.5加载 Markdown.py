# pip install langchain_community unstructured[md]
from langchain_community.document_loaders import UnstructuredMarkdownLoader

docs = UnstructuredMarkdownLoader(
  # 文件路径
  file_path="sgg/chapter04-Retrieval/assets/sample.md",
  # 加载模式:
  #  single 返回单个Document对象
  #  elements 按标题等元素切分文档
  mode="elements",
).load()

print(docs)