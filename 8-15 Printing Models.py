# This is the module print_functions.py
def print_models(unprinted_designs, completed_models):
   while unprinted_designs:
       current_design = unprinted_designs.pop()
       print(f"Printing models: {current_design}")
       completed_models.append(current_design)


def show_completed_models(completed_models):
   print("\nThe Following models have been printed:")
   for completed_model in completed_models:
       print(completed_model)
# This is the code made to call the module this is print_models.py
from print_functions import *
unprinted_designs = ['phone case', 'robot pendant', 'dodocahedron']
completed_models = []


