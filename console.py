#!/usr/bin/python3
"""Araque and Baquero AirBNB Console """
import cmd
from models import storage
from models.engine import file_storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Console that emulate AirBNB"""
    prompt = '(hbnb) '

    # Class Attribute to help precmd
    classes = {"User", "BaseModel"}

    def do_count(self, line):
        """return how many instances are"""
        count = 0
        if line:
            for key, value in storage.all().items():
                if str(value.__class__.__name__) == line:
                    count += 1
        print(count)

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """EOF execution to exit the program
        """
        return True

    def do_create(self, line):
        """Create a instance of a AirBnb class"""
        if line is None or line == "":
            print("** class name missing **")
        else:
            if line:
                new_obj_id = eval(line + "()")
                new_obj_id.save()
                print(new_obj_id.id)
            else:
                print("** class doesn't exist **")
                return

    def do_all(self, line):
        """ Print all instances in string representation """
        objects = []
        if line == "":
            print([str(value) for key, value in storage.all().items()])

        else:
            st = line.split(" ")
            if st[0] not in self.classes:
                print("** class doesn't exist **")
            else:
                for key, value in storage.all().items():
                    clas = key.split(".")
                    if clas[0] == st[0]:
                        objects.append(str(value))
                print(objects)

    def emptyline(self):
        """ Empty File """
        pass

    def do_show(self, line):
        """ command show """
        if line is None or line == "":
            raise SyntaxError("** class name missing **")
        else:
            st = line.split(" ")
            if st[0] not in self.classes:
                raise NameError("** class doesn exist **")
            if len(st) < 2:
                raise IndexError("** instance id missing **")
            key = "{}.{}".format(st[0], st[1])
            obs = storage.all()
            if key in obs:
                print(obs[key])
            else:
                raise KeyError("** no instance found **")

    def do_destroy(self, line):
        """ Function that destroy the instance """
        if line is None or line == "":
            print("** class name missing **")
        else:
            st = line.split(" ")
            if st[0] not in self.classes:
                print("** class doesn't exist **")
            else:
                ob_sto = storage.all()
                obs = "{}.{}" .format(st[0], st[1])
                if obs in ob_sto:
                    del(ob_sto[obs])
                    storage.save()

    def default(self, line):
        """ Dafault function """
        split_line = line.split('.')
        if len(split_line) > 1:
            print("nico")
        else:
            cmd.Cmd.default(self, line)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
