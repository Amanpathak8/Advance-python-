from pydantic import BaseModel, Field,  computed_field
from typing import Optional, Dict, Any, List, Literal

class orders(BaseModel):
    
    id : int = Field(...,description= "Order Id")
    unit_price : int = Field(...,description= "Unitprice")
    amount :int = Field(...,description= "Amount Per unit")
    
    @computed_field
    @property     # we use self  beacuse it is using it after  class is creeated  and their values are set 
    def total_amount(self)-> int:
        return self.unit_price*self.amount

pyd_ins = orders(**{"id": 1, "unit_price":10, "amount":100})
print(pyd_ins)
    
    