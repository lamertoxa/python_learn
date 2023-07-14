def isPalindrome(string):
    str_set = set(string)
    letter_in_middle =False
    for letter in str_set:
        if string.count(str(letter))%2==0:
            continue
        else:
            if letter_in_middle:
                return False
            letter_in_middle = True
    return True
print (isPalindrome("abb"))