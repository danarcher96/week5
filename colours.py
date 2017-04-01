COLOURS = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "blue1": "#0000ff", "DarkGreen": "#006400"}


colourChoice = input("Enter colour: ")
while colourChoice != "":
    if colourChoice in COLOURS:
        print(colourChoice, "is", COLOURS[colourChoice])
    else:
        print("Invalid colour")
    colourChoice = input("Enter colour: ")