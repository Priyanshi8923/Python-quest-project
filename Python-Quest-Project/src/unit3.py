# Unit 3 - Loops
from helpers import ask

def play(name, score):
    print("\nLEVEL 3: Loops")
    
    q1 = "Which loop runs until the condition becomes False?"
    opt1 = ["for", "while", "do-while", "switch"]
    ans1 = 2
    exp1 = "while loop checks condition every time before running"
    score = score + ask(q1, opt1, ans1, exp1)
    
    q2 = "What does 'break' keyword do in a loop?"
    opt2 = ["Skip iteration", "Exit loop", "Restart loop", "Pause loop"]
    ans2 = 2
    exp2 = "break keyword immediately exits the loop"
    score = score + ask(q2, opt2, ans2, exp2)
    
    q3 = "Which loop is used to iterate over a sequence?"
    opt3 = ["while", "for", "if", "switch"]
    ans3 = 2
    exp3 = "for loop is used to iterate over list, string, tuple etc"
    score = score + ask(q3, opt3, ans3, exp3)
    
    return score