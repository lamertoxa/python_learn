def check_odd_even(num):
    try:
        if num%2==0:
            return "Entered number is even"
        else:
            return "Entered number is odd"
    except TypeError:
        return  "You entered not a number."
