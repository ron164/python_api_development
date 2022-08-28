# -*- coding: utf-8 -*-
# @Time : 27-08-2022 11:50
# @Author : rohan
# @File : user.py
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from .. import models, schemas, utils, oauth2
from sqlalchemy.orm import Session
from ..database import engine, get_db

router = APIRouter(prefix="/users", tags=['users'])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # hassh the password
    hashed_pwd = utils.hash(user.password)
    user.password = hashed_pwd
    new_user = models.User(**user.dict())  # Efficient way to get data when 50/100 columns are in the table
    db.add(new_user)  # Add the new user to the DB
    db.commit()
    db.refresh(new_user)  # same as RETURNING in SQL
    return new_user


@router.get("/{id}", response_model=schemas.UserOut)
def get_users(id: int, db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id: {id} does not exists")
    return user
