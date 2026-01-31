from pydantic import BaseModel, Field, field_validator , model_validator 
from typing import Optional, Dict, Any, List, Literal

class Api_auth(BaseModel):
    email: str = Field(...,description="this is name")
    passward: str = Field(..., min_length=8 ,description="this is name")
    confirm_passward: str = Field(..., min_length=8, description="this is name")
    
    
    @model_validator(mode = 'after')
    def password_check(cls,values): 
           # we use cli beacuse it is using it before class is creeated 
        if values.passward != values.confirm_passward :
            raise ValueError("password not matching")
        return values
    
pyd_ins = Api_auth(**{"email":"amanpathak8802@gmail.com","passward":"pass1234","confirm_passward":"pass1234"})
print(pyd_ins)

from pydantic import BaseModel, Field,  computed_field
from typing import Optional, Dict, Any, List, Literal

class orders(BaseModel):
    
    id : int = Field(...,description= "Order Id")
    unit_price : int = Field(...,description= "Unitprice")
    amount :int = Field(...,description= "Amount Per unit")
    
    @computed_field
    @property
    def total_amount(self)-> int:
        return self.unit_price*self.amount

pyd_ins = orders(**{"id": 1, "unit_price":10, "amount":100})
print(pyd_ins)
    
    