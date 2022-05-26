

def importData():
    with open('data.csv', 'r') as record:
        for lines in record:
            print(lines)
