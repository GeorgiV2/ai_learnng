class Food:
    def __init__(self,calories:float,rot:bool):
        self.calories = calories
        self.rot = rot
       

class HealingFood(Food):
    def __init__(self, calories: float, rot: bool, healing: float):
        super().__init__(calories, rot)
        self.healing = healing

class PoisonFood(Food):
     def __init__(self, calories: float, rot: bool,poison:float):
        super().__init__(calories, rot)
        self.poison = poison