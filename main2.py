import psycopg2
import numpy as np
import matplotlib.pyplot as plt


connection_params = {
    'user': 'postgres',
    'password': 'postgres',
    'dbname': 'db_lab4',
    'host': 'localhost',
    'port': '5432'
}

try:
    # Встановлення з'єднання з базою даних
    conn = psycopg2.connect(**connection_params)
    with conn.cursor() as cur:
        # Створення VIEWs
        cur.execute(create_view_1)
        cur.execute(create_view_2)
        cur.execute(create_view_3)

        # Отримання даних з VIEWs
        cur.execute(query_1)
        years_1, durations_1 = zip(*cur.fetchall())

        cur.execute(query_2)
        countries, total_viewership = zip(*cur.fetchall())

        cur.execute(query_3)
        types, avg_durations = zip(*cur.fetchall())

    # Побудова візуалізацій
    fig, ax = plt.subplots(1, 3, figsize=(15, 5))

    # Графік 1
    ax[0].bar(years_1, durations_1, color='g', edgecolor='y')
    ax[0].set_title('Середня тривалість фільмів/шоу за роками')
    ax[0].set_xlabel('Рік')
    ax[0].set_ylabel('Середня тривалість')

    # Графік 2
    ax[1].pie(total_viewership, labels=countries, autopct='%1.1f%%', wedgeprops={'edgecolor': 'y'})
    ax[1].set_title('Загальна кількість переглядів за країною')

    # Графік 3
    ax[2].scatter(types, avg_durations, color='g')
    ax[2].set_title('Середня тривалість фільмів/шоу за типом')
    ax[2].set_xlabel('Тип')
    ax[2].set_ylabel('Середня тривалість')

    plt.show()

except psycopg2.Error as e:
    print("Помилка підключення до бази даних:", e)
finally:
    # Закриття з'єднання з базою даних
    if 'conn' in locals() and conn:
        conn.close()
