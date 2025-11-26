import random 
def rolldice():
    number = random.randint(1, 6)
    print("Your number is ", number)
def main():
    while True:
        print("1. Roll the dice")
        print("2. Exit")
        choice = input("what do you want to do? ")
        if choice == "1":
            rolldice()
        elif choice == "2":
            break
        else:
            print("Invalid input. Please try again with the choice 1 or 2.")

if __name__ == "__main__":
    main()