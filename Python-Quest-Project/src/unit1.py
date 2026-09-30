# Unit 1 - Python Basics
from helpers import ask

def play(name, score):
    print("\nLEVEL 1: Python Basics")
    
    q1 = "Which keyword is used to define a function in Python?"
    opt1 = ["def", "function", "fun", "define"]
    ans1 = 1
    exp1 = "def keyword is used to create a function in Python"
    score = score + ask(q1, opt1, ans1, exp1)
    
    q2 = "Which symbol is used for comments in Python?"
    opt2 = ["//", "#", "/*", "<!--"]
    ans2 = 2
    exp2 = "# symbol is used for single line comments"
    score = score + ask(q2, opt2, ans2, exp2)
    
    q3 = "What is the output of: print(type(5))"
    opt3 = ["<class 'int'>", "<class 'float'>", "<class 'str'>", "Error"]
    ans3 = 1
    exp3 = "5 is an integer, so type is int"
    score = score + ask(q3, opt3, ans3, exp3)
    
    return score