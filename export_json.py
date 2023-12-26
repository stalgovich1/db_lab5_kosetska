import json
import psycopg2
from psycopg2.extras import RealDictCursor

try:
    # Підключення до PostgreSQL бази даних
    conn = psycopg2.connect(
        user='postgres',
        password='postgres',
        dbname='db_lab3',
        host='localhost',
        port='5432'
    )
    cursor = conn.cursor(cursor_factory=RealDictCursor)

    # Функція для експорту даних з таблиці у JSON-файл
    def export_to_json(table_name, json_filename):
        query = f"SELECT * FROM {table_name};"
        cursor.execute(query)
        rows = cursor.fetchall()

        with open(json_filename, 'w', encoding='utf-8') as json_file:
            json.dump(rows, json_file, ensure_ascii=False, indent=2)

        print(f'Data from {table_name} exported to {json_filename}.')

    # Експорт даних з кожної таблиці
    export_to_json('MoviesAndShows', 'MoviesAndShows.json')
    export_to_json('Weeks', 'Weeks.json')
    export_to_json('Countries', 'Countries.json')
    export_to_json('Ratings', 'Ratings.json')
    export_to_json('most_popular', 'most_popular.json')

except psycopg2.OperationalError as e:
    print(f"Unable to connect to the database. Error: {e}")

finally:
    # Закриття підключення до PostgreSQL бази даних
    if 'conn' in locals() and conn is not None:
        conn.close()
