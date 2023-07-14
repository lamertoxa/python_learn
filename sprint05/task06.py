class MyError(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return self.data


def check_positive(number):
    try:
        if str(number).isalpha():
            raise MyError("Error type: ValueError!")
        else:
            number = float(number)
    except MyError as er:
        return er

    if number > 0:
        return f"You input positive number: {number}"
    else:
        return f"You input negative number: {number}. Try again."