from pydantic import BaseModel


class SignInModel(BaseModel):
    work_space_name: str
    email: str
    password: str
