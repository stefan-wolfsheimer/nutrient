def explore_commands(modules):
    """Scans modules for classes derived from Command.
    """
    import inspect
    import command
    iscls = lambda k: \
            inspect.isclass(k) and \
            issubclass(k, command.Command) and \
            k != command.Command
    ret = []
    for module in modules:
        for subklass in inspect.getmembers(module, iscls):
            ret.append(subklass[1])
    return ret
