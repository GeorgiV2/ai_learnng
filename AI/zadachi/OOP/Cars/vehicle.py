class Vehicle:

    def drive(self):
       print("Driving")
    
    def start(self):
        return "Starting"

class Car(Vehicle):
    def __init__(self,model: str,name: str,hp,color: str):
        self.model = model
        self.name = name
        self.hp = hp
        self.color = color