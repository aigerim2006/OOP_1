import sqlite3

connect = sqlite3.connect("recipes.db")
cursor = connect.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS recipes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    ingredients TEXT,
    time_to_cook INTEGER,
    difficulty TEXT
)
""")

connect.commit()

def create_recipe(name, ingredients, time_to_cook, difficulty):
    cursor.execute("""
    INSERT INTO recipes (name, ingredients, time_to_cook, difficulty)
    VALUES (?, ?, ?, ?)
    """, (name,ingredients,time_to_cook,difficulty))
    connect.commit()
    print("Рецепт добавлен!")

def get_all_recipes():
    cursor.execute("SELECT * FROM recipes")
    recipes = cursor.fetchall()
    for r in recipes:
        print(r)

def update_recipe(recipe_id, new_name):
    cursor.execute("""
    UPDATE recipes
    SET name = ?
    WHERE id = ?
    """, (new_name, recipe_id))
    connect.commit()
    print("Рецепт обновлен!")

def delete_recipe(recipe_id):
    cursor.execute("DELETE FROM recipes WHERE id = ?", (recipe_id,))
    connect.commit()
    print("Рецепт удален!")

create_recipe(
    "Лагман",
    "Лапша, мясо, капуста, марковь",
    70,
    "medium"
)

create_recipe(
    "Блинчики",
    "Мука, молоко, яйца, сахар",
    30,
    "easy"
)

print("\nВсе рецепты : ")
get_all_recipes()
update_recipe(1, "Босо лагман")
print("После обновления : ")
get_all_recipes()
delete_recipe(2)
print("\nПосле удаления : ")
get_all_recipes()
connect.close()


