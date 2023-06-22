import psycopg2

# Подключение к БД
conn = psycopg2.connect(database='postgres',
                        user='postgres',
                        password='135790eeg',
                        host='localhost',
                        port=5432)
cursor = conn.cursor()

# Создание таблицы employers
cursor.execute('''CREATE TABLE employers
                  (id serial PRIMARY KEY);''')

# Создание таблицы vacancies
cursor.execute('''CREATE TABLE vacancies
                  (id serial PRIMARY KEY,
                   employer_id integer NOT NULL,
                   title varchar(255) NOT NULL,
                   description text,
                   location varchar(255),
                   salary numeric(10,2));''')

# Закрываем соединение с БД
conn.commit()
conn.close()
