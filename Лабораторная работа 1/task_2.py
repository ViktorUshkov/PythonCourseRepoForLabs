# TODO Найдите количество книг, которое можно разместить на дискете
size_in_Mb = 1.44
pages_in_book = 100
strings_on_page = 50
symbols_in_string = 25
bytes_in_symbol = 4

bytes_in_book = bytes_in_symbol * symbols_in_string * strings_on_page * pages_in_book
size_in_bytes = size_in_Mb * 1024 * 1024
books = int(size_in_bytes // bytes_in_book)
print("Количество книг, помещающихся на дискету:", books)
