import click
from model import Recipe, Ingredient
from database import create_tables

create_tables()


@click.group()
def cli():
    """Meal Planner CLI"""
    pass


@click.command()
@click.argument('name')
@click.argument('instructions')
def add_recipe(name, instructions):
    """Add a new recipe to the meal planner."""
    recipe = Recipe(name, instructions)
    recipe.save()
    click.echo(f"Recipe '{name}' added successfully!")


@click.command()
def list_recipes():
    """List all recipes in the meal planner."""
    recipes = Recipe.get_all()
    if recipes:
        for recipe in recipes:
            click.echo(f"{recipe.id}. {recipe.name}")
    else:
        click.echo("No recipes found.")


@click.command()
@click.argument('recipe_id', type=int)
def delete_recipe(recipe_id):
    """Delete a recipe by ID."""
    recipe = Recipe.find_by_id(recipe_id)
    if recipe:
        recipe.delete()
        click.echo(f"Recipe '{recipe.name}' deleted.")
    else:
        click.echo("Recipe not found.")


@click.command()
@click.argument('recipe_id', type=int)
def view_ingredients(recipe_id):
    """View ingredients for a specific recipe."""
    ingredients = Ingredient.get_all_by_recipe(recipe_id)
    if ingredients:
        for ingredient in ingredients:
            click.echo(f"{ingredient.name} - {ingredient.quantity}")
    else:
        click.echo("No ingredients found for this recipe.")


@click.command()
@click.argument('recipe_id', type=int)
@click.argument('name')
@click.argument('quantity')
def add_ingredient(recipe_id, name, quantity):
    """Add an ingredient to a recipe."""
    recipe = Recipe.find_by_id(recipe_id)
    if recipe:
        ingredient = Ingredient(name, quantity, recipe_id)
        ingredient.save()
        click.echo(f"Ingredient '{name}' added to recipe '{recipe.name}'.")
    else:
        click.echo("Recipe not found.")


@click.command()
@click.argument('ingredient_id', type=int)
def delete_ingredient(ingredient_id):
    """Delete an ingredient by ID."""
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM ingredients WHERE id = ?', (ingredient_id,))
    ingredient = cursor.fetchone()
    
    if ingredient:
        ingredient_obj = Ingredient(id=ingredient[0], name=ingredient[1], quantity=ingredient[2], recipe_id=ingredient[3])
        ingredient_obj.delete()
        click.echo(f"Ingredient '{ingredient[1]}' deleted.")
    else:
        click.echo("Ingredient not found.")
    conn.close()


cli.add_command(add_recipe)
cli.add_command(list_recipes)
cli.add_command(delete_recipe)
cli.add_command(view_ingredients)
cli.add_command(add_ingredient)
cli.add_command(delete_ingredient)


if __name__ == '__main__':
    cli()
