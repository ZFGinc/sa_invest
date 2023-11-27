#region Imports
from typing import Union
from fastapi import Depends, FastAPI, APIRouter, HTTPException

from typing import List,Optional
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from .repositories import UserRepo, ProjectRepo
from .db import get_db, engine
from .schemas import *
from .dependencies import get_token_header

#endregion

#region User endpoints

userRouter = APIRouter(
    prefix="/users",
    tags=["User"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@userRouter.post('/', tags=["User"],response_model=User,status_code=201)
async def create_user(user_request: UserCreate, db: Session = Depends(get_db)):
    db_user = UserRepo.fetch_by_id(db, id=user_request.id)
    if db_user:
        raise HTTPException(status_code=400, detail="User already exists!")

    return await UserRepo.create(db=db, user=user_request)

@userRouter.get('/', tags=["User"],response_model=List[User])
def get_all_users(id: Optional[int] = None,db: Session = Depends(get_db)):
    if id:
        users =[]
        db_user = UserRepo.fetch_by_id(db,id)
        users.append(db_user)
        return users
    else:
        return UserRepo.fetch_all(db)
    
@userRouter.delete('/{user_id}', tags=["User"])
async def delete_user(user_id: int,db: Session = Depends(get_db)):
    db_user = UserRepo.fetch_by_id(db,user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found with the given ID")
    await UserRepo.delete(db,user_id)
    return "User deleted successfully!"

@userRouter.put('/{user_id}', tags=["User"],response_model=User)
async def update_user(user_id: int,user_request: User, db: Session = Depends(get_db)):
    db_user = UserRepo.fetch_by_id(db, user_id)
    if db_user:
        update_user_encoded = jsonable_encoder(user_request)
        db_user.firstName = update_user_encoded['firstName']
        db_user.lastName = update_user_encoded['lastName']
        db_user.middleName = update_user_encoded['middleName']
        db_user.email = update_user_encoded['email']
        db_user.role_code = update_user_encoded['role_code']

        return await UserRepo.update(db=db, user_data=db_user)
    else:
        raise HTTPException(status_code=400, detail="User not found with the given ID")
    
#endregion

#region Project endpoints

projectRouter = APIRouter(
    prefix="/project",
    tags=["Project"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@projectRouter.post('/', tags=["Project"],response_model=Project,status_code=201)
async def create_project(project_request: ProjectCreate, db: Session = Depends(get_db)):
    db_project = ProjectRepo.fetch_by_id(db, id=project_request.id)
    if db_project:
        raise HTTPException(status_code=400, detail="Project already exists!")

    return await ProjectRepo.create(db=db, project=project_request)

@projectRouter.get('/', tags=["Project"],response_model=List[Project])
def get_all_projects(id: Optional[int] = None,db: Session = Depends(get_db)):
    if id:
        projects =[]
        db_project = ProjectRepo.fetch_by_id(db,id)
        projects.append(db_project)
        return projects
    else:
        return ProjectRepo.fetch_all(db)
    
@projectRouter.delete('/{project_id}', tags=["Project"])
async def delete_project(project_id: int,db: Session = Depends(get_db)):
    db_project = ProjectRepo.fetch_by_id(db,project_id)
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found with the given ID")
    await ProjectRepo.delete(db,project_id)
    return "Project deleted successfully!"

@projectRouter.put('/{project_id}', tags=["Project"],response_model=Project)
async def update_project(project_id: int,user_request: Project, db: Session = Depends(get_db)):
    db_project = ProjectRepo.fetch_by_id(db, project_id)
    if db_project:
        update_project_encoded = jsonable_encoder(user_request)
        db_project.user_id = update_project_encoded['user_id']

        return await ProjectRepo.update(db=db, project_data=db_project)
    else:
        raise HTTPException(status_code=400, detail="Project not found with the given ID")
    
#endregion