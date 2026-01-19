# pip install unstructured[local-inference]
from langchain_community.document_loaders import UnstructuredPDFLoader

# 特别注意：要先下载Poppler 和 Tesseract OCR。
# Poppler：https://github.com/oschwartz10612/poppler-windows/releases
# 下载解压后将 .../poppler-24.08.0/Library/bin 添加到环境变量 Path 中即可


# Tesseract OCR：https://github.com/UB-Mannheim/tesseract/wiki
# Tesseract OCR 用于提取图片中的文字 ， 在安装时需要选择 Additional language data(download) 来添加中文语言包。安装后，将安装时设置的安装目录添加到环境变量 Path 中。
docs = UnstructuredPDFLoader(
  file_path="sgg/chapter04-Retrieval/assets/sample.pdf", # 文件路径
  # 加载模式:
  #  single: 返回单个Document对象
  #  elements: 按标题等元素切分文档
  mode="elements",
  # 加载策略:
  #  fast: pdfminer 提取并处理文本
  #  ocr_only: 转换为图片并进行 OCR
  #  hi_res: 识别文档布局，将OCR 输出与 pdfminer 输出融合
  strategy="hi_res",
  # 推断表格结构:仅 hi_res 下起效，如果为 True 则会在表格元素的元数据中添加 text_as_html
  infer_table_structure=True,
  # OCR 使用的语言: eng 英文，chi_sim 中文简体。语言列表参考 https://github.com/tesseract-ocr/langdata
  languages=["eng", "chi_sim"],
  # 更多参数详见 https://github.com/Unstructured-IO/unstructured/blob/main/unstructured/partition/pdf.py
).load()

print(docs)