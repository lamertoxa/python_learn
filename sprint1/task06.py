def order(a):
    for i in range (1,len(a)):
        if a[i - 1] > a[i]:
            continue
        else:
            break
    else:
        return "descending"
    for i in range (1,len(a)):
        if a[i - 1] < a[i]:
            continue
        else:
            break
    else:
        return "ascending"

    return "not sorted"

print(order([6, 20, 160, 420]))

