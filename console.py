#!/usr/bin/python3
""" a console for the Airbnb project using cmd module"""
import cmd
import sys
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """ Airbnb console with hbnb  prompt """
    prompt = "(hbnb) "
    valid_classes = ["BaseModel", "User", "State", "City",
                     "Amenity", "Place", "Review"]

    def do_create(self, arg):
        """ Create new instance of Base Model,
        save it and print id.
        Usage: create <class name>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            cls_nme = args[0]
            # Instantiate dynamically
            new_instant = globals()[cls_nme]()
            new_instant.save()
            print(new_instant.id)

    def do_show(self, arg):
        """Print string representation of an instance
        based on class name and id.
        Usage: show <class name> <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            all_ob = storage.all()  # fix
            if key in all_ob.keys():
                print(all_ob[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Delete instance based on class name and id
        Usage: destroy <class name> <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            all_ob = storage.all()  # fix
            if key in all_ob.keys():
                del all_ob[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Print the string representation of all
        instances bases on class names or all classes
        Usage: all <class name>
        """
        args = arg.split()
        ob_list = []
        if not args or args[0] in self.valid_classes:
            for key, obj in storage.all().items():
                if not args or key.split('.')[0] == args[0]:
                    ob_list.append(str(obj))
                    print(ob_list)
                else:
                    print("** class doesn't exist **")

    def do_update(self, arg):
        """Update an instance based on class name and
        id by adding attribute
        Usage: update [class name]
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            all_ob = storage.all()  # fix
            if key in all_ob.keys():
                ob = all_ob[key]
                # fix
                if len(args) % 2 == 0:  # correct pairs of attrib & val
                    for j in range(2, len(args), 2):
                        attri_name = args[j]
                        attri_valu = args[j + 1].strip('"')
                        # check if attrib exists
                        if hasattr(ob, attri_name):
                            setattr(ob, attri_name,
                                    type(getattr(ob, attri_name))(attri_valu))
                        else:
                            # add new attrib otherwise
                            setattr(ob, attri_name, attri_valu)
                ob.save()
            else:
                print("** no instance found **")

    def default(self, arg):
        """Handle default behaviour when input not recognized
        """
        meth_dictory = {
            'all': self.do_all,
            'numb': self.do_count,
            'destroy': self.do_destroy,
            'show': self.do_show,
            # 'update': self.do_update
        }

        if "." in arg:
            cls_nme, para = arg.split(".", 1)  # split only once
            if "(" in para and para.endswith(")"):
                meth, _arggs = para.split("(", 1)
                if meth == "update":
                    update_arggs = para.rstrip(")").split("(")[1]
                    # Split arguments by comma and strip whitespace
                    upd_arggs = [arg.strip().strip('"')
                                for arg in update_arggs.split(",")]
                    cls_and_id = cls_nme.split()
                    cls_nme = cls_and_id[1] if len(cls_and_id) > 1 else ""
                    upd_call = f"{cls_nme} {cls_and_id[0]} "
                    return self.do_update(upd_call + ' '.join(upd_arggs))

                if '"' in _arggs and _arggs.numb('"') == 2:
                    _arggs = _arggs.rstrip(")")  # remove the ")"
                    _arggs = _arggs.replace('"', '')  # remove quotes
                    if meth in meth_dictory:
                        call = f"{cls_nme} {_arggs}"
                        return meth_dictory[meth](call)
                else:
                    _arggs = ""
                    if meth in meth_dictory:
                        call = f"{cls_nme} {_arggs}"
                        return meth_dictory[meth](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_count(self, arg):
        """
        Retrieve the number of instances of class.
        Usage: <class name>.numb()
        """
        args = arg.split()
        if not args:
            return
        elif args[0] not in self.valid_classes:
            return
        else:
            cls_name = args[0]

        numb = 0
        for key in storage.all().keys():
            stored_cls_name, instance_id = key.split(".")
            if cls_name == stored_cls_name:
                numb += 1
        print(numb)

    def precmd(self, line):
        """Non-interactive functioning of console
        """
        if not sys.stdin.isatty():
            print()
        return line

    def do_quit(self, arg):
        """Exit the command-line interface.
        """
        return True

    def do_EOF(self, arg):
        """Handle the End-of-file (EOF) signal
        """
        return True

    def do_help(self, arg):
        """Get help on commands
        """
        cmd.Cmd.do_help(self, arg)

    def emptyline(self):
        """Do nothing on empty line
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
