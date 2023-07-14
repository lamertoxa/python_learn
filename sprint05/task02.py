import cmath
def solve_quadric_equation(a, b, c):
    try:
        d = (b ** 2) - 4 * a * c

        x1, x2 = complex((-b + d ** (0.5)) / (2 * a)), complex((-b - d ** (0.5)) / (2 * a))
    except ZeroDivisionError:
        return "Zero Division Error"
    except TypeError:
        return "Could not convert string to float"
    return f"The solution are x1={x2} and x2={x1}"


print(solve_quadric_equation(1, 3, -4))