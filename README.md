
# ReShelved - Book Sorting Game
# This is Wyatt Zantua's 1st Python project!

Working on this game through Python was actually very fulfilling, as I could combine/test my general programming knowledge of the language along with learn to experiment with a bunch of new kinds of code of new thanks to the features brought by the Pygame library.

Naturally, designing a video game as my first project had me run into a ***lot*** of new challenges that seemed to come out of nowhere -- a staple in game development.

The greatest struggles I faced throughout this project was with the system of graphics that pygame uses, which I had no experience in and had intended to have my book images be easy to move around as well as clearly visualize what order a given list of call numbers was in. Since the position of any surface is normally static, they can more easily be adjusted by placing *rectangles* over the surface and moving them around specific points on it. I spent a good period of the project timeframe just tinkering around with my book graphics' rectangles trying to find an intuitive way of moving the books around and would constantly run into different roadblocks involving these rectangles, often causing me to change how I wanted the primary gameplay to work. 

Initially, I planned for any given book that the player interacted with to be able to move follow the mouse anywhere, and when the player let go of their MOUSE 1 button, the book would automatically be organized into the closest position on the shelf it was let go from. However, because I used a series of if statements that went in a set order (book 1, then book 2, etc.) to check if a player was interacting with each book on the shelve, any overlapping books would prioritize moving whichever book was observed to be "picked up first" instead of which book was already being grabbed. In addition to this problem, because each surface is placed onto the display one at a time in a given frame, I found early on that books that were loaded later in the code would *always* cover ones loaded before if they were overlapped, making it much harder to come up with a moving mechanic where whatever book the player picked up could be moved around freely and show above all other images. 

To solve the visual glitch, I had to create a seperate list that marked whether a book was currently being interacted with by the mouse, and ensure that this book was loaded onto the screen **after** all the others. At the same time, making a seperate "grabbed" variable actually solved my overlap problem when moving a book, as I could now write an if statement that *first* checks if a grabbed book was still being interacted and continue moving that book, only using the predetermined list of books if no book was currrently being grabbed. 

This design choice also came in handy to easily implement a couple other features in my game, such as switching the position of a grabbed book and an adjacent one if the player lets go of the grabbed book as it collides with another book, which I found to be a much more consistent way of moving the book sprites around compared to my original idea of automatically correcting a book's desired position. Through these experiences of working around strange and alien-like problems, I learned that being flexible and creative with my code could actually lead to solutions that are much easier to implement than what I had initially planned and fix a variety of unexpected obstacles along the way! 


Even with no prior skills in making games with Python, I've been able to further a lot of my general coding skills and the problem-solving process I use to try to bring my concepts to life in my program.
I. . .
- Make things neater (used my own functions more)
- Check for problems systematically
- Predict issues in advance

Plus, I was able to get familiar with a bunch of cool modules that can easily create other kinds of games I'm interesting in thanks the tutorials that have taught me pygame! The process of making games as a whole was actually really fun; I particularly enjoyed making my own custom art for the sprites and playing around with the "physics" I made for the game to see what sliding motions of the books felt the most fluid. I would love to make more games in the future to just to get the chance to personalize my program like this, and really valued this project as a chance to explore this specific medium of game development through a language I have just learned from this class!
