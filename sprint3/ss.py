def m (arg,*args,**kwargs):
    print(args,kwargs)
m(1,2,3,b=4,name="First name",job="First Job")