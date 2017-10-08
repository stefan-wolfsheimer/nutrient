import util
from cliapp import Command


class UselessClass(object):
    pass


class Command1(Command):
    pass


class Command2(Command):
    pass


class Command12(Command1):
    pass


def test_explore_commands():
    import test_util
    assert(sorted(util.explore_commands([test_util])) == 
           sorted([ test_util.Command1,
                    test_util.Command2,
                    test_util.Command12]))


