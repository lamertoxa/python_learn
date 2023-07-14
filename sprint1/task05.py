# print(toPostFixExpression(["(","(", "(",  "1","+","2",")","*","3",")","+","6",")","/","(","2", "+","3",")"]))
#
# 1 2 + 3* 6 + 2 3 +/
def toPostFixExpression(e):
    output = []
    stack = []
    priority ={
        "-":0,
        "+":0,
        "*":2,
        "/":1,
        "%":1
    }

    def stack_out(index):
        output.append(stack[index])
        stack.pop(index)

    for item in e:
        if item.isnumeric():
            output.append(item)
        elif item in "-+*/%":

            for i in range (len(stack)-1,-1,-1):
                if stack[i] in "()":
                    continue
                if priority[item] < priority[stack[i]]:
                    for j in range (len(stack)-1,-1,-1):
                        if stack[j] in "()":
                            break
                        stack_out(j)
            stack.append(item)

        elif item == "(":
            stack.append(item)
        elif item == ")":
            for i in range(len(stack)-1,-1,-1):
                if stack[i] in "(":
                    stack.pop(i)
                    break

                stack_out(i)
    while len(stack) !=0:
        for i in range(len(stack) - 1, -1, -1):
            stack_out(i)
    return output

print(toPostFixExpression(["20",
                           "+",
                           "3",
                           "*",
                           "(",
                           "5",
                           "*",
                           "4",
                           ")"]))

# print(toPostFixExpression(["(","(", "(",  "1","+","2",")","*","3",")","+","6",")","/","(","2", "+","3",")"]))