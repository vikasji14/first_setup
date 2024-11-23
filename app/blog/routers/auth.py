
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from blog import database, schemas, models, token
from blog.hashing import Hash
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter(
    # prefix="/auth",
    tags=["auth"]
)

@router.post("/login")
async def login(req:OAuth2PasswordRequestForm=Depends() ,db:Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == req.username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if not Hash.verify(user.password, req.password):
        raise HTTPException(status_code=404, detail="Incorrect password")
    
    #Generte a token and returen it
    access_token = token.create_access_token( data={"sub": user.email} )
    return {"access_token": access_token, "token_type": "bearer"}
    return user