from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    full_name: str
    hospital_id: str
    role: str  # admin, doctor, nurse

class UserResponse(BaseModel):
    id: int
    email: str
    full_name: str
    hospital_id: str
    role: str
    created_at: datetime
    
    class Config:
        from_attributes = True

class PatientRecordCreate(BaseModel):
    patient_id: str
    hospital_name: str
    department: str
    diagnosis: str
    treatment: str
    doctor: str

class PatientRecordResponse(BaseModel):
    id: int
    patient_id: str
    hospital_name: str
    department: str
    diagnosis: str
    treatment: str
    doctor: str
    fabric_transaction_id: Optional[str]
    created_at: datetime
    
    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None
