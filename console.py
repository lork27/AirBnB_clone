#!/usr/bin/env python3
"""module with the console interpreter"""
import cmd
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

    def default(self, arg):
        """
        Called on an input line when the command prefix is not recognized.
        """
        arglist = arg.split('.')
        arguments = {
            "all()": self.do_all,
            "count()": self.do_count,
        }
        if len(arglist) < 2:
            print(f"** Unknown syntax {arg}**")
            return
        else:
            clsname = arglist[0]
            print(clsname)
            method = arglist[1]
            print(method)
            if clsname not in list_of_classes:
                print("** class doesn't exist **")
            else:
                if method in arguments.keys():
                    arguments[method](clsname)
                else:
                    print(f"** Unknown syntax {arg}**")

    def do_all(self, arg):
        """
        print str representation of all instances
        based on name
        """
        if len(arg) == 0:
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
            print("** class name is missing **")
        else:
            if split_arg[0] not in list_of_classes:
                print("** class doesn't exist **")
            elif len(split_arg) < 2:
                print("** instance id is missing")
            else:
                try:
                    print(objs[split_arg[0] + "." + split_arg[1]])
                except Exception:
                    print("** no instance found **")

    def do_create(self, arg):
        '''create instance of class'''
        if len(arg) == 0:
            print("** class name is missing **")
        elif arg in classes_dict:
            newclass = classes_dict[arg]()
            print(newclass.id)
            storage.new(newclass)
            storage.save()
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """destroy instance of class based on id"""
        split_arg = arg.split(" ")
        if len(arg) == 0:
            print("** class name is missing **")
        else:
            if split_arg[0] not in list_of_classes:
                print("** class name doesn't exist **")
            elif len(split_arg) < 2:
                print("** instance id is missing **")
            else:
                try:
                    idname = split_arg[0] + '.' + split_arg[1]
                    del objs[idname]
                    storage.save()
                except Exception:
                    print("** no instance found **")

    def do_update(self, arg):
        """update or adds attribute to given instance"""
        split_arg = arg.split(" ")
        arglen = len(split_arg)
        if len(arg) == 0:
            print("** class name missing **")
        else:
            if split_arg[0] not in list_of_classes:
                print("** class doesn't exist **")
            elif len(split_arg) < 2:
                print("** instance id missing")
            else:
                try:
                    idname = split_arg[0] + '.' + split_arg[1]
                except Exception:
                    pass
                if idname not in objs.keys():
                    print("** no instance foundi **")
                elif arglen < 3:
                    print("** attribute name missing **")
                elif arglen < 4:
                    print("** value missing **")
                else:
                    setattr(objs[idname], split_arg[2],
                            split_arg[3].strip('"'))
                    storage.save()

    '''Advanced commands below'''

    def do_count(self, arg):
        """counts number of instances of given class"""
        total = 0
        if arg not in classes_dict:
            print("** class doesn't exist **")
            return
        for key in objs.keys():
            if arg in key:
                total += 1
        print(total)
    '''basic commands below'''

    def do_quit(self, line):
        """quit program"""
        self.close()
        quit()

    def emptyline(self):
        """when the user enters no command"""
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
