from random import randint
def inputCorrectCount(name, b):
    while True:
        try:
            x = int(input(f'{name}, введите количество конфет, которое возьмете (от 1 до {b}): '))
        except ValueError:
            print(f'Ошибка - необходимо ввести число от 1 до {b}!')
            continue    
        if x < 1 or x > b:
            print(f'{name}, введите корректное количество конфет (от 1 до {b})!: ')
            continue
        break
    return x
def preResult(name, x, score, candies_count):
    print(f'Ходил {name}. Он взял {x} конфет, и теперь у него {score} конфет. Осталось на столе {candies_count} конфет.')
def getRightTactic1(a, b):
    first_move = a % b
    return first_move
def getRightTactic2(b):  
    next_moves = f'{b + 1} минус количество только что взятых соперником конфет'
    return next_moves
player1 = input('Введите имя первого игрока: ')
player2 = input('Введите имя второго игрока: ')
candies_count = 2021
turn = randint(0, 2)
max_step = 28
if turn:
    print(f'Первым ходит {player1}')
    print(f'Подсказка для ходящего первым игрока: первым ходом возьмите {getRightTactic1(candies_count, max_step)} конфет, а затем каждый раз берите по {getRightTactic2(max_step)}.')
else:
    print(f'Первым ходит {player2}')
    print(f'Подсказка для ходящего первым игрока: первым ходом возьмите {getRightTactic1(candies_count, max_step)} конфет, а затем каждый раз берите по {getRightTactic2(max_step)}.')
score1 = 0 
score2 = 0
while candies_count > max_step:
    if turn:
        x = inputCorrectCount(player1, max_step)
        score1 += x
        candies_count -= x
        turn = False
        preResult(player1, x, score1, candies_count)
    else:
        x = inputCorrectCount(player2, max_step)
        score2 += x
        candies_count -= x
        turn = True
        preResult(player2, x, score2, candies_count)
if turn:
    print(f'Победил {player1}!')
else:
    print(f'Победил {player2}!')