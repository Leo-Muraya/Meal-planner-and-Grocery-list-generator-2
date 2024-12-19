import sqlite3

def setup_database():
    """Create tables if they don't exist."""
    with sqlite3.connect('meal_planner.db') as conn:
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
                recipe_id INTEGER,
                FOREIGN KEY (recipe_id) REFERENCES recipes (id)
            )
        ''')
        conn.commit()

class Recipe:
    def __init__(self, id=None, name=None, instructions=None):
        self.id = id
        self.name = name
        self.instructions = instructions

    @classmethod
    def create(cls, name, instructions):
        with sqlite3.connect('meal_planner.db') as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO recipes (name, instructions) VALUES (?, ?)', (name, instructions))
            conn.commit()
            return cls(id=cursor.lastrowid, name=name, instructions=instructions)

    @classmethod
    def get_all(cls):
        with sqlite3.connect('meal_planner.db') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM recipes')
            recipes = cursor.fetchall()
            return [cls(id=recipe[0], name=recipe[1], instructions=recipe[2]) for recipe in recipes]

    @classmethod
    def delete(cls, recipe_id):
        with sqlite3.connect('meal_planner.db') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM recipes WHERE id = ?', (recipe_id,))
            recipe = cursor.fetchone()
            if recipe:
                cursor.execute('DELETE FROM recipes WHERE id = ?', (recipe_id,))
                conn.commit()
                return True
            return False

    @classmethod
    def find_by_id(cls, recipe_id):
        with sqlite3.connect('meal_planner.db') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM recipes WHERE id = ?', (recipe_id,))
            recipe = cursor.fetchone()
            if recipe:
                return cls(id=recipe[0], name=recipe[1], instructions=recipe[2])
            return None

class Ingredient:
    def __init__(self, id=None, name=None, quantity=None, recipe_id=None):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.recipe_id = recipe_id

    @classmethod
    def create(cls, name, quantity, recipe_id):
        with sqlite3.connect('meal_planner.db') as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO ingredients (name, quantity, recipe_id) VALUES (?, ?, ?)', (name, quantity, recipe_id))
            conn.commit()
            return cls(id=cursor.lastrowid, name=name, quantity=quantity, recipe_id=recipe_id)

    @classmethod
    def get_all_for_recipe(cls, recipe_id):
        with sqlite3.connect('meal_planner.db') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM ingredients WHERE recipe_id = ?', (recipe_id,))
            ingredients = cursor.fetchall()
            return [cls(id=ingredient[0], name=ingredient[1], quantity=ingredient[2], recipe_id=ingredient[3]) for ingredient in ingredients]

    @classmethod
    def delete(cls, ingredient_id):
        with sqlite3.connect('meal_planner.db') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM ingredients WHERE id = ?', (ingredient_id,))
            ingredient = cursor.fetchone()
            if ingredient:
                cursor.execute('DELETE FROM ingredients WHERE id = ?', (ingredient_id,))
                conn.commit()
                return True
            return False
