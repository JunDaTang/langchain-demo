# pip install langchain_community
from langchain_community.document_loaders.csv_loader import CSVLoader

# 加载所有列
docs = CSVLoader(
  file_path="sgg/chapter04-Retrieval/assets/sample.csv", # 文件路径
).load() # 返回List[Document]

print(docs)

# 加载部分列
docs = CSVLoader(
  file_path="sgg/chapter04-Retrieval/assets/sample.csv", # 文件路径
  metadata_columns=["title", "author"], # 将指定列作为元数据
  content_columns=["content"], # 将指定列作为内容
).load()  # 返回List[Document]

print(docs)

# [Document(metadata={'source': 'sgg/chapter04-Retrieval/assets/sample.csv', 'row': 0}, page_content="title: The Great Gatsby\ndate: 2025-01-01\nauthor: F. Scott Fitzgerald\ncontent: In my younger and more vulnerable years my father gave me some advice that 
# I've been turning over in my mind ever since."), Document(metadata={'source': 'sgg/chapter04-Retrieval/assets/sample.csv', 'row': 1}, page_content='title: To Kill a Mockingbird\ndate: 2025-01-02\nauthor: Harper Lee\ncontent: When he was nearly thirteen')] 
# [Document(metadata={'source': 'sgg/chapter04-Retrieval/assets/sample.csv', 'row': 0, 'title': 'The Great Gatsby', 'author': 'F. 
# Scott Fitzgerald'}, page_content="content: In my younger and more vulnerable years my father gave me some advice that I've been 
# turning over in my mind ever since."), Document(metadata={'source': 'sgg/chapter04-Retrieval/assets/sample.csv', 'row': 1, 'title': 'To Kill a Mockingbird', 'author': 'Harper Lee'}, page_content='content: When he was nearly thirteen')]