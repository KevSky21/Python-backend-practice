from practice_main import Person

def prompt():
    print(f"Please enter your name, age, and gender.")
    username = input("Enter your name: ")
    age = int(input("Enter your age: "))
    gender = input("Enter your gender: ")
    print(f"Please enter your partners name, age, and gender.")
    username2 = input("Enter partner name: ")
    age2 = int(input("Enter partner age: "))
    gender2 = input("Enter partner gender: ")

    return Person(username, gender, age), Person(username2, gender2, age2)

def choice(person1: Person, person2: Person) -> None:

    choice_made = "None"

    while choice_made != "exit" and choice_made != "3":
        print(f"What would you like to do?")
        choice_made = input("1.Drink  2. Restroom.  3.Exit")
        choice_made = choice_made.lower()

        if choice_made == "1" or choice_made == "drink":
            if person1.allowed_to_drink():
                print(f"Here is your drink {person1.name}!")
            else:
                print(f"Sorry, you can't drink {person1.name}!")
            if person2.allowed_to_drink():
                print(f"Here is your drink {person2.name}!")
            else:
                print(f"Sorry, you can't drink {person2.name}!")

        elif choice_made == "2" or choice_made == "restroom":
            if person1.bathroom_option():
                print(f"The men's bathroom is over there {person1.name}.")
            else:
                print(f"The women's bathroom is over there {person2.name}.")
            if person2.bathroom_option():
                print(f"The men's bathroom is over there {person2.name}.")
            else:
                print(f"The women's bathroom is over there {person2.name}.")

def main():

    me, partner = prompt()

    choice(me, partner)



if __name__ == "__main__":
    main()
