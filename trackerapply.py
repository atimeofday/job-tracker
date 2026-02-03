
from datetime import datetime

# ----------------------------------------------------------------------------------------------------------------

def apply(optionSets, applyOptions='', companyName='', *args):

    sourceOptions = optionSets.sourceOptions
    typeOptions = optionSets.typeOptions

    optionsList = list(applyOptions)
    if [*args]:
        companyName = companyName + " " + " ".join([*args]).strip()

    if companyName=='' or len(optionsList) != 2:
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
    with open('applications.csv', 'a') as file:
        file.write(newCSVLine)
