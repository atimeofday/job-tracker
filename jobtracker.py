
import os
import pandas
from datetime import datetime
from inspect import isfunction
from collections import ChainMap

# ----------------------------------------------------------------------------------------------------------------

from trackerls import ls
from trackerapply import apply
from trackerhelp import trackerHelp

# ----------------------------------------------------------------------------------------------------------------

# Collects source and type options for passing to other functions 
class collectedOptions:
    def __init__(self, sourceOptions, typeOptions):
        self.sourceOptions = sourceOptions
        self.typeOptions = typeOptions

# Primary interface/logic loop using a dictionary of functions callable by user input
def interact():

    # Handles synonyms of functions and most function calling
    dispatcher = {
        'a':        apply,
        'app':      apply,
        'apply':    apply,
        'ls':       ls,
        'list':     ls,
        'help':     trackerHelp,
        'end':      exit
    }

    # Handles synonyms or alternative orders of input arguments
    options = {
        'delete':   'delete',
        'remove':   'delete',
        'clear':    'delete',
        'del':      'delete', 
        'create':   'create', 
        'make':     'create',
        'add':      'create',
        'new':      'create',
    }

    sourceOptions = {
        'i':    'Indeed',
        'g':    'Glassdoor',
        'w':    'Wellfound',
        'n':    'LinkedIn',
        'b':    'BuiltIn',
        'h':    'Handshake',
        'c':    'Company',
        'r':    'Referral',
    }
    
    typeOptions = {
        's':        'Short',
        'short':    'Short',
        'l':        'Long',
        'long':     'Long',
    }
    
    optionsList = collectedOptions(sourceOptions, typeOptions)
    
    # Input variable and main loop
    action = 'init'
    while action != 'end':

        # Prompts user for input and splits input string into arguments for processing
        inputString = input('\nInput action: ')
        action = inputString.split()
        function = 'help'
        option = 'default'
        
        # Clears screen to maintain readability and consistent user experience
        os.system('cls||clear')
        print(f'Input: {inputString}\n')

        # Assigns variables by permutations of input argument order for grammatically comfortable input
        match action:
            case ['end']: break
            case []: pass
            case ['help' as function]: pass 
            case ['help' as function, option] | [option, 'help' as function]: pass
            case [function, option, *args] if function in dispatcher: pass
            case [option, function, *args] if function in dispatcher: pass
            case ['ls' as function]: pass
            # Calls functions with no arguments if none are given
            case [function] if function in dispatcher:
                dispatcher[function]()
                continue
            # Provides user feedback if no function-call matches are found for a given input
            case _: 
                print('Function not found in dispatcher\n')
                continue
        
        function = dispatcher[function].__name__

        # Calls functions with dispatcher and handles special argument cases
        match function:
            # Passes additional meta-programming information to the help function
            case 'help':    dispatcher[function](dispatcher, options, option)
            case 'apply':   dispatcher[function](optionsList, option, *args)
            case 'ls':      dispatcher[function](optionsList, option)
            case _:         dispatcher[function](options.get(option, option), *args)

# ----------------------------------------------------------------------------------------------------------------

# Interface initialization and isolated top-level for extensibility
def main():
    os.system('cls||clear')
    print('Initiating interface')
    interact()
main()

# ----------------------------------------------------------------------------------------------------------------
