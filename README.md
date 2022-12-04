# This is Wyatt Zantua's 1st Python project!

Working on this game through Python was actually very fulfilling, as I could combine/test my general programming knowledge of the language along with learn to experiment with a bunch of new kinds of code of new thanks to the features brought by the Pygame library.

Naturally, designing a video game as my first project had me run into a ***lot*** of new problems that seemed to come out of nowhere -- a staple in game development.


The greatest struggles I faced throughout this project was with the system of graphics that pygame uses, which I had no experience in and had intended to have my book images be easy to move around as well as clearly visualize what order a given list of call numbers was in. Since the position of any surface is normally static, they can more easily be adjusted by placing *rectangles* over the surface and moving them around specific points on it. I spent a good period of the project timeframe just tinkering around with my book graphics' rectangles trying to find an intuitive way of moving the books around and would constantly run into different roadblocks involving these rectangles, often causing me to change how I wanted the primary gameplay to work. 

Initially, I planned for any given book that the player interacted with to be able to move follow the mouse anywhere, and when the player let go of their MOUSE 1 button, the book would automatically be organized into the closest position on the shelf it was let go from. However, because I used a series of if statements that went in a set order (book 1, then book 2, etc.) to check if a player was interacting with each book on the shelve, any overlapping books would prioritize moving whichever book was observed to be "picked up first" instead of which book was already being grabbed. In addition to this problem, because each surface is placed onto the display one at a time in a given frame, I found early on that books that were loaded later in the code would *always* cover ones loaded before if they were overlapped, making it much harder to come up with a moving mechanic where whatever book the player picked up could be moved around freely and show above all other images. 

To solve the visual glitch, I had to create a seperate list that marked whether a book was currently being interacted with by the mouse, and ensure that this book was loaded onto the screen **after** all the others. At the same time, making a seperate "grabbed" variable actually solved my overlap problem when moving a book, as I could now write an if statement that *first* checks if a grabbed book was still being interacted and continue moving that book, only using the predetermined list of books if no book was currrently being grabbed. 

This design choice also came in handy to easily implement a couple other features in my game, such as switching the position of a grabbed book and an adjacent one if the player lets go of the grabbed book as it collides with another book. Through this, I learned that being flexible and creative with my possible problem-solving efforts could actually lead to solutions that work a lot better that what I had initially planned and fix a variety of unexpected problems along the way!
