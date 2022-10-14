import collections
import json


# Первым делом нужно написать функцию для чтения файла с информацией по новостями.
# У нас есть функция, умеющая читать файл и преобразовывать json в словарь!

# Теперь, когда есть доступ к json файлу, нужно получить из него все слова новостей.
# Точнее не из новостей, а из их описания (description).
# Для простоты слова будем разделять только пробелами.

# Обратите внимание, что news - это просто словарь.
# Через ключи мы можем получить все items из новостей.
# А из item у нас уже есть доступ к каждому описанию(description).
# При получении description мы сразу разделяем его на список из
# слов по пробелам. Для добавления в список descriptions мы используем
# extend, так как хотим получить один большой список

# Отлично! Теперь у нас в списке description слова длиной больше 6 символов.(строка 36)
# Обратите внимание, что число 6 мы вынесли в параметр функции, чтобы в будущем это значение можно было регулировать.
# Для итерации по списку слов мы использовали конструкцию list comprehension (строка 36)

# И последнее действие: получить список из 10 самых популярных длинных слов.
# Для решения этой задачи можно воспользоваться классом collections.Counter
# https://docs.python.org/3/library/collections.html#collections.Counter
# Супер! Для решения задачи мы использовали из модуля collections класс Counter.
# Он автоматически подсчитывает количество вхождений слов в списке.
# И с помощью метода most_common (39 строка) можно получить топ нужных слов.
# Также обратите внимание, что добавился ещё один параметр top_words для удобного изменения
# нужного количества популярных слов.

def read_json(file_path, max_len_word=6, top_words=10):
    with open('newsafr.json', encoding='utf-8') as news_file:
        news = json.load(news_file) # чтение файла через load
        description_words = []
        for item in news['rss']['channel']['items']:
            description = [word for word in item['description'].split(' ') if len(word) > max_len_word]
            description_words.extend(description)
            counter_words = collections.Counter(description_words)
        print(counter_words.most_common(top_words))

if __name__ == '__main__':
    read_json('newsafr.json')
