import random
import string


import pygame
from sys import exit


class Book(pygame.sprite.Sprite):
    def __init__(self, picture_path):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()


pygame.init()
screen = pygame.display.set_mode([1000, 600])
pygame.display.set_caption("ReShelved")

clock = pygame.time.Clock()


### FUNCTIONS OF THE GAME: ###

def r_letter():
    alphabet = list(string.ascii_uppercase)
    i = random.randint(0, 25)
    return alphabet[i]
    

def call_n():

    let1 = r_letter() + r_letter()
    num1 = str(random.randint(1,999))
    let2 = r_letter() + r_letter()
    num2 = str(random.randint(1,999))
    return let1 + ' ' + num1 + ' ' + let2 + ' ' + num2


def sort_calls(shelf):  # USE BUBBLE SORT!
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
    print('Answer:', in_order)  
    return in_order


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
"""
NOTE: This special Library of Congress call number sorting function was adapted from a bubble sort algorithm.
It ensures that the first set of numbers sort regularly based on value, but the second set by DECIMAL.
This means that a book with 'AB 1 CD 100' goes BEFORE 'AB 1 CD 2' since .100 < .2
To better showcase this, use the EXAMPLE p_order list of call numbers.
"""

### SURFACES: ###



bg = pygame.Surface((1000, 600))
bg.fill('white')


shelf = pygame.image.load('graphics/shelf.png').convert()
shelf_rect = shelf.get_rect(topleft = (100, 100))



#book1 = Book('graphics/redbook.png')

book1 = pygame.image.load('graphics/redbook.png').convert()
book1_rect = book1.get_rect(topleft = (125, 125))
title1 = call_n()

book2 = pygame.image.load('graphics/bluebook.png').convert()
book2_rect = book2.get_rect(topleft = (245, 125))
title2 = call_n()

book3 = pygame.image.load('graphics/orangebook.png').convert()
book3_rect = book3.get_rect(topleft = (365, 125))
title3 = call_n()

book4 = pygame.image.load('graphics/greenbook.png').convert()
book4_rect = book4.get_rect(topleft = (485, 125))
title4 = call_n()

book5 = pygame.image.load('graphics/purplebook.png').convert()
book5_rect = book5.get_rect(topleft = (605, 125))
title5 = call_n()

# EXAMPLE call number order listed below to showcase the sort_calls() function:
# p_order = ['DF 486 RT 9', 'DF 486 RT 562', 'DG 486 RT 880', 'DG 50 RT 99', 'DE 119 RZ 899']

start_order = [title1, title2, title3, title4, title5]


text_font = pygame.font.Font('fonts/kongtext.ttf', 30)
call1 = text_font.render(start_order[0], False, 'red')
call2 = text_font.render(start_order[1], False, 'blue')
call3 = text_font.render(start_order[2], False, 'orange')
call4 = text_font.render(start_order[3], False, 'green')
call5 = text_font.render(start_order[4], False, 'purple')

answer_list = sort_calls(start_order)
grabbed = []

player_list = [title1, title2, title3, title4, title5]



### GAMEPLAY LOOP ###


while True:

    mouse_pos = pygame.mouse.get_pos()
    clicks = pygame.mouse.get_pressed()

    
    for event in pygame.event.get():

        book_list = [book1, book2, book3, book4, book5]
        rect_list = [book1_rect, book2_rect, book3_rect, book4_rect, book5_rect]

        
        screen.blit(bg, (0, 0))
        screen.blit(shelf, shelf_rect)
        
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.MOUSEMOTION:

            if grabbed != []:

                if grabbed[1].collidepoint(event.pos):
                    screen.blit(grabbed[2], (150, 30))

                    if clicks[0] is True:
            
                        difference = mouse_pos[0] - grabbed[1].x
                        if difference > 5:
                            grabbed[1].x = event.pos[0] - difference

                        book_collide()
                        

            else:        
                if book1_rect.collidepoint(event.pos):
                    screen.blit(call1, (150, 30))

                    if clicks[0] is True:
                        difference = mouse_pos[0] - book1_rect.x
                        if difference > 5:
                            book1_rect.x = event.pos[0] - difference

                        grabbed = [book1, book1_rect, call1, player_list.index(title1)]

                        book_collide()   
                         

                elif book2_rect.collidepoint(event.pos):
                    screen.blit(call2, (150, 30))
                    
                    if clicks[0] is True:
                        difference = mouse_pos[0] - book2_rect.x
                        if difference > 5:
                            book2_rect.x = event.pos[0] - difference

                        grabbed = [book2, book2_rect, call2, player_list.index(title2)]

                        book_collide()      
                               
                                
    
                elif book3_rect.collidepoint(event.pos):
                    screen.blit(call3, (150, 30))

                    if clicks[0] is True:
                        difference = mouse_pos[0] - book3_rect.x
                        if difference > 5:
                            book3_rect.x = event.pos[0] - difference

                        grabbed = [book3, book3_rect, call3, player_list.index(title3)]

                        book_collide()      
                                                       

                elif book4_rect.collidepoint(event.pos):
                    screen.blit(call4, (150, 30))

                    if clicks[0] is True:
                        difference = mouse_pos[0] - book4_rect.x
                        if difference > 5:
                            book4_rect.x = event.pos[0] - difference

                        grabbed = [book4, book4_rect, call4, player_list.index(title4)]

                        book_collide()     
                         


                elif book5_rect.collidepoint(event.pos):
                    screen.blit(call5, (150, 30))

                    if clicks[0] is True:
                        difference = mouse_pos[0] - book5_rect.x
                        if difference > 5:
                            book5_rect.x = event.pos[0] - difference

                        grabbed = [book5, book5_rect, call5, player_list.index(title5)]

                        book_collide()      
                         


                                
        
        for call, rect in zip(start_order, rect_list):
            if event.type == pygame.MOUSEBUTTONUP and rect.collidepoint(mouse_pos) and grabbed != []:

                if grabbed[1].colliderect(rect) and rect != grabbed[1]:
                    
                    
                    rect.x, grabbed[1].x = grabbed[1].x, rect.x

                    i = player_list.index(call)
                    j = grabbed[3]
                    
                    player_list[i], player_list[j] = player_list[j], player_list[i]

                    print(player_list)

                grabbed = []
                
        
        
        for book, rect in zip(book_list, rect_list):
            if rect.left < 125:
                rect.left = 125

            elif rect.right > 725:
                rect.right = 725
        
            screen.blit(book, rect)
        
        if clicks[0] is True and grabbed != []:
            screen.blit(grabbed[0], grabbed[1])
             

    

    pygame.display.update()
    clock.tick(60)




