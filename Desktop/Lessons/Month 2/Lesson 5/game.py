import random
from decouple import config


def casino():
    my_money = config("startmoney", cast=int)
    balance = my_money
    while True:
        num1_30 = input("Выберите число от 1 до 30:")
        bet = int(input("Ваша ставка: "))
        slot = random.randint(1, 31)
        if slot == num1_30:
            my_cash = bet * 2
            balance += my_cash
        else:
            balance -= bet
        play_again = input("Хотите сыграть еще раз (да/нет)? ")
        if play_again.lower() == 'нет':
            print("Выши деньги: ", balance)
            break
        elif play_again.lower() == 'y':
            continue


if __name__ == '__main__':
    casino()


