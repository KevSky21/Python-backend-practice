class Person:

    def __init__(self, name: str, gender: str, age: int):
        self.name: str = name
        self.gender:  str = gender
        self.age: int = age

    def greet(self) -> None:
        print(f"Hello {self.name}!")

    def allowed_to_drink(self) -> bool:
        return self.age >= 21

    def bathroom_option(self) -> bool:
        if self.gender == "Male":
            return True
        else:
            return False

