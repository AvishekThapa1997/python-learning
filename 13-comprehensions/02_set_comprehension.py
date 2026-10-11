items = {2,2,3,4,5}
print(items)

recipes = {
    "Masala Chai":["ginger", "cardamom", "clove"],
    "Elaichi Chai":["cardamom", "milk"],
    "Spicy Chai":["ginger", "black pepper", "clove"]
}

unique_spices = {
    ingredient
    for ingredients in recipes.values()
    for ingredient in ingredients
}

print(unique_spices)

print(set([1,2,2]))