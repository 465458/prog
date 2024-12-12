class Book:
    className = 'Book'

    def __init__(self, pages, time, pictures):
        self._pages = pages
        self._time = time
        self._pictures = pictures

    def ReadingTime(self):
        print(f'Время чтения книги в минутах: {self._time * self._pages}')


class Encyclopedia(Book):
    className = 'Encyclopedia'

    def __init__(self, pages, time, pictures, articles):
        super().__init__(pages, time, pictures)
        self._articles = articles

    def AverageArticles(self):
        print(f'Среднее количство статей на странице: {self._articles // self._pages}')

class PhoneDirectory(Book):
    className = 'PhoneDirectory'

    def __init__(self, pages, time, pictures, numbers):
        super().__init__(pages, time, pictures)
        self._numbers = numbers

    def AverageNumbers(self):
        print(f'Среднее количство номеров на странице: {self._numbers // self._pages}')


book1 = Book(50,1.5,10)
book1.ReadingTime()

encyclopedia1 = Encyclopedia(150,1.8,50,300)
encyclopedia1.AverageArticles()

phone_directory1 = PhoneDirectory(40,0.8,0,624)
phone_directory1.AverageNumbers()