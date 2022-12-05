import random
import string


import pygame
from sys import exit


pygame.init()
screen = pygame.display.set_mode([1000, 600])
pygame.display.set_caption("ReShelved")

clock = pygame.time.Clock()


### FUNCTIONS USED IN THE GAME: ###

def r_letter():
    alphabet = list(string.ascii_uppercase)
    i = random.randint(0, 25)
    return alphabet[i]
    

def easy_call_n():
    let1 = r_letter() + r_letter()
    num1 = str(random.randint(1,999))
    let2 = r_letter() + r_letter()
    num2 = str(random.randint(1,999))
    return let1 + ' ' + num1 + ' ' + let2 + ' ' + num2

def call_n(first_l):
    let1 = first_l + r_letter()
    num1 = str(random.randint(1,999))
    let2 = r_letter() + r_letter()
    num2 = str(random.randint(1,999))
    return let1 + ' ' + num1 + ' ' + let2 + ' ' + num2


def sort_calls(shelf):  # USES BUBBLE SORT!
    in_order = []
    for book in shelf:
        call = book.split(' ')
        in_order.append(call)
    in_order.sort()
    
    n = len(shelf)

    for i in range(n - 1):
        for j in range(n - i - 1):
            current_l = in_order[j][0]
            current_n = int(in_order[j][1])

            next_l = in_order[j + 1][0]
            next_n = int(in_order[j + 1][1])
            
            if current_l == next_l and current_n > next_n:
                in_order[j], in_order[j + 1] = in_order[j + 1], in_order[j]

    final = []
    for x in in_order:
        item = ''

        for piece in x:
            item += str(piece) + ' '

        item = item.strip()
        final.append(item)
    return final
"""
NOTE: This sort_calls() function that organizes Library of Congress call number was adapted from a bubble sort algorithm.
It ensures that the first set of numbers sort regularly based on value, but the second set by DECIMAL.
This means that a book with 'AB 1 CD 100' goes BEFORE 'AB 1 CD 2' since .100 < .2
To better showcase this, use some of the EXAMPLE start_order list of call numbers.
"""


def book_collide():
    global rect_list
    global grabbed
    
    for rect in rect_list:
        if grabbed[1].colliderect(rect) and rect != grabbed[1]:
                                
            collision_tolerance = 100
                            
            if abs(rect.right - grabbed[1].left) <= collision_tolerance:
                grabbed[1].x = rect.x + 95
                break

            elif abs(rect.left - grabbed[1].right) <= collision_tolerance:
                grabbed[1].x = rect.x - 95
                break
    
    return grabbed[1].x


### SURFACES: ###

bg = pygame.Surface((1000, 600))
bg.fill('white')


shelf = pygame.image.load('graphics/shelf.png').convert()
shelf_rect = shelf.get_rect(topleft = (100, 100))


book1 = pygame.image.load('graphics/redbook.png').convert()
book1_rect = book1.get_rect(topleft = (125, 125))

book2 = pygame.image.load('graphics/bluebook.png').convert()
book2_rect = book2.get_rect(topleft = (245, 125))

book3 = pygame.image.load('graphics/orangebook.png').convert()
book3_rect = book3.get_rect(topleft = (365, 125))

book4 = pygame.image.load('graphics/greenbook.png').convert()
book4_rect = book4.get_rect(topleft = (485, 125))

book5 = pygame.image.load('graphics/purplebook.png').convert()
book5_rect = book5.get_rect(topleft = (605, 125))




check = pygame.image.load('graphics/check.png').convert()
check_rect = check.get_rect(topleft = (825, 200))

checkHover = pygame.image.load('graphics/check_hover.png').convert()
checkHover_rect = checkHover.get_rect(topleft = (825, 200))

checkPress = pygame.image.load('graphics/check_pressed.png').convert()
checkPress_rect = checkPress.get_rect(topleft = (825, 200))



