# Classes
# A Class is like an object constructor, or a "blueprint" for creating objects, Almost everything in Python is an object, with its properties and methods. 
# The phrase "instantiating a class" means the same thing as "creating an object."
# When you create an object, you are creating an "instance" of a class, therefore "instantiating" a class.

# Dictionaries
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates, Dictionaries are used to store data values in key:value pairs, 
# insert or update a value.
# Dictionary items are presented in key:value pairs, and can be referred to by using the key name, Dictionary items are ordered, changeable, and does not allow duplicates.

# Real World Applications of Classes
# A bank account is a real world thing that can be modeled and solved with Classes.
# Classes can help code your code be more tangable, organized and easier to understand.

# Utilization of Dictionaries
# Dictionaries can be utilized for Database Records, Dictionaries are presented in key:value pairs, and they can be referred to by using the key name.
# When Dictionaries are used in combination with classes they can be a great tool for managing objects in applications.
# For example You can use a dictionary to store the attributes object data.

# Python Classes and Dictionaries Demonstration 

class Planet:
    def __init__(self, name, population, continents, climate):
        self.name = name
        self.population = population 
        self.continents = continents
        self.climate = climate

    def set_population(self, population):
        self.population = population

    def set_continents(self, continents):
        self.continents = continents

    def set_climate(self, climate):
        self.climate = climate

    def get_population(self):
        return self.population

    def get_continents(self): 
        return self.continents 

    def get_climate(self):
        return self.climate 

    def get_data(self):
        return {
            "name": self.name,
            "population": self.population,
            "continents": self.continents,
            "climate": self.climate,
        }

# planet instances
nirn = Planet("Nirn", 300000000, "Tamriel, Akavir, Atmora, Yokuda, Aldmeris, and Pyandonea", "Snow and rain are common forms of precipitation on Nirn. Certain areas in northern Tamriel, such as Skyrim and Solstheim, experience rare Auroras, colorful waves of energy in the night sky.")

earth = Planet("Earth", 8000000000, "Asia, Africa, North America, South America, Antarctica, Europe, and Australia.", "Some parts of Earth are hot and rainy nearly every day. They have a tropical wet climate. Others are cold and snow-covered most of the year.")

print("Earth Information:")
print(earth.get_data())

print("    ")

print("Nirn Information:")
print(nirn.get_data())
