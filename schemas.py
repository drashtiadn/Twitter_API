from pydantic import BaseModel
from typing import List, Optional

class TweetBase(BaseModel):
    content: str

class TweetCreate(TweetBase):
    owner_id: int

class Tweet(TweetBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    hashed_password: str

class User(UserBase):
    id: int
    tweets: List[Tweet] = []

    class Config:
        orm_mode = True

class FollowerBase(BaseModel):
    user_id: int
    follower_id: int

class FollowerCreate(FollowerBase):
    pass

class Follower(FollowerBase):
    id: int

    class Config:
        orm_mode = True
