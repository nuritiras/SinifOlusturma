# instance & attribute

class Musician():

    job="musician"

    def __init__(self,name,age,instrument):
        self.name=name
        self.age=age
        self.instrument=instrument

    def sing(self):
        print(f"We are the champions! {self.instrument}")

my_musician=Musician("James",50,"Guitar")
print(my_musician.name, my_musician.age, my_musician.instrument, my_musician.job)
my_musician.sing()

class DogYears():
    year_factor=7

    def __init__(self,age=5):
        self.age=age
        self.age_multiplied=age*7

    def calculation(self):
        return self.age * DogYears.year_factor

my_dog=DogYears()
print(my_dog.calculation())
print(my_dog.age_multiplied)
