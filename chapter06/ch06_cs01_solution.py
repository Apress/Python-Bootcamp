flag = ""
long_names=[]
while flag != 'quit':
    user_input = input("Enter a name (type quit to end): ")
    if user_input =='quit':
        flag = 'quit'
        break
    elif len(user_input) > 3:
        long_names.append(user_input)
print(f"The names with at least four characters: {long_names}")
