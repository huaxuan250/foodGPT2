from scrapping.step_extraction import extract_food_name, extract_tools, extract_temp, extract_time

def if_specific_question(command):
  command = command.lower()
  intentions = ["how much", "temperature","how long",'when', 'what tools']
  for intention in intentions:
    if intention in command:
      return True
  return False

def answer_specific_question(command, step, ingredients):
  command = command.lower()

  if 'how much' in command:
    # Find the best match ingredient
    target_food = extract_food_name(command)
    if target_food:
      for igd in ingredients:
        if target_food in igd:
          return igd
    return "No available food information on that food."
  elif 'tool' in command:
    target_tools = extract_tools(step)
    return target_tools
  elif 'temperature' in command:
    target_temp = extract_temp(step)
    if target_temp:
      return target_temp
    else:
      return 'No available information on temperature.'
  elif 'how long do i' in command or 'when' in command:
    target_time = extract_time(step)
    if target_time:
      return target_time
    else:
      return 'No available information on time.'
  
  return 'Cannot understand your command'