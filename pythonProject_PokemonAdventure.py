import random
import time
import pythonProject_Art


class CatchPokemon:
    def __init__(self):
        self.wildPokemon = {"cave": ["Sandshrew", "Zubat", "Paras", "Diglett", "Geodude", "Magnemite", "Onix", "Hitmonlee", "Hitmonchan",
                            "Koffing", "Rhyhorn", "Electabuzz", "Magmar", "Omanyte", "Kabuto", "Aerodactyl", "Kangaskhan", "Jynx", "Machop"],
                            "beach": ["Squirtle", "Poliwag", "Tentacool", "Slowpoke", "Seal", "Shellder", "Krabby", "Horsea", "Goldeen", "Staryu", "Magikarp", "Lapras", "Dratini", "Psyduck", "Eevee", "Spearow", "Mr. Mime", "Jigglypuff"],
                            "forest": ["Bulbasaur", "Caterpie", "Weedle", "Pidgey", "Rattata", "Ekans", "Pikachu", "Oddish", "Venonat", "Meowth", "Bellsprout", "Farfetch'd", "Doduo", "Exeggcute", "Chansey", "Tangela", "Scyther", "Pinsir", "Snorlax"],
                            "ruins": ["Clefairy", "Vulpix", "Growlithe", "Abra", "Ponyta", "Charmander", "Grimer", "Gastly", "Drowzee", "Voltorb", "Cubone", "Porygon", "Tauros", "Lickitung", "Ditto", "Nidoran", "Mankey"]}
        self.playerPokemon = []
        self.player = [{
            "# of pokeballs": 5}, {"# of berries": 5}]
        self.pokemonItemRocketChance = random.randint(1, 10)
        self.pokemonCatchChance = random.randint(1, 10)
        self.pokemonCaught = "n"
        self.location = "beach"
        self.stayHere = "y"
        self.randomPokemon = random.choice(self.wildPokemon[self.location])
        self.counter = 1
        self.tryAgain = "y"
        self.cueEnding = False

    def menu(self):
        print("****************************************")
        print("                Main Menu")
        print("****************************************")
        print("What would you like to do?")
        print(
            """
    1. Look for a Pokemon
    2. Check your Pokedex and inventory
    3. Quit
        """)

    def catchMenu(self):
        print("""
        1. Throw a Pokeball
        2. Throw a berry
        3. Run
            """)

    def mapMenu(self):
        print("****************************************")
        print("Where would you like to go Pokemon hunting?")
        print(
            """
    1. A cave
    2. The beach
    3. A forest
    4. The ruins
    5. Return to top menu
        """)

    def pokedexAndInventory(self):
        if self.playerPokemon == []:
            print(
                "It looks like you haven't caught any Pokemon yet! Get out there and catch 'em all!")
        else:
            print("These are the Pokemon you have caught so far:")
            for pokemon in self.playerPokemon:
                print(pokemon)
        time.sleep(2)
        print(
            f"There are still lots of Pokemon left in the wild!")
        time.sleep(2)
        print(
            f"You have {self.player[0]['# of pokeballs']} Pokeballs and {self.player[1]['# of berries']} berries left.\n")

    def pokemonEncounter(self):
        self.randomPokemon = random.choice(self.wildPokemon[self.location])
        print(f"A wild {self.randomPokemon} appeared!")
        time.sleep(2)
        print("What do you want to do?")
        time.sleep(2)

    def throwPokeballOrBerry(self):
        while self.pokemonCaught == "n":
            self.catchMenu()
            choice = input("")
            if choice == "1":
                self.throwPokeball()
            elif choice == "2":
                self.throwBerry()
                choice = input("")
                if choice == "1":
                    self.throwPokeball()
                else:
                    self.run()
                    self.pokemonCaught = "y"
            else:
                self.run()
                self.pokemonCaught = "y"

    def atLocation(self):
        while self.stayHere == "y":
            if self.pokemonItemRocketChance == 1:
                self.rocketEncounter()

            elif self.pokemonItemRocketChance <= 3:
                self.itemEncounter()

            else:
                self.pokemonCaught = "n"
                self.pokemonEncounter()
                self.throwPokeballOrBerry()

            if (self.player[0]['# of pokeballs'] == 0) or self.cueEnding == True:
                break

            search = input(
                f"Do you want to search for another Pokemon in the {self.location}? Type y or n. \n")
            if search == "y":
                self.pokemonItemRocketChance = random.randint(1, 10)
                self.stayHere == "y"
                print("****************************************")
            else:
                print(f"You decide to leave the {self.location}.")
                time.sleep(2)
                self.location = ""
                self.stayHere = "n"

    def throwPokeball(self):
        print("****************************************")
        if self.player[0]['# of pokeballs'] > 0:
            print(
                f"You throw a Pokeball at the wild {self.randomPokemon}.")
            self.player[0]['# of pokeballs'] -= 1
            time.sleep(1)
            print("The ball shakes once...")
            time.sleep(1)
            if self.pokemonCatchChance == 1:
                self.pokemonBreaksOut()
            else:
                print("Twice...")
                time.sleep(2)
                if self.pokemonCatchChance <= 3:
                    self.pokemonBreaksOut()
                else:
                    print("Three times...")
                    time.sleep(2)
                    if self.pokemonCatchChance == 4:
                        self.pokemonBreaksOut()
                    else:
                        print(
                            f"Good job! {self.randomPokemon} was caught!\n")
                        self.playerPokemon.append(self.randomPokemon)
                        self.wildPokemon[self.location].remove(
                            self.randomPokemon)
                        time.sleep(1)
                        print(
                            f"You have {self.player[0]['# of pokeballs']} Pokeballs left. \n")
                        self.pokemonItemRocketChance = random.randint(
                            1, 10)
                        self.pokemonCatchChance = random.randint(1, 10)
                        self.randomPokemon = random.choice(
                            self.wildPokemon[self.location])
                        if self.player[0]['# of pokeballs'] == 0:
                            print("It looks like you're out of Pokeballs!")
                            time.sleep(2)
                            self.pokemonCaught = "y"
                            self.cueEnding = True
                        else:
                            self.pokemonCaught = "y"
        else:
            print("It looks like you're out of Pokeballs!")
            time.sleep(2)
            self.pokemonCaught = "y"
            self.cueEnding = True

    def pokemonBreaksOut(self):
        print(
            f"Oh no! The wild {self.randomPokemon} broke out of the Pokeball!")
        time.sleep(1)
        if self.player[0]['# of pokeballs'] == 0:
            print("Oh no! It looks like you're out of Pokeballs!\n")
            time.sleep(1)
            self.pokemonCaught = "y"
            self.cueEnding = True
        else:
            print(
                f"You have {self.player[0]['# of pokeballs']} Pokeballs left. \n")
            time.sleep(1)
            print("What do you want to do?")
            self.pokemonCatchChance = random.randint(1, 10)

    def throwBerry(self):
        print("****************************************")
        if self.player[1]['# of berries'] > 0:
            self.player[1]['# of berries'] -= 1
            print(
                f"You throw a berry at the wild {self.randomPokemon}.")
            time.sleep(1)
            print(f"You have {self.player[1]['# of berries']} berries left.")
            self.pokemonCatchChance += 2
            time.sleep(2)
            print(
                f"The wild {self.randomPokemon} eats it, eying you cautiously the whole time.")
            time.sleep(2)
            print(
                f"The wild {self.randomPokemon} looks a little happier -- maybe it will be easier to catch!")
            time.sleep(3)
            print("Would you like to throw another Pokeball or run away?")
            time.sleep(2)
            print("""
        1. Throw a Pokeball
        2. Run
            """)
        else:
            print("Oh no! It looks like you don't have any berries to throw.")
            time.sleep(1)
            print("Would you like to throw a Pokeball or run away?")
            time.sleep(2)
            print("""
        1. Throw a Pokeball
        2. Run
            """)

    def rocketEncounter(self):
        print("Two figures drop down in front of you.")
        time.sleep(1)
        print("'...Where did they come from?' you wonder.")
        time.sleep(1)
        print("Wait... Oh no! It's Team Rocket!")
        time.sleep(2)
        if self.playerPokemon != []:
            print("They cackle at you, then one of their Pokemon releases a smokescreen.")
            time.sleep(2)
            print(
                f"When the smokescreen clears, you notice one of your Pokeballs is missing! They've stolen {self.playerPokemon[0]}!")
            time.sleep(3)
            stolenPokemon = self.playerPokemon.pop(0)
            self.wildPokemon["forest"].append(stolenPokemon)
            self.pokemonItemRocketChance = random.randint(1, 10)
            if self.counter == 1:
                print("*ring ring ring*")
                time.sleep(2)
                print("Someone is calling you!")
                time.sleep(3)
                print(f"   Hello, Trainer {name}? This is Professor Jaye.")
                time.sleep(2)
                print(
                    "   I see you've just had an encounter with that terrible Team Rocket.")
                time.sleep(3)
                print("   Don't worry!")
                time.sleep(2)
                print(
                    "   If they steal a Pokemon from you, you can still catch it again in the forest.")
                time.sleep(3)
                print("   Good luck!")
                time.sleep(1)
                print("*click*")
                time.sleep(2)
            self.counter = 2
            print("****************************************")
        else:
            print("They cackle at you, then notice that you don't have any Pokemon.")
            time.sleep(2)
            print(
                "   Ha! How pathetic. This wannabe trainer doesn't even have a Pokemon to call their own!")
            time.sleep(2)
            print("They turn and run into the distance.")
            time.sleep(2)
            print(
                "   Hopefully the next time we see you you'll be worth robbing. Team Rocket, out! \n")
            time.sleep(2)
            self.pokemonItemRocketChance = random.randint(1, 10)

    def itemEncounter(self):
        itemFound = random.randint(1, 2)
        numItems = random.randint(2, 3)
        if itemFound == 1:
            print("You find something buried by a rock.")
            time.sleep(2)
            print(f"You uncover {numItems} Pokeballs!")
            self.player[0]['# of pokeballs'] += numItems
            time.sleep(2)
            print(
                f"You now have {self.player[0]['# of pokeballs']} Pokeballs.\n")
            time.sleep(2)
            self.pokemonItemRocketChance = random.randint(1, 10)
        else:
            print("You stumble upon a berry bush.")
            time.sleep(2)
            print(f"You collect {numItems} berries!")
            self.player[1]['# of berries'] += numItems
            time.sleep(2)
            print(f"You now have {self.player[1]['# of berries']} berries.\n")
            time.sleep(2)
            self.pokemonItemRocketChance = random.randint(1, 10)

    def run(self):
        print("****************************************")
        print(
            f"You decide not to catch the wild {self.randomPokemon}. \n")
        self.randomPokemon = random.choice(self.wildPokemon[self.location])

    def ending(self):
        if self.playerPokemon == []:
            print("Thanks for playing! Have a good day!")
        else:
            print("*ring ring ring*")
            time.sleep(2)
            print("Professor Jaye is calling you!")
            time.sleep(2)
            print(f"   Great job, Trainer {name}!")
            time.sleep(2)
            if self.player[0]['# of pokeballs'] <= 0:
                print(
                    "   It looks like you're out of Pokeballs, so your adventure is at an end.")
                time.sleep(2)
            print(
                f"   You were able to catch {len(userCatchPokemon.playerPokemon)} Pokemon!")
            time.sleep(2)
            print("   Thank you for your help with my research.")
            time.sleep(2)
            print("   I couldn't have done it without you!")
            time.sleep(2)
            print("*click*")
            time.sleep(1)


