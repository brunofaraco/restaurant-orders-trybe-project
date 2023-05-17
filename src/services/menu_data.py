import pandas as p
from src.models.ingredient import Ingredient
from src.models.dish import Dish

# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.dishes_path = p.read_csv(source_path).itertuples(index=False)
        self.dishes_map()

    def dishes_map(self):
        for name, price, ingredient, amount in self.dishes_path:
            dish_instance = Dish(name, float(price))

            if dish_instance not in self.dishes:
                dish_instance.add_ingredient_dependency(Ingredient(ingredient), int(amount))
                self.dishes.add(dish_instance)
            else:
                for dish in self.dishes:
                    if dish == dish_instance:
                        dish.add_ingredient_dependency(
                            Ingredient(ingredient), int(amount)
                        )