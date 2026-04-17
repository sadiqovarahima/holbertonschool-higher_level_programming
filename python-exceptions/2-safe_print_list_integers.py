#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        cnt = 0
        for i in range(x):
            if type(my_list[i]) is not int:
                continue
            print("{:d}".format(my_list[i]), end="")
            cnt += 1
        print()
        return cnt
    except Exception:
        pass
