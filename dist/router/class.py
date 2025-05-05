from typing import Optional,List
from datetime import datetime
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi import status,APIRouter
import json

from db.mysql.cvd_daily_move import get_cvd_daily_move
from db.FILES import get_daily_move_textarea

router = APIRouter(prefix='/cvdcapa', tags=['CVD CAPA DAILY MOVE'])

class ErrorMessage(BaseModel):
    error_code:int
    message:str

class TextareaFormatOut(BaseModel):
    FILENAME: str
    CONTENT:str

class TextareaFormatIn(BaseModel):
    FILENAME :str
    CONTENT :str

@router.put("/daily_move_textarea", status_code=200,  response_model=List[TextareaFormatOut], responses={400:{"model":ErrorMessage}})
async def daily_move_textarea(fileinfo:TextareaFormatIn):

    try:
        res = update_daily_move_textarea("CVD",fileinfo.FILENAME, fileinfo.CONTENT)

    except Exception as e:
        error_message = ErrorMessage(error_code=status.HTTP_400_BAD_REQUEST, message=str(e))
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=json.loads(error_message.json()))
    
    return res