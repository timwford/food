from typing import Optional

from odmantic import Field, Model

class Recipe(Model):
    name: str
    portions: int = Field(ge=1)
    owner: Optional[str] = None
    continent: Optional[str] = None


class Ingredient(Model):
    name: str