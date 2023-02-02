# Welcome to Your Pokemon Adventure!

The goal of the game is simple -- catch as many Pokemon as you can. You only start off with 5 Pokeballs, but if you're lucky, you can find more while you're adventuring. If your number of Pokeballs reaches 0, the game ends. And be warned -- Team Rocket has been seen in the area! Now get out there and catch 'em all!

Link to Medium article [here](https://medium.com/@jayelonlasseigne/making-a-pokemon-game-using-python-3d56bd020448).

Link to Replit [here](https://replit.com/@lasseignejk/Pokemon-Adventure).

## What I used

This was built as a final project for the Python section of my bootcamp, so Python is the only language used.

**Some of the things used:**

- **A class** -- Used to store all the functions for the game.
- **Dictionaries** -- Used to store the Pokemon available in the game, as well as the number of Pokeballs and berries the player has. For the Pokemon, a dictionary was built with different locations as the keys, and the Pokemon available in those locations were stored in lists as the values. This way, players can go to different locations and find different Pokemon.
- **Lists** -- Used to store the Pokemon by location, as well as to keep track of the Pokemon the player has caught.
- **while loops** -- Used to keep the game going and to keep the player in a certain location if they want to stay there.
- **if/else statements** -- Used for a lot of the menu logic, where a player chooses an item from whichever menu and the game continues based on that choice.
- **Random numbers** -- Used along with the if/else statements for the encounter logic. The random numbers dictated if Pokemon broke out of the Pokeball while the player is trying to catch them, whether their encounter is a Pokemon, Team Rocket, or an item, and which Pokemon shows up in the Pokemon encounter.
- **The sleep function** -- Used to slow the speed of the print statements appearing in the terminal so the player doesn't get overwhelmed with text.

## Some things I learned

I learned a TON from this project. I think one of the biggest things I learned was **I really need to push my code to github more often.** I usually go two hours between pushes, which is too long when you're constantly changing things around.

I also learned to **be careful of what you call your variables.** There were a couple of times where I kept getting an error and it was because one of my variables shared a name with one of my functions. When the code is as long as mine was getting to be, I feel like I need to have a written list of all my different variables and functions I've made.

One thing that is cementing in my brain after completing this project is **the usefulness of classes.** When we were learning about classes in my bootcamp, I asked the instructor why we need classes when we can do most of the same things in dictionaries. With further examples he gave, it became clear why. And now, after doing this project, its crystal clear why. I can't imagine trying to do this project without using a class.

The last big thing I learned was to **stop being stubborn and just look up the error message.** I got so many different error messages at so many different parts in my coding adventure and in the beginning, I would try to decypher the error message myself and guess at what it meant. I'd go to that line in the code and try to figure out what was going on. Without fully understanding what the error meant. So much time wasted. Now, Google is the first place I go when I get an error.

## Looking forward

Right now, I'm pretty happy with my code because, as far as I've tested, it works. That being said, I am looking forward to coming back to this code in the future and finding ways to make it more efficient. I changed so much at a time that I feel like there are probably lines of code doing the same thing as others.

I also would like to redo this project in the future, once I learn some frontend stuff. It would definitely make it nicer for the user if a picture of the Pokemon appeared when you encountered it, and maybe I'll have some ideas on how to make the code more efficient by then too.

Lastly, I think it might be cool to have an option to skip some of the dialogue, for example the beginning dialogue with the Professor explaining what's going on. Not super crucial, but it would be nice if someone wanted to play the game more than once.
