from pydantic import BaseModel, Field

class address(BaseModel):
    street: str = Field(..., description="this is street")
    city: str = Field(..., description="this is city")
    state: str = Field(..., description="this is state")
    country: str = Field(..., description="this is country")
    zip_code: str = Field(..., description="this is zip_code")


class personal_info(BaseModel):
    name: str = Field(..., description="this is name")
    age: str = Field(..., description="this is age")
    email: str = Field(..., description="this is email")

    # IMPORTANT: use address model here, not str
    addrress: address = Field(..., description="this is address")


pyud_ins = personal_info(**{
    "name": "aman pathak",
    "age": "24",
    "email": "amanpathak8802@gmail.com",
    "addrress": address(**{
        "street": "123 Main st",
        "city": "Anytown",
        "state": "CA",
        "country": "xyz",
        "zip_code": "1234"
    })
})

print(pyud_ins)
