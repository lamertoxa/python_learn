import json
import pprint
from json import JSONEncoder

# type your code here
class Student:
    def __init__(self,full_name:str,avg_rank:float,courses:list):
        self.full_name=full_name
        self.avg_rank=avg_rank
        self.courses=courses

    def __str__(self):
        return f"{self.full_name} ({self.avg_rank}): {self.courses}"

    def __repr__(self):
        return repr(self.__str__())

    @classmethod
    def serialize_to_json(cls,obj,students_file):
        to_serialize = {"full_name":obj.full_name,
                        "avg_rank":obj.avg_rank,
                        "courses":obj.courses}
        with open(students_file,"w") as doc:
            data = json.dumps(to_serialize)
            doc.write(data)

    @classmethod
    def from_json(cls, student_file):
        with open(student_file) as doc:
            data_name = json.load(doc)
        full_name,avg_rank,courses = [i for i in data_name.values()]
        return cls(full_name,avg_rank,courses)

class Group:
    def __init__(self,title:str,students:list):
        self.title =title
        self.students = students

    def __str__(self):
        return f"{self.title}: {[ '{} ({}): {}'.format(i['full_name'],i['avg_rank'],i['courses'])for i in self.students]}"

    @classmethod
    def create_group_from_file(cls,file):
        with open(file) as doc:
            data = json.load(doc)
        students =[]
        if isinstance(data,list):

            for i in data:

                students.append(i)
        else:
            students.append(data)


        return cls(title=file.split('.')[0],students=students)

    @classmethod
    def serialize_to_json(cls,students,file_name):
        to_serialize = []
        for i in range(len(students)):
            to_serialize.append({"title":students[i].title,"students":students[i].students})


        with open(file_name, "w") as doc:
            data = json.dumps(to_serialize)
            doc.write(data)
# user1 = Student.from_json("2020-01.json")
# print(user1)

# g1 = Group.create_group_from_file("2020_2.json")
# g2 = Group.create_group_from_file("2020-01.json")
# Group.serialize_to_json([g1, g2],"g1")


g1 = Group.create_group_from_file("2020_2.json")
print(g1)








