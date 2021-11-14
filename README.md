# 0x00. AirBnB clone - The console

### Introduction
First part of three to create a full web application, an AirBnb clone. In this project, the objective is to write a command interpreter to manage AirBnb objects.

### Management of the objects include:

*    Create a new object (ex: a new User or a new Place)
*    Retrieve an object from a file, a database etc…
*    Do operations on objects (count, compute stats, etc…)
*    Update attributes of an object
*    Destroy an object

### The tasks carried out include:

*    Create a main class (called BaseModel) that takes care of the initialization, serialization, and deserialization of new instances.
*    Create a simple serialization / deserialization flow: Instance <-> Dictionary <-> JSON String <-> file
*    Create all the classes used for AirBnB that inherit from BaseModel (User, State, City, Place, Amenities, Review)
*    Create a storage engine to be able to save and retrieve data.
*    Create all the unittests to validate all the processes

### What’s a command interpreter?
The command interpreter is the program that receives what is written in the terminal and converts it into instructions for the operating system. In this case, we create our own command interpreter for the functions that we need for the correct functioning of our Airbnb clone.