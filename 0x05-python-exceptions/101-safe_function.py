#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        return fct(*args)
    except Exception as e:
        print("Exception: {}".format(str(e)), file=sys.stderr)
        return None
