from langchain_core.prompts import load_prompt

template = load_prompt("chapter02-model IO/2.4 Prompt Template/prompts/prompt.yaml", encoding="utf-8")
print(template.format(name="年轻人", what="滑稽"))
# 请年轻人讲一个滑稽的故事