from bleeping import bleep, load_yaml_from_file
from add_poem import add_new
import cmd
import sys

class PomemShell(cmd.Cmd):
    intro = 'Welcome to Pomem.   Type help or ? to list commands.\n'
    prompt = '(pomem) '
    bleep_character = "."

    def do_bleep(self, arg):
        file, level = arg.split()
        lines = load_yaml_from_file(file)
        for line in bleep(lines, level=int(level), bleep_character=self.bleep_character):
            print line

    def do_add_new(self, arg):
        add_new()

    def do_change_bleep(self, arg):
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

