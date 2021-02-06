from typing import List

import uvicorn
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

from odmantic import AIOEngine

from models import Ingredient, Recipe

app = FastAPI()

motor = AsyncIOMotorClient(host="209.159.204.189", port=5433)
engine = AIOEngine(motor_client=motor, database="Recipe")

@app.get("/ingredient/", response_model=List[Ingredient])
async def get_ingredients():
    results = await engine.find(Ingredient)
    return results

@app.get("/recipe/", response_model=List[Recipe])
async def get_recipes():
    results = await engine.find(Recipe)
    return results

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, log_level="info")

"""
@app.put("/trees/", response_model=Tree)
async def create_tree(tree: Tree):
    await engine.save(tree)
    return tree


@app.get("/trees/", response_model=List[Tree])
async def get_trees():
    trees = await engine.find(Tree)
    return trees


@app.get("/trees/count", response_model=int)
async def count_trees():
    count = await engine.count(Tree)
    return count


@app.get("/trees/{id}", response_model=Tree)
async def get_tree_by_id(id: ObjectId):
    tree = await engine.find_one(Tree, Tree.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree
"""