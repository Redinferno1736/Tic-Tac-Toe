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
    b=copy.deepcopy(board)
    result = check_res(b)
    if result is not None:  # Check if the game has ended
        if result == "O":
            return 10, None
        elif result == "X":
            return -10, None
        else:
            return 0, None

    if is_maximizing:
        best_score = -float('inf')
        best_move = None
        empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
        for move in empty_cells:
            make_move(board, move, "O")  # Simulate computer's move
            score, _ = minimax(board,False)  # Recurse for minimizer
            undo_move(board, move)  # Undo the move
            if score > best_score:
                best_score = score
                best_move = move
        return best_score, best_move

    else:
        best_score = float('inf')
        best_move = None
        empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
        for move in empty_cells:
            make_move(board, move, "X")  # Simulate human's move
            score, _ = minimax(board,True)  # Recurse for maximizer
            undo_move(board, move)  # Undo the move
            if score < best_score:
                best_score = score
                best_move = move
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
    a=set()
    board=[[" " for _ in range(3)] for _ in range(3)]
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

                    if board[y][x]==" ":
                        board[y][x]="X"
                        pygame.draw.line(screen, "red", (250 + x*200 + 20, 120 + y*200 + 20), (250 + (x+1)*200 - 20, 120 + (y+1)*200 - 20), 4)
                        pygame.draw.line(screen, "red", (250 + (x+1)*200 - 20, 120 + y*200 + 20), (250 + x*200 + 20, 120 + (y+1)*200 - 20), 4)
                        pygame.display.flip()

                        flag=False
                        running=functions.check_result(board)

            if flag == False:
                c=copy.deepcopy(board)
                if dificulty=="easy":
                    x,y=easy(c)
                else:
                    x,y=hard(c)
                a.add((x, y))
                pygame.time.delay(500)
                if board[y][x]==" " or (x, y) not in a:
                    board[y][x]="O"
                    
                    pygame.draw.circle(screen, "green", (250 + x*200 + 100, 120 + y*200 + 100), 80, 4)
                    pygame.display.flip()

                    flag=True
                    running=functions.check_result(board)