class Person:
    species = "Homo Sapiens"

    def __init__(self, name, b_year):
        self.name = name
        self.xxx = 10
        self.b_year = b_year

    def __repr__(self):
        return f"{self.name} ({self.b_year})"


    def hello(self):
        return f"Hello, I am {self.name}"

p = Person("Alex", 1992)
p1 = Person("Sofia", 1996)

Person.species = "Homo Erectus"
# p1.species = "Homo Erectus"
print(p, type(p))

print(p.species)
print(p1.species)


persons = [p, p1]

for p in persons:
    print(p.hello())

print(p)

attributes_to_check = ["name", "b_year", "cos"]

def print_attributes(attributes_to_check: list, instance: Person):
    for a in attributes_to_check:
        print(getattr(instance, a, "xxx"))

print_attributes(attributes_to_check, p)


class Square:
    def __init__(self, side):
        self.side = side
        self.__x = 10

    def __repr__(self):
        return f"Square({self.side}"

    def __gt__(self, other):
        return self.side > other.side

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, value):
        if value < 0:
            raise ValueError("...")
        self._side = value

    @property
    def area(self):
        return self.side ** 2

    @area.setter
    def area(self, value):
        if value < 0:
            raise ValueError("Pole nie może być mniejsze niż 0")
        self.side = value ** 0.5

s = Square(10)
s2 = Square(20)

print(s > s2)

s3 = Square(10)
print(s3.area)

s3.area = 100

print(s3.side)
#
# s3.area = -100
# print(s3.side)

print("x", s3._Square__x)
# print(s3.__x)