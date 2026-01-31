from pydantic import BaseModel, Field    # strictInt It is used when you want only fix vakues no changes 

class input(BaseModel):
    
    x : int = Field(...,description = "this is x ")
    y : str  = Field(...,description = "this is y") # this ... means required 

pyd_input = input(**{"x":1,"y":"aman pathak"})  # ** is used for more values in dictonary 
# instance of pydantic model we will use above instance 
# to passs values in other fuctions/variable with pydantic datatype 

# pyd_input = input(x="10",y = "aman pathak ") # can be used like this 

def main(para1:input):  # we made input our own custom data type before so we will use our \
     print("hello amanpathak")  # own data type which have rules  and we have to use our own parser for \
                    #passing values can not pass value normally 

#main(xyz) can not pass any other value it should be pydantic intsance 
main(pyd_input) #- passing pydinsput it is our pydantic instance 