import re
def valid_email(email):
    try:
        check_mail = re.search(r"[\w]+@[a-zA-Z]+[.]?[a-zA-Z]+\.[a-z]{2,3}$", email).group(0)
    except AttributeError:
        return "Email is not valid"

    if check_mail == email:
        return "Email is valid"
    else:
        return "Email is not valid"

