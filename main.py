import pyjson5 as json # JSON5 Format für die Möglichkeit der Formatierungsänderung (Kommentare, Absätze, etc.)
from dataclasses import dataclass
import dataclasses

with open('./recipes.json5',encoding='utf-8') as file:
    data = json.load(file)

@dataclass # Methode __init__() zur Erzeugung von Objekten wird eingespart
class Ingredient: # Aufteilung der Zutaten
    """ ... """
    name: str
    specification: str
    amount: str

@dataclass
class Recipe: # Wiedergabe des Rezepts
    """" ... """
    id: int
    name: str
    portion: str
    difficulty: str
    preparation: str
    tip: str
    ingredient: list[Ingredient] = dataclasses.field(default_factory=list) # Ausgabe der Zutaten in einer Liste

def readJSON():
    for recipe in data["recipes"]:
        #print("id: " + recipe["id"])
        print("name: " + recipe["name"])
        print("portion for: " + recipe["portion"])
        print("difficulty: " + recipe["difficulty"])
        print("preparation: " + recipe["preparation"])
        print("tip: " + recipe["tip"])
        #print("ingredients: " + recipe["ingredient"])
        print("")
print(readJSON())

#def main(): # Testfunktion mit (von Hand) angelegtem Rezept, bevor JSON Daten eingebunden werden
    #new_recipe = Recipe(
        #id = 1,
        #name = "Tomatensuppe",
        #portion = "4 Personen",
        #difficulty = "einfach",
        #preparation = "...",
        #tip = " ",
    #)
    #new_ingredient = Ingredient(
        #name = "Tomaten",
        #specification = " ",
        #amount = "500 gr"
    #)
    #new_recipe.ingredient.append(new_ingredient) # Hinzufügen der Zutat 1
    #new_ingredient = Ingredient(
        #name = "Sahne",
        #specification = " ",
        #amount = "200 gr"
    #)
    #new_recipe.ingredient.append(new_ingredient) # Hinzufügen der Zutat 2
    #new_recipe.ingredient.append(new_ingredient) # Hinzufügen der Zutat n
    #print(new_recipe)
#main()


#food_dict = dict()