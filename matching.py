import csv

def matching(IP_address):
    # debug for correct index
    with open('inputDataForTraining.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for index, row in enumerate(reader):
            if row[0] == IP_address:
                return index
    return False
