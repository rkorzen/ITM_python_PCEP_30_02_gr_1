from abc import ABC, abstractmethod



class Interfejs(ABC):

    @abstractmethod
    def metoda(self):
        pass

    @abstractmethod
    def metoda2(self):
        pass



class Klasa(Interfejs):

    def metoda(self):
        print("Metoda z klasy Klasa")

    def metoda2(self):
        print("Metoda2 z klasy Klasa")


class Klasa2(Interfejs):

    def metoda(self):
        print("Metoda z klasy Klasa")

    def metoda2(self):
        print("Metoda2 z klasy Klasa")


class ManagerPowiadomien:

        def __init__(self, klasa: Interfejs):
            self.klasa = klasa

        def powiadom(self):
            self.klasa.metoda()
            self.klasa.metoda2()


k1 = Klasa()
k2 = Klasa2()

m = ManagerPowiadomien(k2)

m.xxx = lambda: print("xxx")

m.xxx()

ManagerPowiadomien.powiadom = lambda self: print("Powiadomienie")



class Foo:
    # __slots__ = ["a", "b"]

    def __init__(self):
        self.a = 10
        self.b = 20

f = Foo()
# print(f.__dict__)
# f.c = 30
# print(f.__dict__)

print(str.__dict__)

# str.x = 10

def square(self):
    print(self.a ** 2)

x = "test"
f.y = square

f.y(f)