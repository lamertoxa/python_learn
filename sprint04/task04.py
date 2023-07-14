import re
import math


class Testpaper:
    def __init__(self, subject, markscheme, pass_mark):
        self.subject = subject
        self.markscheme = markscheme
        self.pass_mark = pass_mark


class Student:
    def __init__(self, tests_taken="No tests taken"):
        self.tests_taken = tests_taken

    def take_test(self, test, answers):
        grade = 0
        for true_ans, guess in zip(test.markscheme, answers):
            if re.search(r"[A-Z]", true_ans).group(0) == re.search(r"[A-Z]", guess).group(0):
                grade += 1
        if math.ceil((grade / len(answers)) * 100) >= int(re.search(r"[0-9]+[^%]", test.pass_mark).group(0)):
            if type(self.tests_taken) is dict:
                self.tests_taken[test.subject] = f"Passed! ({math.ceil((grade / len(answers)) * 100)}%)"
            else:
                self.tests_taken = {}
                self.tests_taken[test.subject] = f"Passed! ({math.ceil((grade / len(answers)) * 100)}%)"

        else:
            if type(self.tests_taken) is dict:
                self.tests_taken[test.subject] = f"Failed! ({math.ceil((grade / len(answers)) * 100)}%)"
            else:
                self.tests_taken = {}
                self.tests_taken[test.subject] = f"Failed! ({math.ceil((grade / len(answers)) * 100)}%)"


paper1 = Testpaper('Maths', ['1A', '2C', '3D', '4A', '5A'], '60%')
paper3 = Testpaper('Computing', ['1D', '2C', '3C', '4B', '5D', '6C', '7A'], '75%')
student2 = Student()
student3 = Student()
student2.take_test(paper3, ['1A', '2C', '3A', '4C', '5D', '6C', '7B'])
print(student3.tests_taken)
student3.take_test(paper1, ['1C', '2D', '3A', '4C', '5A'])
student3.take_test(paper3, ['1A', '2C', '3A', '4C', '5D', '6C', '7B'])
print(student3.tests_taken)
print(paper3.subject)
print(paper3.markscheme)
print(paper3.pass_mark)