userCatchPokemon = CatchPokemon()
stillPlaying = "y"

print(pythonProject_Art.logo)
print("***********************************************************************")
print("   Hello there!")
time.sleep(2)
print("   Welcome to the world of Pokemon!")
time.sleep(2)
print("   My name is Jaye.")
time.sleep(2)
print("   People call me the Pokemon Prof!")
time.sleep(2)
print("   I study Pokemon for a living.")
time.sleep(2)
name = input("   What might your name be? \n")
print(f"   Welcome to your Pokemon adventure, Trainer {name}!")
time.sleep(2)
print("   Please help me with my research and catch as many Pokemon as you can!")
time.sleep(3)
print("   But be careful, Team Rocket has been seen in the area.")
time.sleep(2)
print(
    f"   Good luck on your adventure, Trainer {name}! I can't wait to see what exciting Pokemon you catch!")
time.sleep(3)
print("Professor Jaye gives you 5 Pokeballs and 5 berries to start your journey.")
time.sleep(3)
print("You leave Professor Jaye's lab. Adventure awaits! \n")
time.sleep(2)
while (stillPlaying == "y"):
    time.sleep(2)
    userCatchPokemon.tryAgain == "y"
    userCatchPokemon.menu()
    choice = input("")
    if choice == "1":
        while (userCatchPokemon.tryAgain == "y") and userCatchPokemon.cueEnding == False:
            userCatchPokemon.mapMenu()
            mapChoice = input("")
            if mapChoice == "1":
                userCatchPokemon.location = "cave"
                if len(userCatchPokemon.wildPokemon["cave"]) == 0:
                    print(
                        "Oh! It looks like there are no more Pokemon to catch in the cave. You should try somewhere else!")
                    time.sleep(2)
                else:
                    userCatchPokemon.stayHere = "y"
                    print("****************************************")
                    print(pythonProject_Art.cave)
                    time.sleep(1)
                    print("Armed with a flashlight, you walk into a dark cave.")
                    time.sleep(2)
                    userCatchPokemon.atLocation()
            elif mapChoice == "2":
                userCatchPokemon.location = "beach"
                if len(userCatchPokemon.wildPokemon["beach"]) == 0:
                    print(
                        "Oh! It looks like there are no more Pokemon to catch at the beach. You should try somewhere else!")
                    time.sleep(2)
                else:
                    userCatchPokemon.stayHere = "y"
                    print("****************************************")
                    print(pythonProject_Art.beach)
                    time.sleep(1)
                    print("You grab a hat and some sunscreen and head to the beach.")
                    time.sleep(2)
                    userCatchPokemon.atLocation()
            elif mapChoice == "3":
                userCatchPokemon.location = "forest"
                if len(userCatchPokemon.wildPokemon["forest"]) == 0:
                    print(
                        "Oh! It looks like there are no more Pokemon to catch in the forest. You should try somewhere else!")
                    time.sleep(2)
                else:
                    userCatchPokemon.stayHere = "y"
                    print("****************************************")
                    print(pythonProject_Art.forest)
                    time.sleep(1)
                    print(
                        "You go to run into the forest, then run back and grab your bugspray.")
                    time.sleep(2)
                    userCatchPokemon.atLocation()
            elif mapChoice == "4":
                userCatchPokemon.location = "ruins"
                if len(userCatchPokemon.wildPokemon["ruins"]) == 0:
                    print(
                        "Oh! It looks like there are no more Pokemon to catch in the ruins. You should try somewhere else!")
                    time.sleep(2)
                else:
                    userCatchPokemon.stayHere = "y"
                    print("****************************************")
                    print(pythonProject_Art.ruins)
                    time.sleep(1)
                    print(
                        "You grab an extra pair of underwear before heading into the ruins.")
                    time.sleep(2)
                    userCatchPokemon.atLocation()
            elif mapChoice == "5":
                break
            else:
                print("I'm sorry, please enter a valid number.")
    elif choice == "2":
        userCatchPokemon.pokedexAndInventory()
    elif choice == "3":
        userCatchPokemon.ending()
        stillPlaying = "n"
    else:
        print("I'm sorry, please choose a valid option.\n")

    if (userCatchPokemon.player[0]['# of pokeballs'] <= 0) or userCatchPokemon.cueEnding == True:
        userCatchPokemon.ending()
        stillPlaying = "n"
