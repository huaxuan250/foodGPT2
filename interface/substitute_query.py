from scrapping.step_extraction import extract_food_name
from pyfood.utils import Shelf

def if_sub_food(command):
  command = command.lower()
  if 'substitute' in command:
    return True
  else:
    return False


def get_food_sub(command):

  food_name = extract_food_name(command)

  shelf = Shelf()
  target_food = shelf.get_food_info(food_name)

  if not target_food:
    return []

  target_taxon = target_food[2]
  all_foods = list(shelf.feats.items())

  results = []
  for food in all_foods:
    _, info = food
    food_taxon = info['taxon']

    if target_taxon == food_taxon:
      results.append(info['en'])

  return results