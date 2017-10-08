import sys
import cmd


class App(cmd.Cmd, object):
    def __init__(self,
                 command_classes=[],
                 completekey='tab',
                 stdin=sys.stdin,
                 stdout=sys.stdout):
        cmd.Cmd.__init__(self, completekey, stdin, stdout)
        self.commands = {}
        for cls in command_classes:
            inst = cls()
            self.commands[inst.get_name()] = inst

    def do_quit(self, rest):
        return True

    def default(self, line):
        command = line.split()[0].lower()
        if command in self.commands:
            self.commands[command].do(self, line.split()[1:])
        else:
            cmd.Cmd.default(self, line)

    def completedefault(self, text, line, beg, end):
        command = line.split()[0].lower()
        if command in self.commands:
            self.commands[command].complete(self, line.split()[1:], beg, end)
        else:
            return []

    def completenames(self, text, *ignored):
        return cmd.Cmd.completenames(self, text) + [
            a for a in self.commands.keys() if a.startswith(text)]
