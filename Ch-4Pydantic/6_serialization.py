from pydantic import BaseModel, Field 
from typing import Optional , Dict , Any , List , Literal 

class InputModel(BaseModel):
    query: str = Field(..., description="this is query")

class OutputModel(BaseModel):
    query: str = Field(..., description="query")
    results: str = Field(..., description="this is result")


def process_data(p_input: InputModel) -> OutputModel:
    input_query = p_input.query
    result = "hello Bro"


    pyd_output = OutputModel(**{"query": input_query,"results":result})
    return pyd_output



input_query = InputModel(**{"query":"how are you "})

# call function
response = process_data(input_query)

print(response)
# we are returing data in pydantic formate it can not be
# used further so we have to covert it into json or dict for this use  model dump 
print("------------------------------dict ")
print(response.model_dump())


print("------------------------------json ")
print(response.model_dump_json())


