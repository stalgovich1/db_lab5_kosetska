import psycopg2
import csv

username = 'postgres'
password = 'postgres'
database = 'lab_3_6'
host = 'localhost'
port = '5432'

CSV_MOVIES_FILE = 'MoviesAndShows.csv'
CSV_WEEKS_FILE = 'Weeks.csv'
CSV_COUNTRIES_FILE = 'Countries.csv'
CSV_RATINGS_FILE = 'Ratings.csv'
files = [CSV_MOVIES_FILE, CSV_WEEKS_FILE, CSV_COUNTRIES_FILE, CSV_RATINGS_FILE]

query_1 = '''
    INSERT INTO MoviesAndShows (MovieOrShowID, Title, Type, ReleaseYear) 
    VALUES (%s, %s, %s, %s);
'''
query_2 = '''
    INSERT INTO Weeks (WeekID, WeekStartDate, WeekEndDate) 
    VALUES (%s, %s, %s);
'''
query_3 = '''
    INSERT INTO Countries (CountryID, CountryName) 
    VALUES (%s, %s);
'''

query_4 = '''
    DELETE FROM Ratings;
'''
query_5 = '''
    DELETE FROM MoviesAndShows;
'''
query_6 = '''
    DELETE FROM Weeks;
'''
query_7 = '''
    DELETE FROM Countries;
'''

queries = (query_4, query_5, query_6, query_7)

conn = None
cur = None

try:
    conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
    conn.autocommit = False  # Встановлюємо ручний режим фіксації транзакції
    cur = conn.cursor()

    for delete_query in queries:
        cur.execute(delete_query)

    for file, query in zip(files, (query_1, query_2, query_3)):
        try:
            with open(file, 'r') as f:
                reader = csv.DictReader(f)
                columns = [col.lower() for col in reader.fieldnames]
                values = [tuple(row[col] for col in columns) for row in reader]
                for data_values in values:
                    cur.execute(query, data_values)

            conn.commit()  # Фіксація транзакції для кожного файлу

        except Exception as e:
            conn.rollback()  # Відміна транзакції у випадку помилки
            print(f"Помилка при обробці файлу {file}: {e}")

    print("Імпорт даних успішно завершено.")

except Exception as e:
    print(f"Помилка: {e}")

finally:
    if cur:
        cur.close()
    if conn:
        conn.close()
