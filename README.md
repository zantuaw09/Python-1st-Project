# This is Wyatt Zantua's 1st Python project!

Working on this game through Python was actually very fulfilling, as I could combine/test my general programming knowledge of the language along with learn to experiment with a bunch of new kinds of code of new thanks to the features brought by the Pygame library.

Naturally, designing a video game as my first project had me run into a ***lot*** of new problems that seemed to come out of nowhere -- a staple in game development.


The greatest struggles I faced throughout this project was with the system of graphics that pygame uses, which I had no experience in and had intended to design unique gameplay where my book images could be easy to move around as well as clearly visualize what order a given list of call numbers was in. Since the position of any surface is normally static, they can more easily be adjusted by placing *rectangles* over the surface and moving them around specific points on it. I spent a good period of the project timeframe just tinkering around with my book graphics' rectangles trying to create an intuitive way of moving the books around and would constantly run into different roadblocks involving these rectangles throughout development. 

One 

In another example, because each image is placed onto the display one at a time in a given frame, I found early on that books that were loaded later in the code would *always* cover ones loaded before if they were overlapped, making it much harder to come up with a moving mechanic where whatever book the player picked up could be moved around freely and show above all other images. To solve this visual glitch, I had to create a seperate list that marked whether a book was currently being interacted with by the mouse, and ensure that this book was loaded onto the screen **after** all the others. This one design choice of making a "grabbed" variable actually came in handy to easily implement other features in my game, such as switching the position of a grabbed book and an adjacent one if the player lets go of the grabbed book as it collides with another book.
