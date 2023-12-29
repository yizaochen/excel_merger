from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse(name="index.html", context={"request": request})

""""
@app.post("/upload")
async def upload_file(request: Request, file: UploadFile = File(...)):
    contents = await file.read()
    contents = contents.decode("utf-8")
    return templates.TemplateResponse(name="display.html", 
                                      context={"request": request, "contents": contents}
                                      )
"""