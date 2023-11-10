#!usr/bin/python3
import cmd
import re
from shlex import split

import models
from models.base_model import BaseModel

CLASSES = [
    "BaseModel"
]

def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)

    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl

def check_args(args):
    """checks if args is valid
    Args:
        args (str): the string containing the arguments passed to a command
    Returns:
        Error message if args is None or not a valid class, else the arguments
    """
    arg_list = parse(args)

    if len(arg_list) == 0:
        print("** class name missing **")
    elif arg_list[0] not in CLASSES:
        print("** class doesn't exist **")
    else:
        return arg_list

class HBNBCommand(cmd.Cmd):
    """The class that implements the console
    for the AirBnB clone web application
    """

    prompt = "(hbnb) "
    storage = models.storage
        
    def do_EOF(self, argv):
        """EOF signal to exit program"""
        print("")
        return True
    
    def do_quit(self, argv):
        """Exits the console"""
        return True

    def emptyline(self):
        """ Do nothing on empty input line """
        pass

    def do_create(self, argv):
        """ Creates a new instance of class """
        args = check_args(argv)
        if args:
            print(eval(args[0])().id)
            self.storage.save()

    def do_show(self, argv):
        """Prints the string representation of an instance based
        on the class name and id"""
        args = check_args(argv)
        if args:
            if len(args) != 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                if key not in self.storage.all():
                    print("** no instance found **")
                else:
                    print(self.storage.all()[key])


if __name__ == '__main__':
    HBNBCommand().cmdloop()