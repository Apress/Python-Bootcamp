location = "e:\\TestData\\OriginalFile.txt"

def print_lines(input_file, lines):
    """ This function prints the first ‘n’ lines from a file."""
    try:
        with open(input_file, "r") as file_object:
            count = 0
            while count < lines:
                line_content = file_object.readline()
                print(line_content,end='')
                count += 1
    except FileNotFoundError as ex:
        print(f"The file {input_file} is not found.")
        print(f"Error details:{ex}")

try:
    user_input = input('Enter how many lines you want to print from the file? ')
    number_of_lines = int(user_input)
    print_lines(location,number_of_lines)
except ValueError as e:
    print("Invalid input! Provide the correct input next time!")
    print(f"Error details:{e}")
except Exception as e:
    print("An unknown error occurred.")
    print(f"Error details:{e}")