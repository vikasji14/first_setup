from sqlalchemy.orm import Session
from blog import models, schemas
from fastapi import HTTPException, status   

def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs

def createBlog(req: schemas.Blog, db: Session):
    new_blog = models.Blog(title=req.title, body=req.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def getById(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    return blog

def deleteByID(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    return {"detail": f"Blog with id {id} deleted"}