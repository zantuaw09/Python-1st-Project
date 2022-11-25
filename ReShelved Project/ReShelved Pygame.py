import pygame
from sys import exit


pygame.init()
screen = pygame.display.set_mode([1000, 600])
pygame.display.set_caption("ReShelved")

clock = pygame.time.Clock()


### FUNCTIONS OF THE GAME: ###

def call_n():
    order = []

    # ***To Do***: MUST MAKE SORTING FUNCTION FOR CALL NUMBERS!!!



### SURFACES: ###

bg = pygame.Surface((1000, 600))
bg.fill('white')


shelf = pygame.image.load('graphics/shelf.png').convert()
shelf_rect = shelf.get_rect(topleft = (100, 100))

book1 = pygame.image.load('graphics/redbook.png').convert()
book1_rect = book1.get_rect(topleft = (125, 125))

book2 = pygame.image.load('graphics/bluebook.png').convert()
book2_rect = book2.get_rect(topleft = (245, 125))

book3 = pygame.image.load('graphics/placeholder.png').convert()
book3_rect = book3.get_rect(topleft = (365, 125))

book4 = pygame.image.load('graphics/placeholder.png').convert()
book4_rect = book4.get_rect(topleft = (485, 125))

book5 = pygame.image.load('graphics/placeholder.png').convert()
book5_rect = book5.get_rect(topleft = (605, 125))


order = ['QC 981.8 .G56 G578', 'QC 981.8 .G56 G578 2002', 'QC 981.8 .G56 G578 2006']


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
        

        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        screen.blit(bg, (0, 0))
        screen.blit(shelf, shelf_rect)
        
        if event.type == pygame.MOUSEMOTION:

            if grabbed != []:
                print(grabbed)

                if grabbed[1].collidepoint(event.pos):
                    screen.blit(grabbed[2], (150, 30))

                    if clicks[0] is True:
                        screen.blit(grabbed[2], (150, 30))
                        
                        difference = mouse_pos[0] - grabbed[1].x
                        grabbed[1].x = event.pos[0] - difference

                        for rect in rect_list:
                            if grabbed[1].colliderect(rect) and rect != grabbed[1]:
                                print('collide!!')
                                if rect.x > grabbed[1].x:
                                    grabbed[1].x = rect.x - 100

                                elif rect.x < grabbed[1].x:
                                    grabbed[1].x = rect.x + 100

            else:        
                if book3_rect.collidepoint(event.pos):
                    screen.blit(call3, (150, 30))

                    if clicks[0] is True:
                        difference = mouse_pos[0] - book3_rect.x
                        book3_rect.x = event.pos[0] - difference

                        grabbed = [book3, book3_rect, call3]


                elif book2_rect.collidepoint(event.pos):
                    screen.blit(call2, (150, 30))
                    
                    
                    if clicks[0] is True:
                        difference = mouse_pos[0] - book2_rect.x
                        book2_rect.x = event.pos[0] - difference

                        grabbed = [book2, book2_rect, call2]


                elif book1_rect.collidepoint(event.pos):
                    screen.blit(call1, (150, 30))

                    if clicks[0] is True:
                        difference = mouse_pos[0] - book1_rect.x
                        book1_rect.x = event.pos[0] - difference

                        grabbed = [book1, book1_rect, call1]

                        
                """
                elif clicks[0] is False:
                    for rect in rect_list:
                        if book1_rect.colliderect(rect) and rect != book1_rect:
                            rect.x, book1_rect.x = book1_rect.x, rect.x

                            
                            if rect.x < book1_rect.x and book1_rect.x < 525:           # moving LEFT
                                rect.x = book1_rect.x + 100
                                pass

                            elif rect.x > book1_rect.x and book1_rect.x > 225:           # moving RIGHT
                                rect.x = book1_rect.x - 100
                                pass
                """
                            
                    
                """
                elif clicks[0] is False:
                    for rect in rect_list:
                        if book2_rect.colliderect(rect) and rect != book2_rect:
                            rect.x, book2_rect.x = book2_rect.x, rect.x
                            
                            if rect.x < book2_rect.x and book2_rect.x < 525:           # moving LEFT
                                rect.x = book2_rect.x + 100
                                pass

                            elif rect.x > book2_rect.x and book2_rect.x > 225:           # moving RIGHT
                                rect.x = book2_rect.x - 100
                                pass
                """

        
        for rect in rect_list:
                if event.type == pygame.MOUSEBUTTONUP and rect.collidepoint(mouse_pos):
                    
                    if book1_rect.colliderect(rect) and rect != book1_rect:
                        rect.x, book1_rect.x = book1_rect.x, rect.x
                        """
                        if rect.x < book1_rect.x:               # moving LEFT
                            
                            overlap = book1_rect.x - rect.x
                            
                            rect.x += overlap
                            book1_rect.x -= 100
                            
                        
                        elif rect.x > book1_rect.x:            # moving RIGHT
                            
                            overlap = rect.x - book1_rect.x
                            
                            rect.x -= 100
                            book1_rect.x += overlap
                        """   
                        

                    elif book2_rect.colliderect(rect) and rect != book2_rect:
                        rect.x, book2_rect.x = book2_rect.x, rect.x
                        """
                        if rect.x < book2_rect.x:           # moving LEFT
                            
                            overlap = book2_rect.x - rect.x
                            
                            rect.x += overlap
                            book2_rect.x -= 100
                            
                        elif rect.x > book2_rect.x:           # moving RIGHT
                            
                            overlap = rect.x - book2_rect.x
                            
                            rect.x -= 100
                            book2_rect.x += overlap
                        """

                    elif book3_rect.colliderect(rect) and rect != book3_rect:
                        rect.x, book3_rect.x = book3_rect.x, rect.x
                        """
                        if rect.x < book3_rect.x:           # moving LEFT
                            
                            overlap = book3_rect.x - rect.x
                            
                            rect.x += overlap
                            book3_rect.x -= 100
                            
                        elif rect.x > book3_rect.x:           # moving RIGHT
                            
                            overlap = rect.x - book3_rect.x
                            
                            rect.x -= 100
                            book3_rect.x += overlap
                        """  






                """
            

                elif clicks[0] is False:
                    for rect in rect_list:
                        if book3_rect.colliderect(rect) and rect != book3_rect:
                            if rect.x < book3_rect.x and book3_rect.x < 525:           # moving LEFT
                                rect.x = book3_rect.x + 100
                                pass

                            elif rect.x > book3_rect.x and book3_rect.x > 225:           # moving RIGHT
                                rect.x = book3_rect.x - 100
                                pass


            

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
                


        
        
        

        """
        screen.blit(book3, book3_rect)
        screen.blit(book4, book4_rect)
        screen.blit(book5, book5_rect)
        """
    

    pygame.display.update()
    clock.tick(60)

    # https://www.youtube.com/watch?v=AY9MnQ4x3zk, 1:13:46 !!


"""
    window.fill((113, 177, 222))

    pygame.draw.rect(window, (190, 119, 80), ((50, 50), (900, 350)))
    pygame.draw.rect(window, (102, 48, 31), ((75, 75), (850, 300)))
"""
