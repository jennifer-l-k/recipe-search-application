from dataclasses import dataclass
import dataclasses

import pyjson5 as json
import Levenshtein

with open('./recipes.json5', encoding='utf-8') as file:
    data = json.load(file)


@dataclass  #Methode __init__() zur Erzeugung von Objekten wird eingespart
class Ingredient:  #Aufteilung der Zutaten
    """The "Ingredient" class describes a more detailed breakdown 
    of the individual ingredient structures. 
    Here, each individual ingredient is fractionated down to "Name", "Specification" and "Amount"."""
    name: str
    specification: str
    amount: str


@dataclass
class Recipe:
    """The container class "Recipe" represents a template for the entire recipe structure.
    In addition, methods are included here, which output a corresponding output 
    within the user interface and go through various case distinctions for the ingredient list."""
    id: int
    name: str
    portion: str
    difficulty: str
    preparation: str
    tip: str
    ingredients: list[Ingredient] = dataclasses.field(
        default_factory=list)


    def __str__(self):
        """Represent recipe with name as a string."""
        return self.name
        

    def format_recipe(self):
        """This specifies a corresponding arrangement 
        of the output of the selected recipe in the text widget."""
        list_of_ingredients = "Zutaten: \n\n"

        for ingredients_list in self.ingredients:
            list_of_ingredients += f"- {ingredients_list.name}\n"
            if ingredients_list.specification != "":
                list_of_ingredients += f"  {ingredients_list.specification}\n"
            if ingredients_list.amount != "":
                list_of_ingredients += f"  {ingredients_list.amount}\n"
            list_of_ingredients += "\n"


        out = f"Ausreichend für: {self.portion}\n\n"
        out += f"{list_of_ingredients}"
        out += f"Schwierigkeit: {self.difficulty}\n\n"
        out += f"Zubereitung: {self.preparation}\n\n"
        out += f"Tipp: {self.tip}"

        return out


@dataclass
class RecipesDatabase:
    """The "RecipesDatabase" class reads the corresponding recipe data from the 
    json5 file so that it can be processed in the methods and dictonaries associated with this class."""
    all_recipes_dict: dict = dataclasses.field(
        default_factory = dict)
    name_dict: dict = dataclasses.field(
        default_factory = dict)
    ingredient_dict: dict = dataclasses.field(
        default_factory = dict) 


    def read_json(self):
        """Read in the recipes from the database "recipes.json5". 
        The corresponding data is then assigned to Dictonaries."""
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

    def fuzzy_search_recipes_by_ingredients(self, ingredient):
        """Ingredient search with Levenshtein distance."""
        cutoff = 3
        max_matches = 3
        
        # Fuzzy match ingredient name first
        matches = []

        for key in self.ingredient_dict:
            dist = Levenshtein.distance(key, ingredient)
            if dist < cutoff:
             matches.append((key, dist))

        if len(matches) == 0:
            return []

        # Sort matches, fetch and return recipes for matched ingredients
        sorted_matches = sorted(matches, key=lambda tup: tup[1])
        max_index = min(max_matches, len(sorted_matches))
        print(sorted_matches)
        recipes = []
        for i in range(max_index):
            for recipe in self.search_recipes_by_ingredients(sorted_matches[i][0]):
                    if recipe not in recipes:
                        recipes.append(recipe)

        return recipes