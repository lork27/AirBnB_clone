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

### Technical Characteristics

*    Written in Python3
*    PEP8 compliant
*    Console created with the module cmd
*    Tested with the unittest module

### How to use the interpreter?
Usage in interactive mode:

$ ./console.py

This executes the command interpreter and displays the prompt:

(hbnb)

and waits for the user to type a command. A command line always ends with a new line. The prompt is displayed again each time a command is executed.

...and in non-interactive mode:

$ echo "help" | ./console.py
(hbnb)
Documented commands (type help<topic>):

========================================

EOF  all  create  destroy  help  quit  show  update

(hbnb)

### Here is an example of how to use our console
(hbnb) create BaseModel
de2630a8-7556-4e6d-8b55-8b0a4ba8082d

(hbnb) show BaseModel 
de2630a8-7556-4e6d-8b55-8b0a4ba8082d

[BaseModel] (de2630a8-7556-4e6d-8b55-8b0a4ba8082d) {'updated_at': datetime.datetime(2021, 11, 14, 14, 4, 12, 756946), 'created_at': datetime.datetime(2021, 11, 14, 14, 4, 12, 756836), 'id': 'de2630a8-7556-4e6d-8b55-8b0a4ba8082d'}

(hbnb) quit


### Commands the console accepts:
* create: creates a new instance of the class, saves it to the JSON file and prints the id. Ex: create BaseModel (Must be used with existing class, otherwise prints error)
* show: Prints the string representation of an instance based on the class name and id. Ex: show BaseModel 1234-1234-1234 (Must be used with existing class and id, otherwise prints error)
* update: Updates an instance based on the class name and id by adding or updating attributes and saves the changes to the JSON file.
* destroy: Deletes an instance based on the class name and id and saves the changes in the JSON file. Ex destroy BaseModel 121212 (Must be used with existing class and id, otherwise prints error)
* all: Prints all string representation of all instances based or not on the class name. Ex all BaseModel (shows all instances of class) or all (shows all instances of all classes) (Must be used with existing class, otherwise prints error)

### File Manifest:

*   models
*   engine
*   init.py
*   file_storage.py
*   init.py
*   amenity.py
*   base_model.py
*   city.py
*   place.py
*   review.py
*   state.py
*   user.py

### Test files:

*             init.py
*             test_console.py
*             test_models
*             init.py
*             test_amenity.py
*             test_base_model.py
*             test_city.py
*             test_file_storage.py
*             test_place.py
*             test_review.py
*             test_state.py
*             test_user.py

### Other files:

*   console.py
*   README.md
*   AUTHORS

### Known bugs
This project is still in under construction, therefore bugs may be present. If you find any, you're welcome to let us know :)
