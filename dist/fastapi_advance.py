import json
from typing import Optional
from fastapi import Depends, FastAPI, Header, Path, HTTPException, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel,Field
import uvicorn
""" 
note:
狀態異常: status_code [201 :創建成功]
依賴注入: Depend(), dependencies [避免重複宣告, 統一驗證]
身分驗證: 
"""

userDict ={
    # 'a':{"id":1},
    'b':{"id":2, "username":"123"},
    'c':{"id":3, "username":"345","desc":"hihihi"}
}

async def verify_auth(api_token:Optional[str]=Header(None, alias="api-token")):
    if not api_token:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Unauthorized")

app = FastAPI(dependencies=[Depends(verify_auth)])

class UserBase(BaseModel):
    id:Optional[int]=None
    username: str
    desc:Optional[str]=None

class UserIn(UserBase):
    password:str

class UserOut(UserBase):
    ...

class ErrorMessage(BaseModel):
    error_code:int
    message:str

def total_params(total:Optional[int]=1):
    return total

class PageInfo:
    def __init__(self, page_index:Optional[str]=1, page_size:Optional[str]=10, total:int=Depends(total_params)) -> None:
        self.page_index = page_index
        self.page_size = page_size
        self.total = total
        
@app.post("/users", status_code=201, response_model=UserOut, responses={
    400:{"model":ErrorMessage}
})
async def create_user(user:UserIn):
    if userDict.get(user.username,None):
        error_message = ErrorMessage(error_code=status.HTTP_400_BAD_REQUEST, message=f"{user.username} exist")
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=json.loads(error_message.json()))
    
    user_dict = json.loads(user.json())
    user_dict.update({"id":10})
    return user_dict

@app.get("/users", status_code=200, dependencies=[Depends(verify_auth)])
async def get_users(page_info:PageInfo=Depends()):
    return {"page_index":page_info.page_index, "page_size":page_info.page_size, "total":page_info.total}

@app.get("/users/{username}", status_code=200, response_model=UserOut)
async def get_user(username:str=Path(..., min_length=1)):
    user = userDict.get(username,None)
    if user:
        return user
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{username} not font" )

if __name__ == "__main__":
    uvicorn.run(app="fastapi_advance:app", host="0.0.0.0", port=28000, reload=True)