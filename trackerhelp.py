
from inspect import isfunction

# ----------------------------------------------------------------------------------------------------------------

# Provides user assistance with job tracker functions
def trackerHelp(dispatcher, dynamicArgs, function='default'):
    match function:
        case 'default':
            print('Available functions: ')
            for key, value in dispatcher.items():
                print(f'{key}:\t{value.__name__ if isfunction(value) else value}')
            print('\nAvailable action synonyms as first or second word:')
            for key, value in dynamicArgs.items():
                print(f'{key}:\t{value}')
            print('\nUse "help [function]" for more detailed information')
            
        case 'ls':
            print('Lists job applications filtered by source, type, and/or date, and their total.')
            
        case 'apply':
            print('Adds a job application to the tracker.')
            
        case 'help':
            print('Displays this help message.')
            
        case _:
            print('Invalid function.')