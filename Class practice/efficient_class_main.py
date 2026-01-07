from efficient_person import Person


def prompt_person(label: str) -> Person:
    print(f"\nEnter {label}'s information:")
    name = input("Name: ")
    age = int(input("Age: "))
    gender = input("Gender: ")
    return Person(name, gender, age)


def menu(people: list[Person]) -> None:
    choice = ""

    while choice not in ("3", "exit"):
        print("\nWhat would you like to do?")
        choice = input("1. Drink  2. Restroom  3. Exit: ").lower()

        if choice in ("1", "drink"):
            for person in people:
                person.request_drink()

        elif choice in ("2", "restroom"):
            for person in people:
                person.use_restroom()


def main():
    people = [
        prompt_person("your"),
        prompt_person("your partner")
    ]

    menu(people)


if __name__ == "__main__":
    main()
