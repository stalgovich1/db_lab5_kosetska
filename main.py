import psycopg2
import matplotlib.pyplot as plt

username = 'postgres'
password = 'postgres'
database = 'lab_3_6'
host = 'localhost'
port = '5432'

query_1 = '''
--Вибрати всі фільми
SELECT * FROM MoviesAndShows;
'''

query_2 = '''
--Вибрати всі країни
SELECT * FROM Countries;
'''

query_3 = '''
--Вибрати всі рейтинги разом із назвою фільму/шоу та ім'ям країни
SELECT MoviesAndShows.Title, Countries.CountryName, Ratings.Rank, Ratings.Viewership, Ratings.Duration
FROM Ratings
JOIN MoviesAndShows ON Ratings.MovieOrShowID = MoviesAndShows.MovieOrShowID
JOIN Countries ON Ratings.CountryID = Countries.CountryID;
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn:
    cur = conn.cursor()

    print('Загальний рейтинг (weekly_rank) для фільму "Red Notice" за всі країни:')
    cur.execute(query_1)

    for row in cur:
       print(row)

    print('\nКількість годин перегляду для кожного фільму в Аргентині:')
    cur.execute(query_2)

    for row in cur:
       print(row)

    print('\nЗагальний рейтинг (weekly_rank) для фільму за всі країни:')
    cur.execute(query_3)

    for row in cur:
       print(row)
