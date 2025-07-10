print("Exercise-8.4")

def test_input():
    flag = True
    while flag:
        user_input = input("Keep entering integers. (Type q to quit):")
        if user_input == 'q':
            break
        try:
            display_input = int(user_input)
        except Exception as e:
            print(f"Invalid input: {e}")
        else:
            print(f"Correct. You entered:{display_input}")
    # This statement is placed outside the while loop
    print("End of the exercise.")
if __name__=="__main__":
    test_input()
