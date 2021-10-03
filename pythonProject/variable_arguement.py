#pythin prog to illustrate *args for variable argument

def myfunc(*args):
    for arg in args:
        print(arg)

myfunc('hello','my','name','maya')
myfunc('hello','my')