from pydantic import BaseModel

class ChatRequest(BaseModel):
    message: str
    role: str = "asistente"
    reset: bool = False
class ChatResponse(BaseModel):
    response: str

