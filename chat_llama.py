from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatOllama(model="llama3.2")

prompt_text = "Tell me a joke about {topic}"
prompt = ChatPromptTemplate.from_template(prompt_text)
chain = prompt | llm

res = chain.invoke({"topic":"cricket"})
print(res)