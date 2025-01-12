import pygame
import functions

def vs_player():
    a=set()
    board=[[" " for i in range(3)] for j in range(3)]
    screen=pygame.display.set_mode((1080, 720))
    screen.fill("black")

    for i in range(3):
        for j in range(3):
            pygame.draw.rect(screen, "white", (250+i*200, 120+j*200, 200, 200), 4)

    pygame.display.flip()

    flag=True
    running=True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if flag == True:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    flag=True
                    mouse_pos = event.pos
                    x, y = mouse_pos
                    x, y = (x - 250) // 200, (y - 120) // 200
                    a.add((x, y))
                    
                    if board[y][x]==" " or (x, y) not in a:
                        board[y][x]="X"
                        pygame.draw.line(screen, "red", (250 + x*200 + 20, 120 + y*200 + 20), (250 + (x+1)*200 - 20, 120 + (y+1)*200 - 20), 4)
                        pygame.draw.line(screen, "red", (250 + (x+1)*200 - 20, 120 + y*200 + 20), (250 + x*200 + 20, 120 + (y+1)*200 - 20), 4)
                        pygame.display.flip()

                        flag=False
                        running=functions.check_result(board)

            if flag == False:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    x, y = mouse_pos
                    x, y = (x - 250) // 200, (y - 120) // 200
                    a.add((x, y))

                    if board[y][x]==" " or (x, y) not in a:
                        board[y][x]="O"
                        pygame.draw.circle(screen, "green", (250 + x*200 + 100, 120 + y*200 + 100), 80, 4)
                        pygame.display.flip()

                        flag=True
                        running=functions.check_result(board)
                        


                    