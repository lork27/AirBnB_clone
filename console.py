#!/usr/bin/env python3
import cmd
import json
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity

classes_dict = {"BaseModel": BaseModel,
                "User": User,
                "City": City,
                "Place": Place,
                "State": State,
                "Review": Review,
                "Amenity": Amenity,
                }

list_of_classes = list(classes_dict.keys())
objs = storage.all()


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand - command line interface implementation
    """
    prompt = "(hbnb) "
    file = None

    def do_all(self, arg):
        """
        print str representation of all instances
        based on name
        """
        if len(arg) == 0:
            # print(objs)
            for key in objs.keys():
                obj = objs[key]
                print(obj)
        elif arg in list_of_classes:
            for key in objs.keys():
                if arg in key:
                    obj = objs[key]
                    print(obj)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        prints str representation of obj based in id
        """
        split_arg = arg.split(" ")
        if len(arg) == 0:
            print("** class is missing **")
        else:
            if split_arg[0] not in list_of_classes:
                print("** class doesn't exist **")
            elif len(split_arg) < 2:
                print("** instance id is missing")
            else:
                try:
                    print(objs[split_arg[0] + "." + split_arg[1]])
                except:
                    print("** no instance found **")
    '''basic commands below'''

    def do_quit(self, line):
        self.close()
        quit()

    def emptyline(self):
        pass

    def do_EOF(self, line):
        """ handle EOF """
        return True

    def help_quit(self):
        print('\n'.join(['Quit command to exit the program\n']))

    def close(self):
        if self.file:
            self.file.close()
            self.file = None


if __name__ == "__main__":
    HBNBCommand().cmdloop()
