from sqlalchemy.orm import Session
from . import models, schemas

class UserRepo():
    async def create(db: Session, user: schemas.UserCreate):
        db_user = models.user(firstName=user.firstName, 
                              lastName=user.lastName, 
                              middleName=user.middleName, 
                              email=user.email, 
                              role_code=user.role_code)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    def fetch_by_id(db: Session,_id):
        return db.query(models.user).filter(models.user.id == _id).first()
 
    def fetch_by_name(db: Session,name):
        return db.query(models.user).filter(models.user.name == name).first()
    
    def fetch_all(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.user).offset(skip).limit(limit).all()
    
    async def delete(db: Session,user_id):
        db_user= db.query(models.user).filter_by(id=user_id).first()
        db.delete(db_user)
        db.commit()
        
        
    async def update(db: Session,user_data):
        updated_user = db.merge(user_data)
        db.commit()
        return updated_user
    
    
class ProjectRepo():
    async def create(db: Session, project: schemas.ProjectCreate):
        db_project = models.project(
                                user_id = project.user_id,
                                owner_id = project.user_id,
                                address_id = project.user_id,
                                industry_id = project.user_id,
                                name = project.user_id,
                                application_own_amount = project.user_id,
                                application_support_amount = project.user_id,
                                work_place_count = project.user_id,
                                nalog_amount = project.user_id,
                                description = project.user_id,
                                state = project.user_id)
        db.add(db_project)
        db.commit()
        db.refresh(db_project)
        return db_project

    def fetch_by_id(db: Session,_id):
        return db.query(models.project).filter(models.project.id == _id).first()
 
    def fetch_by_name(db: Session,name):
        return db.query(models.project).filter(models.project.name == name).first()
    
    def fetch_all(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.project).offset(skip).limit(limit).all()
    
    async def delete(db: Session,project_id):
        db_project= db.query(models.project).filter_by(id=project_id).first()
        db.delete(db_project)
        db.commit()
        
    async def update(db: Session, data):
        updated = db.merge(data)
        db.commit()
        return updated