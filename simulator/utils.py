import sys

from daemon import start, killall


# decorator
def npm_decorator(num_node):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(num_node)


            # npm start
            if not start(num_node):
                print("[FAIL] npm start")
                killall()
                sys.exit(1)

            # function
            results = func(*args, **kwargs)

            # Killall npm
            if not killall():
                print("[FAIL] killall npm")
                sys.exit(1)

            return results
        return wrapper
    return decorator


def hexToBinary(s):
    lookupTable = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011',
        '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'a': '1010', 'b': '1011',
        'c': '1100', 'd': '1101', 'e': '1110', 'f': '1111'
    }

    res = ""
    for i in s:
        if i in lookupTable:
            res += lookupTable[i]
        else:
            return ""

    return res
