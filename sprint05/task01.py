class ToSmallNumberGroupError(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return self.data


def check_number_group(number):
    try:
        if int(number) > 10:
            return f"Number of your group {number} is valid"
        else:
            raise ToSmallNumberGroupError("We obtain error:Number of your group can't be less than 10")

    except ToSmallNumberGroupError as er:
        return er
    except ValueError:
        return "You entered incorrect data. Please try again."