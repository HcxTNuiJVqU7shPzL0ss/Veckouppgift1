#####################################################################
# Jan Berglund - exc3_1a.py
#
# Veckouppgift 1
# Vecka 2, 8/1
# 3 Använda variabler och datatyper
# 1a
#####################################################################


# --------------------------------------------
# 1a Använd input för att be användaren om ett heltal.
# Spara värdet i en variabel.
# Omvandla variabelns värde till ett heltal,
# och skriv ut det för att testa om du har gjort rätt.

# Initial information to the user, 1a
print("\nThis is 1a, where you will be asked to enter an integer")
input("Press Enter to continue!\n")

# Ask for and save an integer in a variable
# Throw ValueError if incorrect input (not an integer), then try again
# Made as a function to be able to reuse in "1b" as a separate file
def userint_1a():
    while True:
        try:
            user_int = int(input("Please type an integer, then press enter: "))
            return user_int
            break
        except ValueError:
            print("\nNot an integer, please try again!\n")

user_int = userint_1a()
print("\nYour selected integer was:", user_int)

# End this exercise
input("\nPress Enter to finish!")
print("This is the end of 1a, thank you for playing!")
