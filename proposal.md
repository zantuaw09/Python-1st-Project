# Proposal

## What will (likely) be the title of your project?

ReShelved - A Speed Sorting Game

## In just a sentence or two, summarize your project. (E.g., "A website that lets you buy and sell stocks.")

An informative game that involves quickly reorganizing library books based on their call numbers, akin to educational typing games. Since I've been working at Charles Library ever since I got here at Temple, I think having a way to learn this skill is pretty valuable to use any library effectively.

## In a paragraph or more, detail your project. What will your software do? What features will it have? How will it be executed?

My software will be a game in which a list of "books" will be displayed with their unique CALL NUMBERS -- the labels used by libraries to organize shelves based on subject -- and has the player move around the books in an attempt to place the list in the correct order. The program will mainly be able to randomly generate a list of possible call numbers according to the rules of the Library of Congress classification. Ideally, I should be able to use pygame to display several sprites of books with these call numbers that can be reorganized in a line and checked to see if it matches the proper sequence. I am planning to generally include a list of 10 call numbers per game, but if possible, I could increase the difficulty by adding more books to the list. I also want to implement some simple button functions such as replays, submits, and the visual shifting of the books across the list.


## If planning to combine 1051's final project with another course's final project, with which other course? And which aspect(s) of your proposed project would relate to 1051, and which aspect(s) would relate to the other course?

Not planning on double-dipping final projects with other courses.

## If planning to collaborate with 1 or 2 classmates for the final project, list their names, email addresses, and the names of their assigned TAs below.

N/A (planning on working alone)

## In the world of software, most everything takes longer to implement than you expect. And so it's not uncommon to accomplish less in a fixed amount of time than you hope.

### In a sentence (or list of features), define a GOOD outcome for your final project. I.e., what WILL you accomplish no matter what?

- Function that sorts a list of strings based on Library of Congress call number system (must implement rules!)
- Randomly generate valid book call numbers in mixed order and _display call numbers_ 
- Allow player to directly change order of books/call numbers in list
- Check accuracy of player's input for a shelf to a correctly sorted list using **INDICIES**

### In a sentence (or list of features), define a BETTER outcome for your final project. I.e., what do you THINK you can accomplish before the final project's deadline?

- ***USING PYGAME***, develop moveable graphics of physical books with call numbers, allowing for visual reorganization on-screen
- Design timer to track how fast books were reorganized
- Implement basic buttons needed to progress game, like check results and replay game

### In a sentence (or list of features), define a BEST outcome for your final project. I.e., what do you HOPE to accomplish before the final project's deadline?

- Add fluid "physics" of book sprite movements; i.e., books realistically *shift* when a book is placed in a new spot
- Add possible difficulty settings (number of shelves and books)
- Create unique graphics that make recognizing each distinct book easier

## In a paragraph or more, outline your next steps. What new skills will you need to acquire? What topics will you need to research? If working with one of two classmates, who will do what?

Much of my next steps will involve learning more about the different 'pygame' modules and how I might be able to apply its interface for designing sprites and other graphics for my game. Since my ideal/"BETTER outcome" goal is to correspond these visuals to a proper list that can be checked by my program, I will need to review different applications made by pygame or any other options I might have for creating interactive graphics. ***I do not yet know how reasonable it will be to develop drag-and-drop graphics in pygame yet, so I may need to come up with an alternative way for players to PHYSICALLY REORGANIZE the list of books; this might include implementing keyboard inputs that allow the player to select a book and shift the shelf using the arrow keys.*** As I explore these possibilities, I must also begin to develop a concise *function* in Python itself that will correctly sort valid call numbers, a crucial component to my concept even if my vision for the game/tool slightly changes over time. This will allow for a list of randomly generated call numbers to be given to the mixed up and create the basic gameplay of trying to move around the items into a proper order.
