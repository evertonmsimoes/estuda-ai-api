from fastapi import APIRouter, HTTPException
from app.api.V1.service import QuestionsServices
from ..schemas.requests import CreateQuestionsRequest

router = APIRouter()

service = QuestionsServices()


@router.post("/create_questions")
def teste(request: CreateQuestionsRequest):
    try:
        response = service.generateQuestions(content=request.content, 
                                     decipline=request.discipline)

        return response
    except Exception as E:
        return HTTPException(
            status_code=500,
            details=f'The following error occurred when generating the questions: {E}'
        )
