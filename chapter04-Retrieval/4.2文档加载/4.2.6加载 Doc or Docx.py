# pip install langchain_community unstructured[docx]
from langchain_community.document_loaders import UnstructuredWordDocumentLoader

docs = UnstructuredWordDocumentLoader(
  # 文件路径
  file_path="assets/sample.docx",
  # 加载模式:
  #  single 返回单个Document对象
  #  elements 按标题等元素切分文档
  mode="single",
).load()

print(docs)