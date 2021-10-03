def my_func(**kargs):
    for key,value in kargs.items():
        print("%s == %s" %(key,value))



my_func(first = 'my', mid = 'name', last = 'pratigya')