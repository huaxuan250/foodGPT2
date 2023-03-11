from transformation.universal import get_food_info

def if_mag(command):
  if "double" in command or "half" in command:
    return True
  else:
    return False

def handle_mag(command):
  if "double" in command:
    return 2
  else:
    return 0.5

def mult_ingredients(ingredients, mult):

  results = []

  for ingredient in ingredients:
    amt, unit, name = get_food_info(ingredient)
    new_amt = float(amt) * mult
    new_amt = str(new_amt)
    new_info = ' '.join([new_amt, unit, name])
    results.append(new_info)
  
  return results