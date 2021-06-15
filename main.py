# JSON5 Format für die Möglichkeit der Formatierungsänderung (Kommentare, Absätze, etc.)
import pyjson5 as json
from dataclasses import dataclass
import dataclasses

with open('./recipes.json5', encoding='utf-8') as file:
    data = json.load(file)


@dataclass  # Methode __init__() zur Erzeugung von Objekten wird eingespart
class Ingredient:  # Aufteilung der Zutaten
    """ ... """
    name: str
    specification: str
    amount: str


@dataclass
class Recipe:  # Wiedergabe des Rezepts
    """" ... """
    id: int
    name: str
    portion: str
    difficulty: str
    preparation: str
    tip: str
    ingredients: list[Ingredient] = dataclasses.field(
        default_factory=list)  # Ausgabe der Zutaten in einer Liste

@dataclass
class RecipesDatabase:
    """ ... """
    all_recipes_dict: dict = dataclasses.field(
        default_factory = dict) 
    ingredient_dict: dict = dataclasses.field(
        default_factory = dict) 


    def read_json(self):
        """ ... """
        for recipe in data["recipes"]:
            new_recipe = Recipe(id=recipe["id"],
                                name=recipe["name"],
                                portion=recipe["portion"],
                                difficulty=recipe["difficulty"],
                                preparation=recipe["preparation"],
                                tip=recipe["tip"])

            for ingredient in recipe["ingredient"]:
                new_ingredient = Ingredient(ingredient["name"], ingredient.get(
                    "specification", ""), ingredient["amount"])
                new_recipe.ingredients.append(new_ingredient)

                current_recipes = self.ingredient_dict.get(
                    new_ingredient.name.casefold(), None)
                if current_recipes is None:
                    current_recipes = []
                current_recipes.append(new_recipe.id)
                self.ingredient_dict[new_ingredient.name.casefold()] = current_recipes
            self.all_recipes_dict[new_recipe.id] = new_recipe  # Dictonary nach ID

    
    def search_recipes_by_ingredients(self,ingredient):
        """ ... """
        recipes = []
        tmp = self.ingredient_dict[ingredient.casefold()]
        for recipe_id in tmp:
            recipes.append(self.all_recipes_dict[recipe_id])
        return recipes


db = RecipesDatabase()
db.read_json()
tmp = db.search_recipes_by_ingredients("Nudeln")
for recipe in tmp:
    #print(f"Id {recipe.id}: {recipe.name}")
    #print(f"Id {recipe.id}: {recipe.name} -> Schwierigkeit: {recipe.difficulty}")
    #print(f"Id {recipe.id}: {recipe.name}, Zubereitung: {recipe.preparation}")
    #print(recipe)