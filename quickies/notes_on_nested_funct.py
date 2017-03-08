""" a quick demo of nesting functions to return functions """


def outer():
    def inner():
        print("This is inner.")

    print("This is outer, returning inner.")
    return inner

i = outer()
#will print This is outer returning inner.
i() # will print this is inner since that was the return value
