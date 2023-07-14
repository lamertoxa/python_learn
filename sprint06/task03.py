import json
import jsonschema
from jsonschema import validate
import csv

class DepartmentName(Exception):
    def __init__(self,data):
        self.data = data
    def __str__(self):
        return self.data
class InvalidInstanceError(Exception):
    def __init__(self,data):
        self.data = data
    def __str__(self):
        return self.data
def user_with_department(csv_file, user_json, department_json):
    with open(user_json)as doc:
        data_name = json.load(doc)
    with open(department_json) as doc:
        data_department_name = json.load(doc)
    schema_name = {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "department_id": {"type": "number"},
        },
        "required":["department_id","name"]
    }
    schema_dep = {
        "type": "object",
        "properties": {
            "id": {"type": "number"},
            "name": {"type": "string"},
        },
        "required": ["id","name"],
    }
    try:
        for i in data_name:
            validate(instance=i, schema=schema_name)
    except:
        raise InvalidInstanceError("Error in user schema")
    try:
        for i in data_department_name:
            validate(instance=i, schema=schema_dep)
    except:
        raise InvalidInstanceError("Error in department schema")
    new_values=[]
    for i in data_name:
        new_values.append([i['name'],[j['name'] for j in data_department_name if j['id']==i['department_id'] ]])
        if new_values[-1][1] == []:
            raise  DepartmentName(f"Department with id {i['department_id']} doesn't exists")
    file = open(csv_file,"w")
    writer = csv.writer(file)
    writer.writerow(["name","department"])
    for i in new_values:
        writer.writerow([i[0],i[1][0]])
    return new_values


user_with_department("user_department.csv", "user.json", "department_without_id.json")
# user_with_department("user_department.csv", "user_without_dep.json", "department.json")
# user_with_department("user_department.csv", "user_without_dep_id.json", "department.json")
# pprint.pp("user_department.csv")