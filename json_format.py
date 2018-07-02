# File: json_format.py
# Description: Examples on how to process json files in Python
# Environment: PyCharm and Anaconda environment
#
# MIT License
# Copyright (c) 2018 Valentyn N Sichkar
# github.com/sichkar-valentyn
#
# Reference to:
# [1] Valentyn N Sichkar. Examples on how to process json files in Python with help of json library // GitHub platform [Electronic resource]. URL: https://github.com/sichkar-valentyn/Processing_json_files_in_Python (date of access: XX.XX.XXXX)



# Working with files in json formats

import json

# Creating dictionaries with information about the students
student1 = {
    'first_name': 'Greg',
    'last_name': 'Dean',
    'scores': [70, 80, 90],
    'description': 'Good job, Greg',
    'certificate': True
}

student2 = {
    'first_name': 'Wirt',
    'last_name': 'Wood',
    'scores': [80, 80.2, 80],
    'description': 'Nicely Done',
    'certificate': True
}

# Creating a list with elements of dictionaries
data = [student1, student2]

# Showing the results with the help of library json
print(json.dumps(data, indent=4, sort_keys=True))

# Writing the data inside the file
with open('students.json', 'w') as f:
    json.dump(data, f, indent=4, sort_keys=True)

# Loading data from json into the Python object as list with dictionaries
data_json = json.dumps(data, indent=4, sort_keys=True)
data_again = json.loads(data_json)

# Calculating the sum of all scores for the first student
print(sum(data_again[0]["scores"]))

# Loading data from json file
with open("students.json", "r") as f:
    data_again = json.load(f)

# Calculating the sum of all scores for the second student
print(sum(data_again[1]["scores"]))
