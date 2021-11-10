#!/usr/bin/env python3

# Created by: Matthew Meech
# Created on: Nov 2021
# This program is a Choose your own adventure game


def main():
    # process & output

    # input
    answer = input("Would you like to become a millionaire? (yes/no): ")
    print("")

    # input and output (if... elif... else... )
    if answer == "yes":
        answer = input(
            "\n\nGREAT, well let's get started. First you have to choose from three professions."
            "(thief/adventurer/shopkeeper): "
        )

        if answer == "thief":
            answer = input(
                "\n\nSo you have chosen the life of crime, your first task will be to rob a fine silk store." 
                "would you like to steal mulberry silk, or golden laced silk (mulberry/gold): "
            )

            if answer == "mulberry":
                answer = input(
                    "\n\nyou successfully steal the mulberry due to low security and made $5000. "
                    " Your next heist will be at a fine Ore store called goldstone. "
                    " You have the choice of stealing gold, diamonds, or the mystery vault (gold/diamonds/vault): "
                )

                if answer == "gold":
                    print(
                        "\n\nyou take all the gold and make a run for it, you get away and hide in the garbage suitable place for a thief, "
                        " But this does not change the fact that you just got away with the gold!"
                        " you ended up stealing $10 000 and were too scared to keep stealing with your ending profit of $15 000. | ENDING #1 $15 000 | "
                    )

                elif answer == "diamonds":
                    print(
                        "\n\nyou took the diamonds and ran but tripped over your shoelaces "
                        " fall and die from the impact on the ground | GAME OVER | cause of death SLOTH | "
                    )

                elif answer == "vault":
                    print(
                        "\n\nyou get to the vault and open it with your master lock picking skills. You are surprised to see jadeite, "
                        "one of the most expensive gemstones. You act fast and take the jadeite stones and run out the door. " 
                        " You later find out that the jadeite is worth $500 000 dollars and this encourages you to keep stealing. "
                        " you become a world-class thief stealing millions of dollars every year. | ENDING #2 $505 000 |  "
                    )

                else:
                    print("\n\ninvaild answer you lose!")

            elif answer == "gold":
                print(
                    "\n\nyou got caught stealing the silk due to the high security. | GAME OVER | cause of death GREAD | "
                )

            else:
                print("\n\ninvaild answer you lose!")

        elif answer == "adventurer":
            answer = input(
                "\n\nso you have chosen the life of an explorer, "
                " now you must pick a bounty you have a choice of fighting slime, or a gorilla. (slime/gorilla): "
            )

            if answer == "slime":
                answer = input(
                    "\n\nyou miraculosuoy take down the slime and complete the bounty. " 
                    " You claim $3000 from the bounty and are ready for your next mission. "
                    " for your next mission you have the choice of either finding and killing a group of bandits "
                    "exploring the forbidden forest or trying to take down the legendary BLUE MAMMOTH(forest/bandits/BLUE): "
                )

                if answer == "bandits":
                    print(
                        "\n\nyou sneak up on the group of bandits and go for a takedown on their leader, " 
                        " you fail horribly and get beaten to death by the gang | GAME OVER | cause of death PRIDE | "
                    )

                elif answer == "forest":
                    print(
                        "\n\nyou traverse into the forest and find yourself lost when you stumble upon a big X marks the spot. "
                        " You dig it up and find a chest. You take the chest to your house and open it. Gold, gems, and artifacts "
                        " that could be priceless are what fill the chest. after this, "
                        " you decide to stop while you're ahead and quit being an adventurer | ENDING #3 $??? ??? ??? + $3000 | "
                    )

                elif answer == "BLUE":
                    print(
                        "\n\nyou travel far to the top of the blue mountain where you find a sleeping BLUE MAMMOTH!?!? "
                        " You are about to kill it when all of the sudden you realize how cute it is. " 
                        " You befriend the legendary monster and go on many adventures with it. "
                        " You gain the nickname kaya and become a legendary adventurer | ENDING #4 BLUE MAMMOTH + $3000| "
                    )

                else:
                    print("\n\ninvaild answer you lose!")

            elif answer == "gorilla":
                answer = input(
                    "\n\nyou get overwhelmed by the gorilla and get brutally "
                    " torn and ripped apart. | GAME OVER | cause of death WARTH | "
                )

            else:
                print("\n\ninvalid answer you lose!")

        elif answer == "shopkeeper":
            answer = input(
                "\n\nso you wanna be the wolf of wall street well guess what it isn't that easy. "
                " First, you will choose what you would like to base you shop around, "
                " your options consist of two things ores or being a blacksmith (ores/blacksmith ): "
            )

            if answer == "blacksmith":
                answer = input(
                    "\n\nyou make your new blacksmith shop and instantly get customers. "
                    " Now you are faced with the challenge of selling swords, shields or armor (swords/shields/armor) "
                )

                if answer == "swords":
                    print(
                        "\n\nyou start selling swords and they take off. "
                        " One day you are walking around your shop when one of the swords falls off the wall and... "
                        " startles you which leads to you dying of shock R.I.P | GAME OVER | cause of death you are just a wimp |: "
                    )

                elif answer == "shields":
                    print(
                        "\n\nyou start selling shields and at first it's slow but soon picks up a bit. "
                        " One day you sell a shield to a man/woman named Addison. "
                        " Their shield later saves them in battle and they fall in love with you and become your husband/wife. "
                        " You and your spouse open a new little shop that sells shields named protectors. | ENDING #5 LOVE + $3000 | "
                    )

                elif answer == "armor":
                    answer = input(
                        "\n\nyou stock your shelves with armor which sell super fast due to the high demand of armor in your village. "
                        " you gain enough money to expand into swords and shields as well. "
                        " Your shop becomes world-class and you have "
                        " made yourself a multimillion dollar business. | ENDING #6 Multimillion-dollar business + 3000$ | "
                    )

                else:
                    print("\n\ninvaild answer you lose!")

            elif answer == "ores":
                answer = input(
                    "\n\nyou picked ores but there is a bigger and better ores shop in "
                    " town called goldstone which put you out of business.  | GAME OVER | cause of death COVETOUSNESS | "
                )

            else:
                print("\n\ninvaild answer you lose!")

        else:
            print("\n\ninvalid answer you lose!")

    elif answer == "no":
        print(
            "\nwhy did you even click run I guess money isn't always the answer (easter egg ending #7)"
        )
    else:
        print("\ninvalid answer you lose!")

    print("\nDone.")


if __name__ == "__main__":
    main()
