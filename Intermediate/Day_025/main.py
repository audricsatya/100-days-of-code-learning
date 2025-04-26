with open('Intermediate/Day_025/weather_data.csv') as data_file:
    data_file_contents = data_file.readlines()
    print(data_file_contents)

import csv

with open('Intermediate/Day_025/weather_data.csv') as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != 'temp':
            temperatures.append(int(row[1]))
    print(temperatures)

import pandas as pd

data = pd.read_csv('Intermediate/Day_025/weather_data.csv')
print(data)
print(data['temp'])

print(data['temp'].mean())
print(data['temp'].max())
print(data['condition'])
print(data['day'])

data['temp'].to_list()

# Get data in row
print(data[data.day == 'Monday'])
print(data[data.temp == data.temp.max()])
print(data[data.temp == data.temp.max()]['condition'])

data_dict = {
    "students": ["Angela", "James", "Lily"],
    "scores": [56, 76, 98]
}

data_frame = pd.DataFrame(data_dict)
print(data_frame)

data_frame.to_csv('Intermediate/Day_025/new_data.csv')