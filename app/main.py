from fastapi import FastAPI, Request, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
#from sqlalchemy.orm import Session
#from database import SessionLocal, Orders

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

origins = [
    "http://127.0.0.1:8000",  # Allow localhost for development
    "http://your-production-url.com",  # Allow your production URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


templates = Jinja2Templates(directory="templates")

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse(name="index.html", context={"request": request})

@app.get("/add_order/")
async def add_order(request: Request):
    return templates.TemplateResponse(name="add_order.html", context={"request": request})

"""
@app.post("/orders/")
def create_customer(customer: Customer, db: Session = Depends(get_db)):
    db.add(customer)
    db.commit()
    db.refresh(customer)
    return customer

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
"""
        
"""
@app.post("/upload")
async def upload_file(request: Request, file: UploadFile = File(...)):
    contents = await file.read()
    contents = contents.decode("utf-8")
    return templates.TemplateResponse(name="display.html", 
                                      context={"request": request, "contents": contents}
                                      )
"""