from ingredient_parser import parse_ingredient
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def get_ingredients(soup):
  html_items = soup.find_all("li","mntl-structured-ingredients__list-item")
  ingredients = []

  for item in html_items:
    text = item.text[1:-1]
    ingredients.append(text)

  return ingredients

def get_food_info(igd):
  info = parse_ingredient(igd)
  quant = info['quantity']
  unit = info['unit']
  name = info['name']
  combo = [quant, unit, name]
  return combo

def get_instructions(soup):
  instructions_steps = soup.find_all("li", {"class": 'comp mntl-sc-block-group--LI mntl-sc-block mntl-sc-block-startgroup'})
  instructions = []

  for instruction in instructions_steps:
    text = instruction.find('p').text
    text = text[1:-1]
    instructions.append(text)
  
  return instructions

def subdivide_instructions(instructions):
  steps = []
  for instruction in instructions:
    sub_instructions = nltk.tokenize.sent_tokenize(instruction)
    for sub in sub_instructions:
      steps.append(sub)
  return steps