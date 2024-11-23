from typing import List
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from blog import schemas, models
from blog.hashing import Hash



def create_user(req: schemas.User, db: Session):
    user = models.User(name=req.name, email=req.email, password=Hash.bcrypt(req.password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user