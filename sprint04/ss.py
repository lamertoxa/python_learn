class Sex:
    def __init__(self):
        pass
class Person(Sex):
    def __init__(self,id):
        Sex.__init__(self)
        self.id = id

sam = Person(100)
sam.__dict__['age']=49

print(sam.age+len(sam.__dict__))