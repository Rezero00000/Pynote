from data import getCategories
import os

os.system('cls')
#getData('data.json')

logoAscii = '''
     ___                   _        
    | _ \ _  _  _ _   ___ | |_  ___ 
    |  _/| || || ' \ / _ \|  _|/ -_)
    |_|   \_, ||_||_|\___/ \__|\___|
          |__/       
     -----------------------------
       -[ My Personal Library ]-
 '''
print(logoAscii)

def createTable (data, headers):
    # get Table Width
    table_width = [max(len(str(item)) for item in column)for column in zip(*data)]
    data_width = [len(header) for header in headers]

    maxData = []
    for i in range(3):
        tes = [table_width[i], data_width[i]]
        maxData.append(sorted(tes, reverse = True)[:1][0])
    
    #Create Header 

    header = "    +" + "+".join("-" * (width+2) for width in maxData) + "+"
    table = []

    table.append(header)
    table.append("    |" + "|".join(
        " " + header.ljust(maxData[i]) + " " for i, header in enumerate(headers)
    ) + "|")

    table.append("    |" + "|".join( 
        "-" * (maxData[i] + 2) for i, header in enumerate(headers)
    ) + "|")

    # Append row item
    for row in data:
        table.append("    |" + "|" .join(
            " " + str(value).ljust(maxData[key]) + " " for key,value in enumerate(row)
        ) + "|")

    table.append(header)
    return "\n".join(table)

header = ['No', 'Categories', 'Notes']
data = getCategories()

table = createTable(data, header)
print()
print(table)
print("    1, 2, 3 ->\n")

options = """
    [1]. Create Category
    [2]. Select Category <No> 
    [3]. Update Category <No>
    [4]. Delete Category <No>
    [5]. Search <Keyword>
"""
print(options)
action = input(str('Chose Your Action --> '))


