import sys

def main(argv=sys.argv[1:]):
    print " ".join(argv)
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
