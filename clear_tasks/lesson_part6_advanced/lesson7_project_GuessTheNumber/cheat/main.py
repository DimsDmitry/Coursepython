import random


class GuessingGame:
    def __init__(self):
        self.number_to_guess = random.randint(1, 100)  # Загаданное число от 1 до 100
        self.attempts = 0

    def start_game(self):
        print("Добро пожаловать в игру 'Угадай число'!")
        print("Я загадал число от 1 до 100. Попробуйте угадать его!")
        while True:
            guess = int(input("Введите ваше предположение: "))
            self.attempts += 1
            if self.make_guess(guess):
                print(f"Поздравляем! Вы угадали число {self.number_to_guess} за {self.attempts} попыток.")
                break

    def make_guess(self, guess):
        if self.is_correct(guess):
            return True
        elif guess < self.number_to_guess:
            print("Загаданное число больше.")
        else:
            print("Загаданное число меньше.")
        return False

    def is_correct(self, guess):
        return guess == self.number_to_guess


def main():
    game = GuessingGame()
    game.start_game()


if __name__ == "__main__":
    main()
