import psycpg2
import csv

# Ваші дані для підключення
username = ''
password = ''
database = ''
host = 'localhost'
port = '5432'

CSV_MOVIES_FILE = 'Movies.csv'
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
    DELETE FROM MoviesAndShows;
'''
query_5 = '''
    DELETE FROM Weeks;
'''
query_6 = '''
    DELETE FROM Countries;
'''

queries = (query_1, query_2, query_3)

try:
    conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
    with conn:
        cur = conn.cursor()

        for delete_query in (query_4, query_5, query_6):
            cur.execute(delete_query)

        for file, query in zip(files, queries):
            with open(file, 'r') as f:
                reader = csv.DictReader(f)

                columns = [col.lower() for col in reader.fieldnames]
                values = [tuple(row[col] for col in columns) for row in reader]

                for data_values in values:
                    cur.execute(query, data_values)

        conn.commit()
        print("Імпорт даних успішно завершено.")

except Exception as e:
    print(f"Помилка: {e}")
finally:
    cur.close()
    conn.close()
