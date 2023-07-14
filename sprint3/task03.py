def create_account(user_name: str, password: str, secret_words: list):
    if len(password) < 6 or not any(x.isupper() for x in password) \
            or not any(x.islower() for x in password) \
            or not any(x.isdigit() for x in password) \
            or not (any(True  if not x.isdigit() and not x.isalpha() else False for x in password )):
        raise ValueError

    def check(guess_pass, guess_secret):

        if guess_pass == password:
            if len(guess_secret) != len(secret_words):
                return False

            check_secret = 2
            for word in secret_words:

                if word in guess_secret:
                    guess_secret.remove(word)
                else:
                    check_secret -= 1
                    if not check_secret:
                        return False
            return True
        else:
            return False

    return check
tom = create_account("Tom", "Qwerty1_", ["1", "word"])
check1 = tom("Qwerty1_",  ["1", "word"])
check2 = tom("Qwerty1_",  ["word"])
check3 = tom("Qwerty1_",  ["word", "2"])
check4 = tom("Qwerty1!",  ["word", "12"])

