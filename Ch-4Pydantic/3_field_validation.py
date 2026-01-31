from pydantic import BaseModel, Field, field_validator  
from typing import Optional, Dict, Any, List, Literal

class personal_info(BaseModel):
    name: str = Field(..., min_length=3, max_length=20, description="this is name")
    age: int = Field(..., gt=0, description="this is age")
    email: str = Field(..., description="this is email")
    
    
    #Field validator for email         can  validated the income data  
    @field_validator("email")           #Field validation in Pydantic means applying rules 
    def email_check(cls, value):   # (like min, max, pattern, type checks) 
        if "@" not in value :       # to a field to make sure the data is
            raise ValueError("Invalid email address")   # valid before creating the model — 
        elif ".com" not in value:                   # all done using one line with Field().
            return value +".com"
        else:
            return value 
   # we use cli beacuse it is using it before class is creeated 
pyd_ins = personal_info(**{"name":"aman", "age":24, "email":"amanpathak8802@gmail.com"})
print(pyd_ins)