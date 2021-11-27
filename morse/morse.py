from playsound import playsound
from morsedict import dictionary
def dash():
    playsound("dash.wav")
def dot():
    playsound("dot.wav")
def space():
    playsound("space.wav")
def conv(symb):
    if symb == "-":
        dash()
    elif symb == ".":
        dot()

class Morse:
    def __init__(self, word):
        self.word = word

    def sound(self):
        x = self.word
        while x:
            letter = x[0]
            if (letter in dictionary.keys()):
                ditanddah = [symb for symb in dictionary[letter]] #list of dot and dashes
                for symb in ditanddah:
                    conv(symb)
                    space()
                space()
                x = x[1:]
            else:
                print("Error: unrecognized character " + "'" + letter + "'")
                break

inp = input("Your message is: ").lower()
xs = inp.split()
while xs:
    temp = Morse(xs[0])
    temp.sound()
    xs.pop(0)