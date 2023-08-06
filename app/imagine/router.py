from fastapi import APIRouter
from typing import Union
from fastapi.responses import Response

from app.model import ImagineRequest, ImageResponse
from app.imagine.main import imagine

router = APIRouter()


@router.post("/generate")
async def generate(request: ImagineRequest) -> Union[ImageResponse, dict]:
    try:
        prompt = request.prompt
        # style = request.style
        upscale = request.upscale
        data = await imagine(prompt, upscale)

        return Response(
            content=data, media_type="image/png", headers={"prompt": prompt}
        )
    except Exception as e:
        return {"message": "error", "prompt": prompt, "content": None, "error": str(e)}


@router.get("/styles")
async def styles() -> dict:
    return {"message": "success", "styles": await all_styles()}
