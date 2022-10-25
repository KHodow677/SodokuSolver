import Board
import pygame

pygame.font.init()

pygame.display.set_caption("Backtracking Sudoku Solver")

# Establish variables for board setup and partitioning
x = 0
y = 0
dif = 500 / 9
val = 0
# Load test fonts for future use
font1 = pygame.font.SysFont("comicsans", 40)
font2 = pygame.font.SysFont("comicsans", 20)

# Function that gets sets the x-y coordinates based on the coordinates of passed position
# Inputs: tuple pos representing x-y coordinates
def SetCoord(pos):
    global x
    x = pos[0]//dif
    global y
    y = pos[1]//dif

# Function that fills value entered in cell the cell  
# Inputs: int val representign of the number entered in the cell  
def DrawVal(val):
    text1 = font1.render(str(val), 1, (0, 0, 0))
    screen.blit(text1, (x * dif + 15, y* dif))  

# Function that draws the selection box
def DrawBox():
    for i in range(2):
        pygame.draw.line(screen, (255, 0, 0), (x * dif-3, (y + i)*dif), (x * dif + dif + 3, (y + i)*dif), 7)
        pygame.draw.line(screen, (255, 0, 0), ( (x + i)* dif, y * dif ), ((x + i) * dif, y * dif + dif), 7)  

# Function that raises error when wrong value entered
def RaiseError1():
    text1 = font1.render("WRONG !!!", 1, (0, 0, 0))
    screen.blit(text1, (20, 620))  

# Display options when solved
def result():
    text1 = font2.render("FINISHED PRESS R or D", 1, (0, 0, 0))
    screen.blit(text1, (20, 570))   

# Display instruction for the game
def Instruction():
    text1 = font2.render("PRESS D TO RESET TO DEFAULT / R TO EMPTY", 1, (0, 0, 0))
    text2 = font2.render("INPUT VALUES OR PRESS ENTER", 1, (0, 0, 0))
    screen.blit(text1, (20, 520))       
    screen.blit(text2, (20, 540))

# Sets up variables for main game loop logic
screen = pygame.display.set_mode((500,700))
run = True
flag1 = 0
flag2 = 0
rs = 0
error = 0

# Set up the board for the game
board = Board.Board(screen)
board.GenerateSolution()
board.RemoveNumbersFromBoard(2)
# The loop thats keep the window running
while run:
    # White color background
    screen.fill((255, 255, 255))
    # Loop through the events stored in event.get()
    for event in pygame.event.get():
        # Quit the game window
        if event.type == pygame.QUIT:
            run = False
        # Get the mouse position to insert number   
        if event.type == pygame.MOUSEBUTTONDOWN:
            flag1 = 1
            pos = pygame.mouse.get_pos()
            SetCoord(pos)
        # Get the number to be inserted if key pressed   
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x-= 1
                flag1 = 1
            if event.key == pygame.K_RIGHT:
                x+= 1
                flag1 = 1
            if event.key == pygame.K_UP:
                y-= 1
                flag1 = 1
            if event.key == pygame.K_DOWN:
                y+= 1
                flag1 = 1   
            if event.key == pygame.K_1:
                val = 1
            if event.key == pygame.K_2:
                val = 2   
            if event.key == pygame.K_3:
                val = 3
            if event.key == pygame.K_4:
                val = 4
            if event.key == pygame.K_5:
                val = 5
            if event.key == pygame.K_6:
                val = 6
            if event.key == pygame.K_7:
                val = 7
            if event.key == pygame.K_8:
                val = 8
            if event.key == pygame.K_9:
                val = 9 
            if event.key == pygame.K_RETURN:
                flag2 = 1
            # If R pressed clear the sudoku board
            if event.key == pygame.K_r:
                rs = 0
                error = 0
                flag2 = 0
                board.board =[
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0]
                ]
            # If D is pressed reset the board to default
            if event.key == pygame.K_d:
                rs = 0
                error = 0
                flag2 = 0
                board.GenerateSolution()
                board.RemoveNumbersFromBoard(2)
    if flag2 == 1:
        board.Solve()
        flag2 = 0
        rs = 1
        error = 0
    if val != 0:           
        DrawVal(val)
        if board.SquareIsValid(val, (int(x), int(y))):
            board.board[int(x)][int(y)]= val
            flag1 = 0
        else:
            board.board[int(x)][int(y)]= 0
            error = 1  
        val = 0   
       
    if error == 1:
        RaiseError1() 
    if rs == 1:
        result()       
    board.Draw()
    if flag1 == 1:
        DrawBox()      
    Instruction()   
 
    # Update window
    pygame.display.update() 
 
# Quit pygame window   
pygame.quit()    