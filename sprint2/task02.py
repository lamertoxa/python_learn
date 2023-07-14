def morse_number(num):
    result = ""
    for digit in num:
        digit = int(digit)
        if digit <6:
            result += "."*digit + "-"*(5-digit)
        elif digit>6 and digit !=0:
            result += "-" * (digit-5) + "." * (5 - (digit-5))
        result +=" "
    return result

print(morse_number("784"))
