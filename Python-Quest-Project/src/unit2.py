# Unit 2 - Data Types
from helpers import ask

def play(name, score):
    print("\nLEVEL 2: Data Types")
    
    q1 = "Which of these is a mutable data type in Python?"
    opt1 = ["tuple", "string", "list", "int"]
    ans1 = 3
    exp1 = "List is mutable, we can change its elements"
    score = score + ask(q1, opt1, ans1, exp1)
    
    q2 = "What is the data type of: x = [1, 2, 3]"
    opt2 = ["tuple", "list", "set", "dict"]
    ans2 = 2
    exp2 = "Square brackets [] represent a list"
    score = score + ask(q2, opt2, ans2, exp2)
    
    q3 = "Which method is used to add element to a list?"
    opt3 = ["add()", "push()", "append()", "insert()"]
    ans3 = 3
    exp3 = "append() method adds element at the end of list"
    score = score + ask(q3, opt3, ans3, exp3)
    
    return score