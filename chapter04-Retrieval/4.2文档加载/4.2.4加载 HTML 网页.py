# pip install langchain_community beautifulsoup4
import bs4
from langchain_community.document_loaders import WebBaseLoader

docs = WebBaseLoader(
  # 网址序列
  web_paths=("https://baike.baidu.com/item/%E5%BE%AE%E6%B3%A2%E7%82%89/84186",),
  # 传给 BeautifulSoup 的解析参数，parse_only 表示只提取指定标签的元素
  bs_kwargs={"parse_only": bs4.SoupStrainer(class_="J-summary")},
).load()

print(docs)