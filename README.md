## Meal Planner & Grocery List Generator
    A command-line application to manage recipes and ingredients using SQLite and Python.

## Features

1. Recipe Management: Add, list, and delete recipes.
2. Ingredient Management: Add, list, and delete ingredients for recipes.

## Technologies

1. Python: Language used to build the CLI.
2. SQLite: Database for storing recipes and ingredients.
3. OOP: Organizing the application using classes. 

## Installation

1. Clone the repository:

    git clone "https://github.com/Leo-Muraya/Meal-planner-and-Grocery-list-generator-2.git"

    cd meal-planner

2. Install Python 3 if not already installed.

3. Set up the database:

    python main.py setup

## Usage

1. Add a Recipe
    python main.py add_recipe "Recipe Name" "Instructions"

2. List Recipes
    python main.py list_recipes

3. Delete a Recipe
    python main.py delete_recipe RECIPE_ID

4. Add an Ingredient to a Recipe
    python main.py add_ingredient RECIPE_ID "Ingredient" "Quantity"

5. List Ingredients for a Recipe
    python main.py view_ingredients RECIPE_ID

6. Delete an Ingredient
    python main.py delete_ingredient INGREDIENT_ID


## Database Schema

    Recipes Table: Stores id, name, and instructions.
    Ingredients Table: Stores id, name, quantity, and recipe_id.

## Code Structure

    model.py: Contains the database setup and classes for recipes and ingredients.
    main.py: Handles user input and interactions.

## License

    MIT License

    By Leo Muraya