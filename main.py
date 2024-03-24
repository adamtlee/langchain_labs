from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv() 
def generate_pet_name():
    llm = OpenAI(temperature=0.7)
    

    name = llm("I have a pet dog and I want to name my pet dog. Suggest five names for my pet dog")

    return name 

if __name__ == "__main__":
    print(generate_pet_name())