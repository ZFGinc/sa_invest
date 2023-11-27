from sqlalchemy import Column, Integer, String, Float, Date, Enum
from .db import Base

from .enums import *




class user(Base):
    __tablename__ = "user"
    
    id = Column(Integer, primary_key=True, index=True)
    firstName = Column(String, nullable=False)
    lastName = Column(String, nullable=False)
    middleName = Column(String, nullable=False)
    email = Column(String, nullable=False)
    role_code = Column(Enum(role_code_type), nullable=True)
    
    def __repr__(self):
        return f"<User(id={self.id}, " \
                f"firstName=\"{self.firstName}\", " \
                f"lastName=\"{self.lastName}\", " \
                f"middleName=\"{self.middleName}\", " \
                f"email=\"{self.email}\", " \
                f"role_code=\"{self.role_code})>"
    
    
class project(Base):
    __tablename__ = "project"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    owner_id = Column(Integer, nullable=False)
    address_id = Column(Integer, nullable=False)
    industry_id = Column(Integer, nullable=False)
    name = Column(String, nullable=False)
    application_own_amount = Column(Float, nullable=False)
    application_support_amount = Column(Float, nullable=False)
    work_place_count = Column(Integer, nullable=False)
    nalog_amount = Column(Integer, nullable=False)
    description = Column(String, nullable=False)
    state = Column(Enum(project_state_type), nullable=False)
    
    def __repr__(self):
        return f"<Project(id={self.id}, " \
                f"user_id=\"{self.user_id}\", " \
                f"owner_id=\"{self.owner_id}\", " \
                f"address_id=\"{self.address_id}\", " \
                f"industry_id=\"{self.industry_id}\", " \
                f"name=\"{self.name}\", " \
                f"application_own_amount=\"{self.application_own_amount}\", " \
                f"application_support_amount=\"{self.application_support_amount}\", " \
                f"work_place_count=\"{self.work_place_count}\", " \
                f"nalog_amount=\"{self.nalog_amount}\", " \
                f"description=\"{self.description}\", " \
                f"state=\"{self.state})>"
    
    
class support(Base):
    __tablename__ = "support"
    
    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, primary_key=True, index=True)
    support_programm_id = Column(Integer, primary_key=True, index=True)
    support_org_id = Column(Integer, primary_key=True, index=True)
    date_start = Column(Date, primary_key=True, index=True)
    date_end = Column(Date, primary_key=True, index=True)
    type_code = Column(Enum(support_type), primary_key=True, index=True)
    amount = Column(Float, primary_key=True, index=True)
    unit = Column(Enum(unit_type), primary_key=True, index=True)
    desc  = Column(String, primary_key=True, index=True)
    
    def __repr__(self):
        return f"<Support(id={self.id}, " \
                f"project_id=\"{self.project_id}\", " \
                f"support_programm_id=\"{self.support_programm_id}\", " \
                f"support_org_id=\"{self.support_org_id}\", " \
                f"date_start=\"{self.date_start}\", " \
                f"date_end=\"{self.date_end}\", " \
                f"type_code=\"{self.type_code}\", " \
                f"amount=\"{self.amount}\", " \
                f"unit=\"{self.unit}\", " \
                f"desc=\"{self.desc})>"
    
    
class address(Base):
    __tablename__ = "address"
    
    id = Column(Integer, primary_key=True, index=True)
    district_id = Column(Integer, primary_key=True, index=True)
    city_id = Column(Integer, primary_key=True, index=True)
    post_code = Column(String, primary_key=True, index=True)
    address = Column(String, primary_key=True, index=True)
    
    def __repr__(self):
        return f"<Address(id={self.id}, " \
                f"district_id=\"{self.district_id}\", " \
                f"city_id=\"{self.city_id}\", " \
                f"post_code=\"{self.post_code}\", " \
                f"address=\"{self.address})>"
    
    
class decision(Base):
    __tablename__ = "decision"
    
    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, primary_key=True, index=True)
    decision_type = Column(Enum(decision_type), primary_key=True, index=True)
    decision_date = Column(String, primary_key=True, index=True)
    protocol_number = Column(String, primary_key=True, index=True)
    decision = Column(String, primary_key=True, index=True) 
    
    def __repr__(self):
        return f"<Decision(id={self.id}, " \
                f"project_id=\"{self.project_id}\", " \
                f"decision_type=\"{self.decision_type}\", " \
                f"decision_date=\"{self.decision_date}\", " \
                f"protocol_number=\"{self.protocol_number}\", " \
                f"decision=\"{self.decision})>"