'''
Created on Oct 24, 2016

@author: https://docs.python.org/3/tutorial/classes.html
'''
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"
        return spam

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)
    x= do_global()
    print("Using value returned in x:", x)

scope_test()
print("In global scope:", spam)