"""EXAMPLE call number order and starting player list can be used below to showcase the sort_calls() function:"""
#start_order = ['DE 119 RZ 899', 'DF 486 RT 9', 'DF 486 RT 562', 'DG 486 RT 880', 'DG 50 RT 99']
#title1, title2, title3, title4, title5 = 'DE 119 RZ 899', 'DF 486 RT 9', 'DF 486 RT 562', 'DG 486 RT 880', 'DG 50 RT 99'

#start_order = ['TF 33 TJ 456', 'TE 34 TI 43', 'TF 4 TT 444', 'TE 34 TI 333', 'TF 33 TJ 5']
#title1, title2, title3, title4, title5 = 'TF 33 TJ 456', 'TE 34 TI 43', 'TF 4 TT 444', 'TE 34 TI 333', 'TF 33 TJ 5'



text_font = pygame.font.Font('fonts/kongtext.ttf', 30)
score_font = pygame.font.Font('fonts/kongtext.ttf', 50)


#player_list = [title1, title2, title3, title4, title5]
grabbed = []


book_list = [book1, book2, book3, book4, book5]
rect_list = [book1_rect, book2_rect, book3_rect, book4_rect, book5_rect]


game_active = True
new_game = True


### GAMEPLAY LOOP ###


while True:

    mouse_pos = pygame.mouse.get_pos()
    clicks = pygame.mouse.get_pressed()

    screen.blit(bg, (0, 0))
    screen.blit(shelf, shelf_rect)


    if new_game:

        x = 125
        for rect in rect_list:
            rect.x = x
            x += 120
        
        gen_line = r_letter()
        title1 = call_n(gen_line)
        title2 = call_n(gen_line)
        title3 = call_n(gen_line)
        title4 = call_n(gen_line)
        title5 = call_n(gen_line)

        start_order = [title1, title2, title3, title4, title5]
        color_order = ['red', 'blue', 'orange', 'green', 'purple']

        call1 = text_font.render(start_order[0], False, 'red')
        call2 = text_font.render(start_order[1], False, 'blue')
        call3 = text_font.render(start_order[2], False, 'orange')
        call4 = text_font.render(start_order[3], False, 'green')
        call5 = text_font.render(start_order[4], False, 'purple')

        player_list = [title1, title2, title3, title4, title5]
        answer_list = sort_calls(start_order)

        new_game = False

    
    if game_active:
        
            
        for event in pygame.event.get():
                        
            
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            if event.type == pygame.MOUSEMOTION:


                # Prioritize mouse movement of book currently "grabbed"
                if grabbed != []:

                    if grabbed[1].collidepoint(event.pos):

                        if clicks[0] is True:
                
                            difference = mouse_pos[0] - grabbed[1].x
                            if difference > 5:
                                grabbed[1].x = event.pos[0] - difference

                            book_collide()
                            
                # Check each book for movement of a new "grabbed" object
                else:        
                    if book1_rect.collidepoint(event.pos):

                        if clicks[0] is True:
                            difference = mouse_pos[0] - book1_rect.x
                            if difference > 5:
                                book1_rect.x = event.pos[0] - difference

                            grabbed = [book1, book1_rect, call1, player_list.index(title1)]

                            book_collide()   
                             

                    elif book2_rect.collidepoint(event.pos):
                        
                        if clicks[0] is True:
                            difference = mouse_pos[0] - book2_rect.x
                            if difference > 5:
                                book2_rect.x = event.pos[0] - difference

                            grabbed = [book2, book2_rect, call2, player_list.index(title2)]

                            book_collide()      
                                   
                                    
        
                    elif book3_rect.collidepoint(event.pos):

                        if clicks[0] is True:
                            difference = mouse_pos[0] - book3_rect.x
                            if difference > 5:
                                book3_rect.x = event.pos[0] - difference

                            grabbed = [book3, book3_rect, call3, player_list.index(title3)]

                            book_collide()      
                                                           

                    elif book4_rect.collidepoint(event.pos):

                        if clicks[0] is True:
                            difference = mouse_pos[0] - book4_rect.x
                            if difference > 5:
                                book4_rect.x = event.pos[0] - difference

                            grabbed = [book4, book4_rect, call4, player_list.index(title4)]

                            book_collide()     
                             


                    elif book5_rect.collidepoint(event.pos):
                        
                        if clicks[0] is True:
                            difference = mouse_pos[0] - book5_rect.x
                            if difference > 5:
                                book5_rect.x = event.pos[0] - difference

                            grabbed = [book5, book5_rect, call5, player_list.index(title5)]

                            book_collide()      
                             


                                    
            # Results of book collision (switches rectangle position and order of "player_list")
            for call, rect in zip(start_order, rect_list):
                if event.type == pygame.MOUSEBUTTONUP and rect.collidepoint(mouse_pos) and grabbed != []:

                    if grabbed[1].colliderect(rect) and rect != grabbed[1]:
                        
                        
                        rect.x, grabbed[1].x = grabbed[1].x, rect.x

                        i = player_list.index(call)
                        j = grabbed[3]
                        
                        player_list[i], player_list[j] = player_list[j], player_list[i]
                        print(player_list)
                    grabbed = []
                    

        # Display call numbers
        for rect, number, color in zip(rect_list, start_order, color_order):
            if rect.collidepoint(mouse_pos):
                call = text_font.render(number, True, color)
                screen.blit(call, (150, 30))
                break

        # Create shelf boundaries and display books
        for book, rect in zip(book_list, rect_list):
            if rect.left < 125:
                rect.left = 125

            elif rect.right > 725:
                rect.right = 725
        
            screen.blit(book, rect)
        
        if clicks[0] is True and grabbed != []:
            screen.blit(grabbed[0], grabbed[1])
             


        # Button to submit answers
        screen.blit(check, check_rect)

        if check_rect.collidepoint(mouse_pos):
            screen.blit(checkHover, checkHover_rect)

            if clicks[0] is True:
                screen.blit(checkPress, checkPress_rect)

            if event.type == pygame.MOUSEBUTTONUP and check_rect.collidepoint(mouse_pos):
                game_active = False





    ### RESULTS PAGE ###
                
    else:
        new_game = False
        for book, rect in zip(book_list, rect_list):
            screen.blit(book, rect)

        
        # Calculate and display score
        correct = pygame.image.load('graphics/correct.png').convert()
        incorrect = pygame.image.load('graphics/incorrect.png').convert()

        score = 0
        x = 150
        
        for i in range(len(player_list)):
            if player_list[i] == answer_list[i]:
                score += 1
                screen.blit(correct, (x, 525))

            else:
                screen.blit(incorrect, (x, 525))
            x += 125

        results = score_font.render(str(score) + '/5', False, 'black')
        screen.blit(results, (800, 200))


        # Display call numbers
        for rect, number, color in zip(rect_list, start_order, color_order):
            if rect.collidepoint(mouse_pos):
                call = text_font.render(number, True, color)
                screen.blit(call, (150, 30))
                break


        # Replay button
        replay = pygame.image.load('graphics/replay.png').convert()
        replay_rect = replay.get_rect(topleft = (825, 300))

        replayHover = pygame.image.load('graphics/replay_hover.png').convert()
        replayHover_rect = checkHover.get_rect(topleft = (825, 300))

        replayPress = pygame.image.load('graphics/replay_pressed.png').convert()
        replayPress_rect = checkPress.get_rect(topleft = (825, 300))

        screen.blit(replay, replay_rect)
        if replay_rect.collidepoint(mouse_pos):
            screen.blit(replayHover, replayHover_rect)

            if clicks[0] is True:
                screen.blit(replayPress, replayPress_rect)

            if replay_rect.collidepoint(mouse_pos) and clicks[0] is True:
                new_game = True
                game_active = True

        
        for event in pygame.event.get():
                        
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
    pygame.display.update()
    clock.tick(60)




