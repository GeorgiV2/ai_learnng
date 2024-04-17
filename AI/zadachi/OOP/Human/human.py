from food import Food,HealingFood,PoisonFood

class Human:
    def __init__(self,name:str,height:float,ecolor:str,weight:float):
        self.name = name
        self.height = height
        self.eyecolor = ecolor
        self.weight = weight
        self.health = 100
    
    def eat(self,food:Food):
        cal = food.calories
        self.weight += cal / 2500
        if isinstance(food, HealingFood):
            self.health = min(self.health + food.healing,100)
        elif isinstance(food, PoisonFood):
            self.health -= food.poison
            if(self.health <= 0):
                self.die()
        elif food.rot:
            self.health -= 5
            if(self.health <= 0):
                self.die()

    def die(self):
        print(self.name, "has died!")
