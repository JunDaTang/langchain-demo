from langchain_core.prompts import load_prompt

template = load_prompt("chapter02-model IO/2.4 Prompt Template/prompts/prompt.json", encoding="utf-8")
print(template.format(name="张三", what="搞笑的"))
# 请张三讲一个搞笑的的故事