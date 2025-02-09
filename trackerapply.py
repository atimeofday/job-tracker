
from datetime import datetime

# ----------------------------------------------------------------------------------------------------------------

def apply(sourceTypeOptions, applyOptions='is', companyName='None', *args):

    optionsList = list(applyOptions)
    companyName = companyName + " " + " ".join([*args])

    if len(optionsList) != 2 or companyName=='None':
        print('Incorrect application details')
        return
    
    for option in optionsList:
        if option in sourceTypeOptions.sourceOptions:
            source = sourceTypeOptions.sourceOptions[option]
        elif option in sourceTypeOptions.typeOptions:
            type = sourceTypeOptions.typeOptions[option]
        else:
            print('Application options not found')
            return
       
    newCSVLine = datetime.today().strftime('%m-%d-%y') + "," + source + "," + type + "," + companyName + "\n"
    print(newCSVLine)
    # 02-06-25,Indeed,Short,CompanyA
    with open('jobtracker.csv', 'a') as file:
        file.write(newCSVLine)