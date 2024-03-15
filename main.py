from fastapi import FastAPI, Depends
from jwtservice import get_current_user

app = FastAPI(docs_url='/')


@app.get('/home')
async def home():
    return "This is home page"


@app.post('/register')
async def register():
    return 'Register page'


@app.post('/login')
async def login():
    return 'Login page'


@app.get("/secure-data")
async def secure_data(current_user: dict = Depends(get_current_user)):
    return {"message": "This data is secure", "user": current_user}
