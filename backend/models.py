from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.sql import func
from database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    full_name = Column(String)
    hospital_id = Column(String)
    role = Column(String)  # admin, doctor, nurse
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class PatientRecord(Base):
    __tablename__ = "patient_records"
    
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(String, unique=True, index=True)
    hospital_name = Column(String)
    department = Column(String)
    diagnosis = Column(Text)
    treatment = Column(Text)
    doctor = Column(String)
    fabric_transaction_id = Column(String)  # Link to Fabric blockchain
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class AuditLog(Base):
    __tablename__ = "audit_logs"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    action = Column(String)
    resource_type = Column(String)
    resource_id = Column(String)
    details = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
