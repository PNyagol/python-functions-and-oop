class Dog():
    species = 'Canis familiaris'

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
    

    def __str__(self):
        return f'{self.name} is {self.age} years old.'
    

    def speak(self, sound):
        return f'{self.name} says {sound}.'

miles = Dog('Miles', 6, 'Jack Russell Terrier')

buddy = Dog('Buddy', 4, 'Dachsund')

kibaki = Dog('Guok', 12, 'Shephard')

print(miles)
print(miles.speak('Yap'))
print(miles.species)

print(buddy)
print(buddy.speak('Woof'))
print(buddy.species)

print(kibaki)
print(kibaki.speak('Goof'))
print(kibaki.species)