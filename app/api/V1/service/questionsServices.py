from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from app.core.factory import Factory
import json

class QuestionsServices:

    def __init__(self) -> None:
        self.factory = Factory()

    def generateQuestions(self, discipline: str, content: str):
        llm = self.factory.getGpt4O()

        # Prompt aprimorado
        prompt_teste = PromptTemplate(
            input_variables=['content', 'discipline'],
            template=(
                "Você é um professor de {discipline}, especialista em elaborar questões do ENEM. "
                "O ENEM é conhecido por avaliar competências como interpretação, análise crítica e resolução de problemas aplicados ao cotidiano. "
                "Crie uma lista numerada de questões de múltipla escolha sobre o tema: {content}. "
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

        # Configuração da chain
        question = LLMChain(llm=llm, prompt=prompt_teste)

        # Executa o modelo com as variáveis
        response = question.run({'content': content, 'discipline': discipline})

        # Processa a string para JSON
        try:
            # Remove caracteres extras e converte para JSON
            cleaned_response = response.strip("```json").strip()
            json_response = json.loads(cleaned_response)
            return json_response
        except json.JSONDecodeError as e:
            # Retorna erro caso a string não seja um JSON válido
            raise ValueError(f"Erro ao decodificar JSON: {e}") from e
