from generatorscript import icc_generator as gen

print("Welcome to ICC Generator!")
print("\nThis will generate a random string divided by dashes (-)")
print("\nFor example: 12AB-34CD-56EF")

# Error handling if user inputted characters instead of numbers in icclength and replong
try:
    chars = input("\nPlease input all the valid letters and numbers: ")
    icclength = int(input("\nPlease input the required length of the ICC: "))
    replong = int(input("\nHow long should your ICC: "))

    # Prints the user's ICC by calling the function
    print("\n\nYour randomly generated ICC is: " + gen(chars, icclength, replong))

except ValueError:
    # Prints an error message if user inputted anything aside from number in icclength and replong
    print("Please only enter a number for the last two questions.")
