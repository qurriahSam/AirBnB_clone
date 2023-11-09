#!usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    """The class that implements the console
    for the AirBnB clone web application
    """

    prompt = "(hbnb) "
        
    def do_EOF(self, argv):
        """EOF signal to exit program"""
        print("")
        return True
    
    def do_quit(self, argv):
        """Exits the console"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()