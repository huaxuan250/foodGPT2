from pyfood.utils import Shelf
from ingredient_parser import parse_ingredient
from transformation.universal import replace_original

VEGIE = {
    'tofu' : ['beef', 'salmon', 'steak', 'ground turkey', 'pork', 'fish', 'trout', 'fillet', 'cod', 'halibut'],
    'seitan': ['beef', 'turkey', 'pork', 'ham'],
    'lentil': ['bacon', 'sausage', 'ham'],
    'mushroom': ['shrimp', 'crab', 'lobster'],
    'jackfruit' : ['octopus', 'squid'],
}

SEAFOOD = {
    'salmon': ['salmon', 'salmon steak'],
    'tuna': ['tuna', 'tuna steak', "ahi tuna steak"]
}

def handle_seafood_name(name):
  for k, values in SEAFOOD.items():
    for v in values:
      if v in name:
        return k

def get_food_info(igd):
  info = parse_ingredient(igd)
  quant = info['quantity']
  unit = info['unit']
  name = info['name']
  combo = [quant, unit, name]
  return combo

def all_meat():
  shelf = Shelf()
  all_foods = list(shelf.feats.items())
  results = []
  for food in all_foods:
    _, info = food
    food_taxon = info['taxon']
    if food_taxon in ['211', '212', '213', '214']:
      if 'egg' not in info['en']:
        results.append(info['en'])
  return results

def all_vegie():
  shelf = Shelf()
  all_foods = list(shelf.feats.items())
  results = []
  for food in all_foods:
    _, info = food
    food_taxon = info['taxon']
    if food_taxon in ['002', '003', '004']:
      results.append(info['en'])
  return results

def find_vegie_sub(food):

  original = ''
  replacement = ''

  is_seafood = handle_seafood_name(food)
  if is_seafood:
    food = is_seafood

  for tar, candidates in VEGIE.items():
    for candidate in candidates:
      if candidate in food:
        replacement = tar
        original = candidate

  return original, replacement

def find_meat_sub(food):

  original = ''
  replacement = ''
  for tar, candidates in VEGIE.items():
    if tar in food:
      original = tar
      replacement = candidates[0]

  return original, replacement

def to_vegie_ingredients(ingredients):
  new_ingredients = []
  replacements = []

  for igd in ingredients:
    quant, unit, name = get_food_info(igd)
    pot_sub = ''

    # Checking if current igd has meat
    for meat in all_meat():
      if meat in name or name in meat:
        replacement = find_vegie_sub(name)
        if all(replacement):
          replacements.append(replacement)
          pot_sub = replace_original(igd, replacement)
    
    if pot_sub:
      new_ingredients.append(pot_sub)
    else:
      new_ingredients.append(igd)

  return new_ingredients, replacements

def to_meat_ingredients(ingredients):
  new_ingredients = []
  replacements = []

  for igd in ingredients:
    quant, unit, name = get_food_info(igd)
    pot_sub = ''

    # Checking if current igd has meat
    for vegie in all_vegie():
      if vegie in name or name in vegie:
        replacement = find_meat_sub(name)

        if all(replacement):
          replacements.append(replacement)
          pot_sub = replace_original(igd, replacement)
    
    if pot_sub:
      new_ingredients.append(pot_sub)
    else:
      new_ingredients.append(igd)

  return new_ingredients, replacements

def if_vegie_transform(command):
  return "vegetarian" in command or 'vegie' in command

def if_meat_transform(command):
  return "meat" in command
