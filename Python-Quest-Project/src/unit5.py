# Unit 5 - File Handling
from helpers import ask

def play(name, score):
    print("\nLEVEL 5: File Handling")
    
    q1 = "Which mode is used to read a file in Python?"
    opt1 = ["w", "a", "r", "x"]
    ans1 = 3
    exp1 = "r mode is used for reading files"
    score = score + ask(q1, opt1, ans1, exp1)
    
    q2 = "Which function is used to open a file?"
    opt2 = ["file()", "open()", "read()", "load()"]
    ans2 = 2
    exp2 = "open() function is used to open files"
    score = score + ask(q2, opt2, ans2, exp2)
    
    q3 = "Which mode creates a new file if it does not exist?"
    opt3 = ["r", "w", "a", "rw"]
    ans3 = 2
    exp3 = "w mode creates file if it does not exist"
    score = score + ask(q3, opt3, ans3, exp3)
    
    return score