user_input=input("Enter an HTTP error code (400,404 or 408): ")
# Converting it to an int( Skipping the validation of the user's input)
value=int(user_input)
msg="n/a"
match value:
    case 400:
        msg=msg.replace("n/a","bad request")
    case 404:
        msg= msg.replace("n/a","not found")
    case 408:
        msg= msg.replace("n/a","request timeout")
    # case _:
    #     msg= msg.replace(  "n/a","unknown")
print(f"The code {value} represents the '{msg}' error.")
