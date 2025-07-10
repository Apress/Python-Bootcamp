user_input=input("Enter the HTTP error code (such as 4xx): ")
# Converting it to an int( Skipping the validation of the user's input)
value=int(user_input)
match value:
    case 400:
        msg="Bad request"
    case 404|408:
        msg= "Not found or request timeout"
    case _:
        msg= "Errors excluding bad request, not found or request timeout"
print(f"The error code {value} is for: {msg}")
