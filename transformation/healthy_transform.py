from transformation.universal import get_food_info, replace_original, search_original


HFOOD = {
    'turkey bacon': ['bacon', 'sausage', 'ham', 'salami'],
    'organic honey': ['brown sugar','sugar', 'syrup'],
    'coconut oil': ['butter', 'sesame oil']
}

HCOOK = [('fry', 'broil'), ('fry', 'steam'), ('fry', 'boil'), ('fry','grill')]

def all_unhealthy_food():
  results = []
  for sub, cands in HFOOD.items():
    for cand in cands:
      results.append(cand)
  return results

def all_healthy_food():
  return list(HFOOD.keys())

def all_unhealthy_methods():
  results = []
  for pair in HCOOK:
    bad, good = pair
    new_pair = (good, bad)
    results.append(new_pair)
  return results

def all_healthy_methods():
  return HCOOK

def find_healthy_sub(food):
  original = ''
  replacement = ''
  for tar, candidates in HFOOD.items():
    for candidate in candidates:
      if candidate in food:
        replacement = tar
        original = candidate
  return original, replacement

def find_unhealthy_sub(food):
  original = ''
  replacement = ''
  for tar, candidates in HFOOD.items():
    if tar in food:
      original = tar
      replacement = candidates[0]

  return original, replacement

def to_healthy_ingredients(ingredients):
  new_ingredients = []
  replacements = []

  for igd in ingredients:
    quant, unit, name = get_food_info(igd)
    pot_sub = ''

    # Checking if current igd is unhealthy
    for unhealthy in all_unhealthy_food():
      if unhealthy in name or name in unhealthy:
        replacement = find_healthy_sub(name)
        if all(replacement):
          replacements.append(replacement)
          pot_sub = replace_original(igd, replacement)
    
    if pot_sub:
      new_ingredients.append(pot_sub)
    else:
      new_ingredients.append(igd)

  return new_ingredients, replacements

def to_unhealthy_ingredients(ingredients):
  new_ingredients = []
  replacements = []

  for igd in ingredients:
    quant, unit, name = get_food_info(igd)
    pot_sub = ''

    # Checking if current igd is healthy
    for healthy in all_healthy_food():
      if healthy in name or name in healthy:
        replacement = find_unhealthy_sub(name)
        if all(replacement):
          replacements.append(replacement)
          pot_sub = replace_original(igd, replacement)
    
    if pot_sub:
      new_ingredients.append(pot_sub)
    else:
      new_ingredients.append(igd)

  return new_ingredients, replacements

def if_healthy_transform(command):
  return search_original(command, "healthy")

def if_unhealthy_transform(command):
  return search_original(command, "unhealthy")