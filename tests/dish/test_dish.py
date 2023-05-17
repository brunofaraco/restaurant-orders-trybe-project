import pytest
from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient


# Req 2
def test_dish():
    carbonara = "Macarrão a carbonara"
    lasanha = "Lasanha de cogumelos"

    carbonara_instance = Dish(carbonara, 79.90)
    lasanha_instance = Dish(lasanha, 69.90)

    assert carbonara_instance.name == carbonara
    assert carbonara_instance == carbonara_instance
    assert carbonara_instance != lasanha_instance
    assert hash(carbonara_instance) == hash(repr(carbonara_instance))
    assert repr(carbonara_instance) == f"Dish('{carbonara}', R$79.90)"

    carbonara_instance.add_ingredient_dependency(Ingredient("Ovo"), 1.90)

    assert carbonara_instance.recipe == {Ingredient("Ovo"): 1.90}
    assert carbonara_instance.get_ingredients() == set(
        carbonara_instance.recipe.keys()
    )
    assert carbonara_instance.get_restrictions() == set()

    FLOAT_ERROR = "Dish price must be float."
    PRICE_GT_ZERO_ERROR = "Dish price must be greater then zero."

    with pytest.raises(TypeError, match=FLOAT_ERROR):
        Dish(carbonara, "79,90")
    with pytest.raises(ValueError, match=PRICE_GT_ZERO_ERROR):
        Dish(carbonara, -9)