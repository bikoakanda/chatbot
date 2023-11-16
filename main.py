from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from models import ChatMessage

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static") # Mount the static directory to the /static route to make the CSS accessible

templates = Jinja2Templates(directory="templates/")

chat_messages = [ # Simple hard coded message history
    ChatMessage(user="AI", message="Hello!"),
    ChatMessage(user="user", message="Please call me Karl."),
    ChatMessage(user="AI", message="Will do. How can I help you?"),
]


@app.get("/", response_class=HTMLResponse)
def index(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(
        "index.html", {"request": request, "chat_messages": chat_messages} # Pass the chat_messages to the template
    )


@app.post("/ask-ai", response_class=HTMLResponse) # Create a new route for the ask-ai endpoint
def ask_ai(request: Request, message: str = Form(...)) -> HTMLResponse:
    chat_messages.append(ChatMessage(user="user", message=message)) # Add the user message to the chat_messages

    return templates.TemplateResponse(
        "chat-messages.html", {"request": request, "chat_messages": chat_messages} # Pass the chat_messages to the template
    )