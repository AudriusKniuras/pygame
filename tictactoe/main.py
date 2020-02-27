import pygame
import random


board = [
    ['','',''],
    ['','',''],
    ['','',''],
]

available = []

players = ['X', 'O']

screen = pygame.display.set_mode((450, 450))

# initial game setup
currentPlayer = random.choice(players)
for i in range(3):
    for j in range(3):
        available.append([i,j])


screen.fill((255,255,255))

width = int(screen.get_width() / 3)
height = int(screen.get_height() / 3)


# draw the board
pygame.draw.line(screen, (0,0,0), (width, 0), (width, screen.get_height()), 2)
pygame.draw.line(screen, (0,0,0), (width*2, 0), (width*2, screen.get_height()), 2)
pygame.draw.line(screen, (0,0,0), (0, height), (screen.get_width(), height), 2)
pygame.draw.line(screen, (0,0,0), (0, height*2), (screen.get_width(), height*2), 2)



def draw_x(pos):
    xr = int(width/4)
    x_rect = pos[0] // height
    x_pos = x_rect * height
    y_rect = pos[1] // width
    y_pos = y_rect * width
    
    # return False if move is not available
    if board[x_rect][y_rect] != '':
        return False
    board[x_rect][y_rect] = 'X'
    available.remove([x_rect,y_rect])

    pygame.draw.line(screen, (0,0,0), (x_pos+xr, y_pos+height-xr), (x_pos+width-xr, y_pos+xr), 2)
    pygame.draw.line(screen, (0,0,0), (x_pos+width-xr, y_pos+height-xr), (x_pos+xr, y_pos+xr), 2)
    # return True if everything was successful
    return True

def draw_o(pos):
    if winner != "":
        return False
    x_rect = pos[0] // height
    x_pos = x_rect * height
    y_rect = pos[1] // width
    y_pos = y_rect * width

    if board[x_rect][y_rect] != '':
        return False

    board[x_rect][y_rect] = 'O'
    available.remove([x_rect,y_rect])

    circle_center = (int(x_pos + width / 2), int(y_pos + height / 2))
    pygame.draw.circle(screen, (0,0,0), circle_center, int(width/3), 3)

    return True

def check_if_equal(a, b, c):
    return (a == b and b == c and a != "")

def check_win():
    for i in range(3):
        # horizontal check
        if check_if_equal(board[i][0], board[i][1], board[i][2]):
            return board[i][0]
        # vertical check
        if check_if_equal(board[0][i], board[1][i], board[2][i]):
            return board[0][i]
    if check_if_equal(board[0][0], board[1][1], board[2][2]):
        return board[0][0]
    if check_if_equal(board[2][0], board[1][1], board[0][2]):
        return board[2][0]
    if len(available) == 0:
        return "TIE"
    return ""

def bestMove():
    best_score = -1000
    best_move = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == '':
                board[i][j] = players[1]
                score = minimax(board)
                # undo the move
                board[i][j] = ''
                if score > best_score:
                    best_score = score
                    best_move = [i,j]
    return [i,j]
    # board[best_move[0], best_move[1]] = players[1]

def minimax(board):
    return 1



running = True
winner = ""
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if winner != "":
            continue

        if currentPlayer == players[0]:
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                validMove = draw_x(pos)
                winner = check_win()
                if validMove and winner == "":
                    currentPlayer = players[1]
                elif winner == "TIE":
                    print(f'TIE')
                else:
                    print(f'{winner} WON')

        else:
            if len(available) > 0:
                # available_rect = random.choice(available)
                best_move = bestMove()
                # pos = (available_rect[0]*height, available_rect[1]*width)
                
                validMove = draw_o(pos)
                winner = check_win()
                if validMove and winner == "":
                    currentPlayer = players[0]
                elif winner == "TIE":
                    print(f'TIE')
                else:
                    print(f'{winner} WON')
                
    # screen.fill((255,255,255))
    
    pygame.display.update()
