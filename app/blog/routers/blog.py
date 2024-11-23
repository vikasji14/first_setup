from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from blog import database, schemas, oauth2
from blog.repository import blog



router = APIRouter(
    tags=["blog"],
    prefix="/blog",
)


@router.get("/", response_model=List[schemas.ShowBlog])
def allBlogs(db:Session = Depends(database.get_db), get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)


@router.post("/", status_code=status.HTTP_201_CREATED )
def createBlog(req: schemas.Blog, db:Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(req, db)




@router.get("/{id}", status_code=status.HTTP_200_OK)
def showBlogByid(id,  db:Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.getById(id, db)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def deleteBlog(id, db:Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.deleteByID(id, db)
