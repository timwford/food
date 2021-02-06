import asyncio

import pandas
from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine

from models import Ingredient

async def create_ingredients_from_csv():
    ingredients = pandas.read_csv('ingredients.csv', header=None)
    print(ingredients[0].tolist())

    models = []
    for ingredient_name in ingredients[0].tolist():
        models.append(Ingredient(name=ingredient_name))

    motor = AsyncIOMotorClient(host="209.159.204.189", port=5433)
    engine = AIOEngine(motor_client=motor, database="Recipe")

    await engine.save_all(models)

if __name__ == "__main__":
    asyncio.run(create_ingredients_from_csv())