# pip install langchain_community jq
from langchain_community.document_loaders import JSONLoader

# 常见 jq schema 参考：
# JSON    -> [{"text": ...}, {"text": ...}, {"text": ...}]
# jq_schema  -> ".[].text"

# JSON    -> {"key": [{"text": ...}, {"text": ...}, {"text": ...}]}
# jq_schema  -> ".key[].text"

# JSON    -> ["...", "...", "..."]
# jq_schema  -> ".[]"

# 提取指定字段中的内容
docs = JSONLoader(
  file_path="assets/sample.json", # 文件路径
  jq_schema=".data.items[]", # 提取data.items中的数据
  text_content=False, # 提取内容是否为字符串格式
).load()

print(docs)

docs = JSONLoader(
  file_path="assets/sample.json", # 文件路径
  jq_schema=".data.items[].content", # 提取data.items[].content中的数据
).load()

print(docs)

docs = JSONLoader(
  file_path="assets/sample.json", # 文件路径
  jq_schema="""
    .data.items[] | {
      author,
      created_at,
      content: (.title + "\n" + .content)
    }
  """, # 提取data.items中指定字段的数据
  text_content=False, # 提取内容是否为字符串格式
).load()

print(docs)
