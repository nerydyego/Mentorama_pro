import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 15
WHITE = (255, 255, 255)
LINE_COLOR = (255, 0, 0)
BLACK = (0, 0, 0)
PLAYER = 'X'
COMPUTER = 'O'


CELL_SIZE = WIDTH // 3


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")


board = [['' for _ in range(3)] for _ in range(3)]


def draw_board():
    for x in range(1, 3):
        pygame.draw.line(screen, BLACK, (0, CELL_SIZE * x), (WIDTH, CELL_SIZE * x), LINE_WIDTH)
        pygame.draw.line(screen, BLACK, (CELL_SIZE * x, 0), (CELL_SIZE * x, HEIGHT), LINE_WIDTH)


def draw_symbol(row, col, symbol):
    font = pygame.font.Font(None, 100)
    text = font.render(symbol, True, BLACK)
    x = col * CELL_SIZE + CELL_SIZE // 4
    y = row * CELL_SIZE + CELL_SIZE // 4
    screen.blit(text, (x, y))


def check_winner():
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] != '':
            return board[row][0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '':
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '':
        return board[0][2]
    return None

def is_board_full():
    for row in board:
        if '' in row:
            return False
    return True

def computer_move():
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == '':
            return row, col


def reset_game():
    for row in range(3):
        for col in range(3):
            board[row][col] = ''
    return 'X' if random.randint(0, 1) == 0 else 'O'

current_player = reset_game()
game_over = False

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x, y = event.pos
            col = x // CELL_SIZE
            row = y // CELL_SIZE
            if board[row][col] == '':
                board[row][col] = current_player
                current_player = 'X' if current_player == 'O' else 'O'

    screen.fill(WHITE)
    draw_board()

    for row in range(3):
        for col in range(3):
            if board[row][col] != '':
                draw_symbol(row, col, board[row][col])

    winner = check_winner()
    if winner:
        font = pygame.font.Font(None, 36)
        text = font.render(f"Você {winner} Ganhou!", True, LINE_COLOR)
        screen.blit(text, (WIDTH // 4, HEIGHT // 2))
        game_over = True

    if not winner and is_board_full():
        font = pygame.font.Font(None, 36)
        text = font.render("Empate!", True, LINE_COLOR)
        screen.blit(text, (WIDTH // 4, HEIGHT // 2))
        game_over = True

    if game_over:
        font = pygame.font.Font(None, 24)
        text = font.render("Pressione 'R' para Reiniciar ou 'S' para Sair", True, LINE_COLOR)
        screen.blit(text, (WIDTH // 4, HEIGHT * 3 // 4))

    pygame.display.update()

    keys = pygame.key.get_pressed()
    if game_over:
        if keys[pygame.K_r]:
            current_player = reset_game()
            game_over = False
            continue
        elif keys[pygame.K_q]:
            running = False

pygame.quit()
sys.exit()
