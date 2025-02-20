import fastapi
from fastapi import FastAPI, APIRouter, HTTPException, Depends
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware



class TestRequest(BaseModel):
    name: str
    age: int

class TestResponse(BaseModel):
    message: str

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


router_ = APIRouter()


@router_.post("/test", response_model=TestResponse)
async def test_1(request: TestRequest):
    # Do something with the request
    return TestResponse(message=f"Hello, {request.name}! You are {request.age} years old.")


if __name__ == "__main__":
    import uvicorn
    app.include_router(router_)
    uvicorn.run(app, host="0.0.0.0", port=8040)
