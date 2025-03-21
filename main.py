# Словник з продуктами та їх кількістю
inventory = {
    'apple': 10,
    'banana': 8,
    'orange': 3,
    'milk': 2,
    'bread': 6
}

# Функція для оновлення кількості продуктів
def update_inventory(product, quantity):
    if product in inventory:
        if quantity == 0:  # Якщо кількість 0 то видаляємо продукт
            del inventory[product]
            return
        inventory[product] += quantity
    else:
        if quantity > 0:  # Додаємо лише якщо кількість > 0
            inventory[product] = quantity
    
    # Видалення продукту, якщо його кількість стала <= 0
    if inventory.get(product, 1) <= 0:
        del inventory[product]

# Функція для отримання списку продуктів з кількістю менше ніж 5
def low_stock_products():
    return [product for product, quantity in inventory.items() if quantity < 5]

while True:
    product = input("Введіть назву продукту (або 'exit' для завершення): ").strip().lower()
    if product == 'exit':
        break
    try:
        quantity = int(input("Введіть кількість (може бути від'ємною або дорівнювати нулю для видалення): "))
        update_inventory(product, quantity)
        print("Оновлений склад:", inventory)
        print("Продукти з кількістю менше ніж 5:", low_stock_products())
    except ValueError:
        print("Помилка: введіть ціле число для кількості!")
