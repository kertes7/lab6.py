import random

# Task #1
def treasure_game():
    try:
        coins = random.randint(1, 1000)
        people = int(input("Введіть кількість людей у команді: "))
        share = coins // people
        print(f"Кожен отримав {share} монет.")
    except ValueError:
        print("Помилка: введене значення не є числом!")
    except ZeroDivisionError:
        print("Помилка: ділити на нуль не можна!")
    finally:
        print("Пригоди тривають!")


# Task #2
def safe_cracking_game():
    code = random.randint(100, 999)
    attempts = 5
    while attempts > 0:
        try:
            guess = int(input("Введіть код сейфу (трицифрове число): "))
            if guess == code:
                print("Ви зламали сейф! Вітаємо!")
                return
            elif guess < code:
                print("Код більший.")
            else:
                print("Код менший.")
        except ValueError:
            print("Помилка: введене значення не є числом!")
        attempts -= 1
        print(f"Залишилось спроб: {attempts}")
    print(f"Ви програли! Код був {code}.")


# Task #3
def rpsls_game():
    choices = ["камінь", "ножиці", "папір", "ящірка", "Спок"]
    rules = {
        "камінь": ["ножиці", "ящірка"],
        "ножиці": ["папір", "ящірка"],
        "папір": ["камінь", "Спок"],
        "ящірка": ["папір", "Спок"],
        "Спок": ["ножиці", "камінь"]
    }
    while True:
        player_choice = input("Виберіть: камінь, ножиці, папір, ящірка або Спок: ").strip().lower()
        if player_choice not in choices:
            print("Некоректний вибір!")
            continue
        computer_choice = random.choice(choices)
        print(f"Комп'ютер вибрав: {computer_choice}")
        if player_choice == computer_choice:
            print("Нічия!")
        elif computer_choice in rules[player_choice]:
            print("Ви перемогли!")
        else:
            print("Комп'ютер переміг!")
        if input("Грати ще раз? (так/ні): ").strip().lower() != "так":
            break


# Task #4
def bonus_system():
    try:
        points = int(input("Введіть кількість набраних очок (0-100): "))
        if points < 0 or points > 100:
            raise ValueError("Очки повинні бути від 0 до 100.")
        ratings = [(49, "Початківець", 1), (69, "Срібний гравець", 1.5),
                   (89, "Золотий гравець", 2), (100, "Платиновий гравець", 3)]
        for max_score, title, multiplier in ratings:
            if points <= max_score:
                final_score = int(points * multiplier)
                print(f"Ваш рейтинг: {title}! Ви отримали {final_score} балів (множник ×{multiplier})!")
                return
    except ValueError as e:
        print(f"Помилка: {e}")


# Task #5
def escape_island():
    try:
        wood = int(input("Скільки деревини у вас є (1-10)?: "))
        if wood < 3:
            print("Деревини замало, пліт затонув!")
            return
    except ValueError:
        print("Це не число!")
        return
    try:
        action = input("Як ви будете втікати? (бігти/сховатися/битися): ").strip().lower()
        if action not in ["бігти", "сховатися", "битися"]:
            raise ValueError("Такого варіанту немає, пірати вас спіймали!")
    except ValueError as e:
        print(e)
        return
    code = random.randint(10, 99)
    try:
        user_code = int(input("Введіть код для скрині: "))
        if user_code != code:
            print("Неправильний код, скриня вибухнула!")
            return
        print("Скарб ваш, ви врятовані!")
    except ValueError:
        print("Це не число!")
    finally:
        print("Гра завершена. Дякуємо за участь у пригоді!")
