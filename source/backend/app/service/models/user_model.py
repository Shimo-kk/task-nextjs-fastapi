from pydantic import BaseModel


class UserCreateModel(BaseModel):
    work_space_id: int
    name: str
    email: str
    password: str
    is_admin: bool


class UserReadModel(BaseModel):
    id: int
    work_space_id: int
    name: str
    email: str
    is_admin: bool


class UserUpdateModel(BaseModel):
    id: int
    name: str
    is_admin: bool
