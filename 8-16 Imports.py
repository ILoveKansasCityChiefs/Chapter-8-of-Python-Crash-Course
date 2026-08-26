# This module is called greeting.py
def display_message(name):
    print((f"Hey! {name.title()}. Today I am learning functions"))
# This is the different types of calls of the module greeting.py
# import module_name(importing entire module)
import greeting


greeting.display_message('jessica')
# from module_name import function_name(importing specific function from module)
from greeting import display_message


display_message('jessica')
# from module_name import function_name as fn(Giving function name an alias(nickname))
from greeting import display_message as dm


dm('jessica')
# import module_name as mn (Giving module name an alias(nickname))
import greeting as greet


greet.display_message('jessica')
# from module_name import *(importing all functions in module)
from greeting import *


display_message('jessica')
