def main():
    location="e:\\TestData\\OriginalFile.txt"
    # location="e:\\TestData\\IncorrectFile.txt" # incorrect file name
    try:
        with open(location, "r") as file_object:
            content = file_object.read()
    except FileNotFoundError as e:
        print(f"The file is not found at {location}")
    else:
        print(content+"\n")

if __name__ == "__main__":
   main()
