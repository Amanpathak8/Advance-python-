from pydantic import BaseModel, Field, EmailStr
from typing import List
from typing_extensions import Literal

class PersonalInfo(BaseModel):
    name: str = Field(..., min_length=3, max_length=20, description="this is name")
    age: int = Field(..., gt=0, description="this is age")
    email: EmailStr = Field(..., description="this is email") #email str is special for Emails make by pydantic
    gender: Literal["male", "female", "other"] = Field(..., description="this is gender")
    salaries: List[int] = Field(..., description="this is salaries")

def main(para1: PersonalInfo):
    print("name:", para1.name)
    print("age:", para1.age)
    print("email:", para1.email)
    print("gender:", para1.gender)
    print("salaries:", para1.salaries)

pyd_ins = PersonalInfo(
    name="aman",
    age=19,
    email="Amanpathak8802@gmail.com",
    gender="male",
    salaries=[1, 2]
)  # another way of maining pydantic instane 
# pyd_ins = personal_info(**{"name":"aman", "age":24, "email":"amanpathak8802@gmail.com"})

main(pyd_ins)