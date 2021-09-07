"""Repeating a beat in a loop."""

__author__ = "730403482"


# Begin your solution here...
beat: str = (input("What beat do you want to repeat? "))
repetitions: int = int(input("How many times do you want to repeat it? "))
x = 0
output = ""
while repetitions <= 0:
    print("No beat...")

while x < repetitions and repetitions >= 1:
    output = output + beat + " "
    x = x + 1
print(output)