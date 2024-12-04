from fastapi import APIRouter, HTTPException
from app.api.V1.service import QuestionsServices
from ..schemas.requests import CreateQuestionsRequest
from ..schemas.requests import CorrectionRequest


router = APIRouter()

service = QuestionsServices()


@router.post("/create_questions")
def teste(request: CreateQuestionsRequest):
    try:
        response = service.generateQuestions(content=request.content, 
                                     discipline=request.discipline)

        return response
    except Exception as E:
        raise HTTPException(
            status_code=500,
            detail=f'The following error occurred when generating the questions: {E}'
        )


@router.post("/generate_summary")
def teste(request: CreateQuestionsRequest):
    try:
        response = service.generateQuestions(content=request.content, 
                                     discipline=request.discipline)

        return response
    except Exception as E:
        raise HTTPException(
            status_code=500,
            detail=f'The following error occurred when generating the questions: {E}'
        )
    

@router.post("/correction")
def teste(request: CorrectionRequest):
    try:
        response = service.generate_results(
            content=request.content,
            discipline=request.discipline,
            answers=request.answers
        )

        return response
    except Exception as E:
        raise HTTPException(
            status_code=500,
            detail=f'The following error occurred when generating the questions: {E}'
        )