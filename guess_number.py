from guess import Guess


if __name__ == '__main__':
    print(
        'Вас приветствует игра "Угадай число"!\n'
        'Для выхода нажмите Ctrl+C'
    )

    game = Guess()
    game.get_username()
    game.guess_number()
