import pygame

def check(board, player):
    for i in range(3):
        if board[i][0]==board[i][1]==board[i][2]==player:
            return True

        if board[0][i]==board[1][i]==board[2][i]==player:
            return True

    if board[0][0]==board[1][1]==board[2][2]==player:
        return True

    if board[0][2]==board[1][1]==board[2][0]==player:
        return True

    return False

def result(player):
    screen=pygame.display.set_mode((1080, 720))
    screen.fill("black")
    font = pygame.font.SysFont("rog fonts", 64)

    if player=="D":
        text = font.render("Draw", True, "Gold")
    else:
        text = font.render(player+" Won", True, "Gold")

    text_rect = text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))
    screen.blit(text, text_rect)

    running=True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()

def check_result(board):
    if check(board, "X"):
        result("X")
        return False

    if check(board, "O"):
        result("O")
        return False

    if " " not in [j for i in board for j in i]:
        result("D")
        return False
    
    return True