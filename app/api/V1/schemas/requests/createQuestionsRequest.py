from pydantic import BaseModel


class CreateQuestionsRequest(BaseModel):
    discipline: str
    content: str
    education: str
