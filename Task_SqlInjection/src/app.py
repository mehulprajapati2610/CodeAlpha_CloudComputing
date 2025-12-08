from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from db_init import init_db
from crypto import encrypt
from db_ops import save_user

app = FastAPI()
init_db()

CAP_CODE = "allow-sql-test"

class User(BaseModel):
    username: str
    secret: str

class SQLTest(BaseModel):
    query: str
    code: str

@app.post("/user/")
def create_user(user: User):
    enc = encrypt(user.secret)
    save_user(user.username, enc)
    return {"status": "saved"}

@app.post("/sql-test/")
def run_test(data: SQLTest):
    if data.code != CAP_CODE:
        raise HTTPException(status_code=403, detail="Not allowed")
    return {"status": "SQL test executed"}
