# Test file to check if all modules are working
import src.unit1 as u1
import src.unit2 as u2
import src.unit3 as u3
import src.unit4 as u4
import src.unit5 as u5
from helpers import header, hud

print("TESTING ALL MODULES...")
header()
print("Module import: SUCCESS")
print("If you see header above, setup is correct")
hud("TestUser", 0, "TEST")
print("TEST COMPLETE")