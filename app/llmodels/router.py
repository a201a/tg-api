from fastapi import APIRouter
from typing import Union
from fastapi.responses import Response

from app.model import simpleRequest, simpleResponse
from app.llmodels.bard import ask_bard

router = APIRouter()


@router.post("/bard")
async def bard(request: simpleRequest) -> simpleResponse:
    try:
        query = request.query
        data = await ask_bard(query)

        return simpleResponse(
            message="success",
            query=query,
            content=data,
            error=""
        )
    except Exception as e:
        return simpleResponse(
            message="error",
            query=query,
            content="",
            error=str(e)
        )
