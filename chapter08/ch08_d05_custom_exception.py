# The following example uses a custom exception
class GreaterThan100Error(Exception):
    """ This is a custom exception."""
    pass

def test_custom_exception():
    try:
        usr_input = float(input("Enter a number below 100: "))
        if usr_input >= 100:
            raise GreaterThan100Error(f"The input {usr_input} is NOT less than 100.")
    except GreaterThan100Error as e:
        print(f"The custom exception is raised: {e}")
    except ValueError as e:
        print(f"Error Details: {e}")
    else:
        print(f"Well done. You have entered: {usr_input}")

if __name__=="__main__":
    test_custom_exception()
