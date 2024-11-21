from fastapi import APIRouter
from app.api.V1.service import QuestionsServices

router = APIRouter()

service = QuestionsServices()


@router.post("/teste")
async def teste(text: str):
    return service.generateQuestions(text=text)