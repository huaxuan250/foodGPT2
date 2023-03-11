from scrapping.step_extraction import extract_actions

def if_general_question(command):
  command = command.lower()
  intentions = ["how to", "how do i", "what is a"]
  for intention in intentions:
    if intention in command:
      return True
  return False

def answer_general_question(command, step):
  command = command.lower()
  if "that" in command:
    action = extract_actions(step)[0]
    command = "how to " + action
  
  query = command.split()
  query = "+".join(query)
  base = "https://www.google.com/search?q="
  return base+query