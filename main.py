from model import Recipe, Ingredient, setup_database


def display_menu():
    print("\n=== Meal Planner & Grocery List Generator ===")
    print("1. Add Recipe")
    print("2. List Recipes")
    print("3. Delete Recipe")
    print("4. Add Ingredient")
    print("5. View Ingredients")
    print("6. Delete Ingredient")
    print("0. Exit")
    choice = input("Enter your choice: ")
    return choice


def main():
    setup_database()  # Initialize the database
    while True:
        choice = display_menu()

        if choice == "1":
            # Add Recipe
            name = input("Enter recipe name: ")
            instructions = input("Enter recipe instructions: ")
            Recipe.create(name, instructions)
            print(f"Recipe '{name}' added successfully!")

        elif choice == "2":
            # List Recipes
            recipes = Recipe.get_all()
            if recipes:
                print("\nRecipes:")
                for recipe in recipes:
                    print(f"ID: {recipe[0]}, Name: {recipe[1]}, Instructions: {recipe[2]}")
            else:
                print("No recipes found.")

        elif choice == "3":
            # Delete Recipe
            try:
                recipe_id = int(input("Enter recipe ID to delete: "))
                Recipe.delete(recipe_id)
            except ValueError:
                print("Invalid input. Please enter a valid numeric ID.")

        elif choice == "4":
            # Add Ingredient
            try:
                recipe_id = int(input("Enter recipe ID: "))
                name = input("Enter ingredient name: ")
                quantity = input("Enter ingredient quantity: ")
                Ingredient.create(name, quantity, recipe_id)
                print(f"Ingredient '{name}' added successfully to Recipe ID {recipe_id}!")
            except ValueError:
                print("Invalid input. Please enter valid numeric data.")

        elif choice == "5":
            # View Ingredients
            try:
                recipe_id = int(input("Enter recipe ID to view ingredients: "))
                ingredients = Ingredient.get_by_recipe(recipe_id)
                if ingredients:
                    print("\nIngredients:")
                    for ingredient in ingredients:
                        print(f"ID: {ingredient[0]}, Name: {ingredient[1]}, Quantity: {ingredient[2]}")
                else:
                    print("No ingredients found for this recipe.")
            except ValueError:
                print("Invalid input. Please enter a valid numeric ID.")

        elif choice == "6":
            # Delete Ingredient
            try:
                ingredient_id = int(input("Enter ingredient ID to delete: "))
                Ingredient.delete(ingredient_id)
            except ValueError:
                print("Invalid input. Please enter a valid numeric ID.")

        elif choice == "0":
            # Exit
            print("Exiting the Meal Planner. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
