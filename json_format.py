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


# Implementing the task
# As an input there is a description of classes in json format
# Calculate the number of inheritance for each class
# Results has to be represented in alphabetical order
# Converting input string into json format and then into list of dictionaries
# data_json = input()
# data = json.loads(dat)

# Tested data with a list of dictionaries in json format
data1 = [{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]
data = [{"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}, {"name": "A", "parents": []}, {"name": "D", "parents":["C", "F"]}, {"name": "E", "parents":["D"]}, {"name": "F", "parents":[]}]

# Creating a dictionary for storing the resulted information
d = {}

# Creating a list for sorting the future results in alphabetic order
list_of_names = []

# Going through all names and writing the all unique names of classes inside new dictionary
for i in range(len(data)):
    for x, y in data[i].items():
        if x == "name":
            if y not in d:
                d[y] = 1
                list_of_names += [y]

# Going through all parents and adding number of met names of classes into appropriate key
for i in range(len(data)):
    for x, y in data[i].items():
        if x == "parents":
            for j in range(len(y)):
                if y[j] in d:
                    d[y[j]] += 1

# Sorting list of names
sorted(list_of_names)

# Showing the result in alphabetic order
for x in list_of_names:
    print(x, ':', d[x])
