'''
Створіть словник в якому зберігаються ім'я
користувача(login), зашифрований пароль та повне ПІБ користувача. Для
хешування пароля використовуйте функцію hashlib.md5(). Зробіть функцію
перевірки введеного паролю користувача; пароль користувач вводить з консолі,
зчитування за допомогою методу input()
'''
import hashlib

# Словник для зберігання інформації користувача
user_data = {
    "login": "user123",
    "password_hash": hashlib.md5("secure_password".encode()).hexdigest(),  # Зашифрований пароль
    "full_name": "Іван Іванович Іванов"
}
def check_password(input_password):
    #Функція для перевірки введеного паролю.
    # Хешуємо введений пароль
    input_password_hash = hashlib.md5(input_password.encode()).hexdigest()
    
    # Порівнюємо з зашифрованим паролем у словнику
    if input_password_hash == user_data["password_hash"]:
        return True
    else:
        return False

# Запитуємо у користувача пароль
user_input = input("Введіть ваш пароль: ")
while True:
# Перевіряємо пароль
    if check_password(user_input):
        print("Пароль вірний! Ласкаво просимо, " + user_data["full_name"] + "!")
        break
    elif check_password(user_input) == False:
        print("Неправильний пароль. Спробуйте ще раз.")
        user_input = input("Введіть ваш пароль: ")