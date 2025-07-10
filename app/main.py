from typing import Union

from fastapi import Body, FastAPI,Response,status,HTTPException,Depends
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
from .import models
from .database import engine,SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class Post(BaseModel):
    title: str
    content: str
    published: bool= True

while True:
    try:
        conn = psycopg2.connect(
            host='localhost',
            database='fastapi',
            user='postgres',
            password='youbitch',
            cursor_factory=RealDictCursor
        )
        cursor = conn.cursor()
        print("Database connection successful")
        break
    except Exception as error:
     print("Error connecting to the database")
     print("Error:", error)
    time.sleep(2)

my_posts = [{"title": "Post 1", "content": "Content 1", "published": True , "id": 1 },
             {"title": "Post 2", "content": "Content 2", "published": False , "id": 2 }]

def find_post(id):
    for post in my_posts:
        if post["id"] == id:
            return post

def find_index_post(id):
    for index,p in enumerate(my_posts):
        if p["id"]==id:
            return  index
        
@app.get("/sqlalchemy")
def test_posts(db: Session = Depends(get_db)):
    return {"message": "SQLAlchemy is working"}   
            
    

@app.get("/")
def read_root():
    return {"Hello": "fuck yo mister"}


@app.get("/posts")
def get_post():
    cursor.execute("""SELECT * FROM posts""")
    posts=cursor.fetchall()
    return {"Data": posts}
  
  

@app.post("/posts")
def create_post(post:Post):
    cursor.execute(""" INSERT INTO posts (title,content,published) VALUES (%s,%s,%s) RETURNING *""",(post.title,post.content,post.published))
    new_post=cursor.fetchone()
    conn.commit()
    return {"data": new_post}



@app.get("/posts/{id}")
def get_post(id: int):
    cursor.execute("""SELECT * FROM posts WHERE id=%s """,str(id),)
    get_new_post=cursor.fetchone()
    if not get_new_post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id: {id} was not found"
        )
    return {"detail": get_new_post}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int):
    cursor.execute("""DELETE FROM posts WHERE id =%s RETURNING *""",str(id),)
    deleted_post=cursor.fetchone()
    conn.commit() 

    if deleted_post== None :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id: {id} does not exist"
        )         
 
 
@app.put("/posts/{id}")
def update_post(id:int,post:Post):
     cursor.execute("""Update posts SET title=%s,content=%s,published=%s WHERE id=%s RETURNING *""",(post.title,post.content,post.published,str(id)))
     updated_post=cursor.fetchone()
     conn.commit()

     if updated_post== None :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id: {id} does not exist"
        )
     return{"data": updated_post}
     
 
    