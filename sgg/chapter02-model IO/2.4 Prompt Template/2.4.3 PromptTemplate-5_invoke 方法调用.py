from langchain_core.prompts import PromptTemplate

template = PromptTemplate.from_template("{foo} {bar}")

prompt = template.invoke({"foo": "hello", "bar": "world"})

print(prompt, type(prompt))
# text='hello world' <class 'langchain_core.prompt_values.StringPromptValue'>

prompt_str = prompt.to_string()
print(prompt_str, type(prompt_str))
# hello world <class 'str'>