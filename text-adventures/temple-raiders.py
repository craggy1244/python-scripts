import os
from colorama import Fore, Back, Style

NL_1 = "\n"
NL_2 = "\n\n"
game_over = False
hint_count = 0


def printText(text, color=Fore.WHITE, end=NL_2):
    print(color, end="")
    print(text, end=end)
    print(Style.RESET_ALL, end="")


def inputChoice(prompt, options, includeHint=False):
    printText(prompt)
    letters = ["A", "B", "C"]
    num_of_options = len(options)
    for i in range(0, num_of_options):
        letter = letters[i]
        option = options[i]
        print("  [" + letter + "] " + option)
    if includeHint is True:
        printText("  [H] USE A HINT", Fore.MAGENTA + Style.BRIGHT, end=NL_1)
    print()
    choice = input(" > ").upper()
    print()
    return choice


def invalidInput():
    printText("Invalid Input", Fore.RED)


def useHint(hintText):
    global hint_count
    hint_count = hint_count + 1
    printText(hintText, Fore.MAGENTA + Style.BRIGHT)


def gameOver():
    global game_over
    print(Fore.WHITE + Back.RED + "GAME OVER" + Style.RESET_ALL)
    game_over = True


os.system('cls')

print()
print(Fore.GREEN + Back.LIGHTBLACK_EX + Style.BRIGHT + "TEMPLE RAIDERS")
print(Style.RESET_ALL)


while game_over is not True:
    printText("You're stood at the entrance of an ancient temple ruins. "
              "Two large mossy stone slabs block your path!", Fore.CYAN)

    choice = inputChoice("What should you do next?", [
        "Try to prise open the two stone slabs.",
        "Look around the area for useful items.",
        "GIVE UP AND GO HOME!"])

    if choice == "A":
        printText("You're a strong guy but these rocks ain't movin'!", Fore.YELLOW)

    elif choice == "B":
        while game_over is not True:
            printText("You found a robust looking tree branch!", Fore.CYAN)

            choice = inputChoice("What do you want to do?", [
                "Use the tree branch to prise open the stone entrance.",
                "Discard the item."
            ])

            if choice == "A":

                printText("The tree branch worked a treet :)", Fore.YELLOW)

                while game_over is not True:

                    printText("You're in a dark passage. " +
                              "You appear to have stepped on a skeleton!", Fore.CYAN)

                    choice = inputChoice("What should you do next?", [
                        "Ignore it and slowly advance down the passage.",
                        "Examine the skeleton."
                    ])

                    if choice == "A":
                        printText("Argh .. "
                                  "You fall down a huge pit and impail "
                                  "yourself at the bottom on iron spikes! "
                                  "Ouch.", Fore.YELLOW)

                        gameOver()

                    elif choice == "B":
                        printText("Seems this guy wasn't as lucky as you. "
                                  "You find a torch in his utility belt. "
                                  "It works!", Fore.YELLOW)

                        while game_over is not True:

                            printText("You shine the torch down the passage. "
                                      "It's lucky you did! "
                                      "A huge pit lays before you, "
                                      "leading to certain death!", Fore.CYAN)

                            choice = inputChoice("What should you do next?", [
                                "Jump in the pit.",
                                "Attempt to jump over the pit.",
                                "Look for another option."
                            ])

                            if choice == "A":
                                printText(
                                    "You fall to your death.", Fore.YELLOW)
                                gameOver()

                            elif choice == "B":
                                printText("You take your best run and jump. "
                                          "Your arms reach the other side but "
                                          "you badly wind yourself against the pit "
                                          "and fall back to your untimely death.", Fore.YELLOW)
                                gameOver()

                            elif choice == "C":
                                printText(
                                    "You spot a rope dangling above the pit.", Fore.YELLOW)

                                while game_over is not True:

                                    printText("You think you could reach it with a jump "
                                              "and swing to the other side.", Fore.CYAN)

                                    choice = inputChoice("What do you want to do?", [
                                        "Make a bold jump for the rope.",
                                        "Attempt to jump over the pit."
                                    ], True)

                                    if choice == "A":
                                        printText(
                                            "You swing across the deadly pit with style!", Fore.YELLOW)

                                        while game_over is not True:
                                            printText("You turn a corner and enter the inner sanctum. "
                                                      "Ahead of you, there is a golden chalice "
                                                      "lit by two beams of sunlight. "
                                                      "Between you and the prize is a floor of numbered tiles. ",
                                                      Fore.CYAN)
                                            choice = inputChoice("What should you do?", [
                                                "Run across the tiles and grab the golden chalice.",
                                                "Step on tiles 1, 2, 5, 8",
                                                "Step on tiles 1, 1, 2, 3, 5, 8"
                                            ], True)

                                            if choice == "A":
                                                printText(
                                                    "You're hit by poisoned arrows and die a painful death!", Fore.YELLOW)
                                                gameOver()

                                            elif choice == "B":
                                                printText("Oops! That was the wrong sequence. "
                                                          "You're hit by poisoned arrows and "
                                                          "die a painful death.", Fore.YELLOW)
                                                gameOver()

                                            elif choice == "C":
                                                printText("You win! You evade the booby traps and "
                                                          "take the golden chalice back to your "
                                                          "museum in London.", Fore.YELLOW)
                                                printText("THE END",
                                                          Fore.GREEN + Back.LIGHTBLACK_EX + Style.BRIGHT, '')
                                                print()
                                                game_over = True

                                            elif choice == "H":
                                                useHint("Inscribed on the chalice is the Phi "
                                                        "symbol (the golden ratio)")

                                    elif choice == "B":
                                        printText("You take your best run and jump. "
                                                  "Your arms reach the other side but "
                                                  "you badly wind yourself against the pit "
                                                  "and fall back to your untimely death.", Fore.YELLOW)
                                        gameOver()

                                    elif choice == "H":
                                        useHint("Last year you won Ninja Warrior. "
                                                "Your speciality was the ropes."
                                                )
                                    else:
                                        invalidInput()
                            else:
                                invalidInput()

                    else:
                        invalidInput()

            elif choice == "B":
                printText("You throw the branch into "
                          "the forest and alert a hungry bear!", Fore.YELLOW)
                gameOver()
            else:
                invalidInput()

    elif choice == "C":
        printText("Like all the other quitters before you, "
                  "you pack up and go home.", Fore.YELLOW)
        gameOver()

    else:
        invalidInput()
