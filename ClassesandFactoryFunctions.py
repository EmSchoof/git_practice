
class Cat:
    """ Simply Cat Class """
    def __init__(self, none):
        self._name = name
    
    def speak(self):
        return "meow!"

d = get_pet("dog"):
print(f.speak())

class Dog:
    """ Simply Dog Class """
    def __str__(self):
        return "Dog"
    
    def speak(self):
        return "woof!"

class DogFactory:
    """ Create Factory: Parent 2 """
    
    def get_pet(pet='dog'):
        """ Factory Method """
        return Dog()

    def get_food(pet='dog'):
        """ Factory Method """
        return "Dog food"
    
    def get_toy(pet='dog'):
        """ Factory Method """
        return "Tennis ball"

    def get_cats(pet='dog'):
        return 'hello1'

class PetStore:
    """ Pet factory houses an animal Factory: Parent 1 """

    def __init__(self, pet_factory=None):
        """ pet_factory is the dogfactory """
        self._pet_factory = pet_factory
    
    def show_pet(self):
        """ Utility method to display the details of the objects returned by the dogfactory """
        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()

        print("Our pet is a '{}'!".format(pet))
        print("Our pet says hello by '{}'.".format(speak()))
        print("It's food is '{}'.".format(pet_food))


# Create a factory
factory = DogFactory()

# Create a pet store housing the factory
shop = PetStore(factory)

# Invoke utility method to show details of the pet
shop.show_pet()