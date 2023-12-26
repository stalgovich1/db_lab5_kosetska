import csv
import psycopg2

try:
    # Підключення до PostgreSQL бази даних
    conn = psycopg2.connect(
        user='postgres',
        password='postgres',
        dbname='db_lab3',
        host='localhost',
        port='5432'
    )
    cursor = conn.cursor()

    # Функція для експорту даних з таблиці у CSV-файл
    def export_to_csv(table_name, csv_filename):
        query = f"COPY (SELECT * FROM {table_name}) TO STDOUT WITH CSV HEADER"
        with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
            cursor.copy_expert(sql=query, file=csv_file)

        print(f'Data from {table_name} exported to {csv_filename}.')

    # Експорт даних з кожної таблиці
    export_to_csv('MoviesAndShows', 'MoviesAndShows.csv')
    export_to_csv('Weeks', 'Weeks.csv')
    export_to_csv('Countries', 'Countries.csv')
    export_to_csv('Ratings', 'Ratings.csv')
    export_to_csv('most_popular', 'most_popular.csv')

except psycopg2.OperationalError as e:
    print(f"Unable to connect to the database. Error: {e}")

finally:
    # Закриття підключення до PostgreSQL бази даних
    if 'conn' in locals() and conn is not None:
        conn.close()
