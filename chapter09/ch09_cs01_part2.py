import pickle

def verify_user(user):
    print("Verifying the user...")
    with open("registered_users.pickle","rb") as f:
        users=pickle.load(f)

    if user in users:
        print(f"Welcome {user}! You are a verified user.")
    else:
        print(f"Sorry. You are not a registered user.")

def main():
    current_user=input("Enter the user ID: ")
    verify_user(current_user)

if __name__ == "__main__":
   main()
