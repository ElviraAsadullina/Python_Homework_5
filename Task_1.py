letter = str(input('Введите Ваш текст через пробел: '))
print(f'Исходный текст: {letter}')
to_delete = 'абв'
if letter.find(to_delete) != 1:
    print(f'Слов, содержащих "{to_delete}", не найдено!')
else:
    letter = [i for i in letter.split() if to_delete not in i]
    print(f'Полученный текст, исключающий слова c "{to_delete}":\n{" ".join(letter)}')