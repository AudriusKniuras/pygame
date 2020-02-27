import pygame
import random, math


# initial game setup

board = [
    ['','',''],
    ['','',''],
    ['','',''],
]

players = ['X', 'O']
currentPlayer = players[0]


screen = pygame.display.set_mode((450, 450))
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
    # diagonal checks
    if check_if_equal(board[0][0], board[1][1], board[2][2]):
        return board[0][0]
    if check_if_equal(board[2][0], board[1][1], board[0][2]):
        return board[2][0]
    
    open_spots = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == '':
                open_spots += 1
    if open_spots == 0:
        return 'TIE'

    return ""

scores = {
    'X': 10,
    'O': -10,
    'TIE': 0
}

def bestMove():
    best_score = -math.inf
    best_move = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == '':
                board[i][j] = players[1]
                score = minimax(board, 0, False)
                # undo the move
                board[i][j] = ''
                if score > best_score:
                    best_score = score
                    best_move = [i,j]
                    print(f'best_score: {best_score}')
    return best_move
    # board[best_move[0], best_move[1]] = players[1]



def minimax(board, depth, is_maximizing):
    result = check_win()
    
    # end state is reached, a winner or a TIE
    if result != "":
        score = scores[result]
        return score

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    board[i][j] = players[1]
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ''
                    best_score = max(score, best_score)
                    # print(f'MAX score: {score}')
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    board[i][j] = players[0]
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ''
                    best_score = min(score, best_score)
                    # print(f'MIN score: {score}')
        return best_score


bestMove()
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
                # available_rect = random.choice(available)
                best_move = bestMove()
                # pos = (available_rect[0]*height, available_rect[1]*width)
                pos = (best_move[0]*height, best_move[1]*width)
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
