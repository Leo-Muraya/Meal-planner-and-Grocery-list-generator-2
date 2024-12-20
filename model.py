import sqlite3

# Database setup
def setup_database():
    conn = sqlite3.connect("meal_planner.db")
    cursor = conn.cursor()

    # Create recipes table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS recipes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        instructions TEXT NOT NULL
    )
    ''')

    # Create ingredients table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS ingredients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        quantity TEXT NOT NULL,
        recipe_id INTEGER NOT NULL,
        FOREIGN KEY (recipe_id) REFERENCES recipes (id)
    )
    ''')

    conn.commit()
    conn.close()


# Recipe model
class Recipe:
    @staticmethod
    def create(name, instructions):
        conn = sqlite3.connect("meal_planner.db")
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO recipes (name, instructions) VALUES (?, ?)',
            (name, instructions)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        conn = sqlite3.connect("meal_planner.db")
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM recipes')
        recipes = cursor.fetchall()
        conn.close()
        return recipes

    @staticmethod
    def delete(recipe_id):
        conn = sqlite3.connect("meal_planner.db")
        cursor = conn.cursor()
        cursor.execute('DELETE FROM recipes WHERE id = ?', (recipe_id,))
        conn.commit()
        if cursor.rowcount == 0:
            print("Recipe not found.")
        else:
            print(f"Recipe with ID {recipe_id} deleted successfully!")
        conn.close()


# Ingredient model
class Ingredient:
    @staticmethod
    def create(name, quantity, recipe_id):
        conn = sqlite3.connect("meal_planner.db")
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO ingredients (name, quantity, recipe_id) VALUES (?, ?, ?)',
            (name, quantity, recipe_id)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def get_by_recipe(recipe_id):
        conn = sqlite3.connect("meal_planner.db")
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM ingredients WHERE recipe_id = ?', (recipe_id,))
        ingredients = cursor.fetchall()
        conn.close()
        return ingredients

    @staticmethod
    def delete(ingredient_id):
        conn = sqlite3.connect("meal_planner.db")
        cursor = conn.cursor()
        cursor.execute('DELETE FROM ingredients WHERE id = ?', (ingredient_id,))
        conn.commit()
        if cursor.rowcount == 0:
            print("Ingredient not found.")
        else:
            print(f"Ingredient with ID {ingredient_id} deleted successfully!")
        conn.close()
