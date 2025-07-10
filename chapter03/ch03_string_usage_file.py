
# I want to print a character, say hash(#) 10 times.
print("#"*10)

# I want to use control codes like \t and \n within a string.
print("How\tare\tyou?")
print("Hello\nWorld!")

print("-"*10)

# I want to print HelloWorld! inside single quotations.
print(" 'Hello World!' ")

print("-"*10)

# Inserting a new line between strings
print("Hello\nWorld!")

print("-"*10)
# The following line prints Abd, but in IDLE the output is different.
print("Abc\bd")
print("-"*10)

# I want to print the word KFC inside single quotations.
print("'KFC'")

print("-"*10)

# I want to print the word HelloWorld! inside double-quotations.
print(" \"Hello World!\"")
# The alternative code to print HelloWorld! inside double-quotations
print(' "Hello World!" ')
# The following syntax is not correct
#print(""HelloWorld"") # Error
print("-"*10)


# I want to print the sentence "The baseball is my favorite game"
# using a string variable.
fav_game = "Baseball is my favorite game"
print(fav_game)

print("-"*10)

# I want to concatenate multiple strings following different approaches.
text1= "Python"
text2 = "programming language."
print(text1+" is a "+text2) # Using + to concatenate
print(text1,"is a",text2) # Using comma to concatenate
print("{} is a {}".format(text1, text2)) # Using a built-in method
print(f"{text1} is a {text2}") # Using f-strings
print("-"*10)

# I want to print the word Cricket in uppercase and lowercase.
game = "Cricket"
print("The original string is:" + game)
# Printing in uppercase
print(game.upper())
# Printing text1 in lowercase
print(game.lower())

print("-"*10)
# I want to use multiple functions together
hello_text = " Hello, Reader!"
print(f"The original string is:{hello_text}")
print(hello_text.upper().islower()) # False
print(hello_text.upper().isupper()) # True

print("-"*10)

# I want to calculate the length of a string
text = "Python"
print(f" The length of the string {text} is {len(text)}")

print("-"*10)

# I want to examine the index positions of the characters inside a string.
fruit = "Mango"
print(f"The fruit name is: {fruit}")
# Printing individual characters inside the string
print(f"Index 0 contains: {fruit[0]}")
print(f"Index 1 contains: {fruit[1]}")
print(f"Index 2 contains: {fruit[2]}")
print(f"Index 3 contains: {fruit[3]}")
print(f"Index 4 contains: {fruit[4]}")
print("-"*10)

# I want to get the first occurrence of a character (or, a word) inside a string.
text = "abcABc"
print(f"The text is: {text}")
# Printing individual characters inside the string
print(f"The first occurrence of 'A' is at index: {text.index("A")}")
print(f"The first occurrence of 'c' is at index: {text.index("c")}")
print(f"The first occurrence of 'bcA' is at index: {text.index("bcA")}")

# print(text.index("z")) # This line will cause error
print("-"*10)
# I want to examine a function that accepts multiple
# parameters. I'm using the replace function in this example.
text = " Hello, John!"
print(f"The initial text is:{text}")
print("Replacing the name 'John' with 'Bob' now.")
text = text.replace("John", "Bob")
print(f"The changed text is:{text}")

print("-"*10)





