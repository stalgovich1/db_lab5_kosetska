import csv
import psycopg2

try:
    # Підключення до PostgreSQL бази даних
    with psycopg2.connect(
        user='postgres',
        password='postgres',
        dbname='lab_3_6',
        host='localhost',
        port='5432'
    ) as conn:
        with conn.cursor() as cursor:
            # Функція для експорту даних з таблиці у CSV-файл
            def export_to_csv(table_name, csv_filename):
                query = f"COPY (SELECT * FROM {table_name}) TO STDOUT WITH CSV HEADER"
                try:
                    with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
                        cursor.copy_expert(sql=query, file=csv_file)
                    print(f'Data from {table_name} exported to {csv_filename}.')
                except psycopg2.Error as e:
                    print(f"Error exporting data from {table_name} to {csv_filename}: {e}")

            # Експорт даних з кожної таблиці
            export_to_csv('MoviesAndShows', 'MoviesAndShows.csv')
            export_to_csv('Weeks', 'Weeks.csv')
            export_to_csv('Countries', 'Countries.csv')
            export_to_csv('Ratings', 'Ratings.csv')

except psycopg2.OperationalError as e:
    print(f"Unable to connect to the database. Error: {e}")
