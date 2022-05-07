def star_pattern_1(x):
    for i in range(x):
        for j in range(i):
            print("* ", end="")
        print()

def star_pattern_2(x):
    space = ""
    word = ""

    for i in range(x+1):
        for j in range(i):
            space = "  " * int(x-i)
            word = "* " * i
        print(space + word)

def star_pattern_3(x):
    for i in reversed(range(x)):
        for j in range(i):
            print("* ", end="")
        print()

def star_pattern_4(x):
    space = ""
    word = ""

    for i in reversed(range(x)):
        for j in range(i):
            space = "  " * int(x-i)
            word = "* " * i
        print(space + word)

