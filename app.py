from bleeping import bleep, load_yaml_from_file
from add_poem import add_new
from argument_parser import *
from list_poems import list_poems
import cmd
import sys

class PomemShell(cmd.Cmd):
    intro = 'Welcome to Pomem.   Type help or ? to list commands.\n'
    prompt = '(pomem) '
    bleep_character = "."

    def do_bleep(self, arg):
        expected_args = [('poem_name', str,), ('level', int,)]
        file, level = parse_args(expected_args, arg)
        lines = load_yaml_from_file(file)
        for line in bleep(lines, level=int(level), bleep_character=self.bleep_character):
            print line[0]
            # print line[1]

    def do_add_new(self, arg):
        """
        Adds a new poem to the library
        """
        add_new()

    def do_library(self, arg):
        """
        Lists all available poem titles
        """
        print "Listing all poems in the library..."
        list_poems()

    def do_change_bleep(self, arg):
        """
        Changes the character used to indicate a blank
        """
        old_bleep = self.bleep_character
        if len(arg) == 1:
            self.bleep_character = arg
            print self.bleep_character
            print "Changed bleep from {old} to {new}.".format(old=old_bleep, new=arg)

    def do_exit(self, arg):
        print('Thank you for using Pomem')
        return True


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding("utf-8")
    PomemShell().cmdloop()

# if __name__ == '__main__':
#     file = sys.argv[1]
#     level = int(sys.argv[2])
#     lines = load_yaml_from_file('data/' + file + '.yml')
#     for line in bleep(lines, level=level):
#         print line

