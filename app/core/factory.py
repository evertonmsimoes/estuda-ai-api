from .models import GptConection

class Factory:
    def __init__(self) -> None:
        self.__gptModel = None

    def getGpt4O(self):
        if self.__gptModel is None:
            self.__gptModel = GptConection()
        model = self.__gptModel.getModel(model_name="gpt-4o")
        return model

