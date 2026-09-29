from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"request": request}
    )


@app.post("/generate")
def generate_comic(
    story_prompt: str = Form(...),
    character_name: str = Form(...),
    setting: str = Form(...),
    story_tone: str = Form(...),
    art_style: str = Form(...)
):
    return {
        "message": "Comic generation request received!",
        "story_prompt": story_prompt,
        "character_name": character_name,
        "setting": setting,
        "story_tone": story_tone,
        "art_style": art_style
    }