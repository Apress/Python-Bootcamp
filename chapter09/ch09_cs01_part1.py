import pickle

def main():
    users=[]
    for i in range(1,4):
        name=input(f"Enter user{i}: ")
        users.append(name)

    with open("registered_users.pickle","wb") as f:
        pickle.dump(users,f)
        print(f"{len(users)} registered user IDs are saved.")

if __name__ == "__main__":
   main()