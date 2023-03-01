class Sp:
    def __init__(self) :
        self.message = "Esto es un subprocess externo (sp1.py), corriendo de forma paralela a main.py"
    
    def callSp(self) :
        return self.message
    
if __name__ == '__main__' :
    object = Sp() 
    print(object.callSp())