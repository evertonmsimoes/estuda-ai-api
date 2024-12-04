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
                "Segue as questões feitas pelo aluno e suas respostas: {answers}"
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

            return response
        
    
    def generate_summary(self, content: str, discipline: str, education: str):
        llm = Factory().getGpt4O()

        prompt_teste = PromptTemplate(
            input_variables=['content', 'discipline', 'education'],
            template=(
                "Você é um professor especializado na área de {discipline}, responsável por criar conteúdos que auxiliem os alunos em seus estudos do seguinte nível: {education}. "
                "Com base no tema fornecido: {content}, elabore um conteúdo abrangente que cubra os seguintes pontos:\n\n"
                "- **Definição completa**: Apresente uma explicação clara e detalhada e completa sobre o tema, incluindo suas variações e conceitos relacionados. OBS: O Conteudo deve conter no minimo de 40 linhas.\n"
                "- **Exemplos práticos**: Forneça exemplos práticos do tema, aplicados em situações reais ou cotidianas.\n"
                "- **Aplicações**: Explique como o tema é utilizado em diferentes contextos ou áreas do conhecimento.\n"
                "- **Teoria e prática**: Discuta a teoria por trás do tema e como ela pode ser aplicada na prática, com foco em como os alunos podem utilizar esse conhecimento.\n"
                "- **Exercícios sugeridos**: Sugira exercícios para os alunos, com diferentes níveis de dificuldade, para ajudar a fixar o conteúdo.\n"
                "- **Dicas de estudo**: Ofereça dicas práticas para estudar esse conteúdo, como métodos de revisão, ferramentas online e áreas de foco.\n"
                "- **Fontes adicionais**: Forneça referências para livros, artigos ou vídeos que podem aprofundar o aprendizado do tema.\n\n"
                "O retorno deve ser estruturado em formato JSON com os seguintes campos:\n\n"
                "{{\n"
                "  \"titulo\": \"Conteúdo completo sobre {content}\",\n"
                "  \"definicao\": \"Definição completa do tema {content}, incluindo variações e conceitos relacionados.\",\n"
                "  \"exemplos\": [\n"
                "    \"Exemplo 1: Descrição detalhada do exemplo 1.\",\n"
                "    \"Exemplo 2: Descrição detalhada do exemplo 2.\"\n"
                "  ],\n"
                "  \"aplicacoes\": \"Explicação sobre como o tema {content} pode ser utilizado em diferentes contextos ou áreas.\",\n"
                "  \"teoria_e_pratica\": \"Discussão sobre a teoria por trás do tema e como ela é aplicada na prática.\",\n"
                "  \"exercicios\": [\n"
                "    \"Exercício 1: Descrição do exercício 1.\",\n"
                "    \"Exercício 2: Descrição do exercício 2.\"\n"
                "  ],\n"
                "  \"dicas_estudo\": [\n"
                "    \"Dica 1: Descrição da dica 1.\",\n"
                "    \"Dica 2: Descrição da dica 2.\"\n"
                "  ],\n"
                "  \"referencias\": [\n"
                "    \"Referência 1: Descrição da referência 1.\",\n"
                "    \"Referência 2: Descrição da referência 2.\"\n"
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