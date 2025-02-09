
import pandas
from datetime import datetime

# ----------------------------------------------------------------------------------------------------------------  

# Lists job applications filtered by source, type, and/or date.
def ls(sourceTypeOptions,listOption='default'):

    # Print available source and type options and returns immediately if 'options' is specified
    if listOption in ('options', 'o', 'h'):
        print('Available source options:')
        for key, value in sourceTypeOptions.sourceOptions.items():
            print(f"  {key}: {value}")
        print('\nAvailable type options:')
        for key, value in sourceTypeOptions.typeOptions.items():
            print(f"  {key}: {value}")
        return

    # Check if listOption is a valid source or type and set listOption to the corresponding dict value
    if listOption in sourceTypeOptions.sourceOptions:
        source = sourceTypeOptions.sourceOptions[listOption]
        listOption = 'Source'
    elif listOption in sourceTypeOptions.typeOptions:
        type = sourceTypeOptions.typeOptions[listOption]
        listOption = 'Type'
    
    # Read file into Pandas DataFrame
    csvFile = pandas.read_csv('./jobtracker.csv')
    csvFile['Date'] = pandas.to_datetime(csvFile['Date'], format="%m-%d-%y")
    filteredCSV = pandas.DataFrame()

    # Define filter functions
    filters = {
        'month':    lambda df: df[df['Date'].dt.month == datetime.today().month],
        'week':     lambda df: df[df['Date'].dt.isocalendar().week == datetime.today().isocalendar().week],
        'day':      lambda df: df[df['Date'].dt.date == datetime.today().date()],
        'all':      lambda df: df,
        'Source':   lambda df: df[df['Source'] == source],
        'Type':     lambda df: df[df['Type'] == type]
    }
    
    # Add aliases
    filters.update({
        'default': filters['month'],
        'm': filters['month'],
        'w': filters['week'],
        'd': filters['day'],
        'a': filters['all']
    })
    
    # Apply the filter
    filteredCSV = filters.get(listOption, lambda df: pandas.DataFrame())(csvFile)

    # Print filtered table of job applications
    if filteredCSV.empty:
        print(f'No job applications found with the given filter')
    else:
        print(filteredCSV)
        print(f'Total: {len(filteredCSV)}')