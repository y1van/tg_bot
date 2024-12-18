import sqlite3


con = sqlite3.connect('db.sqlite')

cur = con.cursor()

ice_cream = [
    ('Классический пломбир',
     'Настоящее мороженое, для истинных ценителей вкуса. Если на столе появляется пломбир — это не надолго.',
     'Обычное'),
    ('Мороженое с кузнечиками',
     'В колумбийском стиле: с добавлением карамелизованных кузнечиков.',
     'Экзотическое'),
    ('Мороженое со вкусом сыра чеддер',
     'Вкус настоящего сыра в вафельном стаканчике.',
     'Экзотическое'),
    ('Пломбир 1937',
     'Пломбир по рецепту 1937 года Московского хладокомбината',
     'Обычное')
]

cur.executemany('INSERT INTO ice_cream (title, description, category) VALUES (?, ?, ?);', ice_cream)

con.commit()

con.close()

