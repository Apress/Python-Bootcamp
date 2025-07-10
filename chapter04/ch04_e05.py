value = 408
match value:
    # The correct placement
    # case 400:
    #     msg="Bad request"
    case 408:
        msg= "Request timeout"
    case _:
        msg= "Error excluding request timeout or bad request"
    # The incorrect placement
    # case 400:
    #     msg = "Bad request"
print(f"The error code {value} represents {msg}")
