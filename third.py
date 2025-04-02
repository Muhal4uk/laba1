'''
Створіть список словників, де кожен словник
представляє продаж з ключами: "продукт", "кількість", "ціна". Напишіть функцію,
яка обчислює загальний дохід для кожного продукту та повертає словник, де
ключі - це назви продуктів, а значення - загальний дохід. Створіть список
продуктів, що принесли дохід більший ніж 1000.
'''
# Створення списку словників з продажами
sales = [
    {"продукт": "Яблуко", "кількість": 50, "ціна": 20},
    {"продукт": "Банан", "кількість": 30, "ціна": 25},
    {"продукт": "Апельсин", "кількість": 40, "ціна": 30},
    {"продукт": "Груша", "кількість": 100, "ціна": 15},
    {"продукт": "Ананас", "кількість": 10, "ціна": 150}
]

# Функція для обчислення загального доходу за кожним продуктом
def calculate_revenue(sales):
    revenue = {}
    for sale in sales:
        product = sale["продукт"]
        total = sale["кількість"] * sale["ціна"]
        revenue[product] = revenue.get(product, 0) + total
    return revenue

# Обчислення загального доходу
revenue = calculate_revenue(sales)
print("Загальний дохід за кожним продуктом:", revenue)

# Список продуктів, що принесли дохід більше 1000
high_revenue_products = [product for product, total in revenue.items() if total > 1000]
print("Продукти з доходом більше 1000:", high_revenue_products)
