from fastapi import FastAPI, Request, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
import model.sqlalchemy_model as sqlalchemy_model
import model.pydantic_model as pydantic_model

# instantiate FastAPI
app = FastAPI()

# mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# instantiate Jinja2Templates
templates = Jinja2Templates(directory="templates")

# CORS
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


# front-end routes
@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse(name="index.html", context={"request": request})

@app.get("/add_order/")
async def add_order(request: Request):
    return templates.TemplateResponse(name="add_order.html", context={"request": request})

@app.get("/add_order/form_success")
async def form_success(request: Request):
    return templates.TemplateResponse(name="form_success.html", context={"request": request})

# back-end routes
@app.post("/add_order/add")
def add_single_order(order: pydantic_model.Orders):
    """
    Add a single order to the database.
    """
    # Covert pydantic model to SQLAlchemy model
    order = sqlalchemy_model.Orders(**order.model_dump())
    session = sqlalchemy_model.SessionLocal()
    session.add(order)
    session.commit()
    session.refresh(order)
    session.close()
    return {"message": "Order added successfully."}


     
"""
@app.post("/upload")
async def upload_file(request: Request, file: UploadFile = File(...)):
    contents = await file.read()
    contents = contents.decode("utf-8")
    return templates.TemplateResponse(name="display.html", 
                                      context={"request": request, "contents": contents}
                                      )
"""