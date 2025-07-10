try:
    raise BaseException("BaseException raised.")
except Exception as e:
    print("Caught the BaseException")
