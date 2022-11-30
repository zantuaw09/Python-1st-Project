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

    # ***To Do***: MUST MAKE SORTING FUNCTION FOR CALL NUMBERS!!!



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

book3 = pygame.image.load('graphics/placeholder.png').convert()
book3_rect = book3.get_rect(topleft = (365, 125))
title3 = call_n()

book4 = pygame.image.load('graphics/placeholder.png').convert()
book4_rect = book4.get_rect(topleft = (485, 125))
title4 = call_n()

book5 = pygame.image.load('graphics/placeholder.png').convert()
book5_rect = book5.get_rect(topleft = (605, 125))
title5 = call_n()



order = [title1, title2, title3, title4, title5]


text_font = pygame.font.Font('fonts/kongtext.ttf', 30)
call1 = text_font.render(order[0], False, 'red')
call2 = text_font.render(order[1], False, 'blue')
call3 = text_font.render(order[2], False, 'gold')





### GAMEPLAY LOOP ###


while True:

    mouse_pos = pygame.mouse.get_pos()
    clicks = pygame.mouse.get_pressed()
    grabbed = []
    
    for event in pygame.event.get():

        book_list = [book1, book2, book3]
        rect_list = [book1_rect, book2_rect, book3_rect]
        call_list = [call1, call2, call3]
        
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
                        screen.blit(grabbed[2], (150, 30))
                        
                        difference = mouse_pos[0] - grabbed[1].x
                        grabbed[1].x = event.pos[0] - difference


                        
                        for rect in rect_list:
                            if grabbed[1].colliderect(rect) and rect != grabbed[1]:
                                
                                collision_tolerence = 10
                                
                                if abs(rect.left - grabbed[1].right) < 10:
                                    grabbed[1].x = rect.x - 100
                                    break

                                elif abs(rect.right - grabbed[1].left) < 10:
                                    grabbed[1].x = rect.x + 100
                                    break

                                """
                                if rect.x > grabbed[1].x:
                                    grabbed[1].x = rect.x - 100
                                    break

                                elif rect.x < grabbed[1].x:
                                    grabbed[1].x = rect.x + 100
                                    break
                                """
                            

            else:        
                if book1_rect.collidepoint(event.pos):
                    screen.blit(call1, (150, 30))

                    if clicks[0] is True:
                        difference = mouse_pos[0] - book1_rect.x
                        book1_rect.x = event.pos[0] - difference

                        grabbed = [book1, book1_rect, call1]


                elif book2_rect.collidepoint(event.pos):
                    screen.blit(call2, (150, 30))
                    
                    
                    if clicks[0] is True:
                        difference = mouse_pos[0] - book2_rect.x
                        book2_rect.x = event.pos[0] - difference

                        grabbed = [book2, book2_rect, call2]


                elif book3_rect.collidepoint(event.pos):
                    screen.blit(call3, (150, 30))

                    if clicks[0] is True:
                        difference = mouse_pos[0] - book3_rect.x
                        book3_rect.x = event.pos[0] - difference

                        grabbed = [book3, book3_rect, call3]


        
        for rect in rect_list:
                if event.type == pygame.MOUSEBUTTONUP and rect.collidepoint(mouse_pos):
                    
                    if book1_rect.colliderect(rect) and rect != book1_rect:
                        rect.x, book1_rect.x = book1_rect.x, rect.x
                       

                    elif book2_rect.colliderect(rect) and rect != book2_rect:
                        rect.x, book2_rect.x = book2_rect.x, rect.x


                    elif book3_rect.colliderect(rect) and rect != book3_rect:
                        rect.x, book3_rect.x = book3_rect.x, rect.x



                """
            

            elif book4_rect.collidepoint(event.pos) and clicks[0] is True:
                difference = mouse_pos[0] - book4_rect.x
                book4_rect.x = event.pos[0] - difference

                for rect in rect_list:
                    if book4_rect.colliderect(rect) and rect != book4_rect:
                        if rect.x < book4_rect.x and book4_rect.x < 525:           # moving LEFT
                            rect.x = book4_rect.x + 100

                        elif rect.x > book4_rect.x and book4_rect.x > 225:           # moving RIGHT
                            rect.x = book4_rect.x - 100



            elif book5_rect.collidepoint(event.pos) and clicks[0] is True:
                difference = mouse_pos[0] - book5_rect.x
                book5_rect.x = event.pos[0] - difference

                for rect in rect_list:
                    if book5_rect.colliderect(rect) and rect != book5_rect:
                        if rect.x < book5_rect.x and book5_rect.x < 525:           # moving LEFT
                            rect.x = book5_rect.x + 100

                        elif rect.x > book5_rect.x and book5_rect.x > 225:           # moving RIGHT
                            rect.x = book5_rect.x - 100
                """

        
        
        for book, rect in zip(book_list, rect_list):
            if rect.x < 125:
                rect.x = 125

            elif rect.x > 625:
                rect.x = 625
        
            screen.blit(book, rect)
        
        if clicks[0] is True and grabbed != []:
            screen.blit(grabbed[0], grabbed[1])
             

    

    pygame.display.update()
    clock.tick(60)

    # https://www.youtube.com/watch?v=AY9MnQ4x3zk, 1:13:46 !!



