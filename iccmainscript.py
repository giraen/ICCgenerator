from generatorscript import icc_generator as gen

print("Welcome to ICC Generator!")

try:
    chars = input("\nPlease input all the valid letters and numbers: ")
    icclength = int(input("\nPlease input the required length of the ICC: "))
    print("\n\nYour randomly generated ICC is: " + gen(chars, icclength))

except ValueError:
    print("Please only enter a number for your length.")
