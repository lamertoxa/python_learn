class Employee:
    def __init__(self,name,**kwargs):
        self.name,self.lastname = [i for i in name.split(" ")]


        for key,value in kwargs.items():
            self.__setattr__(key,value)


a = Employee("sss ss",sex="meow",kto="lol")


