board = list(range(1,10))
def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

def drawBoard(board):
    print(f'{board[0]:^5}|{board[1]:^5}|{board[2]:^5}')
    print('-----------------')
    print(f'{board[3]:^5}|{board[4]:^5}|{board[5]:^5}')
    print('-----------------')
    print(f'{board[6]:^5}|{board[7]:^5}|{board[8]:^5}\n\n')
def getInput(player_favor):
    valid = False
    while not valid:
        player_move = input(f'Играющий за "{player_favor}", делайте ход: ')
        try:
            player_move = int(player_move)
        except:
            print(colored(255, 0, 0, 'Необходимо указать номер поля для хода (число от 1 до 9)!'))
            continue
        if player_move > 0 and player_move < 10:
            if (str(board[player_move - 1]) not in "XO"):
                board[player_move - 1] = player_favor
                valid = True
            else:
                print(colored(255, 0, 0, 'Эта клетка уже занята!'))
        else:
            print(colored(255, 0, 0, 'Необходимо указать номер поля для хода(число от 1 до 9!)'))
def checkWin(board):
    win_lines = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
    for i in win_lines:
        if board[i[0]] == board[i[1]] == board[i[2]]:
            return board[i[0]]
    return False
def main(board):
    counter = 0
    win = False
    while not win:
        drawBoard(board)
        if counter % 2 == 0:
            getInput("X")
        else:
            getInput("O")
        counter += 1
        if counter > 4:
            drawBoard(board)
            tmp = checkWin(board)
            if tmp:
                print(f'Победил игравший за " {colored(255, 0, 0, tmp)}"!')
                win = True
                break
        if counter == 9:
            drawBoard(board)
            print(colored(0, 500, 0, 'Победила Дружба!'))
            break
main(board)