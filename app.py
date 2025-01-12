# Importing the required libraries
import pygame
import player
import computer

# Initialising Pygame
pygame.init()
    
# Setting screen dimensions
screen = pygame.display.set_mode((1080, 720))

# Setting game background
screen.fill("black")

# Setting the fonts of the window
font = pygame.font.SysFont("rog fonts", 64)
font1= pygame.font.SysFont("rog fonts", 32)

# Setting the title of the window
text = font.render("Tic Tac Toe", True, "Gold")
text_rect = text.get_rect(center=(screen.get_width() / 2, text.get_height() / 2 + 20))
screen.blit(text, text_rect)

running=True

# Difiiculty selecting loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = 1
            running = False
    
    t=font1.render("Select Game Mode", True, "lightgreen")
    t_rect = t.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2-100))
    screen.blit(t, t_rect)

    p_text = font1.render("1   Vs   1", True, "White")
    p_rect = p_text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2+50))
    screen.blit(p_text, p_rect)

    c_text = font1.render("Computer", True, "white")
    c_rect = c_text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2+150))
    screen.blit(c_text, c_rect)

    # Check for mouse click events
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = event.pos  # Get the mouse position

        # Check if the mouse click is within the easy button
        if p_rect.collidepoint(mouse_pos):
            running=False
            player.vs_player()
            
        # Check if the mouse click is within the medium button
        if c_rect.collidepoint(mouse_pos):
            running=False
            computer.level()
            

    # flip() the display to put your work on screen
    pygame.display.flip()

    pygame.time.delay(100)

# Exiting pygame
pygame.quit()