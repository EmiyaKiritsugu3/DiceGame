from random import randint
from operator import itemgetter

player1 = input("h")
player2 = input('k')


def roll():
    dice1 = randint(1, 6)
    dice2 = randint(1, 6)
    return [dice1, dice2]


jogo = {player1: roll(),
        player2: roll()}

for k, v, in jogo.items():
    v = v[0] + v[1]

print(v)
print('valores')


def to():
    for k, v, in jogo.items():
        if v[0] == 1:
            v[0] = (
                '#########\n'
                '#       #\n'
                '#   *   #\n'
                '#       #\n'
                '#########')
        elif v[0] == 2:
            v[0] = (
                '#########\n'
                '#     * #\n'
                '#       #\n'
                '# *     #\n'
                '#########')
        elif v[0] == 3:
            v[0] = (
                '#########\n'
                '#     * #\n'
                '#   *   #\n'
                '# *     #\n'
                '#########')
        elif v[0] == 4:
            v[0] = (
                '#########\n'
                '# *   * #\n'
                '#       #\n'
                '# *   * #\n'
                '#########')
        elif v[0] == 5:
            v[0] = (
                '#########\n'
                '# *   * #\n'
                '#   *   #\n'
                '# *   * #\n'
                '#########')
        else:
            v[0] = (
                '#########\n'
                '# *   * #\n'
                '# *   * #\n'
                '# *   * #\n'
                '#########')

        if v[1] == 1:
            v[1] = (
                '#########\n'
                '#       #\n'
                '#   *   #\n'
                '#       #\n'
                '#########')
        elif v[1] == 2:
            v[1] = (
                '#########\n'
                '#     * #\n'
                '#       #\n'
                '# *     #\n'
                '#########')
        elif v[1] == 3:
            v[1] = (
                '#########\n'
                '#     * #\n'
                '#   *   #\n'
                '# *     #\n'
                '#########')
        elif v[1] == 4:
            v[1] = (
                '#########\n'
                '# *   * #\n'
                '#       #\n'
                '# *   * #\n'
                '#########')
        elif v[1] == 5:
            v[1] = (
                '#########\n'
                '# *   * #\n'
                '#   *   #\n'
                '# *   * #\n'
                '#########')
        else:
            v[1] = (
                '#########\n'
                '# *   * #\n'
                '# *   * #\n'
                '# *   * #\n'
                '#########')

        print(f'{k} tirou o\n{v[0]}\nand\n{v[1]}')


to()
