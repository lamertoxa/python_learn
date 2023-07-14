import matplotlib.pyplot as plt
from collections import Counter
import string

# зчитуємо текст з файлу
with open('text.txt', 'r') as f:
    text = f.read().lower()

# видаляємо з тексту всі символи, що не є літерами
text = ''.join(filter(str.isalpha, text))

# підраховуємо кількість кожної літери
letter_counts = Counter(text)

# візуалізуємо дані
plt.figure(figsize=(10, 6))
plt.bar(letter_counts.keys(), letter_counts.values())
plt.xlabel('Letters')
plt.ylabel('Frequency')
plt.title('Letter Frequency Histogram')
plt.grid(True)
plt.savefig('histogram.png')
plt.show()