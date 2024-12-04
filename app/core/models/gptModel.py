from langchain_community.chat_models import ChatOpenAI
from app.config import gptKey

class GptConection:
    def __init__(self) -> None:
        self.__api_key = gptKey

    def getModel(self, model_name: str) -> ChatOpenAI:
        model = ChatOpenAI(api_key=self.__api_key, model_name=model_name, temperature=0.6)
        return model
