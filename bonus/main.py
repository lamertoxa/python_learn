import unittest
import json


def get_users_with_grades(user,subject,grades):
    users_dict = []
    with open(user) as doc:
        user_file = json.load(doc)
    with open(subject) as doc:
        user_file = json.load(doc)
    with open(grades) as doc:
        user_file = json.load(doc)




def get_subjects_from_json():
    pass

users = get_users_with_grades("users.json", "subjects.json", "grades.json")
