def studying_hours(a):
    max_length = 1
    stack =1
    for i in range (1,len(a)):
        if a[i - 1] <= a[i]:
            stack +=1
        else:
            if stack > max_length:
                max_length = stack
            stack = 1

    return max_length


print(studying_hours([10, 100, 111, 1, 2]))