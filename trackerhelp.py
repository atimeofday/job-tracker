
from inspect import isfunction

# ----------------------------------------------------------------------------------------------------------------

# Provides user assistance with job tracker functions
def trackerHelp(modules, aliases, sourceOptions, typeOptions, selection='default'):

    if selection in aliases:
        selection = aliases[selection]

    match selection:

        case 'default' | 'all' | 'a':
            print('Available modules: ')
            for key, value in modules.items():
                print(f'{key}')
            print('\nUse "help aliases" for more ways to select modules')
            print('Use "help [module]" for more detailed information')

        case 'aliases':
            print('Available aliases: ')
            for key, value in aliases.items():
                print(f'{key}:\t{value}')
            
        case 'ls':
            print('Lists job applications filtered by source, type, and/or date, and their total.')
            print('Available source options: ')
            for key, value in sourceOptions.items():
                print(f'{key}:\t{value}')
            print('\nAvailable type options: ')
            for key, value in typeOptions.items():
                print(f'{key}:\t{value}')
            
        case 'apply':
            print('Adds a job application to the tracker.')
            
        case 'help':
            print('Displays this help message.')

        case 'exit':
            print('Exits the job tracker.')
            
        case _:
            print('Invalid selection.')
