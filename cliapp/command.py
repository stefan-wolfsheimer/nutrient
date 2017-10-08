class Command(object):
    def __init__(self):
        pass

    def get_name(self):
        import string
        return string.lower(type(self).__name__)

    def do(self, app, rest):
        pass

    def complete(self, app, rest, beg, end):
        return []
