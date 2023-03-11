import nltk
from pyfood.utils import Shelf
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

ACTIONS = {
        'whip': ['whip'],
        'broil': ['broil'],
        'cut': ['cut'],
        'chop': ['chop'],
        'stir fry': ['stir-fry', 'stir fry', 'stir fried', 'stir-fried'],
        'saute': ['saute', 'sauté'],
        'braise': ['braise', 'braising'],
        'sear' : ['sear'],
        'grill' : ['grill'],
        'roast': ['roast'],
        'simmer': ['simmer', 'simmered'],
        'poach': ['poach', 'poached'],
        'boil': ['boil', 'boiled'],
        'bake': ['bake', 'baking'],
        'deep fry': ['deep-fry', 'deep fry', 'deep fried', 'deep-fried'],
        'stew': ['stew'],
        'steam': ['steam'],
        'broil': ['broil'],
        'blanch': ['blanch'],
        'slice': ['slice'],
        'shred': ['shred'],
        'dice': ['dice'],
        'divide': ['divide'],
        'mince': ['mince'],
        'crush': ['crush'],
        'blend': ['blend'],
        'squeeze': ['squeeze'],
        'peel': ['peel'],
        'stir': ['stir'],
        'mix': ['mix'],
        'whisk': ['whisk'],
        'drain': ['drain'],
        'strain': ['strain'],
        'marinate': ['marinate'],
        'brush': ['brush'],
        'freeze': ['freeze'],
        'cool': ['cool'],
        'caramelize': ['caramelize'],
        'preheat': ['preheat', 'pre-heat', 'pre heat'],
        'sous vide': ['sous vide', 'sous-vide'],
        'shallow fry': ['shallow-fry', 'shallow fry', 'shallow fried', 'shallow-fried'],
        'fry': ['fry', 'fried']
}

TOOLS = ['air fryer',
 'apron',
 'bachelor griller',
 'baking dish',
 'baking tray',
 'barbecue grill',
 'beehive oven',
 'bin',
 'blender',
 'bottle',
 'bottle opener',
 'bowl',
 'brasero (heater)',
 'brazier',
 'bread basket',
 'bread machine',
 'breadbox',
 'burjiko',
 'butane torch',
 'butter dish',
 'butter knife',
 'cake pan',
 'cake slicer',
 'can opener',
 'casserole dish',
 'chapati maker',
 'cheesemelter',
 'chocolatera',
 'chopping board',
 'chopsticks',
 'chorkor oven',
 'cleaver',
 'clome oven',
 'coffee press',
 'colander',
 'comal (cookware)',
 'combi steamer',
 'communal oven',
 'convection microwave',
 'convection oven',
 'cooker',
 'cookie sheet'
 'cookware',
 'cooling rack',
 'corkscrew',
 'corn roaster',
 'crepe maker',
 'cup',
 'cup (mug)',
 'cutlery',
 'cutting board',
 'deep fryer',
 'deep-fryer'
 'dinnerware',
 'dish rack',
 'dishwasher',
 'earth oven',
 'egg slicer',
 'eggbeater',
 'electric cooker',
 'electric mixer',
 'energy regulator',
 'espresso machine',
 'field kitchen',
 'fire pot',
 'flattop grill',
 'food steamer',
 'fork',
 'frying pan',
 'frying pan (stainless steel or nonstick)',
 'fufu machine',
 'funnel',
 'garlic crusher',
 'garlic press',
 'gas stove',
 'glass',
 'glassware',
 'grater',
 'griddle',
 'grill pan',
 'halogen oven',
 'haybox',
 'hibachi',
 'horno',
 'hot box (appliance)',
 'hot plate',
 'hot pot',
 'instant pot',
 'jar',
 'jug',
 'juicer',
 'kamado',
 'kettle',
 'kitchen shears',
 'kitchen paper',
 'kitchen scissors',
 'kitchen towel',
 'kitchener range',
 'knife',
 'knives',
 'kujiejun',
 'kyoto box',
 'ladle',
 'lemon squeezer',
 'makiyakinabe',
 'mandolin',
 'masonry oven',
 'matchbox',
 'measuring cup',
 'measuring cups and spoons',
 'measuring spoon',
 'measuring spoons',
 'meat mallet',
 'meat slicer',
 'mesh skimmer',
 'mess kit',
 'microwave oven',
 'mixer',
 'mixing bowl',
 'mixing bowls',
 'mortar',
 'muffin tin',
 'multicooker',
 'napkin',
 'oven',
 'oven gloves',
 'pan',
 'pancake machine',
 'panini sandwich grill',
 'paring knife',
 'pasta server',
 'peeler',
 'pepper mill',
 'peppermill',
 'perforated spoon',
 'pestle',
 'pie dish',
 'pie plate',
 'pitcher (or jug)',
 'pizza cutter',
 'pizza stone',
 'plate',
 'plates',
 'popcorn maker',
 'potato masher',
 'potato peeler',
 'potato ricer',
 'pressure cooker',
 'pressure fryer',
 'reflector oven',
 'refrigerator',
 'regular spoon',
 'remoska',
 'rice cooker',
 'rice polisher',
 'roasting jack',
 'rocket mass heater',
 'rolling pin',
 'rotimatic',
 'rotisserie',
 'russian oven',
 'sabbath mode',
 'salad spinner',
 'salamander broiler',
 'samovar',
 'sandwich toaster',
 'saucepan',
 'scissors',
 'self-cleaning oven',
 'serving bowl',
 'serving fork',
 'serving spoon',
 'sheet pan',
 'shichirin',
 'sieve',
 'skillet',
 'slotted spoon',
 'slow cooker',
 'solar cooker',
 'soup spoon',
 'sous-vide cooker',
 'soy milk maker',
 'spatula',
 'spice box',
 'spice container',
 'spiral vegetable slicer',
 'spoon',
 'steak hammer',
 'steak knife',
 'steamers',
 'stock pot',
 'stove',
 'strainer',
 'susceptor',
 'tabun oven',
 'tandoor',
 'tangia',
 'teapot',
 'teaspoon',
 'thermal immersion circulator',
 'thermos',
 'timer',
 'toaster',
 'toaster and toaster ovens',
 'tomato slicer',
 'tongs',
 'tray',
 'tureen (or bowl)',
 'turkey fryer',
 'vacuum fryer[1]',
 'waffle iron',
 'washbasin',
 'wet grinder',
 'whisk',
 'wok',
 'wood-fired oven',
 'wooden spoon']

