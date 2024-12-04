from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from app.core.factory import Factory
import json

class QuestionsServices:

    def __init__(self) -> None:
        self.factory = Factory()

    def generateQuestions(self, discipline: str, content: str, education: str):
        llm = self.factory.getGpt4O()

        prompt_teste = PromptTemplate(
            input_variables=['content', 'discipline'],
            template=(
                "Você é um professor de {discipline}, especialista em elaborar questões do ENEM. "
                "O ENEM é conhecido por avaliar competências como interpretação, análise crítica e resolução de problemas aplicados ao cotidiano. "
                "Crie uma lista numerada de questões de múltipla escolha sobre o tema: {content}. "
                "Crie questões projetadas especificamente para atender às necessidades de estudantes de {education}."
                "Certifique-se de que:\n"
                "- O enunciado seja contextualizado e relacionado a situações do mundo real.\n"
                "- As alternativas apresentem escolhas plausíveis e uma correta.\n"
                "- Cada questão envolva uma análise mais profunda do tema.\n"
                "- Forneça o gabarito com a resposta correta para cada questão.\n"
                "O retorno deve estar no formato JSON com os seguintes campos:\n\n"
                "{{\n"
                "  \"titulo\": \"Lista de exercícios de {content}\",\n"
                "  \"questoes\": [\n"
                "    {{\n"
                "      \"numero\": 1,\n"
                "      \"enunciado\": \"Texto do enunciado da questão 1.\",\n"
                "      \"alternativas\": {{\n"
                "        \"A\": \"Texto da alternativa A\",\n"
                "        \"B\": \"Texto da alternativa B\",\n"
                "        \"C\": \"Texto da alternativa C\",\n"
                "        \"D\": \"Texto da alternativa D\"\n"
                "      }},\n"
                "      \"resposta_correta\": \"A\"\n"
                "    }},\n"
                "    ...\n"
                "  ]\n"
                "}}"
            )
        )

        question = LLMChain(llm=llm, prompt=prompt_teste)

        response = question.run({'content': content, 'discipline': discipline, 'education': education})

        try:
            cleaned_response = response.strip("```json").strip()
            json_response = json.loads(cleaned_response)
            return json_response
        except json.JSONDecodeError as e:
            raise ValueError(f"Erro ao decodificar JSON: {e}") from e
        

    def generate_results(self, content: str, discipline: str, answers: list):
        llm = Factory().getGpt4O()

        prompt_teste = PromptTemplate(
            input_variables=['content', 'discipline', 'answers'],
            template=(
                "Você é um professor de {discipline}, especialista em avaliar respostas de questões do ENEM. "
                "O ENEM avalia competências como interpretação, análise crítica e resolução de problemas aplicados ao cotidiano. "
                "Avalie as respostas fornecidas para as questões sobre o tema: {content}. "
                "Cada questão possui alternativas e uma resposta correta. O retorno deve fornecer a pontuação total e feedback para cada questão, indicando se a resposta está correta ou não.\n"
                "O retorno deve estar no formato JSON com os seguintes campos:\n\n"
                "{{\n"
                "  \"titulo\": \"Resultado da avaliação de {content}\",\n"
                "  \"pontuacao_total\": 10,\n"
                "  \"feedback\": [\n"
                "    {{\n"
                "      \"numero\": 1,\n"
                "      \"resposta_aluno\": \"A\",\n"
                "      \"feedback\": \"Resposta correta!\",\n"
                "      \"pontuacao\": 1\n"
                "    }},\n"
                "    ...\n"
                "  ]\n"
                "}}"
            )
        )

        result = LLMChain(llm=llm, prompt=prompt_teste)

        response = result.run({
            'content': content,
            'discipline': discipline,
            'answers': answers  
        })

        try:
            cleaned_response = response.strip("```json").strip()
            json_response = json.loads(cleaned_response)
            return json_response
        except json.JSONDecodeError as e:

            raise ValueError(f"Erro ao decodificar JSON: {e}") from e
        
    
    def generate_summary(self, content: str, discipline: str, education: str):
        llm = Factory().getGpt4O()

        prompt_teste = PromptTemplate(
            input_variables=['content', 'discipline', 'education'],
            template=(
                "Você é um professor especializado na área de {discipline}, responsável por criar conteúdos que auxiliem os alunos em seus estudos do seguinte nivel {education}. "
                "Com base no tema fornecido: {content}, elabore um resumo claro, objetivo e informativo que aborde os pontos principais do assunto. "
                "O retorno deve ser estruturado em formato JSON com os seguintes campos:\n\n"
                "{{\n"
                "  \"titulo\": \"Resumo sobre {content}\",\n"
                "  \"conteudo\": \"Resumo gerado por você com base no tema {content}\",\n"
                "  \"dicas\": [\n"
                "    \"Dica 1 relacionada ao conteúdo.\",\n"
                "    \"Dica 2 relacionada ao conteúdo.\",\n"
                "    \"Dica 3 relacionada ao conteúdo.\"\n"
                "  ],\n"
                "  \"referencias\": [\n"
                "    \"Referência ou fonte 1 usada para gerar o resumo.\",\n"
                "    \"Referência ou fonte 2 usada para gerar o resumo.\"\n"
                "  ]\n"
                "}}"
            )
        )

        result = LLMChain(llm=llm, prompt=prompt_teste)

        response = result.run({
            'content': content,
            'discipline': discipline,
            'education': education  
        })

        try:
            cleaned_response = response.strip("```json").strip()
            json_response = json.loads(cleaned_response)
            return json_response
        except json.JSONDecodeError as e:

            raise ValueError(f"Erro ao decodificar JSON: {e}") from e