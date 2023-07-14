def double_string(data):
    data_set = set(data)
    counter = 0
    for i in range(0,len(data)):
        for j in data_set:

            if data[i] + j in data:
                counter +=1

    return counter


data = ['aa', 'aaaa', 'aaaaaaaa', 'aaaa', 'qwer', 'qwerqwert']
print(double_string(data))