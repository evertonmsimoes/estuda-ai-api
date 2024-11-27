from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from app.core.factory import Factory

class QuestionsServices:

    def __init__(self) -> None:
        self.factory = Factory()

    def generateQuestions(self, discipline: str, content: str):

        llm = self.factory.getGpt4O()

        prompt_teste = PromptTemplate(
            input_variables = ['content', 'discipline'],
            template = '''Você é um professor de {discipline} expecialista em querar questões do enem. 
            Com base nessas instruções gerar questões que devem abranger os seguintes tópicos:

            {content}

            O Título deve ser "Lista de exercícios de ${subject} - ${educationLevel}".
            A lista deve ser numerada.

'''
        )

        question = LLMChain(llm=llm, prompt=prompt_teste)
        return question.run({'content': content, 'discipline': discipline})
    