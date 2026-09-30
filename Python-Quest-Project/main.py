# main file
import src.unit1 as u1
import src.unit2 as u2
import src.unit3 as u3
import src.unit4 as u4
import src.unit5 as u5
from helpers import header, hud

name = input("Enter your name: ")
score = 0

header()
score = u1.play(name, score)
score = u2.play(name, score)
score = u3.play(name, score)
score = u4.play(name, score)
score = u5.play(name, score)

hud(name, score, "FINISH")
print("\nGAME OVER! Final Score:", score, "/750")
percent = (score / 750) * 100
print("Percentage:", round(percent, 2), "%")