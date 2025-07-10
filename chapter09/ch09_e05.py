import json
import random

# The json module uses demo
json_file="numbers.json"
numbers=[]
for i in range(1,11):
    number=random.randint(1,500)
    numbers.append(number)
print("The random numbers are:")
print(numbers)
# Dumping/storing the numbers in the JSON format
with open(json_file,"w") as file:
       json.dump(numbers,file)

# Retrieving the data from the json file
with open(json_file, "r") as file:
    content=json.load(file)
    print("The retrieved numbers are:")
    print(content)

