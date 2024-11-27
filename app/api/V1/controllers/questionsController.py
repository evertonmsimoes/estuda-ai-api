from fastapi import APIRouter
from app.api.V1.service import QuestionsServices
from ..schemas.requests import CreateQuestionsRequest

router = APIRouter()

service = QuestionsServices()


@router.post("/create_questions")
async def teste(request: CreateQuestionsRequest):
    return service.generateQuestions(text=request.content)

