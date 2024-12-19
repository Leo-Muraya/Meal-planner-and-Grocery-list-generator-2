import argparse
from model import Recipe, Ingredient, setup_database

class MealPlannerCLI:
    def __init__(self):
        setup_database()  
        
        self.parser = argparse.ArgumentParser(description="Meal Planner CLI")
        self.subparsers = self.parser.add_subparsers()

        # Add Recipe 
        self.add_recipe_parser = self.subparsers.add_parser('add_recipe', help="Add a new recipe")
        self.add_recipe_parser.add_argument('name', type=str, help="Name of the recipe")
        self.add_recipe_parser.add_argument('instructions', type=str, help="Instructions for the recipe")
        self.add_recipe_parser.set_defaults(func=self.add_recipe)

        # List Recipes 
        self.list_recipes_parser = self.subparsers.add_parser('list_recipes', help="List all recipes")
        self.list_recipes_parser.set_defaults(func=self.list_recipes)

        # Delete Recipe 
        self.delete_recipe_parser = self.subparsers.add_parser('delete_recipe', help="Delete a recipe by ID")
        self.delete_recipe_parser.add_argument('recipe_id', type=int, help="ID of the recipe to delete")
        self.delete_recipe_parser.set_defaults(func=self.delete_recipe)

        # View Ingredients 
        self.view_ingredients_parser = self.subparsers.add_parser('view_ingredients', help="View ingredients for a recipe")
        self.view_ingredients_parser.add_argument('recipe_id', type=int, help="ID of the recipe to view ingredients for")
        self.view_ingredients_parser.set_defaults(func=self.view_ingredients)

        # Add Ingredient 
        self.add_ingredient_parser = self.subparsers.add_parser('add_ingredient', help="Add an ingredient to a recipe")
        self.add_ingredient_parser.add_argument('recipe_id', type=int, help="ID of the recipe")
        self.add_ingredient_parser.add_argument('name', type=str, help="Name of the ingredient")
        self.add_ingredient_parser.add_argument('quantity', type=str, help="Quantity of the ingredient")
        self.add_ingredient_parser.set_defaults(func=self.add_ingredient)

        # Delete Ingredient 
        self.delete_ingredient_parser = self.subparsers.add_parser('delete_ingredient', help="Delete an ingredient by ID")
        self.delete_ingredient_parser.add_argument('ingredient_id', type=int, help="ID of the ingredient to delete")
        self.delete_ingredient_parser.set_defaults(func=self.delete_ingredient)

    def run(self):
        args = self.parser.parse_args()
        if hasattr(args, 'func'):
            args.func(args)
        else:
            self.parser.print_help()

    def add_recipe(self, args):
        """Add a new recipe."""
        recipe = Recipe.create(args.name, args.instructions)
        print(f"Recipe '{recipe.name}' added successfully!")

    def list_recipes(self, args):
        """List all recipes."""
        recipes = Recipe.get_all()
        if recipes:
            for recipe in recipes:
                print(f"{recipe.id}. {recipe.name}")
        else:
            print("No recipes found.")

    def delete_recipe(self, args):
        """Delete a recipe."""
        success = Recipe.delete(args.recipe_id)
        if success:
            print(f"Recipe with ID {args.recipe_id} deleted.")
        else:
            print("Recipe not found.")

    def view_ingredients(self, args):
        """View ingredients for a recipe."""
        ingredients = Ingredient.get_all_for_recipe(args.recipe_id)
        if ingredients:
            for ingredient in ingredients:
                print(f"{ingredient.name} - {ingredient.quantity}")
        else:
            print("No ingredients found for this recipe.")

    def add_ingredient(self, args):
        """Add an ingredient to a recipe."""
        ingredient = Ingredient.create(args.name, args.quantity, args.recipe_id)
        print(f"Ingredient '{ingredient.name}' added to recipe.")

    def delete_ingredient(self, args):
        """Delete an ingredient."""
        success = Ingredient.delete(args.ingredient_id)
        if success:
            print(f"Ingredient with ID {args.ingredient_id} deleted.")
        else:
            print("Ingredient not found.")

if __name__ == '__main__':
    cli = MealPlannerCLI()
    cli.run()
