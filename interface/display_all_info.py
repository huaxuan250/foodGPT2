def handle_all_steps(command):
  command = command.lower()
  intentions = ["show", "display", "see"]
  if "step" in command and "all" in command:
    for intention in intentions:
      if intention in command:
        return True
  return False
  
def handle_all_ingredients(command):
  command = command.lower()
  intentions = ["show", "display", "see"]
  if "ingredient" in command and "all" in command:
    for intention in intentions:
      if intention in command:
        return True
  return False