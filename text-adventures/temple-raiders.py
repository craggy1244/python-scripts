import os
from colorama import Fore, Back, Style

NL_2 = "\n\n"

os.system('cls')

print()
print(Fore.GREEN + Back.LIGHTBLACK_EX + Style.DIM + "Temple Raiders")
print(Style.RESET_ALL)

game_over = False
hint_count = 0

while game_over is not True:
    print(Fore.CYAN, end="")
    print("You're stood at the entrance of the ancient temple ruins.", end=" ")
    print("Two large mossy stone slabs block your path!")
    print(Style.RESET_ALL)
    print("What should you do next?", end=NL_2)

    print("  [A] Try to prise open the two stone slabs.")
    print("  [B] Look around the area for useful items.")
    print("  [C] GIVE UP AND GO HOME!", end=NL_2)
    choice = input(" > ").upper()
    print()

    if choice == "A":
        print(Fore.YELLOW + "You're a strong guy but these rocks ain't movin'!" +
              Style.RESET_ALL, end=NL_2)
    elif choice == "B":
        while game_over is not True:
            print(Fore.CYAN, end="")
            print("You found a robust looking tree branch!", end=" ")
            print("What do you want to do?")
            print(Style.RESET_ALL)

            print("  [A] Use the tree branch to prise open the stone entrance.")
            print("  [B] Discard the item.", end=NL_2)
            choice = input(" > ").upper()
            print()

            if choice == "A":
                print(Fore.YELLOW + "The tree branch worked a treet :)" +
                      Style.RESET_ALL, end=NL_2)
                while game_over is not True:
                    print(Fore.CYAN, end="")
                    print("You're in a dark passage.", end=" ")
                    print("You appear to have stepped on a skeleton!")
                    print(Style.RESET_ALL)

                    print("What should you do next?", end=NL_2)

                    print("  [A] Ignore it and slowly advance down the passage.")
                    print("  [B] Examine the skeleton.", end=NL_2)
                    choice = input(" > ").upper()
                    print()

                    if choice == "A":
                        print(Fore.YELLOW, end="")
                        print("Argh ..", end=" ")
                        print("You fall down a huge pit and impail", end=" ")
                        print("yourself at the bottom on iron spikes!", end=" ")
                        print("Ouch.", end=NL_2)
                        print(Fore.RED + "GAME OVER" +
                              Style.RESET_ALL, end=NL_2)
                        game_over = True

                    elif choice == "B":
                        print(Fore.YELLOW, end="")
                        print("Seems this guy wasn't as lucky as you.", end=" ")
                        print("You find a torch in his utility belt.", end=" ")
                        print("It works!", end=NL_2)

                        while game_over is not True:

                            print(Fore.CYAN, end="")
                            print("You shine the torch down the passage.", end=" ")
                            print("It's lucky you did!", end=" ")
                            print("A huge pit lays before you,", end=" ")
                            print("leading to certain death!", end=" ")
                            print(
                                "It's a hell of a jump and there's no way around it!")
                            print(Style.RESET_ALL)

                            print("What should you do next?", end=NL_2)
                            print("  [A] Jump in the pit.")
                            print("  [B] Attempt to jump over the pit.")
                            print("  [C] Look for another option.", end=NL_2)

                            choice = input(" > ").upper()
                            print()

                            if choice == "A":
                                print(Fore.YELLOW +
                                      "You fall to your death.", end=NL_2)
                                print(Fore.RED + "GAME OVER" +
                                      Style.RESET_ALL, end=NL_2)
                                game_over = True

                            elif choice == "B":
                                print(Fore.YELLOW)
                                print("You take your best run and jump.", end=" ")
                                print("Your arms reach the other side but", end=" ")
                                print(
                                    "you badly wind yourself against the pit", end=" ")
                                print(
                                    "and fall back to your untimely death.", end=NL_2)
                                print(Fore.RED + "GAME OVER" +
                                      Style.RESET_ALL, end=NL_2)
                                game_over = True

                            elif choice == "C":
                                print(Fore.YELLOW, end="")
                                print(
                                    "You spot a rope dangling above the pit.", end=NL_2)

                                while game_over is not True:

                                    print(Fore.CYAN, end="")
                                    print(
                                        "You think you could reach it with a jump", end=" ")
                                    print("and swing to the other side." +
                                          Style.RESET_ALL, end=NL_2)

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
                                        print("Invalid Input", end=NL_2)
                            else:
                                print("Invalid Input", end=NL_2)

                    else:
                        print("Invalid Input", end=NL_2)

            elif choice == "B":
                print(Fore.YELLOW)
                print("You throw the branch into", end=" ")
                print("the forest and alert a hungry bear!", end=NL_2)
                print(Fore.RED + "GAME OVER" + Style.RESET_ALL, end=NL_2)
                game_over = True

            else:
                print("Invalid Input", end=NL_2)

    elif choice == "C":
        print(Fore.YELLOW + "Like all the other quitters before you, you pack up and go home." +
              Style.RESET_ALL, end=NL_2)
        print(Fore.RED + "GAME OVER" + Style.RESET_ALL, end=NL_2)
        game_over = True

    else:
        print("Invalid input", end=NL_2)
