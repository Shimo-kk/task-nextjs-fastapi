from pydantic import BaseModel


class WorkSpaceCreateModel(BaseModel):
    work_space_name: str
    admin_name: str
    admin_email: str
    admin_password: str


class WorkSpaceReadModel(BaseModel):
    id: int
    name: str
