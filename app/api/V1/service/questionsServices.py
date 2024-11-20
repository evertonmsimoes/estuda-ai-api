from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from app.core.factory import Factory

class QuestionsServices:

    def __init__(self) -> None:
        self.factory = Factory()

    def generateQuestions(self, text: str):

        llm = self.factory.getGpt4O()

        prompt_teste = PromptTemplate(
            input_variables = ['text'],
            template = '''Você é um professor expecialista em querar questões do enem. Com base nessas instruções gerar uma questão:
            {text}
'''
        )

        question = LLMChain(llm=llm, prompt=prompt_teste)
        return question.run(text)