import os
from pathlib import Path

def make_ingredient_list():
    try:
        with open("Ingredients.txt", "r") as file:
            ingredients = [line.strip() for line in file]
        return ingredients
    except FileNotFoundError:
        return None

def make_recipe_list():
    try:
        with open("RecipesList.txt", "r") as file:
            recipes = [line.strip().split(",") for line in file]
        return recipes
    except FileNotFoundError:
        return None
        
def output_recipe(ingredients, recipes):
    try:
        file_path = Path("RecipePossible.txt")
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with open(file_path, "w") as file:
            for recipe in recipes:
                recipe_not_in = True
                for ingredient in recipe[1:]:
                    if ingredient in ingredients and recipe_not_in:
                        file.write(recipe[0] + "\n")
                        recipe_not_in = False
                        break
    except IOError:
        print("Error occurred while writing to the file.")

ingredients = make_ingredient_list()
recipes = make_recipe_list()
output_recipe(ingredients, recipes)