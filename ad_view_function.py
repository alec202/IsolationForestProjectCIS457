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
        location = input("Enter your country location\n").upper()
        vpn = input("Enter y/n if you have a VPN\n").lower()
        if vpn == 'y':
            vpn = 1
        else:
            vpn = 0
        num_clicks = 0
        df = pd.read_csv("inputDataForTraining.csv")
        newUserData = {
            'IP_Address': address,
            'Location': location,
            'numberOfTimesClickedAD': num_clicks,
            'Vpn': vpn
        }
        # Create new row
        new_row = pd.DataFrame([newUserData])
        # add the row to the existing data frame
        df = pd.concat([df, new_row], ignore_index=True)
        # Write to the csv file
        df.to_csv('inputDataForTraining.csv', index=False)


    while (1):
        print("\nPlease choose a command")
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