

def checkFile():
    with open('data.csv','r+') as file:
        if file.readlines() == []:
            data = []
            data.append('surname')
            data.append('name')
            data.append('description')       
            file.write(f'{data[0]}; {data[1]}; {data[2]}')
