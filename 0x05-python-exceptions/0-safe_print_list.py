#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if x <= 0:
        print("")
        return 0
    for idx in range(x):
        try:
            print(f"{my_list[idx]}", end="")
        except Exception:
            print("")
            return idx
    else:
        print("")
        return idx+1
