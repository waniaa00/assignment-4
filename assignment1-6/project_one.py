# MAD LIBS GAME

def mad_libs():
  print("Welcome to the Mad Libs game!")

mad_libs()
name = input("Enter a name:")
language = input("Enter a programming language: ")
software_house = input("Enter the name of a software house: ")


story = (
    f"""
    Once upon time, there was a programmer named {name}.
    {name} loved coding in {language} and dreamt of creating the next big game.
    One day, {name} got a job at {software_house}, where they workes on an amazing new game.
    The game became a huge success, and {name} became a legandary game developer!

    """
  )

print("\n Here is your Mad Libs story:")
print(story)
print("\n Thanks for playing!")



