import pandas as pd
import csv

def user():
    previousCommand = " "
    address = input("Please enter your IP address\n")
    if is_ip_in(address):
        #get info from csv
        print("ip is in list")
    else:
        #ask user for info
        print("ip is not in list")

    while (1):
        print("\nPlease choose a function")
        command = input("View ad | Stay | Go back | Help\n")
        if (command == 'View ad'):
            #ad
            print("showing ad")
            previousCommand = "v"
        elif (command == 'Stay'):
            #stay
            print("staying")
            previousCommand = "s"
        elif (command == 'Go back'):
            #go back
            if (previousCommand == "v"):
                changeScore(address, -0.10)
            elif (previousCommand == "s"):
                changeScore(address, 0.10)
            print("going back")
            previousCommand = "b"
        elif (command == 'Help'):
            #help
            print("Command list: \nView ad: type 'view ad' to see an ad \nStay: type 'stay' to stay on the ad page \nGo back: type 'go back' to go back")

def is_ip_in(ip):
    with open('inputDataForTraining.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        return any(ip == row[0] for row in reader)
        
def changeScore(ip, value: float):
    counter = 0
    df = pd.read_csv("outputModelWithPredictions.csv")
    with open('outputModelWithPredictions.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if (ip == row[0]):
                break
            counter = counter + 1
    df.iloc[counter, 4] = df.iloc[counter, 4] + value
    df.to_csv("outputModelWithPredictions.csv", index=False)
    

if __name__ == "__main__":
    user()