# This is Wyatt Zantua's 1st Python project!

Working on this game through Python was actually very fulfilling, as I could combine/test my general programming knowledge of the language along with learn to experiment with a bunch of new kinds of code of new thanks to the features brought by the Pygame library.

Naturally, designing a video game as my first project had me run into a ***lot*** of new problems that seemed to come out of nowhere -- a staple in game development.


One great example of a constant struggle was with making dynamic graphics for my game. . .  **(to be continued)**
I spent a good period of the project timeframe just tinkering around with my book graphics' rectangles trying to create an intuitive way of moving the books around while constantly running into roadblocks because of how image rectangles work in pygame. Because each image is placed onto the display one at a time in a given frame, books that were loaded later would *always* cover ones loaded before if they were overlapped, making it much harder to come up with a moving mechanic where whatever book the player picked up could be moved around freely and show above all other images. To solve this visual glitch, I had to create a seperate list that marked whether a book was currently being interacted with by the mouse, and ensure that this book was loaded onto the screen **after** all the others.
