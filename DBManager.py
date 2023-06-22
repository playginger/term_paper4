import psycopg2


class DBManager:
    def __init__(self):
        self.conn = psycopg2.connect(database='postgres',
                                     user='postgres',
                                     password='135790eeg',
                                     host='localhost',
                                     port=5432)
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def get_companies_and_vacancies_count(self):
        sql = "SELECT employer_id, COUNT(*) FROM vacancies GROUP BY 1"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_all_vacancies(self):
        sql = "SELECT * FROM vacancies"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_avg_salary(self):
        sql = "SELECT AVG(salary) FROM vacancies"
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def get_vacancies_with_higher_salary(self):
        avg_salary = self.get_avg_salary()[0]
        sql = f"SELECT * FROM vacancies WHERE salary > {avg_salary}"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_vacancies_with_keyword(self, keyword):
        sql = f"SELECT * FROM vacancies WHERE description LIKE '%{keyword}%'"
        self.cursor.execute(sql)
        return self.cursor.fetchall()
