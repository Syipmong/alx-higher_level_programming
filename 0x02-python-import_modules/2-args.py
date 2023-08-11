#!/usr/bin/python3
if __name__ == "__main__":
    """give you the index and the args if no args give you 0 args """
    import sys

    counter = len(sys.argv) - 1
    if counter == 0:
        print("0 arguments.")
    elif counter == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(counter))
    for index in range(counter):
        print("{}: {}".format(index + 1, sys.argv[index + 1]))
