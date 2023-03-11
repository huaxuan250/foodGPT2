from scrapping.recipe_scraper import *
from scrapping.step_extraction import *
from scrapping.information_acquisition import *
from interface.display_all_info import *
from interface.navigation import *
from interface.general_query import *
from interface.specific_query import *
from interface.substitute_query import *

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
  steps, items = construct_recipe(url)

  curr_idx = 0
  while True:
    command = input("What would you like to do or know about?:\n")

    # Show all steps
    if handle_all_steps(command):
      for idx, step in enumerate(steps):
        print("Step " + str(idx) + ":", step, '\n')

    # Show all ingredients
    elif handle_all_ingredients(command):
      for ingredient in items:
        print(ingredient, '\n')

    # Naigation Module, curr_idx is modified here
    elif if_navigate(command):
      curr_idx = jump_navigate(command, curr_idx)
      if curr_idx < 0:
        curr_idx = 0
        print("This is the first step\n")
      elif curr_idx >= len(steps):
        curr_idx == len(steps) - 1
        print("This is the last step\n")
      else:
        print("Current step: ", steps[curr_idx],'\n')
    
    # Checking if this is a general question
    elif if_general_question(command):
      answer = answer_general_question(command, steps[curr_idx])
      print(answer, '\n')
    
    # Checking if this is a specific question
    elif if_specific_question(command):
      answer = answer_specific_question(command, steps[curr_idx], items)
      print(answer, '\n')
    
    # Checking if this is about substitution
    elif if_sub_food(command):
      answer = get_food_sub(command)
      print(answer, '\n')