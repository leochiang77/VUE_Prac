from a2wsgi import ASGIMiddleware
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from router import cvdcapa
from router import cvdcapa_chamber
from router import sptcapa



app = FastAPI(title="Array Manage Center API",version="1.0.0", swagger_ui_parameters={"syntaxHighlight": False})
app.include_router(cvdcapa.router)
app.include_router(cvdcapa_chamber.router)
app.include_router(sptcapa.router)

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

wsgi_app = ASGIMiddleware(app)

if __name__ == "__main__":
    uvicorn.run(app="main:app", host="0.0.0.0", port=28000, reload=True)