
class llms:
    token_size = 100 
    def __init__(self, query):   # <-- FIXED
        self.query = query 
        
    
    def openai(self):
        print(f"i am openai you asked {self.query}") 
    
    def claude(self):
        print("i am claude")  
    
    def llam(self):
        print("i am llam")  
        

## to checkcode it will not be inherited by children 
if __name__ == "__main__":
    
    obj = llms("aman is senior enginner ")
    print(obj.openai())

    