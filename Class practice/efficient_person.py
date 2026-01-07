class Person:
    def __init__(self, name: str, gender: str, age: int):
        self.name = name
        self.gender = gender.lower()
        self.age = age

    def allowed_to_drink(self) -> bool:
        return self.age >= 21

    def bathroom_option(self) -> str:
        return "men's" if self.gender == "male" else "women's"

    def request_drink(self) -> None:
        if self.allowed_to_drink():
            print(f"Here is your drink, {self.name}!")
        else:
            print(f"Sorry {self.name}, you can't drink.")

    def use_restroom(self) -> None:
        print(f"The {self.bathroom_option()} bathroom is over there, {self.name}.")
