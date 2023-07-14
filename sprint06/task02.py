import json
import logging


logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')



# type your code here
def parse_user(output_file, *input_files):
    writed_dicts = []

    def parser(key, dictionary):
        nonlocal writed_dicts
        for i in writed_dicts:
            if dictionary[key] in i.values():
                return None
        try:
            if isinstance(dictionary[key], dict):
                writed_dicts.extend(dictionary)
            else:
                writed_dicts.append(dictionary)
            return writed_dicts
        except KeyError:
            return None
    parsed= []
    for file in input_files:
        try:
            with open(file) as data:
                parsed = json.load(data, object_hook=lambda dict: parser("name", dict))
        except FileNotFoundError:
            logging.error(f"File {file} doesn't exist")
            continue
    result = []

    for i in parsed:
        if isinstance(i, list):
            for j in i:
                result.append(j)
        elif i == None:
            continue
        else:
            result.append(i)
    with open(output_file, "wt") as doc:
        json_object = json.dumps(result, indent=4)
        doc.write(json_object)

