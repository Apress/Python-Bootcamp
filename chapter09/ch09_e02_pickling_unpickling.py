import pickle
import random

# pickle_file="e:\\TestData\\numbers.pickle"
pickle_file="numbers.pickle"
numbers=[]
for i in range(1,11):
    number=random.randint(1,500)
    numbers.append(number)
print("The random numbers are:")
print(numbers)
# Dumping/storing the numbers in binary format
with open(pickle_file,"wb") as file:
       pickle.dump(numbers,file)

# Retrieving the data from the pickle file
with open(pickle_file, "rb") as file:
    content=pickle.load(file)
    print("The retrieved numbers are:")
    print(content)