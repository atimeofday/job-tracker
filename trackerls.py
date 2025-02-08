
import pandas
from datetime import datetime

# ----------------------------------------------------------------------------------------------------------------  

# Lists job applications filtered by source, type, and/or date.
def ls(sourceOptions, typeOptions, listOption='default'):

    # Check if listOption is a valid source or type and set listOption to the corresponding dict value
    if listOption in sourceOptions:
        source = sourceOptions[listOption]
        listOption = 'Source'
    elif listOption in typeOptions:
        type = typeOptions[listOption]
        listOption = 'Type'
    
    # Read file into Pandas DataFrame
    csvFile = pandas.read_csv('./jobtracker.csv')
    csvFile['Date'] = pandas.to_datetime(csvFile['Date'], format="%m-%d-%y")
    
    match listOption:
        
        # Filter CSV line entries by current month
        case 'default' | 'month' | 'm':
            filteredCSV = csvFile[(csvFile['Date'].dt.month == datetime.today().month)]
        
        # Filter CSV line entries by current week   
        case 'week' | 'w':
            filteredCSV = csvFile[(csvFile['Date'].dt.isocalendar().week == datetime.today().isocalendar().week)]
        
        # List all CSV line entries
        case 'all' | 'a':
            filteredCSV = csvFile
        
        # Filter CSV line entries by source
        case 'Source':
            filteredCSV = csvFile[(csvFile['Source'] == source)]
        
        # Filter CSV line entries by type
        case 'Type':
            filteredCSV = csvFile[(csvFile['Type'] == type)]
        
        # List all available filter options
        case 'options' | 'o' | 'h':
            print("Available source options:")
            for key, value in sourceOptions.items():
                print(f"  {key}: {value}")
            print("\nAvailable type options:")
            for key, value in typeOptions.items():
                print(f"  {key}: {value}")
            return

    # Print filtered table of job applications
    if filteredCSV.empty:
        print(f'No job applications found with the given filter')
    else:
        print(filteredCSV)