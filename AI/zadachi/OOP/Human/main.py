from food import Food,HealingFood,PoisonFood
from human import Human

gosho = Human("Gosho",185,"blue",70)
berry = HealingFood(50,False,4)
burger = Food(1500,False)
atropa = PoisonFood(100,False,10)

gosho.eat(atropa)
print(gosho.health)
gosho.eat(burger)
gosho.eat(burger)
print(f"{gosho.weight:.2f}")
gosho.eat(berry)
print(gosho.health)