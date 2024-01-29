import MySQLdb
db_1 = MySQLdb.connect('localhost', 'val87', '12345', 'nursery')
cursor_1 = db_1.cursor()

def open_db():
    db = MySQLdb.connect('localhost', 'val87', '12345', 'nursery')
    cursor = db.cursor()
    return(db, cursor)

def close_db(base, cursor_each):
    cursor_each.close()
    base.close()



def count_animals():
    '''возвращает количество животных, которые есть в питомнике'''
    db, cursor = open_db()
    query = '''SELECT COUNT(*) FROM nursery'''
    cursor.execute(query)
    count_rows = cursor.fetchone()
    print(count_rows)
    close_db(db, cursor)
    return count_rows[0]


def create_skills_from_db(id_pets):
    '''позволяет вернуть из строки базы данных тип питомца и его умения'''
    db_1, cursor_1 = open_db()
    query = '''SELECT skills, type FROM nursery WHERE id_animal = %s;'''
    try:
        cursor_1.execute(query,(id_pets,))
        data = cursor_1.fetchall()
        print(data)
        return data
    except Exception:
        print('Ошибка извлечения данных...')
    finally:
        close_db(db_1, cursor_1)

def add_to_db_skill(name_skill, last_skill, id_pets):
    '''добавляет новое умение питомцу к уже существующим'''
    db_1, cursor_1 = open_db()
    result_skill = last_skill + "," + name_skill
    query = '''UPDATE nursery SET skills = %s WHERE id_animal = %s;'''
    try:
        cursor_1.execute(query,(result_skill, id_pets))
        db_1.commit()
    except Exception:
        print('Ошибка добавления умений для питомца...')
        db_1.rollback()
    finally:
        close_db(db_1, cursor_1)

def create_all_animals():
    '''получает массив кортежей из таблицы'''
    db_1, cursor_1 = open_db()
    query = '''SELECT * FROM nursery;'''
    try:
        cursor_1.execute(query)
        data = cursor_1.fetchall()
        return data
    except Exception:
        print('Ошибка чтения данных из таблицы...')
    finally:
        close_db(db_1, cursor_1)


def add_to_db_animal(name, age, skills, type):
    '''добавляет нового питомца в базу данных nursery'''
    db_1, cursor_1 = open_db()
    query = '''INSERT INTO nursery(name, age, skills, type) VALUES (%s, %s, %s, %s);'''
    try:
        cursor_1.execute(query,(name, age, skills, type))
        db_1.commit()
    except Exception:
        print('Ошибка добавления питомца в базу данных...')
        db_1.rollback()
    finally:
        close_db(db_1, cursor_1)

if __name__ == '__main__':
    a = (2, 3, 4)
    print(list(a))