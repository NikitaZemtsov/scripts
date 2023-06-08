import pandas as pd

# Чтение данных из таблицы в формате CSV
data = pd.read_excel('IT words.xlsx')

# Открытие файла для записи
with open('IT_words.txt', 'w', encoding='utf-8', errors='ignore') as file:
    # Запись данных в TXT файл
    for _, row in data.iterrows():
        word = row['Слово']
        transcription = row['Транскрипция']
        translation = row['Перевод']
        example = row['Пример']

        # Запись строки в формате "слово";"транскрипция";"перевод";"пример"
        line = f'"{word}";"{transcription}";"{translation}";"{example}";""\n'
        file.write(line)
