import json
# type your code here
def find(file, key):
    with open(file) as data:
        obj = json.load(data)
    list_of_uniq = []
    for item in obj:
        if isinstance(obj,dict):
            value_of_key = obj[item]
        else:
            value_of_key = item
        def rec(elements):
            new_values = []
            if isinstance(elements,dict):
                for name,value in elements.items() :
                    if name == key:
                         if isinstance(elements[key],list):
                            new_values.extend(elements[key])
                         else:
                             new_values.append(elements[key])
                    elif isinstance(value,dict):
                        new = rec(value)
                        if isinstance(new, list):
                            new_values.extend(new)
                        else:
                            new_values.append(new)
                    elif isinstance(value,list):
                        for i in value:
                            new = rec(i)
                            if isinstance(new, list):
                                new_values.extend(new)
                            else:
                                new_values.append(new)
            elif isinstance(elements,list):
                for i in elements:
                    new = rec(i)
                    if isinstance(new, list):
                        new_values.extend(new)
                    else:
                        new_values.append(new)
            elif isinstance(elements,str):
                if key == item:
                    new_values.append(elements)



            return new_values
        new_values = rec(value_of_key)
        if isinstance(new_values,list):
            for i in new_values[:]:
                if  i in list_of_uniq:
                    new_values.remove(i)
                else:
                    list_of_uniq.append(i)
        elif isinstance(new_values,str):
            list_of_uniq.append(new_values)
    return list_of_uniq


print(find("array_pass.json", 'password'))
print(find("2.json", 'password'))
print(find("5.json", 'username'))
print(find("2020-01.json", 'courses'))






