from firstClass import llms 

class chatbot(llms):
    
    def __init__(self,model, query ):
        self.model = model 
        llms.__init__(self,query)
    
    def showme(self):
        print(f"i am calling {self.model}")
        llms.claude()
        llms.openai()
        
obj_inherit = chatbot("openai","aman is coding king")

print(obj_inherit.openai())
    