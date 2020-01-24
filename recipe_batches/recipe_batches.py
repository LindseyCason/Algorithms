#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  batches=[]
  # count=0
  for item in recipe:
    if item not in ingredients.keys():
      print("MISSING:", item)
      return 0
    else:
        if ingredients[item] // recipe[item] ==0:
          print("NOT ENOUGH INGREDIENTS")
          return 0
        else:
          batches.append(ingredients[item] // recipe[item])
    batches.sort()
      # print("final", amount.sort())
  print(f"You can make {batches[0]} batch(es)")
  return batches[0]



# if __name__ == '__main__':
#   # Change the entries of these dictionaries to test 
#   # your implementation with different inputs
#   recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
#   ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
#   print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))