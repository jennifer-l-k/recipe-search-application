import pyjson5 as json
from dataclasses import dataclass
import dataclasses

with open('./recipes.json5', encoding='utf-8') as file:
    data = json.load(file)


@dataclass  #Methode __init__() zur Erzeugung von Objekten wird eingespart
class Ingredient:  #Aufteilung der Zutaten
    """More precise breakdown of the individual ingredient structures."""
    name: str
    specification: str
    amount: str


@dataclass
class Recipe:
    """Container class or template for the entire recipe structure."""
    id: int
    name: str
    portion: str
    difficulty: str
    preparation: str
    tip: str
    ingredients: list[Ingredient] = dataclasses.field(
        default_factory=list)

    def __str__(self):
        return self.name

    def format_recipe(self):
        return "Rezept hier:" + self.name


@dataclass
class RecipesDatabase:
    """Reading in the recipe database with processing of the data in various functions.
    These are divided into the methods "read_json" and "search_recipes_by_ingredients."""
    all_recipes_dict: dict = dataclasses.field(
        default_factory = dict)
    name_dict: dict = dataclasses.field(
        default_factory = dict)
    ingredient_dict: dict = dataclasses.field(
        default_factory = dict) 


    def read_json(self):
        """Read in the recipes from the database "recipes.json5". 
        The corresponding data is then assigned to Dictonarsys."""
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
            self.all_recipes_dict[new_recipe.id] = new_recipe  #Dictonary after ID
            self.name_dict[new_recipe.name] = new_recipe #Dictionary after name, because of the Listbox Widget

    def search_recipes_by_ingredients(self,ingredient):
        """Search function for a food key within the recipe database."""
        recipes = []
        tmp = self.ingredient_dict[ingredient.casefold()]
        for recipe_id in tmp:
            recipes.append(self.all_recipes_dict[recipe_id])
        return recipes