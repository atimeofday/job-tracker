
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

    modules = {
        'help':     trackerHelp,
        'apply':    apply,
        'ls':       ls,
    }

    # Handles synonyms of functions and most function calling
    aliases = {
        'help':     'help',
        'h':        'help',
        'exit':     'exit',
        'e':        'exit',
        'apply':    'apply',
        'app':      'apply',
        'a':        'apply',
        'list':     'ls',
        'ls':       'ls'
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
    
    optionSets = collectedOptions(sourceOptions, typeOptions)
    optionsList = sourceOptions | typeOptions

    inputString = 'init'
    # Input variable and main loop
    while inputString != 'exit':

        # Initialize default function call parameters
        alias = 'help'
        option = 'default'

        # Prompts user for input and splits input string into arguments for processing
        inputString = input('\nInput: ')
        inputSet = inputString.split()
        
        # Clears screen to maintain readability and consistent user experience
        os.system('cls||clear')
        print(f'Input: {inputString}\n')

        # Assigns variables by permutations of input argument order for grammatically comfortable input
        match inputSet:
            case [alias, option, *args] if alias in aliases: pass
            case [option, alias, *args] if alias in aliases: pass
            case [alias, *args] if alias in aliases: pass
            case []: pass
            case _:
                print('Module not found\n')
                continue

        selection = aliases[alias]
        if selection == 'exit': break

        module = modules[selection]

        match selection:
            case 'help':    module(modules, aliases, sourceOptions, typeOptions, option)
            case 'apply':   module(optionSets, option, *args)
            case 'ls':      module(optionSets, option)
            case _:         module()

# ----------------------------------------------------------------------------------------------------------------

# Interface initialization and isolated top-level for extensibility
def main():
    if not os.path.exists('applications.csv'):
        with open('applications.csv', 'a+') as file: 
            file.write('Date,Source,Type,Company\n')
    os.system('cls||clear')
    print('Initiating interface')
    interact()
main()

# ----------------------------------------------------------------------------------------------------------------
