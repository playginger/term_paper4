from pprint import pprint

import psycopg2
import requests


def load_vac():
    conn = psycopg2.connect(database='postgres',
                            user='postgres',
                            password='135790eeg',
                            host='localhost',
                            port=5432)

    for employer_id in ["2519536", "788921", "72977", "69233", "2657797", "4181", "5158506", "1103383", "840485",
                        "5676844"]:  # ID всех выбранных компаний
        url = f"https://api.hh.ru/vacancies?employer_id={employer_id}&per_page=100"
        response = requests.get(url)
        data = response.json()
        cursor = conn.cursor()
        cursor.execute(f"""INSERT INTO public.employers(id)VALUES ('{employer_id}');""")

        for item in data["items"]:
            title = item

            pprint(item)

            if item.get('salary', {}) and item.get('salary', {}).get('from', 0) != None:
                salary = item.get('salary', {}).get('from', 0)
            else:
                salary = 0

            if item['address'] and item['address'].get('raw') :
                address = item['address'].get('raw')
            else:
                address = 'net'
            cursor = conn.cursor()
            cursor.execute(
                f'''INSERT INTO public.vacancies(id, employer_id, title, description, location, salary) VALUES ('{item['id']}', '{employer_id}', '{item['name']}', '{item['snippet']['requirement']}', '{address}', '{salary}');''')
    conn.commit()
    conn.close()


load_vac()
