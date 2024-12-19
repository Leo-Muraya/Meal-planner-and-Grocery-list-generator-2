import sqlite3
from database import connect_db

class Recipe:
    def __init__(self, name, instructions, id=None):
        self.id = id
        self.name = name
        self.instructions = instructions

    def save(self):
        """Save a new recipe to the database."""
        conn = connect_db()
        cursor = conn.cursor()
        
        cursor.execute('''INSERT INTO recipes (name, instructions) 
                          VALUES (?, ?)''', (self.name, self.instructions))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        """Get all recipes from the database."""
        conn = connect_db()
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM recipes')
        recipes = cursor.fetchall()
        conn.close()
        
        return [Recipe(id=r[0], name=r[1], instructions=r[2]) for r in recipes]

    @staticmethod
    def find_by_id(recipe_id):
        """Find a recipe by its ID."""
        conn = connect_db()
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM recipes WHERE id = ?', (recipe_id,))
        result = cursor.fetchone()
        conn.close()
        
        if result:
            return Recipe(id=result[0], name=result[1], instructions=result[2])
        return None

    def delete(self):
        """Delete this recipe from the database."""
        conn = connect_db()
        cursor = conn.cursor()
        
        cursor.execute('DELETE FROM recipes WHERE id = ?', (self.id,))
        conn.commit()
        conn.close()


class Ingredient:
    def __init__(self, name, quantity, recipe_id, id=None):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.recipe_id = recipe_id

    def save(self):
        """Save a new ingredient to the database."""
        conn = connect_db()
        cursor = conn.cursor()
        
        cursor.execute('''INSERT INTO ingredients (name, quantity, recipe_id)
                          VALUES (?, ?, ?)''', (self.name, self.quantity, self.recipe_id))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all_by_recipe(recipe_id):
        """Get all ingredients for a specific recipe."""
        conn = connect_db()
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM ingredients WHERE recipe_id = ?', (recipe_id,))
        ingredients = cursor.fetchall()
        conn.close()
        
        return [Ingredient(id=i[0], name=i[1], quantity=i[2], recipe_id=i[3]) for i in ingredients]
    
    def delete(self):
        """Delete this ingredient from the database."""
        conn = connect_db()
        cursor = conn.cursor()
        
        cursor.execute('DELETE FROM ingredients WHERE id = ?', (self.id,))
        conn.commit()
        conn.close()
