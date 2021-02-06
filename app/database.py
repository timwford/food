import asyncio
from pprint import pprint

from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine

from models import Recipe

instances = [
    Recipe(name="Banana Bread", portions=2, owner='tim'),
    Recipe(name="Lentil Dip", portions=2, owner='tim')
]

async def get_instances():
    motor = AsyncIOMotorClient(host="209.159.204.189", port=5433)
    engine = AIOEngine(motor_client=motor, database="Recipe")
    results = await engine.find(Recipe, Recipe.owner == 'tim')
    pprint(results)

if __name__ == "__main__":
    asyncio.run(get_instances())
