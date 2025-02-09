class Recipe:
    def __init__(self, name, ingredients, prep_time, cook_time, calories, instructions):
        self.name = name
        self.ingredients = ingredients
        self.prep_time = prep_time
        self.cook_time = cook_time
        self.calories = calories 
        self.instructions = instructions

    def __repr__(self):
        return f"This recipe is {self.name}, it needs {len(self.ingredients)} ingredients totaling {self.calories} calories with a preparation time of {self.prep_time} minutes and a cooking timer of {self.cook_time} minutes"
    
    def total_cook_time(self):
        return self.cook_time + self.prep_time
    
recipe_1_instructions = """
    1 Prep: Bring a large pot of salted water to a boil. Wash and drie produce. Remove and discard any large stems from kale; roughly chop leaves. Peel and mince or grade garlic. Pat chicken dry with paper towels; season all over with salt, peper, and half the Tuscan Heat Spice (all for 4 servings).
    2 Cook Pasta: Once water is boiling, add spaghetti to pot. Cook until al dente, 9-11 minutes. Reserve 1/2 cup pasta cooking water then drain.
    3 Cook Kale: While pasta cooks, heat a drizzle of olive oilin a large pan over medium-high heat. Add kale and a splash of water. Cook until kale is wilted and very tender, 5-7 minutes. Tip: if necessary cook kale in batches. Stir in garlic and cook untill fragrant, 30 seconds. Season with salt and pepper. transfer to plate. 
    4 Cook Chiken: Heat another drizle of olive oil in pan used for kaleover medium-high heat. Add chiken and cook, stirring occasionally, until browned and cooked through, 4-6 minutes.
    5 Make Sauce: Return kale to pan with chicken and reduce heat to medium low. Add cream sauce. Stir in cream cheese and 1/4 cup reserved pasta cooking water. Bring to a simmer and cook until sauce is combined and thickened, 2-3 minutes. 
    6 Finish & Serve: Add drained spaghetti and 1 TBSP butter (2 TBSP for 4 servings) to pan with sauce; toss to combine. Season with salt and pepper. If needed, stir in more reserved pasta cooking water a splash at a time until pasta is ccoated in creamy sauce. Divide pasta between bowls, top with Parmesan and serve.
    """
recipe_1_ingredients = """
    2 people/4 people\n
    Kale: 4oz/8oz
    Garlic: 1 Clove/2 Cloves 
    Chiken Breast Strips: 10oz/20oz
    Tuscan Heat Spice: 1 TBSP
    Spaghetti: 6oz/12oz
    Cream Sauce Base: 4oz/8oz
    Cream Cheese: 2TBSP/4TBSP
    Parmesan Cheese: 1/4Cup / 1/2Cup
    """

recipe_2_instructions = """
    1 Cook Time: In a small pot, combine rice, 1 1/4 cups water (2 1/4 cups for 4 servings), and a pinch of salt. Bring to a boil, then cover and reduce to a low simmer. Cook until rice is tender, 15-18 minutes. Keep covered off heat until ready to serve.
    2 Prep & Mix Mayo: While rice cooks, wash and dry all produce. Zest and quarter lime. Roughly chop cilantro. In a small bowl, combine mayonaise with chili sauce to taste.
    3 Cook Pork: Heat a drizzle of oil in a large pan over medium-high heat. Add pork and a big pinch of salt. Cook, breaking up meat into pieces, until browned, 3-4 minutes.
    4 Finish & Serve: Fluff rice with a fork; stir in lime zest and 1 TBSP butter (2 TBSP for 4 servings). Season with salt and pepper. Divide rice between bowls and top with pork mixture and any remaining sauce from pan. Drizzle with chili mayo. Sprinkle with crispy fried onions and cilantro. Serve with lime wedges on the side.
    """
recipe_2_ingredients = """
    2 people/4 people\n
    Jasmine Rice: 3/4 Cup / 1 1/2 Cup
    Ground Pork: 10oz/20oz
    Mayonnaise: 2TBSP/4TBSP
    Sweet Thai Chili Sauce: 1oz/2oz
    Shredded Carrots: 4oz/8oz
    Sweet Soy Glaze: 4TBSP/8TBSP
    Sesame Dressing: 1.5oz/3oz
    Crispy Fried Onions: 1/2
    Cilantro: 1/4oz
    Lime: 1
    """

recipe_1 = Recipe("Tuscan Trattoria Chiken & Kale Spaguetti", recipe_1_ingredients, 5, 25, 850, recipe_1_instructions)
recipe_2 = Recipe("Sesame Soy Pork Bowl", recipe_2_ingredients, 5, 20, 1070, recipe_2_instructions)

print("""Welcome to the Recipe Book, we currently count with the following recipes:
      1 Tuscan Trattoria Chiken & Kale Spaghetti.
      2 Sesame Soy Pork Bowl.
      """)

while True:
    choice = input("What recipe would you like to make today? \n")
    if choice == "1":
        print(recipe_1.__repr__(), "\n", "Ingredients:\n",recipe_1.ingredients, "\nInstructions:\n", recipe_1.instructions)
    elif choice == "2":
        print("Ingredients:\n",recipe_2.ingredients, "\nInstructions:\n", recipe_2.instructions)
    elif choice != "1" or choice != "2":
        print(choice)