"""-----What will I learn in this project-----
- 1. What is file reading in Python?
- 2. Reading files using open.
- 3. Reading modes (r, rb, r+).
- 4. Handling file reading errors.
- 5. Project 15: recipe viewer app.
"""
# %% 1. What is file reading in Python?
# Reading files using open function reading modes which are R, RB and R plus and handling file reading.

#%% 2. Read files using open.
with open("sample.txt", "r") as file:
  content = file.read()
  print(content)

with open("sample.txt", "r") as file:
  for line in file:
    print(line.strip())

#%% 3. Read models (r, rb, r+).
# "r" is used to read a text file.
# "rb" is used to read a binary file.
# "r+" is use to read and write file.
with open("sample.txt", "r") as file:
  lines = file.readlines()
  for line in lines:
    print(line.strip())

#%%4. Handling file reading errors.
try:
  with open("sample.txt", "r") as file:
    content = file.read()
    print(content)
except FileNotFoundError:
  print("File not found.")

# %% Project 15: recipe viewer app.
# Step 1: Load Recipes from File
def load_recipes(file_path):
  try:
    with open(file_path, "r") as file:
      content = file.read()
      recipes = content.split("\n\n")
      recipe_dict = {}
      for recipe in recipes:
        lines = recipe.split("\n")
        if len(lines) >= 3:
          name = lines[0].strip()
          ingredients = lines[1].replace('Ingredients: ','').strip()
          instructions = lines[2].replace('Instructions: ', '').strip()
          recipe_dict[name] = {"ingredients": ingredients, "instructions": instructions}
      return recipe_dict
  except FileNotFoundError:
    print("File not found.")
    return {}

# Step 2: Display Recipe Menu
def show_menu():
  print("\n--- Recipe Viewer Menu ---")
  print("1. View Recipe by Name")
  print("2. List All Recipes")
  print("3. Exit")

# Step 3: Display Recipe Details
def view_recipe(recipes):
  name = input("Enter the name of the recipe: ").strip()
  if name in recipes:
    print(f"\n--- Recipe {name} Details ---")
    print(f"Ingredients: {recipes[name]['ingredients']}")
    print(f"Instructions: {recipes[name]['instructions']}")
  else:
    print("Recipe not found.")

# Step 4: Main Program
recipe_file = "recipes.txt"
recipes = load_recipes(recipe_file)

while True:
  show_menu()
  choice = input("Enter your choice (1/2/3): ")

  if choice == '1':
    view_recipe(recipes)
  elif choice == '2':
    print("\n--- All Recipes ---")
    for name in recipes:
      print(name)
  elif choice == '3':
    print("Exiting the program.")
    break
  else:
    print("Invalid choice. Please try again.")
# %%
