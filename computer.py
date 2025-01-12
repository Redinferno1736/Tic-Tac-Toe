import pygame
import functions
import random
import copy

def check_res(board):
    if functions.check(board, "X"):
        return "X"

    if functions.check(board, "O"):
        return "O"

    if " " not in [j for i in board for j in i]:
        return "D"
    
    return None

def make_move(board, move, player):
    row, col = move
    board[row][col] = player

def undo_move(board, move):
    row, col = move
    board[row][col] = " "

def minimax(board, is_maximizing):
    result = check_res(board)
    if result == "O":  # Computer wins
        return 10, None
    if result == "X":  # Player wins
        return -10, None
    if result == "D":  # Draw
        return 0, None

    best_move = None
    if is_maximizing:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score, _ = minimax(board, False)
                    board[i][j] = " "
                    if score > best_score:
                        best_score = score
                        best_move = (j, i)
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score, _ = minimax(board, True)
                    board[i][j] = " "
                    if score < best_score:
                        best_score = score
                        best_move = (j, i)

    return best_score, best_move

def easy(board):
    empty_cells = [(j, i) for i in range(3) for j in range(3) if board[i][j] == " "]
    return random.choice(empty_cells)

def hard(board):
    _, best_move = minimax(board,True)
    if best_move is None:  # If no valid move is found, choose a random empty cell
        empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
        best_move = random.choice(empty_cells)
    return best_move

def level():
    screen = pygame.display.set_mode((1080, 720))
    screen.fill("black")

    font1= pygame.font.SysFont("rog fonts", 32)

    running=True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
            t=font1.render("Choose Difficulty", True, "white")
            t_rect = t.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2-100))
            screen.blit(t, t_rect)

            easy_text = font1.render("Easy", True, "white")
            easy_rect = easy_text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2+50))
            screen.blit(easy_text, easy_rect)

            hard_text = font1.render("Hard", True, "white")
            hard_rect = hard_text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2+150))
            screen.blit(hard_text, hard_rect)

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos

                if easy_rect.collidepoint(mouse_pos):
                    running=False
                    vs_computer('easy')
                    
                if hard_rect.collidepoint(mouse_pos):
                    running=False
                    vs_computer('hard')
                    
            pygame.display.flip()


def vs_computer(dificulty):
    board = [[" " for _ in range(3)] for _ in range(3)]
    screen = pygame.display.set_mode((1080, 720))
    screen.fill("black")

    for i in range(3):
        for j in range(3):
            pygame.draw.rect(screen, "white", (250 + i*200, 120 + j*200, 200, 200), 4)

    pygame.display.flip()

    flag = True
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if flag:  # Player's turn
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    x, y = (mouse_pos[0] - 250) // 200, (mouse_pos[1] - 120) // 200
                    if 0 <= x < 3 and 0 <= y < 3 and board[y][x] == " ":
                        board[y][x] = "X"
                        pygame.draw.line(screen, "red", (250 + x*200 + 20, 120 + y*200 + 20), (250 + (x+1)*200 - 20, 120 + (y+1)*200 - 20), 4)
                        pygame.draw.line(screen, "red", (250 + (x+1)*200 - 20, 120 + y*200 + 20), (250 + x*200 + 20, 120 + (y+1)*200 - 20), 4)
                        pygame.display.flip()
                        flag = False
                        result = check_res(board)
                        if result:
                            functions.result(result)
                            running = False

            if not flag:  # AI's turn
                pygame.time.delay(500)  # Delay for AI "thinking"
                if dificulty == "easy":
                    x, y = easy(board)
                else:
                    x, y = hard(board)

                if board[y][x] == " ":
                    board[y][x] = "O"
                    pygame.draw.circle(screen, "green", (250 + x*200 + 100, 120 + y*200 + 100), 80, 4)
                    pygame.display.flip()
                    flag = True
                    result = check_res(board)
                    if result:
                        functions.result(result)
                        running = False