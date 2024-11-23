from fastapi import APIRouter
from blog import database, schemas 
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from blog.hashing import Hash
from blog.repository import user


router = APIRouter(
    tags=["user"],
    prefix="/user",
)


#user login
@router.post("/", status_code=status.HTTP_200_OK)
def create_user(req: schemas.User, db:Session = Depends(database.get_db)):
    return user.create_user(req, db)
   
@router.get("/{id}", status_code=status.HTTP_200_OK)
def get_user(id: int, db: Session = Depends(database.get_db)):
    return user.get_user(id, db)