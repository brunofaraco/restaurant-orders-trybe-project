from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    GLUTEN = "GLUTEN"
    LACTOSE = "LACTOSE"

    gluten_instance = Ingredient(GLUTEN)
    lactose_instance = Ingredient(LACTOSE)

    assert gluten_instance.name == GLUTEN
    assert gluten_instance == gluten_instance
    assert hash(gluten_instance) == hash(GLUTEN)
    assert repr(gluten_instance) == f"Ingredient('{GLUTEN}')"
    assert gluten_instance.restrictions == set()
    assert gluten_instance != lactose_instance