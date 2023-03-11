import re

def replace_original(sentence, replacement):
  original, new = replacement
  regex = r'\b{}\b'.format(original)
  new_senti = re.sub(regex, new, sentence)
  return new_senti

def to_new_steps(steps, replacements):
  new_steps = []
  for step in steps:
    step = step.lower()
    new_step = step
    for ori, sub in replacements:
      if ori in step:
        new_step = replace_original(new_step,(ori,sub))

    if new_step != step:
      new_steps.append(new_step)
    else:
      new_steps.append(step)

  return new_steps

def display_transformations(replacements):
  replacements = list(set(replacements))
  for pair in replacements:
    ori, sub = pair
    print("Replacing {} with {}".format(ori, sub))