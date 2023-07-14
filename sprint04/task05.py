class Gallows:
    def __init__(self):
        self.words = []
        self.game_over = False

    def play(self,word):
        if self.words == [] or (self.words[-1][-1].lower() == word[0].lower() and not word in self.words):
            self.words.append(word)
            return self.words
        else:
            self.game_over = True
            return "game over"
    def restart(self):
        self.game_over = False
        self.words = []
        return "game restarted"

my_gallows = Gallows()
print(my_gallows.game_over)
print(my_gallows.play('apple'))
# print(my_gallows.words)
# print(my_gallows.play('ear'))
# print(my_gallows.play('rhino'))
# print(my_gallows.play('ocelot'))
# print(my_gallows.game_over)
# print(my_gallows.play('oops'))
# print(my_gallows.game_over)
# print(my_gallows.words)