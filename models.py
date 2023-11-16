from pydantic import BaseModel, constr

class ChatMessage(BaseModel):
    user: constr(min_length=1, max_length=20)
    message: constr(min_length=1, max_length=100)