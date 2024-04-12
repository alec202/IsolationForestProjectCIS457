#requirement: pip install flask
from flask import Flask, request
from werkzeug.utils import secure_filename
import webbrowser
import os
import csv
#function that simulates the company's update csv file
app = Flask(__name__)
@app.route('/upload', methods = ['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part in the request.', 400
    file = request.files['file']
    if file.filename == '':
        return 'No selected file.', 400
    if file and file.filename.endswith('.csv'):
        filename = secure_filename(file.filename)
        file.save(os.path.join(os.getcwd(), filename))

        #add the updated csv file information to training csv file
        filenamecsv = f"{file.name}.csv"
        print(file)
        print(filenamecsv)
        with open('inputDataForTraining.csv', 'a', newline= '') as file1:
            with open(filename, 'r') as file2:
                reader = csv.reader(file2)
                # next(reader)
                for row in reader:
                    file1.write('\n')
                    file1.write(','.join(row))
        #delete the uploaded file
        os.remove(filename)
        return 'File uploaded successfully.', 200
    else:
        return 'Unsupported file type.', 400
#function that stimulates the company's login system
def login(ip):
    #check if the ip is trusted
    if is_ip_in(ip):
        print('Welcome to the company!')
        webbrowser.open('file://' + os.path.realpath('update_file.html'))
        app.run(host = '0.0.0.0', port = 8080)
    else: print('Only partners are allowed to access this feature!')
#function that check the ip of the user
def is_ip_in(ip):
    with open('partner_companies_info.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        return any(ip == row[0] for row in reader)

#Test the function
if __name__ == '__main__':
    login('8.8.4.4')