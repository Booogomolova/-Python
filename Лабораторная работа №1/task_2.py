# TODO Найдите количество книг, которое можно разместить на дискете
V = 1.44*1024*1024
page = 100
line = 50
symbol = 25
weight = 4
count_symbol = page*line*symbol
weight_book = weight*count_symbol
count_books = V/weight_book
a = round(count_books)
print("Количество книг, помещающихся на дискету:", a)
