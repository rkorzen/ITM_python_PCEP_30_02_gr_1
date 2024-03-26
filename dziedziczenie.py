
class Xxx:

    def random_number(self):
        return 4

    def speak(self):
        print("Xxx mówi: ...")

class Animal:
    def __init__(self, name,):
        self.name = name

    def voice(self):
        raise NotImplementedError("Metoda voice nie została zaimplementowana")

    def speak(self):
        print(f"Zwierzę mówi: {self.voice()}")


class Dog(Animal, Xxx):
    def voice(self):
        return "Hau hau"

class Cat(Animal, Xxx):
    def voice(self):
        return "Miau miau"

    def speak(self):
        super().speak()
        print("Dodatkowo prężąc grzbiet")

dog = Dog("Burek")
dog.speak()

cat = Cat("Filemon")
cat.speak()
cat.random_number()
