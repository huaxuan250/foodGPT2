from scrapping.recipe_scraper import *
from scrapping.step_extraction import *
from scrapping.information_acquisition import *
from interface.display_all_info import *
from interface.navigation import *
from interface.general_query import *
from interface.specific_query import *
from interface.substitute_query import *
from transformation.universal import to_new_steps, display_transformations
from transformation.vegie_transform import if_meat_transform, if_vegie_transform, to_vegie_ingredients, to_meat_ingredients
from transformation.healthy_transform import if_healthy_transform, if_unhealthy_transform, to_healthy_ingredients, to_unhealthy_ingredients, all_unhealthy_methods, all_healthy_methods
from transformation.american_transform import if_american_transform, to_american_ingredients
from transformation.scale_transform import *

def construct_recipe(url):
  soup = get_soup(url)
  raw_ingredients = get_ingredients(soup)
  raw_steps = get_instructions(soup)
  
  steps = subdivide_instructions(raw_steps)

  return steps, raw_ingredients

def accept_url():
  while True:
    url = input("Please input a url from AllRecipes.com: \n")
    split_url = url.split("/")
    if split_url[2] != 'www.allrecipes.com':
      print("Please provide a recipe from AllRecipes.com\n")
    else:
      return url

def user_interaction():
  # Interface happens here
  url = accept_url()
  ori_steps, ori_items = construct_recipe(url)
  curr_steps = ori_steps
  curr_items = ori_items

  curr_idx = 0
  while True:
    command = input("\nWhat would you like to do or know about?:\n")

    # Show all steps
    if handle_all_steps(command):
      for idx, step in enumerate(curr_steps):
        print("Step " + str(idx) + ":", step, '\n')

    # Show all ingredients
    elif handle_all_ingredients(command):
      for ingredient in curr_items:
        print(ingredient, '\n')

    # Naigation Module, curr_idx is modified here
    elif if_navigate(command):
      curr_idx = jump_navigate(command, curr_idx)
      if curr_idx < 0:
        curr_idx = 0
        print("This is the first step\n")
      elif curr_idx >= len(curr_steps):
        curr_idx == len(curr_steps) - 1
        print("This is the last step\n")
      else:
        print("Current step: ", curr_steps[curr_idx],'\n')
    
    # Checking if this is a general question
    elif if_general_question(command):
      answer = answer_general_question(command, curr_steps[curr_idx])
      print(answer, '\n')
    
    # Checking if this is a specific question
    elif if_specific_question(command):
      answer = answer_specific_question(command, curr_steps[curr_idx], curr_items)
      print(answer, '\n')
    
    # Checking if this is about substitution
    elif if_sub_food(command):
      answer = get_food_sub(command)
      print(answer, '\n')
    
    # Checking if this is about vegie transformation
    elif if_vegie_transform(command):
      vegie_igds, vegie_replacements = to_vegie_ingredients(ori_items)

      display_transformations(vegie_replacements)

      curr_items = vegie_igds
      vegie_steps = to_new_steps(ori_steps, vegie_replacements)
      curr_steps = vegie_steps
    
    elif if_meat_transform(command):
      meat_igds, meat_replacements = to_meat_ingredients(ori_items)

      display_transformations(meat_replacements)

      curr_items = meat_igds
      meat_steps = to_new_steps(ori_steps, meat_replacements)
      curr_steps = meat_steps
    
    # Checking if this is about healthy transformation
    elif if_healthy_transform(command):
      healthy_igds, healthy_replacements = to_healthy_ingredients(ori_items)
      healthy_replacements.extend(all_healthy_methods())

      display_transformations(healthy_replacements)

      curr_items = healthy_igds
      healthy_steps = to_new_steps(ori_steps, healthy_replacements)
      curr_steps = healthy_steps
    
    elif if_unhealthy_transform(command):
      unhealthy_igds, unhealthy_replacements = to_unhealthy_ingredients(ori_items)
      unhealthy_replacements.extend(all_unhealthy_methods())

      display_transformations(unhealthy_replacements)

      curr_items = unhealthy_igds
      unhealthy_steps = to_new_steps(ori_steps, unhealthy_replacements)
      curr_steps = unhealthy_steps
    
    # Checking if the user want to feel the AMERICAN patriotism
    elif if_american_transform(command):
      usa_igds, usa_replacements = to_american_ingredients(ori_items)
      usa_replacements.extend(all_unhealthy_methods())

      print("AMERICA! FUCK YEAH!")
      display_transformations(usa_replacements)

      curr_items = usa_igds
      usa_steps = to_new_steps(ori_steps, usa_replacements)
      curr_steps = usa_steps
    
    # Check if the user want to scale the ingredients
    elif if_mag(command):
      mult = handle_mag(command)
      scaled_igds = mult_ingredients(curr_items, mult)
      curr_items = scaled_igds
    

