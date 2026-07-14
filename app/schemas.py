from pydantic import BaseModel, EmailStr

# ---------- User Schemas ----------

class UserCreate(BaseModel):
    full_name: str
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    full_name: str
    email: EmailStr

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str


# ---------- Task Schemas ----------

class TaskCreate(BaseModel):
    title: str
    description: str
    completed: bool = False


class Task(TaskCreate):
    id: int
    user_id: int

    class Config:
        from_attributes = True