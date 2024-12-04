from pydantic import BaseModel

class CorrectionRequest(BaseModel):
    discipline: str
    content: str
    answers: list
