import re

def if_navigate(command):
  command = command.lower()
  intentions = ['next','back','previous','start','navigate','repeat', 'take']
  for intention in intentions:
    if intention in command:
      return True
  return False

def jump_navigate(command, curr):
  command = command.lower()
  if 'next' in command:
    return curr + 1
  elif 'back' in command or 'previous' in command:
    return curr - 1
  elif 'take' in command:
    matched = re.search(r'\d{1,2}(?:st|nd|rd|th)', command)
    if matched:
      order = matched.group(0)
      order = int(order[:-2])
      order = order - 1 
    return order
  else:
    return curr