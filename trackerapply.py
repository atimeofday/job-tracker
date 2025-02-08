
from datetime import datetime

# ----------------------------------------------------------------------------------------------------------------

def apply(sourceOptions, typeOptions,applyOptions='is', companyName='None', *args):
    
    optionsList = list(applyOptions)
    companyName = companyName + " " + " ".join([*args])
    # source = None  # Initialize source and type variables
    # type = None
    if len(optionsList) != 2 or companyName=='None':
        print('Incorrect application details')
        return
    
    for option in optionsList:
        if option in sourceOptions:
            source = sourceOptions[option]
        elif option in typeOptions:
            type = typeOptions[option]
        else:
            print('Application options not found')
            return
       
    newCSVLine = datetime.today().strftime('%m-%d-%y') + "," + source + "," + type + "," + companyName + "\n"
    print(newCSVLine)
    # 02-06-25,Indeed,Short,CompanyA
    with open('jobtracker.csv', 'a') as file:
        file.write(newCSVLine)