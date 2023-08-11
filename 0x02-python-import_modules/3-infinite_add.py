#!/usr/bin/python3
if __name__ == "__main__":
    """give the result of the addition of all arguments """
    import sys
    total = 0
    cont = len(sys.argv) - 1
    for index in range(cont):
        num = int(sys.argv[index + 1])
        total += num
    print("{}".format(total))
