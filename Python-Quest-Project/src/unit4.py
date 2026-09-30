# Unit 4 - Functions
from helpers import ask

def play(name, score):
    print("\nLEVEL 4: Functions")
    
    q1 = "What does 'return' keyword do in a function?"
    opt1 = ["Stops program", "Sends value back", "Prints value", "Creates loop"]
    ans1 = 2
    exp1 = "return sends a value back to the function caller"
    score = score + ask(q1, opt1, ans1, exp1)
    
    q2 = "How do you call a function named 'myfunc'?"
    opt2 = ["call myfunc", "myfunc()", "function myfunc", "def myfunc"]
    ans2 = 2
    exp2 = "We call function by writing function name with ()"
    score = score + ask(q2, opt2, ans2, exp2)
    
    q3 = "What is a parameter in a function?"
    opt3 = ["Return value", "Variable inside function", "Input to function", "Function name"]
    ans3 = 3
    exp3 = "Parameters are inputs passed to a function"
    score = score + ask(q3, opt3, ans3, exp3)
    
    return score