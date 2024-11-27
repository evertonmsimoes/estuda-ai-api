from pydantic import BaseModel
from typing import List


class CreateQuestionsRequest(BaseModel):
    disciplines: List[str]
    content: str
