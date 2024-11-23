
from fastapi import FastAPI 
from blog.database import engine
from blog.routers import blog, user, auth
from blog import models
import uvicorn


app = FastAPI()


models.Base.metadata.create_all(bind=engine)

app.include_router(blog.router) 
app.include_router(user.router)
app.include_router(auth.router)





if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8002, reload=True)







