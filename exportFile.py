


def recordData(data):
    with open('data.csv', 'a') as record:
        record.write(f'\n{data[0]}; {data[1]}; {data[2]}')
