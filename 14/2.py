def space_game(text):
    if text.count(' ') % 2 == 0:
        print('Вы выиграли')
    else:
        print('Вы проиграли')


space_game(input())