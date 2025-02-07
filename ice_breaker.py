import os
from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain 

information = """
Arvind Krishna (born November 23, 1962)[3] is an Indian-American business executive, and the chairman and CEO of IBM. 
He has been CEO of IBM since April 2020 and chairman since January 2021.[4][5] 
Krishna began his career at IBM in 1990, at its Thomas J. Watson Research Center,[6] and was promoted to senior vice president in 2015, managing IBM Cloud & Cognitive Software and IBM Research divisions. He was a principal architect of the acquisition of Red Hat, the largest acquisition in the company’s history.[7][8]]
"""

load_dotenv()
if __name__ == "__main__":
    print("Hello LangChain!")
    load_dotenv()
    print(os.environ.get('OPENAI_API_KEY'))
    print(os.getenv('OPENAI_API_KEY'))
    print(os.environ['OPENAI_API_KEY'])
    # This is in github - check there in the github page

    summary_template = """given the information {information} about a person from I want you to create:
    1. a short summary
    2. two interesting facts about them"""

    summary_prompt_template = PromptTemplate(input_variables=["information"],template=summary_template)

    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
    chain = summary_prompt_template | llm
    res = chain.invoke(input={"information":information})

    print(res)