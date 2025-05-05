from enum import Enum
import json
from typing import List, Optional, Union
from pydantic import BaseModel,Field
from fastapi import Header,Cookie, FastAPI, Path, Query,Body,Response
import uvicorn

"""
note:
路徑參數驗證:Path
查詢參數驗證:Query
設定為請求體裡的數據:Body
請求體裡驗證:Field
範例數據可於Field,Body的特性值example定義,或採model_config
HEADER, COOKIE 可用alias將'_'轉為'-'
"""


app = FastAPI()

class Gender(str, Enum):
    male = "male"
    female = "female"

class UserModel(BaseModel):
    name: str
    age: Optional[int] = None
    gender : Gender

@app.get("/user/current")
async def get_currentuser():
    return {"get_currentuser"}

@app.get("/users")
async def get_users(page_index:Optional[int]=Query(30,alias="page-index",title="user id", ge=1, le=10000)):
    return {"page_index":f"{page_index}"}

@app.post("/user")
async def create_user(user_model:UserModel):
    user_dict = user_model
    return user_dict

@app.put("/user/{user_id}")
async def update_user(user_id:int, user_model:UserModel):
    user_dict = json.loads(user_model.json())
    user_dict.update({"id":user_id})
    return user_dict

@app.get("/user/{user_id}")
async def get_user(user_id:int = Path(..., title="user id", ge=1, le=10000)):
    return {"userid":f"{user_id}"}

@app.get("/user_regex/{user_regex}")
async def get_user_regex(user_regex:str = Path(..., title="user regex", regex="^[a|b|c]-[\\d]*$")):
    return {"user_regex":f"{user_regex}"}

@app.get("/user/{user_id}/friends")
async def get_user_friends(user_id:int,page_index:Optional[int]=30):
    return {"userid":f"{user_id}","page_index":page_index}

@app.get("/student/{gender}")
async def get_user(gender:Gender):
    return {"gender":f"{gender}"}

#======= 請求體 深入練習 =============
class Address(BaseModel):
    address:str
    postcode:int
    feature:List[str]


class User(BaseModel):
    username:str = Field(..., min_length=3, example="Leo")
    desc:Optional[str] = Field(None, max_length=20)
    gender:Gender
    address:Address

@app.put("/useraddress/{user_id}")
async def update_useraddress(user_id:int, user_model:User, address_model:Address, count:int=Body(3)):
    user_dict = json.loads(user_model.json())
    
    return user_dict

#======= HEADER COOKIE =============
@app.put("/carts")
async def update_cart(*,response:Response ,
                      favorite_type:Optional[str]=Cookie(None, alias="favorite-type"),
                      api_token:Union[str, None] = Header(None, alias="api-token")):
    result_duct = {
        "favorite_type":favorite_type,
        "api_token":api_token
    }
    
    response.set_cookie(key="favorite-type", value="dark")
    return result_duct

#======= RESPONSE MODEL =============
cartDict ={
    # 'a':{"id":1},
    'b':{"id":2, "name":"123"},
    'c':{"id":3, "name":"345","desc":"hihihi"}
}

class CartOut(BaseModel):
    id :int
    name :str

@app.get("/carts/{seq}", response_model=CartOut)
async def get_cart(seq:str):
    
    return cartDict.get(seq,{})

@app.get("/carts", response_model=List[CartOut])
async def get_carts():
     
    return list(cartDict.values())

if __name__ == "__main__":
    uvicorn.run(app="fastapi_basic:app", host="0.0.0.0", port=28000, reload=True)