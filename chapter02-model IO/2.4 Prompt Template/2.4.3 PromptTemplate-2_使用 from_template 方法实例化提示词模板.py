from langchain_core.prompts import PromptTemplate

# 使用 from_template 方法实例化提示词模板
template = PromptTemplate.from_template("请给我一个关于{topic}的{type}解释。")

# 使用模板生成提示
prompt = template.format(type="详细", topic="量子力学")

print(prompt) # 请给我一个关于量子力学的详细解释。