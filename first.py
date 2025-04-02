'''
Напишіть функцію, яка приймає рядок як вхідні дані та
повертає словник, де ключі - це унікальні слова в рядку, а значення - кількість їх
появ.Створіть та виведіть на екран список, де зберігаються слова, що
зустрічаються більше 3 разів.
'''
def count_word_occurrences(text):
    words = text.lower().split()  # Розбиваємо рядок на слова та переводимо в нижній регістр
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts

def find_words_more_than_n_times(word_counts, n):
    result = []
    for word, count in word_counts.items():
        if count > n:
            result.append(word)
    return result

text = "кіт пес кіт миша кіт кіт пес"
word_counts = count_word_occurrences(text)
words_more_than_3 = find_words_more_than_n_times(word_counts, 3)

print(words_more_than_3) 