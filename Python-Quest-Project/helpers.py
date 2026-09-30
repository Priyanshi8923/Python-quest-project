# helper file
def header():
    print("")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(" PYTHON QUEST GAME ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def hud(n, s, r):
    print("")
    print("--------------------------------")
    print("Name:", n)
    print("Score:", s) 
    print("Room:", r)
    print("--------------------------------")

def ask(q, opt, ans, exp):
    t = 0
    while True:
        t = t + 1
        print("")
        print(q)
        x = 0
        while x < len(opt):
            print(x+1, ".", opt[x])
            x = x + 1
        c = input("Your answer: ")
        if c.isdigit():
            c = int(c)
            if c == ans:
                print("Correct!")
                print(exp)
                if t == 1:
                    return 50
                else:
                    return 25
            else:
                print("Wrong. Try again")
        else:
            print("Enter only number")