import pandas as pd

squirrel_data = pd.read_csv('Intermediate/Day_025/2018_central_park_squirrel_census.csv')
print(squirrel_data)

# # Count the number of squirrels with each primary fur color
# gray_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
# cinnamon_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
# black_squirrel_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])

# # make a dictionary to store the data
# squirrel_dic = {
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "No": [gray_squirrels_count, cinnamon_squirrels_count, black_squirrel_count]
# }

# # convert the dictionary to a panda dataframe
# squirrel_dataframe = pd.DataFrame(squirrel_dic)

# Get the count of each fur color
squirrel_data['Primary Fur Color'].value_counts()
squirrel_data['Primary Fur Color'].value_counts().to_csv('Intermediate/Day_025/squirrel_count.csv')