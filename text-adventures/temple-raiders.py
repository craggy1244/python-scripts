import os
from colorama import Fore, Back, Style

NL_2 = "\n\n"
game_over = False
hint_count = 0


def printText(text, color, end="\n\n"):
    print(color, end="")
    print(text, end=end)
    print(Style.RESET_ALL, end="")


def invalidInput():
    printText("Invalid Input", Fore.RED)


def gameOver():
    global game_over
    print(Fore.RED, end="")
    print("GAME OVER")
    print(Style.RESET_ALL)
    game_over = True


os.system('cls')

print()
print(Fore.GREEN + Back.LIGHTBLACK_EX + Style.DIM + "Temple Raiders")
print(Style.RESET_ALL)


while game_over is not True:
    printText("You're stood at the entrance of the ancient temple ruins. " +
              "Two large mossy stone slabs block your path!", Fore.CYAN)

    print("What should you do next?", end=NL_2)
    print("  [A] Try to prise open the two stone slabs.")
    print("  [B] Look around the area for useful items.")
    print("  [C] GIVE UP AND GO HOME!", end=NL_2)
    choice = input(" > ").upper()
    print()

    if choice == "A":
        printText("You're a strong guy but these rocks ain't movin'!", Fore.YELLOW)

    elif choice == "B":
        while game_over is not True:
            printText("You found a robust looking tree branch!", Fore.CYAN)

            print("What do you want to do?")
            print("  [A] Use the tree branch to prise open the stone entrance.")
            print("  [B] Discard the item.", end=NL_2)
            choice = input(" > ").upper()
            print()

            if choice == "A":

                printText("The tree branch worked a treet :)", Fore.YELLOW)

                while game_over is not True:

                    printText("You're in a dark passage. " +
                              "You appear to have stepped on a skeleton!", Fore.CYAN)

                    print("What should you do next?", end=NL_2)
                    print("  [A] Ignore it and slowly advance down the passage.")
                    print("  [B] Examine the skeleton.", end=NL_2)
                    choice = input(" > ").upper()
                    print()

                    if choice == "A":
                        printText("Argh .. " +
                                  "You fall down a huge pit and impail " +
                                  "yourself at the bottom on iron spikes! " +
                                  "Ouch.", Fore.YELLOW)

                        gameOver()

                    elif choice == "B":
                        printText("Seems this guy wasn't as lucky as you. " +
                                  "You find a torch in his utility belt. " +
                                  "It works!", Fore.YELLOW)

                        while game_over is not True:

                            printText("You shine the torch down the passage. " +
                                      "It's lucky you did! " +
                                      "A huge pit lays before you, " +
                                      "leading to certain death!", Fore.CYAN)

                            print("What should you do next?", end=NL_2)
                            print("  [A] Jump in the pit.")
                            print("  [B] Attempt to jump over the pit.")
                            print("  [C] Look for another option.", end=NL_2)

                            choice = input(" > ").upper()
                            print()

                            if choice == "A":
                                printText(
                                    "You fall to your death.", Fore.YELLOW)
                                gameOver()

                            elif choice == "B":
                                printText("You take your best run and jump. " + "Your arms reach the other side but " +
                                          "you badly wind yourself against the pit " +
                                          "and fall back to your untimely death.", Fore.YELLOW)
                                gameOver()

                            elif choice == "C":
                                printText(
                                    "You spot a rope dangling above the pit.", Fore.YELLOW)

                                while game_over is not True:

                                    printText("You think you could reach it with a jump " +
                                              "and swing to the other side.", Fore.CYAN)

                                    print("What do you want to do?", end=NL_2)
                                    print("  [A] Make a jump for the rope.")
                                    print(
                                        "  [B] Attempt to jump over the pit.")
                                    print(Fore.MAGENTA + Style.BRIGHT, end="")
                                    print("  [H] USE A HINT." +
                                          Style.RESET_ALL, end=NL_2)

                                    choice = input(" > ").upper()
                                    print()

                                    if choice == "H":
                                        hint_count = hint_count + 1
                                        print(Fore.MAGENTA +
                                              Style.BRIGHT, end="")
                                        print(
                                            "HINT: Last year you won Ninja Warrior.", end=" ")
                                        print(
                                            "Your speciality was the ropes.", end=NL_2)
                                        print(Style.RESET_ALL)
                                    else:
                                        invalidInput()
                            else:
                                invalidInput()

                    else:
                        invalidInput()

            elif choice == "B":
                printText("You throw the branch into " +
                          "the forest and alert a hungry bear!", Fore.YELLOW)
                gameOver()
            else:
                invalidInput()

    elif choice == "C":
        printText("Like all the other quitters before you, " +
                  "you pack up and go home.", Fore.YELLOW)
        gameOver()

    else:
        invalidInput()
