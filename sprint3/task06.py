import random
def randomWord(arg):
    while True:
        if arg == None:
            return None
        current_list = arg[:]
        for i in range(len(arg)):
            rand_word =  random.choice(current_list)
            current_list.remove(rand_word)
            yield rand_word

