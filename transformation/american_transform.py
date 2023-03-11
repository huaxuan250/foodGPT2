from pyfood.utils import Shelf
from transformation.universal import get_food_info, replace_original, search_original

def all_fish():
  shelf = Shelf()
  all_foods = list(shelf.feats.items())
  results = []
  for food in all_foods:
    _, info = food
    food_taxon = info['taxon']
    if food_taxon in ['211']:
        results.append(info['en'])
  
  results.append("shrimp")
  results.append("prawn")

  return results

def all_pasta_and_carbs():
  shelf = Shelf()
  all_foods = list(shelf.feats.items())
  results = []
  for food in all_foods:
    _, info = food
    food_taxon = info['taxon']
    if food_taxon in ['104']:
        results.append(info['en'])

  results.append("rice")
  results.append("noodle")
  results.append("pho")
  
  return results

AMERICAN = {
    'butter': ['oil'], 
    'french fries': all_pasta_and_carbs(),
    'ketchup': ['vinegar', 'tomato', 'marinara'],
    'bourbon': ['wine', 'broth'],
    'beer': ['water', 'brandy'],
    'hot dog': all_fish()
}

def all_non_american_food():
  results = []
  for sub, cands in AMERICAN.items():
    for cand in cands:
      results.append(cand)
  return results

def find_american_sub(food):
  original = ''
  replacement = ''
  for tar, candidates in AMERICAN.items():
    for candidate in candidates:
      if candidate in food:
        replacement = tar
        original = candidate
  return original, replacement

def to_american_ingredients(ingredients):
  new_ingredients = []
  replacements = []

  for igd in ingredients:
    quant, unit, name = get_food_info(igd)
    pot_sub = ''

    # Checking if current igd is unhealthy
    for unhealthy in all_non_american_food():
      if unhealthy in name or name in unhealthy:
        replacement = find_american_sub(name)
        if all(replacement):
          replacements.append(replacement)
          pot_sub = replace_original(igd, replacement)
    
    if pot_sub:
      new_ingredients.append(pot_sub)
    else:
      new_ingredients.append(igd)

  return new_ingredients, replacements

def if_american_transform(command):
  return search_original(command, "american")