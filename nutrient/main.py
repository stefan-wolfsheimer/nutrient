import sys
import cliapp


class NutrientCliApp(cliapp.App):
    def __init__(self):
        import commands
        cmd = cliapp.explore_commands([commands])
        super(NutrientCliApp, self).__init__(cmd)


def main(argv=sys.argv[1:]):
    return NutrientCliApp().cmdloop()


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
