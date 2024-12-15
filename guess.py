from datetime import datetime as dt
from random import randint
from access_control import access_control
from constants import ADMIN_USERNAME, UNKNOWN_COMMAND


class Guess:
    def __init__(self):
        self.username = ''
        self.total_games = 0
        self.number = 0
        self.start_time = dt.now()

    @access_control
    @staticmethod
    def get_statistics(total_games: int, start_time: dt, *args, **kwargs) -> None:
        game_time = dt.now() - start_time
        print(f'Общее время игры: {game_time}, текущая игра - №{total_games}')


    @access_control
    @staticmethod
    def get_right_answer(number: int, *args, **kwargs) -> None:
        print(f'Правильный ответ: {number}')

    def check_number(self, guess: int) -> bool:
    # Если число угадано...
        if guess == self.number:
            print(f'Отличная интуиция, {self.username}! Вы угадали число :)')
            # ...возвращаем True
            return True
        
        if guess < self.number:
            print('Ваше число меньше того, что загадано.')
        else:
            print('Ваше число больше того, что загадано.')
        return False
    
    def get_username(self) -> str:
        self.username = input('Представьтесь, пожалуйста, как Вас зовут?\n').strip()
        if self.username == ADMIN_USERNAME:
            print(
                '\nДобро пожаловать, создатель! '
                'Во время игры вам доступны команды "stat", "answer"'
            )
            print(f'\n{self.username}, добро пожаловать в игру!')
        return self.username
    
    def guess_number(self) -> None:
        # Счётчик игр в текущей сессии.
        while True:
            self.total_games += 1
            self.game()

            play_again = input(f'\nХотите сыграть ещё? (yes/no) ')

            if play_again.strip().lower() not in ('y', 'yes'):
                break

    
    def game(self) -> None:
        # Получаем случайное число в диапазоне от 1 до 100.
        self.number = randint(1, 100)

        print(
            '\nУгадайте число от 1 до 100.\n'
            'Для выхода из текущей игры введите команду "stop"'
        )

        while True:
            # Получаем пользовательский ввод, 
            # отрезаем лишние пробелы и переводим в нижний регистр.
            user_input = input('Введите число или команду: ').strip().lower()

            match user_input:
                case 'stop':
                    break
                case 'stat':
                    Guess.get_statistics(self.total_games, self.start_time, username=self.username) 
                case 'answer':
                    Guess.get_right_answer(self.number, username=self.username)
                case _:
                    try:
                        guess = int(user_input)                
                    except ValueError:
                        print(UNKNOWN_COMMAND)
                        continue

                    if self.check_number(guess):
                        break  