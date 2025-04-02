'''
Створіть словник, де ключі - це назви задач, а
значення - їх статус ("виконано", "в процесі", "очікує"). Напишіть функції для
додавання, видалення та зміни статусу задач. Додатково: створіть список задач,
які мають статус "очікує".
'''
class TaskManager:
    def __init__(self):
        self.tasks = {}

    def add_task(self, name, status="очікує"):
        self.tasks[name] = status
        print(f'Задача "{name}" додана зі статусом "{status}".')

    def remove_task(self, name):
        if name in self.tasks:
            del self.tasks[name]
            print(f'Задача "{name}" видалена.')
        else:
            print(f'Задача "{name}" не знайдена.')

    def change_status(self, name, status):
        if name in self.tasks:
            self.tasks[name] = status
            print(f'Статус задачі "{name}" змінено на "{status}".')
        else:
            print(f'Задача "{name}" не знайдена.')

    def get_pending_tasks(self):
        pending = [name for name, status in self.tasks.items() if status == "очікує"]
        return pending

# Приклад використання:
tm = TaskManager()
tm.add_task("Підготувати звіт")
tm.add_task("Перевірити код", "в процесі")
tm.add_task("Надіслати лист")

tm.change_status("Підготувати звіт", "виконано")
print("Задачі, що очікують виконання:", tm.get_pending_tasks())
