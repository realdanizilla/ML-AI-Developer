from pydantic import BaseModel, Field, EmailStr, conset, validator, HttpUrl #conlist
from datetime import datetime

class User(BaseModel):
    id: int
    name: str
    age: int = Field (..., gt=0) 
    email: EmailStr
    nota: int = Field (..., ge=0)
    materias: conset(str, min_length=1, max_length=3)
    password: str
    password_confirm: str
    start_date: datetime
    end_date: datetime
    site: HttpUrl

    @validator('password_confirm')
    def password_confirmation(cls, v, values):
        if 'password' in values and v != values['password']:
            raise ValueError("passwords don't match")
        return v
    
    @validator('end_date')
    def end_date_validation(cls, v, values):
        if 'start_date' in values and v <= values['start_date']:
            raise ValueError("end date must be after start date")
        return v


user = User(
    id=1, 
    name="Rapha", 
    age="36", 
    email="raphael@raphael.com", 
    nota=5, 
    materias=["Matemática", "calculo", "Matemática"],
    password='asd13124312',
    password_confirm='asd13124312',
    start_date='2024-01-01',
    end_date='2024-01-31',
    site='http://www.aluno.com'
)

# algumas coisas são convertidas, por exemplo age="36" convert para int 36

print(user)