def extract_actions(step):
  action_results = []

  first_action = step.split(" ")[0].lower()
  action_results.append(first_action)
  
  for action in ACTIONS.keys():
    for variation in ACTIONS[action]:
      if variation in step.lower():
        action_results.append(action)

  # 3rd Case: then/and followed by a verb
  # Ignore it for now bruh
  
  return list(set(action_results))

def extract_tools(step):
  step_tools = []
  words = nltk.tokenize.wordpunct_tokenize(step.lower())
  for word in words:
    if word in TOOLS:
      step_tools.append(word)

  steps_tools = list(set(step_tools))

  return steps_tools

def extract_time(step):
  words = nltk.tokenize.wordpunct_tokenize(step.lower())

  unit = ''
  unit_loc = 0
  for idx, word in enumerate(words):
    if 'hour' in word:
      unit = 'hour'
      unit_loc = idx
    elif 'minute' in word:
      unit = 'minute'
      unit_loc = idx
    elif 'second' in word:
      unit = 'second'
      unit_loc = idx
  
  time = ''
  time_loc = 0
  if unit:
    time_loc = unit_loc - 1
    if words[time_loc].isdigit():
      time = words[time_loc]
      if int(time) > 1:
        unit = unit + 's'
  
  if time and unit:
    return " ".join([time, unit])
  else:
    return []

def extract_temp(step):
  words = nltk.tokenize.wordpunct_tokenize(step.lower())

  degree_idx = 0
  for idx, word in enumerate(words):
    if "degree" in word:
      degree_idx = idx
      break
  
  answer = []
  if degree_idx != 0:
    answer.append(words[degree_idx-1])
    answer.append(words[degree_idx])
    answer.append(words[degree_idx+1])
  
  return " ".join(answer)

def extract_food_name(command):
  shelf = Shelf()
  results = shelf.process_ingredients([command])
  if results['ingredients']:
    return results['ingredients'][0]['foodname']
  elif results['HS']:
    return results['HS'][0]
  else:
    return None